# R2-N5-NEEDB: second-referee check of packet P-N5-NEEDB (L-SI box 13: XG, ANTI, NEED-β incl. (A2*), OLD-THREAT, case (i) ⇐ INTO). REFEREE-2 (successor 12), written 2026-10-25 20:48Z-21:5xZ (date -u)
Signature: (Opus 5.5, D15). Lead queue item 1 (Lead 20:49Z, its stamp: "GO").
Object: docs/si/P-N5-NEEDB-box13.md, sha1 7471aef3 (`git show e6ee6130:docs/si/P-N5-NEEDB-box13.md | sha1sum`), the same at the pin
e6ee6130 and on my tree. Author: L-SI successor 8 (§1-§3 (B), (A1), (A2′), (A2″): L-SI successor 7). Committed l-si 3ea0f5f9, 17:52:24Z.
Source texts named by the packet, sha1 checked on my tree: N5-LV3-box12.md 20ba05d7, N5-A2STAR-box13.md 2a85601d, N5-RISE-box13.md
3b8fea13 (all as stated). The packet governs; I refereed the packet text.
Background read (texts, not recalled): SPEC S1-S5 (docs/new/N5-ssi-global.md); P-N5-FB §1 (lev, COARSE_L, (C1)-(C4)); RESULTS R29 (a)
((C5)-(C7)), (c) OFFGATE, (e) NL (i)-(iii); R31 (d) FLAT-ALL (i)-(iv); R20 (b) FBL with P-N5-XA §0-§3 (its R_k CONTAINS o, so its
"F → R, R → R" is the packet's "F → R̄, R → R̄") and G-CLS-1 (R2-N5-CLS: the strong gate form for u* ≠ none uses state k alone);
P-N5-RL §0-§3 (R37: R-SAME, BL-FORM, BL (a)-(e) with Steps 0, 1, 2a, 2b, CONF-MONO, FREE-FREEZE); P-N5-LV §0-§1 (R41 (a) LV-SHAPE);
P-N5-ENT §0-§1 ((Σ1)-(Σ6), Lemma FZ; R40); R36's statement (Lemma P1); R15 (a), R17 (a) F1, R18 (d) Lemma S (a) as quoted in P-N5-RL §0.
Independence: nothing in docs/referee/ was read for this packet. `ls docs/referee | grep -i needb` -> R-N5-NEEDB.md is on my tree; NOT
opened, and no `git log` of docs/referee/ was read. DISCLOSURE: at 21:3xZ, after §1-§4's verdicts and notes were written (the batch
was done), a repo-wide `grep -rn block_9501 docs notes` printed two lines that report on REFEREE's R-N5-NEEDB: docs/agents/LEAD-STATE.md
l. 1410 ("referee 008ad8a, R-N5-NEEDB: all SIGNED, no gaps. Notes NEEDB-N1..N4. NEED-β case (B) occurs once, on block_9501") and RESULTS
R43 limit (iii) ("reproduced on REFEREE's engine from that start pair, R-N5-NEEDB (referee 008ad8ab)"). I changed no verdict or note
after that; N-NEEDB-5 rests on N5-LV3 §4 and my own runs. No lane script (experiments/si/lv/xg.py, experiments/si/lv13/a2star.py, oldthreat.py,
rise_*.py, none_*.py) was run or imported.
Tools (own code, docs/referee-2/R2-N5-NEEDB/): needb_check.py (on R2-N5-ENT/ent_check.py, R2-N5-OUT/out_check.py traces own | rand |
spec, R2-N5-FRZ, R2-N5-RE even_optimum / vals_of), needb_climb.py (lv2_climb.py's harness, fitness lv | rise, the seed's saved start
pair as an extra run), files.lst (= R2-N5-FBPOLY/files.lst, 492 𝒞^1O files), run_all.sh, run_climbs.sh, run_mut.sh, totals.py,
logs/, logs_mut/, climb/, totals_logs.txt.
Labels: PROVED (L-SI succ. 7 / 8). These are lemmas about the candidate N5: not a running-time bound, not a TARGET.md claim, not a
step-4 pass. G-N5-TIME stays OPEN. No (P) beyond R36.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §1 Lemma XG | SIGN | N-NEEDB-4 (DATA): vacuous in the batch, but reached 7 times in climbs (0 failures); witness saved |
| §2 Lemma ANTI (any one-player game) | SIGN | — |
| §2 instances ANTI-Ξ, ANTI-W | SIGN | — |
| §3 Corollary NEED-β, cases (B), (A1), (A2′), (A2″) | SIGN | N-NEEDB-1 (status): setting (LV+) is NOT vacuous; a saved witness exists and is exercised |
| §3 Corollary NEED-β, case (A2*) | SIGN | — |
| §4.1 Lemma OLD-THREAT | SIGN | N-NEEDB-3 (citation, harmless) |
| §4.2 Reduction INTO ⇒ no case (i) fallback | SIGN | N-NEEDB-2 (wording): "case (i)" must be read as the NEXT fallback of S after k0 |
| §5, §6 | not signed (as briefed): INTO, "THR ⇒ M ≥ 0", case (ii), the dead conjectures | — |
No statement is NOT SIGNED, and no gap is open.

## 1. Lemma XG: SIGN
Setting: k an in-phase THR S4c fallback with (h); y ∈ R_k Even, s := σ_k(y), z := σ*(y) ∈ F_k with z's (σ*, τ)-play inside F_k.
- (i) σ* on z's play, extended by σ_k on the rest of F_k, maps F_k into F_k (the play is closed under successors; σ_k(F_k) ⊆ F_k; Odd
  vertices of F_k other than o keep their single successor in F_k). It is a strategy of G_τ[F_k] with z's σ*-play, so U(z) ⊴
  Opt(G_τ[F_k])(z) = W(z) (F1 in G_τ[F_k], BL (c); BL (c)'s setting is exactly this one). F1 in G_τ gives ⊵. Lemma G: W = Ξ off R̄. ✓
- (ii) y ∈ R_k: y's W-play reaches o, and o is on no W-cycle (H2). If y were on its own W-cycle the whole play would be that cycle and
  contain o. So W(y) = y ⊕ W(s), and s's play does not revisit y. z's σ*-play stays in F_k, so it avoids y: U(y) = y ⊕ U(z). F1 at y,
  then (C7) cancels y (on neither play, not a cycle node). ✓
- (iii) s ∈ R̄_k (s = o allowed: π_o = ∅). Lemma G: W(s) = π_s ⊕ w, Ξ(s) = π_s ⊕ θ, with π_s ⊆ R disjoint from P(θ), P(w) ⊆ {o} ∪ F
  and from c ∈ F. (C7): π_s ⊕ w ▷ π_s ⊕ θ at level r. Hence Ξ(z) = U(z) ⊵ W(s) ▷ Ξ(s): (y, z) is an Ξ-improving edge with z ≠ s
  (z ∈ F, s ∈ R̄), a gate. (C5) with a = Ξ(s) ◁ b = W(s) ⊴ c = Ξ(z): lev(Ξ s, Ξ z) ≥ lev(Ξ s, W s) = r. ✓
- DATA: XG's hypothesis occurred 0 times (batch: 4,488 / 4,440 / 4,426 R → F optimal edges at 2,772 / 2,768 / 2,715 THR in-phase
  fallbacks in the own / spec / rand traces, up to 5 optima each; none with the target's play inside F). Climbs reach it 7 times, all
  checks pass (§6). Mutation xg (drop "z's play inside F_k") FIRES (XG gate/level fails, e.g. gt_a_best.pg state 2, y 18 → z 24).
- N-NEEDB-4 (DATA): the packet calls XG vacuous ("0 cases"). It is not: climb 12004 (seeded from block_9501's lineage) met XG's hypothesis
  7 times; witness R2-N5-NEEDB/climb/witness_xg_12004.pg (sha1 89d9085b; start pair in witness_xg_12004.txt). Reproduce with the climb's
  own evaluate(g, o, "lv", 12004) and that START (inst mode seeds its rng differently and picks other optima): XG_hypothesis 1, 0
  violations.

## 2. Lemma ANTI and its instances: SIGN
- Step 1. Any z_c (a ⊴-best of σ(c) and c's exceptional targets) has V(z_c) = (c, ∅, ·): its σ-play reaches c through vertices ranked below
  c. It meets no other c′ ∈ T first: c′'s σ-play is its own cycle, topped by c′; c on that cycle would force c = c′ (one top per
  cycle). Under σ_ex a play agrees with its σ-play up to its first T vertex c (all earlier vertices are off T, where σ_ex = σ), then runs
  on c → z_c → … → c, a cycle topped by c. The σ-play from c is also a cycle topped by c. The value (cycle node, path set and length up to
  the first visit of c) is the same. Plays meeting no T vertex are unchanged. ✓
- Step 2. H′ keeps σ_ex(v) at every Even v, so it is a one-player game with every vertex having a successor. At v ∉ T, σ_ex(v) = σ(v)
  and every allowed u has V(u) ⊴ V(σ v); at c ∈ T every allowed u is ⊴ V(z_c) by the choice of z_c. With V_{σ_ex} = V there is no
  improving edge in H′, so R36 Lemma P1 makes σ_ex optimal in H′; σ′ is a strategy of H′; F1 in H′. ✓
- ANTI-Ξ: H = G_σ̄ (Odd fixed to σ̄_k; on 𝒞^1O only o has a choice, o → x0), σ_k's valuation there is Ξ_k (SPEC S1; ENG-1 of R25). Gates
  = Ξ-improving edges (S2). In (LV) every gate has level −1, so an (α) gate (y its own Ξ-cycle node, Ξ(σ y) = (y, ∅, ·)) has
  Ξ(z) = (y, ∅, ·): exceptional. ✓
- ANTI-W: a W-improving edge is a gate (then W-exceptional, BL Step 2a) or not a gate (blocked, by definition). ✓
- DATA: general lemma on random one-player games (needb_check.py anti 3000 3 9 1): 18,000 checks, 3,684 using an exceptional edge,
  0 failures; mutation anti (one improving non-exceptional edge allowed) FIRES (5,688). Instances at sampled states of the batch:
  ANTI-Ξ 9,559 / 9,582 / 9,314 and ANTI-W the same numbers (own / spec / rand), exceptional edges used in 1,358 / 1,353 / 1,353 (Ξ) and
  1,269 / 1,302 / 1,259 (W); 0 failures. At THR in-phase fallbacks: 60,385 / 60,037 / 58,958 blocked edges, 0 / 3 / 0 W-improving
  gates, all exceptional.

## 3. Corollary NEED-β: SIGN (all five cases)
- (F-a): x0 ∈ F (H1) and θ = o ⊕ Ξ(x0) ◁ w (o is not its own honest cycle node, H1), so BL Step 1 gives (o, x0) ∉ Iτ_k. x0 ≠ t (else
  θ = o ⊕ W(t) = w). BL Step 0: not improving means U(x0) ⊵ U(t) (the order on triples is total). ✓
- (F-b): t = e* ∈ F (H2), x0 ∈ F: both plays avoid o, so (C7) cancels o in θ ◁ w: W(t) ▷ Ξ(x0) at level r. (F-c) by transitivity and
  (C5). ✓
- Exhaustiveness: B / A1 / (K′ ∋ o: m′ ∈ λ ∪ {o} → A2′, else m′ after o and outside λ ∪ {o}, so its rank differs from m_K's: A2″ or
  A2*). (A2′) with m_K ≠ m′ is passed to (A2″), as written. ✓
- Uses of the "no (β) gate" assumption: every σ*-edge on 𝒫 is σ_k's edge, a non-gate, or a gate; LV-SHAPE with r ≥ 0 leaves (α) and
  (β), so the assumption makes every edge allowed for ANTI-Ξ. ✓
- (B) 𝒫 avoids o: in G_σ̄ the Odd vertices on 𝒫 (≠ o) have the same single edge as in G_τ, so σ′'s play from x0 is 𝒫, of value U(x0).
  ANTI-Ξ: U(x0) ⊴ Ξ(x0), against (F-c). ✓
- (A1) o is on 𝒫's tail, so λ, o and 𝒬 are disjoint. U(t) = W(t) by ANTI-Ξ on 𝒬 (t ∈ F) and F1. σ″: λ, then o → x0 in G_σ̄, the cycle
  K = λ ∪ {o}, value (m_K, ∅, ·) at x0; ANTI-Ξ: rew(m_K) ≤ rew(c), equality iff m_K = c. m_K ≠ c: c ≠ o (c ∈ F), and c ∈ λ is impossible
  since c lies on 𝒬's cycle (U(t) = W(t) has cycle node c) and 𝒬 avoids λ. The comparison K ⊕ W(t) ⊵ W(t): P adds exactly the K-vertices
  ranked above c (K is disjoint from P(W t) ⊆ 𝒬). H ≠ ∅: the top of the difference is m_K, even, ranked above c, so rew(m_K) > rew(c).
  H = ∅: lengths only, longer ⊵ needs c odd, m_K below c, rew(m_K) ≥ −pp(m_K) > −pp(c). Both contradict. ✓
- (A2′) / (A2″): t ∈ K′ (t is o's successor on 𝒫); U(x0), U(t) have cycle node m′. (A2′), m_K = m′: then m′ = c ∈ λ (c ≠ o), U(t) =
  (c, ∅, ·), and ∅ ⊵ P(W t) ▷ P(Ξ x0) ⊵ ∅ uses r ≥ 0 (lev(Ξ x0, W t) = r ≥ 0 is a path-set difference with W(t) the better). (A2″): m_K
  lies on λ before the re-entry vertex (every vertex of K′ ranks ≤ m′ < m_K, o included); P(U t) = ∅, P(U x0) has top m_K, which (F-a)
  makes even; rew(m_K) ≤ rew(c) then forces c even, rank c ≥ rank m_K > rank m′, and rew(m′) < rew(c) contradicts F1 at t. ✓
- (A2*): Step 1: all vertices of x0's play before its first visit to m′ (λ, o, t … m′) rank below m′; P = ∅ for both; ℓ_{x0} = |λ| + 1 + ℓ_t
  > ℓ_t; strict ⊵ on lengths needs m′ odd. Step 2: m′ ≠ c gives rew(c) < rew(m′) = −pp(m′) < 0, so c odd, rank c > rank m′. Step 3:
  rank m_K < rank m′ ≤ rank c, so m_K ≠ c and c is odd: rew(m_K) ≥ −pp(m_K) > −pp(c) = rew(c), against σ″'s rew(m_K) ≤ rew(c). The
  remark (only Step 3 uses "no (β) gate") is correct. ✓
- DATA (own code; checks: (F-a), (F-b), (F-c), LV-SHAPE kinds, a (β) gate on the σ*-play of x0 for every tested optimum, the case):
  - Batch: (LV+) occurs at exactly one state, R2-N5-LV2/climb/block_9501.pg (its saved start pair, all three traces): 3 (β) gates,
    case B, a (β) gate on 𝒫, 0 failures. Every other in-scope THR r ≥ 0 fallback has M ≥ 0 (2,766 / 2,762 / 2,710 states).
  - Climbs (FIT lv, seeded with the witness and its start pair): see §6. Mutation b0 (ask for an (α) gate on 𝒫 instead) FIRES at the
    witness.
  - RECORD (outside the setting): at all 2,766 / 2,762 / 2,710 in-scope THR r ≥ 0 fallbacks with M ≥ 0, the σ*-play from x0 uses an
    R → F gate. Consistent with the packet's §6 "analogue at M ≥ 0".
- N-NEEDB-1 (status / DATA). The packet's table row "(LV+) occurs 0 times … with a saved witness (… 645 level −1 block fallbacks with
  r ≥ 0, none saved) — vacuous" was true at its commit (17:52Z). My predecessor saved one at 18:02Z: R2-N5-LV2/climb/block_9501.pg (sha1
  1b5b76fd; start pair in block_9501.txt; referee-2 f2209fa4): state 1 is in scope, THR, r = 10, M = −1, gates (10, 1), (10, 3),
  (10, 8), all (β). So NEED-β's setting is non-empty, and its conclusion is exercised (case B only, so far). The cases A1, A2′, A2″, A2*
  stay unexercised in the batch and in 297,752 climb states (§6). Not a gap.

## 4. OLD-THREAT and the reduction
### 4.1 Lemma OLD-THREAT: SIGN
- The chain is P-N5-ENT's FZ with t for k. FZ's proof uses (h) at the sources [k0, t − 1], (A_s), r_s > L and NL; not that k is a fallback.
  t > j ≥ k0 + 1 gives t ≥ k0 + 2, so k0 + 1 is a source of a transition of S, and (h) holds at k0 + 1 (FLAT-ALL (iii) needs (h) at k0
  and k0 + 1, M_{k0} = L ≥ 0). OFFGATE at k0 → k0 + 1 gives (A_{k0+1}); NL (iii) carries it along the S4a steps; NL (ii) gives F_{s+1} ⊆
  F_s, so x ∈ F_t ⇒ x ∈ F_s on [k0 + 1, t]; NL (i) freezes COARSE_L(Ξ x) at each S4a step. ✓
- Sandwich: x ∈ F_t, so x's (σ_t, τ)-play avoids o and is the same for every Odd strategy (𝒞^1O). Lemma S (a) with Odd choosing x at o:
  θ_t ⊴ o ⊕ W_t(x) = o ⊕ Ξ_t(x) (o is not on that play, so not a cycle node). (C1) and the freeze give COARSE_L(θ_t) ⊴_L COARSE_L(θ_{k0}). ✓
- Monotonicity: the rise is a transition j → j + 1 ≤ t with COARSE_L(θ_{j+1}) ▷_L COARSE_L(θ_j) (changed and ⊵ by R15 (a), (C1));
  ⊴_L is a total order on coarse values (C3), so COARSE_L(θ_t) ▷_L COARSE_L(θ_{k0}). Contradiction; x ≠ o, so x ∈ R_t. The x_{k0} case:
  θ_{k0} = o ⊕ Ξ_{k0}(x_{k0}) (H1), so the hypothesis holds trivially. ✓
- N-NEEDB-3 (citation, harmless): "(C7) through o ⊕" in the sandwich is used only to pass equal COARSE_L values through o ⊕; (C4) gives that
  directly (and (C7)'s lev form gives it too, since o is on neither play). Nothing changes.
- DATA: 130 / 129 / 126 rises, 445 / 446 / 427 post-rise states, 1,074 / 1,074 / 1,058 exit checks (own / spec / rand), 0 failures; FZt
  (FZ at every post-rise state, all v ∈ F_t ∩ F_{k0}) 0 failures. Mutations: otc (drop the COARSE condition) FIRES (e.g. best_blk_9204.pg
  run 0: exit 11 not in R_21, k0 16, L 34; best_rise_9201.pg run 0: exit 18 not in R_13); otf (drop x ∈ F_{k0}, keep the COARSE
  condition) does NOT fire: no exit of R_{k0} with that condition is ever outside R_t in my data, so the data do not show this hypothesis
  is needed (the proof needs it for the freeze). Climbs: §6.

### 4.2 Reduction INTO ⇒ no case (i) fallback: SIGN
- Let k be the next fallback of S after k0, with r > L on [k0 + 1, k]. Then k > j (no fallback before the rise), every transition s → s + 1
  with k0 < s < k is an in-scope S4a step with r_s > L, so k is a post-rise state. r_k > L ≥ 0 under (h) gives θ_k ≠ w_k, θ_k ◁ w_k
  (XW): THR with u* ≠ none. FBL's strong form at state k alone (G-CLS-1: the u* ≠ none gate argument needs only state k; P-N5-XA's R_k
  contains o, so gates into o are excluded too): every gate has its target in F_k. INTO at k says the opposite. ✓
- N-NEEDB-2 (wording). §4.1's TARGET and §4.2 call case (i) "a later fallback k with r > L on [k0 + 1, k]". A later fallback that is not
  the next one is not a post-rise state (a fallback lies in between). The proof is for the next fallback; that is enough for the TARGET
  ("no further fallback": the first one is excluded). The fixes file should say "the next fallback of S after k0".
- DATA: case (i) occurred 0 times in the batch (as in R2-N5-ENT §6 and the packet's data). INTO (RECORD, a CONJECTURE): 317 / 319 / 303
  post-rise states with r > L, 0 failures. Climbs: §6.

## 5. Not signed (as briefed), and one FALSE conjecture
INTO; "in scope, THR ⇒ M ≥ 0"; case (ii); RISE-DROP, GATE-ABOVE, FEED (recorded FALSE by the lane).
- N-NEEDB-5 (FINDING, about a §5 item, not a signed one): the CONJECTURE "in scope, THR ⇒ M ≥ 0" is FALSE.
  - Its own counterexample shape (N5-LV3-box12.md §4, sha1 20ba05d7): "an in-scope THR fallback with r ≥ 0, every gate of level −1, and at
    least one (β) gate (so rank o < rank c)".
  - Instance: docs/referee-2/R2-N5-LV2/climb/block_9501.pg (sha1 1b5b76fd), from the start pair in block_9501.txt (SPEC allows a start
    pair; N5-LV3 §5's own data use perturbed start pairs). State 1: (h), θ = (5, {9}, 3) ◁ w = (5, ∅, 1), r = 10, M = −1, gates (10, 1),
    (10, 3), (10, 8), all (β) (rank o 2 < rank c 9); k → k+1 in scope (in phase, H2 at 2, w_2 = w_1). Reproduced by my needb_check.py in
    the own, spec and rand traces (logs/*/ for that file: NEEDB_LVplus_states 1 each; the spec trace is re_check.n5_spec, SPEC S1-S5).
  - From the canonical S3 start the run has no such state (Lead re-run, RESULTS R43 limit (iii)), so the conjecture may survive in a
    "from the S3 start" form; that form is not what N5-LV3 §4-§5 states.
  - Status today: still listed as a CONJECTURE in docs/si/N5-LEDGER-box14.md item 4 and RESULTS R41 / R43 "not signed". It should be
    recorded FALSE (L-SI's docs/si/DEAD.md), with this instance. NEED-β then reads: at every such counterexample, the optimal reply from
    x0 uses a (β) gate. On block_9501 it does (case B).

## 6. Climbs (needb_climb.py; seeds are inputs only)
Six climbs, 2026-10-25 21:0xZ-21:48Z (date -u), every evaluation runs needb_check on 4 runs (the seed's saved start pair while it
is valid, S3, own and rand traces); any violation stops a climb and dumps the game. Totals from climb/*.txt:

| climb | seed game | evaluations | (LV+) states | NEED-β cases | XG hyp. | rises / post-rise / OT exit checks | INTO r > L | case (i) | violations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lv 12001 (1,500 s) | R2-N5-LV2/climb/block_9501.pg + start pair | 139,376 | 131,566 | B 157,285 (all) | 0 | — | — | — | 0 |
| lv 12002 (1,500 s) | random n 8-16 | 104,936 | 0 | — | 0 | — | — | — | 0 |
| lv 12004 (1,200 s) | climb/best_lv_12001.pg + start pair | 140,389 | 166,186 | B 171,074 (all) | 7 | — | — | — | 0 |
| rise 12003 (1,500 s) | R2-N5-ENT/climb/best_rise_9201.pg | 21,069 | — | — | — | 33,592 / 33,594 / 38,327 | 2 / 2 | 0 | 0 |
| rise 12005 (1,200 s) | random n 10-16 | 342,575 | — | — | — | 0 | 0 | 0 | 0 |
| rise 12006 (1,200 s) | R2-N5-ENT/climb/best_rise_9202.pg | 4,034 | — | — | — | 3,583 / 5,070 / 19,661 | 1,490 / 1,490 | 0 | 0 |

- (LV+): 297,752 states, 328,359 tested optima, every σ*-play from x0 uses a (β) gate; every one is case B. Cases A1, A2′, A2″ and A2* stay
  unexercised: they rest on the proof (checked line by line in §3). Witnesses: climb/witness_lvplus_12001.pg (sha1 a6bf3bce),
  witness_lvplus_12004.pg, best_lv_12004.pg (sha1 9a8f565a), each with its start pair in the .txt of the same name.
- Random seeds reach neither (LV+) nor a rise in 25 minutes (12002, 12005). The lane's §6 says the same for random 𝒞^1O games.
- OLD-THREAT: 57,988 exit checks at 38,664 post-rise states, 0 failures; INTO 1,492 / 1,492 (CONJECTURE, recorded); case (i) 0.
- Mutation controls (logs_mut/, own trace, whole library): xg FIRES, otc FIRES, b0 FIRES (at the witness), anti FIRES (random games);
  otf does not fire (§4.1).

## 7. Summary
- All statements to sign: SIGN. No gap. Notes N-NEEDB-1 (status: (LV+) is non-empty; witness exercised), N-NEEDB-2 (wording: next
  fallback), N-NEEDB-3 (citation: (C4)), N-NEEDB-4 (DATA: XG reached 7 times in climbs, witness saved), N-NEEDB-5 (FINDING: the §5 CONJECTURE "in scope, THR ⇒ M ≥ 0" is FALSE on block_9501.pg from its saved start pair).
- Batch: 492 files × 4 starts (S3, 2 random, plus the saved pair where one exists) × 3 traces = 5,904 runs, 90,000 states; random games
  3,000 runs (needb_check.py random 3000 6 14 12100 own); 0 violations, 0 nonzero exits (totals_logs.txt).
