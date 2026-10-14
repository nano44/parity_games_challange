#!/usr/bin/env bash
# Diagonal cells in convention V (Lead 20:09Z): w^V, s^V at (n,n), (n,n+1), and the TARGET alphabet {2..n+2} (m=2).
cd "$(dirname "$0")"
lane() { for c in "$@"; do set -- $c; python3 diag.py $1 $2 V $3 --min-letter $4 --klo $5 2>&1 | grep RESULT; done; }
case "$1" in
  A) lane "2 2 weak 1 1" "2 3 weak 1 2" "3 3 weak 1 4" "3 4 weak 1 4" "2 4 weak 2 2" "3 5 weak 2 4" "4 4 weak 1 6" "4 5 weak 1 6" ;;
  B) lane "2 2 strong 1 1" "2 3 strong 1 2" "3 3 strong 1 4" "3 4 strong 1 4" "2 4 strong 2 2" "3 5 strong 2 4" "4 4 strong 1 6" "4 5 strong 1 6" "4 6 strong 2 6" "5 5 strong 1 8" ;;
  C) lane "4 6 weak 2 6" "5 5 weak 1 8" ;;
  D) lane "5 6 strong 1 9" "5 7 strong 2 9" "5 6 weak 1 8" "5 7 weak 2 8" ;;
esac
