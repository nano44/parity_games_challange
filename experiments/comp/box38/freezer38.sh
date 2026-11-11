#!/bin/bash
# L-COMP box 38: every 30 s, every out/climb38/BEST_*.json not yet in out/climb38/FROZEN.txt gets a line (UTC, file, sha1 of the file,
# the BEST log line's numbers). The climb writes each BEST file once under a content-hash name and never rewrites it. Restart-safe.
cd "$(dirname "$0")/out/climb38" || exit 1
touch FROZEN.txt
while true; do
  for f in BEST_*.json; do
    [ -f "$f" ] || continue; grep -q " $f " FROZEN.txt && continue
    ln=$(grep -h "BEST $f " ../climb38_*.log 2>/dev/null | head -1 | cut -c1-400)
    echo "$(date -u +%FT%TZ) $f sha1 $(sha1sum < "$f" | cut -c1-40) $ln" >> FROZEN.txt
  done; sleep 30; done
