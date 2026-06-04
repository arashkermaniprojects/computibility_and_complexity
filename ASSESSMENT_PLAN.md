# BCS 402 — Student-led Lecture Assessment Plan

**Dr. Arash Kermani · CUD · Fall 2026 · Revised for 18 students**

## What changed in this revision

The previous version of this plan had 60 candidate problems for 20 students. After re-auditing:

- **Many entries weren't really problems** — they were concepts the lecture already explains (Cantor's diagonal, growth-rate animator, P-class showcase, etc.) or duplicates of widgets already living in the companion site (Universal TM, A_TM diagonalization, Cook-Levin tableau, Geography game, hierarchy diagonalizers, …). Asking a student to re-build any of these doesn't test the CLOs, it just produces a slicker version of the lecture demo.
- **Enrollment dropped to 18.** Total slots needed: 18 × 3 rounds = **54 presentations**.
- **It's fine for a problem to be assigned to two students** — they can present different example inputs, different gadget focuses, or different proof angles. The second presentation isn't a re-run; it's a separate worked example.

The result: a curated pool of **39 genuine problems** (14 R1 + 13 R2 + 12 R3), each requiring a substantive construction, reduction, or proof. **15 of them get two presenters** (different inputs); the other 24 get one presenter each. Every student touches **3 distinct CLOs** across the semester.

## Logistics

- Instructor's lectures finish by **Thu Jun 11, 2026** (end of the preceding teaching week).
- **Mon Jun 15 – Tue Jun 30** is the student-only block. Classes meet **Mon–Thu only** (no Fri / weekend), giving **10 class days**:
  - Week 1: Mon Jun 15, Tue Jun 16, Wed Jun 17, Thu Jun 18
  - Week 2: Mon Jun 22, Tue Jun 23, Wed Jun 24, Thu Jun 25
  - Week 3: Mon Jun 29, Tue Jun 30
- 18 students × 3 presentations each = **54 student slots** → **5.4 presentations per class on average** (4–6 per class in practice).
- Suggested time per slot: 12–15 min including Q&A. So a typical day runs ≈ 75–105 min of presentations.
- Each student presents **once per round**.

### Daily schedule (Jun 15 – Jun 30, 2026)

| Day | Date | Round | Theme | Slots | Problems |
|---:|---|:---:|---|---:|---|
|  1 | Mon Jun 15 | R1 | Direct reductions + bridge thm (Mod. 2–3) | 6 | R1.1, R1.2, R1.3, R1.4, R1.9 ×2 |
|  2 | Tue Jun 16 | R1 | Computation-history + Rice + recursion thm (Mod. 3) | 6 | R1.5, R1.6, R1.7, R1.8, R1.10, R1.11 |
|  3 | Wed Jun 17 | R1 | Self-reference & LBA contrasts (Mod. 3) | 6 | R1.12 ×2, R1.13 ×2, R1.14 ×2 |
|  4 | Thu Jun 18 | R2 | Cook–Levin NP-complete reductions (Mod. 5) | 6 | R2.1, R2.2, R2.3, R2.4, R2.5, R2.6 |
|  5 | Mon Jun 22 | R2 | Verifiers & self-reducibility (Mod. 5) | 6 | R2.7 ×2, R2.8 ×2, R2.9 ×2 |
|  6 | Tue Jun 23 | R2 | Class containments + Cook–Levin specifics (Mod. 4–5) | 6 | R2.10, R2.11, R2.12 ×2, R2.13 ×2 |
|  7 | Wed Jun 24 | R3 | Savitch & TQBF (Mod. 6) | 5 | R3.1 ×2, R3.2, R3.3 ×2 |
|  8 | Thu Jun 25 | R3 | PSPACE-hardness of games + start NL ⊊ PSPACE (Mod. 6–7) | 4 | R3.4, R3.5 ×2, R3.6 |
|  9 | Mon Jun 29 | R3 | Hierarchy theorems & L/NL consequences (Mod. 7) | 4 | R3.6 *variant*, R3.7 ×2, R3.8 |
| 10 | Tue Jun 30 | R3 | Exotic completeness & inductive counting (Mod. 7) | 5 | R3.9 ×2, R3.10, R3.11, R3.12 |
| **Total** | | | | **54** | |

Round structure:
- **Round 1** = Days 1–3 (Mon Jun 15 – Wed Jun 17). Modules 2–3 (undecidability, reductions, recursion theorem). **CLOs 1, 2.** 30 points.
- **Round 2** = Days 4–6 (Thu Jun 18, Mon Jun 22, Tue Jun 23). Modules 4–5 (time, P, NP, Cook–Levin). **CLOs 3, 4.** 30 points.
- **Round 3** = Days 7–10 (Wed Jun 24, Thu Jun 25, Mon Jun 29, Tue Jun 30). Modules 6–7 (space, PSPACE, L/NL, hierarchy). **CLOs 4, 5.** 40 points. Highest-stakes round — gets the extra day for more time per presenter.

Notes on R3.6: it has two presenters; one gives the introductory pass on Day 8 (right after the PSPACE-hardness games), the other gives the *variant* on Day 9 (alongside the hierarchy-theorem block) — that lets the second presenter build on the first.

### Grading

| Round | Days | Per-student score | Total weight |
|------:|:--------:|:-----------------:|:------:|
| Round 1 | 1–3 (Jun 15–17)  | 30 | first presentation |
| Round 2 | 4–6 (Jun 18, 22, 23)  | 30 | second presentation |
| Round 3 | 7–10 (Jun 24, 25, 29, 30) | 40 | third (highest-stakes) presentation |
| **Total** | | **100** | |

### Course Learning Outcomes

| CLO | Topic | Target touches (of 54) | Actual |
|---|---|---:|---:|
| CLO-1 | Diagonalization → undecidability | 9 | **8** |
| CLO-2 | Reductions → algorithmic unsolvability | 11 | **10** |
| CLO-3 | Finding vs. verifying complexity | 12 | **11** |
| CLO-4 | Mapping reductions → hardness | 14 | **17** |
| CLO-5 | Hierarchy theorems → class separation | 9 | **8** |

CLO-4 runs slightly over target because the bulk of Cook–Levin-style and PSPACE-hardness reductions naturally fall there. CLO-1 / CLO-5 are slightly under because the lectures themselves do most of the heavy lifting on diagonalization and hierarchy — the student presentations focus on the surrounding constructions.

---

## What was removed (and why)

The 26 candidate problems below were cut from the assignment pool. The reasons all fall into the same two buckets:

**Concept-only problems** — the deliverable is just "explain the idea visually," but the instructor has already done exactly that in the live lecture and on the companion site. Asking the student to rebuild it is busywork, not assessment.

**Duplicates of companion-site widgets** — the lecture site already ships the interactive demo. The student would just re-skin it.

| Cut | Topic | Why |
|---:|---|---|
| 1  | Cantor's diagonal interactive proof | Module 2 slide 1 walks the diagonal with the three-moves visual and a working widget. |
| 2  | Universal TM simulator | Module 2 slide 2 has a working UTM with a 3-region-tape figure. |
| 3  | A_TM-undecidability table | Module 2 slide 3 has the diagonal walkthrough + "Pick k" contradiction visual. |
| 4  | R/coR/D Venn classifier | Module 2 slide 5 has the quiz widget. |
| 9  | Computation-history visualizer | Module 3 already renders the configuration trace. |
| 12 | A_DFA / E_DFA / A_CFG side-by-side | Module 1 slides 2–5 have each individually. |
| 17 | Growth-rate animator | Module 4 slide 1. |
| 18 | {0ⁿ1ⁿ} single-tape decider | Module 4 slide 3 (with Sipser-aligned scan + rewind). |
| 19 | Single vs two-tape race | Module 4 slide 4. |
| 20 | Big-O classifier | Module 4 slide 2 explains Big-O directly. |
| 21 | Verifier vs solver race | Module 5 covers it. |
| 22 | Interactive SAT | Module 5 has a SAT widget. |
| 24 | P-class showcase (PATH/RELPRIME/CYK) | Module 4 slide 5 has primer cards + animated demos. |
| 25 | Cook–Levin tableau viewer | Module 5 has the tableau. |
| 33 | Space vs time bar chart | Concept, covered in module 6. |
| 36 | Game-tree evaluator for TQBF | Module 6 has the game-tree widget. |
| 38 | Generalized Geography game | Module 6 already has a playable Geography game. |
| 41 | Log-space pointer-chaser | Concept, covered in module 7. |
| 42 | NL PATH non-deterministic visualization | Module 7 demonstrates non-deterministic PATH. |
| 43 | PATH NL-complete (companion widget) | Module 7. Kept as R3.12 with explicit construction requirement. |
| 44 | Inductive counting | Module 7 has the c_i widget. Kept as R3.9 (different angle: explicit small-graph run). |
| 45 | Space hierarchy diagonalization | Module 7. |
| 46 | Time hierarchy diagonalization | Module 7. Kept as R3.7 (different angle: derive P ⊊ EXPTIME explicitly). |
| 49 | Closure-property explorer | Concept. Folded into R1.9 (bridge theorem proof) and R2.13 (P closure properties — kept as a real-proof exercise). |
| 53 | TM running-time profiler | Concept. |

For comparison, the ones marked "kept but reframed" (R3.7, R3.9, R3.12) ask the student to *prove the result on a small explicit input* rather than just animate the abstract concept — a different deliverable from what the companion widget shows.

---

## ROUND 1 · Days 1–3 (Mon Jun 15 – Wed Jun 17) · 30 points each

*Theme: undecidability, diagonalization, reductions, recursion theorem.* Built on Modules 2–3. CLOs **1, 2**.

### Day 1 — Mon Jun 15 — Direct reductions + bridge theorem (Modules 2–3)

| ID | Problem | CLO |
|----|---|:--:|
| **R1.1** | **HALT_TM ≤_m A_TM (mapping reduction).** Given ⟨M, w⟩, construct M′ such that M′ halts on its input iff M accepts w. Walk through the encoding on **two specific (M, w) examples** of your choice. Defend why HALT_TM is undecidable. | CLO-2 |
| **R1.2** | **E_TM undecidability.** Reduce A_TM to E_TM: build M_w that ignores its input and runs M(w); argue L(M_w) = ∅ iff M does not accept w. | CLO-2 |
| **R1.3** | **REGULAR_TM undecidability.** Build M_w whose language is {0ⁿ1ⁿ : n≥0} if M does NOT accept w, otherwise Σ*. Argue L(M_w) is regular iff M accepts w. | CLO-2 |
| **R1.4** | **A_TM ≤_m EQ_TM mapping reduction.** Construct ⟨M_1, M_2⟩ such that L(M_1) = L(M_2) iff M accepts w. Defend why this proves EQ_TM undecidable. | CLO-2 |

### Day 2 — Tue Jun 16 — Computation-history method + Rice + recursion theorem (Module 3)

| ID | Problem | CLO |
|----|---|:--:|
| **R1.5** | **E_LBA undecidability via computation history.** Build the LBA B_{M,w} that accepts iff its input is a valid accepting history of M on w. Argue L(B) ≠ ∅ iff M accepts w, hence E_LBA undecidable. Walk the construction on a small (M, w). | CLO-2 |
| **R1.6** | **ALL_CFG undecidability.** Build the CFG G_{M,w} that generates *every string except* accepting histories of M on w. Walk the local-violation gadget that detects bad transitions, bad headers, or bad final states. | CLO-2 |
| **R1.7** | **FINITE_TM undecidability.** Reduce A_TM to FINITE_TM: given ⟨M, w⟩, build M′ whose language is finite iff M does NOT accept w. | CLO-2 |
| **R1.8** | **PCP undecidability via computation history.** Encode an arbitrary TM's accepting computation as a Post Correspondence System; sketch the domino tile sets (start, transition, accept) that force solvability ⇔ acceptance. | CLO-2 |

### Day 3 — Wed Jun 17 — Self-reference & LBA contrasts (Module 3)

| ID | Problem | CLO |
|----|---|:--:|
| **R1.9** | **Bridge theorem (constructive proof).** Prove: L is decidable iff both L and L̄ are Turing-recognizable. Show explicitly how to build a decider for L from recognizers for L and L̄ (interleaved simulation). Explain the converse. | CLO-1 |
| **R1.10** | **Rice's theorem applied to three properties.** Choose three concrete properties P (e.g., "L(M) is regular", "L(M) is finite", "L(M) contains ε"). For each: confirm Rice's preconditions (nontrivial + semantic), then conclude the property is undecidable. Walk the contradiction at one chosen property. | CLO-2 |
| **R1.11** | **Recursion theorem fixed point for a chosen t(x).** Pick a computable function t (e.g., "append `bye` to the input"). Construct the fixed-point program p with p ≡ t(⟨p⟩) explicitly. Verify by running p that the fixed-point property holds. | CLO-2 |

<!-- Day 4 reassigned to Round 2 — see ROUND 2 section -->

| ID | Problem | CLO |
|----|---|:--:|
| **R1.12** | **Self-destructing TM (Kamikaze).** Use the recursion theorem to build a TM that on any input prints its own description ⟨M⟩ and halts. Defend why recursion theorem makes self-reference *safe* (no paradox). | CLO-1 |
| **R1.13** | **Quine + data/code split annotation.** In any language, produce a working program that outputs its own source code. Annotate where the data section (the encoded source) ends and the code section (the printer) begins. Defend connection to recursion theorem. | CLO-1 |
| **R1.14** | **A_LBA decidable vs E_LBA undecidable.** Show A_LBA is decided by bounded simulation: a |Q| · |Γ|ⁿ · n state-space gives a halting decider. Contrast with E_LBA's undecidability (R1.5) — same machine model, different question. | CLO-1 |

---

## ROUND 2 · Days 4–6 (Thu Jun 18, Mon Jun 22, Tue Jun 23) · 30 points each

*Theme: time complexity, P, NP, Cook–Levin, NP-completeness.* Built on Modules 4–5. CLOs **3, 4**.

### Day 4 — Thu Jun 18 — Cook–Levin NP-complete reductions (Module 5)

| ID | Problem | CLO |
|----|---|:--:|
| **R2.1** | **SAT → 3SAT reduction.** Take any clause with k > 3 literals; introduce auxiliary variables; transform to ≤3-literal clauses. Walk a worked example with **a 5-literal clause**. Prove satisfiability is preserved. | CLO-4 |
| **R2.2** | **3SAT → CLIQUE.** Build the literal-occurrence graph; argue clique of size k iff formula satisfiable. Walk a 3-clause example. | CLO-4 |
| **R2.3** | **CLIQUE → VERTEX-COVER.** Complement-graph trick: clique of size k in G ⇔ vertex cover of size n−k in G̅. Show the bijection on a 5-vertex graph. | CLO-4 |
| **R2.4** | **3SAT → SUBSET-SUM.** Construct the digit-position number system; show the target sum forces a satisfying assignment. Walk a 2-clause, 3-variable example. | CLO-4 |

### Day 5 — Mon Jun 22 — Verifiers & self-reducibility (Module 5)

| ID | Problem | CLO |
|----|---|:--:|
| **R2.5** | **3SAT → HAMPATH.** Variable diamonds + clause spreaders. Walk the gadget construction on a 2-clause formula. | CLO-4 |
| **R2.6** | **3SAT → 3COLOR.** Variable + OR-gadget graph. Show 3-colorings ↔ satisfying assignments. | CLO-4 |
| **R2.7** | **SAT self-reducibility (search ↔ decision).** Given a poly-time oracle deciding SAT, find an actual satisfying assignment in poly time. Defend why this means "if P = NP, finding is as easy as deciding." | CLO-3 |
| **R2.8** | **COMPOSITES verifier.** Certificate = a non-trivial divisor. Check divisibility in poly time. Argue COMPOSITES ∈ NP. (Footnote: AKS later put it in P; the verifier was the simpler witness.) | CLO-3 |

### Day 6 — Tue Jun 23 — Class containments + Cook–Levin specifics (Modules 4–5)

| ID | Problem | CLO |
|----|---|:--:|
| **R2.9** | **HAMPATH verifier (NP-membership proof).** Given a graph G and a candidate vertex sequence v₁, v₂, …, vₙ, check in poly time whether it is a Hamiltonian path. Defend HAMPATH ∈ NP. | CLO-3 |
| **R2.10** | **SET-COVER NP-completeness.** Reduce VERTEX-COVER ≤_p SET-COVER. Show the gadget on a small example: vertices of VC ↔ elements of SET-COVER; edges ↔ sets. | CLO-4 |
| **R2.11** | **Cook–Levin on a tiny TM.** Pick a 3-state non-deterministic TM that decides a small NP-language. For input |x| = 3, write down the SAT formula φ_{M, x} **explicitly** — all clause families (cell, start, move, accept). | CLO-4 |

<!-- Day 8 absorbed into Day 6 -->

| ID | Problem | CLO |
|----|---|:--:|
| **R2.12** | **NP ⊆ EXPTIME via NTM determinization.** Show every NTM running in time t(n) can be simulated by a DTM in time 2^O(t(n)) (BFS over the computation tree). Walk through how t(n) = n^k gives DTM time 2^O(n^k). | CLO-3 |
| **R2.13** | **P closure properties.** Prove: P is closed under union, intersection, and complement. For each closure, give the constructive proof (a polynomial-time decider for the combined language). Explain why "complement of NP" needs more care. | CLO-3 |

---

## ROUND 3 · Days 7–10 (Wed Jun 24, Thu Jun 25, Mon Jun 29, Tue Jun 30) · 40 points each (highest-stakes)

*Theme: space complexity, PSPACE, games, L/NL, hierarchy theorems.* Built on Modules 6–7. CLOs **4, 5**.

### Day 7 — Wed Jun 24 — Savitch & TQBF (Module 6)

| ID | Problem | CLO |
|----|---|:--:|
| **R3.1** | **Savitch's algorithm — explicit run on a small graph.** Take a 6-vertex directed graph with one path of length ≤ 4. Run CANYIELD(s, t, t=4) recursively; show the call tree, track stack depth = log t. Explain why total space = O(log² n). | CLO-4 |
| **R3.2** | **TQBF ↔ TQBF₃ (alternating, ≤3 literals).** Take an arbitrary QBF; convert to the alternating-quantifier ≤3-literal form. Show satisfiability preserved. | CLO-4 |
| **R3.3** | **TQBF → Generalized Geography.** Encode a small QBF (say ∃x ∀y ∃z. φ) as a directed-graph game. Show the ∃-player wins iff QBF is true. Walk the variable + clause gadgets. | CLO-4 |

### Day 8 — Thu Jun 25 — PSPACE-hardness of games + start NL ⊊ PSPACE (Modules 6–7)

| ID | Problem | CLO |
|----|---|:--:|
| **R3.4** | **Generalized chess PSPACE-hardness.** Encode TQBF as an n × n chess endgame. Sketch the role of each piece in encoding existential vs. universal quantifier moves. | CLO-4 |
| **R3.5** | **Generalized Othello or Hex PSPACE-completeness.** Pick one; show TQBF ≤_p the game on an n × n board. Walk the encoding. | CLO-4 |

### Day 9 — Mon Jun 29 — Hierarchy theorems & L/NL consequences (Module 7)

| ID | Problem | CLO |
|----|---|:--:|
| **R3.6** | **NL ⊊ PSPACE via space hierarchy.** Use SPACE(log n) ⊊ SPACE(n) and NL ⊆ SPACE(log² n) ⊆ SPACE(n^{0.5}) (Savitch) to derive NL ⊊ PSPACE. | CLO-5 |
| **R3.7** | **P ⊊ EXPTIME via time hierarchy.** Use the time hierarchy theorem (TIME(2^n) ⊋ TIME(n^k) for every constant k) to derive P ⊊ EXPTIME explicitly. Defend why this is one of the few known *proven* separations. | CLO-5 |
| **R3.8** | **2-SAT ∈ NL via implication graph.** Build the implication graph (each literal x_i and ¬x_i is a node, each 2-clause gives two implication edges). Show how an NL machine guesses a path from x to ¬x (and back) to detect unsatisfiability. Use NL = coNL to finish. | CLO-3 |

### Day 10 — Tue Jun 30 — Exotic completeness & inductive counting (Module 7)

| ID | Problem | CLO |
|----|---|:--:|
| **R3.9** | **NL = coNL: explicit Immerman–Szelepcsényi run.** Walk inductive counting on a small graph. Compute c_i (vertices reachable from s in ≤ i steps); show how knowing c_n lets an NL machine certify "t is not reachable" in NL. Conclude NL = coNL. | CLO-5 |
| **R3.10** | **EXPTIME vs PSPACE.** Use SPACE(f) ⊆ TIME(2^O(f)) and the time hierarchy to show PSPACE ⊆ EXPTIME. Defend why strict containment PSPACE ⊊ EXPTIME is **open** despite the obvious intuition. | CLO-5 |
| **R3.11** | **EXPSPACE-completeness of REGEX equivalence.** Sketch Stockmeyer–Meyer: deciding whether two regular expressions over Σ define the same language requires exponential space. Walk the lower-bound reduction. | CLO-5 |
| **R3.12** | **PATH NL-complete: explicit configuration graph.** Take a specific NL machine (e.g., one deciding palindromes); construct its configuration graph; show every NL language log-space reduces to PATH via this construction. Walk the encoding on input of length 4. | CLO-4 |

---

## Problems with two presenters

The 15 problems below get two student presentations. Both presenters work the same construction but on **different example inputs** and may emphasize different aspects (one focuses on the gadget mechanics, the other on the correctness proof or the running-time analysis).

| Problem | Presenters | Suggested variation |
|---|---|---|
| R1.9 Bridge theorem | S04, S06 | One does the constructive direction in full; the other focuses on the converse + interleaved-simulation detail. |
| R1.12 Kamikaze TM | S08, S10 | Different deliverable styles (Python program vs. abstract TM transitions). |
| R1.13 Quine | S12, S14 | Different host languages. |
| R1.14 LBA contrast | S16, S18 | One emphasizes A_LBA decider; the other contrasts with E_LBA. |
| R2.7 SAT self-reducibility | S01, S02 | Different number-of-variables; different reduction "trees." |
| R2.8 COMPOSITES verifier | S05, S17 | Different size composites; one mentions AKS. |
| R2.9 HAMPATH verifier | S06, S13 | Different graphs; different rejection examples. |
| R2.12 NP ⊆ EXPTIME | S16, S18 | Different worked NTMs. |
| R2.13 P closure | S03, S15 | One focuses on union/intersection; other on complement + contrast with NP. |
| R3.1 Savitch run | S02, S17 | Different graphs/path-lengths. |
| R3.3 TQBF → Geography | S13, S18 | Different QBF examples. |
| R3.5 Othello/Hex | S03, S15 | Different game choice. |
| R3.6 NL ⊊ PSPACE | S07, S14 | Different chains of containments. |
| R3.7 P ⊊ EXPTIME | S04, S16 | Different machine examples in the diagonalization. |
| R3.9 Immerman–Szelepcsényi | S10, S12 | Different graphs. |

---

## Student → slot assignment (18 students)

Each student touches **3 distinct CLOs** across their three presentations.

| Student | Round 1 | Round 2 | Round 3 | CLOs touched |
|---|---|---|---|---|
| **S01** | R1.1  HALT_TM ≤_m A_TM *(Mon Jun 15)* | R2.7  SAT self-reducibility *(Mon Jun 22)* | R3.2  TQBF ↔ TQBF₃ *(Wed Jun 24)* | CLO-2, CLO-3, CLO-4 |
| **S02** | R1.2  E_TM undecidability *(Mon Jun 15)* | R2.7  SAT self-reducibility *variant* *(Mon Jun 22)* | R3.1  Savitch on small graph *(Wed Jun 24)* | CLO-2, CLO-3, CLO-4 |
| **S03** | R1.3  REGULAR_TM undecidability *(Mon Jun 15)* | R2.13 P closure properties *(Tue Jun 23)* | R3.5  Othello/Hex PSPACE-completeness *(Thu Jun 25)* | CLO-2, CLO-3, CLO-4 |
| **S04** | R1.9  Bridge theorem *(Mon Jun 15)* | R2.2  3SAT → CLIQUE *(Thu Jun 18)* | R3.7  P ⊊ EXPTIME *variant* *(Mon Jun 29)* | CLO-1, CLO-4, CLO-5 |
| **S05** | R1.4  A_TM ≤_m EQ_TM *(Mon Jun 15)* | R2.8  COMPOSITES verifier *variant* *(Mon Jun 22)* | R3.4  Generalized chess PSPACE-hardness *(Thu Jun 25)* | CLO-2, CLO-3, CLO-4 |
| **S06** | R1.9  Bridge theorem *variant* *(Mon Jun 15)* | R2.9  HAMPATH verifier *(Mon Jun 22)* | R3.12 PATH NL-complete *(Tue Jun 30)* | CLO-1, CLO-3, CLO-4 |
| **S07** | R1.5  E_LBA undecidability *(Tue Jun 16)* | R2.3  CLIQUE → VC *(Thu Jun 18)* | R3.6  NL ⊊ PSPACE *(Thu Jun 25)* | CLO-2, CLO-4, CLO-5 |
| **S08** | R1.12 Self-destructing TM (Kamikaze) *(Wed Jun 17)* | R2.1  SAT → 3SAT *(Thu Jun 18)* | R3.10 EXPTIME vs PSPACE *(Tue Jun 30)* | CLO-1, CLO-4, CLO-5 |
| **S09** | R1.6  ALL_CFG undecidability *(Tue Jun 16)* | R2.4  3SAT → SUBSET-SUM *(Thu Jun 18)* | R3.8  2-SAT ∈ NL *(Mon Jun 29)* | CLO-2, CLO-4, CLO-3 |
| **S10** | R1.12 Kamikaze *variant* *(Wed Jun 17)* | R2.10 SET-COVER NP-completeness *(Tue Jun 23)* | R3.9  Immerman–Szelepcsényi *(Tue Jun 30)* | CLO-1, CLO-4, CLO-5 |
| **S11** | R1.7  FINITE_TM undecidability *(Tue Jun 16)* | R2.6  3SAT → 3COLOR *(Thu Jun 18)* | R3.11 EXPSPACE-complete REGEX *(Tue Jun 30)* | CLO-2, CLO-4, CLO-5 |
| **S12** | R1.13 Quine + annotation *(Wed Jun 17)* | R2.11 Cook–Levin on a tiny TM *(Tue Jun 23)* | R3.9  Immerman–Szelepcsényi *variant* *(Tue Jun 30)* | CLO-1, CLO-4, CLO-5 |
| **S13** | R1.8  PCP undecidability *(Tue Jun 16)* | R2.9  HAMPATH verifier *variant* *(Mon Jun 22)* | R3.3  TQBF → Geography *variant* *(Wed Jun 24)* | CLO-2, CLO-3, CLO-4 |
| **S14** | R1.13 Quine *variant* *(Wed Jun 17)* | R2.5  3SAT → HAMPATH *(Thu Jun 18)* | R3.6  NL ⊊ PSPACE *variant* *(Mon Jun 29)* | CLO-1, CLO-4, CLO-5 |
| **S15** | R1.10 Rice's theorem on 3 properties *(Tue Jun 16)* | R2.13 P closure properties *variant* *(Tue Jun 23)* | R3.5  Othello/Hex *variant* *(Thu Jun 25)* | CLO-2, CLO-3, CLO-4 |
| **S16** | R1.14 A_LBA vs E_LBA contrast *(Wed Jun 17)* | R2.12 NP ⊆ EXPTIME *(Tue Jun 23)* | R3.7  P ⊊ EXPTIME *(Mon Jun 29)* | CLO-1, CLO-3, CLO-5 |
| **S17** | R1.11 Recursion fixed-point *(Tue Jun 16)* | R2.8  COMPOSITES verifier *(Mon Jun 22)* | R3.1  Savitch on small graph *variant* *(Wed Jun 24)* | CLO-2, CLO-3, CLO-4 |
| **S18** | R1.14 A_LBA vs E_LBA *variant* *(Wed Jun 17)* | R2.12 NP ⊆ EXPTIME *variant* *(Tue Jun 23)* | R3.3  TQBF → Geography *(Wed Jun 24)* | CLO-1, CLO-3, CLO-4 |

### Verification

- Every CLO appears in every student's three-presentation set as a distinct touch (CLO diversity = 3/3 for all 18 students).
- 39 distinct problems, 54 slots — 15 problems have two presenters, 24 problems have one.
- Day-by-day load: 6, 6, 6, 6, 6, 6, 5, 4, 4, 5. Min 4 (Thu Jun 25 and Mon Jun 29), max 6 (Days 1–6).

---

## Grading rubric per presentation

- **Correctness of the construction (40 %)** — does the reduction / proof actually work? Are the gadgets / clauses / encodings sound?
- **Pedagogical clarity (30 %)** — does the walkthrough make the construction obvious to a peer? Are the right diagrams / examples on screen?
- **Q&A defence (20 %)** — can the presenter answer follow-up questions ("what if M loops?", "where does the reduction fail if you drop this clause?", "what's the running time?")?
- **Polish & code quality (10 %)** — for problems with an interactive component: clean code, no bugs, readable interface.

Scaled to **30** for R1/R2 and **40** for R3.

---

## How students should use the companion site

The seven interactive modules at <https://arashkermaniprojects.github.io/computibility_and_complexity/> already cover the *foundational* widgets students would have otherwise had to rebuild (UTM, A_TM diagonalization, Cook–Levin tableau, Geography game, hierarchy diagonalizers, …).

Students should:

1. **Open the relevant module** and use the companion widgets to *learn* the underlying theorem.
2. **For their assigned problem, build a NEW deliverable** — a slide deck + a small standalone tool *or* a clean written walkthrough with diagrams — focused on the specific construction in their problem. They should NOT just re-skin a companion widget.
3. **Cite the companion module** in their write-up.

---

## Notes on the variant pairs

For each two-presenter problem, the two students present sequentially in the same lecture but should coordinate so the second presenter's example **differs nontrivially** from the first:

- For reductions (R2.1, R2.2, R2.4, R2.5, R2.6, R3.3, R3.5): different inputs / formulas / boards.
- For self-reducibility / NP-membership / closure (R2.7, R2.9, R2.13): different machine examples.
- For hierarchy proofs (R3.7, R3.6): one focuses on the diagonalization machinery, the other on the consequence.
- For computational artifacts (R1.13 quines, R1.12 kamikazes): different host languages.
- For proof-walkthrough problems (R1.9, R1.14): one focuses on the forward direction, the other on the converse / contrast.

The second presenter is **not** repeating the first; they are providing an independent worked example. Encourage them to discuss with each other beforehand so the two presentations complement rather than overlap.
