#!/bin/bash
# L-NEW box 160: resumable driver; skips a target whose log already has a RESULT line. Usage: run_iso.sh "ENV" d t ...
# env LRED must point at the extracted claude/l-red tree (5f3e89e1).
cd "$(dirname "$0")"/..
envs="$1"; d="$2"; shift 2
for t in "$@"; do
  tag=$(echo "$envs" | tr ' =,:' '____')_d${d}_t${t}
  if grep -q "^RESULT" box160/log/$tag.log 2>/dev/null; then echo "skip $tag"; continue; fi
  env $envs python3 box160/iso.py $d $t box160/out/$tag.json > box160/log/$tag.log.part 2>&1; mv box160/log/$tag.log.part box160/log/$tag.log
  grep -q "UNSAT" box160/log/$tag.log && break
done
