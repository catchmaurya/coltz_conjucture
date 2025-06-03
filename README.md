# 🧮 A Structured Approach to the Collatz Conjecture

This repository presents a mathematical and computational framework aimed at exploring and potentially reducing the scope of the Collatz Conjecture using algebraic modeling, dynamic programming, and reverse-path analysis.

---

## 📘 Abstract

The Collatz Conjecture posits that for any positive integer `n`, repeated application of the rule:

T(n) = n / 2 if n is even
T(n) = 3n + 1 if n is odd


will eventually reach the value 1. Despite its simplicity, no general proof exists.

In this work, we:
- Represent Collatz transformations algebraically
- Use backward path construction (`T⁻¹(n)`) to analyze convergence
- Implement dynamic programming to prove the conjecture over bounded domains
- Propose a recursive block-reduction model to generalize toward infinity

---

## 🧠 Key Concepts

- **Symbolic Equation Tracking**: Rewriting full paths using algebraic chains.
- **Reverse Tree Modeling**: Constructing `T⁻¹(n)` as a tree rooted at 1.
- **Memoization**: Caching known paths to avoid recomputation.
- **Recursive Proof Strategy**: Showing that if `[1, N]` is proven, ranges like `[N+1, 3N+1]` follow naturally.

---

## 📂 Repository Contents

| File | Description |
|------|-------------|
| `collatz_conjecture.tex` | Full LaTeX manuscript |
| `collatz_conjecture.pdf` | Compiled paper |
| `collatz_code.py` | Python script to compute and memoize Collatz paths |
| `example_output.csv` | Steps and paths for numbers 1 to 100 |
| `README.md` | This file |

---

## 🖥 Sample Result (from code)

```plaintext
Number: 27  
Steps: 112  
Path: [27, 82, 41, 124, 62, 31, ..., 1]
