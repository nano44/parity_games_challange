# N5-ANC (box 58): key ancestry. A Ξ-change never raises its key going forward through a play prefix, an Even switch or an Odd relay; keys rise only at Odd ESCAPES (an Odd vertex leaving a choice whose new play returns to it), at first switches and at mixed loops. So the FUEL-COUNT recursion cannot come back to its pair with a gain except through an escape. But "no gain cycle" bounds nothing: classical switch-all SI satisfies every lemma here, with no self-feeding at all, and still re-routes one pair 2^N times on switchallexp_N
L-SI successor 37 (Opus 5.5; D18). Lead 2026-10-31 13:06Z, box 58: «Define "feeding" precisely … Then prove that the recursion
FUEL-COUNT → HC(z) → (fuel of z's higher-digit pairs) → … cannot cycle back to (y, z) with a gain (e.g. by a strict decrease of the key
level at each recursion step), which would bound fuel polynomially. Otherwise give the cycling instance. R161's sketch … is the starting
point.» Written 2026-10-31 from 13:2xZ (date -u; see commit).
- Labels: PROVED (lane) / DATA / READING / CONJECTURE / DEAD. Not a TARGET.md claim. G-N5-TIME stays OPEN. Not a packet.
- Outcome: a REDUCTION plus a barrier. (1) PROVED (lane): no gain cycle through Even switches and Odd relays (§3, §4). (2) The only
  places a key can rise are named and counted (§3). (3) DEAD as a route: "no gain cycle ⇒ polynomial fuel". The lemmas' premises also
  hold for classical SI, which shows exponential pair fuel on a family that has no self-feeding (§5).
- Premises: [R15a], [R57], [PLAY] / Φ / (Φ-comp), all as quoted in P-N5-ODD §1 (frozen, sha1 03eec41d); [IMP] (SPEC S2, S4a, S4c): if
  σ_(k+1)(v) ≠ σ_k(v) then (v, σ_(k+1)(v)) ∈ Iσ_k. (S4a picks from A(v) = {σ(v)} ∪ improving targets, S4c picks an improving target,
  S4b leaves σ alone.)

## 1. Keys as an ultrametric (definitions; Lemmas ULT, INT, Φ-KEY PROVED)
- Encode a value a = (c, P, ℓ) as the tuple (c; χ_P(rank n − 1), …, χ_P(rank 0); ℓ). key(a, b) := the first position where the tuples
  differ: (2, 0) (cycle node), (1, r) (rank r), (0, 0) (length); None if a = b. Significance order None < (0, 0) < (1, 0) < … < (1, n − 1)
  < (2, 0). This is srcfuel.py's key (box 56). κ_u(v) := key(Ξ_u(v), Ξ_(u+1)(v)) is the KEY of v's change at u.
- Lemma ULT. key(a, c) ≤ max(key(a, b), key(b, c)) for all values. (Agreement above level i and above level j gives agreement above
  max(i, j).) □
- Lemma INT. If a ⊴ b ⊴ c then key(a, b) ≤ key(a, c) and key(b, c) ≤ key(a, c).
  - Proof. ⊴ is lexicographic on the tuple (SPEC S1, Q1). First the cycle node, ordered by its reward, which is injective. Then, for equal
    c, ranks from the top, each oriented by its parity. Then the length, oriented by c's parity. Each position's order depends only on
    the positions above it. If a and c agree above key(a, c), then position by position a_p ⊴ b_p ⊴ c_p with a_p = c_p, which forces
    b_p = a_p. □
- Lemma Φ-KEY. key(Φ(π; a), Φ(π; b)) ≤ key(a, b) for every finite sequence π and all values a, b (not only values of actual plays).
  - Proof. By (Φ-comp), take π = s. [PLAY]'s case split gives Φ(s; (c, P, ℓ)) = (s, ∅, 0) if c = s, else (c, P ∪ S_c, ℓ + 1) with
    S_c = {s} if p′(s) > p′(c), else ∅.
  - Different cycle nodes: key(a, b) = (2, 0) is the maximum.
  - Equal c = s: both images are (s, ∅, 0).
  - Equal c ≠ s: (P_a ∪ S) Δ (P_b ∪ S) = (P_a Δ P_b) \ S, and both lengths shift by 1. □
- READING (cross-area). Values are the leaves of a rooted tree of depth n + 2, with d(a, b) = 2^level(key). Φ-KEY says every prefix map
  Φ(π; ·) is 1-Lipschitz (non-expanding) in this ultrametric. §3 adds that Even switches and Odd relays are non-expanding too. §5 is the
  standard warning from non-Archimedean dynamics: the 2-adic odometer x ↦ x + 1 is an isometry and still has orbits of length 2^N mod
  2^N. Non-expansion alone never bounds a count; carries do. Here the Odd escape plays the role of the carry (§3).

## 2. Local key laws (PROVED, lane)
Fix a transition u. A vertex s is CHANGED at u if it is Even with σ_(u+1)(s) ≠ σ_u(s), or Odd with σ̄_(u+1)(s) ≠ σ̄_u(s).
- KEY-PREF. Suppose Ξ(z) changes at u. Let s be the first changed vertex on z's old (σ_u, σ̄_u)-play; it exists by OLD-PLAY (P-N5-ODD §2).
  Then κ_u(z) ≤ κ_u(s).
  - Proof. The prefix π before s moves the same way at u + 1, so Ξ_j(z) = Φ(π; Ξ_j(s)) for j = u, u + 1 by [PLAY]. Apply Φ-KEY. □
  - DATA: equality holds at every change of the corpus (PREFV 0).
- EVEN-SPLIT. Let Even s switch w → z′ at u, with GAIN g := key(Ξ_u(w), Ξ_u(z′)). Then κ_u(s) ≤ max(g, κ_u(z′)).
  - Proof. Ξ_u(s) = Φ(s; Ξ_u(w)) and Ξ_(u+1)(s) = Φ(s; Ξ_(u+1)(z′)). Apply Φ-KEY, then ULT through Ξ_u(z′). □
- ODD-KEY. Let Odd s change its choice x → x₂ at u.
  - (I) If s is not on x's (σ_(u+1), σ̄_(u+1))-play, then κ_u(s) ≤ κ_u(x).
    - Proof. Let ρ := σ̄_(u+1) except ρ(s) := x. Then Ξ_u(s) = Φ(s; Ξ_u(x)) ⊴ Ξ_(u+1)(s) by [R15a], and Ξ_(u+1)(s) ⊴ val(σ_(u+1), ρ)(s)
      = Φ(s; Ξ_(u+1)(x)) by [R57], because s's ρ-play is s followed by x's new play. INT, then Φ-KEY. □
  - (II) Always κ_u(s) ≤ max(og, κ_u(x₂)), where og := key(Ξ_u(x), Ξ_u(x₂)) is the SWAP key. (Φ-KEY + ULT.) □
- SUCC-MONO. Ξ_t(σ_t(s)) ⊴ Ξ_(t′)(σ_(t′)(s)) for every Even s and t ≤ t′.
  - Proof. One step at a time. If σ(s) is unchanged, use [R15a]. If it switches to an improving target, [IMP] and [R15a] give
    Ξ_(t+1)(new) ⊵ Ξ_t(new) ▷ Ξ_t(old). □
- ARM. Let Even s switch to z′ at u with gain g. Its ARMING TIME is t := max{t < u : σ_t(s) = z′ or Ξ_t(z′) ⊴ Ξ_t(σ_t(s))}. If t exists,
  then κ_(t′)(z′) ≥ g for some t′ ∈ [t, u).
  - Proof. SUCC-MONO and [IMP] at u give Ξ_t(z′) ⊴ Ξ_u(w) ◁ Ξ_u(z′), and Ξ_t(z′) ⊴ Ξ_u(z′) by [R15a]. INIT gives
    g ≤ key(Ξ_t(z′), Ξ_u(z′)), and ULT along t, …, u bounds that by max_(t ≤ t′ < u) κ_(t′)(z′). □
  - A switch with no arming time is INIT. Each edge has at most one INIT switch per N5 run: afterwards σ(s) = z′, so every later switch
    to z′ is armed by the time s leaves z′.
- Corollary GAIN-DOWN. A fuel re-route of (y, z) at k (P-N5-ODD §6) with key a has gain ≤ a.
  - Proof. (y, z) ∉ H_(k−1) means z ≠ σ_(k−1)(y) and (y, z) ∉ Iσ_(k−1), i.e. Ξ_(k−1)(z) ⊴ Ξ_(k−1)(σ_(k−1)(y)) (S2). So the arming time
    is k − 1, and ARM gives g ≤ κ_(k−1)(z) = a. □

## 3. Theorem ANCESTRY (PROVED, lane) and its sources
- The WALK of a change (z, u). Start at v := z. Repeat:
  - Let s be the first changed vertex on v's old play.
  - Even s: if g_s ≥ κ_u(s), stop at the E-ROOT (s, σ_(u+1)(s), u). Otherwise go to v := σ_(u+1)(s). EVEN-SPLIT gives κ_u(v) ≥ κ_u(s).
  - Odd s, case (I): go to v := σ̄_u(s).
  - Odd s, case (II): if og ≥ κ_u(s), stop at an ESCAPE (s, u): s leaves x because x's new play returns to s. Otherwise go to
    v := σ̄_(u+1)(s).
  - If v repeats, stop at a LOOP.
  - The keys met by the walk never decrease.
- Theorem ANCESTRY. Every change (z, u) has an ANCESTRY (z_0, u_0) = (z, u), (z_1, u_1), …, (z_d, u_d) with:
  - u_0 > u_1 > … > u_d;
  - κ_(u_(i+1))(z_(i+1)) ≥ κ_(u_i)(z_i);
  - each link given by the walk's E-root (s_i, z_(i+1), u_i) at u_i, with u_(i+1) chosen by ARM.
  It ends at an INIT switch, an ESCAPE or a LOOP. Proof: the walk, EVEN-SPLIT, ODD-KEY (I) / (II), and ARM. □
  - READING: going forward in time, a key can only drop along an ancestry. A more significant change must come from a source.
- Proposition LOOP-NEW (PROVED). A loop whose walk took no case (I) step has key (2, 0).
  - Proof. Every step of such a walk follows a new edge: unchanged prefixes, σ_(u+1), or σ̄_(u+1). So the loop L is a cycle of
    (σ_(u+1), σ̄_(u+1)), and all its keys are equal to some κ*. Let m be the top of L; then Ξ_(u+1) has cycle node m all along L.
  - Suppose κ* < (2, 0). Then the old cycle nodes are m as well.
  - If m is a walk vertex or a first changed vertex, its old and new values are both (m, ∅, 0), so it did not change: contradiction.
  - Otherwise m lies inside an unchanged prefix v_i … s_i. Then v_i's old and new plays share the prefix up to m, which is their cycle
    node, so Ξ(v_i) did not change: contradiction. □
  - Key-(2, 0) changes are cheap: the cycle-node reward rises strictly ([R15a]), so each vertex has at most n − 1 of them per N5 run.
- DATA (experiments/si/anc58/anc.py on the 1,132-game corpus of box 50b, every N5 transition):
  - 333,112 changes; PREFV 0, OLDV 0, EVENV 0, ODDV 0, ODD2V 0, ARMV 0 (62,937 armed switches; 11,139 INIT).
  - Walk roots: E 166,056, escape 77,256, loop 89,800. Of the loops, 87,421 are at (2, 0); all 2,379 below (2, 0) took a case (I) step
    (LOOPLOW0 0 on the whole corpus). Preferring x₂ in case (I) (anc.py --newpref) does not remove them: on the games that have them
    it cuts 1,510 such loops to 1,322.
  - Ultimate sources: 13,167 (INIT 6,628, escape 3,435, loop 3,104); at most 1,627 changes descend from one source.
  - On the quadratic pins the change counts are almost all fan-out. sbq2_K8_m16: 2,881 changes from 17 sources (16 INIT + 1 escape),
    one of which has 239 descendants. obs_K12_m24: 4,109 changes from 26 sources. latew_K16_m32: 9,297 from 33.
- CONJECTURE MIXED-LOOP (open): bound the loops below (2, 0), all of which have a case (I) step. They are a real residue (2,379).

## 4. Feeding, defined; Corollary NO-SELF-GAIN (PROVED, lane)
- Definition. Let a pair p = (y, z) have a fuel re-route at k with key a, and let k′ be its next one (or the end of the W-run).
  - HC(p, k) := {(z, u) : k ≤ u < k′, κ_u(z) > a}. These are FUEL-COUNT's higher-digit changes, charged in the window (k − 1, k′ − 1].
  - p FEEDS ITSELF at (z, u) ∈ HC(p, k) if the ancestry of (z, u) contains (i) an E-link whose root switch is a switch of y, or
    (ii) ends at an escape (s, u″) whose escaped cycle (x's new play from x back to s) contains y, with y switching at u″.
  - YONZ (box 57) is the special case where y lies on z's old play at k.
- Corollary NO-SELF-GAIN.
  - (1) Every E-link of an ancestry of a change with key κ is a switch with gain ≥ κ. By GAIN-DOWN, a fuel re-route of p with key a″
    can therefore be an E-link of an ancestry of (z, u) ∈ HC(p, k) only if a″ ≥ κ_u(z) > a.
  - So along E-links and relays, the recursion p(a) → HC → (gain > a) → (target change > a) → … returns to p only at a strictly higher
    level a″ > a: the earlier members of p's descending run (FUEL-LEX).
  - A cycle that returns to p at level ≤ a is impossible.
  - (2) Hence self-feeding by y's own fuel re-routes of key ≤ a goes only through escapes, way (ii).
- Correction to R161 §2 (a) (READING). After the switch y → z that closes a cycle, "Ξ(z) does not depend on y" is consistent. But the
  closing switch makes an Odd vertex of that cycle ESCAPE, and the escape itself is a change of Ξ(z) above a, in the same transition.
  - sbq2_K8_m16, pair (164, 166): fuel re-route at k 151 with key (1, 199); Odd 116 escapes with og (1, 260); Ξ(166) changes at (1, 260)
    at u 151.
  - So a pair can feed its own target's higher digits once per closure. A second time at the same level needs a more significant change
    of Ξ(z) in between (FUEL-LEX's argument).
- DATA (corpus):
  - 27,539 fuel re-routes (every Even switch, not only FS-selectors); GAINV 0. CHAINV 0 (no escape-free ancestry of an HC change has a
    re-route of its own pair at a key ≤ a among its E-links).
  - HC 8,892; self-feeding way (i) 2 (SELF1), way (ii) 443 (SELFESC; 441 at u = k). At most 2 per pair and W-run.
  - Max fuel per pair 18. YONZ 1,444.
  - Escapes inside W-runs (WESC): 1,434 distinct. 416 return to τ(s), 31 leave τ(s), and 12 escape a W-cycle (old choice τ(s), every
    other Odd vertex of the cycle on τ). Each quadratic pin has exactly ONE W-run escape.

## 5. DEAD (as a route): "no gain cycle ⇒ polynomial fuel". The instance and the barrier
- Instance: experiments/si/anc58/inst/switchallexp_N.pg (N = 1..6). Generated by `python3 experiments/hard-families/pgsolver_port.py
  switchallexp N`, byte-identical (cmp), with sha1 in inst/pins.sha1; n = 14N + 7. The algorithm is classical switch-all SI on si.py's VJ
  engine (best-reward start; si.py rule_switch_all; σ̄ by the same S1 procedure). anc.py --si treats the whole run as one W-run, with
  H_(k−1) = {σ_(k−1)} ∪ Iσ_(k−1).

  | N | n | iterations | PREFV / EVENV / ODDV / ODD2V / ARMV / GAINV / CHAINV | SELF1 / SELFESC | max ancestry depth / levels | escapes | MAXHC | max fuel of one pair |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | 1 | 21 | 10 | all 0 | 0 / 0 | 4 / 2 | 3 | 2 | 2 |
  | 2 | 35 | 30 | all 0 | 0 / 0 | 4 / 2 | 9 | 6 | 4 |
  | 3 | 49 | 70 | all 0 | 0 / 0 | 4 / 2 | 21 | 14 | 8 |
  | 4 | 63 | 150 | all 0 | 0 / 0 | 5 / 2 | 45 | 30 | 16 |
  | 5 | 77 | 310 | all 0 | 0 / 0 | 6 / 3 | 93 | 62 | 32 |
  | 6 | 91 | 630 | all 0 | 0 / 0 | 7 / 4 | 189 | 126 | 64 |

- Checks: si_sol.py's final strategies agree with Oink zlk, and both players' strategies are verified (check_sol2.py; si/anc58/oink_si.txt).
  The PGSolver port's switch-all SI, a second engine, takes 11, 31, 71, 151, 311, 631 iterations (pgs_si.txt): ours + 1, its final
  pass. NOT RUN: a state-by-state comparison with that engine (its valuation differs from VJ's, so states are not comparable 1:1).
  n5b / xeng are not involved, because this is not N5.
- What it shows (DATA): a single pair's fuel re-routes double per +14 vertices (2^N for N ≤ 6). This happens with NO self-feeding, NO
  gain cycle, ancestry depth ≤ 7 and ≤ 4 key levels. The recursion of FUEL-COUNT goes exponential by FAN-OUT from outside the pair, fed
  by escapes (3(2^N − 1)), not by cycling.
- Barrier (READING). §§1-4 and P-N5-ODD §6 (FUEL-LEX, FUEL-COUNT) use only [R15a], [R57], [PLAY] and [IMP], and classical SI satisfies
  all four. ([R15a] is the general SI monotonicity that P-N5-ODD §1 quotes as VJ00 Lemma 5.7; σ̄ is computed by the same procedure.)
  - So these lemmas, together with "no gain cycle" or "strict level climbing", cannot give a polynomial bound on pair fuel, HC or
    Ξ-changes.
  - A proof must use something N5 has and classical SI lacks: the fixed τ and constant λ_W of a W-run, and S4a's one-player optimum
    against τ.
  - The table is data for N ≤ 6, not a proof of growth for all N. Friedmann's published lower bound for switch-all SI was not opened in
    this box (L-LIT can supply it), so it is not cited as a source.
- The answer to the brief: the recursion does NOT cycle back to (y, z) with a gain through Even switches or relays (PROVED, §4), but
  that does not bound fuel polynomially (§5). No cycling instance is needed, and none was found. CHAINV is 0 in the corpus and on
  switchallexp.

## 6. What is left (REDUCTION, READING)
- By ANCESTRY, every Ξ-change of an N5 run descends, with keys non-increasing forward, from an INIT switch (≤ m per run), an escape or
  a loop (at (2, 0): cheap; mixed: open).
- A count needs two things: (a) escapes per W-run and mixed loops, and (b) fan-out per source, i.e. the number of descendants.
  - N5-specific DATA for (a): each quadratic pin has exactly one W-run escape, and escapes leaving τ are rare (31 of 1,434).
  - CONJECTURE ESC-W: in a W-run, an Odd vertex escapes from τ(s) only if the escaped cycle is not a W-cycle. Data: 12 exceptions
    (ESC_WCYC), so this needs care; the exceptions are unexamined.
  - (b) is where the quadratic pins live (one source with 239-444 descendants), and switchallexp shows it can be exponential when the
    escapes are.
- Next: bound the escapes per W-run using τ / λ_W (R161 §2 (a)'s W-cycle remark is the right tool there), and measure fan-out per
  escape on L-RED's re-arming cores.

## DONE / FINDINGS / NEEDS
- DONE: this note. Tools experiments/si/anc58/ (anc.py with --si and --newpref, agg.py, runanc.sh, si_sol.py). Outputs anc_sbcg.txt /
  anc_alt.txt (1,132 games), pins_out.txt, si_switchallexp.txt, oink_si.txt, pgs_si.txt. Pins inst/ (sha1). check.sh «box 58». DEAD.md
  «box 58».
- FINDINGS: see §§2-5. In one line each:
  1. PROVED (lane): keys never rise forward along prefixes, Even switches or Odd relays (Φ-KEY, KEY-PREF, EVEN-SPLIT, ODD-KEY, ARM,
     GAIN-DOWN, Theorem ANCESTRY); the sources are INIT, escapes and loops; loops without a case (I) step are at (2, 0).
  2. PROVED (lane): NO-SELF-GAIN. A pair cannot re-arm itself at its own level through Even links. Self-feeding goes only through Odd
     escapes, which corrects R161 §2 (a): corpus 443, at most 2 per pair.
  3. DEAD (route) + barrier: classical switch-all SI satisfies every lemma, with no self-feeding, yet one pair is re-routed 2^N times on
     switchallexp_N (N ≤ 6, Oink OK). Polynomiality must come from N5-specific structure (τ, W-runs, S4a).
  4. DATA: W-run escapes are rare on the quadratic pins (1 each). The open core is escapes per W-run plus fan-out per source.
- NEEDS: none from the owner. (L-LIT, via the Lead, if wanted: the source for Friedmann's switch-all lower bound, theorem number.)

## ERRATUM (same day; P-N5-ODD fixes entry 4)
- The sbq2_K8_m16 rows above used the invalid start (non-edge 242:243). On the repaired start sbq2_K8_m16_fix.start every count is the
  same except FUELEV 497 → 496; the pair (164, 166) self-feeding example is unchanged (SELFESC 2). check.sh «box 58» now pins the repaired
  start. The corpus lists name two other known-invalid starts (red/n3 comp54_n80, n3cov_lean; L-RED R99 erratum): with their *_fixed
  starts anc.py's counts are identical. A rerun of runanc.sh now prints START BAD for those two lines until the lists are switched.

## 7. Box 58 continued (Lead 14:47Z): which N5 property would exclude the switch-all escape engine inside one W-run (DATA, CONJECTURE)
Lead 14:47Z: «name the N5 property that your ANCESTRY chain would need to exclude the escape loop that powers switchallexp_N inside one
W-run. If you can prove that property, escapes per W-run are bounded.» Written 2026-10-31 from 14:5xZ (date -u; see commit).
- New anc.py fields (escapes = §3's escape roots, grouped by (W-run, Odd s, old choice x); SI: the whole run):
  - MAXESC_SX: max escapes of one (s, x).
  - ESCREP: repeat escapes.
  - ESCEQ / ESCASC: repeats whose swap key og equals / strictly exceeds the previous one's.
  - ESCNONMONO: sequences that mix strict ascents with non-ascents.
  - MAXPLAT: the longest run of consecutive equal swap keys (PLAT).
- The engine (DATA). Under classical switch-all SI, ONE Odd vertex escapes from ONE choice again and again at the SAME swap key:
  - switchallexp_N: MAXESC_SX 2, 8, 32 at N = 2, 4, 6, with ESCEQ = ESCREP = 1, 11, 57. For example, one (s, x) escapes at transitions
    3, 21, 41, 59, 81, … always with og (1, 74) (N = 6).
  - switchbestexp_N (new/box54/out), same SI: MAXESC_SX 8, 16, 32 at N = 4, 5, 6, ESCEQ = ESCREP.
  - MAXPLAT under SI: 1, 7, 31 (switchallexp, N = 2, 4, 6) and 7, 15, 31 (switchbestexp, N = 4, 5, 6), i.e. 2^(N−1) − 1.
  - These equal-key repeats are the carries of the counter.
- N5 on the SAME games: switchallexp_N has at most 1 W-run escape and 8-12 iterations. switchbestexp_N has MAXESC_SX 2 and ESCEQ N − 2
  (summed over all (s, x)) at N = 4, 5, 6 (47, 55, 62 iterations).
- N5 corpus (1,132 games; red/n3's two invalid starts replaced by their *_fixed files, list anc58/corpus_fixed.lst; output
  anc58/esc_corpus.txt):
  - 1,434 W-run escapes; 121 repeats = 58 equal-key + 54 strict ascents + 9 strict descents; ESCNONMONO 0.
  - MAXPLAT ≤ 1 on every game (21 games have 1).
  - MAXESC_SX is 24, on red/usplit pp_K48_n449: Odd 447 ping-pongs 441 ↔ 445 at every transition of a 55-transition W-run. τ(447) = 437
    is never used, the escaped 3-cycle has no Even vertex switching, and the swap keys strictly ASCEND (1, 393), (1, 395), …
    (ESCASC 45, ESCEQ 0). On
    pp_K12_n161 the figure is 6. Both are linear in K.
- CONJECTURE ESC-MONO (data 0 violations): inside one W-run, the swap keys of the successive escapes of one (s, x) are either strictly
  ascending throughout, or never ascend.
  - With ESC-MONO, the escapes of one (s, x) per W-run are at most (n + 2)(1 + PLAT), where PLAT is the longest run of equal swap keys.
    So escapes per W-run would be ≤ m(n + 2)(1 + PLAT).
- THE PROPERTY TO PROVE (named for the Lead): PLAT-POLY. Inside one W-run, an Odd s escapes from the same choice x at the same swap key
  only polynomially often (DATA: PLAT ≤ 1 under N5 on every corpus game, against 2^(N−1) − 1 under switch-all SI on switchallexp_N and switchbestexp_N).
  - Between two equal-key escapes of (s, x), s must RETURN to x: Odd's comparison of x and x₂ at the level og must be re-opened. By
    INT / FUEL-LEX's argument, that needs a change of Ξ(x) or Ξ(x₂) at a key > og between them, so the re-opening is itself a
    higher-digit event. This much is generic SI (it holds in switch-all too) and is not where N5 differs.
  - The N5-specific candidates (READING, unproved), which L-RED 38 is testing on the gadget:
    - (a) τ fixed and λ_W constant on the W-run, so the higher-digit event that re-opens x versus x₂ cannot be a W-cycle change.
    - (b) σ_(k+1) is Even's optimum in S4a's arena against τ. A carry that resets lower Even choices to a W-worse edge is then impossible
      inside a W-run, because it would lower W.
  - Proving (b) as «W_k is ⊴-monotone on a W-run and every equal-key re-opening of (s, x) needs a strict W-rise on x's or x₂'s W-play»
    would give PLAT ≤ (number of W-changes on those plays). That is the precise statement I would attack next.
- check.sh «box 58 §7» pins switchallexp_6 (SI ESCEQ 57, MAXPLAT 31), switchbestexp_5 (N5 ESCEQ 3, MAXESC_SX 2, MAXPLAT 1),
  pp_K48_n449 (N5 ESCASC 45, ESCEQ 0, MAXESC_SX 24) and the corpus (MAXPLAT ≤ 1, ESCNONMONO 0).

## 8. PLAT-POLY, the precise statement (Lead 18:36Z; L-RED 38 R164, claude/l-red 74bb2fec) (DATA, DEAD, CONJECTURE)
Written 2026-10-31 from 18:4xZ (date -u; see commit).
- Inputs from R164: Lemma W-MON (lane, L-RED: inside a W-run S4a is W-monotone, since σ_(k+1) is Even's optimum in an arena that contains
  σ_k); DATA: switch-all's carries are W-drops against τ; fbA_K8_m8_m8 (R164 pin) has PLAT 7 in one N5 W-run (so «PLAT ≤ 1» is dead).
  - L-SI check: WMONV 0 on all 1,132 corpus games, fbA_K8_m8_m8, pp_K48_n449 and switchbestexp_5 (W never drops inside a W-run).
- Statement tested (the Lead's wording of my candidate (b)): «inside a W-run, every equal-key re-opening of (s, x) needs a strict W-rise on
  x's or x₂'s W-play». Tool experiments/si/anc58/wrise.py: for consecutive escapes u1 < u2 of one (s, x) in one W-run, does W(x) or W(x₂)
  strictly rise from u1 to u2 (x₂ ranging over s's other choices in (u1, u2])? wplay.py widens this to the W-plays of x and x₂ at u1 and u2.
- DEAD as stated. Corpus: 121 repeats; 118 have the rise; 3 do not (2 at an equal key, 1 not). None of the 3 has a W-rise anywhere on the
  W-plays of x or x₂:
  - red/n3/instances/n3cov_lean.pg with n3cov_lean_fixed.start (L-RED R99's valid start): Odd s 35, x 29, escapes at 12 and 21, both with
    swap key (1, 44); τ(35) = 44.
  - red/n3/instances/n3cov_phi.pg with its start completed by n5x.start_pair (anc58/inst/n3cov_phi_full.start; the original is partial,
    R99): Odd s 14, x 13, escapes at 9 and 16, both (1, 26). Also s 7, x 30 at 3 and 7, keys (1, 24) then (1, 23).
  - Faithfulness: n5b (red/seg/xeng.py) state sequences identical on both (36 and 32 states); n5.py's solutions agree with Oink zlk, and
    both players' strategies verify (check_sol2.py).
  - Mechanism: in all 3, x is itself ODD and the escaped cycle is the 2-cycle s → x → s of two Odd choices (29 ↔ 35, 13 ↔ 14, 30 ↔ 7).
    W fixes Odd to τ, so W cannot see this cycle at all. W does rise elsewhere (36, 12 and 11 vertices) and on x's Ξ-plays, but not on its
    W-play.
- CONJECTURE W-REOPEN (data 0 violations): inside a W-run, if the escaped cycles of two consecutive escapes of (s, x) both contain an Even
  vertex, then W(x) or W(x₂) strictly rises between them.
  - Data: EVEN_NOWRISE 0 on the corpus (117 such repeats) and on fbA_K8_m8_m8 (28), pp_K48_n449 (45), switchbestexp_5 (3). The only
    exceptions to (b) are the 4 Odd-only repeats (ODDONLY 4, 3 without a rise).
  - With W-MON, W-REOPEN bounds the Even-cycle repeat escapes of one (s, x) per W-run by the number of strict W-changes at x and its
    alternatives. That is a W-run count, not yet a polynomial one: whether W changes per vertex per W-run are polynomial is open here.
- Odd-only escapes (both escaped cycles purely Odd): a separate residue, 4 repeats in the corpus. They are Odd's best response
  re-deciding between two Odd vertices that point at each other. W-REOPEN does not cover them.
- Next: prove W-REOPEN. Planned route: at the first escape, x's new Ξ-play returns to s through an Even vertex e. By [R57] with ρ = τ,
  Ξ ⊴ W, and W-MON keeps W(e) from falling. A re-opening at the same swap key needs Ξ(x) or Ξ(x₂) to come back across the same digit
  (INT), and the claim is that this is only possible if the W-values bounding them from above move.
