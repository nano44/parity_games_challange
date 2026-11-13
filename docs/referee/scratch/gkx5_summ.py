#!/usr/bin/env python3
"""REFEREE successor 37: blocks of the stage-5a logs gkx_logs/s37_*.out for the report (pasted by gkx_fill.py, not typed).
blocks(D) returns {NAME: [lines]}; run as a script it prints every block."""
import os, sys

def kv(line):
    w = line.split()
    return {w[i]: w[i + 1] for i in range(1, len(w) - 1, 2)}

def rd(D, name):
    with open(os.path.join(D, name), encoding="utf-8") as f:
        return [l.rstrip("\n") for l in f if l.strip()]

def span(ks):
    ks = sorted(int(k) for k in ks)
    return f"{ks[0]}..{ks[-1]}" if ks == list(range(ks[0], ks[-1] + 1)) else ",".join(map(str, ks))

def tot(rows, c):
    return f"{sum(int(r[c]) for r in rows):,}"

def blocks(D):
    B = {}
    q = rd(D, "s37_quotes.out")
    B["OBJ5"] = [l for l in q if not l.startswith(("quotes", "NOTFOUND", "REF2 source", "untagged"))]
    B["QUOTES5"] = [l for l in q if l.startswith(("quotes", "NOTFOUND", "REF2 source", "untagged"))]
    B["PINS5"] = rd(D, "s37_pins.out")
    B["FACTS5"] = rd(D, "s37_facts.out")
    B["PG13"] = ["pg13: " + l for l in rd(D, "s37_pg13.out")]
    B["RERUN5"] = rd(D, "s37_rerun.out")
    B["LANECMP5"] = rd(D, "s37_lanecmp.out")
    rows = [kv(l) for l in rd(D, "s37_all.out")]
    r0 = [r for r in rows if r["ctrl"] == "0"]
    r2 = [r for r in rows if r["ctrl"] == "2"]
    rf = [r for r in rows if r["ctrl"] == "frozen"]
    out = [f"all (LEMMA′ at every triple and every T): k {span(r['k'] for r in r0)}; triples {tot(r0, 'triples')}; (H1) holds at {tot(r0, 'h1')}; "
           f"h1only {tot(r0, 'h1only')}; windows {tot(r0, 'windows')} expected {tot(r0, 'expected')} notrec {tot(r0, 'notrec')}; full {tot(r0, 'full')}; "
           f"(window, T) pairs {tot(r0, 'pairs')}; viol {tot(r0, 'viol')}"]
    out.append("all control 2 (the list with F / B exchanged): " + "; ".join(f"k {r['k']} fires viol {r['viol']}" for r in r2))
    out.append(f"all, the lemma AS FROZEN (packet l. 192-204): k {span(r['k'] for r in rf)}; frozen hypothesis holds at {tot(rf, 'frozen_hyp_holds')} triples; "
               f"frozen conclusion fails at {tot(rf, 'frozen_conclusion_fails')}, per k " + " ".join(r["frozen_conclusion_fails"] for r in rf) +
               f"; (1, 1, 2^k − 1) among the failures for {sum(int(r['at_1_1_2k-1']) for r in rf)} of {len(rf)} k; the failures are exactly "
               f"(1, 1, 2^k − 1) and (j, 0, 2^k − 1), 2 ≤ j ≤ k − 1, for {sum(int(r['failset_is_expected']) for r in rf)} of {len(rf)} k; "
               f"holds − fails = the recursion's windows for {sum(int(int(r['holds_minus_fails']) == int(r['recursion_windows'])) for r in rf)} of {len(rf)} k")
    B["ALL5"] = out
    lines = rd(D, "s37_exh.out")
    rows = [kv(l) for l in lines]
    out = [l for l, r in zip(lines, rows) if r["ctrl"] == "0"]
    base = [r for r in rows if r["ctrl"] == "0" and r["k"] == "4"][0]
    for r in rows:
        if r["ctrl"] != "0":
            diff = [f"{c} {v}" for c, v in r.items() if c not in ("ctrl", "k") and base.get(c) != v]
            out.append(f"exh control {r['ctrl']} on k {r['k']}: fires " + ", ".join(diff))
    B["EXH5"] = out
    rows = [kv(l) for l in rd(D, "s37_arb.out")]
    r0 = [r for r in rows if r["ctrl"] == "0"]
    cols = ("states", "opt", "stop", "clos", "c0e0", "v0plus", "stcases", "stviol", "sthence", "stcons_cases", "stcons", "onestate_cases",
            "onestate_moves", "h1only", "windows", "full", "proper", "steps", "pviol")
    out = [f"arb: k {span(set(r['k'] for r in r0))}, seeds {', '.join(sorted(set(r['seed'] for r in r0)))}; " + " ".join(f"{c} {tot(r0, c)}" for c in cols)]
    base = [r for r in r0 if r["k"] == "6" and r["seed"] == "1"][0]
    for r in rows:
        if r["ctrl"] != "0":
            diff = [f"{c} {v}" for c, v in r.items() if c not in ("ctrl", "k") and base.get(c) != v]
            out.append(f"arb control {r['ctrl']} on k {r['k']} (proper {r['proper']}): fires " + ", ".join(diff))
    B["ARB5"] = out
    return B

if __name__ == "__main__":
    D = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "gkx_logs")
    for name, ls in blocks(D).items():
        print(f"== {name}")
        for l in ls:
            print(l)
