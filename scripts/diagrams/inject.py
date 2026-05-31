"""Inject diagrams from diagrams.py into each module's HTML at specified anchors.

Each entry in INJECTIONS is (filename, anchor_string, diagram_var).
The anchor must be a unique substring in the file; the diagram is inserted
right after the line containing the anchor.
"""
import os, sys, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

sys.path.insert(0, HERE)
import diagrams as D

# (filename, anchor_substring, diagram_name)
INJECTIONS = [
    # ---- MODULE 1 ----
    ('module-1-decidable-automata.html',
     'L(A) △ L(B) = (L(A) ∩ L(B)<sup>c</sup>) ∪ (L(A)<sup>c</sup> ∩ L(B)).',
     'VENN_SYMDIFF'),

    ('module-1-decidable-automata.html',
     'A DFA recognises a non-empty language iff <em>some accept state is reachable</em>',
     'GRAPH_REACHABILITY'),

    # ---- MODULE 2 ----
    ('module-2-undecidability.html',
     'flip every diagonal bit',
     'CANTOR_DIAGONAL_DIAGRAM'),

    ('module-2-undecidability.html',
     'A<sub>TM</sub> is not decidable',
     'D_CONTRADICTION_MACHINE'),

    ('module-2-undecidability.html',
     'The map of languages',
     'VENN_DECIDABLE_RECOGNIZABLE'),

    # ---- MODULE 3 ----
    ('module-3-reductions-recursion.html',
     'The computation history trick',
     'COMPUTATION_HISTORY_TABLEAU'),

    ('module-3-reductions-recursion.html',
     "Rice's theorem",
     'RICE_DECISION_TREE'),

    # ---- MODULE 4 ----
    ('module-4-time-complexity.html',
     'Watch growth rates race',
     'GROWTH_RATE_CURVES'),

    ('module-4-time-complexity.html',
     'The model matters',
     'SINGLE_VS_TWO_TAPE'),

    # ---- MODULE 5 ----
    ('module-5-np-completeness.html',
     'Cook–Levin',
     'COOK_LEVIN_TABLEAU'),

    ('module-5-np-completeness.html',
     'reduction chain',
     'NP_REDUCTION_TREE'),

    # ---- MODULE 6 ----
    ('module-6-space-pspace.html',
     'Time vs. space',
     'TIME_VS_SPACE'),

    ('module-6-space-pspace.html',
     "Savitch's theorem",
     'SAVITCH_RECURSION_TREE'),

    ('module-6-space-pspace.html',
     'TQBF',
     'TQBF_GAME_TREE'),

    # ---- MODULE 7 ----
    ('module-7-l-nl-hierarchy.html',
     'The full map',
     'FULL_COMPLEXITY_ZOO'),

    ('module-7-l-nl-hierarchy.html',
     'hierarchy theorems',
     'HIERARCHY_DIAGONAL'),
]

def inject_css(html):
    if 'class="diagram"' in html and '.diagram svg' in html:
        return html  # already injected
    return html.replace('</head>', D.DIAGRAM_CSS + '\n</head>', 1)

def insert_after_line(html, anchor, diagram_html):
    """Find the line containing the anchor, insert diagram after the enclosing tag's end."""
    idx = html.find(anchor)
    if idx == -1:
        return html, False
    # Find the end of the enclosing block element (next </p>, </h2>, </h3>, </div> on its own line)
    # Simpler: insert at end of current line, then end of paragraph if any.
    # Find the closing > of the wrapping tag — we look for the next \n after idx.
    line_end = html.find('\n', idx)
    if line_end == -1:
        line_end = len(html)
    # Then skip ahead to past the closing tag of that paragraph/heading
    # Look for the next </p>, </h2>, </h3>, </h4>, </div> after idx
    closing_pat = re.compile(r'</(?:p|h2|h3|h4|li|ul|ol|div)>', re.IGNORECASE)
    m = closing_pat.search(html, idx)
    if m:
        insert_at = m.end()
    else:
        insert_at = line_end
    # Insert at the next newline after insert_at, with a leading blank line
    nl = html.find('\n', insert_at)
    if nl == -1:
        nl = insert_at
    new_html = html[:nl] + '\n' + diagram_html.strip() + '\n' + html[nl:]
    return new_html, True

def main():
    by_file = {}
    for fname, anchor, dname in INJECTIONS:
        by_file.setdefault(fname, []).append((anchor, dname))

    for fname, items in by_file.items():
        path = os.path.join(ROOT, fname)
        if not os.path.exists(path):
            print(f'  WARN: {fname} not found')
            continue
        with open(path) as f:
            html = f.read()
        html = inject_css(html)
        added = 0
        for anchor, dname in items:
            diag = getattr(D, dname, None)
            if diag is None:
                print(f'  WARN: diagram {dname} missing')
                continue
            # Avoid double-injection: check if a unique tag from the diagram is already present
            # use the title text from the diagram (first <text> body) as a fingerprint
            m = re.search(r'<text[^>]*>([^<]{20,80})</text>', diag)
            fingerprint = m.group(1).strip() if m else dname
            if fingerprint in html:
                print(f'  skip {fname}: "{dname}" already present')
                continue
            html, ok = insert_after_line(html, anchor, diag)
            if ok:
                added += 1
                print(f'  ✓ {fname}: inserted {dname}')
            else:
                print(f'  ✗ {fname}: anchor NOT FOUND for {dname} → "{anchor[:60]}"')
        with open(path, 'w') as f:
            f.write(html)
        print(f'  {fname}: {added} diagrams added')

if __name__ == '__main__':
    main()
