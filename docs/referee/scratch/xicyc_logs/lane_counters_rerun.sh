cd /tmp/claude-0/-home-user-parity-games-challange/2faf64dc-0ced-5bb7-8568-ade29db453ad/scratchpad/lnew/experiments/new/box191
O=/tmp/claude-0/-home-user-parity-games-challange/2faf64dc-0ced-5bb7-8568-ade29db453ad/scratchpad/cnt
python3 -I level0_191.py 1000 41 > $O/level0.out 2>&1 &
python3 -I subrun191.py 1000 21 > $O/subrun.out 2>&1 &
python3 -I seg1p191.py 300 11 > $O/seg1p.out 2>&1 &
python3 -I brseg_gen191.py random 2000 3 12 > $O/brseg.out 2>&1 &
wait
python3 -I howard3_191.py 500 31 > $O/h31.out 2>&1 &
python3 -I howard3_191.py 500 32 > $O/h32.out 2>&1 &
python3 -I rand191.py eq 300 1 > $O/eq1.out 2>&1 &
python3 -I rand191.py eq 1000 2 > $O/eq2.out 2>&1 &
wait
echo ALLDONE > $O/done
