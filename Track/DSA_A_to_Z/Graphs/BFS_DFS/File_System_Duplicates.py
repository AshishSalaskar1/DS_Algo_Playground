"""

https://leetcode.com/problems/find-duplicate-file-in-system/


INPUT
"root/a 1.txt(abcd) 2.txt(efgh)",
"root/c 3.txt(abcd)",
"root/c/d 4.txt(efgh)",
"root 4.txt(efgh)"

OUTPUT
["root/a/2.txt","root/c/d/4.txt","root/4.txt"],
["root/a/1.txt","root/c/3.txt"]]


BASE QUESTION: Find duplicate files in the system based on their content.

FOLLOW UPS
1. Imagine you are given a real file system, how will you search files? 
-> BFS is better for HDD since we explore neighboring files first
-> DFS is better for SSD since we can explore deeper files first and SSD has faster access time
-> BFS is easy to parallize. In DFS you need to keep the recursion stack which can be memory intensive if the file system is very deep. In BFS, you can use a queue to keep track of the files to explore, which can be more memory efficient.

2. If the file content is very large (GB level), how will you modify your solution?
-> Do metadata check first, such as file size, last modified time, etc. to filter out files that are unlikely to be duplicates. This can significantly reduce the number of files that need to be compared based on their content.
-> Using MD5 or SHA-1 hash functions to generate a hash for each file's content. This way, you can compare the hashes instead of the actual content, which is much faster and more memory efficient. 
-> Hashing can cause colllisions (FP) -> Use Byte-by-Byte comparison to confirm the duplicates. This can be done by reading the files in chunks (e.g., 1KB at a time) and comparing the chunks until a difference is found or the end of the file is reached.

3. If you can only read the file by 1kb each time, how will you modify your solution?
-> Use Byte-by-Byte comparison to confirm the duplicates. This can be done by reading the files in chunks (e.g., 1KB at a time) and comparing the chunks until a difference is found or the end of the file is reached.

4. What is the time complexity of your modified solution? What is the most time-consuming part and memory-consuming part of it? How to optimize?
-> 

5. How to make sure the duplicated files you find are not false positive?
-> Byte by Byte checks

"""


from typing import List
from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_content_map = defaultdict(list)
        for fpath in paths:
            fpath = fpath.split(" ")
            if len(fpath) == 1:
                continue

            dirs, filelist = fpath[0], fpath[1:]
            files = []
            for f in filelist:
                f = f.split("(")
                fname = f[0]
                fcontent = f[1][:-1]

                file_content_map[fcontent].append(f"{dirs}/{fname}")
        
        res = []
        for fcontent, files in file_content_map.items():
            if len(files) > 1:
                res.append(files)
        
        return res
            
            




        