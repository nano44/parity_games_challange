#!/usr/bin/env python3
"""L-SI P-N5-GATE line L-1: every premise quote, checked VERBATIM inside the named landed entry of docs/RESULTS.md (the text from its
«### R<id> » heading to the next «### R» heading, wrapped lines joined by one space). Prints one line per quote and «quotes: K of K
verbatim»; exit 1 on any miss. Usage: quotesL1.py ROOT (as a module: Q only)."""
import re, sys

Q = [
 ("R104-game-gate", "R104", "e of even priority above every β with one edge to the W-target or to the top even self-loop c_W"),
 ("R104-gates", "R104", "Odd gates of priority 1 with a W-face e and a Ξ-face β"),
 ("R117-pads", "R117", "4M + 4 single-successor Even pads of priority ≤ 2"),
 ("R118-idealcyc", "R118", "The game is Γ(G) with every Even vertex that is not a mover frozen at its start successor. Odd is unrestricted (gates and K2)."),
 ("R118-howard", "R118", "every mover x goes to a successor of ⊴-largest Ω_t value, and keeps σ_t(x) if σ_t(x) is such a successor"),
 ("R118-reach3cyc-b", "R118", "T3 is the first state at which no mover has a strictly better successor in Γ3;"),
 ("R118-redxi", "R118", "an N5′-xi run (box 190's S4a tie rule by Ξσ)"),
 ("R121-emon", "R121", "(Lemma E-MON) if Λ_t(v) = Λ_(t+1)(v) then E_t(v) ≤ E_(t+1)(v)"),
 ("R123-bonly", "R123", "at every state t and every vertex v other than c_W and the e-vertices whose successor is c_W, Λ_t(v) is less relevant than every e-vertex"),
 ("R123-notie", "R123", "at every state and gate g, Ω_t(e_g) ≠ Ω_t(β_g)"),
 ("R123-locgate", "R123", "at every state t and gate g, Odd's optimal counterstrategy σ̄_t chooses the face of strictly ⊴-smaller value"),
 ("R123-cn2", "R123", "the cycle node of every play under every positional pair has priority ≥ 2, so no gate or mover is a cycle node or in a set Π"),
]

def section(text, rid):
    m = re.search(r"^### " + rid + r" .*?(?=^### R|\Z)", text, re.S | re.M)
    assert m, rid
    return re.sub(r"\s*\n\s*", " ", m.group(0))

if __name__ == "__main__":
    import os
    text = open(os.path.join(sys.argv[1], "docs/RESULTS.md"), encoding="utf-8").read()
    ok = 0
    for k, rid, s in Q:
        hit = s in section(text, rid)
        ok += hit
        print(("OK   " if hit else "MISS ") + k + " (" + rid + ")")
    print("quotes: %d of %d verbatim" % (ok, len(Q)))
    sys.exit(0 if ok == len(Q) else 1)
