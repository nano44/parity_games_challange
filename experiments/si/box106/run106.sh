#!/usr/bin/env bash
# L-SI box 106 §3b-§3c runner (resumable: a job whose output line is already in its out/ file is skipped). Builds box 105's environment
# (LNEW, LRED as runclimb106.sh) and the two RUP checkers in a temp dir: drup.c (L-COMP, claude/l-comp 07cec8399, read-only copy
# ../box71/ref/drup.c) and REFEREE's ref_rup.c (claude/referee 2005aee7 docs/referee/scratch/ref_rup.c, read with git show).
# Steps: audit | controls | query. A solve job (solve106.py, Glucose 4 with DRUP) is followed: on UNSAT by both checkers on the DIMACS
# and the proof (lines «CHECK106 TAG drup|ref_rup: <last line>»), then a REGENERATION (CNF and proof rebuilt from scratch in a temp dir;
# line «REGEN106 TAG cnf equal ... proof equal ...»), and the proof gzipped to dump/TAG.drup.gz (kept in git if <= 50 MB); on SAT by the
# N5 replay of the decoded genome (box 105 val105.py). DIMACS files stay in dump/ (git-ignored): cnf106.py regenerates them (sha1 printed).
set -u
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p out best dump "$T/red" "$T/new" "$T/chk"
TOP=${TOP:-$(git rev-parse --show-toplevel)}; SI=${SI:-$TOP/experiments/si}
git -C "$TOP" archive 8c01d40e experiments/red/r217 | tar -x -C "$T/red" || exit 3
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness experiments/hard-families experiments/n5-second | tar -x -C "$T/new" || exit 3
export LNEW="$T/new" LRED="$T/red" BOX104="${BOX104:-$SI/box104}"
cp ../box71/ref/drup.c "$T/chk/drup.c" && git -C "$TOP" show 2005aee7:docs/referee/scratch/ref_rup.c > "$T/chk/ref_rup.c" || exit 3
[ "$(sha1sum < "$T/chk/drup.c" | cut -c1-40)" = 2d4b8eab8fe9e9035c396733bb400d9d6e7d2366 ] || exit 4
[ "$(sha1sum < "$T/chk/ref_rup.c" | cut -c1-40)" = 707c484d449e595d36acdbebebb380294932c4b0 ] || exit 4
gcc -O2 -o "$T/chk/drup" "$T/chk/drup.c" && gcc -O2 -o "$T/chk/ref_rup" "$T/chk/ref_rup.c" || exit 3
step=${1:-audit}
job() {  # job OUTFILE PATTERN COMMAND...: run unless PATTERN is already a line of OUTFILE
  local f=$1 pat=$2; shift 2; touch "$f"; grep -q -- "$pat" "$f" && { echo "skip: $pat"; return 0; }
  "$@" >> "$f" || exit 1
}
solve() {  # solve LEN TAG [--genome FILE]
  local L=$1 tag=$2; shift 2; local f=out/solve106.out
  touch $f; grep -q "^SOLVE106 $tag " $f && { echo "skip: $tag"; return 0; }
  python3 -I solve106.py $L $tag "$@" > "$T/line" || exit 1
  if grep -q ": UNSAT |" "$T/line"; then
    for c in drup ref_rup; do echo "CHECK106 $tag $c: $("$T/chk/$c" dump/$tag.cnf dump/$tag.drup | tail -n 1)" >> "$T/line"; done
    mkdir -p "$T/re" && (cd "$T/re" && cp -r "$OLDPWD"/best . 2>/dev/null; python3 -I "$OLDPWD/solve106.py" $L $tag "$@" > /dev/null) || exit 1
    echo "REGEN106 $tag cnf equal $(cmp -s dump/$tag.cnf "$T/re/dump/$tag.cnf" && echo yes || echo NO) proof equal $(cmp -s dump/$tag.drup "$T/re/dump/$tag.drup" && echo yes || echo NO)" >> "$T/line"
    rm -rf "$T/re"; gzip -9 -n -f dump/$tag.drup; echo "PROOF106 $tag dump/$tag.drup.gz bytes $(stat -c %s dump/$tag.drup.gz) sha1 $(sha1sum < dump/$tag.drup.gz | cut -c1-40)" >> "$T/line"
  else
    python3 -I ../box105/val105.py best/$tag.json | sed "s/^/N5REPLAY106 $tag: /" >> "$T/line" || exit 1
  fi
  cat "$T/line" >> $f
}
if [ "$step" = audit ]; then
  job out/aud106.out "^AUD106 seed 1065 genomes 300 full:" python3 -I aud106.py 1065 300 --full
  job out/aud106.out "^AUD106 seed 1066 genomes 2000:" python3 -I aud106.py 1066 2000
  job out/aud106.out "^AUD106 seed json genomes 40 full:" python3 -I aud106.py json --full $(ls best/climb106_*.json | sort -V)
  for c in 1 2 3; do job out/aud106.out "^AUD106 seed 1067 genomes 100 CTRL $c:" env CTRL=$c python3 -I aud106.py 1067 100; done
fi
if [ "$step" = controls ]; then
  solve 5 c5; solve 5 g5 --genome best/climb106_1.json; solve 6 g6 --genome best/climb106_1.json; solve 9 c9
fi
if [ "$step" = query ]; then   # the monolithic solve (not used: no answer after about 60 min, Glucose 4; see §3d)
  solve 6 q6
fi
cert() {  # cert TAG: both checkers on dump/TAG.cnf + dump/TAG.drup, then gzip the proof; lines appended to $T/line
  local tag=$1
  for c in drup ref_rup; do echo "CHECK106 $tag $c: $("$T/chk/$c" dump/$tag.cnf dump/$tag.drup | tail -n 1)" >> "$T/line"; done
}
if [ "$step" = cubes ]; then   # §3d: 384 cubes of «L* >= 6» (start x level-0 gate order) and the coverage proof; one block per cube
  f=out/cube106.out; touch $f
  for s in 0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111; do
    for g in $(python3 -I -c "import itertools; print(' '.join(''.join(map(str, p)) for p in itertools.permutations(range(4))))"); do
      tag=q6_s${s}_g$g; grep -q "^PROOF106 $tag " $f && continue
      python3 -I cube106.py 6 $s $g $tag > "$T/line" || exit 1
      grep -q ": UNSAT |" "$T/line" || { cat "$T/line" >> $f; echo "SAT CUBE $tag"; exit 5; }
      cert $tag
      mkdir -p "$T/re" && (cd "$T/re" && python3 -I "$OLDPWD/cube106.py" 6 $s $g $tag > /dev/null) || exit 1
      echo "REGEN106 $tag cnf equal $(cmp -s dump/$tag.cnf "$T/re/dump/$tag.cnf" && echo yes || echo NO) proof equal $(cmp -s dump/$tag.drup "$T/re/dump/$tag.drup" && echo yes || echo NO)" >> "$T/line"
      rm -rf "$T/re" dump/$tag.cnf; gzip -9 -n -f dump/$tag.drup
      echo "PROOF106 $tag dump/$tag.drup.gz bytes $(stat -c %s dump/$tag.drup.gz) sha1 $(sha1sum < dump/$tag.drup.gz | cut -c1-40)" >> "$T/line"
      cat "$T/line" >> $f
    done
  done
  if ! grep -q "^PROOF106 cover6 " $f; then
    python3 -I cover106.py 6 > "$T/line" || exit 1
    grep -q ": UNSAT |" "$T/line" || { cat "$T/line" >> $f; exit 6; }
    cert cover6; gzip -9 -n -f dump/cover6.drup; rm -f dump/cover6.cnf
    echo "PROOF106 cover6 dump/cover6.drup.gz bytes $(stat -c %s dump/cover6.drup.gz) sha1 $(sha1sum < dump/cover6.drup.gz | cut -c1-40)" >> "$T/line"
    cat "$T/line" >> $f
  fi
fi
certone() {  # certone TAG CMD...: run CMD (prints one line, writes dump/TAG.cnf and on UNSAT dump/TAG.drup), both checkers, regeneration,
            # proof gzipped (kept if <= 50 MB gzipped, else deleted with its sha1 printed), CNF deleted (regenerable); lines to out/certcore106.out
  local tag=$1; shift; local f=out/certcore106.out; touch $f; grep -q "^PROOF106 $tag " $f && return 0
  "$@" > "$T/line" || exit 1
  grep -q ": UNSAT |\| UNSAT |" "$T/line" || { cat "$T/line" >> $f; echo "NOT UNSAT: $tag"; exit 5; }
  cert $tag
  mkdir -p "$T/re" && (cd "$T/re" && mkdir -p out && cp "$OLDPWD"/out/cores106_L6.json out/ && "$@" > /dev/null) || exit 1
  echo "REGEN106 $tag cnf equal $(cmp -s dump/$tag.cnf "$T/re/dump/$tag.cnf" && echo yes || echo NO) proof equal $(cmp -s dump/$tag.drup "$T/re/dump/$tag.drup" && echo yes || echo NO)" >> "$T/line"
  rm -rf "$T/re" dump/$tag.cnf; gzip -9 -n -f dump/$tag.drup; local sz=$(stat -c %s dump/$tag.drup.gz) sh=$(sha1sum < dump/$tag.drup.gz | cut -c1-40)
  [ "$sz" -gt 52428800 ] && { rm -f dump/$tag.drup.gz; echo "PROOF106 $tag dump/$tag.drup.gz bytes $sz sha1 $sh (deleted: > 50 MB; regenerate)" >> "$T/line"; } || echo "PROOF106 $tag dump/$tag.drup.gz bytes $sz sha1 $sh" >> "$T/line"
  cat "$T/line" >> $f
}
if [ "$step" = cover ]; then certone cover6 python3 -I "$PWD/covercert106.py" 6 cover6; fi
if [ "$step" = certcores ]; then   # certcores MAXLITS: every core with at most MAXLITS literals, in file order
  for i in $(python3 -I -c "import json,sys; M=json.load(open('out/cores106_L6.json')); print(' '.join(str(i) for i,c in enumerate(M) if len(c) <= int(sys.argv[1])))" "${2:-4}"); do
    certone core$i python3 -I "$PWD/certcore106.py" 6 $i core$i
  done
fi
echo DONE "$step"
