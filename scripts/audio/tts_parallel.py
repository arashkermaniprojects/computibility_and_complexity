"""Parallel version of tts_generate.py — issues up to N concurrent TTS calls."""
import os, sys, time, json
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

VOICE = 'nova'
MODEL = 'tts-1-hd'
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEXT_DIR = os.path.join(ROOT, 'scripts', 'audio', 'text')
OUT_DIR = os.path.join(ROOT, 'audio')
CONCURRENCY = 8

def tts_one(text, out_path, api_key):
    payload = json.dumps({'model': MODEL, 'input': text, 'voice': VOICE, 'response_format': 'mp3'}).encode('utf-8')
    req = urllib.request.Request(
        'https://api.openai.com/v1/audio/speech',
        data=payload,
        headers={'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'},
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    with open(out_path, 'wb') as f:
        f.write(data)
    return len(data)

def task(fname, api_key):
    body = fname[:-4]
    m_part, s_part = body.split('-')
    m, s = int(m_part[1:]), int(s_part[1:])
    out_name = f'm{m}-s{s}.mp3'
    out_path = os.path.join(OUT_DIR, out_name)
    if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
        return (out_name, 'skip', 0)
    with open(os.path.join(TEXT_DIR, fname)) as fh:
        text = fh.read().strip()
    t0 = time.time()
    try:
        n = tts_one(text, out_path, api_key)
        return (out_name, 'ok', n, time.time() - t0)
    except Exception as e:
        return (out_name, 'fail', str(e)[:200])

def main():
    api_key = os.environ['OPENAI_API_KEY']
    os.makedirs(OUT_DIR, exist_ok=True)
    files = sorted(f for f in os.listdir(TEXT_DIR) if f.startswith('m') and f.endswith('.txt'))
    print(f'Targets: {len(files)}, concurrency: {CONCURRENCY}')
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as ex:
        futs = {ex.submit(task, f, api_key): f for f in files}
        done = 0
        for fut in as_completed(futs):
            res = fut.result()
            done += 1
            print(f'  [{done}/{len(files)}] {res[0]} {res[1]} {res[2:] if len(res)>2 else ""}')
    print(f'\nElapsed: {time.time()-t0:.1f}s')

if __name__ == '__main__':
    main()
