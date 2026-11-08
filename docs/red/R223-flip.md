# R223 item 2: extending Lemma FLIP (L-RED successor 58, Opus 5.5, D1 / D18 / D14; 2026-11-08, date -u)
Target: Lemma FLIP (docs/red/R222-lockup.md §4, l-red 5fdb96b3e): flips of a SET-type option S of a mover B, on an interval with
Λ(B) ∈ {K1, K2}, are at most 1 + (D_E,I(w) − 1) + Σ_(o ≠ S) (D_E,I(g_o) − 1). Lead brief, box R223 item 2: extend it to
(a) Λ(B) ∉ {K1, K2}, (b) non-SET options, (c) β-decided switches, by proof or by a frozen instance where the bound fails.
Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA / DEAD. Setting throughout: runs of IDEAL-CYC(G) for any genome G (RESULTS R104
format, Γ(G) as P-N5-XICYC [DEF]), Howard best switch at the movers with ties keeping the current option; premises as named in
docs/red/R222-cyc.md §6 ([F1], [OPT], [XICYC-a], [DEF], B-ONLY = R221-quiet.md §3).

## 0. Answer
- (a) PROVED (lane). FLIP holds for EVERY cycle node of B that B-ONLY allows. If Λ(B) = b_S on I, there are 0 flips. If Λ(B) is another
  β or c_X, FLIP's proof goes through word for word. Premise added: B-ONLY, hence [OPT]. §1.
- (b) DEAD as asked: for a NON-SET option, flips are NOT bounded by e-set changes, even with Λ(B) ∈ {K1, K2}. Frozen instance
  inst/flip223_E_NS_K12_rand_2235_10.json (N 2, M 6): 2 flips, FLIP-type bound 1, every e-set empty and constant. §2.
- (c) DEAD in the same instance: both flips are β-decided (P-steps). For SET options, β-decided flips are already covered by FLIP and by
  (a), so there is nothing to add for them.
- What does hold for every option: Lemma FLIP-G (PROVED, trivial): flips of any option o of B ≤ 1 + Σ_(g a gate of B) (#changes of
  Ω(g)) over any interval. This holds with no premise beyond Howard's tie rule. §3. But changes of full values include P-step ascents, so
  this is not an e-set bound.
- Consequence (READING): the counter question is NOT purely «can e-set heights double per level with U(G) growing». Non-SET options
  switch on β-parts and lengths. A counter can use them unless the P-step accounting (box 194 QUIET / T-QUIET, lane-level and on Γ(G)
  only) bounds them. §4.

## 1. (a) FLIP for every Λ(B) allowed by B-ONLY: PROVED (lane)
**Lemma FLIP-A.** Setting as in FLIP: B a mover, S a SET-type option of B (Ξ-target B itself, any β-parity), with gate g_S, e-vertex
e_S, β-vertex b_S (b_S → B) and w := e_S's successor. I is an interval on which Λ(B) = λ, Λ(w) and every Λ(g_o) (o ≠ S) are constant.
Premises: [F1], Odd optimal ([OPT]), E-MON, [DEF], Howard best switch with ties kept, and B-ONLY (so λ ∈ {β-vertices, K1, K2, c_X}).
Claim:
- (i) If λ = b_S, then σ_t(B) = S for every t ∈ I, so there are 0 flips on I.
- (ii) If λ ≠ b_S, then the number of flips of [σ(B) = S] on I is at most
  1 + (D_E,I(w) − 1) + Σ_(o ≠ S) (D_E,I(g_o) − 1).
Proof.
- (i) Suppose σ_t(B) ≠ S. Then no play passes g_S, since its only in-edge is from B ([DEF]). b_S's only in-edge is from g_S, so no play
  passes b_S either, and Λ_t(B) ≠ b_S. So Λ_t(B) = b_S forces σ_t(B) = S at every t ∈ I.
- (ii) FLIP's proof (R222-lockup.md §4, steps (1)-(6)) uses only three facts about λ:
  - (α) λ ≠ b_S (step (1): Odd's β-face at g_S would give B the cycle B g_S b_S with node b_S);
  - (β) λ is less relevant than every e-vertex (step (1): a play from w through B would make B's cycle pass e_S; step (1) also needs
    e_S ∈ Π);
  - (γ) the plays with node λ pass neither K0 nor K3, or both pass them (step (3)).
  - Check for λ ∈ {β-vertices other than b_S, c_X}:
    - (α) holds by assumption.
    - (β): by [DEF], every e-vertex has priority above every β, and c_X has priority 2.
    - (γ): a play that passes K0 ends in the core cycle K0 → K3 → K2 → …, which is frozen in IDEAL-CYC ([DEF]). Its node is K1 or K2,
      not λ. So no play with node λ passes K0 or K3.
  - Steps (4)-(6) never use λ ∈ {K1, K2} beyond (α)-(γ). The case where several values have node λ and different e-sets is step (3):
    with (γ), the most relevant vertex of the Π-difference is an e-vertex. β-vertices above λ can also differ, but every e is above
    every β, so such values are still ordered by their e-sets in lex order. ∎
**Corollary FLIP-ALL (PROVED, lane).** Combine FLIP-A with B-ONLY: every mover's SET-type options satisfy FLIP's bound on every interval
where the Λ's in FLIP's setting are constant, whatever Λ(B) is. So Corollary FLIP-POLY (R222-lockup.md §4) holds on the whole run,
not only on the part with Λ(B) ∈ {K1, K2}, under [E-LEV] with U(G) = O(1), and now with [OPT] as a premise.
DATA (flip223.py; unit: (mover, option, Λ-interval) with I a maximal interval on which NO cycle node changes; counter: units with flips >
FLIP's bound (violE); sets: rand = R221 brute221.rgen d 1-4, w 1-4, degree 2-3, seed 2235, 2,000 genomes; ret = priv222.rgen_ret, seed
2236, 1,000 genomes; out/flip223.txt):
| set | SET units, Λ(B) = b_S | maxflips | SET units, Λ(B) another β | violE | SET units, K1 / K2 | violE |
| --- | --- | --- | --- | --- | --- | --- |
| rand | 3,472 | 0 | 7,381 | 0 | 2,209 | 0 |
| ret | 6,139 | 0 | 16,394 | 0 | 2,732 | 0 |
(No unit had Λ(B) = c_X; the c_X case is covered by the proof only.)

## 2. (b), (c): non-SET options are NOT charged to e-sets: DEAD, instance frozen
Instance inst/flip223_E_NS_K12_rand_2235_10.json, sha1 ef330b146f6e80903ead01b1e9a09f609de8da99 (inst/SHA1SUMS):
{"N": 2, "lev": [0, 1], "opts": [[[-1, -1, 0], [-1, -1, 1], [-1, 1, 2]], [[0, -1, 3], [0, 0, 4], [0, 1, 5]]], "gate": [[0, 3, 5],
[4, 1, 2]], "br": [5, 1, 3, 0, 2, 4], "bp": [1, 1, 0, 0, 1, 1], "start": [0, 1]}.
Run (own.py, IDEAL-CYC, Howard best switch; T = 3). Mover B = x0. Its option 1 has Ξ-target X (b(0,1) → K0): a non-SET option.
Priorities: b(0,0) 17, b(0,1) 9, b(0,2) 12, b(1,0) 6, b(1,1) 11, b(1,2) 15; K1 5.
| t | σ_t(x0) | Ω_t(g(0,0)) | Ω_t(g(0,1)) | Ω_t(g(0,2)) |
| --- | --- | --- | --- | --- |
| 0 | g(0,0) | (K1, {b(0,0), K0, K3}, 5) | (K1, {b(0,1), K0, K3}, 5) | (K1, {b(0,0), b(0,2), b(1,1), K0, K3}, 11) |
| 1 | g(0,1) | (K1, {b(0,0), K0, K3}, 5) | (K1, {b(0,1), K0, K3}, 5) | (K1, {b(0,2), b(1,0), K0, K3}, 8) |
| 2 | g(0,2) | (K1, {b(0,0), K0, K3}, 5) | (K1, {b(0,1), K0, K3}, 5) | (K1, {b(0,2), b(1,0), K0, K3}, 8) |
- On t ∈ {0, 1, 2} no vertex changes its cycle node; Λ(x0) = K1, in FLIP's own class. Odd takes β at every gate, so every e-set in the
  game is ∅ and constant. FLIP's bound for (x0, option 1) is 1 + 0 = 1.
- t = 0 → 1: g(0,1) beats g(0,0): the Π's differ at b(0,0) (17, odd) vs b(0,1) (9, odd), and the top difference b(0,0) is odd and in
  g(0,0)'s Π. g(0,1) also beats g(0,2), which contains b(0,0) too. So x0 switches ON to option 1.
- t = 1 → 2: g(0,2) beats g(0,1). Between t = 0 and t = 1, when x1 switched, g(0,2)'s Π lost b(0,0) and b(1,1) and gained b(1,0). At
  t = 1 the top difference with g(0,1) is b(0,2) (12, even), in g(0,2)'s Π. So x0 switches OFF option 1.
- 2 flips > 1. Both are β-decided: same node, same e-set (∅), and the decision is made by β's in Π. This kills (b) («FLIP's bound for
  non-SET options») and (c) («β-decided switches are charged to e-set changes») in one instance.
- Other frozen instances of the same failure (inst/SHA1SUMS): flip223_E_NS_beta_ret_2236_725.json (N 4, M 11, Λ(B) a β, flips 2 vs
  bound 1), flip223_E_NS_beta_rand_1_40.json (N 12; the switches there are decided by length and by β's), flip223_E_NS_beta_rand_2235_98.json
  (N 12).
- DATA (same sets as §1; counter violE): non-SET units with flips > FLIP's bound: rand 63 of 21,217 (Λ(B) ∈ {K1, K2}) and 80 of 76,654
  (Λ(B) a β); ret 0 of 5,107 and 2 of 37,448. Max flips per unit 3. Switch census (unit: switch of a mover between consecutive states):
  E-decided (old and new option differ in cycle node or e-set) vs P-decided (they don't): rand 7,226 vs 10,836, ret 4,272 vs 3,739.
  So P-decided switches are not rare: they are 40-60 % of all switches.

## 3. What holds for every option: Lemma FLIP-G (PROVED, lane; trivial)
**Lemma FLIP-G.** Let o be any option of a mover B and J any set of consecutive states of a run of IDEAL-CYC(G), with Howard best
switch, ties keeping the current option. Then
#{t : t, t + 1 ∈ J, [σ_t(B) = o] ≠ [σ_(t+1)(B) = o]} ≤ 1 + #{t : t, t + 1 ∈ J, (Ω_t(g))_g ≠ (Ω_(t+1)(g))_g}, with g over B's gates.
By [F1], the right side is at most 1 + Σ_g (D_V,J(g) − 1), where D_V,J(g) is the number of distinct values of g on J.
Proof. Let Q_t := [some gate g′ ≠ g_o of B has Ω_t(g′) ▷ Ω_t(g_o)].
- An on → off flip at t needs Q_t: if no option is strictly better than the current o, Howard keeps o.
- An off → on flip at t needs ¬Q_t: Howard switches to a best option.
- So two consecutive flips have opposite Q at their states, and the gate-value tuple changes strictly between them. Q_t depends only on
  that tuple.
- [F1] makes each Ω(g) monotone, and ⊴ is total on values, so the changes of g number D_V,J(g) − 1. ∎
Remark: this is the trivial bound. Its right side counts EVERY ascent of a gate value, including P-step ascents (β-part and length).
DATA: the sharper candidate with FLIP's vertex set, flips ≤ 1 + Σ_(v ∈ {w_o, b_o's successor if ≠ B} ∪ {g_o′ : o′ ≠ o}) (D_P,I(v) − 1),
D_P = #distinct (Π, length): violP 0 on every unit of §1-§2 (181,803 units: rand 113,488, ret 68,315). PROVED when no play from w_o or from b_o's successor passes
B on I, because then Ω_t(g_o) is the Odd-minimum of the two genuine face values at every t, whether σ_t(B) = o or not (gate in-edge
from B only). The returning case is CONJECTURE.

## 4. What this means for the counter question (READING, not a result)
- SET-type options are bounded by e-set changes on the whole run under B-ONLY (FLIP-ALL), so a SET bit is a polynomial bit when U(G)
  = O(1) under [E-LEV].
- Non-SET options are not bounded by e-set changes (§2). Their flips are bounded by the ascents of the gate values (FLIP-G), and those
  include P-steps. A counter on IDEAL-CYC / N5′-xi could therefore use non-SET options whose comparisons are decided by β-sets in Π, with
  e-sets frozen.
- So the open question has two parts, not one:
  - (Q1) can e-set heights double per level with U(G) growing (P-N5-ASC's open region);
  - (Q2) can P-decided switches of non-SET options compound between e-set changes?
- Q2 is what box 194's QUIET / T-QUIET is meant to bound. Those lemmas are lane-level, on Γ(G) only, and their Γ3 transfer is NOT
  proved (P-N5-END §9, REFEREE 28's QT-L4).
- DATA hint only: in the 3,000 genomes above, max flips per (unit) is 3 and the run lengths are ≤ 13. No compounding seen, but the
  generators are random, not adversarial for Q2.
- Suggested next attack (L-RED): a climb that maximises P-decided flips of one non-SET option between e-set changes, on a W-ladder whose
  β-ranks are chosen per level.

## 5. Tools and reproduction
- experiments/red/r223/flip223.py (own.py from experiments/red/r222; brute221.rgen from experiments/red/r221q; priv222.rgen_ret).
  `python3 experiments/red/r223/flip223.py rand 2235 2000 OUTDIR; python3 experiments/red/r223/flip223.py ret 2236 1000 OUTDIR`
  (out/flip223.txt); `python3 experiments/red/r223/flip223.py experiments/red/r223/inst/*.json` replays the frozen instances.
- Frozen instances: experiments/red/r223/inst/ (SHA1SUMS). Not a TARGET.md claim; nothing here is M3 or M4; G-N5-TIME stays OPEN.

## 6. Sources opened
- claude/l-red 5fdb96b3e docs/red/R222-lockup.md §4 (FLIP, FLIP-POLY), docs/red/R222-cyc.md §6 (premise tags, B-ONLY row 1).
- claude/l-red docs/red/R221-quiet.md §3 (B-ONLY), via R222-cyc.md §6.
- experiments/red/r222/own.py (VJ order, Odd optimisation, Howard run), used unchanged.
