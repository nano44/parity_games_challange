#!/usr/bin/env python3
"""L-SI box 104: the DATA tables of docs/si/box104-map.md §5.2 and the numbers quoted in its §0, §3-§6, computed from out/*.out (no
engine, no number typed by hand). Usage: summ104.py   (prints KEY<TAB>VALUE lines; TABLE and LTABLE are multi-line values)"""
import re, math, os
HERE = os.path.dirname(os.path.abspath(__file__))
def O(f):
    p = os.path.join(HERE, "out", f); return open(p).read().splitlines() if os.path.exists(p) else []
def runs(f):
    d = {}
    for l in O(f):
        m = re.match(r"F104 n (\d+) mode \w+ alg \w+: \|G_n\| (\d+) Howard T (\d+) \| N (\d+) M (\d+) \|V\| (\d+) m (\d+) maxprio (\d+) \| iterations (\d+) fallbacks (\d+)", l)
        if m: d[int(m[1])] = dict(G=int(m[2]), T=int(m[3]), V=int(m[6]), it=int(m[9]), fb=int(m[10]))
    return d
def wruns(files, tag):
    d = {}
    for f in files:
        for l in O(f):
            m = re.match(r"WRAP104 alg \w+ " + tag + r" n (\d+): \|H\| (\d+) m (\d+) .*Howard T \([a-z. ]+\) (\d+)(?: tie events (\d+))? \| \|W\| (\d+) \| [TF] (-?\d+) iterations (\d+) \| iterations - Howard T = (-?\d+) \| (?:2\^n = \d+ \| )?(.*)$", l)
            if m: d[int(m[1])] = dict(G=int(m[2]), m=int(m[3]), T=int(m[4]), ties=m[5], V=int(m[6]), it=int(m[8]), zero=all(x == "0" for x in m[10].split()[1::2]))
    return d
def xck(files, tag):
    d = {}
    for f in files:
        for l in O(f):
            m = re.match(tag + r" n (\d+): .*impl2 iterations (\d+) fallbacks (\d+); .*; (AGREE\+CORRECT|MISMATCH)$", l)
            if m: d[int(m[1])] = (int(m[2]), m[4])
    return d
W = ["wrap_fried_xi.out", "wrap_long.out"]; L = ["wrap_lmcs_xi.out", "wrap_long.out"]
fx, ed, sp = runs("free_xi.out"), runs("edom_xi.out"), runs("free_spec.out")
wx, ws = wruns(W, "switchallexp"), wruns(["wrap_fried_spec.out"], "switchallexp")
lx, lt, ls = wruns(L, "lmcs fig4"), wruns(L, "lmcs table4"), wruns(["wrap_lmcs_spec.out"], "lmcs fig4")
x2f, x2w, x2l = xck(["xck.out"], "XCK104"), xck(["wrap_xck.out", "wrap_long.out"], "WXCK104 switchallexp"), xck(["wrap_xck.out", "wrap_long.out"], "WXCK104 lmcs fig4")
tr = {int(m[1]): (int(m[2]), int(m[3])) for m in (re.match(r"XTRAJ104 n (\d+): .*; pairs (\d+); mism (\d+)$", l) for l in O("xtraj.out")) if m}
nr = "not run"; rows = []
for n in sorted(set(fx) | set(wx)):
    T = (fx.get(n) or wx[n])["T"]; G = (fx.get(n) or wx[n])["G"]
    w = (f"{wx[n]['V']:,} | {wx[n]['it']:,}, 1" + ("" if wx[n]["zero"] else " (A COUNTER IS NOT 0)")) if n in wx else f"{251 * n + 65:,} | {nr}"
    f = f"{fx[n]['V']:,} | {fx[n]['it']:,}, {fx[n]['fb']}" if n in fx else f"- | {nr}"
    e2 = f"{(str(x2w[n][0]) + ', ' + x2w[n][1]) if n in x2w else nr} / {(str(x2f[n][0]) + ', ' + x2f[n][1]) if n in x2f else nr}"
    rows.append(f"| {n} | {G} | {T:,} | {w} | {f} | {e2} | {('%d of %s' % (tr[n][1], format(tr[n][0], ','))) if n in tr else nr} | {ed[n]['it'] if n in ed else nr} | "
                f"{ws[n]['it'] if n in ws else nr} / {sp[n]['it'] if n in sp else nr} |")
lrows = []
for n in sorted(lx):
    r = lx[n]; t4 = lt.get(n)
    lrows.append(f"| {n} | {r['G']}, {r['m']} | {r['T']:,} ({r['ties']}) | {2 ** n} | {r['V']:,} | {r['it']:,}, 1" + ("" if r["zero"] else " (A COUNTER IS NOT 0)")
                 + f" | {(str(t4['it']) + ', 1' + ('' if t4['zero'] else ' (A COUNTER IS NOT 0)')) if t4 else nr} | {(str(x2l[n][0]) + ', ' + x2l[n][1]) if n in x2l else nr} | {ls[n]['it'] if n in ls else nr} |")
ns = sorted(fx); nw = sorted(wx); nl = sorted(lx)
sl = lambda d, k: ", ".join(f"{math.log(d[b]['it'] / d[a]['it']) / math.log(d[b]['V'] / d[a]['V']):.2f}" for a, b in zip(k, k[1:]))
out = {"TABLE": "\n".join(rows), "LTABLE": "\n".join(lrows),
       "SLOPESF": sl(fx, ns), "SLOPESL": sl(lx, nl),
       "ITSF": ", ".join(f"{fx[n]['it']:,}" for n in ns), "TSF": ", ".join(f"{fx[n]['T']:,}" for n in ns),
       "ITSW": ", ".join(f"{wx[n]['it']:,}" for n in nw), "NW": f"{nw[0]}..{nw[-1]}",
       "ITSL": ", ".join(f"{lx[n]['it']:,}" for n in nl), "TSL": ", ".join(f"{lx[n]['T']:,}" for n in nl), "NL": f"{nl[0]}..{nl[-1]}",
       "TL_FORMULA": str(all(lx[n]["T"] == 9 * 2 ** n - 10 for n in nl)), "T4SAME": str(all(n in lt and lt[n]["it"] == lx[n]["it"] for n in nl)),
       "WSAMEF": str(all(fx[n]["it"] == wx[n]["it"] for n in nw)),
       "CROSSL": ", ".join(f"n {n}: {lx[n]['it']} vs {lx[n]['V']}" for n in nl), "CROSSF": ", ".join(f"n {n}: {fx[n]['it']} vs {fx[n]['V']}" for n in ns),
       "PAIRS": f"{sum(v[0] for v in tr.values()):,}", "MISM": str(sum(v[1] for v in tr.values())),
       "EDOM": ", ".join(str(ed[n]['it']) for n in sorted(ed)), "SPECF": ", ".join(str(sp[n]['it']) for n in sorted(sp)),
       "SPECW": ", ".join(str(ws[n]['it']) for n in sorted(ws)), "SPECL": ", ".join(str(ls[n]['it']) for n in sorted(ls)),
       "ODDB": ", ".join(re.search(r"odd betas above some e (\d+)", l)[1] for l in O("prio.out") if "mode free" in l),
       "SHAS": "; ".join(l.split()[1] + " " + l.split()[0][:8] for l in open(os.path.join(HERE, "inst", "SHA1SUMS"))),
       "QUOTES": (O("quotes104.out") or ["-"])[-1]}
for k, f in (("FR", "freereach.out"), ("FC", "freereach_ctrl.out"), ("WR", "wrap_rand.out"), ("WC", "wrap_ctrl.out"), ("XC", "xtraj_ctrl.out"), ("WJ", "wrap_json.out")):
    for i, l in enumerate(O(f)): out[f"{k}{i + 1}"] = l
for k, v in out.items(): print(f"{k}\t{v}")
