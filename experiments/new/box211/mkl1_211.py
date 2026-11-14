#!/usr/bin/env python3
# P-N5-LEVEL line L-1 generator (L-NEW successor 73): the lane's PROPOSED RESULTS line for the frozen packet. Run from the repo root:
#   git show TRUNK:docs/RESULTS.md > RES.md; python3 experiments/new/box211/mkl1_211.py RES.md
# Asserts: the frozen packet's sha1; every statement of the line verbatim (whitespace-normalised) in the packet; the DATA counts of the
# line against the generated tables of the packet's §11; R124's landed TARGET tail verbatim in RESULTS; quotes211.out «missing 0»;
# no «|», one line, balanced parentheses. Writes docs/new/P-N5-LEVEL-line-L1.txt and prints its sha1 and size.
import sys, hashlib, re
PACKET_SHA1 = "7c956df443cfddbf23bfbaa18a26a98369b176ec"
pk = open("docs/new/P-N5-LEVEL.md", "rb").read()
assert hashlib.sha1(pk).hexdigest() == PACKET_SHA1, "packet sha1"
norm = lambda t: " ".join(t.split())
pt = norm(pk.decode("utf-8")); res = norm(open(sys.argv[1], encoding="utf-8").read())
qo = open("experiments/new/box211/quotes211.out", encoding="utf-8").read().strip().split("\n")[-1]
assert re.match(r"quotes \d+ missing 0 \(trunk [0-9a-f]{40}\)$", qo), qo
# statements, verbatim in the packet
for s in ("class_t(v) ≤ class_(t+1)(v) for every vertex v and every step t → t + 1.",
          "class_t(g) = min(class_t(e_g), class_t(β_g)) for every gate g and state t",
          "For every mover x, every step t → t + 1 and every gate y of x: class_(t+1)(x) ≥ class_t(y).",
          "On [a, b] the potential Φ takes at most 2M·(N + 2M) = P values",
          "Hence b − a ≤ M(N + 2M) + N = A.",
          "For every maximal interval [a, b] of states of constant class(R): b − a ≤ A",
          "Then class(R) changes at at most P steps: D^tot(R) ≤ P + 1.",
          "For every genome with Ξ-feedback number 1: T_CYC ≤ P·(A + 1) + N.",
          "For every genome with Ξ-feedback number k: T_CYC ≤ (P + N)·(P + 1)^k.",
          "For every genome, every reference state b and every maximal interval [u, v] of states of constant Φ (reference b): v − u ≤ N + 2M + 5.",
          "For every genome G: T_CYC ≤ P·(N + 2M + 6) + N, P = 2M(N + 2M).",
          "Constants: P := 2M(N + 2M); A := M(N + 2M) + N."):
    assert s in pt, "statement not verbatim in the packet: " + s
# DATA counts, from the generated tables of §11
rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in pk.decode("utf-8").split("\n") if l.startswith("| ")]
def tot(prefix, col, zero_col):
    n = 0
    for r in rows:
        if r[0].startswith(prefix):
            assert r[zero_col] == "0", ("must-0 column not 0", r[0])
            n += int(re.match(r"\d+", r[col]).group(0))
    return n
assert tot("level208_records.out", 1, 2) == 25 and tot("level208_corpus.out", 1, 2) == 53
assert tot("level208_rand_", 1, 2) == 5000 and tot("mut208_", 1, 2) == 2000
assert tot("own208_records.out", 1, 2) == 25 and tot("own208_corpus.out", 1, 2) == 53
assert tot("plat208_records.out", 1, 2) == 25 and tot("plat208_corpus.out", 1, 2) == 53
assert tot("plat208_rand_", 1, 2) == 3600 and tot("plat208_mut", 1, 2) == 1200
assert tot("rv208_frozen.out", 2, 3) == 81 and tot("rv208_mut_", 2, 3) == 480 and tot("rv208_rand_", 2, 3) == 3300
assert "max Phi values 199" in pt and "(longest 26;" in pt and "P = 2,120,796" in pt
assert sum(1 for r in rows if r[0].startswith("CONTROL") and "fires:" in r[2] and "NOTHING" not in r[2]) >= 5
assert any(r[0] == "plat208_ctrl1.out" and r[2].startswith("CONTROL fires") for r in rows)
assert any(r[0] == "rv208_ctrl1.out" and r[3].startswith("CONTROL fires") for r in rows)
TAIL = ("TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4, so "
        "this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim")
assert TAIL in res, "R124's TARGET tail not in RESULTS"
L = ("In IDEAL-CYC(G) (RESULTS R118 (a): Γ(G) with every non-mover Even vertex frozen at R104's start, Odd unrestricted (gates and K2), "
"Howard steps at the movers: every mover goes to a ⊴-best successor and keeps its current successor if that is ⊴-best), for every genome "
"G (Ξ-cycles and Ξ self-loops allowed) with N movers and M options, on the states 0, …, T_CYC of the run, with class_t(v) := (Λ_t(v), "
"E_t(v)) and loud / quiet steps as in RESULTS R123, the classes ordered by the reward of Λ and then by the lexicographic order of "
"RESULTS R121 on E, P := 2M(N + 2M) and A := M(N + 2M) + N: (class facts) (K1) no class ever falls; (K2) of two triples whose cycle "
"node and Π-set are those of plays of vertices outside the core, a ⊴-larger one has a class at least as large; (K3) a vertex has the "
"class of its successor on its play, except an e-vertex with a mover successor, whose class is strictly larger; (K4) a gate has the "
"smaller of the classes of its two faces; (K5) after a step a mover's class is at least the class that each of its gates had before "
"the step; (Lemma LEVEL) for a reference state b and a state t < b, with LAG_t the vertices whose class at t is not their class at b, "
"m_t the least class of a vertex of LAG_t, FRONT_t the vertices of LAG_t of class m_t, f_t their number and Φ_t := (m_t, −f_t) ordered "
"lexicographically: Φ never falls; it stays equal exactly at a stall (a step at which no vertex of FRONT_t changes class); at a stall "
"FRONT_t contains movers x_1, …, x_r that form a cycle of the Ξ-graph through their options at b, with their gates at b and those "
"gates' β-faces; and Φ takes at most P values; (Theorem WIN) if S is a set of movers meeting every cycle of the Ξ-graph and every "
"vertex of S keeps its class on the states a, …, b, then, with reference b and b′ the first state with LAG = ∅, no step before b′ is a "
"stall, b′ − a ≤ M(N + 2M), the steps after b′ are quiet, and b − a ≤ A; (Corollary R-INT) at Ξ-feedback number 1 (RESULTS R126), with R "
"a mover on every cycle of the Ξ-graph, every maximal interval of states of constant class(R) has at most A steps; (Theorem R-HEIGHT) "
"at Ξ-feedback number 1, class(R) changes at at most P steps; (Theorem K1-TCYC) at Ξ-feedback number 1, T_CYC ≤ P·(A + 1) + N; (Theorem "
"FVS-TCYC) at Ξ-feedback number k, T_CYC ≤ (P + N)·(P + 1)^k; (Lemma PLATEAU) for every reference state, every maximal interval of "
"states of constant Φ has at most N + 2M + 5 steps; (Theorem ALL-TCYC) for every genome G, T_CYC ≤ P·(N + 2M + 6) + N (premises: RESULTS "
"R104's definitions of the genome and of Γ(G) only, with the readings (D1), (D3), (D4) of the packet landed as RESULTS R126; RESULTS "
"R118 (a), (b) F1 (RESULTS R15 (a) Lemma A), (c) DOM, (e) with its stated reason, (i) Theorem BR-SEG-G (a) under H0, applied in PLATEAU "
"to a one-player sub-game, and R118's order ⊴ on values (Λ, Π, k) (VJ00 §4.2 / Friedmann arXiv 1106.0778 §3); RESULTS R121 Lemma E-MON "
"and its [DEF] fact E-DOM; RESULTS R123 Lemma CN2, Lemma B-ONLY, Corollary NO-TIE, Lemma LOC-GATE, Lemma LOC-K2 and [OPT] (σ̄_t is "
"optimal at every vertex at once, spelled out in RESULTS R122 as the standing premise 1E-N3 of RESULTS R57 (b)); RESULTS R126 "
"Corollary QUIET-N; the class facts, LEVEL, WIN, R-INT, R-HEIGHT, K1-TCYC and FVS-TCYC use neither PLATEAU nor F1, [OPT], (D1) or "
"BR-SEG-G; not used: any lane packet or lane lemma, any Γ3 fact, [E-LEV], any Lean theorem) (2026-11-12) — this bounds the steps of "
"one improvement rule (Howard all-switch with Even, the maximiser, improving, switch-best with keep-if-best) in one restricted model "
"on one restricted family of games; single-switch rules and other rules are not covered; the proofs use the genome's shape, through "
"E-DOM and B-ONLY in (K2) and (K3), on which Lemma LEVEL and all that follows rest, through DOM with CN2 in (K5), and through QUIET-N and (D1) for Odd's "
"choices while classes stand still, and they are not an argument about Howard's rule on parity games in general; nothing is proved "
"on Γ3, for N5′-xi, for N5 or for other games; when ALL-TCYC stands it supersedes K1-TCYC and FVS-TCYC as bounds for M ≥ 2 and k ≥ 1, "
"and at k = 0 RESULTS R122's T_CYC ≤ N is sharper than FVS-TCYC and ALL-TCYC; the step of PLATEAU's proof in which Odd answers a later strategy by "
"the plateau state's counterstrategy σ̄_s ([OPT], then F1) is referee-originated (REFEREE 32, claude/referee 7524342b, "
"docs/referee/R-box208-preread.md §5.2, gap G-P6; found independently as G-1 by L-RED-B, claude/l-red-b 0510c800, "
"docs/red-b/B1-box208.md §2.5); DATA, clause by clause (scope IDEAL-CYC from the genome's start, every vertex of Γ(G); tools and frozen "
"outputs in experiments/new/box208/, pinned in experiments/new/box211/level.pins; no run tests the constants: at most 199 values of Φ "
"in a run, where P = 2,120,796, and no plateau longer than 26 steps): class facts, LEVEL, WIN, R-HEIGHT: the 16 must-0 counters of "
"level208.py (monofail, k3fail, k4fail, k5fail; einF, l3fail, phifail, stallnocyc, nofvs, rstall, boundfail; winstall, wbeta, wl3fail, "
"wmid, wbound; units in the packet §11) are 0 on the 25 frozen k = 1 genomes, the 53 genomes of box202/inst (window counters for k ≤ 3 "
"only), 5,000 random genomes and 2,000 mutants, and, on a second engine (L-RED 54's own.py through ownhist208.py), on the 78 frozen "
"genomes; PLATEAU: the 6 must-0 counters of plat208.py (p1, pclos, p2, p3, p4, p5) are 0 on the 78 frozen genomes, 3,600 random "
"genomes and 1,200 mutants; every reference state: the 49 must-0 counters of rv208.py (a third implementation with its own builder, "
"valuation, Odd reply and run) are 0 on 81 frozen genomes, 480 mutants and 3,300 random genomes; the controls LV_CTRL, PL_CTRL and "
"RV_CTRL fire; R-INT, K1-TCYC, FVS-TCYC and ALL-TCYC: no separate DATA beyond boundfail (they follow from LEVEL, WIN and PLATEAU); on "
"Friedmann's game G_N, N = 1, …, 8, lifted to a plain parity game by L-COMP 19 (claude/l-comp a6cce717, experiments/comp/box43, cited, "
"not re-run), the counter of (K5) is 0 on G_1 and first fires on G_2 at the step 5 → 6, at an odd vertex above an escape vertex, which "
"E-DOM excludes on Γ(G) (DATA on eight instances); independent replays, every fail counter 0, their counters in their own outputs, "
"cited, not re-run: L-RED 66 R235 (claude/l-red 2d2969c2), L-RED-B B1 (claude/l-red-b 0510c800), REFEREE 32's pre-read (claude/referee "
"7524342b), L-COMP 19 BOX 43 (claude/l-comp a6cce717); " + TAIL + " (P-N5-LEVEL, docs/new/P-N5-LEVEL.md, sha1 " + PACKET_SHA1[:8] +
", frozen together with this line; L-NEW successors 72-73; related lane statements, not premises: L-RED 66's sharper plateau bound "
"through the lane lemma LAM-GAP in its sharp form SHARP, which would give T_CYC ≤ P(N + 1) + N (claude/l-red 2d2969c2, docs/red/R235-box208.md §5), L-FORMAL's "
"lane-level Lean theorems Genome.k1, Genome.k2, Genome.k3, Genome.k5, level_count, plateau and brsegG (claude/l-formal f74d38a4), "
"L-SI 52's Lemma WRAP (claude/l-si 26704e01, docs/si/box104-map.md))")
assert "|" not in L and "\n" not in L and L.count("(") == L.count(")"), (L.count("("), L.count(")"))
open("docs/new/P-N5-LEVEL-line-L1.txt", "w", encoding="utf-8").write(L + "\n")
b = (L + "\n").encode("utf-8")
print("L-1 sha1", hashlib.sha1(b).hexdigest(), "bytes", len(b), "parens", L.count("("))
