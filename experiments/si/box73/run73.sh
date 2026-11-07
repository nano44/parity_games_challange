#!/usr/bin/env bash
# L-SI box 73: resumable queue of frame pq queries (one-flip run with the flip after exactly PRE steps; DIMACS kept, no DRUP).
# Job = "m PRE POST" -> frame.py m pq 1 PRE+POST with PRE fixed. log/pq_m<m>_<PRE>_<POST>.log (skipped if finished).
cd "$(dirname "$0")"; mkdir -p log dump
for job in "$@"; do
  set -- $job; m=$1; p=$2; q=$3; f=log/pq_m${m}_${p}_${q}.log
  if [ -f "$f" ] && grep -q -- "-> \(SAT\|UNSAT\)" "$f"; then echo "skip $f"; continue; fi
  PRE=$p DUMP=dump NOPROOF=1 python3 ../box70/frame.py $m pq 1 $((p + q)) > "$f.part" 2>&1
  tag=$(grep -o "^DIMACS [^ ]*" "$f.part" | awk '{print $2}'); [ -n "$tag" ] && [ -f dump/$tag ] && gzip -f dump/$tag
  mv "$f.part" "$f"
done
