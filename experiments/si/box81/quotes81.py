#!/usr/bin/env python3
"""L-SI box 81, packet P-ACYC §0: every premise quote, checked VERBATIM against the landed text. Sources: docs/RESULTS.md (trunk) and
docs/new/N5-ssi-global.md (the SPEC that RESULTS R15 names as N5's object). Each quote must occur exactly as written (after joining the
source's wrapped lines by one space). Prints one line per quote and «quotes: K of K verbatim»; exit 1 on any miss.
Usage: quotes81.py (run from anywhere)"""
import os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
Q = [
 ("R104-genome", "docs/RESULTS.md", "an IDEAL genome G has N movers x with levels lev(x), M := Σ deg(x) options (x, k), each with a W-target of level lev(x) − 1 (none at level 0), a Ξ-target xt(x, k), a mover or the exit X, a distinct β-rank with a parity, a distinct gate index, and a start"),
 ("R104-xigraph", "docs/RESULTS.md", "the Ξ-graph has an edge x → xt(x, k) for every option with a mover as Ξ-target"),
 ("R104-game", "docs/RESULTS.md", "the game Γ(G) on n = N + 3M + 6 vertices (Even movers of priority 0; Odd gates of priority 1 with a W-face e and a Ξ-face β; β of priority 6 + 2·rank + parity with edges to the Ξ-target and to u, or to u alone; e of even priority above every β with one edge to the W-target or to the top even self-loop c_W; an unused even self-loop of priority 2; c_W's priority top is the least even number at least 2 above every other priority so far; a closed core u = K0 (Even, top + 2) → {K1, K3}, K1 (Even, 5) → {K0, K1}, K2 (Odd, 3) → {K1, K2}, K3 (Even, top + 3) → {K1, K2}"),
 ("R104-start", "docs/RESULTS.md", "with start σ = the genome start at movers, β → its Ξ-target (u when the target is X), K0 → K3, K1 → K1, K3 → K2, τ = e at every gate and K2 → K2"),
 ("R104-realize", "docs/RESULTS.md", "Odd's optimal counterstrategy on the β-face at every gate (strict local preference)"),
 ("R104-acyc", "docs/RESULTS.md", "for every G whose Ξ-graph is ACYCLIC, the game Γ(G)"),
 ("R117-pads", "docs/RESULTS.md", "the game Γ3(G) obtained from Γ(G) by 4M + 4 single-successor Even pads of priority ≤ 2 (pA on K0 → K3, s on K1's loop, q on K1 → K0, r on K2 → K1, pe_g and pβ_g on both faces of every gate g, pb_g on every β_g → u, and m_(x,k) on every mover edge x → (x, k) with priority 2 for the genome start and 0 otherwise, appended after Γ(G)'s vertices; n = N + 7M + 10)"),
 ("R117-reach3", "docs/RESULTS.md", "the N5 run of Γ3(G) FROM S3 has states 0, …, L(G) equal to the transported REALIZE states of the IDEAL run"),
 ("R118-vj", "docs/RESULTS.md", "VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the order ⊴ on values (Λ, Π, k)"),
 ("R118-sbar", "docs/RESULTS.md", "σ̄ is Odd's optimal counterstrategy, chosen by a fixed deterministic rule"),
 ("R118-idealcyc", "docs/RESULTS.md", "The game is Γ(G) with every Even vertex that is not a mover frozen at its start successor. Odd is unrestricted (gates and K2)."),
 ("R118-howard", "docs/RESULTS.md", "every mover x goes to a successor of ⊴-largest Ω_t value, and keeps σ_t(x) if σ_t(x) is such a successor"),
 ("R118-tcyc", "docs/RESULTS.md", "T_CYC := the number of steps to the first state where no mover has a strictly better successor"),
 ("R118-labelC", "docs/RESULTS.md", "C if Λ_t(v) ≠ Λ_(t+1)(v) for some vertex v;"),
 ("R118-labelR", "docs/RESULTS.md", "else R if σ̄_t(v) ≠ σ̄_(t+1)(v) for some Odd vertex v;"),
 ("R118-brseg", "docs/RESULTS.md", "If Λ and σ̄ are constant on the states a, a+1, …, a+j+1 and the step a+j → a+j+1 changes σ, then j ≤ N − 1. Hence every maximal run of consecutive p-steps has at most N steps."),
 ("R118-redxi", "docs/RESULTS.md", "an N5′-xi run (box 190's S4a tie rule by Ξσ)"),
 ("R118-reach3cyc-a", "docs/RESULTS.md", "The N5′-xi run of Γ3(G) from S3 has the following form:"),
 ("R118-reach3cyc-b", "docs/RESULTS.md", "T3 is the first state at which no mover has a strictly better successor in Γ3;"),
 ("R118-reach3cyc-c", "docs/RESULTS.md", "transition T3 + 1 is an S4c fallback."),
 ("R118-reach3cyc-prem", "docs/RESULTS.md", "which RESULTS R117 (P-N5-REACH) signs in its entry (S3-START, PAD, K3, TAU3 for every genome; ESC3, W3 for IDEAL-ACYC) and states in its line only for acyclic Ξ-graphs (S3-START, PAD)"),
 ("R118-T3", "docs/RESULTS.md", "T3 ≤ C + R + (C + R + 1)·N, with C ≤ n3·(2M + 2) and n3 = N + 7M + 10;"),
 ("R118-T3-onG3", "docs/RESULTS.md", "§4 applies on Γ3 (movers priority 0, pads never cycle nodes by PAD (b), non-mover Even vertices frozen in standard states, Odd = gates and K2)"),
 ("R118-firstfb", "docs/RESULTS.md", "the first fallback of N5′-xi on Γ3(G) comes at iteration T3 + 1."),
 ("R118-noR", "docs/RESULTS.md", "no bound on R is claimed (OPEN), so nothing about N5′-xi's or N5's running time follows"),
 ("R15-object", "docs/RESULTS.md", "N5 \"SSI-GLOBAL\" as specified in docs/new/N5-ssi-global.md"),
 ("SPEC-S4", "docs/new/N5-ssi-global.md", "S4 Iteration (one iteration = one pass with Iσ ∪ Iτ ≠ ∅; both steps computed from the SAME (σ, τ), applied together):"),
 ("SPEC-S4c", "docs/new/N5-ssi-global.md", "c. FALLBACK, if σ_new = σ and τ_new = τ: if Iσ ≠ ∅, for every Even v with an improving edge set σ_new(v) = the w with (v, w) ∈ Iσ maximising (Ξσ(w), w) (best valuation, ties: larger index); otherwise do the same for Odd on Iτ with G^d's valuations. Count it."),
]

def flat(p):
    return re.sub(r"\s*\n\s*", " ", open(os.path.join(ROOT, p), encoding="utf-8").read())

if __name__ == "__main__":
    cache = {}; ok = 0
    for qid, p, q in Q:
        if p not in cache: cache[p] = flat(p)
        hit = q in cache[p]; ok += hit
        print(f"{qid} {p} {'VERBATIM' if hit else 'MISSING'}")
    print(f"quotes: {ok} of {len(Q)} verbatim")
    sys.exit(0 if ok == len(Q) else 1)
