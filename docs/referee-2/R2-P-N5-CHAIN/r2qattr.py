#!/usr/bin/env python3
"""Which RESULTS entry (### R<id>) holds each premise quote of P-N5-CHAIN §1 / L-1. Own code. Usage: r2qattr.py TRUNK"""
import re, subprocess, sys
R = subprocess.run(["git", "show", f"{sys.argv[1]}:docs/RESULTS.md"], capture_output=True, text=True, check=True).stdout
ents = re.split(r"\n(?=### R\d+ )", R)
def norm(s): return re.sub(r"\s+", " ", s)
Q = {"R118 (k) R117-SIGN": "RESULTS R117's entry signs S3-START, PAD, K3 and TAU3 for every genome and ESC3, W3 for acyclic Ξ-graphs",
     "R118 K2r": "with σ̄(K2) = r proved for every genome in P-N5-XICYC's fixes",
     "R118 (k) R3C": "visits only standard states and makes Howard steps at the movers until its first fallback",
     "R118 (k) cond": "Theorem REACH3-CYC, CONDITIONAL on P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3 for every genome",
     "R15 (a)": "Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}.",
     "R21 (a)": "(Odd's best reply σ̄_k is pointwise optimal in G_{σ_k})",
     "R104 1E-N3": "used in two forms: S1's σ̄, and τ̄ on the dual game, are pointwise optima; and S4a's σ_new",
     "R104 DEF": "Even movers of priority 0; Odd gates of priority 1 with a W-face e and a Ξ-face β",
     "R117 G3": "obtained from Γ(G) by 4M + 4 single-successor Even pads of priority ≤ 2",
     "R117 S3-START": "S3's start pair on Γ3(G) is the standard state of Γ3 for the genome start s_0."}
for k, q in Q.items():
    hits = [e.split(" ", 2)[1] for e in ents if q in norm(e)]
    print(f"{k}\t{hits}")
