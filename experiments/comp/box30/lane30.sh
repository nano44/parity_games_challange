#!/bin/bash
# L-COMP box 30 (Lead 07:12Z): one restart-proof climb lane. Usage: lane30.sh LANE SEEDFILE SEEDBASE LV GUARD HITLEVEL [ITERS]
# Unit u (state out/LANE.unit): rclimb30 from out/LANE_best.txt (or SEEDFILE), seed SEEDBASE+u, ITERS proposals (default 2e7),
# ANNEAL 0.15 (rclimb lowers it linearly to 0 within the unit), LV, GUARD as rclimb. After the unit: its best replaces LANE_best if
# its score is higher; a line goes to out/LANE.log. HIT: the best's F(0..HITLEVEL) = 2^(l+2) - 2 for every l (exact doubling over F(0) = 2)
# -> copy to out/LANE_HIT_<u>.txt and a line in out/HITS.txt. A restart loses only the unit in flight.
cd "$(dirname "$0")"; LANE=$1; SEED=$2; BASE=$3; export LV=$4 GUARD=$5; H=$6; IT=${7:-20000000}; X=${RCLIMB:?}
u=$(cat out/$LANE.unit 2>/dev/null || echo 0)
while true; do
  in=out/${LANE}_best.txt; [ -s $in ] || in=$SEED
  ANNEAL=0.15 OUT=out/${LANE}_u$u.txt $X $in $((BASE+u)) $IT > out/${LANE}_u$u.run 2>&1
  sc() { grep -o "# score -*[0-9]*" $1 | grep -o -- "-*[0-9]*$"; }
  new=$(sc out/${LANE}_u$u.txt); old=$( [ -s out/${LANE}_best.txt ] && sc out/${LANE}_best.txt || echo -999999999 )
  [ -n "$new" ] && [ "$new" -gt "$old" ] && cp out/${LANE}_u$u.txt out/${LANE}_best.txt
  F=$(grep -o "F [-0-9 ]*moves" out/${LANE}_best.txt | sed 's/^F //; s/ moves//')
  echo "$(date -u +%FT%TZ) $LANE unit $u seed $((BASE+u)) unit-score $new best $(sc out/${LANE}_best.txt) F $F" >> out/$LANE.log
  if python3 -c "import sys; F=list(map(int,sys.argv[2:])); h=int(sys.argv[1]); sys.exit(0 if len(F)>h and all(F[l]==2**(l+2)-2 for l in range(h+1)) else 1)" $H $F; then
    cp out/${LANE}_best.txt out/${LANE}_HIT_u$u.txt; echo "$(date -u +%FT%TZ) HIT $LANE unit $u sha1 $(sha1sum < out/${LANE}_HIT_u$u.txt | cut -c1-40) F $F" >> out/HITS.txt; fi
  rm -f out/${LANE}_u$u.run; u=$((u+1)); echo $u > out/$LANE.unit
done
