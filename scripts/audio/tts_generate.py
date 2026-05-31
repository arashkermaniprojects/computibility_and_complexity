"""Generate MP3 files from the narration scripts using OpenAI TTS.

Usage:
    export OPENAI_API_KEY=sk-...
    python3 tts_generate.py             # generate all 51
    python3 tts_generate.py 1 3         # only module 1, section 3
    python3 tts_generate.py 4           # only module 4 (all its sections)

Output:
    audio/m{module}-s{section}.mp3
"""
import os, sys, time
import urllib.request
import json

VOICE = 'nova'
MODEL = 'tts-1-hd'
SPEED = 1.0  # 1.0 = normal; we keep it normal for educational pacing

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEXT_DIR = os.path.join(ROOT, 'scripts', 'audio', 'text')
OUT_DIR = os.path.join(ROOT, 'audio')

def tts_call(text, out_path, api_key):
    payload = json.dumps({
        'model': MODEL,
        'input': text,
        'voice': VOICE,
        'speed': SPEED,
        'response_format': 'mp3',
    }).encode('utf-8')
    req = urllib.request.Request(
        'https://api.openai.com/v1/audio/speech',
        data=payload,
        headers={
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json',
        },
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    with open(out_path, 'wb') as f:
        f.write(data)
    return len(data)

def main():
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print('ERROR: set OPENAI_API_KEY environment variable', file=sys.stderr)
        sys.exit(1)

    os.makedirs(OUT_DIR, exist_ok=True)

    # Optional filter by module/section
    only_module = int(sys.argv[1]) if len(sys.argv) >= 2 else None
    only_section = int(sys.argv[2]) if len(sys.argv) >= 3 else None

    text_files = sorted(f for f in os.listdir(TEXT_DIR) if f.startswith('m') and f.endswith('.txt'))
    targets = []
    for fname in text_files:
        # parse mX-sY.txt
        body = fname[:-4]
        m_part, s_part = body.split('-')
        m = int(m_part[1:])
        s = int(s_part[1:])
        if only_module and m != only_module:
            continue
        if only_section and s != only_section:
            continue
        targets.append((m, s, fname))

    print(f'Generating {len(targets)} MP3s with voice="{VOICE}", model="{MODEL}"')
    total_bytes = 0
    for i, (m, s, fname) in enumerate(targets, 1):
        with open(os.path.join(TEXT_DIR, fname)) as fh:
            text = fh.read().strip()
        out_name = f'm{m}-s{s}.mp3'
        out_path = os.path.join(OUT_DIR, out_name)
        # Skip if already exists and non-empty (cheap re-run)
        if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
            print(f'  [{i}/{len(targets)}] skip {out_name} (already exists, {os.path.getsize(out_path)} bytes)')
            continue
        try:
            n = tts_call(text, out_path, api_key)
            total_bytes += n
            print(f'  [{i}/{len(targets)}] {out_name} · {len(text)} chars → {n:,} bytes mp3')
            time.sleep(0.3)  # gentle rate limiting
        except urllib.error.HTTPError as e:
            print(f'  [{i}/{len(targets)}] FAILED {out_name}: HTTP {e.code} — {e.read().decode("utf-8", errors="replace")[:200]}', file=sys.stderr)
            sys.exit(2)
        except Exception as e:
            print(f'  [{i}/{len(targets)}] FAILED {out_name}: {type(e).__name__} — {e}', file=sys.stderr)
            sys.exit(2)

    print(f'\nDone. Total mp3 bytes generated this run: {total_bytes:,} ({total_bytes/1024/1024:.2f} MB)')

if __name__ == '__main__':
    main()
