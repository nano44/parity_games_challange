# Box 203 (D18): every gate flip is a face-class change — a polynomial per-gate flip bound in face class heights (L-NEW successor 68, Opus)
Written 2026-11-09 from 04:40Z (date -u). Lead 04:14Z (retarget): «a POLYNOMIAL (not constant) per-gate flip bound at k = 1 — e.g.
flips(g) ≤ p(N + M)·(lamch(g) + 1) — proved on IDEAL-CYC first (where K1-POLY is unconditional), with GATE-LOW-NULL as the tool; MWR's
2n + 1 is the tight-looking test case. Also fix box 202's K1-POLY statement to carry REACH3-CYC's condition on Γ3 (appended correction).»
Lead 04:31Z: «… and say whether MWR's 2n + 1 is the true worst case shape or whether flips can be super-linear at k = 1.»
Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD / READING. Nothing here is a TARGET.md claim.
G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1).
Tools: experiments/new/box203/ (gfc203.py: per-gate flip classes and the counters of §1-§2; rnd203.py: random sweeps; check203.sh, wired
into experiments/new/check.sh «BOX 203 FLIP»); outputs out/; instances inst/ (L-RED 63's MWR4_2, MWR8_2, MWR16_2, copied from claude/l-red
406ef2fd experiments/red/r229/inst, sha1 equal to L-RED's SHA1SUMS; SHA1SUMS here).

## 0. Answer
- **Theorem GATE-CLASS (PROVED, lane; IDEAL-CYC, every genome, any k; premises all LANDED, §1).** If Odd's optimal counterstrategy
  changes at a gate g at step t, then the class (Λ, E) of e_g or of β_g changes at t.
- **Corollary GATE-FLIP (PROVED, lane).** flips(g) ≤ (D^tot(e_g) − 1) + (D^tot(β_g) − 1), where D^tot(v) is the number of distinct classes
  (Λ_t(v), E_t(v)) of v over the run (R123's D^tot_E). With RESULTS R121's HUB-ASC-G (whole-run form): if the e-sequences seq_t(e_g),
  seq_t(β_g) have at most B ascents, then flips(g) ≤ 2((2M + 3)·F′_B(M) − 1); under [E-LEV], B ≤ U(G) (R121 UP-B). This is the polynomial
  per-gate bound the Lead asked for, in the form «polynomial in the class heights of g's two faces», not in lamch(g). It is not k-specific:
  it holds for every genome. No bound of the form p(N + M)·(lamch(g) + 1) is proved; MWR (lamch 0, flips 2n + 1) shows p must be at least linear.
- **Corollary QUIET-N (PROVED, lane).** Every quiet step (R123: no vertex changes class) is a p-step of R118 (neither Λ nor σ̄ changes
  anywhere), so every maximal quiet window has at most N steps (R118 (d) BR-SEG), and T_CYC ≤ Q + (Q + 1)·N with Q the number of loud
  steps, Q ≤ Σ_v (D^tot(v) − 1). This sharpens landed R123 T-QUIET (window bound L = (M + 1)(2M + 1)(N + 1) + N(n − 1) → N). Same class
  of genomes; no new class becomes polynomial.
- **Against TARGET.md (READING).** A bound on IDEAL-CYC iterations for one model; not M3, not M4, not a gauntlet step-4 pass, nothing on
  Γ3 or N5′-xi (a Γ3 form needs GATE-LOW-NULL's Γ3 premises plus REACH3-CYC's open conditions, §4). G-N5-TIME OPEN.
- **MWR (k = 1), the Lead's question.** On MWR(n) the flipping gate (qz, 0) has D^tot(e_qz) = n + 1 and D^tot(β_qz) = 2n + 2, so
  GATE-FLIP gives flips ≤ 3n + 1 against the observed 2n + 1 (DATA §3). So MWR's flips are exactly as large as its faces' class heights
  allow, up to a factor 3/2. A k = 1 family with super-linear flips at one gate must have a face with super-linear class height (PROVED
  direction, GATE-FLIP); by R123 UP-T / R121 HUB-ASC-G this needs U(G) → ∞ and e-sequences with growing ascents (MWR has U(G) = 3n + 3,
  linear). Whether such a k = 1 family exists is OPEN: it is the e-set-height question of R121 / R123 restricted to k = 1, and k = 1 does
  not bound U(G). No data shows super-linear flips (max over everything measured: 2n + 1 on MWR, 4 on 5,000 random k = 1 genomes).
- **Box 202 correction (appended there, §A):** K1-POLY's Γ3 bound is RESULTS R118's REACH3-CYC, CONDITIONAL on P-N5-REACH's S3-START,
  PAD, K3, TAU3, ESC3, W3 for every genome (R117 signs ESC3, W3 for acyclic Ξ-graphs only); on IDEAL-CYC the bound T-CYC + CYC-COUNT
  holds unconditionally. Credit L-RED 63 (R229-box202 §0, §1, claude/l-red 406ef2fd).

## 1. Theorem GATE-CLASS and its proof (PROVED, lane)
Setting: IDEAL-CYC(G) of RESULTS R118 (a) for any genome G (Ξ-cycles allowed): Γ(G) with every non-mover Even vertex frozen at R104's
start, Odd unrestricted, Howard steps at the movers. Ω_t(v) = (Λ_t(v), Π_t(v), k_t(v)) is the VJ value under (σ_t, σ̄_t); E_t(v) := the
e-vertices of Π_t(v) (R121); class_t(v) := (Λ_t(v), E_t(v)) (R123); flips(g) := #{t : σ̄_(t−1)(g) ≠ σ̄_t(g)}.
Premises (each LANDED unless marked):
- [DEF] R104's Γ(G) (quoted in P-N5-QUIET §1): gates are Odd with exactly the two successors e_g and β_g; e_g has one edge, to the W-target
  or c_W, and its only predecessor is g (one e-vertex per option); E-DOM: every vertex more relevant than an e-vertex is an e-vertex, c_W,
  K0 or K3 (e of even priority above every β; c_W top; K0 top + 2; K3 top + 3); core K0 → {K1, K3}, K1 → {K0, K1}, K2 → {K1, K2},
  K3 → {K1, K2}, frozen K0 → K3, K1 → K1, K3 → K2; u = K0 is the escape target of the β's.
- R123 Lemma CN2 (no gate or mover is a cycle node or in a set Π), Lemma B-ONLY («at every state t and every vertex v other than c_W and
  the e-vertices whose successor is c_W, Λ_t(v) is less relevant than every e-vertex»), Corollary NO-TIE («Ω_t(e_g) ≠ Ω_t(β_g)»), Lemma
  LOC-GATE («σ̄_t chooses the face of strictly ⊴-smaller value»), Lemma LOC-K2 («σ̄_t(K2) = K1»).
- [VJ] the order ⊴ (R118 header: VJ00 §4.2 / Friedmann arXiv 1106.0778 §3): first the reward of Λ, then Π by the most relevant vertex of
  the symmetric difference (better for Even iff it is even and in the larger set), then k.
- For the counting only: R118 (e)'s reason «each vertex's Λ moves only to a vertex of strictly larger reward» and R121 Lemma E-MON («if
  Λ_t(v) = Λ_(t+1)(v) then E_t(v) ≤ E_(t+1)(v)»): so the classes of v appear in strictly increasing order and never repeat, and the
  number of steps at which class(v) changes is D^tot(v) − 1.
- For QUIET-N only: R118 (d) BR-SEG («every maximal run of p-steps has at most N steps»; p-step: neither a cycle node nor σ̄ changes).
- Not used: GATE-LOW-NULL itself (L-SI box 92, lane-proved on Γ3); its argument is re-done on IDEAL-CYC in Case 2 from the landed premises
  above. Not used: [E-LEV] (except in the U(G) form of GATE-FLIP), any L-RED lane lemma, OVT-DV, IN-BOUND, P-N5-CHAIN facts.

**Theorem GATE-CLASS.** For every genome G, every gate g and every step t of IDEAL-CYC(G): if σ̄_(t−1)(g) ≠ σ̄_t(g), then
class_(t−1)(e_g) ≠ class_t(e_g) or class_(t−1)(β_g) ≠ class_t(β_g).

Proof. Write a = e_g, b = β_g, and suppose neither a's nor b's class changes at t; we show σ̄(g) does not change. Then Λ_(t−1)(a) = Λ_t(a)
=: w_a and Λ_(t−1)(b) = Λ_t(b) =: w_b.
- Case 1: w_a ≠ w_b. Distinct cycle nodes have distinct rewards (priorities injective by rank, [VJ]), so the comparison of Ω_s(a) and
  Ω_s(b) is decided by Λ, the same way at s = t − 1 and s = t. By LOC-GATE σ̄_s(g) is the face of smaller value, the same at both. No flip.
- Case 2: w_a = w_b =: w. Since a ≠ c_W, the only exception in B-ONLY for a is «a's successor is c_W»; then Λ_s(a) = c_W, while b is not
  an exception (b is a β), so Λ_s(b) is less relevant than every e-vertex, hence ≠ c_W = Λ_s(a): Case 1. So w is less relevant than every
  e-vertex, in particular than e_g = a. As a is the first vertex of its own play and is not its cycle node, a ∈ Π_s(a), so e_g ∈ E_s(a).
  - Case 2a (PRIV at s): e_g ∉ Π_s(b). Let z be the most relevant vertex of Π_s(a) Δ Π_s(b); the set contains e_g, so z is e_g or more
    relevant than e_g, hence by E-DOM z is an e-vertex, c_W, K0 or K3. c_W is in no Π (a play that reaches c_W has Λ = c_W, excluded by
    B-ONLY for a and b). K0 and K3: a play from a non-core vertex enters the core only at K0, and from K0 the frozen edges and LOC-K2 give
    K0 → K3 → K2 → K1 → K1; so a play contains K0 iff it contains K3 iff its cycle node is K1. Both plays have the cycle node w, so K0 and
    K3 lie in both Π's or in neither, not in the symmetric difference. Hence z is an e-vertex at least as relevant as e_g, and z is the
    most relevant element of π(E_s(a)) Δ π(E_s(b)), π(X) := {f ∈ X : f = e_g or f more relevant than e_g}. By [VJ] the side holding z
    (even) is better for Even. By LOC-GATE σ̄_s(g) is the face whose π(E_s) is lexicographically smaller. So on PRIV states σ̄_s(g) is a
    function of (π(E_s(a)), π(E_s(b))).
  - Case 2b (non-PRIV at s): e_g ∈ Π_s(b). Then b's play passes e_g; e_g's only predecessor is g, so b's play passes g and continues to
    e_g: σ̄_s(g) = a.
  - If both s = t − 1 and s = t are PRIV: E_(t−1)(a) = E_t(a) and E_(t−1)(b) = E_t(b) (classes unchanged), so the π-pairs are equal and
    σ̄(g) does not change (Case 2a). If both are non-PRIV, σ̄_(t−1)(g) = σ̄_t(g) = a (Case 2b). If exactly one is non-PRIV, then e_g lies in
    E_s(b) for exactly one s ∈ {t − 1, t} (e_g is more relevant than w, so e_g ∈ Π_s(b) ⟺ e_g ∈ E_s(b)): E(b) changes at t, against the
    assumption. ∎
- Remark (scope of the cases): Case 2a is L-SI's GATE-LOW-NULL (box 92 §1) read on IDEAL-CYC; the hypothesis «e_o above Λ» of its part
  (b) is automatic here by B-ONLY. Case 2b is the non-PRIV gate (L-SI's class K7, «no lemma»): GATE-CLASS does not bound how often it
  happens; it only says each K7 flip moves e_g into or out of the β-face's e-set, so it is paid by a class change of β_g.

**Corollary GATE-FLIP.** flips(g) ≤ (D^tot(e_g) − 1) + (D^tot(β_g) − 1) for every gate g.
Proof. Each flip step is a step at which class(e_g) or class(β_g) changes (GATE-CLASS); each vertex's class changes at exactly
D^tot − 1 steps (counting premise). ∎
- With R121 HUB-ASC-G's whole-run form («D_E(v) ≤ (2M + 3)·F′_B(M)» when every seq_t(v) has at most B ascents, D_E(v) the number of
  distinct (Λ_t(v), E_t(v)) = D^tot(v)): flips(g) ≤ 2((2M + 3)·F′_B(M) − 1) when the plays from e_g and β_g have at most B ascents.
  Only the two faces' ascents matter. Under [E-LEV] (HYPOTHESIS, as in R121 / R123) B ≤ U(G) for every vertex (R121 UP-B).
- No lamch factor and no k: the bound is in the faces' class heights. lamch(g) ≤ (D^tot(e_g) − 1) + (D^tot(β_g) − 1) as well, so GATE-FLIP
  is at least as strong as any bound c·(lamch(g) + 1) would be whenever the e-sets are constant on Λ-intervals — but in general it is
  incomparable with K1-FLIP(c)'s form.

**Corollary QUIET-N.** In IDEAL-CYC(G), every step at which no vertex changes class is a p-step of R118; every maximal window of quiet
steps has at most N steps; and T_CYC ≤ Q + (Q + 1)·N, Q := the number of loud steps ≤ Σ_v (D^tot(v) − 1).
Proof. At a quiet step no Λ changes; σ̄ does not change at any gate (GATE-CLASS) nor at K2 (LOC-K2), and gates and K2 are Odd's only
vertices with a choice ([DEF]); NO-TIE and LOC-GATE make σ̄ unique, so R118's labelling has no choice to fix. So a quiet step is a p-step,
a quiet window lies inside a p-run, and BR-SEG gives ≤ N steps. The T bound: the steps split into Q loud steps and at most Q + 1 quiet
windows. Q ≤ Σ_v (D^tot(v) − 1) since each loud step changes some vertex's class. ∎
- Against landed R123: T-QUIET reads «T_CYC ≤ (1 + Σ_v (D^tot_E(v) − 1))·(L + 1)» with L = (M + 1)(2M + 1)(N + 1) + N(n − 1); QUIET-N
  replaces L + 1 by N + 1 (and gives the loud-steps form). R123's DATA «longest window W ≤ N on every run» is now a theorem. The classes of
  genomes on which T_CYC is proved polynomial (ASC-T, UP-T) are unchanged; the degrees drop.

## 2. What this does NOT give (READING)
- No new polynomial class: GATE-FLIP and QUIET-N are polynomial in the class heights D^tot, which R121 / R123 bound only when ascents are
  bounded (U(G) bounded under [E-LEV]). k = 1 does not bound U(G) (MWR: k = 1, U(G) = 3n + 3). So at k = 1 the per-gate flip question is
  exactly the e-set-height question at the two faces; that is OPEN (it is G-N5-TIME's IDEAL-CYC core restricted to k = 1).
- Not a K1-FLIP(c) repair: lamch is the wrong denominator (MWR: lamch 0 for the whole run, C = 0 on IDEAL-CYC, every one of its 2n + 1
  flips is at globally constant Λ). Any per-gate bound with lamch must carry a factor that grows with the faces' e-set heights.
- Not on Γ3: N5′-xi on Γ3 adds pads; GATE-CLASS's Case 2a needs GATE-LOW-NULL's Γ3 premises (LOC-GATE3, NO-TIE3, E-MON3, PAD) and the
  T bound needs REACH3-CYC, CONDITIONAL (§A of box 202). Not attempted here.

## 3. DATA
Tool gfc203.py (IDEAL-CYC by box191/idealcyc.py and si.py's Engine; --g3: Γ3 by n5v / n5x as box 202). Must-0 counters (unit: (gate,
step) flips unless named; TOTALS): odd (a flip with face Λ's unequal and constant), vfail (a flip with both face values unchanged), glnfail
(Case 2a: a PRIV flip with both π's unchanged), emon (a face value or e-set decreasing at constant Λ), hfail / hefail (per-interval
height bounds), tieflip (a flip at a face tie), lfail (GATE-CLASS: a flip with neither face changing class), gfail (unit gate:
GATE-FLIP violated), qflip (unit step: σ̄ changes at a quiet step), qfail (unit run: a quiet window > N), Tfail (unit run: T > Q + (Q + 1)N).
### 3.1 Corpus (out/gfc203_corpus.out; set: the 53 box 202 genomes, MWR4/8/16_2, k1fail_202; scope IDEAL-CYC from the genome's start, cap 20,000)
Every must-0 counter is 0 on all 57 runs. Columns: T = T_CYC; C = R118's C (steps with a Λ-change anywhere); U = U(G); maxflip = max_g
flips(g) at the gate shown by gfc203 (unit: gate); (D^tot(e_g), D^tot(β_g)) at that gate; GATE-FLIP's bound there = their sum − 2; slack =
min over all flipping gates of (bound − flips) (0 = the bound is attained at some gate); Q = loud steps; W = longest quiet window (≤ N).
| family / instance | N | k (box 202) | T | C | U | maxflip | D^tot faces | bound | slack | Q | W |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MWR4_2 / MWR8_2 / MWR16_2 | 48 / 84 / 156 | 1 | 30 / 54 / 102 | 0 | 15 / 27 / 51 | 9 / 17 / 33 (= 2n + 1) | (n + 1, 2n + 2) | 3n + 1 | 2 | T | 0 |
| MW4_2 … MW32_2 (8 rows) | 48-300 | 2 | 31-199 | T − 3 | 15-99 | 18-130 (= 4n + 2) | (2n + 2, 4n + 3) | 6n + 3 | 0 | T | 0 |
| C2 … C12 frontier (11 rows) | 15-67 | ≤ 2 | 3-24 | 1-20 | 3-21 | 1-24 (= T except C2: 1 of 3) | e.g. C12 (13, 25) | 36 | 0 | T | 0 |
| FW4_2 … FW16_2, FW6_3, FW6_4, FW8_4 | 55-372 | 1 | 17-53 | T − 1..3 | 9-45 | 1 | (1, 2) | 1 | 0 | T | 0 |
| WC4_2 / WC8_2 / WC16_2 | 20-68 | 2 | 4 | 0 | 12-48 | 1 | (2, 3) | 3 | 1 | 4 | 0 |
| CT12_cap200 / CT26 / CT27 | 63-126 | 12 / 8 / 8 | 46-79 | 33-74 | 22-52 | 5 / 2 / 4 | (8, 5) / (53, 2) / (9, 7) | 11 / 53 / 14 | 2 / 0 / 0 | 40-79 | 6 / 0 / 0 |
| DSALT6 / DSALT7 / DSALT9 | 108-416 | 8 / 10 / > 12 | 21 / 11 / 30 | 0-1 | 31-203 | 7 / 7 / 11 | (6, 10) / (6, 10) / (18, 24) | 14 / 14 / 40 | 0 | 10 / 11 / 24 | 10 / 0 / 5 |
| DHIB18 / DHIB26 / DWT20 / DU21_h4 / NK6 | 99-220 | > 12 / > 12 / > 12 / 11 / 8 | 11-28 | 0-4 | 51-105 | 6-15 | DHIB26 (25, 24) | 47 | 0-2 | 10-28 | 0-1 |
| CX4, C2CX4, ROUTELOW, RWX, C6G8, GROW7/8, HOLD2K/3K, W14/68/86, m3, m4 | 21-125 | 2 to > 12 | 8-19 | 1-13 | 12-83 | 3-16 | C6G8 (9, 13) | 20 | 0-7 | 8-19 | 0 |
| k1fail_202 | 15 | 1 | 4 | 0 | 1 | 2 | (2, 3) | 3 | 1 | 3 | 1 |
- Readings of the table (DATA, the rows above only): GATE-FLIP is attained exactly (slack 0) on MW, the C-frontier, FW and most climbed
  genomes; on MWR the flipping gate is at 2n + 1 of 3n + 1. Every growing per-gate count (MW, MWR, C-frontier) comes with a face class
  height that grows at the same rate. W ≤ N on every run (max W 10 at N 108, DSALT6); most runs have no quiet step at all.
### 3.2 Random (unit genome / flip; TOTALS)
- out/rnd203_rand_s2.out: 1,000 genomes rand191.rgen (d 1-6, w 1-3, degree 2-3, seed 2): every must-0 counter 0; max flips at one gate 4,
  max D^tot 6 (per interval DE), max T 8, max quiet window 4.
- out/rnd203_k1_s202.out: 5,000 genomes with k = 1 (k1srch202.mk, seed 202, the box 202 generator): every must-0 counter 0; max flips 4,
  max DE 5, max T 8, max quiet window 5.
### 3.3 Controls (each fires)
- check203.out (MWR4_2): GFC_CTRL=1 (π := the e-vertices strictly below e_g) glnfail 4, hfail 1; GFC_CTRL=2 (every interval with a PRIV
  or non-PRIV flip counted) hefail 5; GFC_CTRL=3 (only the e-face's class looked at) lfail 9 = every flip of the gate (5 of them non-PRIV:
  the β-face's class is the one that changes).
- Γ3 (DATA only, no theorem claimed there): out/gfc203_g3.out, N5′-xi from S3 to the first fallback on MWR4_2, MWR8_2, k1fail_202,
  C4_NM50, C6G8_n54, RWX_n95: every must-0 counter 0, the same flip counts as IDEAL-CYC.
- check203.sh (~8 s; wired into experiments/new/check.sh «BOX 203 FLIP»): MWR4_2, MWR8_2, k1fail_202, C4_NM50, the three controls, and
  rnd203 on 100 + 100 genomes, output frozen in check203.out.

## 4. Next (READING)
- Γ3 form: GATE-CLASS needs LOC-GATE3 / NO-TIE3 / B-ONLY on Γ3 (pads of priority ≤ 2, never cycle nodes or in a Π, R117 PAD); then
  QUIET-N on Γ3 up to the first fallback, CONDITIONAL on REACH3-CYC like every Γ3 bound.
- The open core is now one quantity at two vertices: the class height of a gate's faces. At k = 1 a kill needs a face whose e-set takes
  super-linearly many values (R121's ascents); a proof needs a bound on D^tot at k = 1 with U(G) unbounded. MWR's β-face climbs 2n + 2
  classes through 3n + 3 upward Ξ-edges.

## 5. Part 2 (Lead 05:27Z «go»): does k = 1 force the face class height polynomial? (written after the Lead's 05:27Z message, completed 05:35Z by date -u)
Lead 05:27Z: «whether k = 1 forces the face class height (ch(D) / D^tot at gate faces) polynomial via BETA-ACYC on the Ξ-graph minus the
single feedback vertex f — on IDEAL-CYC first; add the cross-reference to L-SI 49's E-FACE-PAYS.»
### 5.0 Verdict
- NOT PROVED, and the natural route is DEAD. What BETA-ACYC's argument gives at k = 1 is a bound on the cycle nodes (Lemma (k+1)-Λ,
  PROVED), not on the e-sets. The e-set route of landed R121 / R123 (HUB-ASC-G, ASC-T) needs boundedly many ascents per play, and k = 1
  does NOT bound ascents: the staircase ST(m) (k = 1) has a play with m − 1 ascents (DEAD: «ascents ≤ k + 1», §5.2). So at k = 1 the face
  class height, and with it GATE-FLIP's bound and T_CYC (QUIET-N), is OPEN; no k = 1 family with super-linear class height is known
  (MWR: linear), and no proof route through ascents exists.
- Cross-reference: L-SI 49 (claude/l-si f723957b, docs/si/box93-k7k6.md §1-§2, + Add. 1 86dd7e02; lane-proved on Γ3 with LOC-GATE3 /
  NO-TIE3): Lemma NP-SHAPE («a non-PRIV state of gate o has Odd on the e-face p_e, and p_b's play = A · o · (p_e's play)») and Corollary
  E-FACE-PAYS («relocks(o) ≤ ch(p_e), unlocks(o) ≤ 1 + ch(p_e)»; flips(g) ≤ 2·min_f ch_f + 1 ≤ 2·lamch(g) + 2·min_f nl_f + 1). Case 2b
  of GATE-CLASS (§1) is NP-SHAPE's first half on IDEAL-CYC. The two bounds are incomparable: E-FACE-PAYS charges BOTH directions to ONE
  face (min) but counts every value change ch_f; GATE-FLIP charges each flip to whichever face changes but counts only (Λ, E)-changes.
  Both reduce the per-gate question at k = 1 to the same open quantity: how often a gate face's value (class) changes.
### 5.1 Lemma (k+1)-Λ (PROVED, lane; IDEAL-CYC, every genome; premises [DEF], R123 B-ONLY and LOC-K2)
At every state t, the cycle nodes Λ_t(v), over all vertices v other than c_W, c_X and the e-vertices whose successor is c_W, take at
most k + 1 values: K1, and the most relevant vertex of each cycle of the functional graph Ξ_σ on the movers (x → xt(x, σ_t(x)), options
with an X target omitted); Ξ_σ has at most k cycles. In particular at k = 1: Λ_t(v) ∈ {K1, c_t} with c_t the top of the unique cycle of
Ξ_σ through the feedback vertex, if there is one.
Proof. Let Z be the cycle of v's play (under σ_t, σ̄_t) and w its most relevant vertex. By B-ONLY w is less relevant than every e-vertex,
so Z has no e-vertex, and Z ≠ {c_W}. If Z meets the core: the play enters the core only at K0 (the β's escape target), and the frozen
edges K0 → K3 → K2 with σ̄(K2) = K1 (LOC-K2) and K1 → K1 lead to the K1 self-loop: w = K1. c_X has no in-edge from another vertex ([DEF]:
an unused self-loop). Otherwise Z consists of movers, gates and β's: a mover x on Z is followed by its gate (x, σ_t(x)), that gate by
its β-face (no e-vertex on Z), that β by its frozen successor xt(x, σ_t(x)) (a mover; an X target would lead to K0). So the movers of Z
form a cycle of Ξ_σ, and Z is determined by it. Ξ_σ has out-degree ≤ 1, so its cycles are vertex-disjoint; each is a cycle of the
Ξ-graph and so meets every feedback vertex set; a minimum one has k elements, so there are at most k cycles. ∎
- This is what «BETA-ACYC on the Ξ-graph minus f» yields: BETA-ACYC's step (3) («a cycle with no e- and no K-vertex is a cycle of the
  Ξ-graph») now leaves at most k cycles instead of none. It controls Λ (at most k + 1 values per state; at k = 1 two), but not E: MWR
  has Λ ≡ K1 on every vertex and state (C = 0) and still 2n + 2 classes at one face.
- DATA (lam203.py; unit: states; counter lfail = states with more than k + 1 values, TOTAL; maxL = max values per state):
  out2/lam203_k1_s7.out 2,000 k = 1 genomes (k1srch202.mk, seed 7): lfail 0, maxL 2; out2/lam203_k2_s8.out 1,000 k = 2 genomes (seed 8):
  lfail 0, maxL 3; out2/lam203_rand_s2.out 1,000 rand191 genomes (d 1-6, w 1-3, degree 2-3, seed 2): lfail 0, maxL 3. Control
  LAM_CTRL=1 (bound k): lfail 3,492 on the k = 1 set (fires).
### 5.2 DEAD: «at k = 1 (more generally, k), every e-sequence has at most k + 1 ascents» (would have given T_CYC polynomial at k = 1 by R123 ASC-T)
- The pattern looked solid on data (asc203.py; unit: max ascents of seq_t(v) over states and vertices, per genome):
  out2/asc203_k1.out 3,000 k = 1 genomes (seed 202): max 1; out2/asc203_k2.out 1,500 k = 2 genomes (seed 203): max 2; out2/asc203_rand.out
  1,000 rand191 genomes: max 3, histogram by k with max ascents ≤ k + 1 in every row; out2/asc203_corpus.out (corpus; PARTIAL at this
  commit: the first 38 genomes in file order, through MW26_2; the rest in a later commit): C-frontier 2, CT27 4, DHIB26 5, MW 2, all ≤ k + 1;
  MWR4_2 2 (check203.out); climbs (aclimb203.py, objective (max ascents, face ascents, T), k = 1 kept): 4 climbs of
  1,275-17,800 iterations from generated k = 1 genomes (N 4-16) stayed at 1 ascent (out2/aclimb203_gen.out; stopped by me after ST(m) killed the target).
- Killed by construction: STAIRCASE ST(m) (stair203.py; frozen inst/ST4_k1.json sha1 3fa71a98, inst/ST8_k1.json sha1 9dbf71f4): movers
  x_i (level i, e-face to y_(i−1), β to the escape), y_j (level j, β-face Ξ-edge up to x_(j+2)), f (Ξ self-loop, odd β of top β-rank).
  The Ξ-graph's only cycle is f's self-loop: k = 1. Odd's play from x_1 reaches f's odd β-cycle (better for Odd than K1) only through
  every e-face of x_1, …, x_m: e(x_1) < e(x_2) < … < e(x_m) under [E-LEV], m − 1 ascents (asc203: ST4 3, ST8 7; ST3 2, ST5 4).
  Exact obstruction: an ascent needs only an upward Ξ-edge (R121 UP-JUMP), and upward Ξ-edges can be acyclic; k counts Ξ-cycles, not
  upward edges. The play is in one state (T = 0: one option per mover), so ST(m) kills the ascent bound, not a class-height bound.
- Consequence: at k = 1, R121's HUB-ASC-G gives D^tot only through a bound on ascents that k does not provide; any proof of polynomial
  face class height at k = 1 must use the run (which classes a face actually visits), not a per-state play shape.
