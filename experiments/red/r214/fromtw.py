#!/usr/bin/env python3
"""L-RED R214: tw text (fa format + «start» line) -> box150 JSON with that start (r212/conv.py read_txt). Usage: fromtw.py in.txt out.json"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r212")); import conv
G = conv.read_txt(sys.argv[1]); G.pop("xorder", None)
for line in open(sys.argv[1]):
    w = line.split()
    if w and w[0] == "start": G["start"] = [int(x) for x in w[1:]]
json.dump(G, open(sys.argv[2], "w"))
