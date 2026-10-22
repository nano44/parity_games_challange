#!/bin/bash
# L-RED (Opus 5.5): R14 sweep. usage: experiments/red/distract/sweep.sh OUTDIR p MODE LSPEC(N|2N|NN|0|C<k>) N...
# prints tangles, iterations and Oink's --verify result of the pinned A_DTL on distract.py's game (base tc+ N).
out=$1; p=$2; m=$3; ls=$4; shift 4; mkdir -p "$out"
for N in "$@"; do
  case $ls in N) L=$N;; 2N) L=$((2*N));; NN) L=$((N*N));; 0) L=0;; C*) L=${ls#C};; esac
  f=$out/d_${p}_${m}_${ls}_$N.pg
  python3 experiments/red/distract/distract.py tools/oink/build/tc+ $N $L $p $m > $f
  r=$(timeout 300 tools/oink/build/oink --dtl --no-single --no-wcwc --no-loops -v $f /dev/null 2>&1)
  t=$(echo "$r" | grep -o "dominions and [0-9]* tangles" | grep -o "[0-9]* tangles")
  it=$(echo "$r" | grep -o "solved in [0-9]* iterations" | grep -o "[0-9]*")
  vf=$(timeout 300 tools/oink/build/oink --dtl --no-single --no-wcwc --no-loops --verify $f /dev/null 2>&1 | grep -c "verified")
  echo "p=$p $m L=$L N=$N n=$(($(wc -l <$f)-1)) $t it=$it verified=$vf"
done
