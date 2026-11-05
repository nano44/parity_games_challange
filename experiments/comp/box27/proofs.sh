#!/bin/bash
# L-COMP box 27: Glucose 4 proofs for the 16 d 3 cubes of T >= 9 and their RUP check by drup.c (resumable: skips cubes with a .chk)
cd "$(dirname "$0")"; P=${PDIR:-proofs}; mkdir -p $P
for c in $(seq 0 15); do echo $c; done | xargs -P ${PAR:-2} -I{} bash -c '
  [ -f '$P'/c{}.chk ] && exit 0
  python3 mkproof.py 3 9 {} '$P' glucose4 > '$P'/c{}.gen 2>&1 &&
  ./drup '$P'/d3_L9_c{}.cnf '$P'/d3_L9_c{}.glucose4.proof > '$P'/c{}.chk.tmp 2>&1 &&
  sha1sum '$P'/d3_L9_c{}.glucose4.proof >> '$P'/c{}.chk.tmp; mv '$P'/c{}.chk.tmp '$P'/c{}.chk;
  rm -f '$P'/d3_L9_c{}.glucose4.proof'
