# BCS 402 Computability and Complexity — Summer 2026 Schedule
**Dr. Arash Kermani · CUD · 24 students · 5-week intensive**

## Overview

| Item | Value |
|---|---|
| Semester start | Monday, June 1, 2026 |
| Semester end | Thursday, July 2, 2026 |
| Weeks | 5 |
| Lectures per week | 4 (Mon–Thu) |
| Length per session | 3 hours |
| Total sessions | 20 |
| Total students | 24 |
| Presentations per student | 3 (one per round) |
| Total presentation slots | 72 |

## Format

- **Week 1 (June 1–4)** — Pure lecture by Arash. 4 × 3 h = 12 h of teaching. No student presentations.
- **Weeks 2–4 (June 8–25)** — Each session: **1 h Arash lecture + 2 h student presentations**.
- **Week 5 (June 29–July 2)** — Student presentations only. 4 × 3 h = 12 h.

Each presentation slot is **30 minutes** (2 h ÷ 4 slots in weeks 2–4; 3 h ÷ 6 slots in week 5).

Students present **at least one week after** the concept they cover is introduced.

---

## Week-by-week

### Week 1 · June 1–4 · Foundations (12 h lecture, no presentations)

| Day | Date | Time | Content |
|---|---|---|---|
| Mon | Jun 1 | 3 h | **L7 + L8** — Decidable problems for automata (A_DFA, E_DFA, EQ_DFA, A_CFG, E_CFG). Decidable vs recognizable vs co-recognizable. Universal TM. |
| Tue | Jun 2 | 3 h | **L9** — A_TM is recognizable. Cantor diagonalization. A_TM is undecidable. The Venn diagram. |
| Wed | Jun 3 | 3 h | **L10** — Mapping reductions. HALT_TM, E_TM, REGULAR_TM, EQ_TM. |
| Thu | Jun 4 | 3 h | **L11 + L12** — Computation history reductions (E_LBA, ALL_CFG). Recursion theorem · Quine · Rice's theorem. |

### Week 2 · June 8–11 · Time complexity + NP (4 h lecture + 8 h presentations)

| Day | Date | 1 h Lecture | 2 h (4 × 30-min slots) Student Presentations |
|---|---|---|---|
| Mon | Jun 8 | **L13** — Time complexity, P, single vs multi-tape | R1 #1–4 |
| Tue | Jun 9 | **L14a** — NP, verifiers, examples (HAM-PATH, COMPOSITES, SUBSET-SUM) | R1 #5–8 |
| Wed | Jun 10 | **L14b** — Cook–Levin theorem (the tableau construction) | R1 #9–12 |
| Thu | Jun 11 | **L15** — NP-complete examples (3SAT, CLIQUE, VC, HAM-PATH) | R1 #13–16 |

### Week 3 · June 15–18 · Space + PSPACE (4 h lecture + 8 h presentations)

| Day | Date | 1 h Lecture | 2 h Student Presentations |
|---|---|---|---|
| Mon | Jun 15 | **L16** — Space complexity, PSPACE, examples | R1 #17–20 |
| Tue | Jun 16 | **L17** — Savitch's theorem, NPSPACE = PSPACE | R1 #21–24 |
| Wed | Jun 17 | **L18** — TQBF, PSPACE-completeness | R2 #1–4 (on L13–14) |
| Thu | Jun 18 | **L19** — Games (Geography, Generalized Hex/Chess) | R2 #5–8 (on L13–15) |

### Week 4 · June 22–25 · L, NL, Hierarchy (4 h lecture + 8 h presentations)

| Day | Date | 1 h Lecture | 2 h Student Presentations |
|---|---|---|---|
| Mon | Jun 22 | **L20a** — L, NL, log-space reductions | R2 #9–12 (on L15–16) |
| Tue | Jun 23 | **L20b** — NL-completeness (PATH), NL = coNL | R2 #13–16 (on L16–17) |
| Wed | Jun 24 | **L21a** — Space hierarchy theorem | R2 #17–20 (on L17–18) |
| Thu | Jun 25 | **L21b** — Time hierarchy theorem, synthesis | R2 #21–24 (on L18–19) |

### Week 5 · June 29–July 2 · Round 3 presentations (3 h × 4 = 12 h presentations only)

| Day | Date | 3 h (6 × 30-min slots) Round 3 Presentations |
|---|---|---|
| Mon | Jun 29 | R3 #1–6 (on L16–18 content) |
| Tue | Jun 30 | R3 #7–12 (on L18–19 content) |
| Wed | Jul 1 | R3 #13–18 (on L19–20 content) |
| Thu | Jul 2 | R3 #19–24 (on L20–21 content) |

---

## Round-by-round breakdown

### Round 1 (24 slots · 30 pts each) · Weeks 2–3
Foundational: decidability, reductions, Rice's theorem.
- Topics taught Week 1 (L7–L12).
- Presentations: Week 2 (16 slots) + Week 3 first 2 days (8 slots) = 24.
- Problem pool: P1–P16 (Round 1 core) + P49–P52 + 4 more → 24 problems.
- Per-student: each chooses 1 unassigned problem; ~25 min talk + 5 min Q&A.

### Round 2 (24 slots · 30 pts each) · Weeks 3–4
Time / NP / Space / PSPACE / Games.
- Topics taught Weeks 2–3 (L13–L19).
- Presentations: Week 3 last 2 days (8 slots) + Week 4 (16 slots) = 24.
- Problem pool: P17–P32 (Round 2 core) + P53–P56 + 4 more → 24 problems.

### Round 3 (24 slots · 40 pts each) · Week 5
L, NL, Hierarchy, advanced.
- Topics taught Weeks 3–4 (L18–L21).
- Presentations: all of Week 5.
- Problem pool: P33–P48 (Round 3 core) + P57–P60 + 4 more → 24 problems.

---

## Problem-pool expansion (60 → 72)

The existing 60 problems give 20 students × 3 rounds. With 24 students, we need 12 more problems (4 per round). Two options:

**Option A: add 12 new problems** (recommended).
Suggested additions:
- R1: Decider for E_DFA-with-NFA-input · Computability of automaton minimization · ¬HALT recognizability · Closure under intersection for decidable.
- R2: Cook–Levin for 2-tape TM · NP closed under union? · Self-reducibility of TSP · Search vs decision for HAM-PATH.
- R3: NL closed under complement (full Immerman–Szelepcsényi proof) · Reachability in O(log²) space (Savitch applied) · TIME-SPACE tradeoff for SAT · Open: P vs PSPACE landscape.

**Option B: paired presentations on existing problems** (12 of the 60 problems get presented by 2 students, each covering a different angle — e.g., one student does the proof, the other does worked examples & connections).

I recommend Option A for cleaner individual responsibility. I can build the 12 new tool pages on request.

---

## Student-presentation slot grid

Use this grid to fill in student names. Numbers 1–24 = problem index within the round.

```
ROUND 1 (slot → student)
Week 2  Mon: 1__  2__  3__  4__
Week 2  Tue: 5__  6__  7__  8__
Week 2  Wed: 9__  10__ 11__ 12__
Week 2  Thu: 13__ 14__ 15__ 16__
Week 3  Mon: 17__ 18__ 19__ 20__
Week 3  Tue: 21__ 22__ 23__ 24__

ROUND 2
Week 3  Wed: 1__  2__  3__  4__
Week 3  Thu: 5__  6__  7__  8__
Week 4  Mon: 9__  10__ 11__ 12__
Week 4  Tue: 13__ 14__ 15__ 16__
Week 4  Wed: 17__ 18__ 19__ 20__
Week 4  Thu: 21__ 22__ 23__ 24__

ROUND 3
Week 5  Mon: 1__  2__  3__  4__  5__  6__
Week 5  Tue: 7__  8__  9__  10__ 11__ 12__
Week 5  Wed: 13__ 14__ 15__ 16__ 17__ 18__
Week 5  Thu: 19__ 20__ 21__ 22__ 23__ 24__
```

Each student fills three rows — one per round. Round-robin assignment recommended: student S<sub>k</sub> presents R1 slot k, R2 slot ((k+8) mod 24) + 1, R3 slot ((k+16) mod 24) + 1 — guarantees nobody presents on the same day twice.

---

## Grading recap

| Item | Points |
|---|---|
| Round 1 (one presentation, foundational) | 30 |
| Round 2 (one presentation, NP/PSPACE) | 30 |
| Round 3 (one presentation, advanced) | 40 |
| **Total** | **100** |

Rubric per presentation (already in `ASSESSMENT_PLAN.md`):
- Clarity & structure: 25%
- Mathematical correctness: 25%
- Visual / animation use (interactive tool): 20%
- Q&A defence: 20%
- Engagement & timing: 10%

---

## Reading-ahead requirements

So students can prepare before their slot:
- **For R1:** assigned by end of Week 1, presentation in Week 2–3.
- **For R2:** assigned by end of Week 2, presentation in Week 3–4.
- **For R3:** assigned by end of Week 3, presentation in Week 5.

Each student is given their problem ID and the relevant tool page (`/tools/p##-…html`) on the website at assignment time.

---

## Key constraints satisfied

- 5 weeks × 4 lectures/week × 3 h = 60 h total class time ✓
- 24 h Arash lecture (12 h Week 1 + 12 h Weeks 2–4) covering MIT L7–L21 ✓
- 36 h presentations (24 h Weeks 2–4 + 12 h Week 5) ÷ 30 min/slot = 72 slots ✓
- 24 students × 3 rounds = 72 slots ✓
- Every student presents ≥ 1 week after concept is introduced ✓
