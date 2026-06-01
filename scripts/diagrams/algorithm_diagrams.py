"""Sipser-style algorithm visualisations: actual machines, tapes, and configurations.

Each diagram tells the proof's story visually — DFA state diagrams, TM tapes with
head pointers, multi-frame "simulation snapshots", encoded ⟨M⟩ on tape, etc.
"""

# ============================================================
# A_DFA · DFA picture + TM tape + 3 simulation snapshots
# ============================================================

ALGO_ADFA = """
<figure class="diagram">
  <svg viewBox="0 0 700 480" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <defs>
      <marker id="arr-adfa" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
        <polygon points="0 0, 8 3, 0 6" fill="#444"/>
      </marker>
      <marker id="arr-adfa-acc" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
        <polygon points="0 0, 8 3, 0 6" fill="var(--accent-strong, #1c4a3f)"/>
      </marker>
    </defs>

    <text x="350" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      A<tspan baseline-shift="sub" font-size="0.75em">DFA</tspan> is decidable · build TM M that simulates B on w
    </text>

    <!-- ============ ROW 1: The DFA B and the input w ============ -->

    <!-- DFA panel -->
    <text x="20" y="58" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="#1a1a1a">
      Example DFA B · accepts strings with an even number of 0s
    </text>
    <!-- q0 (accept, double-circled) -->
    <circle cx="110" cy="110" r="26" fill="var(--accent-soft)" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2"/>
    <circle cx="110" cy="110" r="20" fill="none" stroke="var(--accent-strong, #1c4a3f)" stroke-width="1.5"/>
    <text x="110" y="115" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="14" font-weight="700">q₀</text>
    <text x="110" y="155" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="var(--accent-strong, #1c4a3f)" font-weight="700">accept · even</text>
    <!-- start arrow -->
    <path d="M 50,110 L 82,110" stroke="#444" stroke-width="1.6" marker-end="url(#arr-adfa)"/>
    <text x="40" y="105" font-family="var(--sans), system-ui" font-size="10" fill="#666">start</text>
    <!-- q1 (reject) -->
    <circle cx="230" cy="110" r="26" fill="#fff" stroke="#1a1a1a" stroke-width="2"/>
    <text x="230" y="115" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="14" font-weight="700">q₁</text>
    <text x="230" y="155" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">reject · odd</text>
    <!-- q0→q1 on 0 -->
    <path d="M 136,100 Q 170,80 204,100" fill="none" stroke="#444" stroke-width="1.5" marker-end="url(#arr-adfa)"/>
    <text x="170" y="78" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="12" font-weight="700">0</text>
    <!-- q1→q0 on 0 -->
    <path d="M 204,120 Q 170,140 136,120" fill="none" stroke="#444" stroke-width="1.5" marker-end="url(#arr-adfa)"/>
    <text x="170" y="150" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="12" font-weight="700">0</text>
    <!-- q0 self loop on 1 -->
    <path d="M 95,86 Q 75,55 110,55 Q 130,60 125,86" fill="none" stroke="#888" stroke-width="1.3" marker-end="url(#arr-adfa)"/>
    <text x="100" y="48" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="12" font-weight="700" fill="#666">1</text>
    <!-- q1 self loop on 1 -->
    <path d="M 215,86 Q 195,55 230,55 Q 250,60 245,86" fill="none" stroke="#888" stroke-width="1.3" marker-end="url(#arr-adfa)"/>
    <text x="220" y="48" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="12" font-weight="700" fill="#666">1</text>

    <!-- Input string panel -->
    <text x="350" y="58" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="#1a1a1a">
      Input string w = "0110":
    </text>
    <!-- 4 tape cells -->
    <g font-family="var(--mono), ui-monospace, monospace" font-size="16" font-weight="700">
      <rect x="350" y="70" width="40" height="50" fill="white" stroke="#444" stroke-width="1.5"/>
      <text x="370" y="103" text-anchor="middle">0</text>
      <rect x="390" y="70" width="40" height="50" fill="white" stroke="#444" stroke-width="1.5"/>
      <text x="410" y="103" text-anchor="middle">1</text>
      <rect x="430" y="70" width="40" height="50" fill="white" stroke="#444" stroke-width="1.5"/>
      <text x="450" y="103" text-anchor="middle">1</text>
      <rect x="470" y="70" width="40" height="50" fill="white" stroke="#444" stroke-width="1.5"/>
      <text x="490" y="103" text-anchor="middle">0</text>
    </g>

    <!-- The TM M -->
    <text x="540" y="58" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="#1a1a1a">
      TM M (on its tape):
    </text>
    <rect x="535" y="70" width="150" height="80" rx="10" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="2"/>
    <text x="610" y="96" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="12" font-weight="700" fill="var(--gold)">M reads ⟨B⟩</text>
    <text x="610" y="114" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">stores δ, q₀, F</text>
    <text x="610" y="128" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">in its work area;</text>
    <text x="610" y="142" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">walks w left→right</text>

    <!-- Divider line -->
    <line x1="20" y1="190" x2="680" y2="190" stroke="#ddd" stroke-width="1"/>

    <!-- ============ ROW 2: Three simulation snapshots ============ -->
    <text x="350" y="215" text-anchor="middle" font-family="var(--sans), system-ui" font-size="13" font-weight="700" fill="#1a1a1a">
      Simulation of M on input ⟨B, "0110"⟩ — three snapshots
    </text>

    <!-- SNAPSHOT 1: t=0, head on cell 0, state q0 -->
    <g transform="translate(20, 240)">
      <text x="0" y="0" font-family="var(--mono), ui-monospace, monospace" font-size="11" font-weight="700" fill="#666">t = 0</text>
      <!-- 4-cell tape -->
      <g font-family="var(--mono), ui-monospace, monospace" font-size="13">
        <rect x="0" y="10" width="32" height="36" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="2"/>
        <text x="16" y="35" text-anchor="middle" font-weight="700">0</text>
        <rect x="32" y="10" width="32" height="36" fill="white" stroke="#888"/>
        <text x="48" y="35" text-anchor="middle">1</text>
        <rect x="64" y="10" width="32" height="36" fill="white" stroke="#888"/>
        <text x="80" y="35" text-anchor="middle">1</text>
        <rect x="96" y="10" width="32" height="36" fill="white" stroke="#888"/>
        <text x="112" y="35" text-anchor="middle">0</text>
      </g>
      <!-- head arrow -->
      <path d="M 16,60 L 16,50" stroke="var(--warn-strong, #b95825)" stroke-width="2.5" marker-end="url(#arr-adfa-acc)"/>
      <text x="16" y="75" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" font-weight="700" fill="var(--warn-strong, #b95825)">head</text>
      <!-- state -->
      <text x="60" y="100" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="13">B-state: <tspan font-weight="700" fill="var(--accent-strong, #1c4a3f)">q₀</tspan></text>
    </g>

    <!-- SNAPSHOT 2: t=2, after reading 0, 1 -->
    <g transform="translate(260, 240)">
      <text x="0" y="0" font-family="var(--mono), ui-monospace, monospace" font-size="11" font-weight="700" fill="#666">t = 2 · after reading "01"</text>
      <g font-family="var(--mono), ui-monospace, monospace" font-size="13">
        <rect x="0" y="10" width="32" height="36" fill="#eee" stroke="#888"/>
        <text x="16" y="35" text-anchor="middle" fill="#888">0</text>
        <rect x="32" y="10" width="32" height="36" fill="#eee" stroke="#888"/>
        <text x="48" y="35" text-anchor="middle" fill="#888">1</text>
        <rect x="64" y="10" width="32" height="36" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="2"/>
        <text x="80" y="35" text-anchor="middle" font-weight="700">1</text>
        <rect x="96" y="10" width="32" height="36" fill="white" stroke="#888"/>
        <text x="112" y="35" text-anchor="middle">0</text>
      </g>
      <path d="M 80,60 L 80,50" stroke="var(--warn-strong, #b95825)" stroke-width="2.5" marker-end="url(#arr-adfa-acc)"/>
      <text x="80" y="75" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" font-weight="700" fill="var(--warn-strong, #b95825)">head</text>
      <text x="60" y="100" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="13">B-state: <tspan font-weight="700" fill="var(--warn-strong, #b95825)">q₁</tspan></text>
      <text x="60" y="116" text-anchor="middle" font-family="var(--sans), system-ui" font-size="9" fill="#666">(δ(q₀,0)=q₁, δ(q₁,1)=q₁)</text>
    </g>

    <!-- SNAPSHOT 3: t=4, end of input -->
    <g transform="translate(500, 240)">
      <text x="0" y="0" font-family="var(--mono), ui-monospace, monospace" font-size="11" font-weight="700" fill="#666">t = 4 · end of input</text>
      <g font-family="var(--mono), ui-monospace, monospace" font-size="13">
        <rect x="0" y="10" width="32" height="36" fill="#eee" stroke="#888"/>
        <text x="16" y="35" text-anchor="middle" fill="#888">0</text>
        <rect x="32" y="10" width="32" height="36" fill="#eee" stroke="#888"/>
        <text x="48" y="35" text-anchor="middle" fill="#888">1</text>
        <rect x="64" y="10" width="32" height="36" fill="#eee" stroke="#888"/>
        <text x="80" y="35" text-anchor="middle" fill="#888">1</text>
        <rect x="96" y="10" width="32" height="36" fill="#eee" stroke="#888"/>
        <text x="112" y="35" text-anchor="middle" fill="#888">0</text>
      </g>
      <path d="M 140,30 L 130,30" stroke="var(--warn-strong, #b95825)" stroke-width="2.5" marker-end="url(#arr-adfa-acc)"/>
      <text x="148" y="34" font-family="var(--sans), system-ui" font-size="10" font-weight="700" fill="var(--warn-strong, #b95825)">end</text>
      <text x="60" y="100" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="13">B-state: <tspan font-weight="700" fill="var(--accent-strong, #1c4a3f)">q₀</tspan></text>
      <text x="60" y="118" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" font-weight="700" fill="var(--accent-strong, #1c4a3f)">q₀ ∈ F → ACCEPT ✓</text>
    </g>

    <!-- Bottom caption -->
    <text x="350" y="395" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" fill="#1a1a1a">
      M never needs more than O(|w|) steps · the DFA's finite state set guarantees termination.
    </text>
    <text x="350" y="416" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-style="italic" fill="#666">
      Trace: q₀ →0→ q₁ →1→ q₁ →1→ q₁ →0→ q₀.  Ends in q₀ ∈ F, so "0110" ∈ L(B).
    </text>
  </svg>
  <figcaption>A<sub>DFA</sub> is decidable because we can build a Turing machine that <em>literally simulates</em> the DFA. Three snapshots show the simulation in motion: at each step, the head reads the next input symbol and the tracked B-state updates via δ. After all of w is consumed, the TM accepts iff the final B-state is in F.</figcaption>
</figure>
"""

# ============================================================
# EQ_DFA · two DFAs + product DFA grid + reachability search
# ============================================================

ALGO_EQDFA = """
<figure class="diagram">
  <svg viewBox="0 0 700 460" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <defs>
      <marker id="arr-eq" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
        <polygon points="0 0, 8 3, 0 6" fill="#444"/>
      </marker>
      <marker id="arr-eq-grn" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
        <polygon points="0 0, 8 3, 0 6" fill="var(--accent-strong, #1c4a3f)"/>
      </marker>
    </defs>

    <text x="350" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      EQ<tspan baseline-shift="sub" font-size="0.75em">DFA</tspan> is decidable · the product DFA, then test for emptiness
    </text>

    <!-- ============ ROW 1: Two DFAs A and B ============ -->

    <!-- DFA A -->
    <text x="20" y="58" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="var(--accent-strong, #1c4a3f)">
      DFA A · even # of 0s
    </text>
    <circle cx="60" cy="105" r="22" fill="var(--accent-soft)" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2"/>
    <circle cx="60" cy="105" r="17" fill="none" stroke="var(--accent-strong, #1c4a3f)" stroke-width="1.4"/>
    <text x="60" y="110" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="12" font-weight="700">a₀</text>
    <circle cx="160" cy="105" r="22" fill="white" stroke="#444" stroke-width="2"/>
    <text x="160" y="110" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="12" font-weight="700">a₁</text>
    <path d="M 82,96 Q 110,80 138,96" fill="none" stroke="#444" stroke-width="1.4" marker-end="url(#arr-eq)"/>
    <text x="110" y="76" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="11" font-weight="700">0</text>
    <path d="M 138,114 Q 110,130 82,114" fill="none" stroke="#444" stroke-width="1.4" marker-end="url(#arr-eq)"/>
    <text x="110" y="143" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="11" font-weight="700">0</text>
    <!-- self loops on 1 -->
    <path d="M 47,84 Q 30,55 60,55 Q 80,60 73,84" fill="none" stroke="#888" stroke-width="1.2" marker-end="url(#arr-eq)"/>
    <text x="55" y="48" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="10" fill="#666">1</text>
    <path d="M 147,84 Q 130,55 160,55 Q 180,60 173,84" fill="none" stroke="#888" stroke-width="1.2" marker-end="url(#arr-eq)"/>
    <text x="155" y="48" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="10" fill="#666">1</text>

    <!-- DFA B -->
    <text x="240" y="58" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="var(--info, #2f60a8)">
      DFA B · ends in 0
    </text>
    <circle cx="280" cy="105" r="22" fill="white" stroke="#444" stroke-width="2"/>
    <text x="280" y="110" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="12" font-weight="700">b₀</text>
    <circle cx="380" cy="105" r="22" fill="#d6e3f4" stroke="var(--info, #2f60a8)" stroke-width="2"/>
    <circle cx="380" cy="105" r="17" fill="none" stroke="var(--info, #2f60a8)" stroke-width="1.4"/>
    <text x="380" y="110" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="12" font-weight="700">b₁</text>
    <path d="M 302,96 Q 330,80 358,96" fill="none" stroke="#444" stroke-width="1.4" marker-end="url(#arr-eq)"/>
    <text x="330" y="76" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="11" font-weight="700">0</text>
    <path d="M 358,114 Q 330,130 302,114" fill="none" stroke="#444" stroke-width="1.4" marker-end="url(#arr-eq)"/>
    <text x="330" y="143" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="11" font-weight="700">1</text>
    <!-- self loops -->
    <path d="M 267,84 Q 250,55 280,55 Q 300,60 293,84" fill="none" stroke="#888" stroke-width="1.2" marker-end="url(#arr-eq)"/>
    <text x="275" y="48" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="10" fill="#666">1</text>
    <path d="M 367,84 Q 350,55 380,55 Q 400,60 393,84" fill="none" stroke="#888" stroke-width="1.2" marker-end="url(#arr-eq)"/>
    <text x="375" y="48" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="10" fill="#666">0</text>

    <!-- =, ↓ -->
    <text x="470" y="105" text-anchor="middle" font-family="var(--sans), system-ui" font-size="24" fill="#444">⊗</text>
    <text x="470" y="125" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">product</text>

    <!-- Product DFA C in a 2x2 grid -->
    <text x="540" y="58" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="var(--gold)">
      Product C · states (a, b)
    </text>
    <!-- 2x2 grid of paired states -->
    <g font-family="var(--mono), ui-monospace, monospace" font-size="11" font-weight="700">
      <!-- (a0,b0): start, a0 ∈ F_A only → XOR accept -->
      <rect x="510" y="70" width="60" height="36" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="2"/>
      <circle cx="540" cy="88" r="14" fill="none" stroke="var(--warn-strong, #b95825)" stroke-width="2"/>
      <text x="540" y="92" text-anchor="middle" font-size="10" fill="var(--warn-strong, #b95825)">(a₀,b₀)</text>
      <!-- (a0,b1): both accept -->
      <rect x="610" y="70" width="60" height="36" fill="#fff" stroke="#444"/>
      <text x="640" y="92" text-anchor="middle" font-size="10">(a₀,b₁)</text>
      <!-- (a1,b0): neither accept -->
      <rect x="510" y="120" width="60" height="36" fill="#fff" stroke="#444"/>
      <text x="540" y="142" text-anchor="middle" font-size="10">(a₁,b₀)</text>
      <!-- (a1,b1): b1 only → XOR accept -->
      <rect x="610" y="120" width="60" height="36" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="2"/>
      <circle cx="640" cy="138" r="14" fill="none" stroke="var(--warn-strong, #b95825)" stroke-width="2"/>
      <text x="640" y="142" text-anchor="middle" font-size="10" fill="var(--warn-strong, #b95825)">(a₁,b₁)</text>
    </g>
    <text x="590" y="178" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="var(--warn-strong, #b95825)" font-weight="700">
      circled = XOR accept
    </text>

    <!-- Divider line -->
    <line x1="20" y1="200" x2="680" y2="200" stroke="#ddd" stroke-width="1"/>

    <!-- ============ ROW 2: BFS reachability test ============ -->
    <text x="350" y="225" text-anchor="middle" font-family="var(--sans), system-ui" font-size="13" font-weight="700" fill="#1a1a1a">
      Now test if any XOR-accept state of C is reachable from the start state
    </text>

    <!-- C's transition graph laid out -->
    <g font-family="var(--mono), ui-monospace, monospace" font-size="11" font-weight="700">
      <!-- start state (a0,b0) -->
      <rect x="100" y="270" width="80" height="44" rx="6" fill="var(--accent-soft)" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2"/>
      <circle cx="140" cy="292" r="20" fill="none" stroke="var(--warn-strong, #b95825)" stroke-width="2"/>
      <text x="140" y="296" text-anchor="middle" fill="var(--warn-strong, #b95825)">(a₀,b₀)</text>
      <text x="140" y="262" text-anchor="middle" font-size="10" fill="#666">start</text>

      <!-- (a1,b1) reached on 0 -->
      <rect x="280" y="270" width="80" height="44" rx="6" fill="white" stroke="#444"/>
      <circle cx="320" cy="292" r="20" fill="none" stroke="var(--warn-strong, #b95825)" stroke-width="2"/>
      <text x="320" y="296" text-anchor="middle" fill="var(--warn-strong, #b95825)">(a₁,b₁)</text>

      <!-- (a0,b1) reached on 1 then 0 -->
      <rect x="460" y="270" width="80" height="44" rx="6" fill="white" stroke="#444"/>
      <text x="500" y="296" text-anchor="middle">(a₀,b₁)</text>

      <!-- (a1,b0) reached on 0 then 1 -->
      <rect x="100" y="360" width="80" height="44" rx="6" fill="white" stroke="#444"/>
      <text x="140" y="386" text-anchor="middle">(a₁,b₀)</text>
    </g>

    <!-- BFS arrows -->
    <path d="M 182,292 L 277,292" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2" marker-end="url(#arr-eq-grn)"/>
    <text x="225" y="285" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="11" font-weight="700" fill="var(--accent-strong, #1c4a3f)">0</text>

    <!-- BFS finds reachable XOR state -->
    <text x="320" y="345" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="var(--warn-strong, #b95825)">
      ✗ XOR-accept reachable
    </text>
    <text x="320" y="360" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="var(--warn-strong, #b95825)">
      ⇒ L(A) ≠ L(B)
    </text>
    <text x="320" y="378" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">
      Disagreement witness: "0" (A rejects, B accepts)
    </text>

    <!-- Bottom caption -->
    <text x="350" y="430" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-style="italic" fill="#666">
      L(A) = L(B) ⇔ no XOR-accept state of C is reachable from (a₀, b₀).
    </text>
  </svg>
  <figcaption>EQ<sub>DFA</sub> is decided by running two DFAs in lock-step. Each product state is a pair (aᵢ, bⱼ) — XOR-accept iff exactly one of aᵢ, bⱼ is accepting. Reachability of any XOR-accept state witnesses a disagreement; absence proves L(A) = L(B). Polynomial in |Q<sub>A</sub>| · |Q<sub>B</sub>|.</figcaption>
</figure>
"""

# ============================================================
# E_CFG marking — keep the existing rounds visualization (already good)
# ============================================================

ALGO_ECFG_MARKING = """
<figure class="diagram">
  <svg viewBox="0 0 700 360" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <defs>
      <marker id="arr-ecfg" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
        <polygon points="0 0, 8 3, 0 6" fill="var(--gold)"/>
      </marker>
    </defs>

    <text x="350" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      E<tspan baseline-shift="sub" font-size="0.75em">CFG</tspan> · propagate "productive" markings from terminals outward
    </text>

    <!-- Grammar box -->
    <rect x="20" y="50" width="200" height="160" rx="8" fill="white" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2"/>
    <text x="120" y="72" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="var(--accent-strong, #1c4a3f)">Grammar G</text>
    <g font-family="var(--mono), ui-monospace, monospace" font-size="13">
      <text x="38" y="98">S → A B</text>
      <text x="38" y="124">A → 0  |  A 0</text>
      <text x="38" y="150">B → A 1</text>
      <text x="38" y="176">C → C C</text>
      <text x="38" y="200" font-size="10" fill="#888">start: S</text>
    </g>

    <!-- Round columns -->
    <text x="300" y="68" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="#666">Round 0</text>
    <text x="420" y="68" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="var(--gold)">Round 1</text>
    <text x="540" y="68" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="var(--gold)">Round 2</text>
    <text x="660" y="68" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="var(--accent-strong, #1c4a3f)">Fixed point</text>

    <text x="300" y="84" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">none marked</text>
    <text x="420" y="84" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">A → 0 (terminal)</text>
    <text x="540" y="84" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">B → A 1 (A ✓)</text>
    <text x="660" y="84" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">S → A B (both ✓)</text>

    <!-- 4 rows × 4 cols grid -->""" + ''.join(
    f'<rect x="{275 + col*120}" y="{96 + row*36}" width="50" height="28" rx="4" fill="{"var(--accent-soft)" if (row == 0 and col == 3) else ("var(--gold-soft)" if (col >= row + 1 and row <= 1) or (col >= 2 and row == 2) else "white")}" stroke="{"var(--accent-strong, #1c4a3f)" if (row == 0 and col == 3) else ("var(--gold)" if (col >= row + 1 and row <= 1) or (col >= 2 and row == 2) else "#bbb")}" stroke-width="{"2" if ((col >= row + 1 and row <= 1) or (col >= 2 and row == 2) or (row == 0 and col == 3)) else "1"}"/>'
    for row in range(4) for col in range(4)
) + ''.join(
    f'<text x="{300 + col*120}" y="{115 + row*36}" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="13" font-weight="{"700" if ((col >= row + 1 and row <= 1) or (col >= 2 and row == 2) or (row == 0 and col == 3)) else "400"}" fill="{"var(--accent-strong, #1c4a3f)" if (row == 0 and col == 3) else ("var(--gold)" if ((col >= row + 1 and row <= 1) or (col >= 2 and row == 2)) else "#999")}">{var}{check}</text>'
    for row, var in enumerate(['S', 'A', 'B', 'C']) for col in range(4)
    for check in ([' ✓'] if ((col >= row + 1 and row <= 1) or (col >= 2 and row == 2) or (row == 0 and col == 3)) else [''])
) + """

    <!-- Variable labels on left -->
    <g font-family="var(--mono), ui-monospace, monospace" font-size="11" font-weight="700" fill="#888">
      <text x="265" y="115" text-anchor="end">S</text>
      <text x="265" y="151" text-anchor="end">A</text>
      <text x="265" y="187" text-anchor="end">B</text>
      <text x="265" y="223" text-anchor="end">C</text>
    </g>

    <!-- Arrows between rounds -->
    <path d="M 332,148 L 376,148" stroke="var(--gold)" stroke-width="1.6" stroke-dasharray="3 2" marker-end="url(#arr-ecfg)"/>
    <path d="M 452,184 L 496,184" stroke="var(--gold)" stroke-width="1.6" stroke-dasharray="3 2" marker-end="url(#arr-ecfg)"/>
    <path d="M 572,112 L 616,112" stroke="var(--accent-strong, #1c4a3f)" stroke-width="1.6" stroke-dasharray="3 2" marker-end="url(#arr-ecfg)"/>

    <!-- Conclusion -->
    <text x="350" y="290" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" fill="#1a1a1a">
      <tspan font-weight="700" fill="var(--accent-strong, #1c4a3f)">S got marked</tspan> ⇒ L(G) ≠ ∅
      &#160;&#160;&#160;
      <tspan font-weight="700" fill="#666">C stayed unmarked</tspan> ⇒ C is unproductive
    </text>
    <text x="350" y="316" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-style="italic" fill="#666">
      At most |V| rounds (each round marks ≥ 1 new var or terminates). Polynomial total.
    </text>
  </svg>
  <figcaption>E<sub>CFG</sub> is decided by computing productive variables — those that derive some terminal string. Start with nothing marked, then repeatedly mark any variable with a rule whose RHS contains only terminals and already-marked variables. L(G) is non-empty iff S is eventually marked. C is unproductive (only rule C → CC requires C itself).</figcaption>
</figure>
"""

# ============================================================
# Universal TM · multi-region tape showing M-description + M's simulated tape + U's head
# ============================================================

ALGO_UNIVERSAL_TM = """
<figure class="diagram">
  <svg viewBox="0 0 700 400" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <defs>
      <marker id="arr-utm" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
        <polygon points="0 0, 8 3, 0 6" fill="#444"/>
      </marker>
    </defs>

    <text x="350" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      Universal TM U · simulates any M on any w using a 3-region tape
    </text>

    <!-- The TM's tape with 3 regions -->
    <text x="20" y="58" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="#1a1a1a">
      U's tape (single tape, three logical regions):
    </text>

    <!-- Region 1: encoded M description -->
    <g>
      <rect x="20" y="70" width="280" height="50" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="1.6"/>
      <text x="160" y="95" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="11" fill="#1a1a1a">
        q₀ , 0 → q₁ , 0 , R ; q₁ , 0 → q₀ , 0 , R ; …
      </text>
      <text x="160" y="111" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="var(--gold)" font-weight="700">
        ⟨M⟩ · transition table (read-only)
      </text>
    </g>
    <!-- separator -->
    <rect x="300" y="70" width="20" height="50" fill="#1a1a1a"/>
    <text x="310" y="100" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="14" fill="white" font-weight="700">#</text>

    <!-- Region 2: M's simulated tape -->
    <g font-family="var(--mono), ui-monospace, monospace" font-size="14" font-weight="700">
      <rect x="320" y="70" width="30" height="50" fill="white" stroke="#444"/>
      <text x="335" y="103" text-anchor="middle">0</text>
      <rect x="350" y="70" width="30" height="50" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="2"/>
      <text x="365" y="103" text-anchor="middle">0</text>
      <rect x="380" y="70" width="30" height="50" fill="white" stroke="#444"/>
      <text x="395" y="103" text-anchor="middle">0</text>
      <rect x="410" y="70" width="30" height="50" fill="white" stroke="#444"/>
      <text x="425" y="103" text-anchor="middle">0</text>
      <rect x="440" y="70" width="30" height="50" fill="white" stroke="#444"/>
      <text x="455" y="103" text-anchor="middle" fill="#aaa">_</text>
      <rect x="470" y="70" width="30" height="50" fill="white" stroke="#444"/>
      <text x="485" y="103" text-anchor="middle" fill="#aaa">_</text>
    </g>
    <text x="410" y="138" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="var(--gold)" font-weight="700">
      M's simulated tape (initially w, evolves under M's δ)
    </text>

    <!-- separator -->
    <rect x="500" y="70" width="20" height="50" fill="#1a1a1a"/>
    <text x="510" y="100" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="14" fill="white" font-weight="700">#</text>

    <!-- Region 3: M's current state (work area) -->
    <g>
      <rect x="520" y="70" width="160" height="50" fill="var(--accent-soft)" stroke="var(--accent-strong, #1c4a3f)" stroke-width="1.6"/>
      <text x="600" y="95" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="12" font-weight="700" fill="var(--accent-strong, #1c4a3f)">
        M's state: q₁
      </text>
      <text x="600" y="111" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">
        head position: cell 1
      </text>
    </g>

    <!-- M's simulated head pointer -->
    <path d="M 365,145 L 365,130" stroke="var(--warn-strong, #b95825)" stroke-width="2.5" marker-end="url(#arr-utm)"/>
    <text x="365" y="160" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" font-weight="700" fill="var(--warn-strong, #b95825)">M's head</text>

    <!-- Divider -->
    <line x1="20" y1="185" x2="680" y2="185" stroke="#ddd" stroke-width="1"/>

    <!-- One step of U's simulation cycle -->
    <text x="350" y="210" text-anchor="middle" font-family="var(--sans), system-ui" font-size="13" font-weight="700" fill="#1a1a1a">
      One step of the simulation: U does this in a loop
    </text>

    <g>
      <!-- 4 boxes in a cycle -->
      <rect x="40" y="240" width="140" height="80" rx="8" fill="white" stroke="var(--accent-strong, #1c4a3f)" stroke-width="1.6"/>
      <text x="110" y="263" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-weight="700">① Read M's state</text>
      <text x="110" y="280" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">from work region</text>
      <text x="110" y="298" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="10" fill="var(--accent-strong, #1c4a3f)">e.g., q₁</text>

      <path d="M 182,278 L 220,278" stroke="#444" stroke-width="1.5" marker-end="url(#arr-utm)"/>

      <rect x="220" y="240" width="140" height="80" rx="8" fill="white" stroke="var(--accent-strong, #1c4a3f)" stroke-width="1.6"/>
      <text x="290" y="263" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-weight="700">② Read symbol</text>
      <text x="290" y="280" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">at M's head pos</text>
      <text x="290" y="298" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="10" fill="var(--accent-strong, #1c4a3f)">e.g., 0</text>

      <path d="M 362,278 L 400,278" stroke="#444" stroke-width="1.5" marker-end="url(#arr-utm)"/>

      <rect x="400" y="240" width="140" height="80" rx="8" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="1.6"/>
      <text x="470" y="263" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="var(--gold)">③ Look up δ in ⟨M⟩</text>
      <text x="470" y="280" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">scan transition table</text>
      <text x="470" y="298" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="10" fill="var(--gold)">→ (q₀, 0, R)</text>

      <path d="M 542,278 L 580,278" stroke="#444" stroke-width="1.5" marker-end="url(#arr-utm)"/>

      <rect x="580" y="240" width="100" height="80" rx="8" fill="white" stroke="var(--warn-strong, #b95825)" stroke-width="1.6"/>
      <text x="630" y="263" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="var(--warn-strong, #b95825)">④ Apply</text>
      <text x="630" y="280" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">write 0,</text>
      <text x="630" y="294" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">move R,</text>
      <text x="630" y="308" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">state ← q₀</text>

      <!-- loop back arrow -->
      <path d="M 630,330 Q 630,355 350,355 Q 110,355 110,330" fill="none" stroke="#888" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#arr-utm)"/>
      <text x="350" y="370" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-style="italic" fill="#666">
        repeat until M reaches q<tspan baseline-shift="sub" font-size="0.75em">accept</tspan> or q<tspan baseline-shift="sub" font-size="0.75em">reject</tspan> — or loop forever
      </text>
    </g>
  </svg>
  <figcaption>The universal TM U lays out three regions on its single tape: M's transition table (loaded from ⟨M⟩), M's simulated tape (initially w), and a small work area tracking M's current state and head position. The 4-step cycle below is U's main loop — read state, read symbol, look up δ in the program region, apply the transition. U is one fixed machine that runs every other machine.</figcaption>
</figure>
"""

# ============================================================
# HALT reduction · S as a machine that wraps R and a direct simulator
# ============================================================

ALGO_HALT_REDUCTION = """
<figure class="diagram">
  <svg viewBox="0 0 700 420" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <defs>
      <marker id="arr-halt" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
        <polygon points="0 0, 8 3, 0 6" fill="#444"/>
      </marker>
      <marker id="arr-halt-y" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
        <polygon points="0 0, 8 3, 0 6" fill="var(--accent-strong, #1c4a3f)"/>
      </marker>
      <marker id="arr-halt-n" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
        <polygon points="0 0, 8 3, 0 6" fill="var(--warn-strong, #b95825)"/>
      </marker>
    </defs>

    <text x="350" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      Reduction A<tspan baseline-shift="sub" font-size="0.75em">TM</tspan> ≤ HALT<tspan baseline-shift="sub" font-size="0.75em">TM</tspan> · build a decider S using a hypothetical R
    </text>

    <!-- Input tape: ⟨M, w⟩ -->
    <text x="20" y="58" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="#1a1a1a">
      Input tape of S:
    </text>
    <g font-family="var(--mono), ui-monospace, monospace" font-size="13">
      <rect x="20" y="70" width="100" height="36" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="1.6"/>
      <text x="70" y="93" text-anchor="middle" font-weight="700">⟨M⟩</text>
      <rect x="120" y="70" width="20" height="36" fill="#1a1a1a"/>
      <text x="130" y="93" text-anchor="middle" fill="white" font-weight="700">#</text>
      <rect x="140" y="70" width="100" height="36" fill="var(--accent-soft)" stroke="var(--accent-strong, #1c4a3f)" stroke-width="1.6"/>
      <text x="190" y="93" text-anchor="middle" font-weight="700">w</text>
    </g>
    <text x="260" y="93" font-family="var(--sans), system-ui" font-size="11" fill="#666">— S is asked: "does M accept w?"</text>

    <!-- Big S outer box -->
    <rect x="20" y="130" width="660" height="250" rx="12" fill="none" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2.4"/>
    <text x="350" y="152" text-anchor="middle" font-family="var(--sans), system-ui" font-size="13" font-weight="700" fill="var(--accent-strong, #1c4a3f)">
      S · the hypothetical decider for A<tspan baseline-shift="sub" font-size="0.75em">TM</tspan>
    </text>

    <!-- Step 1: R sub-machine -->
    <rect x="50" y="175" width="220" height="100" rx="10" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="2"/>
    <text x="160" y="197" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="var(--gold)">① Call R(⟨M, w⟩)</text>
    <text x="160" y="215" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">R is the assumed</text>
    <text x="160" y="229" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">HALT<tspan baseline-shift="sub" font-size="0.75em">TM</tspan> decider</text>
    <text x="160" y="248" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="11" fill="#1a1a1a">"does M halt on w?"</text>
    <text x="160" y="265" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" font-style="italic" fill="#666">R always halts (by assumption)</text>

    <!-- Two output branches from R -->
    <!-- Branch 1: R says no (M loops) -->
    <path d="M 160,277 L 160,310" stroke="var(--warn-strong, #b95825)" stroke-width="2" marker-end="url(#arr-halt-n)"/>
    <text x="200" y="295" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="var(--warn-strong, #b95825)">R: no (loops)</text>
    <rect x="80" y="315" width="160" height="48" rx="6" fill="white" stroke="var(--warn-strong, #b95825)" stroke-width="2"/>
    <text x="160" y="336" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="var(--warn-strong, #b95825)">S rejects ⟨M, w⟩</text>
    <text x="160" y="352" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">M loops ⇒ M doesn't accept</text>

    <!-- Branch 2: R says yes (M halts) → simulate -->
    <path d="M 272,225 L 318,225" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2" marker-end="url(#arr-halt-y)"/>
    <text x="295" y="218" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="var(--accent-strong, #1c4a3f)">R: yes</text>
    <text x="295" y="244" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">(M halts)</text>

    <!-- Step 2: Universal TM simulator -->
    <rect x="320" y="175" width="320" height="100" rx="10" fill="var(--accent-soft)" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2"/>
    <text x="480" y="197" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="var(--accent-strong, #1c4a3f)">② Run U(⟨M, w⟩) directly</text>
    <!-- Mini tape showing M's simulated tape -->
    <g font-family="var(--mono), ui-monospace, monospace" font-size="11" font-weight="700">
      <rect x="365" y="215" width="22" height="26" fill="white" stroke="#444"/>
      <text x="376" y="234" text-anchor="middle">w₀</text>
      <rect x="387" y="215" width="22" height="26" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="1.5"/>
      <text x="398" y="234" text-anchor="middle">w₁</text>
      <rect x="409" y="215" width="22" height="26" fill="white" stroke="#444"/>
      <text x="420" y="234" text-anchor="middle">w₂</text>
      <rect x="431" y="215" width="22" height="26" fill="white" stroke="#444"/>
      <text x="442" y="234" text-anchor="middle" fill="#aaa">_</text>
      <text x="465" y="234" font-size="10" fill="#666">…M's tape</text>
    </g>
    <text x="480" y="262" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">
      Guaranteed to halt (R told us so) — accept iff M accepts.
    </text>

    <!-- output from step 2 -->
    <path d="M 480,277 L 480,310" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2" marker-end="url(#arr-halt-y)"/>
    <rect x="400" y="315" width="160" height="48" rx="6" fill="white" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2"/>
    <text x="480" y="336" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="var(--accent-strong, #1c4a3f)">S accepts iff M accepts</text>
    <text x="480" y="352" text-anchor="middle" font-family="var(--sans), system-ui" font-size="10" fill="#666">direct simulation gives the answer</text>

    <!-- Bottom: contradiction note -->
    <text x="350" y="402" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-style="italic" fill="#666">
      S would decide A<tspan baseline-shift="sub" font-size="0.75em">TM</tspan> — but A<tspan baseline-shift="sub" font-size="0.75em">TM</tspan> is undecidable. So R cannot exist ⇒ HALT<tspan baseline-shift="sub" font-size="0.75em">TM</tspan> is undecidable.
    </text>
  </svg>
  <figcaption>If a decider R for HALT<sub>TM</sub> existed, we could build a decider S for A<sub>TM</sub> as follows: ① ask R whether M halts on w; if R says no, M loops and cannot accept, so S rejects; ② if R says yes, we know it's safe to directly simulate M on w (it will halt), and S accepts iff the simulation accepts. S is a decider for A<sub>TM</sub> — which is impossible, so R cannot exist.</figcaption>
</figure>
"""

# ============================================================
# Recursion theorem · TM with own description on tape (data + code split)
# ============================================================

ALGO_RECURSION_THEOREM = """
<figure class="diagram">
  <svg viewBox="0 0 700 380" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <defs>
      <marker id="arr-rec" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
        <polygon points="0 0, 8 3, 0 6" fill="#444"/>
      </marker>
    </defs>

    <text x="350" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      Recursion theorem · M has its own description ⟨M⟩ available on tape
    </text>

    <!-- TM M outer box -->
    <rect x="20" y="55" width="660" height="220" rx="12" fill="white" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2.4"/>
    <text x="350" y="80" text-anchor="middle" font-family="var(--sans), system-ui" font-size="13" font-weight="700" fill="var(--accent-strong, #1c4a3f)">
      TM M · on input w
    </text>

    <!-- M's tape, split into 2 sections -->
    <text x="50" y="110" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="#666">M's tape:</text>
    <g font-family="var(--mono), ui-monospace, monospace" font-size="11">
      <!-- Data region: M's own description -->
      <rect x="50" y="120" width="280" height="36" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="1.6"/>
      <text x="190" y="141" text-anchor="middle" font-weight="700" fill="var(--gold)">data: ⟨M⟩ (M's own description)</text>
      <!-- Separator -->
      <rect x="330" y="120" width="20" height="36" fill="#1a1a1a"/>
      <text x="340" y="143" text-anchor="middle" font-weight="700" fill="white">#</text>
      <!-- Input region -->
      <rect x="350" y="120" width="100" height="36" fill="var(--accent-soft)" stroke="var(--accent-strong, #1c4a3f)" stroke-width="1.6"/>
      <text x="400" y="141" text-anchor="middle" font-weight="700" fill="var(--accent-strong, #1c4a3f)">input w</text>
      <!-- work area -->
      <rect x="450" y="120" width="200" height="36" fill="white" stroke="#888" stroke-dasharray="3 2"/>
      <text x="550" y="141" text-anchor="middle" fill="#888">work area (scratch)</text>
    </g>

    <!-- Code box (the "code" section of M) -->
    <rect x="50" y="170" width="600" height="90" rx="8" fill="white" stroke="#444" stroke-width="1.2"/>
    <text x="350" y="188" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-weight="700" fill="#1a1a1a">M's program (code):</text>
    <g font-family="var(--mono), ui-monospace, monospace" font-size="11">
      <text x="70" y="208">  step 1: read the data region — this gives ⟨M⟩, my own description</text>
      <text x="70" y="226">  step 2: read the input w from the next region</text>
      <text x="70" y="244">  step 3: compute whatever (e.g., simulate t(⟨M⟩) on w, or output ⟨M⟩, …)</text>
    </g>

    <!-- "uses self" arrow from code to data -->
    <path d="M 130,200 Q 100,180 100,160" stroke="var(--accent)" stroke-width="1.6" stroke-dasharray="4 2" fill="none" marker-end="url(#arr-rec)"/>
    <text x="50" y="180" font-family="var(--sans), system-ui" font-size="10" font-style="italic" fill="var(--accent)">uses self</text>

    <!-- Below the box: the theorem statement and one application -->
    <text x="350" y="305" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-weight="700" fill="#1a1a1a">
      Theorem (Recursion).  For every computable function t, there exists a TM M with L(M) = L(t(⟨M⟩)).
    </text>
    <text x="350" y="325" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" fill="#666">
      Equivalently: M can "look up" its own source code at runtime and compute with it.
    </text>
    <text x="350" y="350" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" font-style="italic" fill="#666">
      Apps: quines (print ⟨M⟩), self-checking proofs, slick re-derivation of A<tspan baseline-shift="sub" font-size="0.75em">TM</tspan> undecidability.
    </text>
  </svg>
  <figcaption>Recursion theorem in pictures: M's tape has a dedicated <em>data region</em> holding M's own description ⟨M⟩, plus the usual input region and work area. The "code" part of M references this data region whenever it needs to know its own source. This is the formal version of "programs can quote themselves" — and is the engine behind quines and several short undecidability proofs.</figcaption>
</figure>
"""

# ============================================================
# Big-O · keep the layered breakdown (already good)
# ============================================================

ALGO_BIGO_LAYERS = """
<figure class="diagram">
  <svg viewBox="0 0 640 260" xmlns="http://www.w3.org/2000/svg" style="background:#fcfbf7;border-radius:8px;">
    <text x="320" y="22" text-anchor="middle" font-family="var(--sans), system-ui" font-size="14" font-weight="700" fill="#1a1a1a">
      Big-O · what we throw away when n grows large
    </text>
    <rect x="30" y="50" width="280" height="70" rx="8" fill="white" stroke="#888" stroke-width="1.4"/>
    <text x="170" y="76" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="14" fill="#1a1a1a">
      <tspan fill="var(--accent-strong, #1c4a3f)" font-weight="700">3 n²</tspan>
      <tspan fill="#888"> + 100 n + 5000</tspan>
    </text>
    <text x="170" y="100" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" fill="#666">exact running time T(n)</text>
    <text x="330" y="92" font-family="var(--sans), system-ui" font-size="20" fill="var(--accent)">→</text>
    <rect x="350" y="50" width="260" height="70" rx="8" fill="var(--accent-soft)" stroke="var(--accent-strong, #1c4a3f)" stroke-width="2"/>
    <text x="480" y="76" text-anchor="middle" font-family="var(--mono), ui-monospace, monospace" font-size="14" font-weight="700" fill="var(--accent-strong, #1c4a3f)">
      O(n²)
    </text>
    <text x="480" y="100" text-anchor="middle" font-family="var(--sans), system-ui" font-size="11" fill="#666">asymptotic growth rate</text>
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
    <text x="320" y="242" text-anchor="middle" font-family="var(--sans), system-ui" font-size="12" font-style="italic" fill="#666">
      f(n) ∈ O(g(n)) ⇔ ∃ c, n₀ such that for all n ≥ n₀, f(n) ≤ c · g(n).
    </text>
  </svg>
  <figcaption>Big-O notation discards constants and lower-order terms. The dominant term defines the complexity class. For n=1000, the n² term is 3,000,000 while the linear and constant terms total 105,000 — the quadratic term is what matters asymptotically.</figcaption>
</figure>
"""
