#!/usr/bin/env bash
# L-SI box 107 runner (resumable: a query whose answer line is already in its out/ file is skipped).
# Environment: L-NEW's one217.py and the five tower genomes, read-only, by git archive of claude/l-new a143d4060 into a temp dir.
# Steps: abandon | small | exact3 | exact4 | bil | up | pn     (SAT answers are SEARCH answers of cadical195 via python-sat: uncertified)
set -u
cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
TOP=${TOP:-$(git rev-parse --show-toplevel)}; mkdir -p out
git -C "$TOP" archive a143d4060 experiments/new/box217/one217.py experiments/new/box212/inst | tar -x -C "$T" || exit 3
[ "$(sha1sum < "$T/experiments/new/box217/one217.py" | cut -c1-40)" = "$(cat one217.sha1)" ] || { echo "one217.py sha1 mismatch"; exit 4; }
ONE="$T/experiments/new/box217"; INST="$T/experiments/new/box212/inst"
q() {  # q OUTFILE KEY COMMAND...: run unless a line starting with KEY is in OUTFILE; append the tool's answer line
  local f=$1 key=$2; shift 2; touch "$f"; grep -q -- "^$key " "$f" && { echo "skip: $key"; return 0; }
  "$@" > "$T/line" 2>&1 || { echo "FAILED: $key"; cat "$T/line"; exit 1; }
  grep -- "^$key " "$T/line" >> "$f" || { echo "no answer line: $key"; cat "$T/line"; exit 1; }
}
case "${1:-abandon}" in
abandon) python3 -I abandon107.py "$ONE" --lmax 7 "$INST"/DBL4_d20_F30.json "$INST"/RECF4_d20_F60.json "$INST"/H5_d20_F62.json "$INST"/H6_d24_F126.json "$INST"/HIT7_d28_F254.json > out/abandon107.out; echo "exit $?"; cat out/abandon107.out;;
small)   # k = 2 on the 2-level ladder (model kept and replayed); exact maxima of the run length at d = 2
  q out/syn107.out "SYN107 d 2 T 6 goal full:2" python3 syn107.py 2 6 full:2 --notime --out out/k2_d2.json
  python3 -I replay107.py "$ONE" out/k2_d2.json > out/replay107.out; cat out/replay107.out
  for T_ in 3 4 5 6 7 8; do q out/syn107.out "SYN107 d 2 T $T_ goal len" python3 syn107.py 2 $T_ len --notime; done;;
exact3)  q out/syn107.out "SYN107 d 3 T 22 goal full:4" python3 syn107.py 3 22 full:4 --notime;;
exact4)  q out/syn107.out "SYN107 d 4 T 12 goal full:4" python3 syn107.py 4 12 full:4 --notime
         q out/syn107.out "SYN107 d 4 T 52 goal full:4" python3 syn107.py 4 52 full:4 --notime;;
bil)     for dT in "2 2" "2 3" "3 3" "3 4" "4 6" "4 7" "5 8" "5 9" "6 11" "6 12"; do set -- $dT; q out/bil107.out "BIL107 d $1 T $2 full None" python3 bil107.py $1 $2 --notime; done;;
up)      # upward ladders (Xi-targets on higher levels only, ranks by level): longest runs, and k = 3
         for dT in "2 3" "2 4" "3 5" "3 6" "4 7" "4 8"; do set -- $dT; q out/up107.out "UP107 d $1 T $2 goal len" python3 up107.py $1 $2 len --notime; done
         q out/up107.out "UP107 d 4 T 7 goal full:2" python3 up107.py 4 7 full:2 --notime --out out/up_k2_d4.json
         python3 -I replay107.py "$ONE" out/up_k2_d4.json > out/replay107_up.out; cat out/replay107_up.out
         q out/up107.out "UP107 d 5 T 12 goal full:4" python3 up107.py 5 12 full:4 --notime
         # the k = 3 model out/up_k3_d6.json was found by `up107.py 6 14 full:4 --out ...` (about 60 s); it is kept and replayed, and the answer line re-derived:
         q out/up107.out "UP107 d 6 T 14 goal full:4" python3 up107.py 6 14 full:4 --notime
         python3 -I replay107.py "$ONE" out/up_k2_d4.json out/up_k3_d6.json > out/replay107_up.out; cat out/replay107_up.out;;
pn)      for PT in "1 1" "1 2" "2 2" "2 3" "3 4" "3 5" "4 6" "4 7" "5 10"; do set -- $PT; q out/pn107.out "PN107 P $1 T $2 chain 0 full None" python3 pn107.py $1 $2 --notime; done
         for PT in "3 22" "4 30" "5 20" "6 20"; do set -- $PT; q out/pn107.out "PN107 P $1 T $2 chain 1 full \[(2, 0)\]" python3 pn107.py $1 $2 --chain --full 2:0 --notime; done;;
esac
