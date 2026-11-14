#!/usr/bin/env bash
# L-SI box 104: N5'-xi on the FREE-priority Gamma3-shaped games F_n (Friedmann's switchallexp_n compiled by L-RED 54's comp.py, built
# without E-DOM), controls, two engines, state-for-state comparison with Howard on G_n, Lemma FREE-REACH's counters on random free
# genomes, the quotes of docs/si/box104-map.md. Engines read-only: L-RED at claude/l-red 8c01d40e (env LRED: experiments/red/r217),
# L-NEW at claude/l-new fcba92fc (env LNEW: experiments/new, experiments/si/si.py, experiments/harness, experiments/hard-families,
# experiments/n5-second). About 40 min, one core (the n = 7, 8 rows of the free xi run take most of it). Output: out/, inst/F_*.pg.
# NMAX (default 8) caps the free xi run. Run before runw104.sh.
set -u
cd "$(dirname "$0")"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p out inst "$T/red" "$T/new"
TOP=${TOP:-$(git rev-parse --show-toplevel)}
git -C "$TOP" archive 8c01d40e experiments/red/r217 | tar -x -C "$T/red" || exit 3
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness experiments/hard-families experiments/n5-second | tar -x -C "$T/new" || exit 3
export LRED="$T/red" LNEW="$T/new"
NS=$(seq 2 "${NMAX:-8}")
python3 -I free104.py prio $NS > out/prio.out || exit 1
python3 -I free104.py run edom xi 2 3 4 5 6 > out/edom_xi.out || exit 1
python3 -I free104.py run free spec 2 3 4 5 6 > out/free_spec.out || exit 1
python3 -I xck104.py 2 3 4 5 > out/xck.out || exit 1
python3 -I xtraj104.py 2 3 4 5 6 > out/xtraj.out || exit 1
CTRL=1 python3 -I xtraj104.py 2 3 > out/xtraj_ctrl.out || exit 1
python3 -I freereach104.py 1041 2000 > out/freereach.out || exit 1
python3 -I freereach104.py 1042 1000 6 4 3 >> out/freereach.out || exit 1
ALG=spec python3 -I freereach104.py 1041 2000 >> out/freereach.out || exit 1
CTRL=1 python3 -I freereach104.py 1041 100 > out/freereach_ctrl.out || exit 1
CTRL=2 python3 -I freereach104.py 1041 100 >> out/freereach_ctrl.out || exit 1
for n in 2 3 4 5 6 7 8; do python3 -I free104.py pg "$n" "inst/F_$n.pg" || exit 1; done   # SHA1SUMS is written by runw104.sh
python3 -I free104.py run free xi $NS > out/free_xi.out || exit 1
(cd "$TOP" && python3 -I "$OLDPWD/quotes104.py" src) > out/quotes104.out || exit 1
echo DONE
