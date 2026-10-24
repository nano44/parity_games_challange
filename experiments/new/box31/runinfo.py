#!/usr/bin/env python3
"""Box 31: list the W-flat runs of route-form pieces of one game: piece kind (U1: c_w above c_θ; P3: c_θ above c_w; EQ: c_θ = c_w),
state type at the piece start, |R|, run start/length, per-vertex switches (vertex: (level, switches, run steps)).
Usage: runinfo.py game.pg [minper]"""
import sys
from casccheck import *
g = load(sys.argv[1]); mp = int(sys.argv[2]) if len(sys.argv) > 2 else 1; rows, o = rows_of(g); E = Engine(g); k = 0
while k < len(rows):
    if not rows[k]["rf"]: k += 1; continue
    j = k
    while j + 1 < len(rows) and rows[j + 1]["rf"] and all(rows[j + 1][f] == rows[k][f] for f in ("ph", "R", "th", "w")): j += 1
    Rs = [v for v in rows[k]["R"] if v != o]; a_, b_ = E.rank[rows[k]["cth"]], E.rank[rows[k]["cw"]]
    kind = "U1" if b_ > a_ else ("P3" if a_ > b_ else "EQc")
    i = k
    while i < j:
        if rows[i]["fb"] or any(rows[i]["Wk"][v] != rows[i + 1]["Wk"][v] for v in Rs): i += 1; continue
        a = i; per = {}
        while i < j and not rows[i]["fb"] and all(rows[i]["Wk"][v] == rows[i + 1]["Wk"][v] for v in Rs):
            for v in Rs:
                if g.owner[v] == 0 and rows[i]["s"][v] != rows[i + 1]["s"][v]: per.setdefault(v, [rows[i]["Wl"][v] - rows[i]["Wl"][o], []])[1].append(i - a)
            i += 1
        if per and max(len(x[1]) for x in per.values()) >= mp:
            print(f"piece {k}..{j} {kind} c_th {rows[k]['cth']} c_w {rows[k]['cw']} |R minus o| {len(rows[k]['R'])} run {a}..{i} :",
                  {v: (x[0], len(x[1]), x[1]) for v, x in per.items() if len(x[1]) >= mp})
    k = j + 1
