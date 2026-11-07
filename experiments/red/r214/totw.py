#!/usr/bin/env python3
"""L-RED R214: box150 JSON (R197 convention, renumbered) -> tw text (r212/conv.py totxt + a «start» line). Usage: totw.py in.json out.txt"""
import sys, os, json, subprocess
H = os.path.dirname(os.path.abspath(__file__))
subprocess.run(["python3", os.path.join(H, "..", "r212", "conv.py"), "totxt", sys.argv[1], sys.argv[2]], check=True)
G = json.load(open(sys.argv[1])); open(sys.argv[2], "a").write("start " + " ".join(map(str, G["start"])) + "\n")
