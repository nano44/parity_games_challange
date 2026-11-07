#!/usr/bin/env python3
"""L-RED 54 R217: fdiff.py under an E-DOM priority state. Usage: edomdiff.py n state.json"""
import sys, os, json, runpy
import fried, comp
from edomprio import apply
n, sf = int(sys.argv[1]), sys.argv[2]; d = json.load(open(sf)); V = apply(fried.game(n), d["order"], d["par"])
fried.game = lambda m: V; comp.game = lambda m: V
sys.argv = ["fdiff.py", str(n)]; runpy.run_path("fdiff.py", run_name="__main__")
