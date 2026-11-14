#!/usr/bin/env python3
"""REFEREE successor 37: blocks of the stage-5b logs (gkx_logs/s37_gloss, s37_r3, s37_xt, s37_e7_*, s37_linedata, s37_line_*.out)
for the report (pasted by gkx_fill.py, placeholders @@S6:NAME@@, not typed). blocks(D) returns {NAME: [lines]}."""
import os, sys, re

def rd(D, name):
    p = os.path.join(D, name)
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as f:
        return [l.rstrip("\n") for l in f if l.strip()]

def kv(l):
    w = l.split()
    return {w[i]: w[i + 1] for i in range(1, len(w) - 1, 2)}

def span(ks):
    ks = sorted(int(k) for k in ks)
    if len(ks) == 1:
        return str(ks[0])
    return f"{ks[0]}..{ks[-1]}" if ks == list(range(ks[0], ks[-1] + 1)) else ",".join(map(str, ks))

def blocks(D):
    B = {}
    for name, f in (("E7QUOTES", "s37_e7_quotes.out"), ("E7PINS", "s37_e7_pins.out"), ("E7FACTS", "s37_e7_facts.out"), ("LINEDATA", "s37_linedata.out"),
                    ("LINE3", "s37_line_L3.out"), ("LINE6", "s37_line_L6.out"), ("E9QUOTES", "s37_e9_quotes.out"), ("E9PINS", "s37_e9_pins.out"),
                    ("E9FACTS", "s37_e9_facts.out"), ("LINECHAIN", "s37_linechain.out"), ("LINEDATA6", "s37_linedata_L6.out"),
                    ("TERMXI", "s37_termxi.out")):
        ls = rd(D, f)
        if ls is not None:
            B[name] = ls
    g = rd(D, "s37_gloss.out")
    if g is not None:
        ks, ok, lform, viol, eq, per = [], 0, 0, 0, 0, {}
        for l in g:
            w = l.split()
            ks.append(w[2])
            ok += int(w[4])
            lform += int(w[w.index("Lform") + 1])
            viol += int(re.search(r"member_viol \(all four\) (\d+)", l).group(1))
            eq += int(re.search(r"runs equal to rule R's (\d+) of 4", l).group(1))
            for name, L in re.findall(r"(\w+_depth_first,bid_\w+) L (\d+)", l):
                per.setdefault(name, set()).add(L)
        B["GLOSS6"] = [f"gloss: k {span(ks)}; rule R's br is the rank of the triple (−depth, local δ, β-id) for {ok} of {len(ks)} k, and its run has L = 2^k − 2 (Lform sum {lform})",
                       "gloss, the line's words as written (br = the rank of (Ξ-depth, β-id), no local δ; a wire at depth 2k + 5 as in the rule), L for every k: " +
                       "; ".join(f"{n.replace('_', ' ').replace(',', ', ').replace('bid up', 'ties by increasing β-id').replace('bid down', 'ties by decreasing β-id')}: L {' or '.join(sorted(v))}" for n, v in per.items()) +
                       f"; member_viol sum {viol} (each variant is in IDEAL-ACYC); runs equal to rule R's: {eq} of {4 * len(ks)}"]
    g2 = rd(D, "s37_gloss2.out")
    if g2 is not None:
        rows = [kv(l) for l in g2]
        B["GLOSS2"] = [f"gloss2 (the corrected wording, every reading its words leave open: ties by increasing or decreasing β-id; the wires last as in the rule, first, "
                       f"in the middle, or at depth 0): k {span(x['k'] for x in rows)}; readings per k {'/'.join(sorted(set(x['readings'] for x in rows)))}; member_viol "
                       f"{sum(int(x['member_viol']) for x in rows)}; runs equal to G_k's {sum(int(x['run_equal_to_G_k']) for x in rows)} of "
                       f"{sum(int(x['readings']) for x in rows)}; Lform {sum(int(x['Lform']) for x in rows)}"]
    r = rd(D, "s37_r3.out")
    if r is not None:
        rows = [kv(l) for l in r]
        r0 = [x for x in rows if x["ctrl"] == "0"]
        t = lambda c: f"{sum(int(x[c]) for x in r0):,}"
        B["R36"] = [f"r3: k {span(x['k'] for x in r0)}; windows {t('windows')} windows2 {t('windows2')} r3in {t('r3in')} r3move {t('r3move')} r3rest {t('r3rest')}; "
                    f"literal {t('literal')} expected {t('expected')} litdiff {t('litdiff')}",
                    "r3 control 1 (the range one step too long, t − 1 ≤ τ ≤ last): " + "; ".join(f"k {x['k']} fires r3in {x['r3in']} (windows2 {x['windows2']})" for x in rows if x["ctrl"] == "1")]
    x = rd(D, "s37_xt.out")
    if x is not None:
        ks, wt, et, yd, yp, kinds = [], 0, 0, 0, [], {}
        for l in x:
            w = l.split()
            ks.append(w[2])
            wt += int(w[w.index("wiretgt") + 1]); et += int(w[w.index("etgt") + 1]); yd += int(w[w.index("ypdiff") + 1])
            yp.append(w[w.index("yptgt") + 1])
            kinds.setdefault(" ".join(w[w.index("kinds") + 1:w.index("wiretgt")]), []).append(w[2])
        B["XT6"] = [f"xt: k {span(ks)}; wiretgt {wt} etgt {et} ypdiff {yd}; yptgt per k {' '.join(yp)} (= the options outside 5.1's list as written); kinds of Ξ-targets: " +
                    "; ".join(f"{kd} (k {span(v)})" for kd, v in kinds.items())]
    return B

if __name__ == "__main__":
    D = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "gkx_logs")
    for name, ls in blocks(D).items():
        print(f"== {name}")
        for l in ls:
            print(l[:400])
