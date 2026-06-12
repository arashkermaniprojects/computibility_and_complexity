#!/usr/bin/env python3
"""
Generate teaching-narration audio for every section of every tool.

For each tool in tools/, extract each <section>, generate a ~150-200 word
spoken-narration script via GPT-4o-mini, generate MP3 via OpenAI TTS-1-HD,
and insert a 🔊 chip into the HTML at the top of each section.

Usage: python3 gen_section_audio.py [tool_id_lo] [tool_id_hi]
       e.g. python3 gen_section_audio.py 1 5  -> processes p01..p05
"""
import os, re, json, sys, glob, subprocess, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
AUDIO = ROOT / "audio" / "sections"
AUDIO.mkdir(parents=True, exist_ok=True)
KEY = open("/tmp/oai_key.txt").read().strip()

CHIP_TEMPLATE = (
    '<div class="component-audio" style="margin:8px 0 6px;padding:6px 10px;'
    'background:#fbf6ef;border-left:3px solid var(--gold,#c0a04e);'
    'border-radius:4px;display:flex;align-items:center;gap:8px;'
    'font-family:var(--sans,system-ui);font-size:11.5px;color:#555;">'
    '<span style="font-weight:700;color:var(--gold,#a68526);">🔊 Listen</span>'
    '<audio controls preload="none" src="../audio/sections/{audio}.mp3" '
    'style="height:28px;flex:1;max-width:280px;"></audio></div>'
)

def get_problem_context(html):
    """Extract problem title + subtitle for prompt context."""
    h1 = re.search(r'<h1[^>]*>([\s\S]*?)</h1>', html)
    sub = re.search(r'class="sub"[^>]*>([\s\S]*?)</p>', html)
    h1_txt = re.sub(r'<[^>]+>', '', h1.group(1)).strip() if h1 else ''
    sub_txt = re.sub(r'<[^>]+>', '', sub.group(1)).strip() if sub else ''
    return h1_txt, sub_txt


def extract_sections(html):
    """Return list of (label, plain_text) for each <section> with a section-label."""
    sections = []
    for m in re.finditer(r'<section[^>]*>([\s\S]*?)</section>', html):
        body = m.group(1)
        lab_m = re.search(r'class="section-label[^"]*"[^>]*>([^<]+)<', body)
        if not lab_m:
            continue
        label = lab_m.group(1).strip()
        # Strip diagrams and code to get clean text
        text = body
        text = re.sub(r'<svg[\s\S]*?</svg>', ' ', text)
        text = re.sub(r'<style[\s\S]*?</style>', '', text)
        text = re.sub(r'<script[\s\S]*?</script>', '', text)
        text = re.sub(r'<pre[^>]*>([\s\S]*?)</pre>', r' [code: \1] ', text)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        sections.append((label, text[:3000]))
    return sections


def gen_script(label, content, problem_title, problem_sub):
    """Call GPT-4o-mini to generate a ~150-200 word spoken teaching narration."""
    prompt = f"""You are teaching a student about: {problem_title} ({problem_sub}).

Write a spoken teaching narration for the topic "{label}" within this lesson. The student is studying this topic and needs a verbal walkthrough that makes the content clear and intuitive.

CRITICAL RULES:
- Write as natural spoken language, not formal prose
- 130-200 words (one to two minutes of speech)
- Be informative, concrete, and pedagogical
- Do NOT say "slide", "section", "this picture", "above", "below", "the diagram", "as shown", "here we see"
- Just teach the subject directly, as if explaining one-on-one
- For abbreviations like SAT, CLIQUE, NP — pronounce as words ("sat" "clique" "N P" or "NP" — keep them natural)
- For subscripts (e.g. A_TM), say "A sub T M"
- For Greek letters, say their name (phi, psi, etc.)
- Don't restate the label; just teach

Topic content to teach:
{content[:2000]}

Output ONLY the narration. No headers, no commentary, no quotes around it."""

    payload = json.dumps({
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 450,
        "temperature": 0.7,
    })
    result = subprocess.run(
        ["curl", "-s", "https://api.openai.com/v1/chat/completions",
         "-H", f"Authorization: Bearer {KEY}",
         "-H", "Content-Type: application/json",
         "-d", payload],
        capture_output=True, text=True, timeout=60
    )
    try:
        d = json.loads(result.stdout)
        return d['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"[ERROR generating script: {e}; raw: {result.stdout[:200]}]"


def gen_tts(text, out_path):
    """Call OpenAI TTS-1-HD with nova voice."""
    payload = json.dumps({
        "model": "tts-1-hd",
        "voice": "nova",
        "input": text,
    })
    result = subprocess.run(
        ["curl", "-s", "https://api.openai.com/v1/audio/speech",
         "-H", f"Authorization: Bearer {KEY}",
         "-H", "Content-Type: application/json",
         "-d", payload,
         "--output", str(out_path)],
        capture_output=True, timeout=60
    )
    return out_path.exists() and out_path.stat().st_size > 0


def insert_chips(html, tool_id, sections):
    """Insert chips at the top of each section."""
    # We need a stable way to find each section. Use the section-label text.
    for idx, (label, _) in enumerate(sections, start=1):
        audio_name = f"p{tool_id:02d}-s{idx}"
        # Look for <section ...><div class="section-label...">LABEL<
        escaped_label = re.escape(label)
        # Pattern: <section><div class="section-label...">LABEL<
        chip = CHIP_TEMPLATE.format(audio=audio_name)
        # Find: <div class="section-label[^"]*"[^>]*>LABEL<
        pat = r'(<section[^>]*>)(\s*<div class="section-label[^"]*"[^>]*>' + escaped_label + r'</div>)'
        replacement = r'\1' + chip + r'\2'
        new_html, n = re.subn(pat, replacement, html, count=1)
        if n > 0:
            html = new_html
        else:
            # Sometimes section starts with newline or whitespace
            pat2 = r'(<section[^>]*>\s*<div class="section-label[^"]*"[^>]*>)' + escaped_label
            new_html, n = re.subn(pat2, chip + r'\1' + label, html, count=1)
            if n > 0:
                html = new_html
            else:
                print(f"  WARN: could not find anchor for section '{label}'")
    return html


def process_tool(tool_file):
    """Generate all section audios for one tool and insert chips."""
    name = tool_file.name
    m = re.match(r'p(\d+)-', name)
    if not m: return
    tool_id = int(m.group(1))
    html = tool_file.read_text()

    # Skip if already has chips (look for "../audio/sections/" pattern)
    if '../audio/sections/' in html:
        print(f"{name}: already has section chips, skipping")
        return

    problem_title, problem_sub = get_problem_context(html)
    sections = extract_sections(html)
    if not sections:
        print(f"{name}: no sections found")
        return

    print(f"{name}: {len(sections)} sections (title: {problem_title[:60]})")

    # Generate scripts in parallel (up to 4 at once)
    def make_one(idx_label_text):
        idx, (label, text) = idx_label_text
        audio_name = f"p{tool_id:02d}-s{idx}"
        txt_path = AUDIO / f"{audio_name}.txt"
        mp3_path = AUDIO / f"{audio_name}.mp3"
        # Skip if already exists
        if mp3_path.exists() and mp3_path.stat().st_size > 5000:
            return (idx, label, "[cached]")
        script = gen_script(label, text, problem_title, problem_sub)
        txt_path.write_text(script + "\n")
        ok = gen_tts(script, mp3_path)
        return (idx, label, "ok" if ok else "fail")

    indexed = list(enumerate(sections, start=1))
    with ThreadPoolExecutor(max_workers=10) as ex:
        results = list(ex.map(make_one, indexed))

    for idx, label, status in results:
        print(f"  s{idx} ({label[:50]}): {status}")

    # Insert chips into HTML
    new_html = insert_chips(html, tool_id, sections)
    tool_file.write_text(new_html)
    print(f"  HTML updated with {len(sections)} chips")


def main():
    files = sorted(TOOLS.glob('p*.html'))
    # Filter by tool id range if args given
    if len(sys.argv) >= 3:
        lo, hi = int(sys.argv[1]), int(sys.argv[2])
        files = [f for f in files if (m := re.match(r'p(\d+)', f.name)) and lo <= int(m.group(1)) <= hi]
    for f in files:
        try:
            process_tool(f)
        except Exception as e:
            print(f"ERROR on {f.name}: {e}")
        time.sleep(0.3)  # be nice to the API


if __name__ == '__main__':
    main()
