#!/bin/bash
# L-COMP box 28 (Lead 05:18Z item 3): L-SI frame query 2 («T_2(3) >= 13», box27/lsi/dump/m3_tk_T13_T20_K2_NOIM0.cnf.gz, sha1 f3d4b6ad
# unzipped) -- the open sub-cubes of L-COMP 9 (box27/subcubes0.sh: cube C = BASE (3 literals on vars 2, 8, 14), sub s = bit 0 -> +20,
# bit 1 -> +26) split further into 8 PIECES on vars 32, 38, 44 (piece p: bit 0 -> +32, bit 1 -> +38, bit 2 -> +44; all 8 sign patterns,
# so the pieces partition the sub-cube). Per piece: Glucose 4 proof streamed by box27/dimproof.py, then box27/drup.c; proof and cube CNF
# deleted after the check (VERIFIED or not); records log/q2/q2_c<C>s<s>p<p>.gen|.chk (final once .chk holds «s VERIFIED»).
# Resumable: a piece with a VERIFIED .chk is skipped; any other piece is regenerated from scratch (Glucose is deterministic).
# Usage: PDIR=dir ./q2pieces.sh   (order: c0s0, c0s1, c4s0, c4s2, c0s2, c0s3, c4s3; one piece at a time)
cd "$(dirname "$0")"; P="${PDIR:?}"; mkdir -p "$P"; B=../box27; F="$P/m3_tk_T13_T20_K2_NOIM0.cnf"
[ -f "$F" ] || zcat $B/lsi/dump/m3_tk_T13_T20_K2_NOIM0.cnf.gz > "$F"
[ "$(sha1sum < "$F" | cut -c1-8)" = f3d4b6ad ] || { echo "query 2 DIMACS sha1 mismatch"; exit 1; }
for cs in 0:0 0:1 4:0 4:2 0:2 0:3 4:3; do C=${cs%:*}; s=${cs#*:}
  if [ $C = 0 ]; then BASE=-2,-8,-14; else BASE=-2,-8,14; fi
  a=$(( s & 1 ? 20 : -20 )); b=$(( s & 2 ? 26 : -26 ))
  for p in 0 1 2 3 4 5 6 7; do n=q2_c${C}s${s}p$p; R=log/q2/$n
    [ -f $R.chk ] && grep -q "^s VERIFIED" $R.chk && continue
    e=$(( p & 1 ? 32 : -32 )); f=$(( p & 2 ? 38 : -38 )); g=$(( p & 4 ? 44 : -44 )); cube="$BASE,$a,$b,$e,$f,$g"; pf="$P/$n.proof"
    python3 $B/dimproof.py "$F" "$pf" "$cube" > $R.gen 2>&1
    t0=$(date +%s); { $B/drup "$pf.cnf" "$pf"; echo "drup exit $? wall $(( $(date +%s) - t0 )) s"; } > $R.chk.tmp 2>&1; mv $R.chk.tmp $R.chk
    rm -f "${P:?}/$n.proof" "${P:?}/$n.proof.cnf"
    echo "$(date -u +%FT%TZ) $n ($cube): $(grep -o 'glucose4 [A-Z]* [0-9.]* s\|sha1 [0-9a-f]*\|bytes [0-9]*' $R.gen | tr '\n' ' ') $(grep -h '^s ' $R.chk)" >> log/q2/summary.txt
  done
done
echo "$(date -u +%FT%TZ) q2pieces: all pieces processed" >> log/q2/summary.txt
