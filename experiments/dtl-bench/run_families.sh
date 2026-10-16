#!/usr/bin/env bash
# Steps (3)-(4): every family in families.txt (or those named), 3 sweeps in parallel. Logs: out/fam_<family>.log.
# Wall times are measured with up to 3 sweeps sharing 4 cores: compare sizes within a family, not across runs.
set -uo pipefail
cd "$(dirname "$0")"
TMAX="${TMAX:-200}"; TO="${TO:-400}"; RTO="${RTO:-120}"
grep -v '^#' families.txt | while IFS='|' read -r fam gen sizes; do
  fam=$(echo $fam); gen=$(echo $gen)
  if [ $# -gt 0 ] && ! [[ " $* " == *" $fam "* ]]; then continue; fi
  printf '%s\t%s\t%s\n' "$fam" "$gen" "$sizes"
done | xargs -P 3 -d '\n' -I{} bash -c 'IFS=$'"'"'\t'"'"' read -r f g s <<< "{}"; python3 sweep.py "$f" --gen "$g" --sizes $s --tmax '"$TMAX"' --timeout '"$TO"' --ref-timeout '"$RTO"' > out/fam_$f.log 2>&1; echo "$f exit $?: $(tail -1 out/fam_$f.log)"'
