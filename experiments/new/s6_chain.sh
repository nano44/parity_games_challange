#!/usr/bin/env bash
# S6 (cunningham) lifted renumbering chain on switchbestexp: climb at N=2, lift the best numbering by labels to N+1
# (lift.py), climb again from it (renum2 --init), up to N=$NMAX. Output out/s6/chain_N<N>.{txt,pg,pg.perm}.
cd "$(dirname "$0")"; mkdir -p out/s6; R=${RULE:-cunningham}; F=${FAM:-switchbestexp}; S=${STEPS:-800}
./renum2 $R out/inst/${F}_2.pg --restarts 2 --steps $S --seed 7 --out out/s6/${F}_${R}_N2.pg > out/s6/${F}_${R}_N2.txt
for N in $(seq 3 ${NMAX:-5}); do
  P=$((N-1)); python3 lift.py out/inst/${F}_$P.pg out/s6/${F}_${R}_N$P.pg.perm out/inst/${F}_$N.pg > out/s6/${F}_${R}_lift$N.perm
  timeout ${TO:-3000} ./renum2 $R out/inst/${F}_$N.pg --restarts 1 --steps $S --seed $N --init out/s6/${F}_${R}_lift$N.perm --out out/s6/${F}_${R}_N$N.pg > out/s6/${F}_${R}_N$N.txt
done
