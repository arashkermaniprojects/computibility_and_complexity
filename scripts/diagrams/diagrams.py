"""Diagram SVGs to be injected into the lecture modules.

Each diagram is a self-contained <figure> with an <svg> + caption.
All colors use CSS variables from styles.css so they match the site theme.
"""

# ============================================================
# MODULE 1 — Decidable problems for automata
# ============================================================

VENN_SYMDIFF = """
<figure class="diagram">
  <svg viewBox="0 0 640 280" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <defs>
      <pattern id="hatch-symdiff" patternUnits="userSpaceOnUse" width="6" height="6" patternTransform="rotate(45)">
        <line x1="0" y1="0" x2="0" y2="6" stroke="var(--warn)" stroke-width="1.4"/>
      </pattern>
    </defs>
    <!-- title -->
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      Symmetric difference · L(A) △ L(B) = (L(A) \\ L(B)) ∪ (L(B) \\ L(A))
    </text>
    <!-- circle A -->
    <circle cx="240" cy="155" r="80" fill="url(#hatch-symdiff)" stroke="var(--accent-strong)" stroke-width="2"/>
    <!-- circle B -->
    <circle cx="400" cy="155" r="80" fill="url(#hatch-symdiff)" stroke="var(--info)" stroke-width="2"/>
    <!-- intersection painted white to mask hatch -->
    <path d="M 320,82 A 80,80 0 0,1 320,228 A 80,80 0 0,1 320,82 Z" fill="#fcfbf7" stroke="none"/>
    <!-- intersection outline -->
    <path d="M 320,82 A 80,80 0 0,1 320,228" fill="none" stroke="var(--accent-strong)" stroke-width="2"/>
    <path d="M 320,82 A 80,80 0 0,0 320,228" fill="none" stroke="var(--info)" stroke-width="2"/>
    <!-- labels -->
    <text x="195" y="60" font-family="var(--mono), ui-monospace" font-size="15" font-weight="700" fill="var(--accent-strong)">L(A)</text>
    <text x="425" y="60" font-family="var(--mono), ui-monospace" font-size="15" font-weight="700" fill="var(--info)">L(B)</text>
    <text x="320" y="160" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" fill="#1a1a1a">L(A) ∩ L(B)</text>
    <text x="320" y="178" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" fill="#666">both DFAs agree</text>
    <!-- annotations for shaded regions -->
    <text x="180" y="200" font-family="var(--sans), system-ui" font-size="12" font-weight="600" fill="var(--warn-strong, #b95825)">A accepts, B rejects</text>
    <text x="450" y="200" font-family="var(--sans), system-ui" font-size="12" font-weight="600" fill="var(--warn-strong, #b95825)">B accepts, A rejects</text>
    <!-- arrows pointing at the symmetric difference -->
    <path d="M 195,210 Q 180,225 175,235" fill="none" stroke="var(--warn)" stroke-width="1.5" stroke-dasharray="3 2"/>
    <path d="M 470,210 Q 480,225 485,235" fill="none" stroke="var(--warn)" stroke-width="1.5" stroke-dasharray="3 2"/>
    <!-- bottom note -->
    <text x="320" y="265" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-style="italic" fill="#666">
      Striped region = symmetric difference. L(A) = L(B) iff the striped region is empty.
    </text>
  </svg>
  <figcaption>The symmetric difference of two languages is the set of strings on which the two DFAs disagree. Two DFAs are equivalent if and only if their symmetric difference is the empty language — and that is what the product construction lets us test.</figcaption>
</figure>
"""

GRAPH_REACHABILITY = """
<figure class="diagram">
  <svg viewBox="0 0 640 220" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      E<tspan baseline-shift="sub" font-size="0.75em">DFA</tspan> via reachability · BFS frontier expanding from q&#8320;
    </text>
    <!-- nodes -->
    <g font-family="var(--mono), ui-monospace" font-size="13">
      <circle cx="80"  cy="120" r="22" fill="var(--accent-soft)" stroke="var(--accent-strong)" stroke-width="2"/>
      <text x="80"  y="125" text-anchor="middle" font-weight="700">q&#8320;</text>
      <text x="80"  y="170" text-anchor="middle" font-size="10" fill="#666">start · level 0</text>

      <circle cx="200" cy="80"  r="22" fill="var(--accent-soft)" stroke="var(--accent-strong)" stroke-width="2"/>
      <text x="200" y="85"  text-anchor="middle" font-weight="700">q&#8321;</text>

      <circle cx="200" cy="160" r="22" fill="var(--accent-soft)" stroke="var(--accent-strong)" stroke-width="2"/>
      <text x="200" y="165" text-anchor="middle" font-weight="700">q&#8322;</text>

      <circle cx="340" cy="50"  r="22" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="2"/>
      <text x="340" y="55"  text-anchor="middle" font-weight="700">q&#8323;</text>

      <circle cx="340" cy="120" r="22" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="2"/>
      <text x="340" y="125" text-anchor="middle" font-weight="700">q&#8324;</text>

      <circle cx="340" cy="190" r="22" fill="#f5f5f0" stroke="#bbb" stroke-width="2"/>
      <text x="340" y="195" text-anchor="middle" font-weight="700" fill="#888">q&#8325;</text>

      <!-- ACCEPT state — double circle -->
      <circle cx="480" cy="80"  r="22" fill="var(--warn-soft)" stroke="var(--warn-strong, #b95825)" stroke-width="2"/>
      <circle cx="480" cy="80"  r="17" fill="none" stroke="var(--warn-strong, #b95825)" stroke-width="1.5"/>
      <text x="480" y="85"  text-anchor="middle" font-weight="700">q&#8326;</text>
      <text x="480" y="130" text-anchor="middle" font-size="10" fill="var(--warn-strong, #b95825)" font-weight="600">accept</text>
    </g>
    <!-- arrows showing edges (forward only for clarity) -->
    <g stroke="#888" stroke-width="1.5" fill="none" marker-end="url(#arrow-r)">
      <path d="M 102,114 L 178,90"/>
      <path d="M 102,128 L 178,155"/>
      <path d="M 222,73 L 318,55"/>
      <path d="M 222,87 L 318,115"/>
      <path d="M 222,155 L 318,128"/>
      <path d="M 222,165 L 318,185"/>
      <path d="M 362,50 L 458,77"/>
      <path d="M 362,118 L 458,85"/>
    </g>
    <defs>
      <marker id="arrow-r" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
        <polygon points="0 0, 8 3, 0 6" fill="#888"/>
      </marker>
    </defs>
    <!-- BFS frontiers -->
    <text x="80"  y="200" text-anchor="middle" font-size="9" fill="#888">level 0</text>
    <text x="200" y="200" text-anchor="middle" font-size="9" fill="#888">level 1</text>
    <text x="340" y="215" text-anchor="middle" font-size="9" fill="#888">level 2</text>
    <text x="480" y="200" text-anchor="middle" font-size="9" fill="#888">level 3</text>
  </svg>
  <figcaption>BFS expands outward from the start state. The DFA's language is empty if and only if no accept state is ever reached. Linear time in the number of states and transitions.</figcaption>
</figure>
"""

# ============================================================
# MODULE 2 — Undecidability
# ============================================================

CANTOR_DIAGONAL_DIAGRAM = """
<figure class="diagram">
  <svg viewBox="0 0 640 320" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      Cantor's diagonal · flip every diagonal bit to build a function not in the list
    </text>
    <!-- header row -->
    <g font-family="var(--mono), ui-monospace" font-size="13" fill="#1a1a1a">
      <text x="100" y="60" font-weight="700">input n →</text>
      <text x="195" y="60" text-anchor="middle">0</text>
      <text x="245" y="60" text-anchor="middle">1</text>
      <text x="295" y="60" text-anchor="middle">2</text>
      <text x="345" y="60" text-anchor="middle">3</text>
      <text x="395" y="60" text-anchor="middle">4</text>
      <text x="445" y="60" text-anchor="middle">…</text>
      <text x="510" y="60" text-anchor="middle" font-weight="700">function</text>
    </g>
    <!-- horizontal rule below header -->
    <line x1="170" y1="68" x2="540" y2="68" stroke="#888" stroke-width="1"/>
    <!-- 5 rows of f_i with diagonal cells highlighted -->
    <g font-family="var(--mono), ui-monospace" font-size="13">
      <!-- row 1: diagonal is column 0 -->
      <text x="100" y="95" font-weight="700">f&#8321;</text>
      <rect x="180" y="80" width="30" height="22" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="1.5"/>
      <text x="195" y="95" text-anchor="middle" font-weight="700" fill="var(--gold)">1</text>
      <text x="245" y="95" text-anchor="middle">0</text>
      <text x="295" y="95" text-anchor="middle">1</text>
      <text x="345" y="95" text-anchor="middle">0</text>
      <text x="395" y="95" text-anchor="middle">1</text>
      <text x="445" y="95" text-anchor="middle">…</text>
      <!-- row 2: diagonal is column 1 -->
      <text x="100" y="125" font-weight="700">f&#8322;</text>
      <text x="195" y="125" text-anchor="middle">1</text>
      <rect x="230" y="110" width="30" height="22" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="1.5"/>
      <text x="245" y="125" text-anchor="middle" font-weight="700" fill="var(--gold)">1</text>
      <text x="295" y="125" text-anchor="middle">0</text>
      <text x="345" y="125" text-anchor="middle">1</text>
      <text x="395" y="125" text-anchor="middle">0</text>
      <text x="445" y="125" text-anchor="middle">…</text>
      <!-- row 3 -->
      <text x="100" y="155" font-weight="700">f&#8323;</text>
      <text x="195" y="155" text-anchor="middle">0</text>
      <text x="245" y="155" text-anchor="middle">1</text>
      <rect x="280" y="140" width="30" height="22" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="1.5"/>
      <text x="295" y="155" text-anchor="middle" font-weight="700" fill="var(--gold)">0</text>
      <text x="345" y="155" text-anchor="middle">1</text>
      <text x="395" y="155" text-anchor="middle">1</text>
      <text x="445" y="155" text-anchor="middle">…</text>
      <!-- row 4 -->
      <text x="100" y="185" font-weight="700">f&#8324;</text>
      <text x="195" y="185" text-anchor="middle">1</text>
      <text x="245" y="185" text-anchor="middle">1</text>
      <text x="295" y="185" text-anchor="middle">0</text>
      <rect x="330" y="170" width="30" height="22" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="1.5"/>
      <text x="345" y="185" text-anchor="middle" font-weight="700" fill="var(--gold)">0</text>
      <text x="395" y="185" text-anchor="middle">1</text>
      <text x="445" y="185" text-anchor="middle">…</text>
      <!-- row 5 -->
      <text x="100" y="215" font-weight="700">f&#8325;</text>
      <text x="195" y="215" text-anchor="middle">1</text>
      <text x="245" y="215" text-anchor="middle">0</text>
      <text x="295" y="215" text-anchor="middle">1</text>
      <text x="345" y="215" text-anchor="middle">1</text>
      <rect x="380" y="200" width="30" height="22" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="1.5"/>
      <text x="395" y="215" text-anchor="middle" font-weight="700" fill="var(--gold)">1</text>
      <text x="445" y="215" text-anchor="middle">…</text>
      <!-- ellipsis row -->
      <text x="100" y="240" font-weight="700">⋮</text>
    </g>
    <!-- horizontal rule above g -->
    <line x1="170" y1="255" x2="540" y2="255" stroke="var(--warn-strong, #b95825)" stroke-width="2"/>
    <!-- diagonal flip row g -->
    <g font-family="var(--mono), ui-monospace" font-size="13" fill="var(--warn-strong, #b95825)">
      <text x="100" y="280" font-weight="700">g(n) = 1 − f&#8345;(n)</text>
      <text x="195" y="280" text-anchor="middle" font-weight="700">0</text>
      <text x="245" y="280" text-anchor="middle" font-weight="700">0</text>
      <text x="295" y="280" text-anchor="middle" font-weight="700">1</text>
      <text x="345" y="280" text-anchor="middle" font-weight="700">1</text>
      <text x="395" y="280" text-anchor="middle" font-weight="700">0</text>
      <text x="445" y="280" text-anchor="middle" font-weight="700">…</text>
      <text x="510" y="280" text-anchor="middle" font-weight="700" font-size="11">≠ every f&#8345;</text>
    </g>
    <!-- bottom note -->
    <text x="320" y="310" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-style="italic" fill="#666">
      The new function g disagrees with each f&#8345; at column i, so it cannot appear in the list.
    </text>
  </svg>
  <figcaption>Cantor lists every alleged function on the natural numbers as a row. By flipping each diagonal cell, he constructs a brand-new function that disagrees with row i at column i — so it cannot already be in the list. The same trick proves A<sub>TM</sub> undecidable when the rows become Turing machines.</figcaption>
</figure>
"""

VENN_DECIDABLE_RECOGNIZABLE = """
<figure class="diagram">
  <svg viewBox="0 0 640 360" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      The four regions of language classification
    </text>
    <!-- outer rectangle: all languages -->
    <rect x="40" y="50" width="560" height="270" fill="#fff" stroke="#1a1a1a" stroke-width="1.6"/>
    <text x="55" y="72" font-family="var(--sans), system-ui" font-size="12" fill="#888">All languages over Σ*</text>
    <!-- recognizable (blue) -->
    <ellipse cx="260" cy="185" rx="200" ry="100" fill="#d6e3f4" stroke="var(--info)" stroke-width="2" opacity="0.7"/>
    <text x="110" y="100" font-family="var(--sans), system-ui" font-size="14" fill="var(--info)" font-weight="700">Recognizable</text>
    <!-- co-recognizable (orange) -->
    <ellipse cx="400" cy="185" rx="200" ry="100" fill="#f4dfcf" stroke="var(--warn-strong, #b95825)" stroke-width="2" opacity="0.55"/>
    <text x="560" y="100" text-anchor="end" font-family="var(--sans), system-ui" font-size="14" fill="var(--warn-strong, #b95825)" font-weight="700">co-Recognizable</text>
    <!-- decidable (green oval in intersection) -->
    <ellipse cx="330" cy="185" rx="115" ry="50" fill="#d6ebe4" stroke="#1c4a3f" stroke-width="2.2"/>
    <text x="330" y="190" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1c4a3f">Decidable</text>
    <!-- example language pills -->
    <g font-family="var(--mono), ui-monospace" font-size="11.5">
      <!-- decidable -->
      <rect x="285" y="155" width="90" height="20" rx="4" fill="#fff" stroke="#1c4a3f"/>
      <text x="330" y="170" text-anchor="middle" fill="#1c4a3f">A<tspan baseline-shift="sub" font-size="0.75em">DFA</tspan> · E<tspan baseline-shift="sub" font-size="0.75em">CFG</tspan></text>
      <!-- recognizable not decidable -->
      <rect x="120" y="190" width="80" height="20" rx="4" fill="#fff" stroke="var(--info)"/>
      <text x="160" y="205" text-anchor="middle" fill="var(--info)">A<tspan baseline-shift="sub" font-size="0.75em">TM</tspan></text>
      <rect x="130" y="215" width="100" height="20" rx="4" fill="#fff" stroke="var(--info)"/>
      <text x="180" y="230" text-anchor="middle" fill="var(--info)">HALT<tspan baseline-shift="sub" font-size="0.75em">TM</tspan></text>
      <!-- co-rec not decidable -->
      <rect x="450" y="190" width="100" height="20" rx="4" fill="#fff" stroke="var(--warn-strong, #b95825)"/>
      <text x="500" y="205" text-anchor="middle" fill="var(--warn-strong, #b95825)">co-A<tspan baseline-shift="sub" font-size="0.75em">TM</tspan></text>
      <rect x="440" y="215" width="120" height="20" rx="4" fill="#fff" stroke="var(--warn-strong, #b95825)"/>
      <text x="500" y="230" text-anchor="middle" fill="var(--warn-strong, #b95825)">co-HALT<tspan baseline-shift="sub" font-size="0.75em">TM</tspan></text>
      <!-- neither -->
      <rect x="320" y="290" width="100" height="22" rx="4" fill="#fff" stroke="#1a1a1a" stroke-width="1.5"/>
      <text x="370" y="305" text-anchor="middle" font-weight="700">EQ<tspan baseline-shift="sub" font-size="0.75em">TM</tspan></text>
      <text x="370" y="280" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" fill="#888" font-style="italic">neither recognizable nor co-recognizable</text>
    </g>
    <!-- bridge theorem note -->
    <text x="320" y="345" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11.5" fill="#444">
      <tspan font-weight="600">Bridge theorem:</tspan> L is decidable ⇔ both L and its complement L̅ are recognizable.
    </text>
  </svg>
  <figcaption>The four regions: decidable (in both circles); recognizable but not decidable (left only, e.g. A<sub>TM</sub>); co-recognizable but not decidable (right only, e.g. ¬A<sub>TM</sub>); and neither (outside both, e.g. EQ<sub>TM</sub>).</figcaption>
</figure>
"""

D_CONTRADICTION_MACHINE = """
<figure class="diagram">
  <svg viewBox="0 0 640 280" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <text x="320" y="24" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      The contradiction machine D · feeds itself its own description
    </text>
    <!-- input arrow -->
    <text x="40" y="135" font-family="var(--mono), ui-monospace" font-size="13">⟨M⟩</text>
    <path d="M 75,130 L 130,130" stroke="var(--accent)" stroke-width="2" marker-end="url(#arr-d)"/>
    <!-- D box -->
    <rect x="130" y="70" width="380" height="130" rx="10" fill="#fff" stroke="var(--accent-strong)" stroke-width="2.5"/>
    <text x="320" y="92" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="var(--accent-strong)">D · on input ⟨M⟩</text>
    <!-- H inside D -->
    <rect x="160" y="115" width="180" height="60" rx="6" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="2"/>
    <text x="250" y="138" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" font-weight="700">H(⟨M, ⟨M⟩⟩)</text>
    <text x="250" y="156" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" fill="#666">does M accept its own ⟨M⟩?</text>
    <!-- flip box -->
    <rect x="360" y="115" width="130" height="60" rx="6" fill="var(--warn-soft)" stroke="var(--warn-strong, #b95825)" stroke-width="2"/>
    <text x="425" y="138" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" font-weight="700">flip the bit</text>
    <text x="425" y="156" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" fill="#666">yes ↦ reject<tspan dx="6">/</tspan>no ↦ accept</text>
    <!-- arrow H → flip -->
    <path d="M 340,145 L 360,145" stroke="var(--accent)" stroke-width="2" marker-end="url(#arr-d)"/>
    <!-- output arrow -->
    <path d="M 490,145 L 545,145" stroke="var(--accent)" stroke-width="2" marker-end="url(#arr-d)"/>
    <text x="555" y="150" font-family="var(--mono), ui-monospace" font-size="13">✓ / ✗</text>
    <defs>
      <marker id="arr-d" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto">
        <polygon points="0 0, 9 3, 0 6" fill="var(--accent)"/>
      </marker>
    </defs>
    <!-- contradiction note -->
    <text x="320" y="230" text-anchor="middle" font-family="var(--sans), system-ui" font-size="13" fill="#1a1a1a">
      Now run D on ⟨D⟩. By definition, D outputs the opposite of D(⟨D⟩).
    </text>
    <text x="320" y="252" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-style="italic" fill="var(--warn-strong, #b95825)">
      D contradicts itself ⇒ H cannot exist ⇒ A<tspan baseline-shift="sub" font-size="0.75em">TM</tspan> is undecidable.
    </text>
  </svg>
  <figcaption>D is built from H by composition: ask H whether M accepts its own description, then output the opposite. When D is fed its own description, D's answer must equal its own opposite — impossible. The hypothetical decider H cannot exist.</figcaption>
</figure>
"""

# ============================================================
# MODULE 3 — Reductions, recursion theorem, Rice
# ============================================================

COMPUTATION_HISTORY_TABLEAU = """
<figure class="diagram">
  <svg viewBox="0 0 640 320" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      Computation history · each row is a configuration of M on w
    </text>
    <!-- column labels: tape positions -->
    <g font-family="var(--mono), ui-monospace" font-size="11" fill="#888">
      <text x="100" y="55" text-anchor="middle">pos 0</text>
      <text x="160" y="55" text-anchor="middle">pos 1</text>
      <text x="220" y="55" text-anchor="middle">pos 2</text>
      <text x="280" y="55" text-anchor="middle">pos 3</text>
      <text x="340" y="55" text-anchor="middle">pos 4</text>
      <text x="400" y="55" text-anchor="middle">pos 5</text>
      <text x="460" y="55" text-anchor="middle">pos 6</text>
      <text x="520" y="55" text-anchor="middle">pos 7</text>
      <text x="580" y="55" text-anchor="middle">…</text>
    </g>
    <!-- row labels -->
    <g font-family="var(--mono), ui-monospace" font-size="11" fill="#888">
      <text x="42" y="85" text-anchor="end">t = 0</text>
      <text x="42" y="115" text-anchor="end">t = 1</text>
      <text x="42" y="145" text-anchor="end">t = 2</text>
      <text x="42" y="175" text-anchor="end">t = 3</text>
      <text x="42" y="205" text-anchor="end">t = 4</text>
      <text x="42" y="235" text-anchor="end">t = 5</text>
    </g>
    <!-- table cells -->""" + ''.join(
    f'<rect x="{70 + col*60}" y="{70 + row*30}" width="60" height="30" fill="#fff" stroke="#ccc" stroke-width="0.8"/>'
    for row in range(6) for col in range(9)
) + """
    <!-- row 0: initial config -->
    <text x="100" y="90" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" font-weight="700" fill="var(--info)">q&#8320;</text>
    <text x="160" y="90" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">0</text>
    <text x="220" y="90" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">1</text>
    <text x="280" y="90" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">1</text>
    <text x="340" y="90" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">0</text>
    <text x="400" y="90" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" fill="#aaa">_</text>
    <text x="460" y="90" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" fill="#aaa">_</text>
    <text x="520" y="90" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" fill="#aaa">_</text>
    <!-- row 1 -->
    <text x="100" y="120" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">0</text>
    <text x="160" y="120" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" font-weight="700" fill="var(--info)">q&#8321;</text>
    <text x="220" y="120" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">1</text>
    <text x="280" y="120" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">1</text>
    <text x="340" y="120" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">0</text>
    <!-- row 2 -->
    <text x="100" y="150" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">0</text>
    <text x="160" y="150" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">0</text>
    <text x="220" y="150" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" font-weight="700" fill="var(--info)">q&#8320;</text>
    <text x="280" y="150" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">1</text>
    <text x="340" y="150" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">0</text>
    <!-- row 3 -->
    <text x="100" y="180" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">0</text>
    <text x="160" y="180" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">0</text>
    <text x="220" y="180" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">1</text>
    <text x="280" y="180" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" font-weight="700" fill="var(--info)">q&#8322;</text>
    <text x="340" y="180" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">0</text>
    <!-- row 4: accept -->
    <text x="100" y="210" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">0</text>
    <text x="160" y="210" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">0</text>
    <text x="220" y="210" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">1</text>
    <text x="280" y="210" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">1</text>
    <text x="340" y="210" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" font-weight="700" fill="var(--warn-strong, #b95825)">q&#8336;</text>
    <!-- highlight a 2x3 local window -->
    <rect x="158" y="129" width="184" height="62" fill="none" stroke="var(--gold)" stroke-width="2" stroke-dasharray="4 3"/>
    <text x="358" y="160" font-family="var(--sans), system-ui" font-size="11" fill="var(--gold)" font-weight="700">local 2×3 window</text>
    <text x="358" y="175" font-family="var(--sans), system-ui" font-size="10" fill="#888">must obey δ</text>
    <!-- accept label -->
    <text x="395" y="215" font-family="var(--sans), system-ui" font-size="11" fill="var(--warn-strong, #b95825)" font-weight="700">accept</text>
    <!-- bottom note -->
    <text x="320" y="285" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-style="italic" fill="#666">
      The whole tableau is a valid history iff every 2×3 window is consistent with M's transition function δ.
    </text>
  </svg>
  <figcaption>A computation history records every configuration of M on w, one row per time step. Local 2×3 windows of consecutive rows must follow the transition function. The accepting tableau exists iff M accepts w — this is what gadgets in L<sub>BA</sub> and CFG reductions check.</figcaption>
</figure>
"""

RICE_DECISION_TREE = """
<figure class="diagram">
  <svg viewBox="0 0 640 360" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <text x="320" y="24" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      Rice's theorem · is the property of L(M) decidable?
    </text>
    <!-- root -->
    <rect x="220" y="50" width="200" height="50" rx="10" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="2"/>
    <text x="320" y="74" text-anchor="middle" font-family="var(--sans), system-ui" font-size="13" font-weight="700">Property P of L(M)</text>
    <text x="320" y="90" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" fill="#666">about the language, not the description</text>
    <!-- branch: trivial? -->
    <path d="M 320,100 L 160,150" stroke="#888" stroke-width="1.5" fill="none"/>
    <path d="M 320,100 L 480,150" stroke="#888" stroke-width="1.5" fill="none"/>
    <text x="220" y="125" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" fill="#888">trivial</text>
    <text x="420" y="125" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" fill="#888">nontrivial</text>
    <!-- left: decidable trivial -->
    <rect x="60" y="150" width="200" height="50" rx="10" fill="#d6ebe4" stroke="#1c4a3f" stroke-width="2"/>
    <text x="160" y="172" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="#1c4a3f">Decidable</text>
    <text x="160" y="190" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" fill="#666">always true or always false</text>
    <!-- right: nontrivial → about description? -->
    <rect x="380" y="150" width="200" height="50" rx="10" fill="#fff" stroke="#888" stroke-width="1.5"/>
    <text x="480" y="173" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12">depends only on L(M)?</text>
    <text x="480" y="190" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" fill="#666">vs M's syntax</text>
    <!-- nontrivial branches -->
    <path d="M 480,200 L 380,260" stroke="#888" stroke-width="1.5" fill="none"/>
    <path d="M 480,200 L 580,260" stroke="#888" stroke-width="1.5" fill="none"/>
    <text x="420" y="230" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" fill="#888">yes — semantic</text>
    <text x="555" y="230" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" fill="#888">no — syntactic</text>
    <!-- left bottom: undecidable -->
    <rect x="280" y="260" width="200" height="55" rx="10" fill="var(--warn-soft)" stroke="var(--warn-strong, #b95825)" stroke-width="2"/>
    <text x="380" y="282" text-anchor="middle" font-family="var(--sans), system-ui" font-size="13" font-weight="700" fill="var(--warn-strong, #b95825)">Undecidable (Rice)</text>
    <text x="380" y="300" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">"L(M) is empty", "L(M) regular"</text>
    <!-- right bottom: may be decidable -->
    <rect x="490" y="260" width="140" height="55" rx="10" fill="#d6ebe4" stroke="#1c4a3f" stroke-width="2"/>
    <text x="560" y="282" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="#1c4a3f">May be decidable</text>
    <text x="560" y="300" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">"M has 5 states"</text>
    <!-- note -->
    <text x="320" y="345" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-style="italic" fill="#666">
      Rice's theorem: every nontrivial semantic property of L(M) is undecidable.
    </text>
  </svg>
  <figcaption>A decision tree for applying Rice's theorem. Only nontrivial properties that depend solely on the language L(M) — not on the syntactic description of M — are guaranteed undecidable.</figcaption>
</figure>
"""

# ============================================================
# MODULE 4 — Time complexity
# ============================================================

GROWTH_RATE_CURVES = """
<figure class="diagram">
  <svg viewBox="0 0 640 320" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <text x="320" y="24" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      Growth rates · why polynomial vs exponential is THE divide
    </text>
    <!-- axes -->
    <line x1="60" y1="280" x2="600" y2="280" stroke="#888" stroke-width="1.4"/>
    <line x1="60" y1="60" x2="60" y2="280" stroke="#888" stroke-width="1.4"/>
    <text x="600" y="298" text-anchor="end" font-family="var(--sans), system-ui" font-size="11" fill="#666">input length n →</text>
    <text x="58" y="55" text-anchor="end" font-family="var(--sans), system-ui" font-size="11" fill="#666">time</text>
    <!-- gridlines -->
    <g stroke="#eee" stroke-width="1">
      <line x1="60" y1="220" x2="600" y2="220"/>
      <line x1="60" y1="160" x2="600" y2="160"/>
      <line x1="60" y1="100" x2="600" y2="100"/>
    </g>
    <!-- curves: log n, n, n log n, n^2, n^3, 2^n -->
    <!-- log n (slow) -->
    <path d="M 70,275 Q 200,260 360,250 T 590,240" fill="none" stroke="#2A6F5F" stroke-width="2"/>
    <text x="600" y="240" font-family="var(--mono), ui-monospace" font-size="11" fill="#2A6F5F">log n</text>
    <!-- n -->
    <path d="M 60,280 L 590,200" fill="none" stroke="#1c4a3f" stroke-width="2"/>
    <text x="600" y="195" font-family="var(--mono), ui-monospace" font-size="11" fill="#1c4a3f">n</text>
    <!-- n log n -->
    <path d="M 60,280 Q 250,250 400,200 T 580,160" fill="none" stroke="var(--info)" stroke-width="2"/>
    <text x="600" y="160" font-family="var(--mono), ui-monospace" font-size="11" fill="var(--info)">n log n</text>
    <!-- n^2 -->
    <path d="M 60,280 Q 250,260 400,180 T 530,80" fill="none" stroke="var(--gold)" stroke-width="2"/>
    <text x="540" y="78" font-family="var(--mono), ui-monospace" font-size="11" fill="var(--gold)">n²</text>
    <!-- n^3 -->
    <path d="M 60,280 Q 300,275 380,200 Q 410,150 430,80" fill="none" stroke="var(--accent-strong)" stroke-width="2"/>
    <text x="440" y="78" font-family="var(--mono), ui-monospace" font-size="11" fill="var(--accent-strong)">n³</text>
    <!-- 2^n (sharp) -->
    <path d="M 60,280 Q 230,278 310,265 Q 340,250 360,180 Q 370,130 380,80" fill="none" stroke="var(--warn-strong, #b95825)" stroke-width="2.5"/>
    <text x="390" y="78" font-family="var(--mono), ui-monospace" font-size="11" fill="var(--warn-strong, #b95825)" font-weight="700">2ⁿ</text>
    <!-- divider band: polynomial / exponential -->
    <line x1="60" y1="62" x2="600" y2="62" stroke="#888" stroke-width="0.5" stroke-dasharray="2 3"/>
    <text x="320" y="50" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-style="italic" fill="#666">
      every polynomial is eventually crushed by 2ⁿ
    </text>
  </svg>
  <figcaption>The vertical scale grows much faster for exponential curves than for polynomials. The class P consists of problems whose running time stays below some polynomial — that's why P is the central "tractable" class.</figcaption>
</figure>
"""

SINGLE_VS_TWO_TAPE = """
<figure class="diagram">
  <svg viewBox="0 0 640 280" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      Single-tape vs two-tape · deciding 0ⁿ1ⁿ
    </text>
    <!-- single-tape: head bounces -->
    <text x="40" y="65" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="var(--accent-strong)">single tape</text>
    <!-- tape cells -->
    <g font-family="var(--mono), ui-monospace" font-size="13">""" + ''.join(
    f'<rect x="{40 + i*32}" y="78" width="32" height="32" fill="#fff" stroke="#888"/>' +
    f'<text x="{56 + i*32}" y="100" text-anchor="middle">{"0" if i < 3 else "1"}</text>'
    for i in range(6)
) + """</g>
    <!-- zigzag head path -->
    <path d="M 56,128 Q 100,160 56,140 Q 88,170 56,150 Q 152,180 56,160 Q 184,180 56,170" fill="none" stroke="var(--warn)" stroke-width="1.6" stroke-dasharray="3 3"/>
    <text x="280" y="140" font-family="var(--sans), system-ui" font-size="12" fill="var(--warn-strong, #b95825)">head must zig-zag</text>
    <text x="280" y="158" font-family="var(--mono), ui-monospace" font-size="11" fill="#666">→ O(n²) steps</text>
    <!-- two-tape -->
    <text x="40" y="200" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="var(--accent-strong)">two tapes</text>
    <!-- tape 1: 0s -->
    <g font-family="var(--mono), ui-monospace" font-size="13">""" + ''.join(
    f'<rect x="{40 + i*32}" y="213" width="32" height="22" fill="#fff" stroke="#888"/>' +
    f'<text x="{56 + i*32}" y="230" text-anchor="middle">0</text>'
    for i in range(3)
) + ''.join(
    f'<rect x="{40 + (3+i)*32}" y="213" width="32" height="22" fill="#fff" stroke="#888"/>' +
    f'<text x="{56 + (3+i)*32}" y="230" text-anchor="middle">1</text>'
    for i in range(3)
) + """</g>
    <!-- tape 2: copy of 0s -->
    <g font-family="var(--mono), ui-monospace" font-size="13">""" + ''.join(
    f'<rect x="{40 + i*32}" y="240" width="32" height="22" fill="var(--gold-soft)" stroke="var(--gold)"/>' +
    f'<text x="{56 + i*32}" y="257" text-anchor="middle">0</text>'
    for i in range(3)
) + """</g>
    <text x="240" y="230" font-family="var(--sans), system-ui" font-size="11" fill="var(--gold)">→ copy 0s onto tape 2</text>
    <text x="240" y="257" font-family="var(--sans), system-ui" font-size="11" fill="var(--gold)">→ pop one 0 per 1 seen on tape 1</text>
    <text x="510" y="245" font-family="var(--mono), ui-monospace" font-size="12" font-weight="700" fill="var(--accent-strong)">O(n) steps</text>
  </svg>
  <figcaption>On a single-tape TM, deciding 0ⁿ1ⁿ requires the head to bounce back and forth, paying O(n²) time. With a second tape, the same task runs in linear time. The Hennie–Stearns theorem guarantees the gap is at most quadratic — multi-tape TMs are not more powerful, just more efficient by a polynomial factor.</figcaption>
</figure>
"""

# ============================================================
# MODULE 5 — NP-completeness
# ============================================================

NP_REDUCTION_TREE = """
<figure class="diagram">
  <svg viewBox="0 0 640 360" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      The NP-completeness reduction tree · every node reduces from its parent
    </text>
    <!-- root: SAT -->
    <rect x="270" y="50" width="100" height="40" rx="8" fill="var(--warn-soft)" stroke="var(--warn-strong, #b95825)" stroke-width="2.5"/>
    <text x="320" y="75" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="14" font-weight="700">SAT</text>
    <text x="320" y="42" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#888">Cook–Levin (1971)</text>
    <!-- level 2 -->
    <g font-family="var(--mono), ui-monospace" font-size="12">
      <rect x="240" y="130" width="100" height="32" rx="6" fill="#fff" stroke="var(--accent-strong)" stroke-width="1.6"/>
      <text x="290" y="151" text-anchor="middle">3-SAT</text>
      <path d="M 320,90 L 290,130" stroke="#888" stroke-width="1.4" fill="none" marker-end="url(#arr-np)"/>
    </g>
    <!-- level 3: children of 3-SAT -->
    <g font-family="var(--mono), ui-monospace" font-size="12">
      <rect x="50"  y="210" width="100" height="32" rx="6" fill="#fff" stroke="var(--accent-strong)" stroke-width="1.4"/>
      <text x="100" y="231" text-anchor="middle">CLIQUE</text>
      <path d="M 270,162 L 110,210" stroke="#888" stroke-width="1.4" fill="none" marker-end="url(#arr-np)"/>

      <rect x="170" y="210" width="100" height="32" rx="6" fill="#fff" stroke="var(--accent-strong)" stroke-width="1.4"/>
      <text x="220" y="231" text-anchor="middle">SUBSET-SUM</text>
      <path d="M 285,162 L 230,210" stroke="#888" stroke-width="1.4" fill="none" marker-end="url(#arr-np)"/>

      <rect x="290" y="210" width="100" height="32" rx="6" fill="#fff" stroke="var(--accent-strong)" stroke-width="1.4"/>
      <text x="340" y="231" text-anchor="middle">HAM-PATH</text>
      <path d="M 305,162 L 340,210" stroke="#888" stroke-width="1.4" fill="none" marker-end="url(#arr-np)"/>

      <rect x="410" y="210" width="100" height="32" rx="6" fill="#fff" stroke="var(--accent-strong)" stroke-width="1.4"/>
      <text x="460" y="231" text-anchor="middle">3-COLOR</text>
      <path d="M 325,162 L 450,210" stroke="#888" stroke-width="1.4" fill="none" marker-end="url(#arr-np)"/>

      <rect x="530" y="210" width="100" height="32" rx="6" fill="#fff" stroke="var(--accent-strong)" stroke-width="1.4"/>
      <text x="580" y="231" text-anchor="middle">PARTITION</text>
      <path d="M 340,162 L 555,210" stroke="#888" stroke-width="1.4" fill="none" marker-end="url(#arr-np)"/>
    </g>
    <!-- level 4: VC, TSP, … -->
    <g font-family="var(--mono), ui-monospace" font-size="12">
      <rect x="80"  y="280" width="120" height="32" rx="6" fill="#fff" stroke="#888" stroke-width="1.4"/>
      <text x="140" y="301" text-anchor="middle">VERTEX-COVER</text>
      <path d="M 100,242 L 140,280" stroke="#888" stroke-width="1.4" fill="none" marker-end="url(#arr-np)"/>

      <rect x="220" y="280" width="100" height="32" rx="6" fill="#fff" stroke="#888" stroke-width="1.4"/>
      <text x="270" y="301" text-anchor="middle">KNAPSACK</text>
      <path d="M 220,242 L 250,280" stroke="#888" stroke-width="1.4" fill="none" marker-end="url(#arr-np)"/>

      <rect x="340" y="280" width="100" height="32" rx="6" fill="#fff" stroke="#888" stroke-width="1.4"/>
      <text x="390" y="301" text-anchor="middle">TSP</text>
      <path d="M 340,242 L 380,280" stroke="#888" stroke-width="1.4" fill="none" marker-end="url(#arr-np)"/>
    </g>
    <defs>
      <marker id="arr-np" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
        <polygon points="0 0, 8 3, 0 6" fill="#888"/>
      </marker>
    </defs>
    <text x="320" y="345" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-style="italic" fill="#666">
      Edge A → B means "we know a polynomial-time reduction A → B, so B is at least as hard as A."
    </text>
  </svg>
  <figcaption>The NP-completeness family tree rooted at SAT. Every edge is a known polynomial-time reduction. Karp's 1972 paper added 21 such reductions in one stroke; today the tree has hundreds of nodes.</figcaption>
</figure>
"""

COOK_LEVIN_TABLEAU = """
<figure class="diagram">
  <svg viewBox="0 0 640 320" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      Cook–Levin · the verifier's tableau becomes a SAT formula
    </text>
    <!-- grid 7 rows x 9 cols -->""" + ''.join(
    f'<rect x="{80 + col*55}" y="{50 + row*30}" width="55" height="30" fill="#fff" stroke="#ddd" stroke-width="0.7"/>'
    for row in range(7) for col in range(9)
) + """
    <!-- row labels -->
    <g font-family="var(--mono), ui-monospace" font-size="11" fill="#888">
      <text x="72" y="69"  text-anchor="end">t=0</text>
      <text x="72" y="99"  text-anchor="end">t=1</text>
      <text x="72" y="129" text-anchor="end">t=2</text>
      <text x="72" y="159" text-anchor="end">t=3</text>
      <text x="72" y="189" text-anchor="end">⋮</text>
      <text x="72" y="219" text-anchor="end">t=k</text>
      <text x="72" y="249" text-anchor="end">⋮</text>
    </g>
    <!-- column labels -->
    <g font-family="var(--mono), ui-monospace" font-size="10" fill="#888">""" + ''.join(
    f'<text x="{108 + i*55}" y="45" text-anchor="middle">cell {i}</text>'
    for i in range(9)
) + """</g>
    <!-- fill start configuration -->
    <text x="107" y="69" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" font-weight="700" fill="var(--info)">q&#8320;</text>
    <text x="162" y="69" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">x&#8321;</text>
    <text x="217" y="69" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">x&#8322;</text>
    <text x="272" y="69" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13">x&#8323;</text>
    <text x="327" y="69" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" fill="#aaa">_</text>
    <text x="382" y="69" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" fill="var(--gold)">c&#8321;</text>
    <text x="437" y="69" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" fill="var(--gold)">c&#8322;</text>
    <text x="492" y="69" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" fill="var(--gold)">c&#8323;</text>
    <text x="547" y="69" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" fill="#aaa">…</text>
    <!-- highlight 2x3 window -->
    <rect x="162" y="98" width="167" height="62" fill="none" stroke="var(--warn-strong, #b95825)" stroke-width="2" stroke-dasharray="4 3"/>
    <text x="340" y="135" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="var(--warn-strong, #b95825)">2×3 window → SAT clause</text>
    <!-- accept marker -->
    <rect x="270" y="208" width="55" height="30" fill="var(--accent-soft)" stroke="var(--accent-strong)" stroke-width="2"/>
    <text x="297" y="227" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" font-weight="700" fill="var(--accent-strong)">q&#8336;</text>
    <text x="370" y="225" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="var(--accent-strong)">∃ accept somewhere</text>
    <!-- caption -->
    <text x="320" y="290" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-style="italic" fill="#666">
      Variables: x<tspan baseline-shift="sub" font-size="0.75em">t,p,s</tspan> = "cell (t,p) holds symbol s". Clauses: each 2×3 window must be δ-consistent.
    </text>
    <text x="320" y="308" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" fill="#888">
      Polynomial in |w| ⇒ NP ≤<tspan baseline-shift="sub" font-size="0.75em">p</tspan> SAT.
    </text>
  </svg>
  <figcaption>The verifier V running on input x with certificate c sweeps a tape over polynomial time. Each row is a configuration; each 2×3 window must follow δ. Converting each window into a SAT clause produces a formula φ<sub>x</sub> that is satisfiable iff some certificate makes V accept. Every NP problem reduces this way.</figcaption>
</figure>
"""

# ============================================================
# MODULE 6 — Space, PSPACE, games
# ============================================================

TIME_VS_SPACE = """
<figure class="diagram">
  <svg viewBox="0 0 640 320" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      Time vs space · the diagonal of complexity
    </text>
    <!-- axes -->
    <line x1="80" y1="270" x2="600" y2="270" stroke="#888" stroke-width="1.4"/>
    <line x1="80" y1="60"  x2="80" y2="270"  stroke="#888" stroke-width="1.4"/>
    <text x="600" y="290" text-anchor="end" font-family="var(--sans), system-ui" font-size="12" fill="#666">SPACE →</text>
    <text x="78" y="55" text-anchor="end" font-family="var(--sans), system-ui" font-size="12" fill="#666">TIME ↑</text>
    <!-- labels along axes -->
    <text x="160" y="290" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="11" fill="#888">log n</text>
    <text x="280" y="290" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="11" fill="#888">poly</text>
    <text x="450" y="290" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="11" fill="#888">exp</text>
    <text x="70"  y="265" text-anchor="end" font-family="var(--mono), ui-monospace" font-size="11" fill="#888">poly</text>
    <text x="70"  y="155" text-anchor="end" font-family="var(--mono), ui-monospace" font-size="11" fill="#888">exp</text>
    <text x="70"  y="75"  text-anchor="end" font-family="var(--mono), ui-monospace" font-size="11" fill="#888">2^poly</text>
    <!-- regions -->
    <!-- L (low time low space) -->
    <rect x="100" y="240" width="100" height="30" fill="#d6ebe4" stroke="#1c4a3f" stroke-width="1.4"/>
    <text x="150" y="259" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="12" font-weight="700" fill="#1c4a3f">L · NL</text>
    <!-- P -->
    <rect x="100" y="200" width="200" height="40" fill="#e8f0ec" stroke="#1c4a3f" stroke-width="1.4"/>
    <text x="200" y="225" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" font-weight="700" fill="#1c4a3f">P</text>
    <!-- NP -->
    <rect x="100" y="160" width="270" height="40" fill="var(--accent-soft)" stroke="var(--accent-strong)" stroke-width="1.4"/>
    <text x="235" y="186" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" font-weight="700" fill="var(--accent-strong)">NP (and coNP)</text>
    <!-- PSPACE -->
    <rect x="100" y="120" width="350" height="40" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="1.6"/>
    <text x="275" y="146" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" font-weight="700" fill="var(--gold)">PSPACE = NPSPACE</text>
    <!-- EXPTIME -->
    <rect x="100" y="80" width="490" height="40" fill="#f4dfcf" stroke="var(--warn-strong, #b95825)" stroke-width="1.6"/>
    <text x="345" y="106" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="13" font-weight="700" fill="var(--warn-strong, #b95825)">EXPTIME ⊆ EXPSPACE</text>
    <!-- inclusion ladder annotation -->
    <text x="500" y="265" font-family="var(--sans), system-ui" font-size="11" fill="#666">L ⊆ NL ⊆ P ⊆ NP ⊆ PSPACE ⊆ EXPTIME</text>
    <text x="500" y="246" font-family="var(--sans), system-ui" font-size="10" font-style="italic" fill="#666">strict at hierarchy gaps only</text>
  </svg>
  <figcaption>Roughly: space ≤ time, but time ≤ 2^O(space). Polynomial time fits inside polynomial space; polynomial space gives exponential time. The diagonal of complexity is dominated by these two trade-offs.</figcaption>
</figure>
"""

SAVITCH_RECURSION_TREE = """
<figure class="diagram">
  <svg viewBox="0 0 640 320" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      Savitch's recursion tree · log depth × O(f) bits per frame = O(f²) space
    </text>
    <!-- root -->
    <circle cx="320" cy="60" r="16" fill="var(--gold)" stroke="var(--gold)" stroke-width="2"/>
    <text x="320" y="65" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="11" font-weight="700" fill="#fff">A→B, t</text>
    <!-- level 2 -->
    <line x1="320" y1="76" x2="180" y2="120" stroke="#888" stroke-width="1.4"/>
    <line x1="320" y1="76" x2="460" y2="120" stroke="#888" stroke-width="1.4"/>
    <circle cx="180" cy="130" r="14" fill="var(--accent)" stroke="var(--accent-strong)" stroke-width="1.5"/>
    <text x="180" y="134" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="10" fill="#fff">A→M, t/2</text>
    <circle cx="460" cy="130" r="14" fill="var(--accent)" stroke="var(--accent-strong)" stroke-width="1.5"/>
    <text x="460" y="134" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="10" fill="#fff">M→B, t/2</text>
    <!-- level 3 -->""" + ''.join(
    f'<line x1="{180 + i*280}" y1="144" x2="{120 + i*280 + j*120}" y2="180" stroke="#888" stroke-width="1.2"/>' +
    f'<circle cx="{120 + i*280 + j*120}" cy="190" r="11" fill="#fff" stroke="#888" stroke-width="1.4"/>'
    for i in [0, 1] for j in [0, 1]
) + """
    <!-- level 4 (leaves) -->""" + ''.join(
    f'<line x1="{120 + i*120}" y1="200" x2="{100 + i*120 + j*60}" y2="240" stroke="#ccc" stroke-width="0.8"/>' +
    f'<circle cx="{100 + i*120 + j*60}" cy="248" r="6" fill="#eee" stroke="#bbb"/>'
    for i in range(4) for j in range(2)
) + """
    <!-- side annotations -->
    <text x="540" y="65"  font-family="var(--sans), system-ui" font-size="11" fill="#666">level 0 · t = full</text>
    <text x="540" y="135" font-family="var(--sans), system-ui" font-size="11" fill="#666">level 1 · t/2</text>
    <text x="540" y="195" font-family="var(--sans), system-ui" font-size="11" fill="#666">level 2 · t/4</text>
    <text x="540" y="252" font-family="var(--sans), system-ui" font-size="11" fill="#666">…log t levels</text>
    <!-- bracket showing stack depth -->
    <line x1="40" y1="60" x2="40" y2="250" stroke="var(--warn-strong, #b95825)" stroke-width="2"/>
    <text x="30" y="160" text-anchor="end" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="var(--warn-strong, #b95825)">depth = log t = O(f(n))</text>
    <text x="320" y="295" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-style="italic" fill="#666">
      Exponentially many nodes, but only one root-to-leaf path lives on the stack at a time.
    </text>
  </svg>
  <figcaption>Savitch's recursion tree has 2^(log t) leaves — exponentially many nodes — but at any moment only a single root-to-leaf path occupies the call stack. log t × O(f) bits per frame = O(f²) space, proving NSPACE(f) ⊆ SPACE(f²).</figcaption>
</figure>
"""

TQBF_GAME_TREE = """
<figure class="diagram">
  <svg viewBox="0 0 640 320" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      TQBF game tree · ∃x∀y∃z. φ(x,y,z) evaluated bottom-up
    </text>
    <!-- root: exists x -->
    <circle cx="320" cy="55" r="22" fill="var(--accent-soft)" stroke="var(--accent-strong)" stroke-width="2.5"/>
    <text x="320" y="62" text-anchor="middle" font-family="var(--sans), system-ui" font-size="18" fill="var(--accent-strong)">∃</text>
    <text x="320" y="40" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="11" fill="#1a1a1a">x</text>
    <!-- branches: x=0, x=1 -->
    <line x1="304" y1="68"  x2="160" y2="115" stroke="#888" stroke-width="1.4"/>
    <text x="225" y="90" font-family="var(--mono), ui-monospace" font-size="11" fill="#888">x=0</text>
    <line x1="336" y1="68"  x2="480" y2="115" stroke="#888" stroke-width="1.4"/>
    <text x="410" y="90" font-family="var(--mono), ui-monospace" font-size="11" fill="#888">x=1</text>
    <!-- universal y -->
    <circle cx="160" cy="130" r="20" fill="var(--warn-soft)" stroke="var(--warn-strong, #b95825)" stroke-width="2"/>
    <text x="160" y="136" text-anchor="middle" font-family="var(--sans), system-ui" font-size="16" fill="var(--warn-strong, #b95825)">∀</text>
    <text x="160" y="115" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="10" fill="#1a1a1a">y</text>
    <circle cx="480" cy="130" r="20" fill="var(--warn-soft)" stroke="var(--warn-strong, #b95825)" stroke-width="2"/>
    <text x="480" y="136" text-anchor="middle" font-family="var(--sans), system-ui" font-size="16" fill="var(--warn-strong, #b95825)">∀</text>
    <text x="480" y="115" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="10" fill="#1a1a1a">y</text>
    <!-- branches: y=0, y=1 for left ∀ -->
    <line x1="148" y1="142" x2="80"  y2="180" stroke="#888" stroke-width="1.2"/>
    <line x1="172" y1="142" x2="240" y2="180" stroke="#888" stroke-width="1.2"/>
    <line x1="468" y1="142" x2="400" y2="180" stroke="#888" stroke-width="1.2"/>
    <line x1="492" y1="142" x2="560" y2="180" stroke="#888" stroke-width="1.2"/>
    <!-- existential z -->""" + ''.join(
    f'<circle cx="{80 + i*160}" cy="195" r="16" fill="var(--accent-soft)" stroke="var(--accent-strong)" stroke-width="1.6"/>' +
    f'<text x="{80 + i*160}" y="201" text-anchor="middle" font-family="var(--sans), system-ui" font-size="13" fill="var(--accent-strong)">∃</text>'
    for i in range(4)
) + """
    <!-- leaves: phi values -->""" + ''.join(
    f'<rect x="{50 + i*45}" y="240" width="30" height="22" fill="{"#d6ebe4" if (i % 3 == 0) else "#f4dfcf"}" stroke="{"#1c4a3f" if (i % 3 == 0) else "var(--warn-strong, #b95825)"}" stroke-width="1.2"/>' +
    f'<text x="{65 + i*45}" y="257" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="12" font-weight="700" fill="{"#1c4a3f" if (i % 3 == 0) else "var(--warn-strong, #b95825)"}">{1 if (i % 3 == 0) else 0}</text>'
    for i in range(13)
) + """
    <!-- legend -->
    <rect x="80" y="285" width="14" height="14" fill="var(--accent-soft)" stroke="var(--accent-strong)"/>
    <text x="100" y="296" font-family="var(--sans), system-ui" font-size="11" fill="#1a1a1a">∃ node = OR</text>
    <rect x="220" y="285" width="14" height="14" fill="var(--warn-soft)" stroke="var(--warn-strong, #b95825)"/>
    <text x="240" y="296" font-family="var(--sans), system-ui" font-size="11" fill="#1a1a1a">∀ node = AND</text>
    <text x="400" y="296" font-family="var(--sans), system-ui" font-size="11" fill="#666" font-style="italic">depth-first eval · O(n) space</text>
  </svg>
  <figcaption>A TQBF formula is true iff there is a winning strategy for the existential player in this game tree. ∃ nodes are OR, ∀ nodes are AND. Polynomial depth, exponential tree — depth-first evaluation needs only polynomial space.</figcaption>
</figure>
"""

# ============================================================
# MODULE 7 — L, NL, hierarchy
# ============================================================

FULL_COMPLEXITY_ZOO = """
<figure class="diagram">
  <svg viewBox="0 0 640 360" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      The complexity zoo · everything from L to EXPSPACE
    </text>
    <!-- nested ellipses, biggest first -->
    <!-- EXPSPACE -->
    <ellipse cx="320" cy="190" rx="290" ry="150" fill="#fefaf3" stroke="#444" stroke-width="1.4"/>
    <text x="50" y="80" font-family="var(--mono), ui-monospace" font-size="13" font-weight="700" fill="#444">EXPSPACE</text>
    <!-- EXPTIME -->
    <ellipse cx="320" cy="195" rx="245" ry="125" fill="#f4dfcf" stroke="var(--warn-strong, #b95825)" stroke-width="1.6"/>
    <text x="92" y="105" font-family="var(--mono), ui-monospace" font-size="12" font-weight="700" fill="var(--warn-strong, #b95825)">EXPTIME</text>
    <!-- PSPACE -->
    <ellipse cx="320" cy="200" rx="200" ry="100" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="1.6"/>
    <text x="140" y="130" font-family="var(--mono), ui-monospace" font-size="12" font-weight="700" fill="var(--gold)">PSPACE</text>
    <!-- NP -->
    <ellipse cx="270" cy="205" rx="100" ry="65" fill="var(--accent-soft)" stroke="var(--accent-strong)" stroke-width="1.6"/>
    <text x="195" y="170" font-family="var(--mono), ui-monospace" font-size="12" font-weight="700" fill="var(--accent-strong)">NP</text>
    <!-- P -->
    <ellipse cx="240" cy="215" rx="60" ry="38" fill="#d6ebe4" stroke="#1c4a3f" stroke-width="1.6"/>
    <text x="230" y="200" font-family="var(--mono), ui-monospace" font-size="12" font-weight="700" fill="#1c4a3f">P</text>
    <!-- NL -->
    <ellipse cx="225" cy="225" rx="30" ry="22" fill="#fff" stroke="#1c4a3f" stroke-width="1.4"/>
    <text x="225" y="229" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="11" font-weight="700" fill="#1c4a3f">NL</text>
    <!-- L (inside NL) -->
    <ellipse cx="218" cy="230" rx="15" ry="10" fill="#fcfbf7" stroke="#1c4a3f" stroke-width="1.2"/>
    <text x="218" y="234" text-anchor="middle" font-family="var(--mono), ui-monospace" font-size="9" fill="#1c4a3f">L</text>
    <!-- complete-problem markers -->
    <g font-family="var(--mono), ui-monospace" font-size="11">
      <!-- PATH in NL -->
      <text x="320" y="222" font-size="10" fill="var(--accent-strong)">↓ PATH ∈ NL-c</text>
      <!-- SAT in NP -->
      <text x="345" y="195" font-size="10" fill="var(--accent-strong)">↑ SAT ∈ NP-c</text>
      <!-- TQBF in PSPACE -->
      <text x="395" y="155" font-size="10" fill="var(--gold)">↑ TQBF ∈ PSPACE-c</text>
      <!-- Generalized chess in EXPTIME -->
      <text x="450" y="125" font-size="10" fill="var(--warn-strong, #b95825)">↑ Gen. chess ∈ EXPTIME-c</text>
      <!-- REGEX-eq in EXPSPACE -->
      <text x="495" y="92" font-size="10" fill="#444">↑ REGEX-EQ ∈ EXPSPACE-c</text>
    </g>
    <!-- strict separations -->
    <text x="320" y="345" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11.5" fill="#1a1a1a">
      <tspan font-weight="700">strict by hierarchy:</tspan> L ⊊ PSPACE · P ⊊ EXPTIME · PSPACE ⊊ EXPSPACE
    </text>
  </svg>
  <figcaption>The full nested-ovals map of complexity classes. Strict containments between adjacent classes are mostly open (P vs NP, NP vs PSPACE, PSPACE vs EXPTIME) — but the hierarchy theorems give us at least L ⊊ PSPACE, P ⊊ EXPTIME, and PSPACE ⊊ EXPSPACE.</figcaption>
</figure>
"""

HIERARCHY_DIAGONAL = """
<figure class="diagram">
  <svg viewBox="0 0 640 300" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      Hierarchy theorem · D diagonalizes against every M<tspan baseline-shift="sub" font-size="0.75em">i</tspan> in SPACE(f)
    </text>
    <!-- header -->
    <g font-family="var(--mono), ui-monospace" font-size="12" fill="#888">
      <text x="100" y="55">M&#8345;</text>
      <text x="200" y="55">⟨M&#8321;⟩</text>
      <text x="270" y="55">⟨M&#8322;⟩</text>
      <text x="340" y="55">⟨M&#8323;⟩</text>
      <text x="410" y="55">⟨M&#8324;⟩</text>
      <text x="480" y="55">⟨M&#8325;⟩</text>
      <text x="540" y="55">…</text>
    </g>
    <line x1="170" y1="62" x2="570" y2="62" stroke="#888" stroke-width="1"/>
    <!-- rows -->
    <g font-family="var(--mono), ui-monospace" font-size="12">
      <text x="100" y="90" font-weight="700">M&#8321;</text>
      <rect x="185" y="75" width="30" height="20" fill="var(--gold-soft)" stroke="var(--gold)"/>
      <text x="200" y="90" text-anchor="middle" font-weight="700" fill="var(--gold)">1</text>
      <text x="270" y="90" text-anchor="middle">0</text>
      <text x="340" y="90" text-anchor="middle">1</text>
      <text x="410" y="90" text-anchor="middle">1</text>
      <text x="480" y="90" text-anchor="middle">0</text>

      <text x="100" y="120" font-weight="700">M&#8322;</text>
      <text x="200" y="120" text-anchor="middle">0</text>
      <rect x="255" y="105" width="30" height="20" fill="var(--gold-soft)" stroke="var(--gold)"/>
      <text x="270" y="120" text-anchor="middle" font-weight="700" fill="var(--gold)">0</text>
      <text x="340" y="120" text-anchor="middle">1</text>
      <text x="410" y="120" text-anchor="middle">0</text>
      <text x="480" y="120" text-anchor="middle">1</text>

      <text x="100" y="150" font-weight="700">M&#8323;</text>
      <text x="200" y="150" text-anchor="middle">1</text>
      <text x="270" y="150" text-anchor="middle">1</text>
      <rect x="325" y="135" width="30" height="20" fill="var(--gold-soft)" stroke="var(--gold)"/>
      <text x="340" y="150" text-anchor="middle" font-weight="700" fill="var(--gold)">1</text>
      <text x="410" y="150" text-anchor="middle">0</text>
      <text x="480" y="150" text-anchor="middle">0</text>

      <text x="100" y="180" font-weight="700">M&#8324;</text>
      <text x="200" y="180" text-anchor="middle">1</text>
      <text x="270" y="180" text-anchor="middle">0</text>
      <text x="340" y="180" text-anchor="middle">1</text>
      <rect x="395" y="165" width="30" height="20" fill="var(--gold-soft)" stroke="var(--gold)"/>
      <text x="410" y="180" text-anchor="middle" font-weight="700" fill="var(--gold)">1</text>
      <text x="480" y="180" text-anchor="middle">1</text>

      <text x="100" y="210" font-weight="700">M&#8325;</text>
      <text x="200" y="210" text-anchor="middle">0</text>
      <text x="270" y="210" text-anchor="middle">1</text>
      <text x="340" y="210" text-anchor="middle">0</text>
      <text x="410" y="210" text-anchor="middle">1</text>
      <rect x="465" y="195" width="30" height="20" fill="var(--gold-soft)" stroke="var(--gold)"/>
      <text x="480" y="210" text-anchor="middle" font-weight="700" fill="var(--gold)">1</text>
    </g>
    <!-- D row -->
    <line x1="170" y1="225" x2="570" y2="225" stroke="var(--warn-strong, #b95825)" stroke-width="2"/>
    <g font-family="var(--mono), ui-monospace" font-size="12" fill="var(--warn-strong, #b95825)">
      <text x="100" y="250" font-weight="700">D</text>
      <text x="200" y="250" text-anchor="middle" font-weight="700">0</text>
      <text x="270" y="250" text-anchor="middle" font-weight="700">1</text>
      <text x="340" y="250" text-anchor="middle" font-weight="700">0</text>
      <text x="410" y="250" text-anchor="middle" font-weight="700">0</text>
      <text x="480" y="250" text-anchor="middle" font-weight="700">0</text>
      <text x="540" y="250">…</text>
    </g>
    <text x="320" y="285" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-style="italic" fill="#666">
      D disagrees with every M<tspan baseline-shift="sub" font-size="0.75em">i</tspan> at column i ⇒ D ∉ SPACE(f). But D ∈ SPACE(f · log f).
    </text>
  </svg>
  <figcaption>The space hierarchy theorem is proved by diagonalization. We enumerate all SPACE(f) machines, then build D that disagrees with each on its own description. D uses slightly more space (a log factor) — exactly the gap between SPACE(f) and SPACE(f log f).</figcaption>
</figure>
"""

# ============================================================
# CSS (injected once per file inside <head>)
# ============================================================

DIAGRAM_CSS = """
<style>
.diagram {
  margin: 18px 0;
  padding: 12px 14px;
  background: #fcfbf7;
  border: 1px solid var(--rule, #eee);
  border-left: 4px solid var(--gold, #c89933);
  border-radius: 8px;
}
.diagram svg {
  width: 100%;
  height: auto;
  max-height: 360px;
  display: block;
}
.diagram figcaption {
  margin-top: 10px;
  font-family: var(--sans, system-ui), sans-serif;
  font-size: 12.5px;
  line-height: 1.55;
  color: var(--ink-soft, #555);
}
</style>
"""
