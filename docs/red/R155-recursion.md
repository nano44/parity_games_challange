# R155: the two-level recursion the brief asks for ADDS. When the upper selector's dynamic options all take their value from ONE lower vertex, its switches are bounded by its own degree, whatever the lower level does. PROVED (lane), Lemma ONE-SOURCE: if h's options split into K_0 static options and K_1 options that reach one common source u through fixed prefixes, then in a W-run h switches at most K_1(K_0 + 1) + K_0 times, however often W(u) or Ξ(u) changes. No gate is involved. Instance src1_K4 (n 289): the source (Even 247 of obs_K12_m24) changes W 301 times in ONE 325-transition W-run, and h2 switches twice (bound 24). Also PROVED (lane): GATE-r with dynamic branches (≤ r(1 + B), B = transitions with a branch change), which is multiplicative, so gates are not the obstruction. The obstruction is the COMMON SUFFIX. A product needs ≥ 2 dynamic sources whose values leapfrog at every level (READING); not built
L-RED successor 36 (Opus 5.5; D1/D18). Lead 2026-10-31 04:52Z: «R155 … build two levels of recursion: the lower level is a selector h1
with gated options (as in sgate) whose switches are driven by an observer; each option λ_j of the upper selector h2 takes its Ξ from h1's
current choice, so Ξ(λ_j) changes every time h1 switches. Test whether h2's switches reach (h1's switches) × r, or anything super-linear
in n, in ONE W-run … If it adds rather than multiplies, prove the lane lemma that says why … state its premises exactly.» Written
2026-10-31 from 05:10Z (date -u).
- Labels: PROVED (lane) / DATA / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.
- Sources opened: docs/red/R154-gates.md (GATE-r); docs/si/P-N5-SETTLE-box52.md §4 (W-MON); R151 §3 (O2, «a common suffix cancels in B's
  comparisons», which this note turns into a lemma).

## 1. Lemma GATE-r^dyn (PROVED, lane): gates multiply
- Setting and notation as R154 GATE-r, but with Λ_j and Ω_j allowed to change. B := the number of transitions of the τ-stretch at which
  some Λ_j or some Ω_j changes. An EPOCH is a maximal interval of states on which all Λ_j and Ω_j are constant.
- Statement. h switches at most r(1 + B) times.
- Proof. There are ≤ 1 + B epochs. Inside one epoch every hypothesis of GATE-r holds. GATE-r's proof compares only two landings k < k′
  whose states, and the states k + 1, k′ + 1, lie in the epoch, plus the monotone chain of landing values, which holds everywhere. So an
  epoch has ≤ r landings. □
- So a selector driven by r signals CAN switch r times per epoch, and epochs come for free from a lower level that moves the branches.
  As far as gating goes, the Lead's product (h1's switches) × r is allowed. What blocks it is §2.

## 2. Lemma ONE-SOURCE (PROVED, lane; L-RED successor 36)
- Setting. A W-run F of an N5 run (τ, λ_W fixed; W-MON). An Even vertex h ∉ C with successors split into two classes:
  - class 0 (static), K_0 options b: W(b) is constant on F;
  - class 1 (one source), K_1 options a: a's (σ, τ)-play is a FIXED prefix a = p_0 → … → p_t = u, the same vertex u for every class-1
    option, and then u's play. «Fixed» means no Even vertex of the prefix switches in F.
- Hypotheses:
  - (S1) no play from an option passes h;
  - (S2) at every state of F the options of h have pairwise distinct W-values.
- Statement. h switches at most K_1(K_0 + 1) + K_0 times in F. The bound does not depend on how often W(u), Ξ(u) or the gates at h change.
- Proof.
  - (i) Common-suffix cancellation. Each class-1 value is W(a) = (c, P_a ∪ Q_u, |prefix| + ℓ(u)), where Q_u is u's path set and P_a is
    the prefix's set of vertices more relevant than c. The prefix vertices are not on u's play: otherwise a's play would close a cycle
    avoiding c, against λ_W(a) = c. So P_a ∩ Q_u = ∅, and for two class-1 options P_a ∪ Q_u Δ P_a′ ∪ Q_u = P_a Δ P_a′, and the length
    difference is |prefix_a| − |prefix_a′|. The order of the class-1 options is therefore the same at every state of F. Call it ≺_1.
  - (ii) Landings strictly raise W(h). At a switch k → k + 1 from x to y, x is in the arena. S4a takes the pointwise optimum, so
    W_(k+1)(y) ⊵ W_(k+1)(x), strictly by (S2). By W-MON, W_(k+1)(x) ⊵ W_k(x). So W_(k+1)(h) = h ⊕ W_(k+1)(y) ▷ h ⊕ W_k(x) = W_k(h). (S1)
    makes h ⊕ · the value at h.
  - (iii) Each static option is landed at most once: a second landing on b would give W(h) = h ⊕ W(b) twice, against (ii).
  - (iv) Between two consecutive class-0 landings, and before the first and after the last, the landings are all class 1. Inside such a
    block each landing a → a′ has W_(k+1)(a′) ▷ W_(k+1)(a) (a is current, so in the arena), hence a ≺_1 a′ by (i). A block therefore has
    ≤ K_1 landings, and there are ≤ K_0 + 1 blocks.
  - Total ≤ K_0 + K_1(K_0 + 1). □
- The brief's design is exactly this setting. Every λ_j of h2 takes its value from h1's current choice through a fixed prefix, so all
  dynamic options share the source u = h1. However often h1 switches (even if every switch changes Ξ(λ_j), so GATE-r^dyn would allow it),
  h2 re-climbs only between distinct static options. h1's rises lift the whole class 1 at once, including h2's current option, and
  nothing in class 1 can be re-entered from below.
- Premises used: W-MON and S4a's pointwise optimum (ARENA-MAX), both signed (P-N5-SETTLE §4, L-RED R140); the W-run definition (RESULTS
  R89). Gates, Ξ and τ-behaviour are not used. The lemma holds for any arena rule.

## 3. DATA
- Instance wlev/instances/src1_K4 (wlev/mksrc1.py on red/xich/instances/obs_K12_m24; priorities rescaled p → 4p + (p mod 2)):
  - source u = the Even observer 247, whose W rises 301 times (top relevant vertex 752 → 800);
  - h2 has 4 class-1 options da_j → mda_j (odd markers just above z) → 247, and 4 static options sb_i → msb_i (even markers between the
    source's levels, rescaled 4y + 2 for y = 760, 770, 780, 790) → M.
  - wlev/srctrace.py: «SRC1 src1_K4.pg n 289 iters 325 wruns 1 maxL 325 tau-changes 0 WCH(SRC) 301 h2-switches-in-F 2 (all 2) landings
    ['sb4', 'da4'] W(h2)-not-rising 0 bound 24 (K1 4, K0 4)».
  - xeng: state sequences identical. Oink 8fbf0a7: OK.
  - h2 jumps once to the best static option, and later once to the best class-1 option when the source passes it. The static options
    in between are skipped (ARENA-MAX). 301 source rises give 2 switches.
- Variant with 5 static options (y = 755 … 795): 2 switches, bound 29 (not pinned).

## 4. What a product needs (READING)
- By ONE-SOURCE, a selector h re-climbs class 1 only after a landing outside it. A product over levels needs ≥ 2 DYNAMIC classes with
  sources u, u′ whose class values overtake each other again and again. Then h alternates blocks between the classes, and each block
  climbs up to K. Each alternation needs a W-overtake between the two sources' shifted values, i.e. a leapfrog of W(u) and W(u′).
- So the recursive counter needs, at every level, a PAIR of lower vertices whose W leapfrogs as often as the level above wants to
  switch. R154 §1 measured W-order flips of a successor pair in one W-run: at most 24 on every pin (linear). GATE-r^dyn shows gates do not
  forbid this.
- Next attack: a two-source selector whose sources are two copies of a lower selector, run out of phase. That is Friedmann's
  two-lane bit shape inside one W-run. ONE-SOURCE's proof does not extend to two sources. Whether the W-leapfrog count of a pair is
  bounded additively by its own W-changes (each overtake needs a rise of the overtaker, so flips ≤ WCH(u) + WCH(u′)) or can be made to
  multiply up the levels is the open question. It is R95's XI-CH-POLY / R* in its sharpest form.

## 5. Pins (experiments/red/check.sh «R155»)
- wlev/pins.sha1 (adds src1_K4); srctrace line above; xeng; Oink.

## DONE / FINDINGS / NEEDS
- DONE: this note; wlev/mksrc1.py, wlev/srctrace.py, wlev/instances/src1_K4; check.sh «R155». SHA: see the commit.
- FINDINGS:
  - PROVED (lane): ONE-SOURCE. Options sharing one dynamic source give ≤ K_1(K_0 + 1) + K_0 switches, so the brief's two-level
    recursion adds.
  - PROVED (lane): GATE-r^dyn (≤ r(1 + B); gates allow products).
  - DATA: src1_K4, 301 source rises → 2 switches (xeng, Oink OK).
  - READING: a product needs two leapfrogging dynamic sources per level.
- NEEDS: none.
