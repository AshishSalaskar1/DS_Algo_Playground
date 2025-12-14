### What is this Counting DP??
> In some problems you are asked to count number of ways

❎ You think its a Pick/Nopick DP or Branching Type <br>
✅ Its a counting DP 

Most of times you can solve it by <br>
1. Some smarter logic + Combinatronics
    - Example: [Num Ways to divide corridor](https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor)
2. In the DP function you iterate the next subset types

---
# 🧠 How to Decide: Recursive / Choice DP vs Combinatorics-on-Gaps

This guide helps build intuition for **when to use DP** and **when NOT to**, using reasoning instead of memorization.

---

## 🔁 Recursive / Choice DP

Use this when:

> You actively make **choices**, and those choices **change future possibilities**.

### 🚩 Strong signals
- “At position `i`, I can either do A or B”
- Choices affect later choices
- Order matters
- State depends on earlier decisions

### 📌 Typical examples
- House Robber
- Knapsack
- Decode Ways
- Stock Buy/Sell
- Grid paths with obstacles

---

## 🧮 Combinatorics-on-Gaps

Use this when:

> Choices come from **spacing between fixed constraints**, and each choice is **independent**.

### 🚩 Strong signals
- Placing dividers or separators
- Fixed elements + flexible elements
- Flexible elements only create **positions**
- Final answer is a **product of independent choices**

### 📌 Typical examples
- Corridor / divider problems
- Splitting by special elements
- Arrangements with fixed anchors
- Grouping with exact constraints

---

## ❓ The Litmus Test (MOST IMPORTANT)

Ask yourself:

> **If I make a choice now, does it affect what choices I can make later?**

- ✅ YES → 🔁 Recursive / Choice DP  
- ❌ NO → 🧮 Combinatorics (count & multiply)

---

## 🪑 Applying the Test to the Corridor Problem

### Fixed constraints
- Seats (`S`) → cannot move, cannot skip

### Flexible elements
- Plants (`P`) → only create space

### Key question
Does choosing a divider in one gap affect choices in another gap?

👉 **No. Each gap is independent.**

### 🔑 Conclusion
- Independent choices → ✖️ MULTIPLY  
- Dependent choices → ➕ DP / ADD  

---

## ⚠️ Why Recursive DP Feels Natural (But Is Wrong Here)

Natural thought:

> “At each position, I can place a divider or not.”

### ❌ Why this fails
- Dividers are not free choices
- Seats force the structure
- Plants do **not** branch futures — they only increase valid positions

The recursion invents choices that don’t actually exist.

---

## 👀 Visual Rule

### 🔴 DP-style problems
i → choice A → different future
i → choice B → different future


### 🟢 Gap-combinatorics problems
[S S] --- gap1 --- [S S] --- gap2 --- [S S]

gap1 = x + 1 ways
gap2 = y + 1 ways

Answer = (x + 1) × (y + 1)

No branching. No recursion.

---

## 🗝️ Keyword Heuristic

If the problem mentions:
- divide
- split
- between
- groups
- exactly k per group

🛑 Pause DP.  
🧠 Think in **blocks + gaps**.

---

## 🔄 When DP WOULD Be Needed

DP makes sense if:
- Elements can move
- Group sizes are flexible
- Dividers change future possibilities
- Constraints depend on earlier placements

If none apply → DP is likely overkill.

---

## 🏋️ How to Train This Intuition

1. 🧪 Try greedy or counting first  
2. 🧩 Compress the problem into **fixed elements + gaps**  
3. 🧠 Use DP only if choices affect future options  

---

## 🧩 One-Line Rule to Remember

**Choices about WHERE → 🧮 Combinatorics**  
**Choices about WHAT TO DO → 🔁 DP**

---

## 🎯 Final Takeaway

If flexible elements only create **space** and not **decisions**:

🛑 Stop recursion  
🔢 Count positions  
✖️ Multiply  

That’s the key insight.
