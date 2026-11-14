# Box 81 BRIDGE: the tower route (N5, R104 / R117) and the N5′-xi route (R118, box 193) on the same genomes
L-SI successor 43 (Opus 5.5), under D18 / D14 / D1. Lead GO 21:52Z (2026-11-07). Written from 21:55Z (date -u; see the commits).
Labels: PROVED (lane, unrefereed) / PROVED-CONDITIONAL (on named premises) / CONJECTURE / DATA (counter: unit, set, scope) / DEAD /
READING (not to sign). Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1). No bound on N5 is
claimed. Tools, pins and frozen outputs: experiments/si/box81/ (check81.sh, wired into experiments/si/check.sh).

## 0. Answer (milestone 1)
- **The two routes are about two different S4a tie rules on the same games.** They cannot contradict each other on tower genomes, and the
  tower route cannot reach N5′-xi:
  - PROVED (lane, §3, Lemma BETA-ACYC + Theorem ACYC-LIN): on EVERY Ξ-acyclic genome, in IDEAL-CYC(G) from any mover state, Odd's
    optimal counterstrategy takes the β-face at every gate, no play contains an e-vertex, every cycle node is constant, and the Howard
    run has C = R = 0 and T_CYC ≤ N.
  - PROVED-CONDITIONAL (§3, Corollary ACYC-XI): N5′-xi from S3 on Γ3(G) has its first fallback at iteration T3 + 1 ≤ N + 1. The
    condition is R118's REACH3-CYC, whose premises R117's entry signs for acyclic Ξ-graphs.
  - Every tower genome of the R104 model is Ξ-acyclic (R104 requires it; DATA below for the four towers). So a tower's T says nothing
    about N5′-xi's R: R = 0 on all of them, whatever T is. A tower with R growing in its height is impossible (PROVED). The «news»
    case of the brief cannot occur.
- DATA, the census (§2): on the four towers (SL41, H5_d20_F62, H6_d24_F126, L6Z_KILL238) IDEAL-CYC Howard has T 9-12, C 0, R 0,
  0 ascents in every play, and e-set height 1. N5 (SPEC) on the same Γ3(G) from S3 reproduces each tower's T exactly (136, 209, 290,
  283), state for state; N5′-xi takes 12-15 iterations.
- DATA: on the eight library instances every play has ≤ 1 ascent (box 193's ASC1 hypothesis holds), R 2-8, e-set height ≤ 7.
  UP-B, HUB-ASC-G, OVT-DV and R-SPLIT are never violated (0 failures).
- Step 3 of the brief (extract a ≥ 2-ascent gadget from the towers) is NOT TRIGGERED: the towers have no ascents at all. No gadget is
  handed on. The ≥ 2-ascent plays of the fleet live in L-NEW's other instances (box 193 §4: rd2_d9, rd3_d7, RS3, FPORT_n3, …), not in
  towers.
- READING: the tower family measures only N5's root-first-key tie rule in a regime where Odd's choice is frozen (one-player in
  effect). N5′-xi's Ξσ tie rule is exactly Howard there (REACH3-CYC), and Howard is linear in N on that regime. So the bridge
  measurement is complete and says the routes are independent: neither can inform the other's open core.

## 1. What each route bounds (from the landed RESULTS text)
- **Tower route = N5 with SPEC's S4a tie rule** (root-first key; R104's IDEAL step «moves every mover to the lexicographically least key
  (gate indices of the chain of W-targets under the new state, lowest level first) among its current option and the options with a
  strictly better Ξ-value»).
  - R104 (Theorem REALIZE, acyclic Ξ-graphs only): N5 on Γ(G) from R104's stated start has an FL run of length exactly L(G) = T, with
    «Odd's optimal counterstrategy on the β-face at every gate (strict local preference), τ unchanged».
  - R117 (Theorem REACH3, acyclic Ξ-graphs): «the N5 run of Γ3(G) FROM S3 has states 0, …, L(G) equal to the transported REALIZE
    states of the IDEAL run».
  - Both are «a REDUCTION / NECESSITY statement only (no count is bounded …; Ξ-cyclic genomes are not covered)».
  - So the tower route, if S(h) is polynomial, gives super-polynomially long N5 runs from S3 (R117 Corollary REAL-IDEAL-S3).
- **N5′-xi route = N5 with S4a's TIE broken by the best Ξσ value** (box 190's mode "xi": «S4a's TIE … broken by the BEST Xi_sigma value
  (ties: SPEC's choice, then larger index)»).
  - R118 (RED-XI, REACH3-CYC): N5′-xi from S3 on Γ3(G) «visits only standard states and makes Howard steps at the movers until its first
    fallback, at iteration T3 + 1 with T3 ≤ C + R + (C + R + 1)·N». «no bound on R is claimed (OPEN)».
  - Howard's tie rule (R118 (a)): «every mover x goes to a successor of ⊴-largest Ω_t value, and keeps σ_t(x) if σ_t(x) is such a
    successor»; idealcyc.py breaks the remaining tie by the larger index.
  - R counts the steps labelled R: «else R if σ̄_t(v) ≠ σ̄_(t+1)(v) for some Odd vertex v». σ̄ is «any fixed deterministic choice»; here
    it is si.py Engine's choice (the R118 reference). My independent implementation (§4) picks its own σ̄ and gets the same labels on
    all 10 xcheck instances.
  - ASC1 / HUB-ASC-G / UP-B (box 193 Addenda 2, 4; PROVED (lane), unrefereed) bound the e-set height D_E,I(v) of THIS run.
  - Bounding R needs more than that. The chain is OVT-DV and R-SPLIT (PROVED-CONDITIONAL on [LOC]), plus CONJECTURE IN-BOUND (D(v) ≤
    (IN + 1)·D_E(v)), plus Σ L_g polynomial (box 192 §2, A10; box 193 §2 Remarks). So «ASC1 + OVT-DV bound R» is conditional on IN-BOUND,
    [LOC] and Σ L_g. I checked each inequality of the chain on the data (§2); IN-BOUND itself is not checked here.
- Definitions used in the census, quoted from box 193 (claude/l-new 9cdb7209):
  - «seq_t(v) := the e-vertices of Π_t(v) in play order»;
  - «consecutive a, b in seq_t(v) with rank(b) > rank(a) (an ascent)»;
  - e-set height D_E,I(v) := the number of distinct e-parts E_t(v) while Λ_t(v) = w (Corollary ASC1);
  - «U(G) be the number of strictly upward Ξ-edges of G (options (x, k) whose Ξ-target is a mover of level > lev(x))».

## 2. Census (DATA)
Counters (census81.py; L-NEW's runners as byte copies, ref/, pinned in ref.sha1). Unit: play = the play from vertex v at state t, under
(σ_t, σ̄_t). Set: all (state, vertex) pairs of the run. Scope: IDEAL-CYC(G) Howard from the genome's stored start, i.e. R104's stated
start. Real runs (real81.py): N5′-xi («xi») and N5 («spec») on Γ3(G) from S3; iterations / T3 (mover phase: transitions keeping τ and every
non-mover, non-β Even vertex).

| instance | N | M | Ξ-acyc | T_CYC | C | R | R_mov | U(G) | max asc | plays by #ascents | max D_E per Λ | max D_E(v) | max D(v) | max gate flips | xi iters / T3 | spec iters / T3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rd2_d3 | 6 | 12 | no | 9 | 3 | 5 | 5 | 4 | 1 | 464 / 16 | 3 | 6 | 7 | 3 | 12 / 9 | 6 / 3 |
| rd2_d4 | 8 | 16 | no | 11 | 3 | 8 | 8 | 6 | 1 | 688 / 56 | 7 | 12 | 12 | 6 | 14 / 11 | 7 / 4 |
| rd3_d3 | 6 | 15 | no | 12 | 3 | 4 | 4 | 5 | 1 | 739 / 2 | 2 | 7 | 9 | 4 | 15 / 12 | 5 / 2 |
| rf_d4 | 8 | 16 | no | 12 | 6 | 4 | 4 | 6 | 1 | 772 / 34 | 3 | 11 | 12 | 7 | 15 / 12 | 4 / 1 |
| RS2 | 18 | 30 | no | 10 | 0 | 4 | 4 | 4 | 1 | 1249 / 5 | 4 | 4 | 7 | 3 | 13 / 10 | 4 / 1 |
| RS2_L8M6 | 29 | 52 | no | 17 | 0 | 4 | 4 | 7 | 1 | 3433 / 5 | 4 | 4 | 11 | 3 | 20 / 17 | 4 / 1 |
| RSG_K4 | 14 | 23 | no | 7 | 0 | 2 | 2 | 1 | 1 | 548 / 164 | 7 | 7 | 7 | 1 | 10 / 7 | 4 / 1 |
| FPORT_n2 | 54 | 92 | no | 14 | 0 | 3 | 3 | 4 | 1 | 4122 / 918 | 4 | 4 | 15 | 1 | 17 / 14 | 5 / 2 |
| H5_d20_F62 | 40 | 80 | yes | 9 | 0 | 0 | 0 | 33 | 0 | 2860 / 0 | 1 | 1 | 9 | 0 | 12 / 9 | 139 / 136 |
| H6_d24_F126 | 48 | 96 | yes | 12 | 0 | 0 | 0 | 42 | 0 | 4446 / 0 | 1 | 1 | 12 | 0 | 15 / 12 | 212 / 209 |
| SL41_d28 | 56 | 112 | yes | 10 | 0 | 0 | 0 | 48 | 0 | 4378 / 0 | 1 | 1 | 10 | 0 | 13 / 10 | 293 / 290 |
| L6Z_KILL238_d28 | 56 | 112 | yes | 9 | 0 | 0 | 0 | 49 | 0 | 3980 / 0 | 1 | 1 | 8 | 0 | 12 / 9 | 286 / 283 |

- Columns (per instance; unit, set and scope as above unless named):
  - «plays by #ascents»: plays with 0 / 1 ascents; no play has ≥ 2.
  - «max D_E per Λ»: max over (v, w) of distinct e-parts of v while Λ(v) = w (box 193's maxDE).
  - «max D_E(v)»: max over v of distinct (Λ, e-part) pairs over the run. «max D(v)»: distinct values.
  - «max gate flips»: max over gates of the number of steps where σ̄ changes there.
  - R_mov: R-steps that change σ̄ at a gate whose Ξ-target is a mover (box 192 R-SPLIT).
- Checks, all instances (census81.py; unit as named; set: the 12 rows; scope: IDEAL-CYC):
  - UP-B (max ascents ≤ U(G)): 0 violations.
  - HUB-ASC-G: per (v, Λ)-interval, distinct e-parts ≤ F′_B(M_w), with B the max ascents of v's plays there and M_w the e's above w;
    hubfail 0.
  - OVT-DV: flips(g) ≤ 2·min(D(e_g), D(β_g)) − 1 over the whole run; every face tie count L_g = 0, so the tie-free form applies to
    every gate; ovtfail 0.
  - R-SPLIT: R ≤ R_mov + Σ over X-gates of (4M + 5 + L_g); 0 violations.
  - E-DOM, CHAIN-DECOMP, TAIL-MON: not re-counted here. L-NEW's asc193.py gives 0 on its instances; this lane re-ran it on RS2, rd2_d3
    and rd3_d3 (scratch; same maxasc / maxDE as this census).
- The library rows match box 193's own numbers where box 193 reports them (RS2_L8M6: max ascents 1, max D_E per Λ 4; the ASC1 list
  «rd2_d3, rd2_d4, rd3_d3, rf_d4, RS2, RS2_L8M6, RSG_K4 and FPORT_n2 (max ascents per play 1)»; RSG_K4: U 1, max 1).
- Real runners vs the model (real81.py; unit: states; set: the 12 instances; scope: Γ3(G) from S3):
  - the N5′-xi mover phase equals the IDEAL-CYC Howard run state for state, with T3 = T_CYC, in 12 of 12 (REACH3-CYC's prediction);
  - the first fallback is at T3 + 1, and the run ends after T3 + 3 iterations, in 12 of 12.
- Tower T reproduced: N5 (spec) from R104's STATED start on Γ(G) (no pads) and from S3 on Γ3(G) both give T3 = T, with mover states
  equal to the R104 IDEAL run (box 80 sim80.Sim), in 4 of 4 towers (out/stated_*.out, out/real_*.out). Tower T and capped levels by
  sim80.py: H5 T 136, 5 capped; H6 T 209, 6; SL41 T 290, 6 (F(6) 222); L6Z_KILL238 T 283, 6 (F(6) 238, as the Lead's brief states).

## 3. The acyclic regime: Lemma BETA-ACYC, Theorem ACYC-LIN, Corollary ACYC-XI
Setting: IDEAL-CYC(G) as in R118 (a): Γ(G) of R104 with every non-mover Even vertex frozen at R104's start, i.e. β_g → its Ξ-target
(u = K0 when the target is X), K0 → K3, K1 → K1, K3 → K2, e_g → its only successor. Movers have any fixed strategy σ; Odd (gates, K2)
is free. Values (Λ, Π, k) and ⊴ as in R118 [VJ]. Ξ-graph: x → xt(x, k) for every option whose Ξ-target is a mover (R104).
Facts used (all from R104's definition of Γ(G), quoted in §1 and in RESULTS R104):
- [RANK] e-vertices have even priority above every β, gate and mover; only c_W (even), K0 (even) and K3 (odd) lie above the e's (R104
  «e of even priority above every β»; c_W top, K0 top + 2, K3 top + 3; box 193 §1 E-DOM-ALL-d, checked there by DATA). K1 (5) and
  K2 (3) lie below every β (6 + 2·rank + parity ≥ 6).
- [CORE] the K-core is entered only at u = K0 (no other vertex has an edge to K1, K2 or K3), and K0 → K3 → K2 are frozen.
- [cX] the unused loop has no in-edge.
- [OPT] σ̄ is an optimal counterstrategy: for every Odd strategy τ and every vertex v, Ω_σ̄(v) ⊴ Ω_τ(v), where Ω_τ is the value of the
  (σ, τ)-play (VJ00 §4.2 / R118 [VJ]: «Odd's optimal counterstrategy»).

**Lemma BETA-ACYC (PROVED, lane).** Let G be Ξ-acyclic, σ any mover strategy of IDEAL-CYC(G), and σ̄ any optimal counterstrategy.
Then σ̄(g) = β_g at every gate g. Moreover, under (σ, σ̄) no play contains an e-vertex in its prefix, except the plays that start at an
e-vertex.
Proof.
- Let τ′ := σ̄ changed to β at every gate (σ̄(K2) kept).
- Under (σ, τ′), the play from any gate g goes g → β_g → x′ := xt(β_g) → gate (x′, σ(x′)) → β → … . Each step from a β to a mover
  follows a Ξ-edge, and the Ξ-graph is acyclic, so the movers on it are distinct. So the play reaches a β whose Ξ-target is X, then
  u = K0 → K3 → K2 → σ̄(K2), and ends in the K1 loop or the K2 loop.
- Its cycle node is w* := K1 if σ̄(K2) = K1, else K2. Its prefix contains K0 and K3 (both above w*). It contains no e-vertex and not
  c_W.
- Now suppose σ̄(g) = e_g and let π be the (σ, σ̄)-play from g, with cycle node w.
  - Which cycles can π end in? c_W's loop; the K1 or K2 loop; or a cycle through movers, gates, β's and e's (cX is never entered, [cX]).
  - A cycle that contains no e uses only mover → gate → β → mover steps, i.e. Ξ-edges: impossible (acyclic).
  - A cycle through an e has an e or c_W as its most relevant vertex. That is even and above K1, K2 [RANK], so its reward beats w*'s.
  - Likewise if w = c_W.
  - In all these cases Ω_σ̄(g) ▷ Ω_τ′(g), contradicting [OPT].
- So w ∈ {K1, K2}. Then π enters the core at u [CORE], runs K0 → K3 → K2 → σ̄(K2), and w = w*. Both plays have cycle node w* and
  contain K0 and K3; neither contains c_W (c_W occurs only as a cycle node).
- π contains e_g, which is above w*. The play from τ′ contains no e.
- So the most relevant vertex of the symmetric difference of the two Π-sets is an e-vertex of π [RANK]. It is even, so
  Ω_σ̄(g) ▷ Ω_τ′(g), contradicting [OPT].
- Hence σ̄(g) = β_g at every gate, i.e. σ̄ = τ′ at the gates, and the plays are those of the first bullets. A play from a vertex other than
  an e-vertex never passes a gate's e-face, so it contains no e. ∎

**Lemma LAMBDA-CONST (PROVED, lane).** Under the hypotheses of BETA-ACYC, Λ(v) does not depend on σ: it is c_W for v = c_W and for the
e-vertices of level-0 options (whose successor is c_W), cX for cX, and w* for every other vertex.
- w* does not depend on σ: K2's two plays (K2 → K1 → K1 loop and K2's own loop) do not depend on σ, so neither does Odd's optimal choice
  at K2.
- Proof of the rest: by the play description in BETA-ACYC. An e-vertex of a level-ℓ option with ℓ ≥ 1 goes to a mover, and from there
  as above. ∎

**Theorem ACYC-LIN (PROVED, lane).** For every Ξ-acyclic genome G and every start mover state, the Howard run of IDEAL-CYC(G) has C = 0,
R = 0 and T_CYC ≤ N. With R104's stated start, the label sequence is p^T.
Proof.
- By LAMBDA-CONST no step changes a cycle node: C = 0.
- By BETA-ACYC, σ̄ is β at every gate in every state. At K2 it is the σ-independent optimal choice; for a fixed deterministic rule it
  is constant. So R = 0, and every step is a p-step.
- R118 (d), Theorem BR-SEG: «every maximal run of consecutive p-steps has at most N steps». The whole run is one p-run, so T_CYC ≤ N. ∎
- Remark: this is R118's Corollary ONEP-POLY's regime (gates on the β-face) reached without restricting the game. For acyclic genomes
  Odd chooses β anyway. The bound N is sharper than ONEP-POLY's, because C = 0 here.

**Corollary ACYC-XI (PROVED-CONDITIONAL on R118's Theorem REACH3-CYC for acyclic Ξ-graphs).** For every Ξ-acyclic genome, N5′-xi from S3
on Γ3(G) makes Howard steps at the movers until its first fallback, at iteration T3 + 1 ≤ N + 1.
- REACH3-CYC's premises, as R118 states them: «P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3 for every genome (RESULTS R117's entry
  signs S3-START, PAD, K3 and TAU3 for every genome and ESC3, W3 for acyclic Ξ-graphs …)», σ̄(K2) = r (proved in P-N5-XICYC's fixes), and
  «the landed premise [1E-N3]».
- For acyclic genomes every premise is signed in R117's entry or landed. R117's line states S3-START and PAD for acyclic Ξ-graphs only,
  which covers this case.
- Then T3 = T_CYC ≤ N by ACYC-LIN.
- Nothing is claimed about the iterations after the first fallback. DATA: 2 more on all 12 instances, total T3 + 3.
- Consequence for the tower route (READING of PROVED statements): R104's IDEAL model needs acyclic Ξ-graphs, so every tower genome lies
  in this regime. Under the condition, N5′-xi's mover phase on every tower is ≤ N, whatever the tower's T. The tower program can give a
  lower bound for N5 only. Its relevance to N5′-xi is nil, and the ASC / OVT route is vacuous on towers (no e on any play).

DATA (lemma81.py; unit: (state, gate) pairs for notbeta / nonstrict, steps for C / R, runs for T > N; scope: IDEAL-CYC Howard from the
stored start):
- Set A: 300 Ξ-acyclic random genomes (own generator agen, the rand191 shape: d 1-6, w 1-3, degree 2-3, seed 7; 768 states). σ̄ off the
  β-face 0; β-face not strictly better for Odd 0; C 0; R 0; runs with T > N 0. Max T/N 1.0, so the bound T ≤ N is reached.
- Set B: the 4 towers (44 states): all counters 0, max T/N 0.25.
- Negative control, set C: 5 Ξ-cyclic library genomes (59 states). σ̄ off β 121, not strict 121, C 15, R 25, T > N in 4 of 5. So the
  counters fire, and acyclicity is what the lemma needs.

## 4. Cross-check against an independent implementation (DATA)
- xchk81.py shares no code with ref/ or si.py:
  - it builds Γ(G) from R104's text;
  - it computes Odd's optimal counterstrategy by Odd switch-all policy iteration, with plays evaluated explicitly on the functional
    graph and its own ⊴;
  - it runs Howard with R118's tie rule;
  - it computes the ascents from its own plays.
- Unit: instances (for each: the whole game, the whole state sequence, every value at every state, the ascent histogram over all plays,
  the C/R/p label string). Set: rd2_d3, rd2_d4, rd3_d3, rf_d4, RS2, RSG_K4, RS2_L8M6, H5_d20_F62, H6_d24_F126, L6Z_KILL238_d28.
  Scope: IDEAL-CYC from the stored start.
- Result: game SAME, states SAME, value differences 0, histograms SAME, labels SAME (so R agrees too) in 10 of 10 (out/xchk_*.out).
- The real runner (N5′-xi, box 190 n5v.py) is a second, separate implementation of the mover phase. It agrees with idealcyc on 12 of 12
  (§2).
- Oink: NOT RUN (not built in this container). Solution correctness of the real runs is not checked here.

## 5. Frozen inputs (copies + sha1; experiments/si/box81/inst.sha1, ref.sha1)
- Library (L-NEW claude/l-new 9cdb7209, sha1s equal to L-NEW's own SHA1SUMS):
  - box192/inst: rd2_d3 1605f24b…, rd2_d4 51ebb242…, rd3_d3 9fc8c62d…, rf_d4 14b8c77c…;
  - box193/inst: RS2 e8fff77e…, RS2_L8M6 982d5911…, RSG_K4 e3626d62…, FPORT_n2 4ef73ca1….
- Towers:
  - H5_d20_F62.json 2204079d… and H6_d24_F126.json fb37fec9…: claude/l-lower 5158ba4e, experiments/lower/l4/rec/; equal to
    box79/inst.
  - SL41_d28.txt c1b46c31…: claude/l-lower 5158ba4e, experiments/lower/l5/rec/.
  - L6Z_KILL238_d28.txt 54450906…: claude/l-comp efdd6010, experiments/comp/box30/out/; the Lead's quoted sha1.
  - The .txt files are mapped to genome JSON by box80/j2t.py's t2j (the 𝓛^R_d layout: W-pointer of mover x is 2(⌊x/2⌋ − 1) + k).
    SL41_d28.json 93eff94d…, L6Z_KILL238_d28.json 71c81450….
  - sim80.py on the JSON reproduces the towers' T and F (§2), so the map is the one the tower lanes use.
- Runners (ref/, byte copies of claude/l-new 9cdb7209; each compared with `git show` there): box189/gamma3.py, box191/{idealcyc,
  subrun191, rand191, trace191}.py, box193/{asc193, ug193}.py, box190/n5v.py, box21/n5x.py, n5.py, si/si.py, harness/pg.py. si.py and
  pg.py are also byte-equal to this branch's own experiments/si/si.py and experiments/harness/pg.py.

## 6. Open, and what this does not say
- Not said: anything about N5's running time; anything about Ξ-cyclic genomes beyond the census rows; anything after N5′-xi's first
  fallback.
- For the N5′-xi route the open core is unchanged: plays with ω(1) ascents (box 193 A4), CONJECTURE IN-BOUND, [LOC], and Σ L_g.
  Every candidate counter must be Ξ-cyclic (ACYC-LIN): with an acyclic Ξ-graph, R = 0. So L-RED's counter designs must use Ξ-cycles. They
  do: every library instance with R > 0 is Ξ-cyclic.
- READING: Corollary NOUP (box 193) excludes upward Ξ-edges, and ACYC-LIN excludes Ξ-cycles. A super-polynomial R needs both: some
  Ξ-cycle (for R > 0 at all) and growing ascents per play, hence many upward Ξ-edges on one play (UP-B). Every Ξ-cycle across levels
  contains an upward Ξ-edge (box 193 §4).
