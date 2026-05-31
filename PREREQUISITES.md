# Prerequisites for BCS 402 · Computability and Complexity

Our course begins at **MIT 18.404J Lecture 7** (Sipser Chapter 4). Everything in MIT lectures 1–6 / Sipser Chapters 0–3 is assumed. This page lists what you need to know, the exact place in Sipser to read it, and the matching free MIT OCW lecture video.

> **Textbook.** Sipser, M. *Introduction to the Theory of Computation*, 3rd ed., Cengage 2012.
> **Free videos.** MIT 18.404J / 6.840J Fall 2020 · <https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/>
> **MIT lecture notes (free PDFs).** Same page → "Lecture Notes" → individual L1–L6 slides.

---

## 0 · Mathematical preliminaries — Sipser Chapter 0

You need to be comfortable with:

- **Sets, subsets, union, intersection, complement, symmetric difference** — Sipser §0.2
- **Sequences, tuples, Cartesian product** — Sipser §0.2
- **Functions and relations** — domain, range, injective / surjective / bijective — Sipser §0.2
- **Graphs** — directed / undirected, paths, connectivity, degree — Sipser §0.2
- **Strings, alphabets, languages** — Σ, Σ*, |w|, ε, concatenation — Sipser §0.2
- **Boolean logic** — AND, OR, NOT, implication, quantifiers ∀ and ∃ — Sipser §0.2
- **Proof techniques** — direct, contradiction, induction — Sipser §0.4

This is the absolute floor. If any of this feels shaky, spend a day on Sipser Chapter 0 before anything else.

---

## 1 · Finite automata and regular languages — Sipser Chapter 1

### 1a · Deterministic finite automata (DFA)
> Sipser §1.1 · MIT 18.404J Lecture 1

What to learn:
- Five-tuple definition (Q, Σ, δ, q₀, F)
- How a DFA reads a string symbol by symbol
- What "language of M" means: L(M) = strings the DFA accepts
- The **regular operations** — union, concatenation, star
- Drawing state diagrams

**Why we need it.** Module 1 problems A<sub>DFA</sub>, E<sub>DFA</sub>, EQ<sub>DFA</sub> are entirely about DFAs. The product construction in EQ<sub>DFA</sub> assumes you already understand simulating a DFA.

### 1b · Nondeterministic finite automata (NFA)
> Sipser §1.2 · MIT 18.404J Lecture 1–2

What to learn:
- ε-transitions and multiple successor states
- **NFA → DFA conversion** (subset construction) and the exponential blow-up
- Regular languages closed under union, concat, star, complement, intersection

**Why we need it.** Module 2 brings nondeterminism back when we move to Turing machines. The "non-deterministic guess and verify" idea first appears with NFAs and reappears everywhere afterwards (NP, NL, NPSPACE).

### 1c · Regular expressions
> Sipser §1.3 · MIT 18.404J Lecture 2

What to learn:
- Regex syntax: ε, ∅, ∪, ·, *, parentheses
- Equivalence: regex ⇔ NFA ⇔ DFA (Kleene's theorem)

**Why we need it.** Problem 60 (EXPSPACE-completeness of REGEX equivalence) directly extends this to a complexity question. You'll also see "L(M) is regular?" questions, which require knowing what regular even means.

### 1d · Pumping lemma for regular languages
> Sipser §1.4 · MIT 18.404J Lecture 3

What to learn:
- The pumping lemma statement
- Using it to prove a language is **not** regular (classic: 0ⁿ1ⁿ)

**Why we need it.** REGULAR<sub>TM</sub> undecidability (Module 3, Problem 7) uses {0ⁿ1ⁿ} as its non-regular gadget. The construction only makes sense if you've already convinced yourself 0ⁿ1ⁿ is non-regular.

---

## 2 · Context-free languages — Sipser Chapter 2

### 2a · Context-free grammars (CFG)
> Sipser §2.1 · MIT 18.404J Lecture 3–4

What to learn:
- Production rules, variables vs terminals
- Derivations and parse trees
- L(G) = strings derivable from start variable

**Why we need it.** Module 1 problems A<sub>CFG</sub> and E<sub>CFG</sub> are about CFGs. The widget for A<sub>CFG</sub> uses the CYK parsing table, which requires CFGs in **Chomsky Normal Form** (Sipser §2.1 Theorem 2.9).

### 2b · Pushdown automata (PDA)
> Sipser §2.2 · MIT 18.404J Lecture 4

What to learn:
- PDA model: finite states + unbounded stack
- CFG ⇔ PDA equivalence (Sipser §2.2 Theorem 2.20)

**Why we need it.** Less central to our course, but the LBA (linear bounded automaton) in Module 3 — a Turing machine restricted to its input cells — is the natural in-between point between PDAs and TMs. Knowing PDAs makes LBAs intuitive.

### 2c · Non-context-free languages
> Sipser §2.3 · MIT 18.404J Lecture 5

What to learn:
- Pumping lemma for CFLs
- Classic non-CFL: {0ⁿ1ⁿ2ⁿ}

**Why we need it.** Module 3 problem ALL<sub>CFG</sub> uses the computation-history trick to encode TM runs in grammars; the analysis relies on knowing what CFGs can and cannot express.

---

## 3 · Turing machines — Sipser Chapter 3

### 3a · Turing machine definition
> Sipser §3.1 · MIT 18.404J Lecture 5–6

What to learn:
- Seven-tuple definition (Q, Σ, Γ, δ, q₀, q<sub>accept</sub>, q<sub>reject</sub>)
- Tape, head, transitions
- Configurations: (state, tape contents, head position)
- L(M) for Turing machines · accept / reject / loop
- **Decidable vs Turing-recognizable** languages — this is the single most important distinction in the course

**Why we need it.** Literally everything from Module 2 onward uses TMs. If you remember nothing else from Chapter 3, remember: a TM can halt-and-accept, halt-and-reject, or loop forever. A *decider* never loops. A *recognizer* may loop on rejected inputs.

### 3b · TM variants
> Sipser §3.2 · MIT 18.404J Lecture 6

What to learn:
- **Multi-tape TMs** — simulated by single-tape with quadratic time overhead
- **Nondeterministic TMs** — simulated by deterministic with exponential time overhead
- **Enumerators** — a TM that lists all strings in its language

**Why we need it.** Module 4 contrasts single-tape vs two-tape TMs for 0ⁿ1ⁿ. Module 5 defines NP using nondeterministic TMs. Module 7 uses log-space TMs as a variant with severely restricted resources.

### 3c · Church–Turing thesis
> Sipser §3.3 · MIT 18.404J Lecture 6

What to learn:
- Informal claim: "anything an algorithm can do, a TM can do"
- Why this lets us interchange "algorithm" and "Turing machine" in proofs
- The standard encoding ⟨M⟩ of a Turing machine as a string

**Why we need it.** The contradiction machine D in Module 2 is constructed in English ("on input ⟨M⟩: run H, flip the answer"), and we casually claim D is a TM. That casual claim is the Church–Turing thesis in action. Encodings ⟨M⟩ and ⟨M, w⟩ appear in every theorem statement from this point on.

---

## Quick checklist — what every student must be able to do day one

Before our Lecture 7, every student should be able to:

- [ ] Draw a DFA for "strings with an even number of 0s" and trace a 6-character input through it
- [ ] Convert an NFA with ε-transitions into an equivalent DFA via subset construction
- [ ] Write a regex for "strings ending in 01" and an equivalent NFA
- [ ] Prove {0ⁿ1ⁿ} is not regular using the pumping lemma
- [ ] Write a CFG for balanced parentheses and parse a small string via CYK
- [ ] Describe a Turing machine that decides {0ⁿ1ⁿ} — by hand, transition by transition
- [ ] Explain what it means for a language to be **Turing-recognizable but not decidable** (preview of A<sub>TM</sub>)
- [ ] Encode a small Turing machine as a binary string ⟨M⟩ (rough sketch is fine)

If you can do all eight, you're ready.

---

## Recommended self-study sequence (≈ 8 hours, before week 1)

| Day | Topics | Reading | Video |
|---|---|---|---|
| 1 | Sets, functions, languages, proofs | Sipser §0.2 + §0.4 | — |
| 2 | DFA + NFA + regex | Sipser §1.1–§1.3 | MIT L1 + L2 |
| 3 | Pumping lemma; CFG | Sipser §1.4 + §2.1 | MIT L3 |
| 4 | PDA; non-CFL | Sipser §2.2–§2.3 | MIT L4 + L5 |
| 5 | Turing machines + variants + Church-Turing | Sipser §3.1–§3.3 | MIT L5 + L6 |

The MIT videos are free at <https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/>.

---

## Notation conventions used throughout this course

| Symbol | Meaning |
|---|---|
| Σ | finite alphabet |
| Σ* | set of all finite strings over Σ |
| ε | empty string |
| \|w\| | length of string w |
| L | a language (subset of Σ*) |
| ⟨M⟩ | a fixed encoding of TM M as a string |
| ⟨M, w⟩ | encoding of (M, w) as a single string |
| L(M) | the language of TM M (or DFA/NFA/CFG/PDA) |
| A<sub>DFA</sub>, A<sub>TM</sub>, etc. | the membership-question language for that model |
| E<sub>DFA</sub>, E<sub>TM</sub>, etc. | the emptiness-question language |
| EQ<sub>DFA</sub>, EQ<sub>TM</sub>, etc. | the equivalence-question language |
| δ | transition function |
| ⊆ | subset · ⊊ proper subset |
| ≤<sub>p</sub>, ≤<sub>m</sub>, ≤<sub>T</sub> | polynomial, mapping, Turing reduction |

If any of these symbols feel unfamiliar, the corresponding chapter in Sipser introduces them on the first page.
