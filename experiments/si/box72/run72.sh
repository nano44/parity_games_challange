#!/usr/bin/env bash
# L-SI box 72: resumable runner for the box 70 frame (DIMACS kept, no DRUP: NOPROOF=1). Job = "K m MODE T [T2]".
# Writes log/<name>.log (skipped if finished); the gzipped CNF stays in dump/ (gitignored); its sha1 is in the log.
cd "$(dirname "$0")"; mkdir -p log dump
for job in "$@"; do
  set -- $job; K=$1; shift
  name="K${K}_$(echo "$*" | tr ' ' '_')"; f=log/$name.log
  if [ -f "$f" ] && grep -q -- "-> \(SAT\|UNSAT\)" "$f"; then echo "skip $name"; continue; fi
  K=$K DUMP=dump NOPROOF=1 python3 ../box70/frame.py "$@" > "$f.part" 2>&1
  tag=$(grep -o "^DIMACS [^ ]*" "$f.part" | awk '{print $2}')
  [ -n "$tag" ] && [ -f dump/$tag ] && gzip -f dump/$tag
  mv "$f.part" "$f"
done
