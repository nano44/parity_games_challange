# Draft RESULTS R47 (Lead, 2026-10-25 20:56Z by date -u; renumbered from R46 at 21:05Z; fixes-file line to be filled when L-SI 10 pushes it) — to CHECKER C56

### R47 [refereed-only] N5: cycle nodes only rise and Odd's dual cycle nodes only fall along a run, so every run has at most 2n(n − 1) + 1 joint λ-runs (Lemma Φ, every game), and on one-Odd-choice games τ changes at most deg(o) − 1 times and a run has at most n(n − 1) + deg(o) phases (Corollary Φ-1O) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C56.md, checker PENDING)
- Object (packet P-N5-PHI, added at l-si af3a3b5a, pinned trunk 02ad3f88, unchanged during review): docs/si/P-N5-PHI-box14.md, sha1
  35e79ec1a91d0213b2b673779b69eb58a3e76b39 (L-SI successor 9, Opus 5.5). Its source is docs/new/N5-time-box21.md §2.3 (L-NEW box 21),
  which RESULTS R21, R23, R25, R27 and R28 call unrefereed; the packet re-proves it from landed results and governs where they differ.
  The referees' notes are collected by the lane in FIXES-PENDING; on trunk; repairs only.
  Setting: N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md; states (σ_k, τ_k); Ξ_k := Ξ_{σ_k} (Even's valuation, R15's Ω_σ), λ_k(v) its
  cycle node; U_k := Odd's valuation of τ_k in the dual game G^d (R38 (a)'s U_k), λ^U_k(v) its cycle node; reward(c) := p′(c) if Ω(c)
  is even, −p′(c) if odd, with p′(v) = 2·rank(v) + (Ω(v) mod 2) and rank injective (SPEC S1), so reward is injective on V. A JOINT
  λ-RUN is a maximal run of consecutive states with (λ_k, λ^U_k) constant. On 𝒞^1O, d := deg(o), and a PHASE is a maximal run with
  (λ_k, τ_k) constant (a joint λ-phase by RESULTS R38 (a) KEY).
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); landed premises only:
  (a) Lemma Φ (every game): (a) reward(λ_{k+1}(v)) ≥ reward(λ_k(v)) for every v and k, with equality iff λ_{k+1}(v) = λ_k(v) (RESULTS
      R15 (a), (d)); (b) reward(λ^U_{k+1}(v)) ≤ reward(λ^U_k(v)), with equality iff λ^U_{k+1}(v) = λ^U_k(v) (RESULTS R18 (d) Lemma S (b));
      (c) along a run at most n(n − 1) transitions change λ and at most n(n − 1) change λ^U, so a run has at most 2n(n − 1) + 1 joint
      λ-runs. R18's gaps S1, S2 do not touch (b): S1 concerns Lemma S (a), and S2 is (b)'s own citation, R15 (a), (d) applied on G^d
      with R18 (d) Lemma R (PHI-N1 = N-PHI-2, citation, both referees); G-1OA-6 concerns Lemma S (c)-(d) and is not used.
  (b) Corollary Φ-1O (𝒞^1O): (a) along any N5 run τ changes at most d − 1 times (the τ's form a strict ≺_{G^d}-chain by R15 (c), (d)
      on G^d, so no τ repeats; N-PHI-1); (b) a run has at most n(n − 1) + d phases.
- Not signed (packet §2 "Use", §3): the READING that with Φ-1O a polynomial bound for N5 on 𝒞^1O needs only a polynomial bound on the
  length of one phase (docs/si/N5-LEDGER-box14.md, docs/si/N5-FBPHASE-box14.md); the packet's data.
- Honest limits: (i) Lemma Φ holds on every game but bounds only λ- and λ^U-changes, not iterations; Corollary Φ-1O is on 𝒞^1O. (ii)
  Nothing here bounds the length of a phase, so G-N5-TIME stays open. (iii) Φ-1O (a)'s bound d − 1 is reached in data (REFEREE-2:
  1000‰, library and random), so it is tight.
- Data (DATA, not proof): REFEREE (own probe phifx_probe.py on rl_engine): 367 library games (any game; 253 𝒞^1O) and 8,000 random
  games (half general n 3-10, half 𝒞^1O n 4-14; 4,995 𝒞^1O): Φ (a) and (b) 278,285 + 57,066 checks each, λ^U checked directly (PHI-N2),
  joint λ-runs at most 15.3% of the bound, max 29 phases, 0 failures. REFEREE-2 (own phi_check.py): 492 𝒞^1O files × 3 traces × 3 starts
  and 64,000 random 𝒞^1O runs, 1,484 logs OK: 3,219,607 checks each of (a) and (b), 0 drops / 0 rises; phases at most 375‰ of
  n(n − 1) + d (max 30); mutation control ub bites (2,385 violations). Lane phicheck.py: 590 traces, 427,644 reward checks, 0 drops
  (λ^U not checked).
- Signatures: REFEREE docs/referee/R-N5-PHI.md (referee 843ba1f8, successor 10; §C 37608e06 + count fix 92628d03): Lemma Φ (a)-(c),
  Corollary Φ-1O (a), (b) SIGNED; notes PHI-N1, PHI-N2; no gaps. REFEREE-2 docs/referee-2/R2-N5-PHI.md (referee-2 b621f9af, successor
  11; §C f8cb3ef3): all SIGN; notes N-PHI-1, N-PHI-2; no gap. §C (both): verdicts identical; joint gap map empty; N-PHI-2 = PHI-N1's
  recommendation and N-PHI-1 accepted by REFEREE; REFEREE's general-game data cover REFEREE-2's thin spot ("every game").
- TARGET.md diff: not a claim of TARGET.md section 1 (Lemma Φ bounds cycle-node changes of N5 on every game, not its running time).
  GAPS G-N5-TIME: open.
