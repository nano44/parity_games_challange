#!/bin/bash
# L-COMP box 27: Glucose 4 proofs for the 16 d 3 cubes of T >= 9 (mkproof.py) and their RUP check by drup.c.
# Resumable: a cube with c<id>.chk is done; an existing proof without .chk is re-checked without regeneration.
# Proofs (~1 GB each) are deleted after the check; c<id>.chk keeps the drup output, the proof's sha1 and size, and the wall time.
# Usage: PDIR=dir PAR=2 ./proofs.sh
cd "$(dirname "$0")"
export P="${PDIR:-proofs}"; mkdir -p "$P"
one() {
  c=$1; pf="${P:?}/d3_L9_c$c.glucose4.proof"
  [ -f "$P/c$c.chk" ] && return 0
  if [ ! -f "$pf" ] || ! grep -q UNSAT "$P/c$c.gen" 2>/dev/null; then
    python3 mkproof.py 3 9 "$c" "$P" glucose4 > "$P/c$c.gen" 2>&1 || return 1
  fi
  t0=$(date +%s)
  { ./drup "$P/d3_L9_c$c.cnf" "$pf"; echo "drup exit $?"; echo "drup wall $(( $(date +%s) - t0 )) s";
    sha1sum "$pf"; stat -c "proof size %s bytes" "$pf"; } > "$P/c$c.chk.tmp" 2>&1
  if grep -q "^s VERIFIED" "$P/c$c.chk.tmp"; then mv "$P/c$c.chk.tmp" "$P/c$c.chk"; rm -f "$pf"; fi
}
export -f one
seq 0 15 | xargs -P "${PAR:-2}" -I{} bash -c 'one {}'
