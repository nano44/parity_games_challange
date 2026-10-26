#!/usr/bin/env bash
# Box 13: run every line of scale_jobs.txt (python3 <line> > <out>.log), 4 at a time.
cd "$(dirname "$0")"
grep -v '^#' scale_jobs.txt | xargs -P 4 -I{} sh -c 'out=$(echo "{}" | sed "s/.*--out //"); python3 {} > $out.log 2>&1'
