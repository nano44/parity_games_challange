#!/bin/bash
# Box 210 Addendum A (L-NEW successor 72): DATA runs of brute210.py (brute-force reply of Odd; every even up-set H; every reference
# state), resumable. Run from experiments/new/box210:  bash run210b.sh H | I
#   H: exhaustive: every split of every 3-vertex game with every start strategy; every general split-form game with 2 choice and 3
#      priority vertices;   I: random games and the three controls.
set -u
export PYTHONDONTWRITEBYTECODE=1
main() {   # one function: bash has read the whole script before it runs anything
one() { local out="out/$1"; shift; [ -s "$out" ] && return 0; "$@" > "$out.tmp" 2>&1 && mv "$out.tmp" "$out"; }
case "${1:-H}" in
H)
  one brute210_exh3.out python3 brute210.py exh3
  one brute210_exhgen23.out python3 brute210.py exhgen 2 3 ;;
I)
  one brute210_rand.out bash -c 'python3 brute210.py rsplit 2131 20000 5 6 3; python3 brute210.py rsplit 2132 10000 6 8 3; python3 brute210.py rgen 2133 20000 4 5 6; python3 brute210.py rgen 2134 10000 5 7 8'
  one brute210_ctrl.out bash -c 'CTRL=H python3 brute210.py rsplit 2135 3000 5 6 3; CTRL=Hodd python3 brute210.py rsplit 2136 3000 5 6 3; CTRL=nosplit python3 brute210.py rsplit 2137 3000 5 6 3' ;;
esac
echo "run210b ${1:-H} finished"
}
main "$@"; exit $?
