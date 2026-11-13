#!/usr/bin/env python3
"""L-SI box 104: every «…» of docs/si/box104-map.md that is marked [Q] is one of the strings below, checked here as an exact substring
of its source at a pinned commit (git show SHA:PATH).
Usage: quotes104.py src            (needs the pinned commits in the local repository; writes one line per quote: OK / FAIL)
       quotes104.py doc DOC.md     (no git: every string below must occur in DOC.md, verbatim up to line wrapping; one summary line)"""
import sys, subprocess, os
TRUNK = "a9699c30c5cfce333b8c4b160321e42652d52560"   # claude/vibrant-johnson-nxvvxo
LNEW = "8db300fe3"                                    # claude/l-new (box 208)
LNEW9 = "3f8960998"                                   # claude/l-new (box 209)
LRED = "06e7ececd"                                    # claude/l-red
LLIT = "4a0db9d17"                                    # claude/l-lit
Q = [
 ("T-2", TRUNK, "TARGET.md", "There is a deterministic algorithm A and a polynomial p such that for every parity game G, A on input G halts within"),
 ("T-4a", TRUNK, "TARGET.md", "Polynomial only on a restricted class (bounded d, treewidth, Strahler/register number, ...)."),
 ("T-4d", TRUNK, "TARGET.md", "Correctness or running time resting on an unproved conjecture, an empirical observation, or a \"clearly\"."),
 ("T-5.4", TRUNK, "TARGET.md", "its correctness formalized in Lean against TARGET.md (no sorry, allowed axioms only)."),
 ("G-11", TRUNK, "docs/GAPS.md", "N5 SSI-GLOBAL makes polynomially many iterations (gauntlet step 4, running time)"),
 ("R15-d", TRUNK, "docs/RESULTS.md", "N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d), and"),
 ("R15-lim", TRUNK, "docs/RESULTS.md", "h(≺) can be exponential; NO polynomial or other useful iteration bound follows"),
 ("R47-a", TRUNK, "docs/RESULTS.md", "along a run at most n(n − 1) transitions change λ and at most n(n − 1) change λ^U, so a run has at most 2n(n − 1) + 1 joint"),
 ("R57-b", TRUNK, "docs/RESULTS.md", "Iτ = ∅ is not used; determinacy is derived, not assumed (W_E ∩ W_O = ∅ is proved)."),
 ("R57-c", TRUNK, "docs/RESULTS.md", "iteration and the final output step cost O(n³(n + m)) word operations on O(log(n + m))-bit words and O(n)-bit vectors on every"),
 ("R90", TRUNK, "docs/RESULTS.md", "so T is polynomial if and only if B*, REP*, SC* and O* are"),
 ("R104-def", TRUNK, "docs/RESULTS.md", "e of even priority above every β with one edge to the W-target or to the top even self-loop c_W"),
 ("R104-lim", TRUNK, "docs/RESULTS.md", "a REDUCTION / NECESSITY statement only (no count is bounded; Ξ-cyclic genomes are not covered; nothing about N5's default start S3; the converse is not claimed"),
 ("R117-ri", TRUNK, "docs/RESULTS.md", "if every FL run of N5 from S3 on every n-vertex game has length at most p(n) for a nondecreasing polynomial p (in particular if N5 from S3 makes at most p(n) iterations), then L(G) ≤ p(N + 7M + 10) for every acyclic G"),
 ("R117-lim", TRUNK, "docs/RESULTS.md", "a REDUCTION / NECESSITY statement only (no count is bounded; nothing is claimed about whether long IDEAL-ACYC runs exist; Ξ-cyclic genomes are not covered; the converse is not claimed"),
 ("R118-l", TRUNK, "docs/RESULTS.md", "«N5′-xi's FL run on Γ3(G) is polynomial in N + M for every genome» ⇔ «R is polynomial along these Howard runs»"),
 ("R118-R", TRUNK, "docs/RESULTS.md", "no bound on R is claimed (OPEN), so nothing about N5′-xi's or N5's running time follows"),
 ("R118-x1", TRUNK, "docs/RESULTS.md", "so RED-XI says nothing about general games without TIE-FULL"),
 ("R118-sae", TRUNK, "docs/RESULTS.md", "on Friedmann's switchallexp for N = 2, …, 7 (pgsolver_port.py switchallexp N, Howard from si.py's best-reward start): C = 0; R = 4, 10, 24, 54, 116, 241; T = 30, 70, 150, 310, 630, 1243"),
 ("R121-edom", TRUNK, "docs/RESULTS.md", "Every vertex more relevant than some e-vertex is an e-vertex, c_W, K0 or K3, by [DEF]"),
 ("R124-eg", TRUNK, "docs/RESULTS.md", "N5′-xi, and N5, from S3 on Γ3(G) have exactly one fallback, at an iteration F ≥ 1, and exactly F + 2 iterations"),
 ("R124-el", TRUNK, "docs/RESULTS.md", "N5 (SPEC S1-S5 with its FIX 1-4 tie-breaks) from S3 on Γ3(G) makes exactly L(G) + 3 iterations"),
 ("R124-t3", TRUNK, "docs/RESULTS.md", "if REACH3-CYC holds for G, N5′-xi from S3 on Γ3(G) makes exactly T3 + 3 iterations"),
 ("R124-lim", TRUNK, "docs/RESULTS.md", "it bounds none of F, T3, L(G) (OPEN), and nothing outside Γ3(G)"),
 ("R125-ra", TRUNK, "docs/RESULTS.md", "N5′-xi from S3 on Γ3(G) visits only standard states and its mover parts form a run of HOW3(G) until its first fallback, at iteration T3 + 1"),
 ("R125-cond", TRUNK, "docs/RESULTS.md", "holds without its condition, the premises ESC3 and W3 being proved here for every genome"),
 ("R125-lim", TRUNK, "docs/RESULTS.md", "says nothing about N5 (whose pre-fallback run on Ξ-cyclic genomes is not a Howard run), about genomes with U(G) unbounded (Σ_v D^tot_E(v) stays OPEN), about other games or about general parity games"),
 ("R125-rt", TRUNK, "docs/RESULTS.md", "T3 is not the IDEAL-CYC count on Γ(G)"),
 ("R113-tb", TRUNK, "docs/RESULTS.md", "(T-BOUND) on 𝓛^R_d, F(l) ≤ 2^(l+2) − 2 and T ≤ 2d + 2(F(0) + … + F(d − 2)) ≤ 2^(d+2) − 2d − 4"),
 ("L50-3", TRUNK, "docs/DECISIONS.md", "A family doing so on linearly many levels would, by RESULTS R104 Corollary REAL-IDEAL, make FL-POLY false."),
 ("NOW-M4", TRUNK, "docs/NOW.md", "candidate N5 SSI-GLOBAL; gauntlet step 4 (running time, G-N5-TIME) OPEN; termination proved (R15)"),
 ("NOW-tower", TRUNK, "docs/NOW.md", "SEVEN capped levels: HIT7 F(6) = 254 at d 28 (L-COMP 11, sha1 6a3b274d, DATA, CANDIDATE tower; S(5,6,7) ≤ 20,24,28)"),
 ("NOW-fblin", TRUNK, "docs/NOW.md", "FB-LIN (f ≤ n per phase; 5 L-RED boxes, no kill, data 0.79n) OPEN"),
 ("R122-acyc", TRUNK, "docs/RESULTS.md", "the Howard run of IDEAL-CYC(G) from any mover state has C = 0, R = 0 and T_CYC ≤ N"),
 ("CH-R", LNEW, "docs/new/P-N5-CHAIN.md", "(R) Rank order, by Ω first: pads, movers, gates, c_X (Ω ≤ 2) < K2 (3) < K1 (5) < every β (≥ 6) < every e < c_W (top) < K0 (top + 2)"),
 ("CH-W3", LNEW, "docs/new/P-N5-CHAIN.md", "all less relevant than c_W ((R)): P = ∅."),
 ("CH-N5", LNEW, "docs/new/P-N5-CHAIN.md", "For SPEC's S4a the same induction gives standard states, but SPEC picks in TIE(x) = A(x) by its root-first key, not by Ξσ:"),
 ("RE-PAD", LNEW, "docs/new/P-N5-REACH.md", "with Ω(e_g), Ω(β_g) ≥ 6"),
 ("RE-TAU", LNEW, "docs/new/P-N5-REACH.md", "node K0 (Ω top + 2, above c_W); τ̄ maximises (Fact DUAL)"),
 ("RE-RANK", LNEW, "docs/new/P-N5-REACH.md", "Rank facts (from [DEF] and §3): pads, movers, gates, c_X < K2 (Ω 3) < K1 (Ω 5) < every β < every e < c_W < K0 < K3."),
 ("EN-R", LNEW, "docs/new/P-N5-END.md", "K0 is the most relevant EVEN vertex, so a value with"),
 ("EN-W", LNEW, "docs/new/P-N5-END.md", "It meets no β and no core vertex, and no vertex above c_W: its value is (c_W, ∅, 5ℓ + 3)."),
 ("B208-scope", LNEW, "docs/new/N5-LEVEL-box208.md", "IDEAL-CYC on Γ(G) only; not Γ3, not N5′-xi, not M4; G-N5-TIME stays OPEN."),
 ("B208-all", LNEW, "docs/new/N5-LEVEL-box208.md", "For every genome G: T_CYC ≤ P·(N + 2M + 6) + N, P = 2M(N + 2M)."),
 ("B208-sae", LNEW, "docs/new/N5-LEVEL-box208.md", "those games are not genome games Γ(G), and ALL-TCYC says nothing about them"),
 ("B209-t3", LNEW9, "docs/new/N5-LEVEL3-box209.md", "For every genome G: T3 ≤ P3·(n_E3 + 1) + n_E3, with P3 = 2M(N + 4M) and n_E3 = N + 6M + 9."),
 ("B209-n5", LNEW9, "docs/new/N5-LEVEL3-box209.md", "For every genome G, N5′-xi from S3 on Γ3(G) makes exactly T3 + 3 ≤ P3·(n_E3 + 1) + n_E3 + 3 iterations."),
 ("B209-scope", LNEW9, "docs/new/N5-LEVEL3-box209.md", "Not N5, not another start, not another game, not M4; G-N5-TIME stays OPEN."),
 ("B209-edom", LNEW9, "docs/new/N5-LEVEL3-box209.md", "the added vertices are pads of priority ≤ 2 (R117's line above), below every e-vertex. Call this (E-DOM3)."),
 ("B190-def", LNEW, "docs/new/N5XI-GAUNTLET-box190.md", "with ONE rule changed, inserted after S4a:"),
 ("B190-opt", LNEW, "docs/new/N5XI-GAUNTLET-box190.md", "Not claimed: that σ_new is still a pointwise optimum of H. No argument above needs it."),
 ("R217-6", LRED, "docs/red/R217-ovt.md", "Steps 1-6 coincide exactly with the original run at every mover. So the compilation is faithful until step 7."),
 ("R217-only", LRED, "docs/red/R217-ovt.md", "can reach N5′-xi only through the Howard-equivalence on Γ3 genomes (REACH3-CYC), and E-DOM blocks the direct port there."),
 ("R217-edom", LRED, "docs/red/R217-ovt.md", "Obstruction E-DOM (structural fact of R104's Γ(G); P-N5-XICYC [DEF], gamma3.build)."),
 ("R217-thm8", LRED, "docs/red/R217-ovt.md", "13·2^n − 9 iterations on G_n using the locally optimizing improvement policy."),
 ("T67-deep", LLIT, "docs/lit/T67-n5-route-summary.md", "DEEP is the only chain link that fails on Friedmann's games."),
]
if __name__ == "__main__":
    if sys.argv[1] == "src":
        top = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip(); cache = {}; bad = 0
        for (qid, sha, path, s) in Q:
            if (sha, path) not in cache:
                cache[(sha, path)] = subprocess.run(["git", "-C", top, "show", f"{sha}:{path}"], capture_output=True, text=True, check=True).stdout
            txt = cache[(sha, path)]; ok = s in txt; bad += not ok
            line = txt[:txt.index(s)].count("\n") + 1 if ok else 0
            print(f"QUOTE104 {qid}: {'OK' if ok else 'FAIL'} {sha[:9]}:{path} l. {line} ({len(s)} chars)")
        print(f"QUOTES104 total {len(Q)} fail {bad}"); sys.exit(1 if bad else 0)
    else:
        norm = lambda t: " ".join(t.split())   # a quote may be wrapped over lines in the doc; nothing else may differ
        doc = norm(open(sys.argv[2], encoding="utf-8").read()); miss = [qid for (qid, _, _, s) in Q if norm(s) not in doc]
        print(f"QUOTES104 doc {os.path.basename(sys.argv[2])}: {len(Q) - len(miss)} of {len(Q)} quoted strings present" + (f"; MISSING {miss}" if miss else "")); sys.exit(1 if miss else 0)
