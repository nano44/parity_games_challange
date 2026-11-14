#!/usr/bin/env bash
# fetch.sh: THE ONLY NETWORK STEP of the R131 build. build.sh never fetches by itself; it reads fetch.txt, which
# this script writes. Run it by hand (or `bash build.sh --fetch`) when a lane head has moved, then copy the new
# heads from fetch.txt into cfg.json ("heads", "trunk.commit", "line", ...): fetch.sh does NOT edit cfg.json.
#
# It runs, for every lane branch named in cfg.json "heads" and "pins", for claude/checker and for the trunk branch:
#   git fetch origin +refs/heads/claude/<lane>:refs/remotes/origin/claude/<lane>     (plain fetch, no --depth)
# and records `date -u`, each fetch's exit code, the fetched heads and the `git ls-remote` lines into fetch.txt.
# It changes nothing but remote-tracking refs: no merge, no checkout, no commit, no push.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(git -C "$HERE" rev-parse --show-toplevel)"
OUTF="$HERE/fetch.txt"
TMPF="$HERE/fetch.txt.new"
LANES="$(python3 -B -c "
import json,sys
c=json.load(open(sys.argv[1],encoding='utf-8'))
print(' '.join(list(c['heads'].keys())+[k for k in c.get('pins',{}) if not k.startswith('_')]+['checker']))
" "$HERE/cfg.json")"
TRUNK="$(python3 -B -c "
import json,sys
print(json.load(open(sys.argv[1],encoding='utf-8'))['trunk']['branch'])
" "$HERE/cfg.json")"
rc_all=0
{
  echo "date $(date -u)"
  for b in $LANES; do
    git -C "$ROOT" fetch origin "+refs/heads/claude/$b:refs/remotes/origin/claude/$b" > "$HERE/fetch.err" 2>&1
    rc=$?
    [ $rc -ne 0 ] && rc_all=1
    echo "fetch claude/$b rc $rc head $(git -C "$ROOT" rev-parse "refs/remotes/origin/claude/$b" 2>/dev/null)"
  done
  git -C "$ROOT" fetch origin "+refs/heads/$TRUNK:refs/remotes/origin/$TRUNK" > "$HERE/fetch.err" 2>&1
  rc=$?
  [ $rc -ne 0 ] && rc_all=1
  echo "fetch $TRUNK rc $rc head $(git -C "$ROOT" rev-parse "refs/remotes/origin/$TRUNK" 2>/dev/null)"
  echo "local HEAD $(git -C "$ROOT" rev-parse HEAD) branch $(git -C "$ROOT" rev-parse --abbrev-ref HEAD)"
  git -C "$ROOT" ls-remote origin > "$HERE/fetch.lsremote" 2> "$HERE/fetch.err"
  rc=$?
  [ $rc -ne 0 ] && rc_all=1
  echo "ls-remote rc $rc"
  for b in $LANES; do
    grep -E "refs/heads/claude/$b\$" "$HERE/fetch.lsremote" | tr '\t' ' ' | sed 's/^/ls-remote /'
  done
  grep -E "refs/heads/$TRUNK\$" "$HERE/fetch.lsremote" | tr '\t' ' ' | sed 's/^/ls-remote /'
  echo "rc $rc_all"
} > "$TMPF"
rm -f "$HERE/fetch.err" "$HERE/fetch.lsremote"
mv "$TMPF" "$OUTF"
cut -c1-160 "$OUTF"
exit $rc_all
