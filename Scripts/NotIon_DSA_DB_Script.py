#!/usr/bin/env python3
"""
NotIon_DSA_DB_Script.py

All-in-one script that combines:
- Crawler (from crawl_github_dsa_a2z.py): Lists repo files at a fixed commit, extracts problem links, infers topic/subtopic/difficulty, and generates new + merged CSVs.
- Filter (from filter_keep_only_py_solutions.py): Keeps only rows whose Solution is a GitHub link ending in .py.

Default locations (relative to this script):
  Workspace root             = parent of this file's folder
  Seed/Existing CSV (input)  = Notion_DSA_Data_Backup.csv (can be overridden with --seed-csv)
  Outputs folder             = scripts_output/
  New-only CSV               = scripts_output/new_only_Notion_DSA_Data.csv
  Final merged CSV           = scripts_output/final_merged_Notion_DSA_Data.csv

Typical usage:
  # Crawl + merge using Notion_DSA_Data_Backup.csv, then filter to only .py solutions
  python Scripts/NotIon_DSA_DB_Script.py

  # Use a custom seed CSV (e.g., an updated CSV you exported)
  python Scripts/NotIon_DSA_DB_Script.py --seed-csv "c:/Users/you/Downloads/updated_final_merged_Notion_DSA_Data.csv"

  # Skip crawling and just filter an already prepared final CSV
  python Scripts/NotIon_DSA_DB_Script.py --skip-crawl --final-csv scripts_output/final_merged_Notion_DSA_Data.csv

Notes:
- This script performs network calls to GitHub (ZIP download) and optionally to LeetCode's public problems API for difficulty mapping.
- After writing the final merged CSV, it filters in-place to keep only GitHub .py Solution links (a backup is created with suffix .filter.backup.csv).
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import zipfile
from typing import Dict, List, Set, Tuple


# ----------------------
# Config / Defaults
# ----------------------
REPO_OWNER = "AshishSalaskar1"
REPO_NAME = "DS_Algo_Playground"
COMMIT_SHA_DEFAULT = "5d94dda81894f4b8787b59823fc086daaee90a58"

WORKSPACE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
OUTPUT_DIR = os.path.join(WORKSPACE_ROOT, "scripts_output")
DEFAULT_EXISTING_CSV = os.path.join(WORKSPACE_ROOT, "Notion_DSA_Data_Backup.csv")
DEFAULT_NEW_ONLY_CSV = os.path.join(OUTPUT_DIR, "new_only_Notion_DSA_Data.csv")
DEFAULT_FINAL_MERGED_CSV = os.path.join(OUTPUT_DIR, "final_merged_Notion_DSA_Data.csv")

LEETCODE_API = "https://leetcode.com/api/problems/algorithms/"
A2Z_PREFIX = "Track/DSA_A_to_Z/"
MASTER_BLOB_BASE = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/blob/master/"


# ----------------------
# HTTP helpers
# ----------------------

def http_get(url: str, retries: int = 3, timeout: int = 25) -> str:
    last_err = None
    headers = {"User-Agent": "Mozilla/5.0 (crawler)"}
    for _ in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except Exception as e:  # noqa: BLE001
            last_err = e
            time.sleep(1)
    raise RuntimeError(f"Failed to fetch {url}: {last_err}")


def http_get_bytes(url: str, retries: int = 3, timeout: int = 60) -> bytes:
    last_err = None
    headers = {"User-Agent": "Mozilla/5.0 (crawler)"}
    for _ in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except Exception as e:  # noqa: BLE001
            last_err = e
            time.sleep(1)
    raise RuntimeError(f"Failed to fetch bytes {url}: {last_err}")


# ----------------------
# Repo/ZIP processing
# ----------------------

def list_files_from_zip(zip_url: str) -> Tuple[str, List[Tuple[str, bytes]]]:
    """Download the repo at COMMIT_SHA as a ZIP and list files under A2Z_PREFIX.

    Returns: (root_dir_name, [(relative_path_under_A2Z, content_bytes), ...])
    """
    zip_bytes = http_get_bytes(zip_url, timeout=60)
    zf = zipfile.ZipFile(io.BytesIO(zip_bytes))
    names = zf.namelist()
    if not names:
        raise RuntimeError("Empty ZIP archive from GitHub")
    root = names[0].split("/")[0]  # e.g., DS_Algo_Playground-<sha>
    prefix = f"{root}/{A2Z_PREFIX}"

    files: List[Tuple[str, bytes]] = []
    for name in names:
        if not name.startswith(prefix):
            continue
        if name.endswith("/"):
            continue
        rel = name[len(prefix):]
        ext = os.path.splitext(rel)[1].lower()
        if ext not in {".py", ".md", ".txt"}:
            continue
        with zf.open(name) as f:
            content = f.read()
        files.append((rel, content))
    return root, files


PROBLEM_URL_PATTERNS = [
    r'https?://leetcode\.com/[^\)\s"<>]+',
    r'https?://takeuforward\.org/[^\)\s"<>]+' ,
    r'https?://www\.geeksforgeeks\.org/[^\)\s"<>]+',
    r'https?://geeksforgeeks\.org/[^\)\s"<>]+',
    r'https?://codeforces\.com/[^\)\s"<>]+',
    r'https?://atcoder\.jp/[^\)\s"<>]+',
    r'https?://cses\.fi/[^\)\s"<>]+' ,
]


def extract_problem_links(text: str) -> List[str]:
    found: List[str] = []
    for pat in PROBLEM_URL_PATTERNS:
        found.extend(re.findall(pat, text, flags=re.IGNORECASE))
    # Clean & stable order
    cleaned: List[str] = []
    seen: Set[str] = set()
    for url in found:
        url = url.strip().rstrip(".),]")
        if url not in seen:
            seen.add(url)
            cleaned.append(url)

    def key(u: str) -> Tuple[int, int, str]:
        # Prioritize leetcode > takeuforward > rest
        return (
            0 if "leetcode.com" in u else 1,
            0 if "takeuforward.org" in u else 1,
            u,
        )

    cleaned.sort(key=key)
    return cleaned


def extract_leetcode_slug(url: str) -> str:
    """Return the problem slug from a LeetCode URL ('' if not applicable)."""
    try:
        if "leetcode.com" not in url:
            return ""
        u = urllib.parse.urlparse(url)
        parts = u.path.strip("/").split("/")
        if len(parts) >= 2 and parts[0] == "problems":
            return parts[1]
    except Exception:
        return ""
    return ""


def get_leetcode_difficulty_map() -> Dict[str, str]:
    """Fetch LeetCode problems and build slug->difficulty mapping (Easy/Medium/Hard)."""
    mapping: Dict[str, str] = {}
    try:
        body = http_get(LEETCODE_API, timeout=40)
        data = json.loads(body)
        stat_status_pairs = data.get("stat_status_pairs", [])
        for item in stat_status_pairs:
            stat = item.get("stat", {})
            meta = item.get("difficulty", {})
            slug = stat.get("question__title_slug", "")
            level = meta.get("level", 0)
            if not slug:
                continue
            diff = ""
            if level == 1:
                diff = "Easy"
            elif level == 2:
                diff = "Medium"
            elif level == 3:
                diff = "Hard"
            if diff:
                mapping[slug] = diff
    except Exception:
        return {}
    return mapping


def infer_topic_subtopic(rel_path: str) -> Tuple[str, str]:
    parts = rel_path.split("/")
    if len(parts) < 2:
        return (parts[0] if parts else "", "")
    topic = parts[0]
    sub_parts = parts[1:-1]
    subtopic = "/".join(sub_parts) if sub_parts else ""
    return topic, subtopic


def infer_difficulty(text: str, rel_path: str) -> str:
    blob = f"{text}\n{rel_path}"
    if re.search(r"\bHard\b", blob, re.IGNORECASE):
        return "Hard"
    if re.search(r"\bMedium\b", blob, re.IGNORECASE):
        return "Medium"
    if re.search(r"\bEasy\b", blob, re.IGNORECASE):
        return "Easy"
    return ""


def load_existing(csv_path: str) -> Tuple[List[Dict[str, str]], Set[str], Set[str]]:
    rows: List[Dict[str, str]] = []
    problems: Set[str] = set()
    solutions: Set[str] = set()
    if not os.path.exists(csv_path):
        return rows, problems, solutions
    # utf-8-sig to handle BOM in header if any
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for r in reader:
            status = (r.get("Status") or r.get("\ufeffStatus") or "").strip()
            problem_link = (r.get("Problem ") or r.get("Problem") or "").strip()
            solution_link = (r.get("Solution") or "").strip()
            topic = (r.get("Topic") or "").strip()
            sub_topic = (r.get("Sub Topic") or r.get("Sub Topic ") or r.get("Subtopic") or "").strip()
            difficulty = (r.get("Difficulty") or "").strip()
            remarks = (r.get("Remarks") or "").strip()
            link = (r.get("Link") or "").strip()

            std = {
                "Status": status or "Yes",
                "Problem ": problem_link,
                "Solution": solution_link,
                "Topic": topic,
                "Sub Topic": sub_topic,
                "Difficulty": difficulty,
                "Remarks": remarks,
                "Link": link,
            }
            rows.append(std)
            if problem_link:
                problems.add(problem_link)
            if solution_link:
                solutions.add(solution_link)
    return rows, problems, solutions


def make_master_blob_link(rel_path: str) -> str:
    encoded = "/".join(urllib.parse.quote(p) for p in rel_path.split("/"))
    return MASTER_BLOB_BASE + A2Z_PREFIX + encoded if not rel_path.startswith("Track/") else MASTER_BLOB_BASE + encoded


# ----------------------
# Filter helpers
# ----------------------

def is_github_py(url: str) -> bool:
    if not url:
        return False
    url = url.strip()
    if not (url.startswith("http://") or url.startswith("https://")):
        return False
    try:
        p = urllib.parse.urlparse(url)
    except Exception:
        return False
    host = (p.netloc or "").lower()
    if "github.com" not in host:
        return False
    path = (p.path or "").rstrip("/")
    return path.lower().endswith(".py")


def filter_csv_only_py(csv_path: str) -> Tuple[int, int, str]:
    """Filter the given CSV in-place to keep only rows whose Solution is a GitHub .py.
    Returns: (kept, total, backup_path)
    """
    backup_path = csv_path.replace(".csv", ".filter.backup.csv")
    if not os.path.exists(backup_path):
        with open(csv_path, "rb") as src, open(backup_path, "wb") as dst:
            dst.write(src.read())

    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows_in = list(reader)

    kept = [r for r in rows_in if is_github_py((r.get("Solution") or ""))]

    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(kept)

    return len(kept), len(rows_in), backup_path


# ----------------------
# Pipeline
# ----------------------

def crawl_and_merge(
    seed_csv: str,
    final_csv: str,
    new_only_csv: str,
    commit_sha: str,
) -> Tuple[int, int]:
    """Crawl the repo at commit, merge with seed_csv, and write final_csv and new_only_csv.
    Returns: (num_new_rows, num_merged_rows)
    """
    os.makedirs(os.path.dirname(final_csv), exist_ok=True)

    zip_url = f"https://codeload.github.com/{REPO_OWNER}/{REPO_NAME}/zip/{commit_sha}"
    print(f"Downloading repo ZIP once to list and read files: {zip_url}")
    root_name, files = list_files_from_zip(zip_url)
    print(f"Total candidate files: {len(files)}")

    existing_rows, existing_problem_links, existing_solution_links = load_existing(seed_csv)
    print(
        f"Existing rows: {len(existing_rows)}; Problems: {len(existing_problem_links)}; Solutions: {len(existing_solution_links)}"
    )

    lc_diff_map = get_leetcode_difficulty_map()

    # Improve difficulty for existing rows (if empty and Problem is a LeetCode link)
    improved_existing: List[Dict[str, str]] = []
    for r in existing_rows:
        difficulty = (r.get("Difficulty") or "").strip()
        prob = (r.get("Problem ") or r.get("Problem") or "").strip()
        if (not difficulty) and prob:
            slug = extract_leetcode_slug(prob)
            if slug and slug in lc_diff_map:
                r["Difficulty"] = lc_diff_map[slug]
        improved_existing.append(r)

    new_rows: List[Dict[str, str]] = []
    for rel, content in files:
        try:
            text = content.decode("utf-8", errors="replace")
        except Exception:
            text = ""

        links = extract_problem_links(text)
        problem_link = links[0] if links else ""
        solution_link = make_master_blob_link(rel)

        # Dedup vs existing
        if problem_link and problem_link in existing_problem_links:
            continue
        if solution_link in existing_solution_links:
            continue

        topic, subtopic = infer_topic_subtopic(rel)
        difficulty = ""
        if problem_link:
            slug = extract_leetcode_slug(problem_link)
            if slug and slug in lc_diff_map:
                difficulty = lc_diff_map[slug]
        if not difficulty:
            difficulty = infer_difficulty(text, rel)

        new_rows.append(
            {
                "Status": "Yes",
                "Problem ": problem_link,
                "Solution": solution_link,
                "Topic": topic.replace("_", " "),
                "Sub Topic": subtopic.replace("_", " "),
                "Difficulty": difficulty,
                "Remarks": "",
                "Link": "",
            }
        )

    fieldnames = [
        "Status",
        "Problem ",
        "Solution",
        "Topic",
        "Sub Topic",
        "Difficulty",
        "Remarks",
        "Link",
    ]

    with open(new_only_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_rows)

    # Merge existing + new
    merged: List[Dict[str, str]] = []
    merged_solution_set: Set[str] = set()
    merged_problem_set: Set[str] = set()

    for r in improved_existing:
        merged.append(r)
        sol = (r.get("Solution") or "").strip()
        prob = (r.get("Problem ") or r.get("Problem") or "").strip()
        if sol:
            merged_solution_set.add(sol)
        if prob:
            merged_problem_set.add(prob)

    for r in new_rows:
        sol = r.get("Solution", "").strip()
        prob = r.get("Problem ", "").strip()
        if sol and sol in merged_solution_set:
            continue
        if prob and prob in merged_problem_set:
            continue
        merged.append(r)
        if sol:
            merged_solution_set.add(sol)
        if prob:
            merged_problem_set.add(prob)

    with open(final_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(merged)

    print(f"New rows: {len(new_rows)} -> {new_only_csv}")
    print(f"Final merged rows: {len(merged)} -> {final_csv}")
    return len(new_rows), len(merged)


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Crawl, merge, and filter Notion DSA CSV data in one script.")
    parser.add_argument("--seed-csv", default=DEFAULT_EXISTING_CSV, help="Seed/existing CSV to merge with (can be your updated CSV)")
    parser.add_argument("--final-csv", default=DEFAULT_FINAL_MERGED_CSV, help="Path to write the final merged CSV")
    parser.add_argument("--new-only-csv", default=DEFAULT_NEW_ONLY_CSV, help="Path to write the new-only CSV")
    parser.add_argument("--commit-sha", default=COMMIT_SHA_DEFAULT, help="Git commit to crawl")
    parser.add_argument("--skip-crawl", action="store_true", help="Skip crawling; only filter the provided final CSV")
    parser.add_argument("--no-filter", action="store_true", help="Do not apply the .py-only filter after merge")

    args = parser.parse_args(argv)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if not args.skip_crawl:
        try:
            crawl_and_merge(
                seed_csv=args.seed_csv,
                final_csv=args.final_csv,
                new_only_csv=args.new_only_csv,
                commit_sha=args.commit_sha,
            )
        except Exception as e:  # noqa: BLE001
            print(f"ERROR during crawl/merge: {e}")
            return 1
    else:
        if not os.path.exists(args.final_csv):
            # If skipping crawl but final doesn't exist, try copying seed to final
            if os.path.exists(args.seed_csv):
                with open(args.seed_csv, "rb") as src, open(args.final_csv, "wb") as dst:
                    dst.write(src.read())
                print(f"Skip-crawl: copied seed CSV -> {args.final_csv}")
            else:
                print("Skip-crawl requested, but neither final CSV nor seed CSV exist.")
                return 1

    if not args.no_filter:
        try:
            kept, total, backup = filter_csv_only_py(args.final_csv)
            print(f"Filtered rows: kept {kept} of {total}. Backup at {os.path.basename(backup)}")
        except Exception as e:  # noqa: BLE001
            print(f"ERROR during filtering: {e}")
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
