"""REFEREE successor 27: every «…» quote in the P-TOWER-FUEL packet and L-1, searched verbatim (fragments split at ' … ')
in trunk docs/RESULTS.md, restricted to the line of the cited result where one is named. Usage: tf_quotes.py RESULTS.md FILE..."""
import sys, re
R = open(sys.argv[1], encoding="utf-8").read().split("\n")
heads = {m.group(1): i for i, l in enumerate(R) for m in [re.match(r"### (R\d+) ", l)] if m}
for f in sys.argv[2:]:
    T = open(f, encoding="utf-8").read()
    for q in re.findall(r"«(.*?)»", T, re.S):
        q1 = re.sub(r"\s*\n\s*", " ", q)
        frags = [p.strip() for p in re.split(r"…", q1) if p.strip()]
        hits = [h for h, i in heads.items() if all(fr in R[i] for fr in frags)]
        anywhere = all(fr in "\n".join(R) for fr in frags)
        print(f.split("/")[-1], "| frags", len(frags), "| in result lines:", hits or "NONE", "| anywhere:", anywhere, "|", q1[:90])
