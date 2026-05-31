"""Narration scripts for BCS 402 Computability and Complexity modules.

Each entry is a section of one module. Used by tts_generate.py to produce MP3s.
Keyed by (module_number, section_index_1based). Section index matches the order
of <section> elements in the corresponding module-N.html file.
"""

SCRIPTS = {

# =============================================================================
# MODULE 1 — Decidable problems for automata (Sipser §4.1)
# =============================================================================

(1, 1): """
Welcome to Module 1 of our Computability and Complexity course. In this module
we will explore the boundary between problems that can be solved by an algorithm
and problems that cannot. We start where the news is good — with finite automata
and context-free grammars, where almost every natural question turns out to be
decidable. The reason is simple: these models are restricted enough that we can
mechanically inspect their behavior in finite time. We will study five canonical
questions: does this DFA accept a particular string, is its language empty, do
two DFAs accept the same language, does a context-free grammar generate a given
string, and is the language of a context-free grammar empty. For each, we will
build the decider and watch it run on the interactive widget. By the end of the
module you should be fluent in saying out loud why each problem is decidable and
how the algorithm works. This sets up Module 2, where we move to Turing machines
and discover that the analogous questions become undecidable — a profoundly
different world.
""",

(1, 2): """
Our first decidable problem is A-D-F-A. The question is: given a deterministic
finite automaton B and an input string w, does B accept w? The answer is yes,
this is decidable, and the algorithm is delightfully simple. We just simulate
the DFA step by step on the string. Start in the initial state, read the first
symbol, follow the transition, repeat. After the last symbol, check whether the
current state is an accept state. The whole simulation runs in time proportional
to the length of w — linear time. Crucially, a DFA is finite. It has a bounded
number of states, no stack, no tape. So the simulation always terminates. The
interactive widget below lets you build a DFA, type in strings, and watch the
head move from state to state. Pay attention to how the input strip highlights
which character is being consumed at each step. This is the simplest possible
example of an algorithmic decider — a Turing machine that always halts with a
correct yes-or-no answer. Many of the harder problems we tackle later will be
reduced back to this one or one of its cousins.
""",

(1, 3): """
The second question is E-D-F-A: is the language of a DFA empty? In other words,
does this DFA accept any string at all? You might be tempted to enumerate
strings of length zero, one, two, and so on, and feed each into the simulator —
but that procedure never halts if the language is empty. We need a smarter
algorithm. The right idea is reachability. A DFA accepts at least one string if
and only if some accept state is reachable from the start state, following the
edges of the transition graph. So convert the DFA into a directed graph,
forget the labels for a moment, and run breadth-first search from the start
state. If you ever reach an accept state, the language is non-empty; otherwise
it is empty. This is a polynomial-time decider, in fact linear in the number of
states and transitions. The widget shows the reachability computation expanding
outward from the start state, lighting up cells as it discovers them. Watch how
the same trick will show up again later, in much more advanced settings — but
the core idea, search the configuration graph, never really changes.
""",

(1, 4): """
Our third decidable problem is E-Q-D-F-A: given two DFAs, do they accept the
same language? The classical algorithm uses the symmetric difference. The
languages of A and B are equal if and only if their symmetric difference is the
empty language. We can construct a DFA recognizing the symmetric difference
using a product construction. Take pairs of states, one from each DFA, and run
both in parallel; the pair is an accept state of the product if exactly one of
the two components is an accept state. Then we run our earlier E-D-F-A decider
on the product DFA. If the product accepts nothing, the symmetric difference is
empty, and the two DFAs are equivalent. The widget builds the product table
cell by cell. Each cell represents a joint configuration of the two machines.
Pay attention to how the product can be polynomial in size, even when the two
underlying DFAs are small — the product has size proportional to the product of
their state counts. This becomes important later when we discuss space
complexity and the cost of subset construction.
""",

(1, 5): """
Moving to context-free grammars, our fourth question is A-C-F-G: given a CFG G
and a string w, does G generate w? This is decidable, but it requires a bit
more work than the DFA case. The standard algorithm is C-Y-K, named after its
inventors Cocke, Younger, and Kasami. It works on grammars in Chomsky normal
form, where every rule has either two non-terminals or one terminal on the
right-hand side. C-Y-K fills in a triangular parsing table bottom-up: each
cell records which non-terminals can derive a particular substring of w. The
bottom row handles single characters; higher rows combine results from below
using the rules of the grammar. The string is in the language if and only if
the start symbol appears in the topmost cell. C-Y-K runs in time cubic in the
length of the string. The interactive widget animates the table filling in
diagonal by diagonal — a beautiful visual demonstration of dynamic programming
applied to language recognition. Note that for general grammars the problem
remains polynomial, but the constants and the algorithm are more involved.
""",

(1, 6): """
Our final decidable question for the module is E-C-F-G: is the language of a
context-free grammar empty? Once again, we need a clever algorithm because
enumerating all derivations does not terminate when the language is empty.
The right idea is to mark productive variables. A variable is productive if it
can derive at least one terminal string. We initialize the set of productive
variables to empty, then iterate: in each round, mark a variable as productive
if it has a rule whose right-hand side contains only terminals and already-
productive variables. Repeat until no new variables get marked. The grammar's
language is non-empty if and only if the start variable is productive at the
end. This is a polynomial-time decider — at most as many rounds as there are
variables, each round inspecting all rules. The widget walks through the
rounds, highlighting which variables flip from unmarked to productive at each
step. This idea — propagation rounds over a fixed set — will return when we
study reachability in directed graphs in Module 7.
""",

(1, 7): """
A short word about practice. The Sipser textbook chapter four point one has a
collection of exercises that map exactly onto the five problems we have just
covered. I strongly recommend you do at least exercises four point three,
four point five, and four point seven — they each strengthen a different
algorithmic intuition. Exercise four point three asks you to give a polynomial-
time decider for a variant of A-D-F-A. Exercise four point five is about
emptiness of two-way DFAs, which requires a small twist on the reachability
idea. Exercise four point seven asks you to prove decidability of a property
that is not in our list but follows the same pattern. As you do them, try to
write down, for each problem, both the algorithm and the running-time bound.
Knowing why each problem is decidable, and why the running time is what it
is, will make Module 2 — where almost nothing is decidable — much easier to
absorb.
""",

(1, 8): """
One-sentence summary of Module 1: every natural decision problem about finite
automata and context-free grammars is decidable in polynomial time, because
their behavior is finite enough to inspect mechanically. Hold that thought as
we now turn to Turing machines, where the situation reverses completely.
""",

# =============================================================================
# MODULE 2 — Undecidability and the halting problem (Sipser §4.2 + §5.1)
# =============================================================================

(2, 1): """
Welcome to Module 2. We begin with Cantor's diagonal argument, the single most
important idea in all of computability and complexity theory. Cantor's original
question was about real numbers: are there strictly more reals than naturals?
He proved yes, using a beautiful trick. Imagine someone hands you an alleged
list of all real numbers, one per row. You can always construct a new real
number that is not on the list by looking down the diagonal and flipping each
digit. The newly constructed number must differ from row i at position i, for
every i — so it cannot appear anywhere in the list. The list was incomplete.
Cantor concluded that no list of all reals can exist; the reals are uncountable.
Why does this matter for our course? Because the same trick will appear over
and over: to defeat a hypothetical universal solver, build a thing that disagrees
with it at its own diagonal. Today we apply it to Turing machines, in Module 7
we apply it to space hierarchies, and Gödel applied a sibling idea to arithmetic
provability. Watch the animation carefully — the diagonal flip is the engine of
half the negative results in this course.
""",

(2, 2): """
Now we switch gears to a positive result before delivering the bad news. We
want to show that A-T-M, the language of pairs ⟨M, w⟩ such that the Turing
machine M accepts the string w, is Turing-recognizable. Recognizable means
there is a Turing machine that accepts every yes-instance, even if it loops
forever on no-instances. The recognizer is just the universal Turing machine.
Given the description of M and the input w, the universal machine simulates M
step by step on w. If M halts and accepts, the universal machine accepts. If M
rejects, the universal machine rejects. If M loops forever, the universal
machine loops forever too, which is allowed for a recognizer. The widget below
shows the universal machine running a small example. Watch how the simulation
faithfully reproduces every step of M on its own tape. This positive result
sets up the punchline of the next section: A-T-M is recognizable, but it is not
decidable. The gap between those two notions is the gap between yes-instances
being recognizable and no-instances being recognizable too. Closing one half of
the gap, but not the other, is exactly what makes the halting problem so hard.
""",

(2, 3): """
Now the main event: A-T-M is undecidable. Suppose, for contradiction, that some
Turing machine H decides A-T-M. That means H always halts, and H accepts
⟨M, w⟩ if and only if M accepts w. We construct a new machine D as follows. On
input ⟨M⟩, D runs H on ⟨M, ⟨M⟩⟩ — that is, it asks H whether M accepts its own
description. If H says yes, D rejects. If H says no, D accepts. In other words,
D does the opposite of what M would do on its own description. Now we feed D
its own description: what does D do on ⟨D⟩? If D accepts ⟨D⟩, then by
construction H said D rejects ⟨D⟩ — so D rejects ⟨D⟩, contradicting our
assumption that D accepts. Symmetrically, if D rejects ⟨D⟩, then H said D
accepts ⟨D⟩, contradicting our assumption that D rejects. Either way we get a
contradiction. Therefore H cannot exist. This is the Cantor diagonal in
disguise: row M of an imagined acceptance matrix records whether M accepts
each input. D is the row that disagrees with every row at its own diagonal
entry. The widget walks the diagonal cell by cell, so you can see the
contradiction emerge concretely.
""",

(2, 4): """
Once we have one undecidable problem, we get many for free using reductions.
A reduction from problem A to problem B is a transformation that converts every
instance of A into an instance of B, preserving the yes/no answer. If we have
a reduction A reduces to B, and A is undecidable, then B is also undecidable —
because a decider for B would give us a decider for A. The classic example is
the halting problem H-A-L-T. We reduce A-T-M to H-A-L-T as follows. Given
⟨M, w⟩, build a new machine M-prime that on every input simulates M on w; if
M accepts, M-prime halts; if M rejects, M-prime enters an infinite loop. Then
⟨M, w⟩ is in A-T-M if and only if ⟨M-prime, anything⟩ is in H-A-L-T. A decider
for H-A-L-T would let us decide A-T-M, which we just proved is impossible.
H-A-L-T is therefore undecidable. The widget lets you build a small chain of
reductions and see how each new undecidable problem inherits its undecidability
from A-T-M. By the end of the course you'll have a whole zoo of undecidable
problems, all rooted in this one.
""",

(2, 5): """
Now the map of languages. Every language over a finite alphabet falls into one
of four regions: decidable, recognizable but not decidable, co-recognizable but
not decidable, and neither recognizable nor co-recognizable. Decidable is the
sweet spot — a Turing machine halts with the right answer on every input.
Recognizable is weaker — the machine accepts yes-instances but may loop on no-
instances. A-T-M lives here. Co-recognizable means the complement is
recognizable; the complement of A-T-M lives here. There is a critical theorem:
a language is decidable if and only if both it and its complement are
recognizable. This bridge theorem implies that the complement of A-T-M is not
recognizable — otherwise A-T-M would be decidable. So we have a concrete
example of a language that is neither recognizable nor co-recognizable: the
language E-Q-T-M, whose decision asks whether two Turing machines accept the
same language. The widget animates this Venn diagram and places each canonical
language in the correct region. Studying this picture is the cleanest way to
keep the recognizable-versus-decidable distinction straight in your head.
""",

(2, 6): """
A few words on practice. Sipser chapter four point two and chapter five point
one have many exercises that solidify these ideas. Try four point eleven —
prove a specific language is undecidable by reduction. Try four point twenty —
classify a list of languages into our four regions. Try five point one — show a
problem about context-free grammars is undecidable, which requires a more
elaborate reduction. The single most important habit to develop is this: when
you see a new problem, ask yourself whether it is recognizable, decidable,
neither, or both. Then try to fit it into the diagonal-plus-reductions
framework. Most problems you'll meet professionally either trivially decide
themselves or trace back to A-T-M.
""",

(2, 7): """
One-sentence summary of Module 2: the diagonal argument proves that A-T-M is
undecidable, and once we have one undecidable problem we generate many more by
reduction. Hold that thought as we explore deeper undecidability results next.
""",

# =============================================================================
# MODULE 3 — Reductions, recursion theorem, Rice (Sipser §5.1 + §6.1 + §6.3)
# =============================================================================

(3, 1): """
Welcome to Module 3. We start with the computation history method, a tool that
lets us prove undecidability for problems where the simple A-T-M-to-X reduction
does not directly work. A computation history is a list of configurations of a
Turing machine, one per time step, showing the entire trace of a run. We can
encode a Turing machine's execution as a sequence of these configurations.
The key insight is that an accepting history must satisfy local consistency:
each configuration must follow legally from the previous one according to the
transition function. We can construct gadgets — small grammars or small linear
bounded automata — that recognize exactly the strings that fail to encode a
valid accepting history. If accepting M on w is undecidable, then deciding
whether the gadget accepts everything is also undecidable. This trick gives us
undecidability for a host of language-theoretic problems that would otherwise
be hard to handle directly. The widget shows a computation history forming row
by row for a small machine — pay attention to how local windows of two
consecutive rows encode the transition.
""",

(3, 2): """
A linear bounded automaton, or L-B-A, is a Turing machine that is only allowed
to use the cells of tape originally occupied by the input. No expansion onto
fresh tape — strictly bounded in space by the input length. L-B-As are
strictly more powerful than push-down automata and strictly weaker than full
Turing machines. There is a surprising positive result: A-L-B-A, the
acceptance problem for linear bounded automata, is decidable. The decider is
based on configuration counting. An L-B-A on input of length n has at most
some polynomial number of configurations — bounded by the product of the
number of states, tape alphabet size raised to n, and head positions. If the
machine runs for longer than this many steps, it must repeat a configuration,
which means it will loop forever. So we simulate the L-B-A for that many steps;
if it has not halted, we know it loops, and we reject. This sounds easy, but
the configuration count grows exponentially in n, so the decider runs in
exponential time — decidable but expensive.
""",

(3, 3): """
Now the negative result for L-B-As: E-L-B-A is undecidable. The question E-L-B-A
asks whether the language of an L-B-A is empty. This is undecidable, and the
proof uses the computation history trick. Given ⟨M, w⟩, an instance of A-T-M,
we construct an L-B-A B that on its input checks whether the input encodes an
accepting computation history of M on w. B accepts a string if and only if
that string is exactly such a history. So the language of B is empty if and
only if M does not accept w. A decider for E-L-B-A would therefore decide
A-T-M, which is impossible. The widget animates the construction of B's
checking procedure, walking through how local consistency between consecutive
configurations is verified using bounded tape. The key technical fact is that
the check fits within the linear space bound of an L-B-A — that's why we used
an L-B-A rather than a finite automaton here.
""",

(3, 4): """
A similar trick proves that A-L-L-C-F-G is undecidable. A-L-L-C-F-G asks
whether a given context-free grammar generates every possible string over its
alphabet — that is, whether L of G equals sigma-star. This is undecidable. The
proof again uses computation histories. We build a context-free grammar that
generates every string except those that encode accepting histories of M on w.
The grammar handles failures of local consistency between consecutive
configurations and emits anything that violates at least one local rule. So the
grammar generates everything if and only if M does not accept w. A decider for
A-L-L-C-F-G would decide A-T-M, contradiction. The reason we use a grammar
rather than an L-B-A here is that we want to generate the complement of valid
histories, and context-free grammars are good at expressing union-of-violations.
This pair of results, E-L-B-A and A-L-L-C-F-G, shows that even modest extensions
of automata get us into undecidable territory the moment we ask about full
languages rather than single strings.
""",

(3, 5): """
Now one of the most beautiful theorems in computability: the recursion theorem.
Informally, it says that any program can access its own description as if it
were data, and use that description to compute. So programs that print
themselves — quines — exist not as parlor tricks but as a special case of a
general theorem. The proof builds a fixed point: given any computable function
t that transforms programs to programs, there is a program p such that p and
t of ⟨p⟩ compute the same function. This lets us prove undecidability results
elegantly. For example, to prove A-T-M undecidable, we can use the recursion
theorem: assume a decider H for A-T-M, then build a program M-prime that
consults H on ⟨M-prime⟩ and does the opposite. Recursion theorem guarantees
such an M-prime exists. The widget walks through building a quine, layer by
layer. Pay attention to the data-code split: every quine contains a piece of
data describing its code, and a piece of code that prints both the data and
itself reconstructed from the data.
""",

(3, 6): """
Rice's theorem is the grand generalization of many earlier undecidability
results. It says: any non-trivial property of the language of a Turing machine
is undecidable. Non-trivial means there exists at least one Turing machine
whose language has the property and at least one whose language does not. A
property of the language means the property depends only on the function the
machine computes, not on the syntactic details of its description. So
"the language is empty", "the language is regular", "the language contains the
string hello", "the language is decidable" — all of these are undecidable
properties because they are non-trivial and semantic. The proof is a slick
reduction from A-T-M. Given ⟨M, w⟩, build a new machine M-prime whose language
has the property if and only if M accepts w. A decider for the property would
decide A-T-M. The widget lets you check a list of candidate properties and
predict which are Rice-style and therefore undecidable, versus which are
syntactic and decidable. Mastering Rice's theorem is the single most useful
shortcut for undecidability proofs.
""",

(3, 7): """
Sipser five point one, six point one, and six point three contain the
exercises that build the techniques in this module. The most important ones
are five point twenty-eight, six point ten, and six point eighteen. Five
point twenty-eight asks you to apply the computation history method to a new
problem. Six point ten asks you to build a quine in a real programming
language. Six point eighteen asks you to apply Rice's theorem and to identify
exactly which non-trivial properties are involved. As you do them, watch how
the same three tools — diagonal, reduction, recursion theorem — keep coming
back in different costumes.
""",

(3, 8): """
One-sentence summary of Module 3: the computation history method, the
recursion theorem, and Rice's theorem are the three power tools of advanced
undecidability — together they reduce almost any semantic question about
Turing machines to the halting problem.
""",

# =============================================================================
# MODULE 4 — Time complexity (Sipser §7.1 + §7.2)
# =============================================================================

(4, 1): """
Welcome to Module 4. We pivot from "what can be computed in principle" to
"what can be computed efficiently". The first question is, how do we measure
efficiency? The natural answer is running time as a function of input length.
But raw step counts depend on the model — a single-tape Turing machine is
slower than a multi-tape one — and we want a coarse classification that is
robust to such variations. The standard solution is Big-O notation, which
discards constants and lower-order terms, focusing on growth rate. The widget
in this section lets several growth rates race on the same axis: logarithmic,
linear, n log n, quadratic, cubic, and exponential. You can switch between
linear and logarithmic scales to see how dramatically the curves diverge.
Exponential growth eventually dominates every polynomial, no matter how steep.
This intuition is the foundation of why we cherish polynomial-time algorithms
and dread exponential ones — even though "polynomial" is a wide net that
includes algorithms running in n to the hundred, in practice the polynomial
versus exponential boundary is where computational feasibility actually lives.
""",

(4, 2): """
Big-O notation, formally: f of n is O of g of n if there exist constants c and
n-naught such that for every n at least n-naught, f of n is at most c times g
of n. In plain words, eventually f is bounded above by g, up to a multiplicative
constant. Big-O cares about asymptotics, not specific values. So three n squared
plus 100 n plus 5000 is O of n squared, because for large n the n squared term
dominates. Related notations are little-o, Big-Omega, and Big-Theta. Big-Omega
is a lower bound; Big-Theta means tight matching upper and lower bounds. These
are the language we will speak for the rest of the course. The widget here
classifies polynomial expressions you type — pick out the dominant term and
declare the Big-O class. Practice with the widget until you can do this in
your head for any expression. Note one subtle pitfall: Big-O is an upper bound,
not an exact statement. So saying an algorithm runs in O of n squared just
means it never runs longer than that asymptotically; it might actually run
faster in practice.
""",

(4, 3): """
A concrete time-complexity case study: the language zero-to-the-n one-to-the-n.
Strings of n zeros followed by n ones. A single-tape Turing machine deciding
this language has to pair off zeros with ones. The natural algorithm sweeps
left to right, crosses off a zero, sweeps to the matching one and crosses it
off, returns left, and repeats. Each pair of zero and one takes a linear sweep
across the input, so the total time is quadratic in the input length. The
widget animates this sweep on a tape. You can watch the head bounce back and
forth, with the step counter clicking up. Pay attention to where the step
count actually accumulates: most of the cost is in the long sweeps, not in the
crossings-off themselves. This is a foundational result: single-tape Turing
machines pay quadratic time even for tasks that feel like they should be
linear, because the head can only move one cell per step.
""",

(4, 4): """
The model matters more than you might think. The same language zero-to-the-n
one-to-the-n is decidable in linear time on a two-tape Turing machine. Copy the
zeros onto the second tape, then scan the input ones while popping zeros off
the second tape — both heads move in their natural direction, no sweeping back
and forth. The widget races a single-tape simulator against a two-tape one on
the same input. The single-tape machine's step count crawls upward, while the
two-tape machine finishes in a single linear pass. A classical theorem of
Hennie and Stearns: every k-tape Turing machine can be simulated by a single-
tape Turing machine with quadratic time overhead. So the gap between single
and multi-tape is at most quadratic — they are polynomially equivalent. This
is one reason we define classes like P in terms of polynomial time on any
reasonable model: the model details get washed out by the polynomial closure.
""",

(4, 5): """
The class P consists of all languages decidable in polynomial time on a
deterministic Turing machine. P is the canonical class of efficiently decidable
problems. It is robust: it does not matter whether you use single-tape,
multi-tape, RAM machines, or any sensible variant — the class is the same.
Classic examples in P include graph reachability via breadth-first search,
greatest common divisor via Euclid's algorithm, and membership in any context-
free language via C-Y-K. The widget showcases three classical P algorithms,
each annotated with its polynomial running time. P is generally considered
"the class of tractable problems," with the understanding that some polynomials
are still impractically large. The famous open question P versus N-P asks
whether problems that can be verified in polynomial time can also be solved in
polynomial time. We turn to N-P in the next module, but the foundation we have
built here — Big-O, multi-tape simulation, robustness of P — is exactly what
makes that question well-defined.
""",

(4, 6): """
Practice for Module 4 comes from Sipser sections seven point one and seven
point two. Exercises to do: seven point five, which exercises Big-O
classification; seven point thirteen, which constructs a polynomial-time
algorithm for a graph problem; and seven point twenty, which is a meta-question
about the closure properties of P. As you work through them, build an internal
library of "P-style" algorithms — graph search, dynamic programming, divide
and conquer, table look-up. When you encounter a new problem, your first move
should be to check whether one of these techniques can dispatch it in
polynomial time.
""",

(4, 7): """
One-sentence summary of Module 4: time complexity is measured in Big-O of the
input length, and the class P captures problems decidable in polynomial time
on any reasonable Turing machine model.
""",

# =============================================================================
# MODULE 5 — NP, NP-completeness, Cook-Levin (Sipser §7.3 to §7.5)
# =============================================================================

(5, 1): """
Welcome to Module 5. We have just seen the class P. Now we meet its more
mysterious sibling, N-P. A problem is in N-P if it has a polynomial-time
verifier: there exists a Turing machine V that takes the original input plus a
short witness, and accepts in polynomial time exactly when the original input
is a yes-instance, for some witness. So N-P is the class of problems where
finding the answer might be hard, but checking a proposed answer is easy. The
quintessential example is the Boolean satisfiability problem, S-A-T. Given a
formula, finding a satisfying assignment can be very hard. But given a candidate
assignment, plugging it in and checking is trivially linear time. The widget
in this section contrasts a polynomial-time verifier with a brute-force solver
that enumerates the exponential space of assignments. The verifier finishes
instantly; the solver crawls. This finding-versus-checking gap is the heart of
the P versus N-P question: are all problems whose answers can be checked
quickly also problems whose answers can be found quickly?
""",

(5, 2): """
S-A-T, the Boolean satisfiability problem, is the canonical N-P problem. We
take a Boolean formula in conjunctive normal form — a big AND of clauses, each
clause being an OR of literals — and ask whether some truth assignment to the
variables makes the entire formula true. The widget lets you click variables to
flip them, and the clauses light up green or red showing whether they are
satisfied. There's also an auto-solver that enumerates all two-to-the-n
assignments and announces what fraction of them satisfy the formula. The
companion problem 3-S-A-T restricts each clause to exactly three literals.
3-S-A-T is just as hard as S-A-T — there is a polynomial-time reduction from
S-A-T to 3-S-A-T using auxiliary variables to split long clauses. 3-S-A-T is
the workhorse of N-P-completeness proofs because its simple structure makes
gadget constructions easier. We will use 3-S-A-T many times in this module.
""",

(5, 3): """
Cook–Levin, proven independently by Stephen Cook in 1971 and Leonid Levin
shortly after, is the founding theorem of N-P-completeness. It says: S-A-T is
N-P-complete. That means every N-P problem reduces in polynomial time to
S-A-T. The proof is constructive and beautiful. Given any N-P language L with
verifier V running in polynomial time t of n, and an input x, we build a
Boolean formula phi-x in polynomial time such that phi-x is satisfiable if and
only if x is in L. The formula encodes a tableau — a grid where each row is a
configuration of the verifier V at one time step. The grid has t of n rows and
t of n columns; each cell stores one tape symbol or state. Local consistency
clauses ensure that every 2-by-3 window of the grid reflects a legal transition
of V. The widget animates the tableau filling in step by step, and highlights
the 2-by-3 windows that become S-A-T clauses. Once Cook–Levin is in your hand,
every other N-P-completeness proof in the course is a reduction starting from
S-A-T or one of its descendants.
""",

(5, 4): """
The N-P-completeness story spreads outward from S-A-T via reductions. We will
walk through the classical chain: S-A-T reduces to 3-S-A-T using auxiliary
variables to break long clauses. 3-S-A-T reduces to C-L-I-Q-U-E by building a
graph whose vertices are literal occurrences and whose edges connect
compatible literals across different clauses. C-L-I-Q-U-E reduces to V-E-R-T-E-X-
C-O-V-E-R by taking complement graphs. 3-S-A-T reduces to S-U-B-S-E-T-S-U-M by
encoding satisfiability as an arithmetic equation with carefully designed digit
positions. 3-S-A-T reduces to H-A-M-P-A-T-H by clever gadgets that route a
Hamiltonian path through a graph if and only if the formula is satisfiable.
And 3-S-A-T reduces to 3-C-O-L-O-R by gadgets that force a three-coloring of
a graph to encode a satisfying assignment. Each of these reductions is a small
masterpiece. The widget walks through them step by step, showing the gadget
constructions. Once you see them, you can recognize gadget-based reductions in
the wild.
""",

(5, 5): """
Let us zoom out. The full map so far: P is inside N-P, which is inside P-S-P-A-
C-E, which is inside E-X-P-T-I-M-E. We know strict separations P inside E-X-P-
T-I-M-E and P inside E-X-P-S-P-A-C-E by hierarchy theorems we will see later.
We do not know whether P equals N-P. We do not know whether N-P equals P-S-P-
A-C-E. We do not know whether P-S-P-A-C-E equals E-X-P-T-I-M-E. These three
open questions are arguably the most important problems in theoretical computer
science. The Clay Millennium Prize offers a million dollars for the first.
N-P-complete problems sit at the top of N-P, hardest to break out of. If even
one N-P-complete problem were in P, all of N-P would collapse into P. So far
no such breakthrough — despite hundreds of N-P-complete problems and decades
of intense effort, the boundary between P and N-P remains intact.
""",

(5, 6): """
Practice for Module 5 lives in Sipser seven point three through seven point
five. The must-do exercises are seven point seventeen — verifier construction
for a specific N-P problem; seven point twenty-one — reduction from 3-S-A-T
to a less famous N-P-complete problem; and seven point thirty — a meta-question
about the closure of N-P under various operations. As you do them, internalize
the three step proof template for N-P-completeness: show the problem is in
N-P by giving a polynomial-time verifier; then reduce a known N-P-complete
problem to it; then conclude.
""",

(5, 7): """
One-sentence summary of Module 5: N-P captures problems with polynomial-time
verifiers; Cook–Levin proves S-A-T is N-P-complete; and the entire family of
N-P-complete problems is connected by polynomial-time reductions starting from
S-A-T.
""",

# =============================================================================
# MODULE 6 — Space, PSPACE, games (Sipser §8.1 to §8.3)
# =============================================================================

(6, 1): """
Welcome to Module 6. We shift from time to space. A Turing machine's space
complexity is the number of tape cells it uses, as a function of input length.
This is a different resource from time. A machine can use very little space
yet run for a long time, or vice versa. The relationship is: space at most t
of n implies time at most some exponential of space, because a machine
running in space s of n has at most exponential-in-s distinct configurations,
and it cannot revisit a configuration without looping. So time and space are
related, but loosely. We define analogues of P and N-P based on space:
P-S-P-A-C-E is the class of languages decidable in polynomial space,
N-P-S-P-A-C-E is the same with nondeterminism, L is logarithmic space, and
N-L is nondeterministic logarithmic space. The widget here charts a few
classic algorithms by their time and space requirements, so you can see the
two resources visually decoupled.
""",

(6, 2): """
Savitch's theorem is the surprise result of space complexity. It says: for any
function f of n at least log n, N-S-P-A-C-E of f is contained in S-P-A-C-E of
f squared. In particular, P-S-P-A-C-E equals N-P-S-P-A-C-E — nondeterminism
gives no real benefit in polynomial space. This is the opposite of the time
situation, where N-P versus P is wide open and most people believe they differ.
The proof is a clever recursion. We want to check whether configuration A
reaches configuration B in t steps. We try every possible intermediate
configuration M and recursively check whether A reaches M in t-over-2 steps
and whether M reaches B in t-over-2 steps. The recursion depth is log of t,
and we reuse the same scratch space at each level — giving an f-squared
overhead. The widget animates the recursion tree, highlighting how only a
single root-to-leaf path lives on the stack at any moment.
""",

(6, 3): """
Now T-Q-B-F, the canonical P-S-P-A-C-E-complete problem. T-Q-B-F stands for
true quantified Boolean formula. A quantified Boolean formula has the shape
there exists x-1, for all x-2, there exists x-3, alternating quantifiers, then
a propositional formula in the variables. The question: is this whole thing
true? T-Q-B-F is P-S-P-A-C-E-complete, meaning every P-S-P-A-C-E problem
reduces to it in polynomial time, and T-Q-B-F itself is in P-S-P-A-C-E. To
decide T-Q-B-F, you evaluate the formula in a depth-first manner: when you
hit an existential quantifier, try both values; for the universal, both must
hold; recurse. The recursion depth is the number of variables, polynomial in
the input, and only one branch lives on the stack at a time. The widget
animates this game-tree evaluation. Note that T-Q-B-F has a natural game-
theoretic flavor: existential quantifiers are the existential player making
moves, universal quantifiers are the universal player; the formula is true if
and only if the existential player has a winning strategy.
""",

(6, 4): """
Generalized geography is a beautiful playable example of a P-S-P-A-C-E-complete
problem. Two players alternate; the current player must move from the current
vertex to an unused neighbor; the player who cannot move loses. Determining
whether the starting player has a winning strategy is P-S-P-A-C-E-complete.
The reduction from T-Q-B-F is one of the more elegant constructions in the
field: gadgets encode existential and universal quantifiers as alternating
moves in the game graph. The widget lets you play generalized geography
against the computer; you can also visualize the game tree, with each branch
representing a possible play. Many natural games turn out to be P-S-P-A-C-E-
complete or harder: generalized chess, hex, checkers, Othello. The deep
intuition is that P-S-P-A-C-E corresponds exactly to two-player perfect-
information games of polynomial-depth move sequences.
""",

(6, 5): """
Zooming out: the big map at this point. P is inside N-P is inside P-S-P-A-C-E,
and P-S-P-A-C-E equals N-P-S-P-A-C-E by Savitch. P-S-P-A-C-E is inside E-X-P-
T-I-M-E. We know P is strictly inside E-X-P-T-I-M-E by the time hierarchy
theorem, which we will see in the next module. So at least one of the
containments P inside N-P, N-P inside P-S-P-A-C-E, P-S-P-A-C-E inside E-X-P-
T-I-M-E must be strict — but we cannot tell you which one. This is one of the
most striking gaps in our understanding of computation. The widget visualizes
this nested-circles picture, with classic problems placed at the right level.
N-P-complete problems sit at the boundary of N-P; P-S-P-A-C-E-complete problems
sit at the boundary of P-S-P-A-C-E. Both kinds of completeness give us proxy
measures of how hard a class actually is.
""",

(6, 6): """
Practice for Module 6 comes from Sipser eight point one through eight point
three. Must-do exercises: eight point eight on the space cost of specific
algorithms; eight point twenty on N-P-S-P-A-C-E containment; and eight point
twenty-six on T-Q-B-F gadgets. As you do them, build the habit of asking,
for every new algorithm, "what does it use, time or space?" — and notice how
often the answer is "much less space than time."
""",

(6, 7): """
One-sentence summary of Module 6: P-S-P-A-C-E equals N-P-S-P-A-C-E by Savitch,
and T-Q-B-F is the canonical P-S-P-A-C-E-complete problem, corresponding to
two-player games.
""",

# =============================================================================
# MODULE 7 — L, NL, hierarchy theorems (Sipser §8.4 + §9.1)
# =============================================================================

(7, 1): """
Welcome to Module 7, the final lecture. We zoom in on the lowest reaches of
space complexity. L is the class of languages decidable in logarithmic space.
N-L is the same with nondeterminism. Logarithmic space is enough to store a
constant number of pointers into the input, but not a full copy of it. The
input is on a separate read-only tape — we never count input space. Classic
problems in L include palindrome checking and A-D-F-A. A classic problem in
N-L is graph reachability P-A-T-H: given a directed graph and two vertices,
is there a path from start to end? Nondeterministically, we guess the path
one vertex at a time and only remember the current vertex — that's log n
space. The widget lets you decide A-D-F-A in log space, by storing only a
pointer to the input head and the current DFA state. Watch how minimal the
working memory really is — just a couple of pointers.
""",

(7, 2): """
P-A-T-H is N-L-complete. That means every N-L problem reduces to P-A-T-H via
a log-space reduction, and P-A-T-H itself is in N-L. The reduction is
particularly elegant: take any N-L machine M and input w, and build the
configuration graph of M on w. Each configuration is a node, with edges
representing single steps. M accepts w if and only if there is a path from
the start configuration to the accept configuration in this graph. The graph
has polynomial size, and we can construct it in log space because each
configuration is described by a log-number of bits. So P-A-T-H is at least as
hard as everything in N-L. The widget animates the configuration graph
construction and shows the reduction running on a small example. N-L-complete
problems are the analog of N-P-complete problems, but at the log-space level.
""",

(7, 3): """
Immerman and Szelepcsényi independently proved a stunning result in 1987–88:
N-L equals co-N-L. That is, the class of languages decidable in nondeterministic
log space is closed under complement. This was unexpected because the
analogous question for time, N-P versus co-N-P, is widely believed to be
"no, they differ". The proof uses inductive counting. We count the number of
reachable vertices from the start at each distance i. Knowing the count c-i,
we can certify in N-L that a particular vertex v is not reachable: enumerate
all c-i candidate reachable vertices, verify each one, and confirm v is not
among them. The widget walks through this counting argument step by step,
showing the reachability sets R-zero, R-one, R-two expanding, and the
certificates that prove non-reachability. The technique reappears later in
many surprising places.
""",

(7, 4): """
The hierarchy theorems are the only unconditional separation results in
complexity theory. They say: more time gives strictly more power, and more
space gives strictly more power, provided the increases are large enough. The
time hierarchy theorem says TIME of t is strictly inside TIME of t times log
t, for any reasonable t. The space hierarchy theorem says SPACE of s is
strictly inside SPACE of s times log s. The proofs are Cantor-style
diagonalizations. We enumerate all machines of the smaller class, then build a
machine in the larger class that disagrees with each one on its own
description. The diagonal machine is in the larger class because we have just
enough extra resource to simulate the smaller-class machine. The widget walks
the diagonal in the same style as Module 2's diagonal-against-Turing-machines.
Consequences: P strictly inside E-X-P-T-I-M-E, L strictly inside P-S-P-A-C-E,
and N-L strictly inside P-S-P-A-C-E. These are the few separations we can
actually prove.
""",

(7, 5): """
Now the full map of complexity classes we have built. L inside N-L inside P
inside N-P inside P-S-P-A-C-E equals N-P-S-P-A-C-E inside E-X-P-T-I-M-E
inside N-E-X-P-T-I-M-E inside E-X-P-S-P-A-C-E. Within these we have strict
separations: L is strictly inside P-S-P-A-C-E, P is strictly inside E-X-P-T-I-
M-E, P-S-P-A-C-E is strictly inside E-X-P-S-P-A-C-E. All other separations
between adjacent levels remain open. N-L equals co-N-L by Immerman–
Szelepcsényi, but L versus N-L is open. The widget shows the entire zoo with
classic problems placed at each level: A-D-F-A in L, P-A-T-H in N-L, primes
in P, S-A-T in N-P, T-Q-B-F in P-S-P-A-C-E, and so on. This is the picture
to carry around in your head whenever someone says "this problem is in
class X" — fit it into the zoo and you'll know roughly how hard it is.
""",

(7, 6): """
Practice for Module 7 lives in Sipser eight point four and nine point one.
Must-do exercises: eight point thirty-four for log-space reductions; nine
point five for the time hierarchy theorem on specific functions; nine point
eleven for the space hierarchy theorem and its consequences. As you do them,
appreciate that hierarchy theorems are the rare wins of complexity theory —
proofs are constructive, results are unconditional, and they give us the only
firm landmarks on the otherwise foggy P-versus-N-P map.
""",

(7, 7): """
One-sentence summary of the entire course: computability draws the line
between possible and impossible algorithms, complexity draws the lines between
fast, slow, and infeasible — and almost every interesting line between
complexity classes remains, even after fifty years, an open mystery.
""",

}

if __name__ == '__main__':
    import os, sys
    out_dir = os.path.join(os.path.dirname(__file__), 'text')
    os.makedirs(out_dir, exist_ok=True)
    total_chars = 0
    for (m, s), txt in SCRIPTS.items():
        # Clean up the script: strip leading/trailing whitespace, collapse spaces
        clean = ' '.join(txt.split())
        path = os.path.join(out_dir, f'm{m}-s{s}.txt')
        with open(path, 'w') as f:
            f.write(clean)
        total_chars += len(clean)
    print(f'Wrote {len(SCRIPTS)} script files to {out_dir}')
    print(f'Total characters: {total_chars:,}')
    print(f'Estimated TTS cost (tts-1-hd at $0.030/1000 chars): ${total_chars / 1000 * 0.03:.2f}')
