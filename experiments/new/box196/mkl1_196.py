#!/usr/bin/env python3
# P-N5-CHAIN line L-1 generator (L-NEW successor 64). From the repo root: python3 experiments/new/box196/mkl1_196.py RESULTS_COPY
# RESULTS_COPY = git show a1decf9a0:docs/RESULTS.md (trunk at writing). Asserts: the frozen packet's sha1, the RESULTS quotes verbatim, every
# statement name of the «To sign» table, one line, no «|», balanced parentheses.
import sys, hashlib
pk = open("docs/new/P-N5-CHAIN.md", encoding="utf-8").read()
PK = hashlib.sha1(pk.encode()).hexdigest(); assert PK == "6e613ba762b6ecf67247ef6d8674b4c960013039", "frozen packet changed"
res = " ".join(open(sys.argv[1], encoding="utf-8").read().split())
Q = {"R3CC": "Theorem REACH3-CYC, CONDITIONAL on P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3 for every genome",
     "SIGN": "RESULTS R117's entry signs S3-START, PAD, K3 and TAU3 for every genome and ESC3, W3 for acyclic Ξ-graphs",
     "R15": "Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}.",
     "STD": "under the standing SPEC premise 1E-N3"}
for k, q in Q.items(): assert q in res, k
L = ("On Γ3(G) of RESULTS R117 (n3 = N + 7M + 10), for N5′-xi (RESULTS R118's [N5XI]) from SPEC's default start S3, iterations counted as in SPEC S4, "
"and on HOW3(G), the Howard run on Γ3(G) (every non-mover Even vertex frozen at the standard state's choice of P-N5-REACH §3, Odd unrestricted at the gates and K2, every mover moving to a ⊴-best successor and keeping a best current one; T3 := the first state at which no mover has a strictly better successor), "
"for every genome G (Ξ-cycles and Ξ self-loops allowed), each PROVED (every genome): "
"(Lemma ESC3-ALL) in every standard state Iσ ∋ (K0, K1), every pointwise optimum of S4a's arena agrees with σ off the movers, and TIE(β_g) = {xt(g)}, TIE(K0) = {pA}; "
"(Lemma W3-ALL) in every standard state every option of a level-ℓ mover has arena value (c_W, ∅, 5ℓ + 4), no mover is its own arena cycle node and TIE(x) = A(x); "
"(Theorem REACH3-ALL) N5′-xi from S3 on Γ3(G) visits only standard states and its mover parts form a run of HOW3(G) until its first fallback, at iteration T3 + 1, i.e. RESULTS R118 (k)'s Theorem REACH3-CYC («" + Q["R3CC"] + "») holds without its condition, the premises ESC3 and W3 being proved here for every genome (RESULTS R118 (k): «" + Q["SIGN"] + "»); "
"(Facts F1, F3, F4′, F5, F6, DOM, STRICT on HOW3(G)) F1 from RESULTS R15 (a) («" + Q["R15"] + "»), not from R118 (b); "
"(Lemma CN2-3) for every positional pair and every vertex v other than c_X the cycle node of v's play has priority ≥ 3, so no mover, gate or pad is ever a cycle node or in a set Π; "
"(Lemma LOC-GATE3) at every state and gate g, if the faces pe_g, pβ_g have different values then Odd's optimal counterstrategy σ̄_t picks the strictly ⊴-smaller one; "
"(Lemma LOC-K2-3) σ̄_t(K2) = r and Ω_t(r) ◁ Ω_t(K2) at every state; "
"(Lemma B-ONLY3) at every state and every vertex v other than c_W, the e-vertices whose successor is c_W and their pads pe_g, Λ_t(v) is less relevant than every e-vertex; "
"(Corollary NO-TIE3) Ω_t(pe_g) ≠ Ω_t(pβ_g) at every state and gate; "
"(Theorem QUIET3) with class_t(v) := (Λ_t(v), E_t(v)), E_t(v) the e-vertices of Π_t(v), every maximal window of steps in which no vertex changes class has at most L3 := (M + 1)(2M + 1)(N + 1) + N(n3 − 1) steps; "
"(Corollary T-QUIET3) T3 ≤ (1 + Σ_v (D^tot_E(v) − 1))·(L3 + 1), D^tot_E(v) the number of distinct classes of v over the run, the sum over the n3 vertices; "
"(Lemma E-MON3, Lemma CHAIN-DECOMP3, Corollary HUB-ASC-G3, the last CONDITIONAL on P-N5-ASC §4) P-N5-ASC's game lemmas on HOW3(G), so that if seq_t(v), the e-vertices of Π_t(v) in play order, has at most B ascents for every state then D^tot_E(v) ≤ (2M + 3)·F′_B(M), for every vertex v of Γ3(G); "
"(Lemma UP-JUMP3, Corollary UP-B3, under HYPOTHESIS [E-LEV]: lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′))) every seq_t(v), for every vertex v including pads and K-vertices, has at most U(G) ascents, U(G) the number of options whose Ξ-target is a mover of higher level; "
"(Theorem CHAIN3, PROVED under HYPOTHESIS [E-LEV] and CONDITIONAL on the unlanded lane packets P-N5-END (ENDGAME-3) and P-N5-ASC §4 (its abstract core and F′; RESULTS R121 when landed)) N5′-xi from S3 on Γ3(G) makes at most T3 + 3 ≤ (1 + n3·((2M + 3)·F′_(U(G))(M) − 1))·(L3 + 1) + 3 iterations, a polynomial in N + M for U(G) ≤ B, B fixed; "
"(DEAD RUN-TRANSFER) T3 is not the IDEAL-CYC count on Γ(G): instance RT_n1 (experiments/new/box196/inst/RT_n1.json, sha1 829f3c97…; N 1, three options, all Ξ self-loops) has T3 = 1 and T_CYC = 2, two options being exactly tied in both games and the tie rules differing "
"(premises, all " + Q["STD"] + " (RESULTS R57 (b)), as in RESULTS R104 / R117: RESULTS R104's definitions of the genome and of Γ(G) only; RESULTS R117's Γ3, standard state, S3-START, PAD (a), K3 and TAU3, signed for every genome; RESULTS R118's σ̄(K2) = r for every genome, [N5XI] and (k)'s proof (P-N5-XICYC §7) re-run with ESC3-ALL and W3-ALL; RESULTS R15 (a); VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the value (Λ, Π, k) and its order ⊴; [OPT] for HOW3's σ̄_t = RESULTS R118's σ̄ as used in R118 (b) and RESULTS R21 (a), R57 (b) not used there; in the SPEC run (S4a's arena, REACH3-ALL) [1E-N3] = RESULTS R57 (b) as landed in R104; "
"lane packets, not landed: P-N5-END's Theorem ENDGAME-3 (frozen at l-new 131b4c1c, REFEREE 29 SIGN) for CHAIN3, P-N5-ASC §4's game-free abstract core CS(M) and its constants F′_B (RESULTS R121 when landed) for HUB-ASC-G3 and CHAIN3; P-N5-QUIET's proofs are templates, none of its statements is a premise; HYPOTHESIS [E-LEV] for UP-JUMP3, UP-B3 and CHAIN3 only; "
"not used: PLAY3, SBAR3, KEY3, Fact X, R118 (b)'s F1 and STRICT, any L-RED lemma) (2026-11-08) — "
"this bounds N5′-xi's iteration count on one restricted family, {Γ3(G) : U(G) ≤ B} under [E-LEV], and says nothing about N5 (whose pre-fallback run on Ξ-cyclic genomes is not a Howard run), about genomes with U(G) unbounded (Σ_v D^tot_E(v) stays OPEN), about other games or about general parity games; the degree in M grows like 5·2^B (from P-N5-ASC's F′, not re-checked here) and the per-iteration cost at bit cost is a separate gauntlet step-4 item; "
"DATA, clause by clause (unit: runs of N5′-xi, or N5 with Q196_MODE spec, from S3 on Γ3(G) built by box189/gamma3.py, stepped by box190/n5v.py, observed on states 0, …, T3; tool experiments/new/box196/qt3_196.py; scope: gamma3.py's e-priorities by (lev, gate), so [E-LEV] holds; "
"set: box195 eg195.gen families rand, esc, noesc, deep, dense, lvl0, late, acyc × 500 × seeds 1961, 1962, 8,000 runs, plus 58 pinned genomes of box189/corpus, box191-box195/inst and RT_n1, data/sweep196.out; check196.sh, re-run by check.sh: 8 families × 100, seed 1964, controls, spec on 100 runs and 5 pinned genomes, check196.out): "
"REACH3-ALL: nonstd 0 (unit: states), nohoward 0 (unit: (state, mover) pairs); CN2-3: cnlow 0 (unit: (state, vertex) pairs); LOC-GATE3: locfail 0, NO-TIE3: ties 0 (unit: (state, gate) pairs); B-ONLY3: bonly 0 (unit: (state, vertex) pairs); LOC-K2-3: k2fail 0 (unit: states); "
"QUIET3: wfail 0 (unit: quiet windows), crossflip 0 (unit: σ̄ flips on quiet steps at gates whose faces are in different classes), longest quiet window 32 (RS2_L32M6); T-QUIET3: Tfail 0 (unit: runs); E-MON3: emon 0 (unit: (step, vertex) pairs); UP-B3: upfail 0 (unit: (state, vertex) pairs with more than U(G) ascents), max ascents 4; max T3 129 (LEAP_k64); "
"controls fire (every fail counter has one): ctrl1 (L3 := 0, U(G) := −1) wfail 32, Tfail 22, upfail 26,477 in 50 runs; ctrl2 (order reversed) locfail 3,320; ctrl3 (no excluded vertex) bonly 2,269; spec mode nohoward 599 (rand, 200 runs) and 911 (dense, 200 runs); "
"nonstd, cnlow, k2fail, crossflip and emon by L-RED 58's fault injection (experiments/red/r224/ctrl224.py at claude/l-red e7937985, copied with credit as box196/ctrl196.py, output ctrl196.out): 75 of 75 (genome, counter) controls fire on L-SI's 11 box-85 genomes (box196/inst_si85/) and 4 corpus genomes; "
"record only: tdiff (runs with T3 ≠ T_CYC) 100 of the 8,000 runs; independent checks cited, not re-run: L-RED 58 R223-reach (claude/l-red 71133de5) and R224-chain (claude/l-red e7937985), both SURVIVES; every run is short, so the data test only that nothing exceeds L3, not its tightness; "
"no separate DATA for HUB-ASC-G3 and CHAIN3; "
"G-N5-TIME stays OPEN, N5′-xi stays a CANDIDATE (D1); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4: not M3, not M4, not a step-4 pass, not a TARGET.md claim "
"(P-N5-CHAIN, docs/new/P-N5-CHAIN.md, frozen at l-new 93531b03, sha1 " + PK[:8] + "; source box 196, docs/new/N5-CHAIN-box196.md; L-NEW successor 64; credit: chain map L-RED 58 R223-q2 §4, F1 / STRICT re-citation R223-reach §3, controls R224-chain §5)")
assert "|" not in L and "\n" not in L and L.count("(") == L.count(")"), (L.count("("), L.count(")"))
for k in ("ESC3-ALL", "W3-ALL", "REACH3-ALL", "CN2-3", "LOC-GATE3", "LOC-K2-3", "B-ONLY3", "NO-TIE3", "QUIET3", "T-QUIET3", "E-MON3", "CHAIN-DECOMP3", "HUB-ASC-G3", "UP-JUMP3", "UP-B3", "CHAIN3", "RUN-TRANSFER"):
    assert k in L and k in pk, k
open("docs/new/P-N5-CHAIN-line-L1.txt", "w", encoding="utf-8").write(L + "\n")
print("ok", len((L + "\n").encode()), hashlib.sha1((L + "\n").encode()).hexdigest(), "packet", PK)
