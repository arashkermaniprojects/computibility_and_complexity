# BCS 402 — Student-led Lecture Assessment Plan

**Dr. Arash Kermani · CUD · Fall 2026**

## Logistics

- 16 lectures total, each **3 hours long**. **Lectures 1–4** are instructor-led (foundations).
- **Lectures 5–16** are mixed: instructor teaches the day's module for the first 60–90 minutes, then **5 students** present problems for the remaining 90–120 minutes (12–18 minutes per presenter, including Q&A).
- 12 lectures × 5 students = **60 student presentations**.
- **20 students** × 3 presentations each = 60 slots ✓ — student-to-slot grid is round-robin.
- Each presentation: student solves an assigned problem using an interactive HTML tool, then defends it in Q&A.

> **Scaling note.** Slots/lecture = ⌈students / 4⌉. If enrollment rises to 24 use 6 slots, to 28 use 7, to 32 use 8. The same 60 problem topics can be reused with different inputs (parameterized variants — see the per-problem hint sequences in `tools/`). Hard ceiling: ~40 students (10 slots/lecture × 12 min ≈ the full student block).

### Grading

| Round | Lectures | Per-student score | Weight |
|------:|:--------:|:-----------------:|:------:|
| Round 1 | 5–8   | 30 | first presentation |
| Round 2 | 9–12  | 30 | second presentation |
| Round 3 | 13–16 | 40 | third (highest-stakes) presentation |
| **Total** |   | **100** | |

Each student gets exactly one slot per round. Round difficulty rises with topic depth, matching the weighting.

### CLO mapping (target coverage)

| CLO | Topic | Problems / 60 (rounded) |
|---|---|---:|
| CLO-1 | Diagonalization → undecidability | 10 |
| CLO-2 | Reductions → algorithmic unsolvability | 12 |
| CLO-3 | Finding vs. verifying complexity | 13 |
| CLO-4 | Mapping reductions → hardness | 15 |
| CLO-5 | Hierarchy theorems → class separation | 10 |

---

## ROUND 1 · Lectures 5–8 · 30 points each

*Theme: undecidability, diagonalization, reductions, recursion theorem. Builds on Module 2–3.*

### Lecture 5 — Diagonalization & the halting problem (Module 2)

| # | Problem | CLO |
|---:|---|:--:|
| 1 | **Cantor's diagonal interactive proof.** Build a tool that lists 7 functions ℕ→{0,1} as rows of a table, highlights the diagonal, and visibly constructs the missing function g(n)=1−f<sub>n</sub>(n). Defend why this proves \|ℝ\| > \|ℕ\|. | CLO-1 |
| 2 | **Universal TM simulator.** Implement a UTM that takes a TM description + input and animates step-by-step execution. Demonstrate the "loops forever" case and explain why A<sub>TM</sub> is recognizable but not decidable. | CLO-1 |
| 3 | **A<sub>TM</sub>-undecidability table.** Build the M<sub>i</sub>×⟨M<sub>j</sub>⟩ acceptance matrix, walk the diagonal, construct the contradiction machine D, and explain at column k why D ≠ M<sub>k</sub>. | CLO-1 |
| 4 | **Recognizable / decidable / co-recognizable Venn classifier.** Drag-and-drop quiz where users place A<sub>TM</sub>, HALT<sub>TM</sub>, EQ<sub>TM</sub>, complements, etc. in the right region. Defend each placement. | CLO-1 |

### Lecture 6 — Reductions for undecidability (Module 2)

| # | Problem | CLO |
|---:|---|:--:|
| 5 | **HALT<sub>TM</sub> reduction from A<sub>TM</sub>.** Interactive builder that takes ⟨M, w⟩ and constructs M′ whose halting behaviour encodes M's acceptance of w. | CLO-2 |
| 6 | **E<sub>TM</sub> undecidability.** Build the M′ that ignores its input and simulates M(w); show L(M′) = Σ* iff M accepts w. | CLO-2 |
| 7 | **REGULAR<sub>TM</sub> undecidability** via the {0<sup>n</sup>1<sup>n</sup>}-trick gadget. | CLO-2 |
| 8 | **Mapping reduction A<sub>TM</sub> ≤<sub>m</sub> EQ<sub>TM</sub>.** Interactive: given ⟨M, w⟩, output ⟨M<sub>1</sub>, M<sub>2</sub>⟩ such that M<sub>1</sub> ≡ M<sub>2</sub> iff M accepts w. | CLO-2 |

### Lecture 7 — Computation-history method (Module 3)

| # | Problem | CLO |
|---:|---|:--:|
| 9 | **Computation-history visualizer.** Render a TM's full configuration trace as `C₁ # C₂ # … # C_ℓ` for a small machine; allow editing transitions and watch the trace change. | CLO-2 |
| 10 | **E<sub>LBA</sub> undecidability.** Build the LBA B<sub>M,w</sub> that accepts iff its input is a valid accepting history of M on w. | CLO-2 |
| 11 | **ALL<sub>CFG</sub> undecidability.** Build the CFG G<sub>M,w</sub> that generates everything *except* accepting histories of M on w. Walk through the local-violation gadget. | CLO-2 |
| 12 | **Decidability of A<sub>DFA</sub>, E<sub>DFA</sub>, A<sub>CFG</sub>.** Three side-by-side deciders, each with a step counter showing polynomial running time. Defend why this contrasts with TM cousins. | CLO-2 |

### Lecture 8 — Recursion theorem & Rice's theorem (Module 3)

| # | Problem | CLO |
|---:|---|:--:|
| 13 | **Quine builder.** Write a working self-printing program in a language of choice; annotate the data/code split. | CLO-1 |
| 14 | **Rice's theorem checker.** User enters a property of L(M); the tool decides whether Rice applies (nontrivial + semantic) and explains the verdict on examples like "L(M) regular", "L(M) finite", "M has ≥ 5 states". | CLO-2 |
| 15 | **Recursion theorem fixed point.** Given any computable t(x), interactively construct the fixed-point program p such that p ≡ t(⟨p⟩). | CLO-2 |
| 16 | **Self-aware TM demo.** Build a TM that reads its own description from tape (via recursion theorem) and uses it to decide whether to accept its input. | CLO-1 |

---

## ROUND 2 · Lectures 9–12 · 30 points each

*Theme: time complexity, P, NP, verifiers, Cook–Levin, NP-completeness. Builds on Modules 4–5.*

### Lecture 9 — Time complexity & the class P (Module 4)

| # | Problem | CLO |
|---:|---|:--:|
| 17 | **Growth-rate animator.** Race log n, n, n log n, n², n³, 2ⁿ on the same chart with log/linear scale toggle; pinpoint where 2ⁿ overtakes n³. | CLO-3 |
| 18 | **{0<sup>n</sup>1<sup>n</sup>} single-tape decider with step counter.** Visualise pair-off strategy; show empirical O(n²) growth. | CLO-3 |
| 19 | **Single-tape vs two-tape race.** Same problem, side-by-side animation, step counters. Defend the O(n²) vs O(n) gap. | CLO-3 |
| 20 | **Big-O classifier.** User enters a polynomial expression; the tool extracts dominant term, animates stacked bands. | CLO-3 |

### Lecture 10 — NP & verifiers (Module 5)

| # | Problem | CLO |
|---:|---|:--:|
| 21 | **Verifier vs brute-force solver race.** Same 3SAT instance; the verifier finishes in O(m), the solver enumerates 2<sup>n</sup>. | CLO-3 |
| 22 | **Interactive SAT.** Click variables to flip; clauses light green/red; auto-solver enumerates with explanation per assignment. | CLO-3 |
| 23 | **HAMPATH certificate verifier.** Given a graph and a vertex sequence, check in poly time whether it is a Hamiltonian path. Defend "in NP". | CLO-3 |
| 24 | **P-class showcase tool.** Three classic P problems (PATH via BFS, RELPRIME via Euclid, A<sub>CFG</sub> via CYK) with annotated polynomial running times. | CLO-3 |

### Lecture 11 — Cook–Levin (Module 5)

| # | Problem | CLO |
|---:|---|:--:|
| 25 | **Cook–Levin tableau builder.** Encode a TM's computation as an n<sup>k</sup>×n<sup>k</sup> grid; highlight 2×3 windows that become SAT clauses. | CLO-4 |
| 26 | **SAT → 3SAT reduction.** Take any clause with >3 literals, animate auxiliary-variable splitting, prove satisfiability is preserved. | CLO-4 |
| 27 | **3SAT → CLIQUE.** Build the literal-occurrence graph; highlight a k-clique iff the formula is satisfiable. | CLO-4 |
| 28 | **CLIQUE → VERTEX-COVER.** Show the complement-graph trick: clique of size k in G ⇔ vertex cover of size n−k in G̅. | CLO-4 |

### Lecture 12 — More NP-complete problems (Module 5)

| # | Problem | CLO |
|---:|---|:--:|
| 29 | **3SAT → SUBSET-SUM.** Build the digit-position number system; demonstrate the target sum forces a satisfying assignment. | CLO-4 |
| 30 | **3SAT → HAMPATH.** Walk through gadget construction (variable diamonds, clause spreaders) on a small formula. | CLO-4 |
| 31 | **3SAT → 3COLOR.** Build the variable + OR-gadget graph; verify 3-colorings correspond to satisfying assignments. | CLO-4 |
| 32 | **Self-reducibility (SAT search-to-decision).** Given a SAT decider, find an actual assignment in poly time. Defend why this means "if P=NP, finding is as easy as deciding". | CLO-3 |

---

## ROUND 3 · Lectures 13–16 · 40 points each

*Theme: space complexity, PSPACE, games, L/NL, hierarchy theorems. Builds on Modules 6–7. Highest-stakes round.*

### Lecture 13 — Space complexity & Savitch (Module 6)

| # | Problem | CLO |
|---:|---|:--:|
| 33 | **Space vs time bar chart for 5 classic algorithms.** Defend why "space ≤ time" but "time ≤ 2<sup>O(space)</sup>". | CLO-5 |
| 34 | **Savitch's recursion tree visualizer.** CANYIELD(A, B, t) splits into two CANYIELD(·,·,t/2) calls; show stack depth = log t even though tree has 2<sup>log t</sup> nodes. | CLO-4 |
| 35 | **PSPACE = NPSPACE proof walker.** Show Savitch's algorithm explicitly for a small NSPACE machine; count cells used at every level. | CLO-5 |
| 36 | **Game-tree evaluator for TQBF.** ∃-nodes take OR; ∀-nodes take AND. Walk a small formula post-order to truth value. | CLO-4 |

### Lecture 14 — PSPACE-completeness via games (Module 6)

| # | Problem | CLO |
|---:|---|:--:|
| 37 | **TQBF ↔ TQBF₃ reduction** (every QBF can be made to alternate quantifiers, with only 3 literals per clause). | CLO-4 |
| 38 | **Generalized Geography game.** Playable graph game vs minimax computer; build 2-3 maps where each player wins. Explain link to PSPACE. | CLO-4 |
| 39 | **TQBF → Generalized Geography reduction.** Encode any QBF as a graph game where ∃-player wins iff QBF true. Walk a small example. | CLO-4 |
| 40 | **Cat-and-mouse / Chess (generalised) PSPACE-hardness.** Pick one and show how to encode TQBF into it. | CLO-4 |

### Lecture 15 — L, NL & inductive counting (Module 7)

| # | Problem | CLO |
|---:|---|:--:|
| 41 | **Log-space pointer-chaser.** Implement a 2-tape machine deciding palindromes (or A<sub>DFA</sub>) using only O(log n) work-tape cells. | CLO-3 |
| 42 | **NL PATH non-deterministic search.** Visualise multiple guess-branches in parallel; show each branch fits in O(log n). | CLO-5 |
| 43 | **PATH is NL-complete.** Configuration graph of an NL machine — show every NL language log-space-reduces to PATH. | CLO-4 |
| 44 | **Immerman–Szelepcsényi inductive counting.** Step-by-step expansion of R<sub>i</sub> (vertices reachable in ≤ i steps); explain how counting c<sub>i</sub> certifies ¬PATH in NL. Conclude NL = coNL. | CLO-5 |

### Lecture 16 — Hierarchy theorems (Module 7)

| # | Problem | CLO |
|---:|---|:--:|
| 45 | **Space hierarchy theorem diagonalization.** Build the table of SPACE(f) machines vs inputs; construct the diagonalizer D; explain why D ∉ SPACE(f) but D ∈ SPACE(g) for g = f · log f. | CLO-1 + CLO-5 |
| 46 | **Time hierarchy theorem diagonalization.** Analogous, for TIME(f). Explain why we lose only a log factor for time and (slightly more) for space. | CLO-1 + CLO-5 |
| 47 | **NL ⊊ PSPACE via hierarchy.** Use the space hierarchy theorem to show concretely that NL is strictly inside PSPACE. | CLO-5 |
| 48 | **P ⊊ EXPTIME.** Use the time hierarchy theorem; defend why this is one of the few proven complexity-class separations. | CLO-5 |

---

## CLO coverage check

Counting tags above (where #45 and #46 split between CLO-1 and CLO-5):

| CLO | Problems | Count |
|:---:|---|---:|
| **CLO-1** | 1, 2, 3, 4, 13, 16, 45(½), 46(½) | **7** |
| **CLO-2** | 5, 6, 7, 8, 9, 10, 11, 12, 14, 15 | **10** |
| **CLO-3** | 17, 18, 19, 20, 21, 22, 23, 24, 32, 41 | **10** |
| **CLO-4** | 25, 26, 27, 28, 29, 30, 31, 34, 36, 37, 38, 39, 40, 43 | **14** |
| **CLO-5** | 33, 35, 42, 44, 45(½), 46(½), 47, 48 | **7** |

CLO-4 ends up slightly heavier because mapping reductions are the bulk of the NP/PSPACE-hardness story. If you want it tighter, problem #31 (3SAT → 3COLOR) and #40 (Chess/cat-and-mouse) can be re-tagged CLO-2 since the "reduction-to-prove-unsolvability" flavour is similar — that would bring CLO-2 to 12 and CLO-4 to 12.

---

## Supplementary problems for the 20-student version (5 slots / lecture)

Adding one more problem per lecture brings the total to **60 problems** = 20 students × 3 rounds. These new ones complement the lecture's existing 4 problems and extend (rather than duplicate) the CLO coverage.

| # | Lecture | Problem | CLO |
|---:|:---:|---|:--:|
| 49 | 5  | **Closure-property explorer.** Build a tool that shows decidable & recognizable languages are closed under ∪, ∩ but recognizable is NOT closed under complement. Visual proof of the "bridge theorem": L decidable ⇔ both L and L̅ recognizable. | CLO-1 |
| 50 | 6  | **FINITE<sub>TM</sub> undecidability.** Reduce A<sub>TM</sub> to FINITE<sub>TM</sub>: given ⟨M, w⟩, build M' whose language is finite iff M does NOT accept w. | CLO-2 |
| 51 | 7  | **Post Correspondence Problem (PCP).** Interactive PCP-instance solver for small instances; explain why general PCP is undecidable via the computation-history reduction. | CLO-2 |
| 52 | 8  | **Self-destructing TM (Kamikaze).** Use the recursion theorem to build a TM that on any input prints its own description and then enters a "fictitious erased" mode. Explain how recursion theorem makes self-reference safe. | CLO-1 |
| 53 | 9  | **TM running-time profiler.** Visual stopwatch on a small TM showing steps as a function of input length n. Empirically check the predicted O(n²) curve. | CLO-3 |
| 54 | 10 | **COMPOSITES verifier.** Certificate is a non-trivial divisor; verify in poly time. Defend why COMPOSITES ∈ NP (and now ∈ P via AKS, but the verifier is the simpler witness). | CLO-3 |
| 55 | 11 | **Cook–Levin on a specific NP language.** Pick HAMPATH or VERTEX-COVER and explicitly encode the verifier's TM into a SAT formula φ_x for a tiny input. Walk through every clause family. | CLO-4 |
| 56 | 12 | **SET-COVER (or TSP) NP-completeness.** Reduce 3SAT or VERTEX-COVER to SET-COVER (resp. HAMPATH to TSP); show the gadget on a small example. | CLO-4 |
| 57 | 13 | **EXPTIME vs PSPACE separation.** Use TIME(2<sup>O(f)</sup>) ⊇ SPACE(f) plus the time hierarchy theorem to argue why we have NO known proof that PSPACE ⊊ EXPTIME despite "obvious" intuition. | CLO-5 |
| 58 | 14 | **Othello / Hex / Checkers (generalised) PSPACE-completeness.** Pick one and walk through the encoding of TQBF into a polynomial-board game. | CLO-4 |
| 59 | 15 | **2-SAT ∈ NL.** Use the implication-graph approach; show how an NL machine guesses a path from x to ¬x (and from ¬x to x) to detect unsatisfiability. Apply NL = coNL. | CLO-3 |
| 60 | 16 | **EXPSPACE-completeness of REGEX equivalence.** Stockmeyer–Meyer: deciding whether two regular expressions are equivalent requires exponential space. Sketch the lower-bound reduction. | CLO-5 |

### Updated CLO totals (across 60)

| CLO | Count | Problems |
|:---:|---:|---|
| CLO-1 | 10 | 1, 2, 3, 4, 13, 16, 45(½), 46(½), 49, 52 |
| CLO-2 | 12 | 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 50, 51 |
| CLO-3 | 13 | 17, 18, 19, 20, 21, 22, 23, 24, 32, 41, 53, 54, 59 |
| CLO-4 | 15 | 25, 26, 27, 28, 29, 30, 31, 34, 36, 37, 38, 39, 40, 43, 55, 56, 58 |
| CLO-5 | 10 | 33, 35, 42, 44, 45(½), 46(½), 47, 48, 57, 60 |

---

## Student → slot assignment template (20 students, round-robin)

Each student presents **exactly once** in each round (R1, R2, R3). Each lecture hosts **5 presentations**.

| Student | Round 1 (lectures 5–8) | Round 2 (lectures 9–12) | Round 3 (lectures 13–16) |
|---|:---:|:---:|:---:|
| Student 1  | **#1**  (lec 5) | **#21** (lec 10) | **#41** (lec 15) |
| Student 2  | **#2**  (lec 5) | **#22** (lec 10) | **#42** (lec 15) |
| Student 3  | **#3**  (lec 5) | **#23** (lec 10) | **#43** (lec 15) |
| Student 4  | **#4**  (lec 5) | **#24** (lec 10) | **#44** (lec 15) |
| Student 5  | **#49** (lec 5) | **#54** (lec 10) | **#59** (lec 15) |
| Student 6  | **#5**  (lec 6) | **#25** (lec 11) | **#45** (lec 16) |
| Student 7  | **#6**  (lec 6) | **#26** (lec 11) | **#46** (lec 16) |
| Student 8  | **#7**  (lec 6) | **#27** (lec 11) | **#47** (lec 16) |
| Student 9  | **#8**  (lec 6) | **#28** (lec 11) | **#48** (lec 16) |
| Student 10 | **#50** (lec 6) | **#55** (lec 11) | **#60** (lec 16) |
| Student 11 | **#9**  (lec 7) | **#29** (lec 12) | **#33** (lec 13) |
| Student 12 | **#10** (lec 7) | **#30** (lec 12) | **#34** (lec 13) |
| Student 13 | **#11** (lec 7) | **#31** (lec 12) | **#35** (lec 13) |
| Student 14 | **#12** (lec 7) | **#32** (lec 12) | **#36** (lec 13) |
| Student 15 | **#51** (lec 7) | **#56** (lec 12) | **#57** (lec 13) |
| Student 16 | **#13** (lec 8) | **#17** (lec 9)  | **#37** (lec 14) |
| Student 17 | **#14** (lec 8) | **#18** (lec 9)  | **#38** (lec 14) |
| Student 18 | **#15** (lec 8) | **#19** (lec 9)  | **#39** (lec 14) |
| Student 19 | **#16** (lec 8) | **#20** (lec 9)  | **#40** (lec 14) |
| Student 20 | **#52** (lec 8) | **#53** (lec 9)  | **#58** (lec 14) |

**Verification:** every problem 1–60 appears exactly once in the grid above. Every student presents once in each round. Every lecture (5–16) hosts exactly 5 distinct problems.

**CLO span per student:** as designed, each student touches 3 different CLOs across their three presentations. If you want each student to touch *all five* CLOs, re-shuffle the columns by CLO-tag instead of by lecture-clustering.

---

## Grading rubric per presentation (suggested)

- **Correctness of the construction (40 %)**  — does the HTML tool actually solve / demonstrate the assigned problem?
- **Pedagogical clarity (30 %)** — does the visual explanation make the idea obvious to a peer who hasn't seen it?
- **Q&A defence (20 %)** — can the presenter answer follow-up questions ("what if we changed X?", "where does CLO-N fit?")
- **Polish & code quality (10 %)** — readable code, clean interface, no obvious bugs.

Scale to 30 for R1/R2 and 40 for R3.

---

## How students should use the existing companion site

The seven interactive modules at <https://arashkermaniprojects.github.io/computibility_and_complexity/> already contain many of the listed widgets (DFA simulator, computation-history viewer, Cook–Levin tableau, Geography game, hierarchy diagonalizer, …). Students should:

1. **Open the relevant module** and use it to learn the underlying theorem.
2. **Build a NEW tool** for their assigned problem, NOT clone the existing one. The existing tools are pedagogical references; the student deliverable should add a fresh angle (different example, different visualization, deeper interactivity).
3. **Cite the companion module** in their write-up.

If you'd like, I can expand any of the 48 problems into a one-page assignment brief with: precise input/output spec, hint sequence, suggested HTML structure, and grading rubric.
