#!/usr/bin/env bash
# L-SI successor 40: regenerate the DIMACS of every frame UNSAT listed in UNSAT-LIST.txt (DUMPONLY=1, no solving) into $1 (default
# /tmp/si_unsat) and compare its sha1 with the listed one. Run from anywhere. Prints OK / MISMATCH per line; exit 1 on any mismatch.
set -uo pipefail
cd "$(dirname "$0")/box70"; out=${1:-/tmp/si_unsat}; mkdir -p "$out"; bad=0
while IFS='|' read -r q sha cmd; do
  [ -z "$sha" ] && continue; case "$q" in \#*) continue;; esac
  got=$(env $cmd 2>/dev/null | grep -o "^DIMACS [^ ]* sha1 [0-9a-f]*" | awk '{print $4}')
  if [ "$got" = "$(echo $sha)" ]; then echo "OK $q"; else echo "MISMATCH $q (got $got)"; bad=1; fi
done < ../UNSAT-LIST.txt
exit $bad
