"""Make the Sipser and MIT reference pills clickable across all module
and prerequisite HTML pages. Also add an "Ask Khayyam" link to every page.

- MIT 18.404J L#  pill  →  YouTube video (in user's playlist)
- Sipser §X.Y     pill  →  MIT OCW lecture page (with slides + reading)
- Ask Khayyam     button →  https://khayyammath.com/

All links open in new tabs (target="_blank" rel="noopener").
"""
import os, re

ROOT = '/sessions/wizardly-peaceful-gates/mnt/Computability and Complexity'
PLAYLIST = 'PLidiQIHRzpXIFFbyGrWkqXXVj0BztDcTF'

# YouTube IDs for each MIT 18.404J lecture (Fall 2020)
YT_ID = {
    1:  '9syvZr-9xwk',  2:  'oNsscmUwjMU',  3:  'KAySmSEGc9U',
    4:  'm9eHViDPAJQ',  5:  'IycOPFmEQk8',  6:  'TTArY7ojshU',
    7:  '4MgN6uxd4i4',  8:  '3PzuSPQPEU4',  9:  'N28g_YBXY8Y',
    10: 'MGqoLm2aAgc', 11: 'N-_XmLanPYg',  12: 'asjAc90L8rE',
    14: '1VhnDdQsELo', 15: 'iZPzBHGDsWI',  16: '6Az1gtDRaAU',
    17: 'cT_qwkTigv4', 18: 'aVv9WXwW95w',  19: '4dFPVJrNLDs',
    20: 'q3xvno_KgRY', 21: 'vqFRAWeEcUs',
}

def yt(n):
    return f'https://www.youtube.com/watch?v={YT_ID[n]}&list={PLAYLIST}'

# MIT OCW lecture resource pages (slides + video + reading list)
OCW = {
    1:  'https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/introduction-finite-automata-regular-expressions/',
    2:  'https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/nondeterminism-closure-properties-regular-expressions-2192-finite-automata/',
    3:  'https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/regular-pumping-lemma-finite-automata-2192-regular-expressions-cfgs/',
    4:  'https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/pushdown-automata-cfg-2194-pda/',
    5:  'https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/cf-pumping-lemma-turing-machines/',
    6:  'https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/tm-variants-church-turing-thesis/',
    7:  'https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/decision-problems-for-automata-and-grammars/',
    8:  'https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/lecture-8-undecidability/',
    9:  'https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/lecture-9-reducibility/',
    10: 'https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/lecture-10-computation-history-method/',
    11: 'https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/lecture-11-recursion-theorem-and-logic/',
    12: 'https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/lecture-12-time-complexity/',
    14: 'https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/lecture-14-p-and-np-sat-poly-time-reducibility/',
    15: 'https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/lecture-15-np-completeness/',
    16: 'https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/lecture-16-cook-levin-theorem/',
    17: 'https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/lecture-17-space-complexity-pspace-savitchs-theorem/',
    18: 'https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/lecture-18-pspace-completeness/',
    19: 'https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/lecture-19-games-generalized-geography/',
    20: 'https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/lecture-20-l-and-nl-nl-conl/',
    21: 'https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/lecture-21-hierarchy-theorems/',
}

# Map Sipser sections to the MIT lecture that covers them (for OCW page link)
SIPSER_TO_LECTURE = {
    '0.2': 1,  '0.4': 1,
    '1.1': 1,  '1.2': 2,  '1.3': 2,  '1.4': 3,
    '2.1': 3,  '2.2': 4,  '2.3': 5,
    '3.1': 5,  '3.2': 6,  '3.3': 6,
    '4.1': 7,  '4.2': 8,
    '5.1': 9,  '5.2': 10,
    '6.1': 11, '6.3': 11,
    '7.1': 12, '7.2': 12, '7.3': 14, '7.4': 15, '7.5': 16,
    '8.1': 17, '8.2': 17, '8.3': 18, '8.4': 20,
    '9.1': 21,
    # Chapter-level shorthands
    'Ch. 4.1': 7, 'Ch. 4.2': 8,
}

ASK_KHAYYAM = 'https://khayyammath.com/'

# ============================================================
# Prerequisites page: wrap existing ref-pills with anchors
# ============================================================
def patch_prerequisites(path):
    with open(path) as f:
        html = f.read()
    before = html

    # 1) wrap MIT pills:  <span class="ref-pill mit">MIT 18.404J L#</span>  →  <a target=blank ...>
    def mit_repl(m):
        full = m.group(0)
        lec_num_match = re.search(r'L(\d+)', full)
        if not lec_num_match:
            return full
        n = int(lec_num_match.group(1))
        if n not in YT_ID:
            return full
        return f'<a href="{yt(n)}" target="_blank" rel="noopener" style="text-decoration:none;">{full}</a>'
    html = re.sub(r'<span class="ref-pill mit">[^<]+</span>', mit_repl, html)

    # 2) wrap Sipser §X.Y pills
    def book_repl(m):
        full = m.group(0)
        sm = re.search(r'§\s*(\d+\.\d+)', full)
        if not sm:
            return full
        sec = sm.group(1)
        if sec not in SIPSER_TO_LECTURE:
            return full
        lec = SIPSER_TO_LECTURE[sec]
        if lec not in OCW:
            return full
        return f'<a href="{OCW[lec]}" target="_blank" rel="noopener" style="text-decoration:none;">{full}</a>'
    html = re.sub(r'<span class="ref-pill book">[^<]+</span>', book_repl, html)

    # 3) inject Ask Khayyam button into the hero (right after the existing back-to-course button)
    if 'khayyammath.com' not in html:
        html = html.replace(
            '← back to course site</a>',
            '← back to course site</a>\n    <a href="' + ASK_KHAYYAM + '" target="_blank" rel="noopener" class="btn" style="display:inline-block;padding:8px 14px;margin-left:8px;background:var(--accent-strong, #1c4a3f);color:white;border-radius:4px;text-decoration:none;font-weight:600;">💬 Ask Khayyam ↗</a>',
            1
        )

    if html != before:
        with open(path, 'w') as f:
            f.write(html)
        print(f'  ✓ prerequisites.html: pills linked + Ask Khayyam')
    else:
        print(f'  skip prerequisites.html: no changes')


# ============================================================
# Module pages: link the eyebrow refs and add Ask Khayyam button
# ============================================================
EYEBROW_PATTERN = re.compile(
    r'<div class="eyebrow">\s*Module\s+(\d+)\s*·\s*'
    r'MIT\s*18\.404J\s*Lecture(s)?\s*([^·<]+?)\s*·\s*'
    r'Sipser\s*§([^<]+?)\s*</div>',
    re.IGNORECASE
)

def parse_lec_numbers(s):
    """Parse strings like '7' or '8-9' or '20-21' into a list of ints."""
    s = s.strip()
    nums = []
    for part in re.split(r'[,\s]+', s):
        if '-' in part:
            a, b = part.split('-')
            nums.extend(range(int(a), int(b) + 1))
        elif part:
            try: nums.append(int(part))
            except: pass
    return nums

def parse_sipser_secs(s):
    """Parse strings like '4.1' or '4.2 + 5.1' or '7.1-2 + 7.5'."""
    s = s.strip()
    out = []
    # split on '+', ',', and 'and'
    parts = re.split(r'\s*\+\s*|\s*,\s*|\s+and\s+', s)
    for part in parts:
        m = re.match(r'(\d+)\.(\d+)(?:\s*-\s*(\d+))?', part)
        if not m: continue
        chap = m.group(1)
        a = int(m.group(2))
        b = int(m.group(3)) if m.group(3) else a
        for sub in range(a, b + 1):
            out.append(f'{chap}.{sub}')
    return out

def patch_module(path):
    with open(path) as f:
        html = f.read()
    before = html

    # Patch eyebrow
    m = EYEBROW_PATTERN.search(html)
    if not m:
        print(f'  ⚠ {os.path.basename(path)}: no eyebrow found')
        return

    mod_num = int(m.group(1))
    is_plural = bool(m.group(2))
    lec_str = m.group(3).strip()
    sip_str = m.group(4).strip()

    lecs = parse_lec_numbers(lec_str)
    secs = parse_sipser_secs(sip_str)

    # Build linked HTML
    lec_label = 'Lectures' if (is_plural or len(lecs) > 1) else 'Lecture'
    lec_links = []
    for n in lecs:
        if n in YT_ID:
            lec_links.append(f'<a href="{yt(n)}" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:3px;">L{n}</a>')
        else:
            lec_links.append(f'L{n}')
    lec_html = ', '.join(lec_links)

    sip_links = []
    for sec in secs:
        if sec in SIPSER_TO_LECTURE and SIPSER_TO_LECTURE[sec] in OCW:
            url = OCW[SIPSER_TO_LECTURE[sec]]
            sip_links.append(f'<a href="{url}" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:3px;">§{sec}</a>')
        else:
            sip_links.append(f'§{sec}')
    sip_html = ' + '.join(sip_links)

    new_eyebrow = (
        f'<div class="eyebrow">Module {mod_num} · MIT 18.404J {lec_label} '
        f'{lec_html} · Sipser {sip_html}</div>'
    )
    # Insert Ask Khayyam ribbon right after the eyebrow
    if 'khayyammath.com' not in html:
        ask = (
            '\n  <div class="ask-khayyam-bar" style="margin:6px 0 14px;display:flex;gap:8px;flex-wrap:wrap;justify-content:flex-end;font-family:var(--sans), system-ui, sans-serif;">'
            '<span style="font-size:11.5px;color:var(--ink-soft, #666);align-self:center;">references open in new tabs →</span>'
            f'<a href="{ASK_KHAYYAM}" target="_blank" rel="noopener" '
            'style="display:inline-block;padding:5px 12px;background:var(--accent-strong, #1c4a3f);color:white;border-radius:4px;text-decoration:none;font-weight:600;font-size:12px;">💬 Ask Khayyam ↗</a>'
            '</div>'
        )
        new_eyebrow = new_eyebrow + ask

    html = html.replace(m.group(0), new_eyebrow, 1)

    # Also: in the "Practice (Sipser Ch. X.Y)" header, link the chapter
    h2_pat = re.compile(r'<h2>(\d+\s*·\s*)?Practice\s*\(Sipser\s+Ch\.\s+([\d.]+)\)</h2>')
    def h2_repl(mm):
        prefix = mm.group(1) or ''
        chap = mm.group(2)
        if chap in SIPSER_TO_LECTURE and SIPSER_TO_LECTURE[chap] in OCW:
            url = OCW[SIPSER_TO_LECTURE[chap]]
            return f'<h2>{prefix}Practice (Sipser Ch. <a href="{url}" target="_blank" rel="noopener" style="color:inherit;">{chap}</a>)</h2>'
        return mm.group(0)
    html = h2_pat.sub(h2_repl, html)

    if html != before:
        with open(path, 'w') as f:
            f.write(html)
        print(f'  ✓ {os.path.basename(path)}: linked {len(lec_links)} lectures, {len(sip_links)} sections + Ask Khayyam')


def main():
    # Prerequisites page
    print('Prerequisites page:')
    patch_prerequisites(os.path.join(ROOT, 'prerequisites.html'))

    # Module pages
    print('\nModule pages:')
    for f in sorted(os.listdir(ROOT)):
        if f.startswith('module-') and f.endswith('.html'):
            patch_module(os.path.join(ROOT, f))

if __name__ == '__main__':
    main()
