"""Narration scripts for the prerequisites page (prerequisites.html).

One file per topical section: intro, then § 0 through § 11.
Output goes to audio/p-{key}.mp3 to keep them separate from module audio.
"""

SCRIPTS = {

'intro': """
Welcome to the prerequisites page for our Computability and Complexity course.
This page covers everything you need to know before our first lecture. Our
course begins at Sipser chapter four and at MIT eighteen point four oh four J
lecture seven. So we assume you are already comfortable with finite automata,
context-free grammars, and Turing machines from Sipser chapters zero through
three. On this page you will find eleven short topics. For each one, a written
explanation, a hand-drawn diagram, a pointer to where in Sipser to read it, and
a link to the free MIT lecture video on OpenCourseWare. Read it top to bottom
in one sitting. By the end you will have all the vocabulary for our entire
semester. If two or more topics feel impossible, spend a day with Sipser
chapters zero through three before our first session. The total self-study
effort is about eight hours, spread comfortably across five days.
""",

'sets': """
Section zero, sets, functions, and languages. This is the floor of mathematical
notation that runs through everything in this course. A finite alphabet, written
sigma, is just a finite collection of symbols. The simplest alphabet is sigma
equals the set of zero and one. A string is a finite sequence of symbols from
sigma. The empty string is written epsilon. The set of all finite strings over
sigma is written sigma star, and includes epsilon, plus zero, one, then all the
two-symbol strings, three-symbol strings, and so on, infinitely. A language is
any subset of sigma star. Every algorithmic question in this course is, is this
string in this language. You also need to be comfortable with set operations.
Union, intersection, complement, and symmetric difference. The symmetric
difference of A and B is the set of strings on which A and B disagree. It is
the key to the equivalence test for DFAs in module one. You also need
functions. Injective means distinct inputs go to distinct outputs. Surjective
means every output value is hit. Bijective means both. Bijections will let us
prove two infinite sets are the same size, an idea used by Cantor in the most
important proof of computability theory. Spend about one hour reviewing Sipser
chapter zero, sections zero point two and zero point four.
""",

'dfa': """
Section one, deterministic finite automata, abbreviated DFA. A DFA is the
simplest computing model. Finitely many states, a read-only input head moving
left to right, and a deterministic transition function. Given a string, the DFA
processes one symbol at a time, following the transition arrow corresponding to
the current symbol. After reading the last symbol, the DFA either accepts the
string if it ends in an accept state, or rejects otherwise. Formally, a DFA is
a five-tuple. The state set Q, the alphabet sigma, the transition function delta
from Q cross sigma to Q, the start state q zero, and the set of accept states F.
The diagram on the page shows a DFA for strings with an even number of zeros.
Two states. State q zero is the accept state and means "even count so far".
State q one is the reject state and means "odd count so far". Each zero flips
between them, each one stays in place. Trace the string zero one zero one. You
start in q zero, read zero, go to q one, read one, stay in q one, read zero, go
to q zero, read one, stay in q zero. You end in q zero, an accept state, so
zero one zero one is accepted. DFAs are the simplest possible deciders. Module
one of our course uses them for the problems A-D-F-A, E-D-F-A, and E-Q-D-F-A.
Read Sipser section one point one. Watch MIT lecture one.
""",

'nfa': """
Section two, nondeterministic finite automata, or NFA. An NFA is a DFA with two
new freedoms. First, multiple edges can leave a state on the same symbol, and
the machine "guesses" which one to take. Second, the machine can take epsilon
transitions, moving between states without reading any input. An NFA accepts a
string if there exists some sequence of choices that leads to an accept state.
Surprisingly, NFAs are no more powerful than DFAs. Every NFA can be converted
to an equivalent DFA via the subset construction. Each DFA state is a subset of
NFA states. The DFA simulates "all possible current NFA states in parallel". For
an NFA with n states, the resulting DFA can have up to two to the n states,
exponential blow-up, but always finite. The diagram on the page shows a small
NFA for strings ending in zero one, with three states A, B, and C. The
equivalent DFA tracks subsets of these three NFA states. Starting from the set
containing only A, reading zero takes you to the set containing A and B, then
reading one takes you to the set containing A and C, which contains the NFA
accept state C and is therefore a DFA accept state. The "guess and verify" idea
behind nondeterminism appears throughout the course. It is the foundation of
the class NP in module five, and the class NL in module seven. Read Sipser
section one point two. Watch MIT lectures one and two.
""",

'regex': """
Section three, regular expressions. Regular expressions describe regular
languages using a compact algebra. Building blocks. The empty set, the empty
string epsilon, single characters from the alphabet. Operators. Union, written
as or; concatenation, written as juxtaposition or with a dot; and Kleene star,
which means "zero or more repetitions". Parentheses control grouping. For
example, the regex zero or one, star, zero one, means "any prefix of zeros and
ones, then exactly zero one". So it matches strings ending in zero one. Kleene's
theorem says that regular expressions, NFAs, and DFAs all recognize exactly the
same class of languages, the regular languages. This is a beautiful three-way
equivalence. You can convert a regex to an NFA by structural induction. Each
operator corresponds to a small NFA gadget. You can convert an NFA to a regex
by state elimination. The diagram on the page shows the three faces of regular
languages side by side. The algebraic regex on the left. The nondeterministic
machine in the middle. The deterministic machine on the right. All three
describe the language of strings ending in zero one. In our course, regular
expressions reappear in problem sixty, where the equivalence of regex with
squaring is shown to be EXPSPACE-complete. Read Sipser section one point
three. Watch MIT lecture two.
""",

'pumping': """
Section four, the pumping lemma. The pumping lemma is the standard tool for
proving a language is not regular. It says, every regular language has a
pumping length p such that every string in the language of length at least p
can be split into three parts, x, y, and z, where the middle part y is not
empty, and the prefix x y has length at most p. And here is the magic part. For
every non-negative integer i, the string x followed by y repeated i times
followed by z is also in the language. So you can pump the middle. To prove a
language is not regular, you assume it is regular, pick a long enough string,
and exhibit some value of i for which the pumped string is not in the
language, contradicting the assumption. The classic example is the language
zero to the n one to the n, strings of n zeros followed by n ones. We claim
this is not regular. Proof. Suppose it is regular with pumping length p. Take
the string w equals zero to the p one to the p. Then w decomposes as x, y, z
with x y of length at most p. So x and y both lie entirely in the prefix of
zeros. Pumping by i equals two adds extra zeros without adding ones,
breaking the matching count. The pumped string is not in the language.
Contradiction. The pumping lemma reappears in our course when we prove the
problem REGULAR-T-M undecidable, where the language zero to the n one to the n
is used as the non-regular gadget. Read Sipser section one point four. Watch
MIT lecture three.
""",

'cfg': """
Section five, context-free grammars, or CFGs. A CFG is a finite set of
production rules. Each rule rewrites a variable as a string of variables and
terminals. Terminals are the actual letters of the language. Variables are
intermediate symbols that get rewritten further. There is a designated start
variable. The language of the grammar is the set of strings made entirely of
terminals that can be derived from the start variable by repeated rule
application. The diagram on the page shows a CFG for balanced parentheses. The
start variable is S. The rules are S goes to open paren S close paren, S goes
to S S, and S goes to epsilon, the empty string. To derive the string open
paren open paren close paren close paren, we apply S goes to open paren S close
paren twice nested, then S goes to epsilon. The parse tree captures this. Each
internal node is a variable, each leaf is a terminal, and reading the leaves
left to right gives the derived string. CFGs are strictly more powerful than
regular expressions. They can express nested structure that regular expressions
cannot, such as balanced parentheses or palindromes. Every CFG can be converted
to Chomsky normal form, where every rule has either two variables on the right
side or a single terminal. Chomsky normal form is what the C-Y-K algorithm
needs, which we use in module one to decide the membership problem for CFGs in
polynomial time. Read Sipser section two point one. Watch MIT lectures three
and four.
""",

'pda': """
Section six, pushdown automata, or PDA. A PDA is a finite-state automaton
augmented with an unbounded LIFO stack. LIFO means last in, first out, like a
stack of plates. At each step, the PDA reads one input symbol or epsilon, can
optionally pop the top of the stack, can optionally push new symbols onto the
stack, and transitions to a new state. The diagram on the page shows a PDA
with an input tape on the left, a finite control in the middle, and a stack on
the right. The stack lets the PDA remember an unbounded amount of context,
which is exactly the power needed for nested structure. PDAs are equivalent in
power to context-free grammars. Every CFG can be converted to a PDA, and every
PDA can be converted to a CFG. So PDAs accept exactly the context-free
languages. Why are PDAs important for our course. Because the linear bounded
automaton model in module three, a Turing machine restricted to its input
tape, is the natural intermediate between PDAs and full Turing machines.
Knowing how a stack and a state machine combine prepares you for the more
elaborate computation history method we will study later. Read Sipser section
two point two. Watch MIT lecture four.
""",

'tm': """
Section seven, Turing machines, or TMs. A Turing machine is the full
computational model. It has a two-way infinite tape, a head that can read and
write one cell per step and move left or right, and a finite control with
designated accept and reject states. The diagram on the page shows a TM with
a tape extending in both directions, currently containing the string one zero
one zero, plus blank cells. The head sits over one specific cell. The finite
control reads the current cell and the current state, then according to the
transition function delta, writes a new symbol, transitions to a new state,
and moves the head one cell left or right. Formally, a TM is a seven-tuple.
States Q, input alphabet sigma, tape alphabet gamma, transition function delta,
start state q zero, accept state q accept, and reject state q reject. A TM has
three possible behaviors on a given input. It can halt and accept, halt and
reject, or run forever. The last possibility, looping, is the crucial twist
that separates Turing machines from finite automata and pushdown automata. A
TM that always halts decides its language. A TM that may loop on rejected
inputs only recognizes. This distinction is the heart of the entire course.
Read Sipser section three point one. Watch MIT lectures five and six.
""",

'variants': """
Section eight, Turing machine variants. The basic single-tape TM model is one
of several equivalent definitions. The variants look more powerful, but they
all recognize the same class of languages. Variant one. Multi-tape Turing
machines. These have k tapes, each with its own head, all controlled by a
single finite state. Multi-tape TMs can be simulated by single-tape TMs with
at most a quadratic time blow-up. Variant two. Nondeterministic Turing
machines. These allow multiple possible transitions from each state and
symbol. The machine accepts if any branch of the computation tree leads to
the accept state. Nondeterministic TMs can be simulated by deterministic TMs
with at most an exponential time blow-up. Variant three. Enumerators. These
are TMs that, rather than deciding membership in a language, print all the
strings of the language in some order. A language is Turing-recognizable if
and only if some enumerator enumerates it. All four variants recognize
exactly the same class of languages, the Turing-recognizable languages, also
called the recursively enumerable languages. The robustness of this class is
what makes the Turing machine the gold standard model of computation. Read
Sipser section three point two. Watch MIT lecture six.
""",

'ct': """
Section nine, the Church-Turing thesis. The Church-Turing thesis is an
informal claim, not a theorem. It says, anything that can be computed by an
algorithm can also be computed by a Turing machine. Equivalently, the class of
algorithmically solvable problems coincides exactly with the class of
TM-decidable problems. Why is it a thesis and not a theorem. Because the word
"algorithm" is intuitive and informal. There is no purely mathematical
definition of "algorithm" that can be proven equivalent to the Turing machine
model. Instead, the thesis is a working assumption, supported by the
historical fact that every formal model of computation people have ever
proposed, lambda calculus, recursive functions, register machines, cellular
automata, and many others, turns out to be Turing-equivalent in power. The
practical effect of the Church-Turing thesis on our course is that we can
describe Turing machines informally in English, as algorithms, and trust that
a fully formal TM construction exists in the background. So when we write a
proof like "the contradiction machine D, on input some encoding M, runs H on
M of M and flips the answer", we are leaning on the thesis when we casually
declare D is a Turing machine. Read Sipser section three point three. Watch
MIT lecture six.
""",

'enc': """
Section ten, encodings. A Turing machine is just a finite table of
transitions. So you can encode any Turing machine M as a binary string,
written as M between angle brackets. The encoding can be any reasonable
scheme. List the states, list the alphabet, list each transition in order,
separated by delimiters. Once a TM is a string, you can do something
extraordinary. You can feed one TM as input to another TM. This is the
foundation of the universal Turing machine, which we will study in detail
in module two. You can also encode pairs of objects. The encoded pair M
comma w between angle brackets is a single string that contains both the
encoding of M and the encoding of w, separated by a distinguishing marker.
We use such pair encodings to define languages like A-T-M, the set of all
encoded pairs M comma w such that M accepts w. These language-of-encodings
definitions make abstract questions like "does this program accept this
input" into well-defined membership questions, which Turing machines can
themselves potentially decide or recognize. Mastering encodings, even
informally, is the difference between getting lost and following the
proofs in module two. Read Sipser sections three point one and three
point three for the encoding ideas, woven throughout chapter three.
""",

'decrec': """
Section eleven, decidable versus Turing-recognizable. This is the single most
important distinction in the entire course. A Turing machine M decides a
language L if it always halts on every input, accepts every input that is in
L, and rejects every input that is not in L. M recognizes a language L if it
accepts every input in L, but is allowed to loop forever on inputs not in L.
The diagram on the page shows the two cases side by side. A decider always
gives a verdict, accept or reject. A recognizer can give three responses,
accept, reject, or loop forever. The class of decidable languages is also
called the recursive languages. The class of Turing-recognizable languages
is also called the recursively enumerable languages, or RE for short. Every
decidable language is recognizable. The reverse is not true. The famous
language A-T-M, all encoded pairs M, w such that M accepts w, is
Turing-recognizable, by the universal Turing machine. We will prove in
module two that it is not decidable, by a diagonal argument. The gap between
recognizable and decidable is the gap on which all of undecidability rests.
Every undecidability proof in this course exploits it. Hold this distinction
crisp in your head. Read Sipser section three point one and the introduction
to chapter four. Watch MIT lectures five and six. With this in hand, you are
ready for our first lecture.
""",

}

if __name__ == '__main__':
    import os
    out_dir = os.path.join(os.path.dirname(__file__), 'text')
    os.makedirs(out_dir, exist_ok=True)
    for key, text in SCRIPTS.items():
        clean = ' '.join(text.split())
        with open(os.path.join(out_dir, f'p-{key}.txt'), 'w') as f:
            f.write(clean)
    total = sum(len(' '.join(t.split())) for t in SCRIPTS.values())
    print(f'Wrote {len(SCRIPTS)} prerequisite scripts, {total:,} chars total')
    print(f'TTS cost (tts-1-hd at $0.030/1000): ${total / 1000 * 0.03:.2f}')
