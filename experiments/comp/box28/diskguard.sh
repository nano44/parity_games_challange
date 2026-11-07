#!/bin/bash
# L-COMP box 28: kill proof generation (dimproof.py) when free disk drops below MINGB (default 6); logs to log/diskguard.out
MIN=${MINGB:-6}; while true; do f=$(df -BG --output=avail / | tail -1 | tr -dc 0-9)
  if [ "$f" -lt "$MIN" ]; then echo "$(date -u +%FT%TZ) free ${f}G < ${MIN}G: killing dimproof.py" >> log/diskguard.out; pkill -f "box27/dimproof.py"; fi; sleep 30; done
