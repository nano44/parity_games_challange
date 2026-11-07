#!/usr/bin/env bash
# L-SI box 70: resumable driver. Each job "m MODE T [T2]" writes log/<name>.log; a finished log (line with SAT/UNSAT) is skipped.
cd "$(dirname "$0")"
for job in "$@"; do
  name=$(echo "$job" | tr ' ' '_'); f=log/$name.log
  if [ -f "$f" ] && grep -q -- "-> \(SAT\|UNSAT\)" "$f"; then echo "skip $name"; continue; fi
  python3 frame.py $job > "$f.part" 2>&1 && mv "$f.part" "$f"
done
