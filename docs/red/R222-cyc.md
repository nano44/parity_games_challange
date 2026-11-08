# R222 item 1: ρ at CYC-type RET gates (L-RED successor 57)
Lead box R222 item 1 (brief; order after item 2 per Lead 01:54Z). Question: at CYC-type RET gates (Ξ-loops longer than a self-loop) the
β-loop value is not fixed, so R221 RHO-SET (a) does not transfer. Bound ρ_g there, or build a family where it grows.
Labels: PROVED (lane, unrefereed) / PROVED-CONDITIONAL (named premise) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD (instance).
Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1).
Tools: experiments/red/r222/cyc222.py on own.py (R217's independent IDEAL-CYC run). Outputs: experiments/red/r222/out/cyc_*.txt.

## 0. Answer
- BOUNDED, in the same form as R221 RHO-COUNT, with the W-target y replaced by the Ξ-target x′ (Lemma RHO-CYC, §2, PROVED-CONDITIONAL on
  F1 and Odd's optimal response, as RHO-SET is). The β-loop's value never enters the proof.
- ρ_g ≤ 1 + #changes of (Λ(x′), E(x′)) over the run + A′_g ≤ (2M + 3)·F′_B(M) + A′_g.
  - B = the maximum number of ascents of x′'s plays. B ≤ U(G) under [E-LEV] (P-N5-ASC UP-B).
  - A′_g = #RET starts at which Λ_t(x′) is not less relevant than e_g. This is the CYC analogue of RHO-COUNT's A_g, and DATA gives 0
    everywhere.
- So Σρ_g over ALL gates of level ≥ 1, SET and CYC alike, is polynomial when U(G) = O(1) and ΣA′_g is polynomial.
- The CYC part of GATE-POLY's premise «Σρ_g polynomial» (R219, wording kept: «U(G) = O(1) ⇒ polynomial before the first fallback IF
  Σρ_g and ΣH_g are polynomial») now rests on the same open item as the SET part, the A-count. No growing family exists below that
  bound; one would need unbounded U(G) or A′ ≠ 0.
- The RET-start anatomy (§1) shows that RHO-SET (a)'s failure mode is real but rare. A τ-flip with the loop closed can start a RET
  stretch at a CYC gate (15 / 430 in the corpus), and twice the gate's own cycle node did not change. So «C-starts ≤ changes of Λ(g)»
  is FALSE (§1). RHO-CYC does not need it.

## 1. Anatomy of RET starts at CYC gates (DATA)
Setting: g = gate of option k of x, lev(x) ≥ 1, Ξ-target x′ ≠ x, β-vertex b with the single edge b → x′. RET_t ⇔ τ_t(g) = e and the play
from b passes g (R221 rho221.py's definition). A RET start t ≥ 1 is of type:
- A: σ_(t−1)(x) ≠ k (adoption of k at x).
- B: σ_(t−1)(x) = k, but the play from b did not pass g at t − 1 (the loop closes).
- C: σ_(t−1)(x) = k and the loop was closed at t − 1, so τ_(t−1)(g) = β (a τ-flip with a closed loop; impossible at SET gates by
  RHO-SET (a)).
- Cs: a C start with Λ_(t−1)(g) = Λ_t(g).

Unit: RET starts at CYC gates. Scope: own.py. Files: out/cyc_inst.txt, out/cyc_inst_set.txt (both via cyc222.py).
| set | CYC gates with RET | A | B | C | Cs | max ρ_g |
| --- | --- | --- | --- | --- | --- | --- |
| L-RED frozen instances r21*/inst, r22*/inst + R221 climbs r221/out (99 genome files) | 341 | 120 | 309 | 1 | 0 | 7 (R102K6, r221/out) |
| random Ξ-cyclic, brute221.rgen seeds 1, 2 (4,000 genomes) | 1,874 | 688 | 590 | 25 | 0 | 3 |
| random, seeds 11, 12, SET gates included (4,000 genomes) | 3,198 (SET + CYC) | 1,319 | 643 | 14 | 2 | 3 |

The two Cs cases are CYC gates (g = option 1 of mover 7). Frozen as experiments/red/r222/inst/CS_11_526.json and CS_11_1399.json (N 16,
d 4; sha1 in inst/SHA1SUMS).

## 2. Lemma RHO-CYC (PROVED-CONDITIONAL on F1 and Odd's optimal response, lane; new)
Let g, x, k, x′, b be as in §1. Here x′ = x is allowed, so this covers SET gates too.
- [BELOW]_t: Λ_t(x′) is less relevant than e_g.
- A′_g := #{t ≥ 1 : t is a RET start and [BELOW]_t fails}.
- ρ_g := #maximal RET stretches.

(a) e_g ∈ Π_t(x′) implies RET_t. Conversely, RET_t together with [BELOW]_t implies e_g ∈ Π_t(x′).

(b) ρ_g ≤ 1 + #{t ≥ 1 : (Λ_t(x′), E_t(x′)) ≠ (Λ_(t−1)(x′), E_(t−1)(x′))} + A′_g.

(c) Hence ρ_g ≤ (2M + 3)·F′_B(M) + A′_g, where B is the maximum number of ascents of seq_t(x′) over the run. Under [E-LEV], B ≤ U(G).

Proof.
- (a)
  - In Γ(G), e_g's only in-edge is from g, and g's only in-edge is from x ([DEF]).
  - The play from b is b followed by the play from x′. So «the play from b passes g» ⇔ «the play from x′ passes g» (b ≠ g).
  - A play passes e_g iff it passes g while Odd takes e there.
  - If e_g ∈ Π_t(x′), then x′'s play passes g with τ_t(g) = e, which is RET_t.
  - Conversely, under RET_t, x′'s play passes g and then e_g. A play vertex more relevant than its cycle node lies in Π: vertices of the
    cycle other than Λ are less relevant than Λ, P-N5-ASC [VJ]. Under [BELOW]_t, e_g is more relevant than Λ_t(x′), so e_g ∈ Π_t(x′).
- (b)
  - Let t ≥ 1 be a RET start with [BELOW]_t.
  - By (a), e_g ∈ Π_t(x′). Also ¬RET_(t−1), so by (a) e_g ∉ Π_(t−1)(x′).
  - So either Λ(x′) changes at t, or Λ(x′) stays the same and E(x′) gains e_g, an e-vertex. Either way the pair changes at t.
  - Distinct starts are distinct times t. Add at most 1 for a stretch that contains t = 0, and A′_g for the starts without [BELOW].
- (c)
  - By R118 (e) (per-vertex form, quoted in P-N5-ASC §1), Λ(x′) changes at most 2M + 2 times.
  - On each interval I with Λ(x′) constant, E(x′) is lex non-decreasing (E-MON). So it changes at most D_E,I(x′) − 1 times, and
    D_E,I(x′) ≤ F′_B(M) by Corollary HUB-ASC-G.
  - Summing over the ≤ 2M + 3 intervals gives (2M + 2) + (2M + 3)(F′_B(M) − 1) + 1 ≤ (2M + 3)·F′_B(M).
  - Under [E-LEV], UP-B gives B ≤ U(G). ∎

Remarks:
- No property of the β-loop is used. The loop can grow, shrink, open, close, or switch its top. Every RET start is still paid for by x′
  gaining e_g.
- For SET gates (x′ = x), (b) reads ρ_g ≤ 1 + #changes of (Λ(x), E(x)) + A′_g. That is a second bound, next to RHO-COUNT's version with y.
- A′_g needs x′'s cycle node to be an e-vertex at least as relevant as e_g, or c_W (K0 / K3 are never cycle nodes). In words: the
  W-side of g ends in a cycle above e_g. That is the same shape as RHO-COUNT's A_g. No bound on it is proved here.

DATA for RHO-CYC (cyc222.py: rviol = #gates with ρ_g > 1 + chg + A′; ing = #(t, g) with [BELOW]_t and RET_t ≠ [e_g ∈ Π_t(x′)];
unit: gates of level ≥ 1 with a RET; set and scope as in §1):
| set | gates | Σρ_g | rviol | ing | A′ | gates with slack 0 |
| --- | --- | --- | --- | --- | --- | --- |
| frozen + climbs, CYC only (out/cyc_inst.txt) | 341 | 458 | 0 | 0 | 0 | the bound is attained in 4 files |
| frozen + climbs, SET and CYC (out/cyc_inst_set.txt) | 952 | 1,221 | 0 | 0 | 0 | attained in 28 files |
| random seeds 1, 2, 11, 12 (8,000 genomes) | 5,072 | | 0 | 0 | 0 | |

The bound in (b) is attained on real runs, so (b) cannot be improved by a constant factor in general.

## 3. Where this leaves Σρ (READING)
- SET gates: RHO-COUNT (y) and RHO-CYC (x′ = x). CYC gates: RHO-CYC (x′). Both are polynomial for U(G) = O(1), given ΣA_g and ΣA′_g.
- The A-counts remain the open premise: RET starts where the gate's W-side or Ξ-side ends in a cycle above e_g.
- Item 2 (R222-lockup.md §3) reached the same place from the other side. Under bounded U(G), a SET bit can flip often only through Λ
  changes, or through a play that returns to the bit (PRIV fails).
- A CYC gate IS such a returning play. RHO-CYC says its RET stretches are still paid for by the Ξ-target's e-set changes. So the
  returning play does not escape the e-set accounting at the gate level.
- Whether it escapes at the mover level (bit flips of x when PRIV fails) is OPEN. That is the next question, and the natural target
  for L-SI's hub-pair candidate.

## 5. A′_g = 0 (Lead 02:56Z: prove it or break it): PROVED-CONDITIONAL on [OPT], via R221 Lemma B-ONLY
**Corollary RHO-CYC-0 (PROVED-CONDITIONAL on F1 and [OPT], lane; [OPT] is the standing premise of R57 (b), Lead reading).** In
IDEAL-CYC(G), for every genome G and every gate g of level ≥ 1 whose Ξ-target x′ is a mover:
- A′_g = 0, and ρ_g ≤ 1 + #changes of (Λ(x′), E(x′)) ≤ (M + 3)·F′_B(M);
- B is the maximum number of ascents of seq_t(x′), and B ≤ U(G) under [E-LEV].

Proof.
- x′ is a mover: not c_W, and not an e-vertex.
- So by B-ONLY (R221-quiet.md §3, PROVED lane, from [OPT] and [XICYC-a]), Λ_t(x′) is a β-vertex, K1, K2 or c_X at every state t.
- Each of these is less relevant than every e-vertex ([DEF]: e-vertices lie above every β, K1 = 5, K2 = 3, c_X = 2).
- So [BELOW]_t holds at every t, and A′_g = 0 by definition.
- B-ONLY also says Λ(x′) ranges over at most M + 3 values (the β's, K1, K2, c_X). R118 (e)'s monotonicity makes these changes strictly
  rising in reward, so there are at most M + 2 of them.
- Insert both facts into RHO-CYC (b), (c): 1 + (M + 2) + (M + 3)(F′_B(M) − 1) ≤ (M + 3)·F′_B(M). ∎

Remarks:
- If the Ξ-target is −1 (u = K0), the β-play enters the closed core and never returns to g. Such a gate has no RET, so it is not counted.
- This is the same step R221-quiet.md §3 used for RHO-COUNT's A_g (= 0). Hence, for IDEAL-CYC under [OPT]: Σρ_g over ALL gates of
  level ≥ 1 is at most M·(M + 3)·F′_U(G)(M) under [E-LEV]. That is polynomial for U(G) = O(1), with NO open A-premise left in the
  gate-flip accounting.
- What this does NOT cover:
  - N5′-xi on Γ3 itself: its mover phase equals Howard on IDEAL-CYC only before the first fallback (R118 (d), REACH3-CYC CONDITIONAL).
  - Unbounded U(G).
  - Mover-level flips when PRIV fails (R222-lockup.md §3).
- DATA (§2): A′ = 0 on all 6,024 gates measured. That agrees with the proof; it adds nothing to it.

## 6. Consolidated lemma list for the gate / bit accounting (Lead 03:15Z: packet-ready form)
Scope of every item: runs of IDEAL-CYC(G) for an arbitrary genome G (RESULTS R104 format, Γ(G) as P-N5-XICYC [DEF]). Howard at the movers
(best option, ties keep the current one). Odd's counterstrategy σ̄_t is optimal. Values [VJ] (Λ, Π, k).
Nothing here is about N5′-xi on Γ3 beyond the first fallback. G-N5-TIME stays OPEN.

Premises, named once and cited by tag below:
- [F1] R118 (b) Fact F1: Ω_t(v) ⊴ Ω_(t+1)(v) for every vertex v. LANDED.
- [R118e] R118 (e): «C ≤ n·(2M + 2)», with its reason «(each vertex's Λ moves only to a vertex of strictly larger reward among at most
  2M + 3 possible cycle nodes)». Used in the per-vertex form. LANDED.
- [XICYC-a] R118 (a): Odd is unrestricted at gates and at K2 in IDEAL-CYC. LANDED.
- [DEF] P-N5-XICYC [DEF] priorities: movers 0, gates 1, c_X 2, K2 3, K1 5, β ≥ 6, e-vertices above every β, c_W above those, K0 = top + 2,
  K3 = top + 3. Edges: e_g's only in-edge is from g, g's only in-edge is from its mover, K0 → K3 → K2 is frozen. In R104 / R118.
- [OPT] the pointwise optimum: one σ̄_t is ⊴-minimal at every vertex at once. Lead reading 03:15Z: this is RESULTS R57 (b)'s standing
  SPEC premise, quoted verbatim from trunk docs/RESULTS.md l. 2915: «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC
  conformance». Every packet using an item below must cite that clause and name it as the standing premise.
- [E-LEV] e-priorities increase with the level of the gate's mover. Not landed; a HYPOTHESIS wherever it is used.
- Lane results used: E-MON, HUB-ASC-G, UP-B from P-N5-ASC (claude/l-new 95dc76d7 §3, §5, §6; both referees SIGN, landing as R121 per the
  Lead's brief); B-ONLY from R221-quiet.md §3.

| # | name | statement (short) | premises | where | status |
| --- | --- | --- | --- | --- | --- |
| 1 | B-ONLY | for every v ≠ c_W, and every v that is not an e-vertex with W-target c_W: Λ_t(v) ∈ {β's, K1, K2, c_X}, below every e-vertex; Λ_t(v) takes ≤ M + 3 values | [OPT], [XICYC-a], [DEF] | R221-quiet.md §3 | PROVED (lane) |
| 2 | no gate ties | Ω_t(e_g) ≠ Ω_t(β_g) at every gate and every state | 1 | R221-quiet.md §3 | PROVED (lane) |
| 3 | RHO-SET | at a SET gate a RET stretch after the first starts with an adoption; ρ_g ≤ D(y) | [F1], Odd optimal | R221-ladder.md §7 | PROVED-COND (lane) |
| 4 | RHO-E / RHO-COUNT | SET gate: ρ_g ≤ 1 + #changes (Λ(y), E(y)) + A_g ≤ (2M + 3)F′_B(M) + A_g; A_g = 0 by 1 | [F1], E-MON, HUB-ASC-G, 1 | R221-ladder.md §7, R221-quiet.md §3 | PROVED-COND (lane) |
| 5 | RHO-CYC | ANY gate of level ≥ 1 whose Ξ-target x′ is a mover: (a) RET_t ⇔ e_g ∈ Π_t(x′) under [BELOW]_t; (b) ρ_g ≤ 1 + #changes (Λ(x′), E(x′)) + A′_g | [F1], [R118e], E-MON, HUB-ASC-G, [DEF] | this file §2 | PROVED-COND (lane) |
| 6 | RHO-CYC-0 | A′_g = 0, ρ_g ≤ (M + 3)·F′_B(M) with B = max ascents of x′'s plays; Σρ_g ≤ M(M + 3)F′_U(G)(M) under [E-LEV] | 5, 1, UP-B | this file §5 | PROVED-COND (lane; [F1] + [OPT]) |
| 7 | PRIV-FLIP | SET-type option S of mover B on a Λ-interval I with Λ(B) ∈ {K1, K2} and PRIV (no play from S's W-target or from B's other gates passes B): #changes of [σ(B) = S] ≤ 1 + Σ_{v ∈ {w} ∪ {g_o}} (D_E,I(v) − 1) | [F1], Odd optimal, E-MON, [DEF], Howard best switch | R222-lockup.md §3 | PROVED (lane) |
| 8 | PRIV-POLY | 7 + HUB-ASC-G / UP-B: per Λ-interval ≤ 1 + deg(B)(F′_B(M) − 1); over the run polynomial for bounded U(G) under [E-LEV] | 7, HUB-ASC-G, UP-B, [R118e] | R222-lockup.md §3 | PROVED (lane) |
| 9 | (DEAD) | «a RET start by a τ-flip with a closed loop changes Λ(g)» | — | this file §1 | DEAD: inst/CS_11_526.json (sha1 047bd550…), CS_11_1399.json (5ec8880b…) |

Remarks for a packet writer:
- Item 7's Λ(B) ∈ {K1, K2}: B-ONLY (1) allows a β or c_X as cycle node too. Item 7's proof needs only that λ is less relevant than β_S,
  and that g_S and B are not in Π. That holds for c_X (2) as well. For λ = a β-vertex it fails when β_S is less relevant than λ. So do
  not widen the hypothesis without that check.
- Items 4 and 6 bound RET STRETCHES. Item 2 says every face flip is a strict ⊴-comparison. Neither bounds Howard's iteration count by
  itself: GATE-POLY (R219) still needs ΣH_g (H_g = 0 by 1, R221-quiet.md §3) and the P-step accounting (box 194 QUIET / T-QUIET,
  SURVIVES).
- Item 7 is the only one about Even's choices. It does not cover a bit whose own option's play returns to it (PRIV fails). That case is
  OPEN, and it is where an exponential SET counter would have to live under bounded U(G).
- DATA backing: §1-§2 of this file; R222-lockup.md §2-§3; R221-ladder.md §7-§8; R221-quiet.md §3. No referee has seen items 5-8.

## 7. Sources opened
- trunk claude/vibrant-johnson-nxvvxo docs/RESULTS.md l. 2913-2916 (R57 (b) standing premise, verbatim), l. 2893 (R57 title).
- claude/l-red docs/red/R221-quiet.md §1 ([OPT] status), §3 (Lemma B-ONLY).
- claude/l-new 95dc76d7 docs/new/P-N5-ASC.md §1 (R118 (e) per-vertex form, [VJ] Π), §3 (E-MON), §5 (HUB-ASC-G), §6 (UP-B).
- claude/l-red docs/red/R221-ladder.md §7 (RHO-SET, RHO-E, RHO-COUNT), experiments/red/r221/rho221.py (RET definition),
  experiments/red/r221q/brute221.py (rgen).
