#!/usr/bin/env bash
# REFEREE s33: Friedmann's G_n (own transcription) and its wrapper under N5'-xi / N5. Logs wrap_logs/f11_*.out
cd "$(dirname "$0")"; mkdir -p wrap_logs
python3 -I wrap_f11.py 1 2 3 4 5 6 7 8 9 10 > wrap_logs/f11_H_fig4.out 2>&1
VER=table4 python3 -I wrap_f11.py 1 2 3 4 5 6 7 8 > wrap_logs/f11_H_table4.out 2>&1
WRAP=xi python3 -I wrap_f11.py 1 2 3 4 5 6 > wrap_logs/f11_W_xi_fig4.out 2>&1 &
WRAP=xi VER=table4 python3 -I wrap_f11.py 1 2 3 4 5 > wrap_logs/f11_W_xi_table4.out 2>&1 &
WRAP=spec python3 -I wrap_f11.py 1 2 3 4 5 6 > wrap_logs/f11_W_spec_fig4.out 2>&1 &
WRAP=xi PERM=1 python3 -I wrap_f11.py 1 2 3 4 5 > wrap_logs/f11_W_xi_fig4_perm.out 2>&1 &
wait
echo "f11 done $(date -u +%Y-%m-%dT%H:%M:%SZ)"
