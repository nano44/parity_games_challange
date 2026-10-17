#!/usr/bin/env python3
"""Print an SLP as modal formulas: each Cpre gate as s_i = <>(argument), arguments as Boolean formulas over
P2 (= priority 2) and earlier s_j, simplified by truth-table minimisation over the inputs actually used."""
import sys, os, json, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slp import cost, depth


def formula(prog, i, names):
    g = prog[i]
    if g[0] == "P": return f"P{g[1]}"
    if g[0] == "VE": return "VE"
    if g[0] == "EMPTY": return "0"
    if g[0] == "not": return f"~{formula(prog, g[1], names)}"
    if g[0] == "or": return f"({formula(prog, g[1], names)} | {formula(prog, g[2], names)})"
    if g[0] == "and": return f"({formula(prog, g[1], names)} & {formula(prog, g[2], names)})"
    if g[0] == "cpre": return names[i]
    raise ValueError(g)


def truth_table(prog, i, inputs):
    """Evaluate gate i as a Boolean function of the given input gates (dict gate index -> name) over all assignments."""
    keys = list(inputs)
    rows = {}
    for bits in itertools.product((0, 1), repeat=len(keys)):
        val = {}
        for j, g in enumerate(prog[: i + 1]):
            if j in inputs:
                val[j] = bits[keys.index(j)]
            elif g[0] == "P": val[j] = None
            elif g[0] == "EMPTY": val[j] = 0
            elif g[0] == "VE": val[j] = 1
            elif g[0] == "not": val[j] = None if val[g[1]] is None else 1 - val[g[1]]
            elif g[0] == "or":
                a, b = val[g[1]], val[g[2]]
                val[j] = None if (a is None or b is None) and not (a == 1 or b == 1) else (1 if (a == 1 or b == 1) else 0)
            elif g[0] == "and":
                a, b = val[g[1]], val[g[2]]
                val[j] = None if (a is None or b is None) and not (a == 0 or b == 0) else (0 if (a == 0 or b == 0) else 1)
            elif g[0] == "cpre": val[j] = None
        rows[bits] = val[i]
    return keys, rows


def minimise(keys, rows, names):
    """Quine-McCluskey-lite: return a DNF string using only the variables that matter."""
    used = [k for k in keys if any(rows[b] != rows[b[:keys.index(k)] + (1 - b[keys.index(k)],) + b[keys.index(k) + 1:]] for b in rows)]
    sub = {}
    for b, v in rows.items():
        key = tuple(b[keys.index(k)] for k in used)
        sub[key] = v
    ones = [k for k, v in sub.items() if v == 1]
    if len(ones) == len(sub): return "1"
    if not ones: return "0"
    # prime implicants by brute force (few variables)
    terms = []
    m = len(used)
    for r in range(0, m + 1):
        for fixed in itertools.combinations(range(m), r):
            for vals in itertools.product((0, 1), repeat=r):
                cover = [k for k in sub if all(k[f] == v for f, v in zip(fixed, vals))]
                if cover and all(sub[k] == 1 for k in cover):
                    terms.append((fixed, vals, set(cover)))
    # greedy cover
    need = set(ones); chosen = []
    terms.sort(key=lambda t: (len(t[0]), -len(t[2])))
    while need:
        best = max(terms, key=lambda t: len(t[2] & need))
        chosen.append(best); need -= best[2]
    parts = []
    for fixed, vals, _ in chosen:
        lits = [(names[used[f]] if v else "~" + names[used[f]]) for f, v in zip(fixed, vals)]
        parts.append(" & ".join(lits) if lits else "1")
    return " | ".join(parts)


def show(prog):
    names = {}
    cp = [i for i, g in enumerate(prog) if g[0] == "cpre"]
    for k, i in enumerate(cp):
        names[i] = f"s{k + 1}"
    p2 = next(i for i, g in enumerate(prog) if g == ("P", 2))
    inputs = {p2: "P2"}
    lines = []
    for k, i in enumerate(cp):
        arg = prog[i][1]
        keys, rows = truth_table(prog, arg, dict(inputs))
        lines.append(f"s{k + 1} = <>( {minimise(keys, rows, inputs)} )")
        inputs[i] = names[i]
    keys, rows = truth_table(prog, len(prog) - 1, dict(inputs))
    lines.append(f"out = {minimise(keys, rows, inputs)}")
    return "\n".join(lines)


if __name__ == "__main__":
    for f in sys.argv[1:]:
        d = json.load(open(f)); d["program"] = [tuple(g) for g in d["program"]]
        print(f"{f}: n={d['n']} min={d.get('B1', d.get('cost'))} cost={cost(d['program'])} depth={depth(d['program'])}")
        print(show(d["program"]))
