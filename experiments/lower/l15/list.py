#!/usr/bin/env python3
"""L-LOWER 15: print a client's required-preference list (l13/reqpref.py) as lines "t r". Usage: list.py GENOME TARGET X P"""
import sys, os, subprocess, ast
here = os.path.dirname(os.path.abspath(__file__))
l = subprocess.run([sys.executable, os.path.join(here, '..', 'l13', 'reqpref.py')] + sys.argv[1:5], capture_output=True, text=True).stdout
for t, r in ast.literal_eval(l[l.index('['):l.index('] |') + 1]): print(t, r)
