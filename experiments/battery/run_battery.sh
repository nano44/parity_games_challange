#!/usr/bin/env bash
# THE BATTERY: run_battery.sh '<engine command>' [set ...]   (sets: a b c d e; default: every set present). See README.md.
# Never pipe this script: a pipe hides its exit code (0 pass, 1 wrong winner / bad strategy, 2 engine error, 3 battery broken).
exec python3 -B "$(cd "$(dirname "$0")" && pwd)/battery.py" "$@"
