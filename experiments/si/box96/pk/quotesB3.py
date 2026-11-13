#!/usr/bin/env python3
"""L-SI packet P-N5-BONLY3 (draft): every premise quote, checked VERBATIM in its source and inside the packet text. Sources: the named
landed entry of docs/RESULTS.md (from its «### R<id> » heading to the next «### R»), or P-N5-CHAIN at claude/l-new 93531b03 (git show;
NOT RUN if that commit is absent). Wrapped lines joined by one space. Prints one line per quote and «quotes: K of K verbatim»; exit 1 on any
miss. Usage: quotesB3.py ROOT"""
import os, re, subprocess, sys
Q = [
 ("R104", "Even movers of priority 0; Odd gates of priority 1 with a W-face e and a Ξ-face β; β of priority 6 + 2·rank + parity with edges to the Ξ-target and to u, or to u alone; e of even priority above every β with one edge to the W-target or to the top even self-loop c_W"),
 ("R104", "a closed core u = K0 (Even, top + 2) → {K1, K3}, K1 (Even, 5) → {K0, K1}, K2 (Odd, 3) → {K1, K2}, K3 (Even, top + 3) → {K1, K2}"),
 ("R104", "with start σ = the genome start at movers, β → its Ξ-target (u when the target is X), K0 → K3, K1 → K1, K3 → K2, τ = e at every gate and K2 → K2"),
 ("R117", "pA on K0 → K3, s on K1's loop, q on K1 → K0, r on K2 → K1, pe_g and pβ_g on both faces of every gate g, pb_g on every β_g → u, and m_(x,k) on every mover edge x → (x, k)"),
 ("R118", "VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the order ⊴ on values (Λ, Π, k)"),
 ("R118", "Theorem REACH3-CYC, CONDITIONAL on P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3 for every genome"),
 ("R118", "visits only standard states and makes Howard steps at the movers until its first fallback"),
 ("R122", "every Even strategy that agrees with the stated start off the movers (transported through the pads on Γ3)"),
 ("R122", "an optimal counterstrategy being pointwise optimal (at every vertex its play value is ⊴ the value under every Odd strategy; RESULTS R57 (b), [1E-N3], as landed in R104)"),
 ("R123", "[OPT] (σ̄_t is optimal at every vertex at once against σ_t) = RESULTS R118's σ̄, Odd's optimal counterstrategy for the order ⊴, as used in R118 (b)"),
 ("R123", "at every state t and every vertex v other than c_W and the e-vertices whose successor is c_W, Λ_t(v) is less relevant than every e-vertex"),
 ("CHAIN", "For every genome G, the N5′-xi run from S3 on Γ3(G) visits only standard states and its mover parts form a run of HOW3(G) (tie rule: Ξσ-best, then SPEC's choice, then the larger index) until its first fallback, at iteration T3 + 1."),
]
J = lambda s: re.sub(r"\s*\n\s*", " ", s)
def sec(t, rid):
    m = re.search(r"^### " + rid + r" .*?(?=^### R|\Z)", t, re.S | re.M); assert m, rid
    return J(m.group(0))
if __name__ == "__main__":
    R = sys.argv[1]
    t = open(os.path.join(R, "docs/RESULTS.md"), encoding="utf-8").read()
    pk = J(open(os.path.join(R, "docs/si/P-N5-BONLY3.md"), encoding="utf-8").read())
    try:
        ch = J(subprocess.run(["git", "-C", R, "show", "93531b03:docs/new/P-N5-CHAIN.md"], capture_output=True, text=True, check=True).stdout)
    except Exception:
        ch = None
    ok = n = 0
    for rid, s in Q:
        if rid == "CHAIN" and ch is None:
            print("NOT RUN CHAIN (commit 93531b03 absent)"); continue
        n += 1
        src = ch if rid == "CHAIN" else sec(t, rid)
        hit = s in src and ("«" + s + "»") in pk
        ok += hit; print(("OK   " if hit else "MISS ") + rid + ": " + s[:60])
    print("quotes: %d of %d verbatim" % (ok, n)); sys.exit(0 if ok == n else 1)
