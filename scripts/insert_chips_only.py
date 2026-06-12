#!/usr/bin/env python3
"""For each tool, count existing audios/sections/p{NN}-s{N}.mp3 files and
prepend a chip into each section. Uses lambda replacement to avoid regex
backreference issues."""
import re, glob
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
AUDIO = ROOT / "audio" / "sections"

CHIP = ('<div class="component-audio" style="margin:8px 0 6px;padding:6px 10px;'
        'background:#fbf6ef;border-left:3px solid var(--gold,#c0a04e);'
        'border-radius:4px;display:flex;align-items:center;gap:8px;'
        'font-family:var(--sans,system-ui);font-size:11.5px;color:#555;">'
        '<span style="font-weight:700;color:var(--gold,#a68526);">🔊 Listen</span>'
        '<audio controls preload="none" src="../audio/sections/{NAME}.mp3" '
        'style="height:28px;flex:1;max-width:280px;"></audio></div>')

total_inserted = 0
for f in sorted(TOOLS.glob('p*.html')):
    m = re.match(r'p(\d+)-', f.name)
    if not m: continue
    tid = int(m.group(1))
    html = f.read_text()
    if '../audio/sections/' in html:
        continue  # already has section chips
    # Count available audios for this tool
    audios = sorted(AUDIO.glob(f'p{tid:02d}-s*.mp3'))
    if not audios:
        continue
    # Find sections
    pat = r'(<section[^>]*>)(\s*<div class="section-label[^"]*"[^>]*>)'
    counter = [0]
    def rep(m):
        counter[0] += 1
        audio_name = f'p{tid:02d}-s{counter[0]}'
        # Check audio file exists
        if not (AUDIO / f'{audio_name}.mp3').exists():
            return m.group(0)  # leave unchanged if no audio
        return m.group(1) + CHIP.replace('{NAME}', audio_name) + m.group(2)
    new_html = re.sub(pat, rep, html)
    if counter[0] > 0:
        f.write_text(new_html)
        print(f"{f.name}: inserted {counter[0]} chips")
        total_inserted += counter[0]
print(f"\nTotal chips inserted: {total_inserted}")
