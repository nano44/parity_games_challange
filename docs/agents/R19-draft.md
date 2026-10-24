# Draft RESULTS R19 (Lead, 2026-10-24 15:15Z by date -u) — awaits CHECKER C28; lands in "## Results" after R18, before "## Dead ends"

### R19 [refereed-only] N5 on one-Odd-choice games: gate/selection structure (Lemma G), monotone w (Wo), monotone routes (RM), re-entry (RE) and two-run decomposition between crossings (PIECE) (2026-10-24) — partial step-4 lemmas for N5 on a subclass (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C28.md, checker PENDING)
- Object (packet P-N5-RE, pinned trunk 52c7261, unchanged during review): docs/new/P-N5-RE-box26.md, sha1
  8dba4576950d4888b90d4c0cc86217b9b8fec745 (L-NEW successor 9, Opus 5.5). The repairs both referees require are written in the
  referees' reports and applied by the lane in docs/new/N5-xing-box27.md §9 (not refereed as text; the signed statements are below).
  N5 as in docs/new/N5-ssi-global.md (SPEC S1-S5; RESULTS R15). Setting: 𝒞^1O (exactly one Odd vertex o of out-degree d > 1),
  o-acyclic or not; θ := Ξ(o) (Odd's honest value at o), w := W(o) (the value N5's selection trusts at o); R := the vertices whose
  current play reaches o; (h) the packet's regularity hypothesis.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma G (a)-(c): on 𝒞^1O the honest gate and N5's selection against τ agree except on edges entering R (withheld) and on
      R→F edges refused in trust mode; R→R edges are honest-improving iff route-improving iff W-improving.
  (b) Lemma Wo: under (h) at consecutive states, τ(o) ∉ R, w = o ⊕ Ξ(τ(o)), and w is non-decreasing.
  (c) Lemma RM: in a stretch with τ and θ constant and (h), routes of vertices staying in R never decrease (route order (c, A_π, |π|)
      without the terminal, RM-1).
  (d) Lemma RE, WITHOUT the packet's hypothesis (NC): if x leaves R at L and next re-enters at E, then route_{E+1}(x) ▷ route_L(x) or
      θ_{E+1} ▷ θ_L. Proof as repaired by both referees: key step (SG) — at any N5 transition a switched Even vertex y with λ(y) ≠ y
      gains strictly (Ξ_{L+1}(z) ⊵ Ξ_L(z) ▷ Ξ_L(σ_L y), then one strict (V2)); the packet's step-2 caveat and step-3 sentence are
      false as written (RE-1 = G-RE-1, RE-2 = G-RE-2) and are replaced. Gap G26-1 is CLOSED; the packet's §6 "flat leave" cannot occur
      (nc_fail_n12.pg, REFEREE-2).
  (e) Corollary RE: re-entries per joint λ-phase ≤ n·#θ-changes + #(route-improving re-entries), with τ constant on each
      leave-to-re-entry interval (N-RE-3; REFEREE reads RE as needing no τ hypothesis, not signed by REFEREE-2).
  (f) Lemma PIECE: in a stretch with τ, w, R constant, (h), no fallback (θ constant not needed, N-RE-4), N5 runs two independent R17
      arena runs, the route game on R with o's frozen continuation as terminal and the o-free game on F; with the contraction 𝓡* (o a
      self-loop with c's priority; REFEREE) or Lemma P re-run with base case at o (REFEREE-2) each piece has ≤ |R| − 1 resp. |F| − 1
      value-changing transitions (P-1 = G-RE-3); the Consequence holds inside one joint λ-phase (P-2).
- Honest limits: (i) SUBCLASS (𝒞^1O) that is polynomial by other means; a bound on N5 itself, not on parity games. (ii) These lemmas
  do NOT bound N5 on o-cyclic 𝒞^1O: the open items are (CYC') θ- and w-changes per joint λ-phase and (NH) non-(h) transitions
  (L-NEW box 27 reduction, READING; its Lemmas C, FBL, FBF, CR, XA are in a second packet, P-N5-XA, under review). (iii) Data caveat:
  the lane's random re-entry samples are vacuous (737 leaves, 0 re-entries; REFEREE); RE's support is the proof plus the referees' own
  checks. (iv) Code link G-N1 (inherited): n5.py agrees with the referees' definitions on all tested runs, DATA.
- Data (DATA, not proof): REFEREE (re_probe.py): 17,473 switches of non-cycle-node vertices, 0 non-strict (494 (NC) cases); 512 leaves
  (RE step 3), 0 violations; PIECE split bounds 480 transitions, 0 violations; negative control 57/446 non-strict off the setting.
  REFEREE-2 (own checker from the definitions): 31,827 runs, 60,225 transitions, 0 violations; 1,321 re-entries (400 with θ unchanged)
  all strict; (SG) 25,283 switches; all 3,356 non-strict leaves at non-(h) states. L-RED 13: RM/RE attacks on rt48/ph64 climbs, 0
  violations.
- Signatures: REFEREE docs/referee/R-N5-RE.md (referee 4457a9a; §C 87beaa6, a3d1f70): G, Wo, RM SIGNED; RE SIGNED WITH GAPS (closed),
  (NC) not needed; Corollary RE SIGNED WITH GAP N-RE-3; PIECE SIGNED WITH GAPS (P-1 closed, P-2 wording). REFEREE-2
  docs/referee-2/R2-N5-RE.md (referee-2 3ee7b73, c66da44; §C dd5aaa2): G, Wo, RM SIGN (RM-1 noted); RE SIGN without (NC); Corollary RE
  SIGN WITH GAPS (N-RE-3); PIECE SIGN WITH GAPS (P-1 closed, P-2 open as wording). Both §C: no disagreement; gap map RE-1 = G-RE-1,
  RE-2 = G-RE-2, P-1 = G-RE-3, P-2 = N-RE-4 (second half); (SG) = REFEREE §4.2.
- TARGET.md diff: not a claim of TARGET.md section 1. Gauntlet: partial step-4 lemmas for N5 on a subclass. GAPS G-N5-TIME: open.
