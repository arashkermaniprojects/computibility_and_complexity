"""Algorithm flowchart SVGs — one per major algorithm in modules 1-3.

Each diagram visualizes the steps in an algorithm callout, showing input flowing
through processing boxes with arrows and output. Style matches existing diagrams.
"""

# ============================================================
# Module 1 — Automata algorithms
# ============================================================

ALGO_ADFA = """
<figure class="diagram">
  <svg viewBox="0 0 640 220" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <defs>
      <marker id="arr-adfa" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto">
        <polygon points="0 0, 9 3, 0 6" fill="var(--accent)"/>
      </marker>
    </defs>
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      A<tspan baseline-shift="sub" font-size="0.75em">DFA</tspan> decider · simulate B on w step by step
    </text>
    <!-- Input -->
    <rect x="30" y="80" width="100" height="60" rx="8" fill="white" stroke="var(--info, #2f60a8)" stroke-width="2"/>
    <text x="80" y="105" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="13" font-weight="700" fill="var(--info, #2f60a8)">⟨B, w⟩</text>
    <text x="80" y="124" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" fill="#666">DFA + string</text>
    <!-- Arrow -->
    <path d="M 132,110 L 180,110" stroke="var(--accent)" stroke-width="2" marker-end="url(#arr-adfa)"/>
    <!-- Step 1 -->
    <rect x="185" y="80" width="120" height="60" rx="8" fill="#fff" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2"/>
    <text x="245" y="100" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="var(--accent-strong, #1c4a3f)">Parse ⟨B⟩</text>
    <text x="245" y="118" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">load states, δ,</text>
    <text x="245" y="132" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">start q₀, accepts F</text>
    <!-- Arrow -->
    <path d="M 307,110 L 355,110" stroke="var(--accent)" stroke-width="2" marker-end="url(#arr-adfa)"/>
    <!-- Step 2 -->
    <rect x="360" y="80" width="140" height="60" rx="8" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="2"/>
    <text x="430" y="100" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="var(--gold)">Simulate on w</text>
    <text x="430" y="118" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="11" fill="#666">q ← δ(q, w[i])</text>
    <text x="430" y="132" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">for i = 0..|w|-1</text>
    <!-- Arrow -->
    <path d="M 502,110 L 550,110" stroke="var(--accent)" stroke-width="2" marker-end="url(#arr-adfa)"/>
    <!-- Output -->
    <rect x="555" y="80" width="65" height="60" rx="8" fill="#fff" stroke="var(--warn-strong, #b95825)" stroke-width="2"/>
    <text x="587" y="100" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="var(--warn-strong, #b95825)">q ∈ F ?</text>
    <text x="587" y="118" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="12" fill="var(--accent-strong, #1c4a3f)">✓ / ✗</text>
    <!-- Bottom -->
    <text x="320" y="180" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-style="italic" fill="#666">
      Linear time in |w|. The DFA is finite, so the simulation always halts.
    </text>
  </svg>
  <figcaption>A<sub>DFA</sub> is decided by a Turing machine that simply <em>simulates</em> the DFA on the given string. Read the description, set up the state, walk the string symbol-by-symbol, then check if the final state is in F.</figcaption>
</figure>
"""

ALGO_EQDFA = """
<figure class="diagram">
  <svg viewBox="0 0 640 260" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <defs>
      <marker id="arr-eqdfa" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto">
        <polygon points="0 0, 9 3, 0 6" fill="var(--accent)"/>
      </marker>
    </defs>
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      EQ<tspan baseline-shift="sub" font-size="0.75em">DFA</tspan> decider · product construction + emptiness test
    </text>
    <!-- Input pair -->
    <rect x="20" y="100" width="80" height="50" rx="6" fill="white" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2"/>
    <text x="60" y="125" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="13" font-weight="700" fill="var(--accent-strong, #1c4a3f)">DFA A</text>
    <text x="60" y="142" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">states Q<tspan baseline-shift="sub" font-size="0.7em">A</tspan></text>

    <rect x="20" y="160" width="80" height="50" rx="6" fill="white" stroke="var(--info, #2f60a8)" stroke-width="2"/>
    <text x="60" y="185" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="13" font-weight="700" fill="var(--info, #2f60a8)">DFA B</text>
    <text x="60" y="202" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">states Q<tspan baseline-shift="sub" font-size="0.7em">B</tspan></text>

    <!-- Arrows merge -->
    <path d="M 102,125 L 145,150" stroke="var(--accent)" stroke-width="2" marker-end="url(#arr-eqdfa)"/>
    <path d="M 102,185 L 145,160" stroke="var(--accent)" stroke-width="2" marker-end="url(#arr-eqdfa)"/>

    <!-- Step 1: Product DFA -->
    <rect x="150" y="115" width="160" height="80" rx="8" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="2"/>
    <text x="230" y="138" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="var(--gold)">Build product C</text>
    <text x="230" y="156" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="10" fill="#666">states: (q<tspan baseline-shift="sub" font-size="0.7em">A</tspan>, q<tspan baseline-shift="sub" font-size="0.7em">B</tspan>)</text>
    <text x="230" y="172" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="10" fill="#666">accept: XOR of</text>
    <text x="230" y="186" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="10" fill="#666">A.accept and B.accept</text>

    <!-- Arrow -->
    <path d="M 312,155 L 360,155" stroke="var(--accent)" stroke-width="2" marker-end="url(#arr-eqdfa)"/>
    <text x="336" y="148" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">L(C) = L(A) △ L(B)</text>

    <!-- Step 2: Reachability test -->
    <rect x="365" y="115" width="160" height="80" rx="8" fill="var(--accent-soft)" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2"/>
    <text x="445" y="138" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="var(--accent-strong, #1c4a3f)">BFS from start</text>
    <text x="445" y="156" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">does any accept state</text>
    <text x="445" y="170" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">of C get reached?</text>
    <text x="445" y="186" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">(call E<tspan baseline-shift="sub" font-size="0.7em">DFA</tspan> on C)</text>

    <!-- Arrow -->
    <path d="M 527,155 L 570,155" stroke="var(--accent)" stroke-width="2" marker-end="url(#arr-eqdfa)"/>

    <!-- Output -->
    <rect x="575" y="120" width="55" height="70" rx="8" fill="#fff" stroke="var(--warn-strong, #b95825)" stroke-width="2"/>
    <text x="603" y="145" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="var(--accent-strong, #1c4a3f)">empty</text>
    <text x="603" y="160" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="11" fill="#666">↓</text>
    <text x="603" y="178" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="var(--accent-strong, #1c4a3f)">L(A)=L(B)</text>

    <!-- Bottom -->
    <text x="320" y="232" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-style="italic" fill="#666">
      L(A) = L(B) ⇔ symmetric difference is empty ⇔ no accept state of the product DFA is reachable.
    </text>
  </svg>
  <figcaption>The EQ<sub>DFA</sub> decider turns "do two DFAs accept the same language?" into "is the product DFA's language empty?" — which we already know how to solve via BFS. Polynomial time in |Q<sub>A</sub>| · |Q<sub>B</sub>|.</figcaption>
</figure>
"""

ALGO_ECFG_MARKING = """
<figure class="diagram">
  <svg viewBox="0 0 640 280" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      E<tspan baseline-shift="sub" font-size="0.75em">CFG</tspan> · mark "productive" variables, round by round
    </text>
    <!-- Round-0 -->
    <text x="60" y="60" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="#666">Round 0 · seed</text>
    <g font-family="var(--mono), ui-monospace, monospace" font-size="11">
      <rect x="40" y="70" width="60" height="28" fill="white" stroke="#bbb"/>
      <text x="70" y="89" text-anchor="middle" fill="#888">S</text>
      <rect x="40" y="100" width="60" height="28" fill="white" stroke="#bbb"/>
      <text x="70" y="119" text-anchor="middle" fill="#888">A</text>
      <rect x="40" y="130" width="60" height="28" fill="white" stroke="#bbb"/>
      <text x="70" y="149" text-anchor="middle" fill="#888">B</text>
      <rect x="40" y="160" width="60" height="28" fill="white" stroke="#bbb"/>
      <text x="70" y="179" text-anchor="middle" fill="#888">C</text>
    </g>
    <text x="70" y="208" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">none yet</text>

    <!-- Round 1: rules with only terminals on RHS -->
    <text x="220" y="60" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="var(--gold)">Round 1</text>
    <text x="220" y="74" font-family="var(--sans), system-ui" font-size="10" fill="#666">A → 0 (terminal)</text>
    <g font-family="var(--mono), ui-monospace, monospace" font-size="11">
      <rect x="200" y="80" width="60" height="28" fill="white" stroke="#bbb"/>
      <text x="230" y="99" text-anchor="middle" fill="#888">S</text>
      <rect x="200" y="110" width="60" height="28" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="2"/>
      <text x="230" y="129" text-anchor="middle" font-weight="700" fill="var(--gold)">A ✓</text>
      <rect x="200" y="140" width="60" height="28" fill="white" stroke="#bbb"/>
      <text x="230" y="159" text-anchor="middle" fill="#888">B</text>
      <rect x="200" y="170" width="60" height="28" fill="white" stroke="#bbb"/>
      <text x="230" y="189" text-anchor="middle" fill="#888">C</text>
    </g>

    <!-- Round 2: B → A1 now valid because A is productive -->
    <text x="380" y="60" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="var(--gold)">Round 2</text>
    <text x="380" y="74" font-family="var(--sans), system-ui" font-size="10" fill="#666">B → A 1 (uses A ✓)</text>
    <g font-family="var(--mono), ui-monospace, monospace" font-size="11">
      <rect x="360" y="80" width="60" height="28" fill="white" stroke="#bbb"/>
      <text x="390" y="99" text-anchor="middle" fill="#888">S</text>
      <rect x="360" y="110" width="60" height="28" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="2"/>
      <text x="390" y="129" text-anchor="middle" font-weight="700" fill="var(--gold)">A ✓</text>
      <rect x="360" y="140" width="60" height="28" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="2"/>
      <text x="390" y="159" text-anchor="middle" font-weight="700" fill="var(--gold)">B ✓</text>
      <rect x="360" y="170" width="60" height="28" fill="white" stroke="#bbb"/>
      <text x="390" y="189" text-anchor="middle" fill="#888">C</text>
    </g>

    <!-- Round 3: S → A B becomes productive -->
    <text x="540" y="60" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="var(--accent-strong, #1c4a3f)">Round 3 · fixed point</text>
    <text x="540" y="74" font-family="var(--sans), system-ui" font-size="10" fill="#666">S → A B (uses A, B)</text>
    <g font-family="var(--mono), ui-monospace, monospace" font-size="11">
      <rect x="520" y="80" width="60" height="28" fill="var(--accent-soft)" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2"/>
      <text x="550" y="99" text-anchor="middle" font-weight="700" fill="var(--accent-strong, #1c4a3f)">S ✓</text>
      <rect x="520" y="110" width="60" height="28" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="2"/>
      <text x="550" y="129" text-anchor="middle" font-weight="700" fill="var(--gold)">A ✓</text>
      <rect x="520" y="140" width="60" height="28" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="2"/>
      <text x="550" y="159" text-anchor="middle" font-weight="700" fill="var(--gold)">B ✓</text>
      <rect x="520" y="170" width="60" height="28" fill="white" stroke="#bbb"/>
      <text x="550" y="189" text-anchor="middle" fill="#888">C</text>
    </g>

    <!-- Conclusion -->
    <text x="320" y="232" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" fill="#1a1a1a">
      <tspan font-weight="700">S got marked</tspan> ⇒ L(G) is non-empty.   <tspan font-weight="700">C stayed unmarked</tspan> ⇒ no terminal string derives from C.
    </text>
    <text x="320" y="254" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-style="italic" fill="#666">
      The algorithm halts because at most |V| variables can ever be marked. Polynomial time.
    </text>
  </svg>
  <figcaption>E<sub>CFG</sub> via marking: start with no variable marked, then repeatedly mark any variable that has a production whose RHS contains only terminals and already-marked variables. Halt when nothing new gets marked. The CFG's language is non-empty iff the start variable S ends up marked.</figcaption>
</figure>
"""

# ============================================================
# Module 2 — Universal TM + diagonal
# ============================================================

ALGO_UNIVERSAL_TM = """
<figure class="diagram">
  <svg viewBox="0 0 640 260" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <defs>
      <marker id="arr-utm" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto">
        <polygon points="0 0, 9 3, 0 6" fill="var(--accent)"/>
      </marker>
    </defs>
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      Universal TM · one machine that runs every other machine
    </text>
    <!-- Outer U box -->
    <rect x="40" y="60" width="560" height="160" rx="12" fill="none" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2.4"/>
    <text x="320" y="82" text-anchor="middle" font-family="var(--sans), system-ui" font-size="13" font-weight="700" fill="var(--accent-strong, #1c4a3f)">Universal Turing Machine U</text>
    <!-- ⟨M, w⟩ input arrow at left -->
    <text x="50" y="142" font-family="var(--mono), ui-monospace, monospace" font-size="13" fill="#1a1a1a">⟨M, w⟩</text>
    <path d="M 100,140 L 145,140" stroke="var(--accent)" stroke-width="2" marker-end="url(#arr-utm)"/>
    <!-- TM-description region -->
    <rect x="150" y="100" width="160" height="80" rx="8" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="1.6"/>
    <text x="230" y="123" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="var(--gold)">M's description</text>
    <text x="230" y="142" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="10" fill="#666">states, δ-table,</text>
    <text x="230" y="156" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="10" fill="#666">accept/reject</text>
    <text x="230" y="170" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">(read-only)</text>
    <!-- Arrow between -->
    <path d="M 312,140 L 360,140" stroke="var(--accent)" stroke-width="2" marker-end="url(#arr-utm)"/>
    <text x="336" y="132" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">consult</text>
    <!-- Simulation loop -->
    <rect x="365" y="100" width="160" height="80" rx="8" fill="var(--accent-soft)" stroke="var(--accent-strong, #1c4a3f)" stroke-width="1.6"/>
    <text x="445" y="123" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="var(--accent-strong, #1c4a3f)">Step-by-step sim</text>
    <text x="445" y="142" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="10" fill="#666">tape ← w</text>
    <text x="445" y="156" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="10" fill="#666">apply δ until halt</text>
    <text x="445" y="170" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">…or run forever</text>
    <!-- Arrow out -->
    <path d="M 527,140 L 580,140" stroke="var(--accent)" stroke-width="2" marker-end="url(#arr-utm)"/>
    <text x="590" y="135" font-family="var(--mono), ui-monospace, monospace" font-size="13" fill="var(--accent-strong, #1c4a3f)">✓</text>
    <text x="590" y="152" font-family="var(--mono), ui-monospace, monospace" font-size="13" fill="var(--warn-strong, #b95825)">✗</text>
    <!-- Bottom note -->
    <text x="320" y="245" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-style="italic" fill="#666">
      U accepts ⟨M, w⟩ iff M accepts w. If M loops on w, U loops too — that's why A<tspan baseline-shift="sub" font-size="0.75em">TM</tspan> is recognizable but not decidable.
    </text>
  </svg>
  <figcaption>The universal TM U takes an encoded machine ⟨M⟩ and an input w, reads M's description as data, and simulates M's transitions step-by-step on its own tape. This is the machine that recognizes A<sub>TM</sub>. Its existence is what lets us treat programs as data.</figcaption>
</figure>
"""

# ============================================================
# Module 3 — Reduction box diagrams + Recursion theorem
# ============================================================

ALGO_HALT_REDUCTION = """
<figure class="diagram">
  <svg viewBox="0 0 640 280" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <defs>
      <marker id="arr-halt" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto">
        <polygon points="0 0, 9 3, 0 6" fill="var(--accent)"/>
      </marker>
    </defs>
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      A<tspan baseline-shift="sub" font-size="0.75em">TM</tspan> ≤ HALT<tspan baseline-shift="sub" font-size="0.75em">TM</tspan> · the decider S built from a hypothetical R
    </text>
    <!-- ⟨M, w⟩ input arrow -->
    <text x="40" y="130" font-family="var(--mono), ui-monospace, monospace" font-size="13" fill="#1a1a1a">⟨M, w⟩</text>
    <path d="M 100,127 L 145,127" stroke="var(--accent)" stroke-width="2" marker-end="url(#arr-halt)"/>
    <!-- S box (outer) -->
    <rect x="150" y="60" width="430" height="170" rx="10" fill="white" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2.4"/>
    <text x="365" y="82" text-anchor="middle" font-family="var(--sans), system-ui" font-size="13" font-weight="700" fill="var(--accent-strong, #1c4a3f)">S · the assumed decider for A<tspan baseline-shift="sub" font-size="0.75em">TM</tspan></text>
    <!-- Step 1: ask R -->
    <rect x="170" y="105" width="160" height="55" rx="8" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="2"/>
    <text x="250" y="127" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="var(--gold)">Call R(⟨M, w⟩)</text>
    <text x="250" y="145" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" fill="#666">does M halt on w ?</text>
    <!-- R rejects → S rejects -->
    <path d="M 250,162 L 250,200" stroke="var(--warn-strong, #b95825)" stroke-width="2" marker-end="url(#arr-halt)"/>
    <text x="260" y="180" font-family="var(--sans), system-ui" font-size="11" fill="var(--warn-strong, #b95825)">R says no</text>
    <text x="260" y="195" font-family="var(--sans), system-ui" font-size="11" fill="var(--warn-strong, #b95825)">→ reject</text>
    <!-- R accepts → continue -->
    <path d="M 332,127 L 380,127" stroke="var(--accent)" stroke-width="2" marker-end="url(#arr-halt)"/>
    <text x="355" y="118" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="var(--accent)">R says yes</text>
    <text x="355" y="142" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">(M halts)</text>
    <!-- Step 2: simulate M directly (safe) -->
    <rect x="385" y="100" width="175" height="65" rx="8" fill="var(--accent-soft)" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2"/>
    <text x="472" y="123" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="var(--accent-strong, #1c4a3f)">Simulate M on w directly</text>
    <text x="472" y="141" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">guaranteed to halt</text>
    <text x="472" y="155" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">(R just told us so!)</text>
    <!-- Output -->
    <path d="M 472,167 L 472,205" stroke="var(--accent)" stroke-width="2" marker-end="url(#arr-halt)"/>
    <text x="485" y="185" font-family="var(--mono), ui-monospace, monospace" font-size="12" fill="var(--accent-strong, #1c4a3f)">accept iff M accepts</text>
    <!-- Bottom -->
    <text x="320" y="262" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-style="italic" fill="#666">
      If HALT<tspan baseline-shift="sub" font-size="0.75em">TM</tspan> had a decider R, we could decide A<tspan baseline-shift="sub" font-size="0.75em">TM</tspan>. But A<tspan baseline-shift="sub" font-size="0.75em">TM</tspan> is undecidable, so R cannot exist.
    </text>
  </svg>
  <figcaption>The reduction A<sub>TM</sub> ≤ HALT<sub>TM</sub>: assuming a halting-checker R exists, we build a decider S for A<sub>TM</sub> — first ask R "does M halt on w?", and if yes, simulate M directly (which we now know is safe). Since A<sub>TM</sub> has no decider, neither can HALT<sub>TM</sub>.</figcaption>
</figure>
"""

ALGO_RECURSION_THEOREM = """
<figure class="diagram">
  <svg viewBox="0 0 640 260" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <defs>
      <marker id="arr-rec" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto">
        <polygon points="0 0, 9 3, 0 6" fill="var(--accent)"/>
      </marker>
    </defs>
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      Recursion theorem · a program that has access to its own description ⟨M⟩
    </text>
    <!-- M box -->
    <rect x="40" y="65" width="220" height="140" rx="10" fill="white" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2.4"/>
    <text x="150" y="88" text-anchor="middle" font-family="var(--sans), system-ui" font-size="13" font-weight="700" fill="var(--accent-strong, #1c4a3f)">TM M</text>
    <!-- Inside: data region (⟨M⟩) and code region -->
    <rect x="60" y="105" width="80" height="80" rx="6" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="1.6"/>
    <text x="100" y="128" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="12" font-weight="700" fill="var(--gold)">data</text>
    <text x="100" y="148" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="11" fill="#666">⟨M⟩</text>
    <text x="100" y="170" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">own description</text>

    <rect x="160" y="105" width="80" height="80" rx="6" fill="var(--accent-soft)" stroke="var(--accent-strong, #1c4a3f)" stroke-width="1.6"/>
    <text x="200" y="128" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="12" font-weight="700" fill="var(--accent-strong, #1c4a3f)">code</text>
    <text x="200" y="148" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">read data,</text>
    <text x="200" y="162" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">use ⟨M⟩ to</text>
    <text x="200" y="176" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">compute</text>

    <!-- Loop arrow from code back to data -->
    <path d="M 200,108 Q 200,75 140,108" stroke="var(--accent)" stroke-width="2" stroke-dasharray="3 2" fill="none" marker-end="url(#arr-rec)"/>
    <text x="170" y="68" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="var(--accent)">access self</text>

    <!-- Arrow to outside -->
    <path d="M 262,135 L 320,135" stroke="var(--accent)" stroke-width="2" marker-end="url(#arr-rec)"/>
    <text x="291" y="125" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">on input w</text>

    <!-- t(⟨M⟩) result -->
    <rect x="325" y="100" width="240" height="80" rx="8" fill="white" stroke="var(--info, #2f60a8)" stroke-width="2"/>
    <text x="445" y="123" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="var(--info, #2f60a8)">Behavior of M(w)</text>
    <text x="445" y="143" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="11" fill="#1a1a1a">= behavior of t(⟨M⟩)(w)</text>
    <text x="445" y="160" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">for any computable transformer t</text>
    <text x="445" y="174" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">(quines, fixed points, …)</text>

    <!-- Bottom -->
    <text x="320" y="232" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-style="italic" fill="#666">
      For any TM transformer t, there is a TM M whose behavior is t(⟨M⟩) — a "fixed point" of t.
    </text>
  </svg>
  <figcaption>The recursion theorem says that any TM can access its own description ⟨M⟩ during computation. This is what makes quines (self-printing programs) possible — and gives a slick second proof of A<sub>TM</sub>'s undecidability by building a machine that consults a hypothetical A<sub>TM</sub>-decider on its own description.</figcaption>
</figure>
"""

# ============================================================
# Module 4 — Time complexity
# ============================================================

ALGO_BIGO_LAYERS = """
<figure class="diagram">
  <svg viewBox="0 0 640 260" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      Big-O · what we throw away when n grows large
    </text>
    <!-- Original expression -->
    <rect x="30" y="50" width="280" height="70" rx="8" fill="white" stroke="#888" stroke-width="1.4"/>
    <text x="170" y="76" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="14" fill="#1a1a1a">
      <tspan fill="var(--accent-strong, #1c4a3f)" font-weight="700">3 n²</tspan>
      <tspan fill="#888"> + 100 n + 5000</tspan>
    </text>
    <text x="170" y="100" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" fill="#666">exact running time T(n)</text>

    <!-- Arrow -->
    <text x="330" y="92" font-family="var(--sans), system-ui" font-size="20" fill="var(--accent)">→</text>

    <!-- Dominant term boxed -->
    <rect x="350" y="50" width="260" height="70" rx="8" fill="var(--accent-soft)" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2"/>
    <text x="480" y="76" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="14" font-weight="700" fill="var(--accent-strong, #1c4a3f)">
      O(n²)
    </text>
    <text x="480" y="100" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" fill="#666">asymptotic growth rate</text>

    <!-- Below: what we discarded -->
    <text x="60" y="155" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="#1a1a1a">Discarded:</text>
    <rect x="60" y="165" width="180" height="50" rx="6" fill="white" stroke="#bbb" stroke-dasharray="3 2"/>
    <text x="150" y="184" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="12" fill="#888">constant 3</text>
    <text x="150" y="202" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">(swallowed by O)</text>

    <rect x="260" y="165" width="180" height="50" rx="6" fill="white" stroke="#bbb" stroke-dasharray="3 2"/>
    <text x="350" y="184" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="12" fill="#888">100 n</text>
    <text x="350" y="202" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">(lower-order term)</text>

    <rect x="460" y="165" width="150" height="50" rx="6" fill="white" stroke="#bbb" stroke-dasharray="3 2"/>
    <text x="535" y="184" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="12" fill="#888">5000</text>
    <text x="535" y="202" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">(constant)</text>

    <!-- Bottom -->
    <text x="320" y="242" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-style="italic" fill="#666">
      f(n) ∈ O(g(n)) ⇔ ∃ c, n₀ such that for all n ≥ n₀, f(n) ≤ c · g(n).
    </text>
  </svg>
  <figcaption>Big-O notation discards constants and lower-order terms. The dominant term defines the complexity class. For n=1000, the n² term is 3,000,000 while the linear and constant terms total 105,000 — the quadratic term is what matters asymptotically.</figcaption>
</figure>
"""
