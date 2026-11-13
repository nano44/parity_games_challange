#!/bin/bash
# experiments/red-b self-check (L-RED-B; run by scripts/verify.sh). Fast (a few seconds): the engine against brute force on
# 200 small genomes, the counters on three frozen genomes (must be 0), both controls (must fire), and the pinned outputs.
set -u
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1
fail=0
x=$(python3 xcheck.py 200 7 8 | tail -n 1); case "$x" in *"naive-walk value mismatches 0 mismatches 0") ;; *) echo "red-b: xcheck FAILED: $x"; fail=1;; esac
t=$(python3 lev.py --all inst/CFI3_n48.json inst/RINT_n48.json ../new/box203/inst/MWR4_2.json | tail -n 1)
z=$(echo "$t" | sed 's/^.*| //' | tr ' ' '\n' | grep -E '^[0-9]+$' | grep -cv '^0$')
[ "$z" = "0" ] || { echo "red-b: lev counters not all 0: $t"; fail=1; }
c1=$(RB_CTRL=1 python3 lev.py inst/CFI3_n48.json | tail -n 1); case "$c1" in *" l3 0 "*) echo "red-b: control 1 did not fire"; fail=1;; esac
c2=$(RB_CTRL=2 python3 lev.py inst/CFI3_n48.json | tail -n 1); case "$c2" in *" p1 0 "*) echo "red-b: control 2 did not fire"; fail=1;; esac
# B2 (box 209, successor 3): Gamma3 engine vs brute force, the 32 lev3 counters on three frozen genomes (sum 0), controls fire
x3=$(python3 xcheck3.py 1 120 4 | tail -n 1); case "$x3" in *"valfail 0 padfail 0"*) ;; *) echo "red-b: xcheck3 FAILED: $x3"; fail=1;; esac
for f in inst/CFI3_n48.json inst/RINT_n48.json ../new/box203/inst/MWR4_2.json; do
  l3=$(python3 lev3.py --all "$f" | tail -n 1); case "$l3" in *" sum 0 "*) ;; *) echo "red-b: lev3 not 0: $l3"; fail=1;; esac
done
c31=$(python3 lev3.py --ctrl=1 inst/CFI3_n48.json | tail -n 1); case "$c31" in *" sum 0 "*) echo "red-b: lev3 control 1 did not fire"; fail=1;; esac
c32=$(python3 lev3.py --ctrl=2 inst/CFI3_n48.json | tail -n 1); case "$c32" in *" p2 "*) ;; *) echo "red-b: lev3 control 2 did not fire"; fail=1;; esac
ce=$(python3 edomctl.py 1 300 5 12 | tail -n 1); case "$ce" in *" k2 "*) ;; *) echo "red-b: E-DOM control did not fire k2: $ce"; fail=1;; esac
if [ -f data/SHA1SUMS ]; then (cd data && sha1sum -c --quiet SHA1SUMS) || { echo "red-b: data/SHA1SUMS mismatch"; fail=1; }; fi
(cd inst && echo "d55b20b8f00d0e4e08c606879c8c6ec44283e114  CFI3_n48.json
35b48913a615d4c88f0eb69afc38e42ecb0ab0b0  RINT_n48.json" | sha1sum -c --quiet) || { echo "red-b: inst sha1 mismatch"; fail=1; }
# B6 attempt 2 (P-N5-EXP, successor 5): the rule G_k, the proof's direct test and R104 membership, on k = 6 (0.1 s)
g6=$(python3 gk.py 6 | tail -n 1); case "$g6" in *"key 62 howard 4 k 1 khalf 2 maxsw 16") ;; *) echo "red-b: gk.py 6 FAILED: $g6"; fail=1;; esac
l6=$(python3 b6lemma.py 6 | tail -n 1); case "$l6" in *"kfact 0 vfact 0 sched 0 tlen 0 rest 0 swk 0 T 62 "*) ;; *) echo "red-b: b6lemma 6 FAILED: $l6"; fail=1;; esac
lc=$(B6L_CTRL=1 python3 b6lemma.py 5 | tail -n 1); case "$lc" in *" sched 0 "*) echo "red-b: b6lemma control did not fire"; fail=1;; esac
m6=$(python3 b6member.py data/b6b/G/G_6.json | tail -n 1); case "$m6" in *"member 1 viol 0 "*) ;; *) echo "red-b: b6member G_6 FAILED: $m6"; fail=1;; esac
mc=$(python3 b6member.py --ctrl 8 data/b6b/G/G_6.json | tail -n 1); case "$mc" in *"member 0 "*) ;; *) echo "red-b: b6member control did not fire: $mc"; fail=1;; esac
if [ -f data/b6b/SHA1SUMS_b6b ]; then (cd data/b6b && sha1sum -c --quiet SHA1SUMS_b6b) || { echo "red-b: data/b6b SHA1SUMS mismatch"; fail=1; }; fi
[ $fail -eq 0 ] && echo "red-b check PASS" || echo "red-b check FAILED"
exit $fail
