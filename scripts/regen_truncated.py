#!/usr/bin/env python3
"""Regenerate truncated MP3 files identified by ffprobe duration check.
Uses requests-like blocking call so we know the full audio is downloaded."""
import os, sys, json, subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = Path(__file__).resolve().parent.parent
AUDIO = ROOT / "audio" / "sections"
KEY = open("/tmp/oai_key.txt").read().strip()

def gen_tts(text, out_path):
    """Call OpenAI TTS-1-HD, write the response body to disk."""
    payload = json.dumps({"model": "tts-1-hd", "voice": "nova", "input": text})
    # Use --max-time to give the request enough time
    result = subprocess.run(
        ["curl", "-s", "-S", "--max-time", "90",
         "https://api.openai.com/v1/audio/speech",
         "-H", f"Authorization: Bearer {KEY}",
         "-H", "Content-Type: application/json",
         "-d", payload,
         "--output", str(out_path)],
        capture_output=True, timeout=120
    )
    if result.returncode != 0:
        return False, result.stderr.decode('utf-8', errors='ignore')[:200]
    if not out_path.exists() or out_path.stat().st_size < 30000:
        return False, f"file too small: {out_path.stat().st_size if out_path.exists() else 'missing'}"
    return True, "ok"

def regen_one(stem):
    txt = AUDIO / f"{stem}.txt"
    mp3 = AUDIO / f"{stem}.mp3"
    if not txt.exists():
        return (stem, False, "no txt")
    text = txt.read_text().strip()
    # Overwrite the bad mp3 (curl --output truncates)
    ok, msg = gen_tts(text, mp3)
    if ok:
        size = mp3.stat().st_size
        return (stem, True, f"{size} bytes")
    return (stem, False, msg)

def main():
    stems = sys.argv[1:] if len(sys.argv) > 1 else \
            [l.strip() for l in open('/tmp/truncated_mp3s.txt')]
    print(f"Regenerating {len(stems)} files...")
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(regen_one, s): s for s in stems}
        ok = fail = 0
        for fut in as_completed(futs):
            stem, success, msg = fut.result()
            if success:
                ok += 1
                print(f"  ✓ {stem}: {msg}")
            else:
                fail += 1
                print(f"  ✗ {stem}: {msg}")
    print(f"\nDone: {ok} ok, {fail} failed")

if __name__ == '__main__':
    main()
