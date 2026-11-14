#!/bin/bash
# L-COMP box 27: resource log every ${INT:-60} s (Lead 18:50Z): free -m, df, top RSS processes. Appends to $1, synced each sample.
OUT=${1:?}; while true; do
  { echo "== $(date -u +%H:%M:%S) up $(cut -d' ' -f1 /proc/uptime)s"; free -m | sed -n 2p; df -h / | tail -1;
    ps -eo rss,etime,args --sort=-rss | head -6 | cut -c1-110; } >> "$OUT"; sync "$OUT" 2>/dev/null; sleep ${INT:-60}; done
