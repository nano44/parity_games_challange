#!/usr/bin/env bash
# L-SI box 71: resumable job runner for the box 70 frame. Job = "K m MODE T [T2] [PROOF]". Writes log/<name>.log (skipped if finished).
# PROOF=1: DIMACS + DRUP into dump/; on UNSAT the proof is RUP-checked at once with ref/drup.c (L-COMP's checker), the verdict, sha1
# and size are appended to the log, the CNF is gzipped (kept), and the proof is gzipped and kept only if <= 50 MB gzipped.
cd "$(dirname "$0")"; mkdir -p log dump
for job in "$@"; do
  set -- $job; K=$1; shift; PR=${@: -1}; if [ "$PR" = "PROOF" ]; then set -- "${@:1:$(($#-1))}"; else PR=""; fi
  name="K${K}_$(echo "$*" | tr ' ' '_')"; f=log/$name.log
  if [ -f "$f" ] && grep -q -- "-> \(SAT\|UNSAT\)" "$f"; then echo "skip $name"; continue; fi
  if [ -n "$PR" ]; then K=$K DUMP=dump python3 ../box70/frame.py "$@" > "$f.part" 2>&1; else K=$K python3 ../box70/frame.py "$@" > "$f.part" 2>&1; fi
  tag=$(grep -o "^DIMACS [^ ]*" "$f.part" | awk '{print $2}' | sed 's/\.cnf$//')
  if [ -n "$PR" ] && grep -q -- "-> UNSAT" "$f.part"; then
    ./drup dump/$tag.cnf dump/$tag.drup | tail -n 1 | sed 's/^/DRUPCHECK /' >> "$f.part"
    gzip -f dump/$tag.drup; sz=$(stat -c %s dump/$tag.drup.gz); echo "DRUP.gz bytes $sz sha1 $(sha1sum dump/$tag.drup.gz | cut -c1-40)" >> "$f.part"
    [ "$sz" -gt 52428800 ] && { rm -f dump/$tag.drup.gz; echo "DRUP.gz deleted (> 50 MB; sha1 above)" >> "$f.part"; }
  fi
  [ -n "$tag" ] && [ -f dump/$tag.cnf ] && gzip -f dump/$tag.cnf
  mv "$f.part" "$f"
done
