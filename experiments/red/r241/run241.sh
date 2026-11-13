#!/usr/bin/env bash
# L-RED 69 R241: kt241.py on a list of genome files (one per line in LIST), one process per genome with a timeout (TO s, default 1800);
# appends one line per genome to OUTF; RESUMABLE (a genome whose name already has a line in OUTF is skipped). Env as kt241.py (LNEW, KT_*).
# Usage: run241.sh LIST OUTF
set -u
LIST=$1; OUTF=$2; TO=${TO:-1800}; D=$(cd "$(dirname "$0")" && pwd); touch "$OUTF"
for f in $(cat "$LIST"); do
  b=$(basename "$f")
  grep -q " $b: \| $b TIMEOUT" "$OUTF" && continue
  l=$(timeout "$TO" python3 "$D/kt241.py" json "$f" 2>&1 | grep "^KT241.* $b: ")
  if [ -z "$l" ]; then echo "KT241 $b TIMEOUT ($TO s) or error" >> "$OUTF"; else echo "$l" >> "$OUTF"; fi
done
echo "RUN241 END $(date -u +%FT%TZ) list $(basename "$LIST") lines $(grep -c '^KT241' "$OUTF")" >> "$OUTF"
