# N5 on 𝒞^1O: the G-N5-TIME ledger (box 14)
L-SI successor 9 (Opus 5.5; D18, L40), session_018jN1MJkw56F58G3qcfcuZA. Written 2026-10-25 18:32Z (date -u). Lead's GO 18:25Z, item (1).
- What this is: READING. It is a map of the chain from the landed results (RESULTS R15-R42) to a polynomial bound on N5's iterations on
  𝒞^1O, written as inequalities, each with a status. It is not a proof, not a TARGET.md claim, and not a step-4 pass. G-N5-TIME stays
  OPEN. NO polynomial bound for N5 is proved, on 𝒞^1O or anywhere else.
- Status labels:
  - LANDED Rnn: a RESULTS entry, signed by two referees.
  - SIGNED-IN-LANDING: signed by both referees, not yet in RESULTS.
  - IN REVIEW: pinned, with one or no signature.
  - LANE-PROVED: a lane's proof, unrefereed (lane named).
  - CONJECTURE; OPEN; DATA.
  - READING (L-SI 9): an inference first written here.
- Statuses were taken from trunk e358c6b5 (RESULTS, GAPS row G-N5-TIME, docs/agents/LEAD-STATE.md up to 18:21Z) and from the packets'
  own headers.
- Setting: 𝒞^1O, i.e. exactly one Odd vertex o with out-degree d = d_o > 1. Priorities are injective (SPEC, docs/new/N5-ssi-global.md
  l.27). n_E is the number of Even vertices.
- A PHASE is a run with λ_Ξ and τ constant. By R38 (a) KEY it is the same thing as a joint λ-phase with τ constant.
- T := n² + 2n − 1 bounds the H1-toggles of a phase (R34 (e)).

## 1. The top of the chain (phases)
| # | inequality | status |
| --- | --- | --- |
| L0 | #iterations ≤ Σ_phases (T_P + 1) | definition (every transition lies inside a phase or ends one) |
| L1 | #phases ≤ #(λ_Ξ-changing transitions) + #(τ-changing transitions) + 1 | definition + R38 (a) KEY (λ_U is a function of τ) |
| L2 | #(λ_Ξ-changing transitions) ≤ n(n − 1) | Lemma Φ, LANE-PROVED (L-NEW box 21, docs/new/N5-time-box21.md §2.3), **never refereed**; see §5 |
| L3 | #(τ-changing transitions) ≤ d − 1 | READING checked by REFEREE (R21 "Consequence"; R15 (c), (d) on G^d: τ never repeats, and τ lives on o's d edges) |
So #phases ≤ n(n − 1) + d. **The polynomial question is the length T_P of one phase.**

## 2. One phase: T_P in terms of crossings X, wakes K and fallbacks f
| # | inequality | status |
| --- | --- | --- |
| P1 | T_P ≤ (m − n + 1)·((n + 1)(2f + 2X + K + 1)·n(n − 1) + X + 1) = O(m·n⁵(1 + X + K)) | LANDED R28 (c) (v) (via R27 Theorem LP) |
| P2 | f ≤ n_E(2n − 1)(X + 1) + X | LANDED R28 (c) (iv) (via R25 Theorem FB, J ≤ X) |
| P3 | K (wakes per phase) ≤ poly(n)·(1 + f) in U1 pieces | LANDED R24 (d) Theorem U1 (given f) |
| P4 | K in U2 / U3 / U23 stretches ≤ poly(n)·(1 + f + K_W + E) | LANDED R26 (b), (d) (given f, K_W, E) |
| P5 | (E) events per W-flat run; (K_W) non-fallback W-changes on R outside route form | **OPEN** (R26 limit (ii)); K = Θ(n) per phase occurs (R30 limit (iv), kchain) |
- So T_P = poly(n)·(1 + X + K), and f is poly(n)·(1 + X) (LANDED). **Everything rests on X and K per phase.**
- READING (L-SI 9): K is missing from the Lead's list of guesses, and it is a separate open link. Through R27 Theorem LP it enters the
  rise count ρ ≤ 2f + 2X + K (R28 (c) (iii)), so a bound on X alone does not bound T_P. Wakes at route-form states lie in U1 pieces
  (R27 (e) WAKE) and are bounded given f. The open part is wakes at states whose honest frame or W frame is not in route form, i.e. ¬H1
  (U2) and HN (U3) states.

## 3. Crossings X per phase, split by phase type
R33 (a) H3-CONST (LANDED): in a phase, H3 holds at all H2 states or at none. So every phase has one of three types:
- TYPE H: its states are (h) = H1 ∧ H2 ∧ H3, HN = H1 ∧ ¬H2, and ¬H1;
- TYPE Q: its states are Q = H1 ∧ H2 ∧ ¬H3, and ¬H1. A Q phase has no HN state (NHN §6 H3-IN-HN, IN REVIEW);
- TYPE N: no H2 state; its states are HN and ¬H1.

Two facts used throughout:
- A crossing changes R. By R33 (e) R-CONST (LANDED), no transition between two ¬H1 states is a crossing. So every crossing with a ¬H1
  end is an H1-toggle, and there are ≤ T of them.
- By R23 (c) LOOP (LANDED), at an H1 state every leave has an active leaver: a switched s ∈ R_k with σ_{k+1}(s) ∈ F_k.

| # | inequality | status |
| --- | --- | --- |
| X1 | crossings with a ¬H1 end ≤ T | LANDED R33 (e) + R34 (e) |
| X2 | HN stretch S: S4a steps never evict and fallbacks never enter (SPLIT), so X_S ≤ (e_S + 1)(n − 1) + e_S, where e_S = evicting fallbacks in S | LANDED R39 (a); the arithmetic is READING (L-SI 9) |
| X3 | Q-run: the same split (Q-SPLIT), so X_Q-run ≤ (e + 1)(n − 1) + e | Q-SPLIT LANE-PROVED (L-NEW 19, docs/new/N5-Q-box40.md §2) |
| X4 | **no in-phase fallback evicts after the phase's (\|U\| − 2)-th fallback g_{\|U\|−2}**, so evicting fallbacks per phase ≤ max(\|U\| − 2, 0) | LANE-PROVED (L-NEW 19, docs/new/N5-FBCAP-route-box40.md §2 (iii); κ-HAT-FREEZE, from P-N5-PFZ FB-ROUND + P-N5-RHO HAT-FREEZE, both SIGNED-IN-LANDING) |
| X5 | N_HN ≤ 1 + ⌈T/2⌉ + 2·max(\|U\| − 2, 0) | NHN-BOUND, IN REVIEW (P-N5-NHN §5; needs RHO §2-§4) |
| X6 | Q-runs per phase ≤ ⌈T/2⌉ + 1 | LANE-PROVED (N5-Q §1; separated by toggles, R34 (e)) |
| X7 | (h)-runs per phase ≤ 1 + T + #(EV2 ends) ≤ 1 + T + 2·max(\|U\| − 2, 0) | READING (L-SI 9): the proof of R34 (g) RESTARTS charges each fallback restart to an HN → H1 ∧ H2 transition, which is exactly an EV2 end (NHN §2); then NHN §5 (a) |
| X8 | crossings between two (h) states ≤ 13(d_o + 1)n³(f + 1 + T) + T + #(evicting fallbacks) | LANDED R34 (f) X-SN-PHASE, plus X4 for the fallback part |
| X9 | HN crossings by breaks: Σ_S X_S ≤ O(n⁶), and HN fallbacks ≤ O(n⁸) | HN-POLY-ALL: CONDITIONAL; P-N5-PFZ + ext (REFEREE-2: (i) gap G-PFX-1, (i′) signed), RHO (both signed), NHN (IN REVIEW) |

READING (L-SI 9) from X1-X6, all LANE-PROVED or better. It makes X9 unnecessary for crossings.
- In a TYPE Q or TYPE N phase:
  X ≤ T + (#runs + #evictions)(n − 1) + #evictions ≤ T + (2 + ⌈T/2⌉ + 3n)(n − 1) + n = O(n³).
  - TYPE Q uses X3 + X4 + X6.
  - TYPE N uses X2 + X4 + N_HN ≤ 1 + ⌈T/2⌉. A TYPE N phase has no H2 state, hence no EV2 end, so its HN stretches are separated by
    drops (R34 (e)) and X5 is not needed.
  - So in TYPE Q and TYPE N phases, **X is polynomial**, given X3 + X4 (TYPE Q) or X4 alone (TYPE N); both are lane proofs.
  - In TYPE H the HN part uses X5 (IN REVIEW) as well.
- In a TYPE H phase: X ≤ T + [HN part, O(n³) as above] + [(h)→HN and HN→(h) boundaries ≤ 2·#(h)-runs, O(n²) by X7] + X_hh.
  - X_hh := crossings with both ends (h).
  - By X8, X_hh ≤ 13(d_o + 1)n³(f + 1 + T) + T + n.
  - **X_hh carries the f-term.**

## 4. The weakest open links (READING, L-SI 9), in order
1. **f per phase in TYPE H phases, i.e. the f ↔ X loop, which now sits only at (h) states.**
   - X8 needs f: a fallback starts a new fallback-free run, and R32 / R33 X-RUN bound crossings per fallback-free run.
   - P2 bounds f by X. Every other crossing term is polynomial (§3), so the loop is
     X_hh ≤ c·n⁴(f + T + 1) and f ≤ c′·n²(1 + X_hh + O(n³)).
   - Where the fallbacks sit: TYPE Q and TYPE N phases need no f-bound for X. In TYPE H, the HN fallbacks are O(n⁸) by X9, and the ¬H1
     fallbacks are poly(n) by R38 (e) NH1-FB (LANDED). **The open term is f_h: fallbacks at (h) states.**
   - The scope-run route for f_h: f_h ≤ #(scope runs)·(4·n·n_E + 3) (SCOPE-FB, P-N5-LV2 §8, SIGNED-IN-LANDING) + #(scope-run ends).
     - #scope runs ≤ #(h)-runs + #WCH (R38 (c)).
     - #(h)-runs is now poly(n) by X7 (READING).
     - **#WCH ≤ (n − 2)(X + 1) + X (R38 (b)) is the only X-term left in f_h.**
   - So the loop is: w-changes at (h) states ⇐ crossings ⇐ fallback-free runs ⇐ fallbacks at (h) states ⇐ scope runs ⇐ w-changes.
   - Two ways to cut it:
     - (a) A bound on w-changes per (h)-run without X. Under (h), w = o ⊕ Ξ(t0) with t0 = τ(o) ∈ F fixed (R19 (b) Wo). So this asks
       for poly(n) changes of ONE vertex's honest value Ξ(t0) across crossings. Ξ(t0) is monotone (R15 (a)) with fixed cycle node
       c_θ (H3-CONST).
     - (b) A bound on fallbacks at (h) states per phase without scope runs, which is FB-CAP restricted to (h) states. The FB-CAP route
       doc §2 already closes evictions (iii), F∩U → F∩U switches (i, except the c_θ-cycle case), and, at (h) states, F → R̄ gates.
       - THR: θ ◁ w and Lemma G (a) give W(σv) = Ξ(σv) ◁ π_z ⊕ θ ⊴ π_z ⊕ w = W(z); with FBL-N (ii) this rules out a gate from F into
         R̄.
       - EQ: FBL-N (ii) leaves no gate from F at all.
       - Left open: R → R̄ route changes at EQ states and at u* = none states (FBL for u* = none is unproved, R20 (b)); the c_θ-cycle
         case; vertices outside U.
2. **K per phase (wakes at ¬H1 and HN states, P5).** No packet addresses it. Data are thin, but K = Θ(n) occurs.
3. **Lemma Φ is unrefereed (L2).** Its proof is three lines from LANDED R15 (a), (d) and injective priorities: Ξ never decreases, the
   reward of the cycle node is its first key, and so each vertex's cycle node changes ≤ n − 1 times. Cheap to sign; see §5.
4. Smaller items, each OPEN or IN REVIEW, none on the critical path once 1-3 close:
   - u* = none fallbacks per scope run: LV-NONE ≤ n·n_E + 1, SIGNED-IN-LANDING; FBL for u* = none OPEN.
   - REL(S) at level −1 (R41 limit (ii)).
   - INTO (CONJECTURE). Wording per L-RED R71: restrict to Iσ_t ≠ ∅, or to fallback states.
   - "THR ⇒ M ≥ 0" (CONJECTURE).
   - NJB's straddling interval (OPEN).
   - These bound fallbacks inside one scope run. They matter only through f_h, and SCOPE-FB already bounds f_h per scope run.

On the Lead's four guesses:
- "Crossings X per phase (the f ↔ X loop)": confirmed. By §3 it narrows to (h) states, item 1.
- "Q states": READING says X in TYPE Q phases is polynomial given Q-SPLIT + X4 (lane); f_Q then follows from P2. No break count is
  needed.
- "Scope runs per phase beyond R38": these are item 1's WCH term. The (h)-run term is closed by X7 (READING).
- "Number of phases": L1-L3. Only Lemma Φ's signature is missing.

## 5. Was box 21's Lemma Φ ever refereed?
- No. Searched: every RESULTS entry that mentions it says "unrefereed".
  - R21 "Consequence" and limit (iii); R23 limit (iii); R25 limit (iv); R27 limit (iii); R28 limit (ii).
- REFEREE R-N5-Z l.16, l.45: "The READING part (Lemma Φ, τ-changes ≤ d − 1) is not signed". REFEREE-2 R2-N5-Z l.22 says the same.
- REFEREE R-N5-1OA l.87 uses #λ ≤ 2n(n−1) "(Lemma Φ, R15 (a))" inside a ✓ for a READING, not a signature.
- No packet contains it.
- The statement in docs/new/N5-time-box21.md §2.3:
  - "Each vertex's cycle node in L_σ changes at most n − 1 times in a run. The same holds for the cycle node in Ξ^d_τ. So a run has at
    most 2n(n − 1) + 1 joint λ-phases."
  - Its proof: R15 (a) monotonicity; the cycle-node reward is the first key; rewards are injective.
- READING (L-SI 9): with R38 KEY the dual half is not needed, because λ_U changes only when τ does. So L1-L3 give
  #phases ≤ n(n − 1) + d.
  - What a referee must check: Ξ_k = L_{σ_k} along N5, including at S4c fallbacks. This is R15 (d) (every Even move is Switch_I with
    I ⊆ Iσ) together with R15 (a).
- Suggestion to the Lead: a one-page micro-packet (Φ′: #phases ≤ n(n − 1) + d), written by L-NEW (its owner) or by me.

## 6. What I attack next (item (2) of the GO)
Item 1 (b): fallbacks at (h) states per phase, without scope runs. The first step is DATA on the pinned library and the L-RED / REFEREE-2
climb instances. At every in-phase fallback from an (h) state, classify the switched vertices:
- R → R̄ (route change);
- the c_θ-cycle case;
- outside U;
- anything else (the READING above says it is empty after g_{|U|−2}).

Item 1 (a) in parallel, on paper: does Ξ(t0) admit a Lemma-P-type potential across crossings inside one (h)-run?
