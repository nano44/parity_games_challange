# Box 105 (D18; O2 of box 104, proof side): N5's key rule on free-priority genomes — the model KEY(G*), its equivalence with N5 (Lemma KEY-MODEL), key monotonicity and a depth bound
L-SI successor 52 (Fable 5.2), D18 / D14 / D1; Lead rulings 2026-11-12 17:16Z («O2 and O3 stay with YOU, on the proof side: write the
statement O2 would need («N5's key rule on free-priority genomes is …») and try to prove or refute it on small cases») and 17:27Z («go»
with four changes: KEY-MODEL's proof first; GLO-1P stays a CONJECTURE and WRAP-GLO a READING, a primary source on one-player policy
iteration or «no source opened»; D2 checks regions and S3-standardness on every genome; commit by section).
Labels: PROVED (L-SI lane, unrefereed) / CONJECTURE / DATA (counter, unit, set, scope) / DEAD / OPEN / READING.
**SCOPE LINE: nothing here is a TARGET.md claim, M3 or M4, or a gauntlet step. G-N5-TIME stays OPEN. Every statement is about N5 (SPEC
S1-S5 with FIX 1-4) from its default start S3 on the games Γ3*(G*) of box 104 §4, up to the first fallback; nothing is claimed about
any other game.**
D1 (owner, verbatim): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the
fleet's own, as wrong until it passes the gauntlet below.»
This file was first pushed as the LEMMA SECTION (§0-§3; Lead 18:06Z: «push the lemma section on its own»); §4 D1 added by successor 53. Tools in it: experiments/si/box105/
quotes105.py (the [Q] strings at their sources and in this file) and check105.sh; «BOX 105» in experiments/si/check.sh. The files
key105.py (the direct simulator of KEY(G*)), ladder105.py, chain105.py and run105.sh are committed as tools only, WITHOUT outputs,
and check105.sh did not run them at that commit; D1's outputs and §4 came with successor 53's commit, D2 / D3 follow later.

## 0. What this box is for, and what stands after its first sections
- O2 (box 104 §8, KEY-FREE): is the first fallback F* of N5 from S3 on Γ3*(G*) polynomial in N + M for every free genome G*? It is
  necessary for G-N5-TIME (box 104 §4, FREE-REACH (e): N5 makes exactly F* + 2 iterations there) and contains O1 and O1′.
- §1 states the rule that N5 is on these games as a rule on the genome alone: KEY(G*). §2 proves that N5's run is KEY(G*)'s run, state
  for state (Lemma KEY-MODEL), from landed premises named by R-id and from box 104's Lemma FREE-REACH (lane, unrefereed). Until
  KEY-MODEL is refereed, every number produced by key105.py is «L*(G*) of KEY(G*), equal to N5's run on the validated set only».
- §3 proves two facts about KEY(G*) that use no priority at all: every mover's key only decreases (KEY-MONO*), and the run has at most
  Π_ℓ (1 + w_ℓ·(Δ − 1)) − 1 steps on a genome with w_ℓ movers on level ℓ and at most Δ options per mover (DEPTH-BOUND*). So O2 holds
  on free genomes of bounded depth, and a kill family for O2 needs unboundedly many levels.
- O2 itself stays OPEN.

## 1. Definitions
- FREE genome G* = (G, π), the game Γ3*(G*), its rank order (R*) and its standard states: box 104 §4, unchanged. Notation: movers x
  with levels lev(x) ∈ {0, …, d − 1}; options (x, k), k < deg(x); wt(x, k) the W-target (a mover of level lev(x) − 1; none at level
  0); xt(x, k) the Ξ-target (a mover or X); gate(x, k) the gate index (distinct over all options); the start s_0. The STANDARD STATE
  of a mover state s (one option per mover) is the pair (σ_s, τ0): σ_s(x) = m_(x, s(x)) at every mover, every β on its Ξ-target (on
  pb when the target is X), K0 → pA, K1 → s, K3 → K2; τ0 = pe at every gate and K2 → K2.
- KEY of an option under a mover state s: key_s(x, k) := key_s(wt(x, k)) followed by gate(x, k), where key_s(y) := key_s(y, s(y))
  and the key of «no W-target» is the empty sequence. So key_s(x, k) is the sequence of gate indices of the chain of W-targets
  below (x, k) under s, lowest level first; it has lev(x) + 1 entries and depends on s only through the movers of level < lev(x).
  Keys are compared lexicographically. Two options of one mover never have equal keys (their last entries differ).
- VALUE of an option under s: V_s(x, k) := Ξ_(σ_s)(m_(x,k)), SPEC S1's valuation of the pad m_(x,k) of Γ3*(G*) under σ_s and Odd's
  optimal counterstrategy. AVAILABLE options: A_s(x) := {s(x)} ∪ {k : V_s(x, k) ▷ V_s(x, s(x))}.
- **Definition KEY(G*).** The run s_0, s_1, … with s_(j+1) defined from s_j level by level, lowest level first: s_(j+1)(x) := the
  option k ∈ A_(s_j)(x) with the least key_(s_(j+1))(x, k) (the key reads the NEW choices of the lower movers, the value the OLD
  state). The run stops at the first j with s_(j+1) = s_j; L*(G*) := that j.
- On an R104 genome with an acyclic Ξ-graph this is R104's IDEAL run and L* = L(G): [Q] R104 «an IDEAL step moves every mover to the
  lexicographically least key (gate indices of the chain of W-targets under the new state, lowest level first) among its current
  option and the options with a strictly better Ξ-value, and the run stops when nothing is available or nothing changes», with
  R104's Ξ-value (the β-set of the Ξ-chain) in place of V_s; the two agree there by R117's SBAR3, PLAY3 and KEY3 (a). On a free
  genome V_s has no such closed form: Odd may answer on the e-face of a gate, so the inner game is two-player.

## 2. Lemma KEY-MODEL (PROVED, lane; from landed premises and box 104's FREE-REACH)
**Lemma KEY-MODEL.** For every free genome G*, under the standing SPEC premise 1E-N3 (RESULTS R57 (b), in the two forms of R104) and
R104's premise [RULE] (RESULTS R24 (a) Lemma R and R24 (b)'s choice rule with R103's bridge B and (R1) ruling): the N5 run from S3
on Γ3*(G*) has states 0, …, L* equal to the standard states of s_0, …, s_(L*) of KEY(G*); its transitions 1, …, L* are not
fallbacks; transition L* + 1 is its only fallback (F* = L* + 1); it makes exactly L* + 3 iterations.
Proof. Induction on j: state j is the standard state of s_j.
- j = 0: FREE-REACH (a) (S3-START on Γ3*).
- Step j → j + 1, j < L*. τ: Iτ = ∅ in a standard state (FREE-REACH (b)), so S4b leaves τ, and S4c would change τ only if Iσ = ∅. σ
  off the movers: σ_new = σ there (ESC3-ALL, in FREE-REACH's table: it uses c_W even and K1, K2 odd only). At a mover x: by W3-ALL
  (same table: «every e < c_W») every option of x has the same arena value and x is not its own cycle node, so TIE(x) = R(x) :=
  {σ(x)} ∪ Iσ(x); by SPEC S2, (x, m_(x,k)) ∈ Iσ iff Ξσ(m_(x,k)) ▷ Ξσ(σ(x)), so R(x) = {m_(x,k) : k ∈ A_(s_j)(x)} by the definition
  of V and A (this replaces KEY3 (a), whose proof uses SBAR3 and so E-DOM). By [RULE], σ_new(x) is the κ-least element of TIE(x),
  κ the root-first key under (σ_new, τ0). By RESULTS R117's Lemma KEY3 (b) (P-N5-REACH §6.7 (b), INDEX): for options y, y′ of x and
  any σ′ that is standard on the movers of level < lev(x), κ(y) < κ(y′) iff the gate-index sequences compare that way. Its proof
  reads only the τ0-play m → g → pe → e → (mover one level down) → … → c_W and the vertex INDICES ([Q] «a gate determines its pad,
  its owner and its faces», [Q] «e-indices follow gate indices ([DEF]; unchanged in Γ3)»); it uses no priority, and Γ3*(G*) has
  R117's vertices, indices and edges. So, by induction on the level, σ_new(x) = m_(x, s_(j+1)(x)): state j + 1 is the standard
  state of s_(j+1). It differs from state j (j < L*), so S4c does not fire.
- Step L*. s_(L*+1) = s_(L*): the same argument gives σ_new = σ and τ_new = τ, while Iσ ∋ (K0, K1) (K3 (b)): S4c fires. The rest is
  FREE-REACH (e) (ENDGAME-3-N5 read on Γ3*): one fallback, F* + 2 = L* + 3 iterations. ∎
- What the proof rests on: landed R57 (b), R24, R103 (premises), R117 (KEY3 (b), K3), R124 (ENDGAME-3-N5), R125 (ESC3-ALL, W3-ALL),
  each through box 104 §4's reading of its proof without E-DOM. That reading is lane work, unrefereed; KEY-MODEL is as good as it.
- Finiteness of L*: N5 terminates (RESULTS R15 (d)), and the induction realises every KEY step as an N5 transition.

## 3. Two facts about KEY(G*) that use no priority (PROVED, lane)
**Lemma KEY-MONO\*.** Along KEY(G*), for every mover x and every step j → j + 1: key_(s_(j+1))(x) ≤ key_(s_j)(x), with < if
s_(j+1)(x) ≠ s_j(x).
Proof, by induction on lev(x). Write s = s_j, s′ = s_(j+1), k = s(x), k′ = s′(x). The key of x's option (x, k) under s′ is
key_(s′)(wt(x, k)) followed by gate(x, k); by induction (or because there is no W-target) its first part is ≤ key_s(wt(x, k)), so
key_(s′)(x, k) ≤ key_s(x, k) = key_s(x) (sequences of equal length; a smaller or equal prefix with the same last entry). k′ is the
key-least element of A_s(x) ∋ k under s′, so key_(s′)(x) = key_(s′)(x, k′) ≤ key_(s′)(x, k), with < if k′ ≠ k (distinct options
have distinct keys). ∎
**Lemma DEPTH-BOUND\*.** Let G* have levels 0, …, d − 1, w_ℓ movers on level ℓ, and at most Δ options per mover. Then
L*(G*) ≤ Π_(ℓ=0)^(d−1) (1 + w_ℓ·(Δ − 1)) − 1.
Proof. Number the steps t = 1, …, L* (step t is s_(t−1) → s_t). Say that a mover y has a KEY CHANGE at step t if key_(s_t)(y) ≠
key_(s_(t−1))(y), and let C_ℓ be the number of steps at which some mover of level ≤ ℓ has a key change (C_(−1) := 0).
- (A) L* = C_(d−1): every step t ≤ L* moves some mover, and a mover that moves has a key change (KEY-MONO*).
- (B) A mover x of level ℓ moves at most (Δ − 1)·(C_(ℓ−1) + 1) times. The steps at which some mover of level ≤ ℓ − 1 has a key
  change cut {1, …, L*} into at most C_(ℓ−1) + 1 intervals, each starting at such a step (the first one at step 1). The key of an
  option (x, k) under s_t depends on s_t only through the keys of the movers of level ℓ − 1 (none if ℓ = 0), so for all t of one
  interval I it is one and the same function κ^I of k. If x moves at t ∈ I, then s_t(x) is the κ^I-least element of a set that
  contains s_(t−1)(x) and differs from it, so κ^I(s_t(x)) < κ^I(s_(t−1)(x)). Between two moves x's option does not change. So along
  the moves of x inside I the value κ^I(current option) strictly decreases; κ^I takes at most Δ values: at most Δ − 1 moves in I.
- (C) If a mover y of level ℓ has a key change at step t and does not move at t, then its W-target wt(y, s_t(y)), of level ℓ − 1,
  has a key change at t (key_s(y) is key_s of that W-target followed by a gate index that did not change). So every step counted
  in C_ℓ and not in C_(ℓ−1) is a step at which a mover of level ℓ moves: C_ℓ ≤ C_(ℓ−1) + w_ℓ·(Δ − 1)·(C_(ℓ−1) + 1) by (B), i.e.
  C_ℓ + 1 ≤ (C_(ℓ−1) + 1)·(1 + w_ℓ·(Δ − 1)). With (A), L* + 1 ≤ Π_ℓ (1 + w_ℓ·(Δ − 1)). ∎
- Corollaries. (1) For every fixed depth d, O2 holds on the free genomes of depth ≤ d: L* ≤ (1 + N·(Δ − 1)/d)^d − 1 (AM-GM), a
  polynomial in N + M of degree d. (2) A family of free genomes with L* super-polynomial in N + M has unboundedly many levels. (3)
  With one mover per level and Δ = 2 the bound is 2^d − 1; with two movers per level and Δ = 2 it is 3^d − 1. On R110's ladder
  genomes 𝓛^R_d (IDEAL, E-DOM) the landed bound is sharper: [Q] R113 «(T-BOUND) on 𝓛^R_d, F(l) ≤ 2^(l+2) − 2».
- Neither lemma uses V, π, the Ξ-targets or the start: they hold for ANY rule of the form «move to the key-least element of a set
  that contains the current option». What the values decide is which sets occur; that is where O2 lives.
- VAL-MONO* (from a published theorem): V and every other value of Ξσ never decrease along the run. A KEY step keeps every vertex
  inside the improvement arena (current or strictly better successors) and switches at least one improving edge, so it is the
  value of an improvement policy in the sense of [F11] §3 (arXiv 1106.0778v2), and [F11] Theorem 3.2 (from VJ00) applies to
  Γ3*(G*); SPEC's own form is RESULTS R15 (d). Its DATA counter (valmono) comes with D1.
- With adversarial sets (any set that contains the current option, at every step) the bound of DEPTH-BOUND* is the right order on
  the ladder shape: L-RED's ladderbf.py (claude/l-red 707c0e82, experiments/red/r177) computes the longest such chain; the DATA
  commit reports its numbers next to 3^d − 1. Whether sets that come from VALUES can come near it is O2.

## 4. DATA: D1 (key105.py, the direct simulator of KEY(G*), against N5 from S3; run105.sh, outputs experiments/si/box105/out/)
Label of every number below (Lead 17:27Z, 18:06Z): «KEY(G*), equal to N5's run on the validated set only» — until KEY-MODEL (§2) is
refereed, a KEY(G*) count is a statement about N5 only on the genomes listed here, where it was compared state by state. Run:
`bash experiments/si/box105/run105.sh` (L-SI successor 53, finished 2026-11-12T20:57Z by date -u; engines n5v.py mode spec at claude/l-new
fcba92fc and box 104's free104.py / freereach104.py, read-only). The lines below are the tool's output lines, inserted by script.
- Counters (key105.py header): keymono (unit (step, mover): the mover's key under the new state is lexicographically larger than under
  the old state, or the mover moved and its key did not strictly decrease: KEY-MONO*), valmono (unit (step, vertex of Γ3*): a valuation
  decreased); validation, unit genomes: s3fail (S3's pair is not the standard state of the start), keyfail (some state 0..L* of the N5
  run does not carry KEY's state at the movers, or the first fallback is not at L* + 1), endfail (fallbacks ≠ 1 or iterations ≠ L* + 3),
  wrong (regions ≠ harness Zielonka). Control CTRL=1: keys read under the OLD state (keyfail must fire).
- Random FREE genomes (box 104's freereach104.rand_free; SEED, COUNT, depth ≤ DMAX, movers per level ≤ WMAX, degree ≤ DEGMAX):
  «KEY105 rand seed 1051 genomes 2000 d<=4 w<=3 deg<=3: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | max L* 4 sum L* 1485 max |V| 217»
  «KEY105 rand seed 1052 genomes 1000 d<=6 w<=4 deg<=3: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | max L* 4 sum L* 1008 max |V| 332»
  «KEY105 rand seed 1053 genomes 1000 d<=8 w<=2 deg<=2: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | max L* 3 sum L* 523 max |V| 208»
- Control (fires: keyfail 14, endfail 8 of 200):
  «KEY105 rand seed 1051 genomes 200 d<=4 w<=3 deg<=3 CTRL 1: s3fail 0 keyfail 14 endfail 8 wrong 0 keymono 0 valmono 0 | max L* 4 sum L* 158 max |V| 182»
- The lane's frozen R104 genomes with R104's own (E-DOM) priorities (box 91, box 93, box 98 instances; one SKIPPED by design: box
  93's Kprev_8 has an option whose W-target is not one level down, so it is not a genome in R104's sense and KEY is not defined on it):
  «KEY105 json WC4_2.json (E-DOM priorities) N 20 M 40 |V| 310: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 2»
  «KEY105 json WC16_2.json (E-DOM priorities) N 68 M 148 |V| 1114: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 2»
  «KEY105 json FW8_2.json (E-DOM priorities) N 123 M 248 |V| 1869: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 28»
  «KEY105 json FW16_2.json (E-DOM priorities) N 259 M 528 |V| 3965: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 52»
  «KEY105 json MW8_2.json (E-DOM priorities) N 84 M 177 |V| 1333: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 52»
  «KEY105 json MW32_2.json (E-DOM priorities) N 300 M 657 |V| 4909: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 196»
  «KEY105 json C6G8_n54.json (E-DOM priorities) N 54 M 150 |V| 1114: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 3»
  «KEY105 json RWX_n95.json (E-DOM priorities) N 95 M 233 |V| 1736: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 3»
  «KEY105 json DWT20_2803.json (E-DOM priorities) N 102 M 262 |V| 1946: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 2»
  «KEY105 json DHIB26_2804.json (E-DOM priorities) N 108 M 292 |V| 2162: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 3»
  «KEY105 json DHIB18_2805.json (E-DOM priorities) N 99 M 301 |V| 2216: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 3»
  «KEY105 json Kprev_8.json: SKIPPED, not a genome in R104's sense (some W-target is not one level down), so KEY(G*) is not defined»
  «KEY105 json Ku_16.json (E-DOM priorities) N 156 M 337 |V| 2525: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 100»
  «KEY105 json Ku_4.json (E-DOM priorities) N 48 M 97 |V| 737: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 28»
  «KEY105 json Ku_8.json (E-DOM priorities) N 84 M 177 |V| 1333: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 52»
  «KEY105 json MWR16_2.json (E-DOM priorities) N 156 M 337 |V| 2525: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 100»
  «KEY105 json MWR4_2.json (E-DOM priorities) N 48 M 97 |V| 737: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 28»
  «KEY105 json MWR8_2.json (E-DOM priorities) N 84 M 177 |V| 1333: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 52»
  «KEY105 json k1fail_202.json (E-DOM priorities) N 15 M 45 |V| 340: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 1»
  «KEY105 json C98_2_2_3.json (E-DOM priorities) N 4 M 10 |V| 84: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 1»
  «KEY105 json C98_2_3_3.json (E-DOM priorities) N 6 M 14 |V| 114: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 4»
  «KEY105 json C98_3_3_3.json (E-DOM priorities) N 9 M 22 |V| 173: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 1»
  «KEY105 json C98_3_4_3.json (E-DOM priorities) N 12 M 29 |V| 225: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 0»
  «KEY105 json C98_4_4_3.json (E-DOM priorities) N 16 M 40 |V| 306: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 1»
  «KEY105 json C98_4_5_3.json (E-DOM priorities) N 20 M 52 |V| 394: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 2»
  «KEY105 json C98_5_5_3.json (E-DOM priorities) N 25 M 59 |V| 448: s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0 | L* 2»
- Summary: all six must-0 counters are 0 on 4,000 random free genomes (max L* 4) and on 25 frozen E-DOM genomes (L* from 0 to 196,
  the largest on MW32_2.json with |V| = 4909); the control fires. So key105.py agrees with N5 state by state on these genomes (L* + 3 = N5's
  iterations, first fallback at L* + 1, regions correct) and KEY-MONO* (keymono 0) and the valuation monotonicity (valmono 0) on them.
  It is DATA: it bounds nothing. The random free genomes are small (L* ≤ 4); the long runs (L* 52-196) are the lane's frozen E-DOM instances (families
  FW, MW, MWR, Ku), i.e. R104 genomes, not free ones. D2 (search for long free runs against the ceiling) follows in a later commit.

## 5. Questions, and what is not done
- LAG* (how many steps a level-ℓ mover can be behind level ℓ − 1; the tower's doubling needs it): not stated yet.
- Question (Lead 17:27Z change 2): «Is the globally optimizing rule covered by such a bound?», i.e. by a published bound for policy
  iteration on ONE-player games. One primary source opened so far, on the neighbouring rule: Asadi, Chatterjee, de Raaij, «Lower
  Bound on Howard Policy Iteration for Deterministic Markov Decision Processes», arXiv 2506.12254v1 (pdf sha256 78c4ee071961b89e…).
  It is about HOWARD's rule on one-player games with the MEAN-PAYOFF objective. Its Theorem 3.2 (Main Result): a family with 2n
  vertices and (3n² + n)/2 edges on which Howard's algorithm performs (n² + 7n − 6)/2 iterations; its abstract: «the best known upper
  bound is exponential»; its Conjecture 3.1, quoted from Hansen's thesis ([Hansen, 2012, Conjecture 6.1.1]): «The number of iterations
  performed by Howard’s algorithm, when applied to a DMDP, is at most the number of edges.», called there «a major open problem». The
  paper does not treat the globally optimizing rule and does not treat parity valuations (its text has no «globally»; «parity» occurs
  once, in a reference title). So: NOT covered by the one source opened; CONJECTURE GLO-1P (box 104 Addendum B.3) stays a conjecture
  with no published bound known to me in either direction. A second source to open: Hansen and Zwick, ISAAC 2010 (DOI
  10.1007/978-3-642-17517-6_37), NOT opened (no open copy found); the paper above reports its bound as m − n + 1 iterations.

## 6. Sources opened (this box)
- Trunk a9699c30c docs/RESULTS.md: R104 (title line: the IDEAL model), R113 (title line), R117 (title line); R15, R57 as in box 104.
- claude/l-new 8db300fe docs/new/P-N5-REACH.md §6.6 (W3), §6.7 (KEY3), §7 (Theorem REACH3).
- docs/si/box104-map.md §4 (this lane).
- arXiv 1106.0778v2 (as in box 104): §3 (the definition of an improvement policy), Theorem 3.2.
- arXiv 2506.12254v1 (PDF fetched from arxiv.org, sha256 78c4ee071961b89e4f1aa51559eaafda34493162a06bbb91be1b91d088f66301; pdftotext):
  abstract, §1 (known bounds), Conjecture 3.1, Theorem 3.2, the conclusion.
