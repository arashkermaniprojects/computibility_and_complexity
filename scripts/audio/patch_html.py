"""Insert a seekable audio player at the top of each <section> in each module HTML.

The player uses HTML5 native <audio controls preload="metadata"> which gives
play/pause/seek/volume/playback-rate (in most browsers) for free, with no JS.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
AUDIO_DIR_REL = 'audio'  # relative URL from each module HTML

MODULES = [
    ('module-1-decidable-automata.html', 1),
    ('module-2-undecidability.html', 2),
    ('module-3-reductions-recursion.html', 3),
    ('module-4-time-complexity.html', 4),
    ('module-5-np-completeness.html', 5),
    ('module-6-space-pspace.html', 6),
    ('module-7-l-nl-hierarchy.html', 7),
]

# CSS block injected once per file, inside <head>
AUDIO_CSS = """
<style>
.section-audio {
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 8px 0 18px;
  padding: 10px 14px;
  background: linear-gradient(180deg, #fffaf3 0%, #fff5e8 100%);
  border: 1px solid var(--gold-soft, #e8d8b4);
  border-left: 4px solid var(--gold, #c89933);
  border-radius: 8px;
}
.section-audio .audio-label {
  font-family: var(--sans, system-ui), sans-serif;
  font-size: 12.5px;
  font-weight: 600;
  color: var(--gold, #8a6a1d);
  white-space: nowrap;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}
.section-audio audio {
  flex: 1;
  height: 36px;
  max-width: 540px;
}
.section-audio audio::-webkit-media-controls-panel {
  background: #fffaf3;
}
@media (max-width: 640px) {
  .section-audio { flex-wrap: wrap; }
}
</style>
"""

PLAYER_HTML_FMT = (
    '<div class="section-audio">'
    '<span class="audio-label">🎧 Narration</span>'
    '<audio controls preload="metadata" src="{src}"></audio>'
    '</div>'
)

def inject_css(html):
    if 'section-audio' in html:
        return html  # already injected
    return html.replace('</head>', AUDIO_CSS + '\n</head>', 1)

def inject_players(html, module_num):
    # Match each <section ...> opening tag and insert player right after it.
    section_index = [0]
    def repl(match):
        section_index[0] += 1
        src = f'{AUDIO_DIR_REL}/m{module_num}-s{section_index[0]}.mp3'
        player = PLAYER_HTML_FMT.format(src=src)
        return match.group(0) + '\n  ' + player
    # The section tag itself may have attributes; match opening only
    patched = re.sub(r'<section\b[^>]*>', repl, html)
    print(f'  module {module_num}: inserted {section_index[0]} players')
    return patched

def remove_old_players(html):
    """Remove any previously inserted .section-audio blocks so we can re-inject cleanly."""
    return re.sub(r'<div class="section-audio">.*?</div>', '', html, flags=re.S)

def main():
    for fname, mnum in MODULES:
        path = os.path.join(ROOT, fname)
        if not os.path.exists(path):
            print(f'  warning: {fname} not found, skipping')
            continue
        with open(path) as f:
            html = f.read()
        html = remove_old_players(html)
        html = inject_css(html)
        html = inject_players(html, mnum)
        with open(path, 'w') as f:
            f.write(html)
    print('\nAll module HTMLs patched.')

if __name__ == '__main__':
    main()
