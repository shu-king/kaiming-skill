#!/usr/bin/env bash
# Fetch Kaiming's talk slide PDFs (people.csail.mit.edu) and YouTube auto-captions.
# Idempotent: skips files that already exist.
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
SEED="$REPO/assets/seed_talks.txt"
OUT="$REPO/talks"
mkdir -p "$OUT"

UA="kaiming-he-skill/1.0"

# Read seed file: skip blank lines and comments. Fields are whitespace-separated:
# <type> <url> <short_id> <year> <title...>
grep -vE '^\s*(#|$)' "$SEED" | while read -r type url short_id year rest; do
  case "$type" in
    pdf)
      out="$OUT/${short_id}.pdf"
      if [ -f "$out" ]; then
        size=$(stat -f%z "$out" 2>/dev/null || stat -c%s "$out")
        if [ "$size" -gt 50000 ]; then
          echo "[skip] $out already present ($size bytes)"
          continue
        fi
      fi
      echo "[pdf] $url"
      curl --silent --show-error --fail-with-body \
           --user-agent "$UA" \
           --max-time 60 \
           --output "$out" \
           "$url" && echo "  → $out" || echo "  FAILED $url"
      sleep 1
      ;;
    youtube)
      if ls "$OUT/${short_id}".*.vtt >/dev/null 2>&1; then
        echo "[skip] $short_id captions already present"
        continue
      fi
      echo "[yt]  $url"
      yt-dlp \
        --write-auto-sub --sub-lang en \
        --skip-download \
        --sub-format vtt \
        -o "$OUT/${short_id}.%(ext)s" \
        "$url" || echo "  yt-dlp failed for $url"
      sleep 2
      ;;
    *)
      echo "[?]   unknown type: $type"
      ;;
  esac
done

echo
echo "Done. Files in $OUT:"
ls -la "$OUT" 2>/dev/null | tail -n +4
