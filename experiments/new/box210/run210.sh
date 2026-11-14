#!/bin/bash
# Box 210 (L-NEW successor 72): the DATA runs of docs/new/N5-GENLEVEL-box210.md §5, resumable (a set is skipped when its output exists).
# Run from experiments/new/box210:  bash run210.sh A | B | C | D | E | F | G
#   A: gen210.py --pg on the exponential families (Friedmann's switch-all N = 2..7: box191/inst/sae_N.pg; friedmannsubexp_1..8 and
#      fearnleysubexp_1..6: experiments/n5-box21/instances; switchallexp_N3, zadehexp_N5, randomfacetsubexp_N5: experiments/si/instances),
#      with the sha1 of every instance file;   B: random games;   C: the three controls;
#   D: --xcheck (values against si.Engine, state by state) on the files of A;   E: scale profiles (scale210.py --blocks);
#   F: every reference state b (GEN_ALLB=1) on six family games and 1,500 random games; hill-climbs towards long runs (climb210.py);
#   G: n5lev210.py: the same counters along N5's own sigma-sequence (K5, L4 are expected to fire).
# Outputs in out/.
set -u
export PYTHONDONTWRITEBYTECODE=1
main() {   # one function: bash has read the whole script before it runs anything
I=../box191/inst; J=../../n5-box21/instances; K=../../si/instances
FAM="$I/sae_2.pg $I/sae_3.pg $I/sae_4.pg $I/sae_5.pg $I/sae_6.pg $I/sae_7.pg $J/friedmannsubexp_1.pg $J/friedmannsubexp_2.pg $J/friedmannsubexp_3.pg $J/friedmannsubexp_4.pg
$J/friedmannsubexp_5.pg $J/friedmannsubexp_6.pg $J/friedmannsubexp_7.pg $J/friedmannsubexp_8.pg $J/fearnleysubexp_1.pg $J/fearnleysubexp_2.pg $J/fearnleysubexp_3.pg
$J/fearnleysubexp_4.pg $J/fearnleysubexp_5.pg $J/fearnleysubexp_6.pg $K/switchallexp_N3.pg $K/zadehexp_N5.pg $K/randomfacetsubexp_N5.pg"
one() { local out="out/$1"; shift; [ -s "$out" ] && return 0; "$@" > "$out.tmp" 2>&1 && mv "$out.tmp" "$out"; }
case "${1:-A}" in
A)
  one gen210_instances.sha1 sha1sum $FAM
  one gen210_families.out python3 gen210.py --pg $FAM ;;
B)
  one gen210_rand.out bash -c 'python3 gen210.py 2111 3000 8 6 3 1; python3 gen210.py 2112 3000 8 6 3 0; python3 gen210.py 2113 1500 16 10 3 1; python3 gen210.py 2114 400 40 12 4 1; GEN_H=none python3 gen210.py 2115 1500 12 8 3 1' ;;
C)
  one gen210_ctrl.out bash -c 'GEN_CTRL=1 python3 gen210.py 2116 300 16 10 3 1; GEN_CTRL=2 python3 gen210.py 2117 300 8 6 3 0; GEN_CTRL=3 python3 gen210.py 2118 3000 6 6 3 1' ;;
F)
  one gen210_allb.out bash -c 'GEN_ALLB=1 python3 gen210.py --pg $0 $1 $2 $3 $4 $5; GEN_ALLB=1 python3 gen210.py 2120 1500 8 6 3 1' $I/sae_2.pg $I/sae_3.pg $I/sae_4.pg $J/friedmannsubexp_1.pg $J/friedmannsubexp_2.pg $J/friedmannsubexp_3.pg
  one climb210.out bash -c 'GEN_ALLB=1 python3 climb210.py 2121 6000 7 8; python3 climb210.py 2122 6000 10 10; python3 climb210.py 2123 3000 14 12' ;;
G)
  one n5lev210.out bash -c 'python3 n5lev210.py --pg $0 $1 $2 $3 $4 $5 $6 $7; python3 n5lev210.py 2124 1500 8 6 3 1; python3 n5lev210.py 2125 500 16 10 3 1' $I/sae_2.pg $I/sae_3.pg $I/sae_4.pg $I/sae_5.pg $I/sae_6.pg $J/friedmannsubexp_2.pg $J/friedmannsubexp_3.pg $J/friedmannsubexp_4.pg ;;
D)
  one gen210_xcheck.out python3 gen210.py --xcheck $FAM ;;
E)
  one scale210.out python3 scale210.py --blocks $I/sae_2.pg $I/sae_3.pg $I/sae_4.pg $I/sae_5.pg $I/sae_6.pg $I/sae_7.pg $J/friedmannsubexp_2.pg $J/friedmannsubexp_3.pg $J/friedmannsubexp_4.pg $J/friedmannsubexp_5.pg $J/friedmannsubexp_6.pg $J/fearnleysubexp_2.pg $J/fearnleysubexp_3.pg $J/fearnleysubexp_4.pg $J/fearnleysubexp_5.pg ;;
esac
echo "run210 ${1:-A} finished"
}
main "$@"; exit $?
