#!/usr/bin/env python3
# P-N5-END line L-1 generator (L-NEW successor 64). Run from the repo root: python3 experiments/new/box195/mkl1_195.py RESULTS_COPY
# RESULTS_COPY = git show c8f42538f:docs/RESULTS.md (trunk at writing). Asserts: verbatim RESULTS quotes, packet sha1, the W-1 sentence of
# fixes entry 1 verbatim, no «|», one line.
import sys, hashlib
pk = open("docs/new/P-N5-END.md", encoding="utf-8").read()
assert hashlib.sha1(pk.encode()).hexdigest() == "5cae845b1da1a1c40b52e73da6edae3d6aadbf29", "packet changed"
res = open(sys.argv[1], encoding="utf-8").read()
fx = " ".join(open("docs/new/P-N5-END-fixes.md", encoding="utf-8").read().split())
W1 = "Hypotheses of every row: under the standing SPEC premise 1E-N3 (RESULTS R57 (b)), as in RESULTS R104 / R117."
assert fx.count("«" + W1 + "»") == 1, "W-1 sentence not verbatim in fixes entry 1"
assert "under the standing SPEC premise 1E-N3" in res
Q = {
 "1E": "used in two forms: S1's σ̄, and τ̄ on the dual game, are pointwise optima; and S4a's σ_new",
 "R15": "every non-empty switch of improvements goes strictly up in ≺",
 "ACYC": "Ξ-graph is ACYCLIC (self-loops count as cycles).",
 "TAU3": "RESULTS R117's entry signs S3-START, PAD, K3 and TAU3 for every",
 "R3C": "visits only standard states and makes Howard steps at the movers until its first fallback, at iteration T3 + 1",
 "R3CC": "CONDITIONAL on P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3 for every genome",
 "R117F": "FROM S3 has states 0, …, L equal to the standard states of Γ3 for s_0, …, s_L",
}
for k, q in Q.items(): assert q in res, k
pkflat = " ".join(pk.split())
for k, q in Q.items():
    if k in ("1E", "R15", "R3C", "R3CC"): assert q in pkflat or k in ("R3CC",), ("packet", k)
SCOPE = ("this gives the exact END of two runs on one family of games and, for IDEAL-ACYC genomes, an identity between N5's count and L(G); "
 "it bounds none of F, T3, L(G), and nothing outside Γ3(G)")
L = ("On Γ3(G) of RESULTS R117 (Γ(G) of R104 with 4M + 4 single-successor Even pads of priority ≤ 2, n = N + 7M + 10), for N5 (SPEC S1-S5) and N5′-xi (RESULTS R118's [N5XI], SPEC with box 190's S4a tie rule) from SPEC's default start S3, iterations counted as in SPEC S4, "
"for every genome G: (Lemma E0) τ never changes and Iτ = ∅ at every state; "
"(Lemma E1) at every state with the core K-config κ0 = (σ(K0), σ(K1), σ(K3)) = (pA, s, K2) the only improving core edge is (K0, K1) and every S4a step keeps κ0, so the K-config changes only at a fallback and the run cannot stop before one; "
"(Lemma E2) the first fallback, at iteration F ≥ 1, is an Even fallback with result K-config κ1 = (K1, s, K2); "
"(Lemma E3) from κ1 the next iteration is an S4a step to κ2 = (K1, q, K2); "
"(Lemma E4) from κ2 the next iteration is an S4a step to σ* with K-config κ3 = (K1, q, K1) and σ*(β_g) = pb_g at every gate g, and Iσ* = ∅ whatever σ* is at the movers; "
"(Lemma TERM-XI) both runs terminate; "
"(Theorem ENDGAME-3, Theorem ENDGAME-3-N5) N5′-xi, and N5, from S3 on Γ3(G) have exactly one fallback, at an iteration F ≥ 1, and make exactly F + 2 iterations, iterations 1, …, F − 1 being S4a steps with K-config κ0 and τ0; "
"(Corollary EXACT-L, for G ∈ IDEAL-ACYC: «" + Q["ACYC"][:-1] + "», premise RESULTS R117 (f)) N5 from S3 on Γ3(G) makes exactly L(G) + 3 iterations, L(G) the length of G's IDEAL run, so on {Γ3(G) : G ∈ IDEAL-ACYC} N5's count is polynomial in n iff L(G) is polynomial in N + M; "
"(Corollary END-T3, PROVED-CONDITIONAL on RESULTS R118 (k)'s Theorem REACH3-CYC, which is itself «" + Q["R3CC"] + "», and of these RESULTS R117 signs S3-START, PAD, K3 and TAU3 for every genome but ESC3 and W3 for acyclic Ξ-graphs only) if REACH3-CYC holds for G, N5′-xi from S3 on Γ3(G) makes exactly T3 + 3 iterations, T3 + 1 being REACH3-CYC's first fallback "
"(premises, all under the standing SPEC premise 1E-N3 of RESULTS R57 / R104 / R117 (fixes entry 1, W-1: «" + W1 + "»): RESULTS R104's definitions of the genome, of Γ(G), of IDEAL-ACYC and of the start pair only; RESULTS R117's definition of Γ3 and pad priorities (P-N5-REACH §3), Lemma S3-START and, for E0, TAU3 («In the standard state, Iτ = ∅, so S4b leaves τ unchanged.», signed for every genome per R118: «" + Q["TAU3"] + " genome»); "
"[1E-N3] = RESULTS R57 (b) as landed in R104 («" + Q["1E"] + "»…, a pointwise optimum of the S4a arena before S4c), used for σ̄ and for S4a's σ_new inside SPEC runs (R118 (b)'s [OPT] is not used); "
"RESULTS R15 (c) («" + Q["R15"] + "») for TERM-XI; RESULTS R117 (f) for EXACT-L only; RESULTS R118 (k) for END-T3 only; the SPEC text docs/new/N5-ssi-global.md S1-S5 with FIX 1 and FIX 3; "
"not used: ESC3, W3, KEY3, SBAR3, PLAY3, PAD (b)-(c), R118 (b)'s [OPT], any P-N5-QUIET or box 194 lemma, any L-RED lane lemma) (2026-11-08) — "
+ SCOPE + "; EXACT-L is false without IDEAL-ACYC's self-loop clause: L-RED 57's SELFL_n3 (N 3, two Ξ self-loops; experiments/new/box195/inst/SELFL_n3.json, sha1 27bc7f72…) has L(G) = 1 and N5 makes 3 iterations (F = 1); "
"END-T3 gives no bound on T3: P-N5-QUIET's QUIET / T-QUIET bound IDEAL-CYC's T_CYC on Γ(G), and their transfer to the Γ3 run (equal runs at exact VJ ties) is NOT proved; "
"DATA, clause by clause (unit: runs of N5′-xi (EG195_MODE xi) or N5 (spec) from S3 on Γ3(G) built by box189/gamma3.py, stepped by box190/n5v.py; tool experiments/new/box195/eg195.py, run by check195.sh; "
"set: 8 families (rand d 1-5; L-RED R221 §11's esc, noesc, deep, dense, lvl0, transcribed; late, a stand-in with start = each mover's last option; acyc) × 1,500 × seeds 1951, 1952, 24,000 runs per mode, 48,000 in all (data/sweep195.out), plus the 14 R117 corpus genomes and every pinned genome of box189 and box191-box194, all pinned in box195/end.pins): "
"E0: e0fail 0 (unit: states); E1: e1fail 0 (unit: iterations before the first fallback); E2, E3, E4 (a): e2fail, e3fail, e4fail 0 (unit: the iterations F, F + 1, F + 2); "
"E4 (b): stopfail 0, finsbar 0, fintie 0 (unit: final states); ENDGAME-3, ENDGAME-3-N5: nofb 0, late 0, capped 0 (unit: runs), every run «one fallback, 3 iterations from it»; "
"EXACT-L: lfail 0 (unit: IDEAL-ACYC genomes with F ≠ L(G) + 1 or total ≠ L(G) + 3) on 4,297 genomes (4,283 random IDEAL-ACYC ones in the spec sweep, 3,000 of them from acyc, and the 14 corpus genomes; L(G) up to 59, RECT_d11_T59_norm; L(G) by L-RED's ideal.traj at claude/l-red 86a7a7a8, record only); "
"controls fire (ctrl1 100 of 100 runs, ctrl2 200 states; check195.out); independent replay L-RED 57 R222 item 3 (claude/l-red 6f56004c, own code): 8,100 runs, every counter 0, and L-RED 58 R223 item 1 (claude/l-red 143f0b4c): 8,100 family runs, 48,816 exhaustive N ≤ 2 genomes × 3 modes, 30,000 N = 3 genomes, 515 second-implementation checks, 0 fails; both cited, not re-run; "
"no separate DATA for TERM-XI and END-T3; "
"G-N5-TIME stays OPEN, N5′-xi stays a CANDIDATE (D1); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4: "
"not M3, not M4, not a step-4 pass, not a TARGET.md claim "
"(P-N5-END, docs/new/P-N5-END.md, frozen at l-new 131b4c1c, sha1 5cae845b, with fixes entry 1, docs/new/P-N5-END-fixes.md; L-NEW successors 63-64; credit: ENDGAME-3 conjecture, E0-E4 skeleton and family generator L-RED 56, R221 §10-§11)")
assert "|" not in L and "\n" not in L and L.count(W1) == 1
for k in ("E0", "E1", "E2", "E3", "E4", "TERM-XI", "ENDGAME-3", "ENDGAME-3-N5", "EXACT-L", "END-T3"): assert ("Lemma " + k in L) or ("Theorem " + k in L) or ("Corollary " + k in L), k
for s in ("SELFL_n3", "lfail 0", "4,297", "24,000 runs and spec 24,000"): assert s in pk, s
assert "In the standard state, Iτ = ∅, so S4b leaves τ unchanged." in pkflat
open("docs/new/P-N5-END-line-L1.txt", "w", encoding="utf-8").write(L + "\n")
print("ok", len((L + "\n").encode()), hashlib.sha1((L + "\n").encode()).hexdigest())
