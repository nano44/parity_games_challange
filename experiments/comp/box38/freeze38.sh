#!/bin/bash
# L-COMP box 38: one-shot freezer (freezer38.sh's loop body once): every out/climb38/BEST_*.json not yet in FROZEN.txt gets a line
# (UTC, file, sha1, the BEST log line). Climbs write each BEST file once under a content-hash name.
cd "$(dirname "$0")/out/climb38" || exit 1; touch FROZEN.txt
for f in BEST_*.json; do grep -q " $f " FROZEN.txt && continue
  ln=$(grep -h "BEST $f " ../climb38_*.log 2>/dev/null | head -1 | cut -c1-400)
  echo "$(date -u +%FT%TZ) $f sha1 $(sha1sum < "$f" | cut -c1-40) $ln" >> FROZEN.txt; done
