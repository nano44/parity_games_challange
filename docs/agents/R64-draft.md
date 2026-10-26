# Draft RESULTS R64 (Lead, 2026-10-26 07:19Z by date -u; both §Cs and the fixes file filled) — to CHECKER C73

### R64 [refereed-only] N5 on EVERY game: inside an epoch (σ̄|Q constant within a phase) N5 runs, state by state, as the variant N5^τ on the restricted game G′_E in which only the epoch's disagreement vertices keep a choice (RESTRICT_E, REPRO); an epoch with no disagreement has at most n + m in-phase transitions (EP-0); per phase, in-phase transitions are the sum over epochs of at most one N5^τ phase plus one (EP-k); and, under premise (Στ), an epoch with one disagreement vertex has at most T*(G′_E) + 1 = O(m·Δ·n¹¹) (EP-1, an implication) (2026-10-26) — partial step-4 lemmas for N5 beyond one Odd choice vertex (a reduction: the number of epochs is not bounded here; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C73.md, checker PENDING)
- Object (packet P-N5-EPR, added at l-new 08abd9cb, pinned trunk a3b1cff3, unchanged during review): docs/new/P-N5-EPR-box45.md, sha1
  8fecca797478d1a77564ac1c5b82d11e952559e0 (L-NEW successor 24, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-EPR-fixes-box45.md (l-new 5d14c991, sha1 5af1fde6f0c1a926bb556ecbe47cc2c0f3d562d3, L-NEW successor 24: EPR-1 = G-EPR-1,
  EPR-N1, N-EPR-1, the (Στ) list, data); on trunk; repairs only.
  Setting (every game): N5 = SPEC S1-S5 (with FIX 1-4, Q1-Q4); n := |V|, m := |E|, Δ := the maximum out-degree; state k = (σ_k, τ_k);
  σ̄_k := S1's Odd counterstrategy to σ_k; Ξ_k := V_{σ_k,σ̄_k}; W_k := V_{σ_k,τ_k}; λ := Ξ's cycle-node map; phases as in RESULTS R38 (a);
  Q := the Odd vertices of out-degree ≥ 2. An EPOCH is a maximal run E = (x, …, y) of a phase on which σ̄|Q is constant; σ̄_E, D_E := {u ∈ Q
  : σ̄_E(u) ≠ τ(u)}; len(E) := the in-phase transitions whose source lies in E. G′_E: G with every Odd v ∉ D_E cut to τ(v) and every u ∈ D_E
  cut to {τ(u), σ̄_E(u)}; so G′_E ∈ 𝒞^{|D_E|}O with every Odd choice vertex of out-degree 2. N5^τ: SPEC N5 with S4b replaced by S4b^τ (if
  Iτ ≠ ∅ and τ is value-optimal against σ in S4b's arena, keep τ; otherwise SPEC's S4b).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC; RESULTS R18 (d) Lemma S (a)
  (= (VJ), signed on every game in RESULTS R57 (a)); R17 (c), (e); R38 (a); and, for EP-1 only, R48 (i), R50 (h), R51 (a), (b) read through
  premise (Στ). RESTRICT_E (i) rests on the standing SPEC premise that S1's counterstrategy is optimal (1E-N3, RESULTS R57; N-EPR-1, a
  landing note):
  (a) Lemma RESTRICT_E: for an epoch E and k ∈ E, at the pair (σ_k, τ): (i) Ξ′_k = Ξ_k and W′_k = W_k; (ii) Iσ′_k = Iσ_k, SPEC S4a's output on
      G′_E equals its output on G, and S4c's Even switch-all on Iσ is the same on both; (iii) Odd's dual valuation of τ is the same on both,
      so Iτ′_k = Iτ_k ∩ E(G′_E); (iv) if k → k+1 is an in-phase transition of N5 on G and Iτ′_k ≠ ∅, then τ is value-optimal against σ_k in
      S4b's arena of G′_E.
  (b) Corollary REPRO, read with the joint repair EPR-1 = G-EPR-1 (found independently by both referees): N5^τ on G′_E from the start pair
      (σ_x, τ) passes through the pairs (σ_x, τ), …, (σ_{y′}, τ), y′ := x + len(E), with the same fallback / non-fallback type at each of its
      len(E) transitions as N5 on G; the states x, …, y lie in ONE phase of that N5^τ run, and the last transition y → y′ has its source there
      and may leave it. The packet's clause that y′ also lies in that phase is FALSE in general: RESTRICT_E (i) needs σ̄_k = σ̄_E, and y + 1
      ∉ E (witnesses below).
  (c) Corollary EP-0: if D_E = ∅, then len(E) ≤ n + m. The statement stands; its proof covers the exit or fallback-last case (EPR-N1).
  (d) Corollary EP-k (a REDUCTION), with the repair: for every phase P of N5 on any game, the in-phase transitions of P number Σ_E len(E)
      over its epochs, and for each epoch len(E) ≤ 1 + the in-phase transitions of one phase of an N5^τ run on G′_E ∈ 𝒞^{|D_E|}O started at
      (σ_x, τ).
  (e) Corollary EP-1, an IMPLICATION, with the repair: premise (Στ) — RESULTS R48 (i) (f ≤ 1 + (n − 2)(2n − 1) ≤ 2n², as used by R51 (a)) and
      R50 (h), with the per-phase statements they cite and their own landed chains, hold for every phase of every N5^τ run on every 𝒞^1O
      game from every start pair — implies that every epoch E with D_E = {u} has len(E) ≤ T*(G′_E) + 1, with T* R51 (a)'s per-phase bound at
      G′_E's parameters (n, m′ ≤ m, Δ′ ≤ Δ, d_o = 2); so len(E) = O(m·Δ·n¹¹). (Στ) is NOT claimed here. The packet's (Στ) list names R49
      under R48; R48 does not cite R49, so that entry is spurious and only strengthens the premise (fixes §2, lane remark). REFEREE-2 checked
      the list item by item against R51 (a)'s per-phase citations (R36 (c), R47 (b) rightly absent); REFEREE accepts that as the stronger
      form of its catch-all reading.
  (f) Consequence: every count inside one epoch (its S4a steps, fallbacks, crossings, in particular RESULTS R63's residual X_SN^pre(E)) is
      ≤ len(E); so X_SN^pre(E) ≤ n + m if D_E = ∅, and, under (Στ), O(m·Δ·n¹¹) if |D_E| = 1.
- Not signed (packet §4-§6): the (Στ) audit as written in the packet (a text search; READING), Lemma TIE-W (offered, not needed), the data,
  and the combination with ALT (READING). L-NEW's later line-by-line audit of (Στ) (docs/new/N5-EPR-box45.md §9, l-new bcca6c83, a198c9b9;
  Lemma Στ-STEP lane-PROVED plus a per-entry table) is a premise check for a separate packet (P-N5-STAU), not part of this entry.
- Honest limits: (i) A REDUCTION: the number of epochs per phase (N_ep, tied to ρ and its residuals by RESULTS R61 (f)) is not bounded, and
  epochs with |D_E| ≥ 2 are not bounded here. (ii) EP-1 is conditional on (Στ). (Στ) IS exercised: on L-NEW's DIV instance
  experiments/new/box45/instances/div_n8.pg (n 8, sha1 4ed57ef2c1c92ee526ccd2683ae7c28b1caf5bfa, with div_n8.start) SPEC's S4b on G′_E moves
  τ inside an epoch while N5^τ keeps it, reproduced on both referees' engines; so the packet's §5 line "(Στ) is never exercised" holds
  only for its listed samples. Both referees' own samples give DIV = 0. L-COMP's independent N5^τ engine (l-comp 16c960b5; not a referee
  check) finds N5^τ ≠ SPEC on 497 of 26,573 runs and 0 violations of R48 (i), R50 (h) and R51 (a)'s f-form on 66,709 N5^τ phases (DATA).
  (iii) The exit mismatch of EPR-1 is common: 491 of 3,791 epoch exits (REFEREE) and 1,063 of 8,436 (REFEREE-2).
- Data (DATA, not proof): REFEREE (successor 12, own engine and own N5^τ): 52,631 epochs, 64,331 RESTRICT_E checks, 0 failures; REPRO
  reproduced; witness fb17_n32 from S3 (epoch (26), D_E = {11}: λ′ at 27 ≠ λ); div_n8 DIV = 1, 0 failures. REFEREE-2 (successor 14, own
  epr_check.py; lane code not run): 38,834 sample runs, 4 climbs and 72,000 tie-seeded runs, DIV = 0 there; witnesses
  docs/referee-2/R2-N5-EPR/instances/lamend_D0.pg (n 5, sha1 7f78faf7, D = ∅) and lamend_D1.pg (n 7, sha1 80063b9f), re-run by REFEREE;
  div_n8 reproduced (Addendum A); its step function equals the Runner at every step; the d1 mutation bites; longest epochs 92 / 56 on both
  engines.
- Signatures: REFEREE docs/referee/R-N5-EPR.md (referee 3def3e11, Addendum A e18b4370, §C a0858144, successor 12): RESTRICT_E, REPRO (state
  sequence, fallback types), EP-0, the consequence SIGNED; REPRO's one-phase clause SIGNED WITH GAP EPR-1; EP-k / EP-1 with the +1. REFEREE-2
  docs/referee-2/R2-N5-EPR.md (referee-2 796b4d36, Addendum A 9a5692ad, §C 61022fe3, successor 14): RESTRICT_E, REPRO's pairs and types,
  EP-0, EP-k's sum, the consequence SIGN; the one-phase clause "not signed as stated" (G-EPR-1); EP-1 signed as an implication with the +1.
  §C (both): verdicts identical in substance; one joint gap EPR-1 = G-EPR-1, same repair; EPR-N1 = REFEREE-2's EP-0 bullet; N-EPR-1 =
  REFEREE's standing-premise line; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a reduction; EP-1 conditional; no running-time bound). GAPS G-N5-TIME: open.
