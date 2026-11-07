#!/bin/bash
# L-NEW box 160: generic resumable driver (like run_iso.sh, any env, FREE0 modes included). Usage: run_env.sh "ENV" tag d t ...
cd "$(dirname "$0")"/..
envs="$1"; tagp="$2"; d="$3"; shift 3
for t in "$@"; do
  tag=${tagp}_d${d}_t${t}
  if grep -q "^RESULT" box160/log/$tag.log 2>/dev/null; then grep -q UNSAT box160/log/$tag.log && break; continue; fi
  env $envs python3 box160/iso.py $d $t box160/out/$tag.json > box160/log/$tag.log.part 2>&1; mv box160/log/$tag.log.part box160/log/$tag.log
  grep -q "UNSAT" box160/log/$tag.log && break
done
