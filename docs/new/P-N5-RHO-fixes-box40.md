# Fixes to packet P-N5-RHO (docs/new/P-N5-RHO-box40.md, sha1 cd5df65c2f3e6829f85739a57023fc3da6944baa, pinned trunk c8144551): repairs only
L-NEW successor 20 (Opus 5.5, D15/D18), session_018pjn8Y8JRES3YuFDUCAJgM. Written 2026-10-25 19:14Z by date -u, after the Lead's relay of both RHO §Cs
(REFEREE §C 06d6e6d; REFEREE-2 §C in docs/referee-2/R2-N5-RHO.md, referee-2 e6bccdf, commit ab7843a; both on trunk 0ea336ed). A record of the referees' notes and the lane's repairs; not itself refereed text. The packet is
frozen and unchanged. No statement of the packet changes; every item below is wording, citation or data.
- Reports: REFEREE docs/referee/R-N5-RHO.md (59278313 + §C 06d6e6d): all SIGNED, HN-POLY conditional as labelled; notes RHO-N1..N3.
  REFEREE-2 docs/referee-2/R2-N5-RHO.md (269ae45a + §C e6bccdf): all SIGN; notes N-RHO-1, N-RHO-2.

| item | where | kind | repair |
| --- | --- | --- | --- |
| RHO-N1 (REFEREE) | §2 HAT-FREEZE, §3 RHO-TAIL ("If |U| = 1, o = c_θ") | wording | Replace by: "If o = c_θ (any |U| ≥ 1), every z ∈ U ∖ {o} has an honest play reaching o, so F_t ∩ U = ∅ ((HP)); (b), (c) and RHO-TAIL hold vacuously, and θ = (o, ∅, 0) is constant." (o = c_θ with |U| ≥ 2: 89 of 990 library phases, REFEREE's data.) |
| RHO-N2 (REFEREE) = NHN-N1 | §6 HN-POLY, τ(o) = o line, citing NE-COUNT (c) (RESULTS R39 (f)) | citation | R39 (f) is signed for τ(o) = o in case A only. Cite instead: "τ(o) = o ⇒ ¬H2 at every state (o's W-play is the loop o → o), so HN = H1 and the HN stretches are the H1 runs; N_HN ≤ ⌊T_ph/2⌋ + 1 by TOGGLE-COUNT (RESULTS R34 (e))", valid in cases A and B. The bound is unchanged. (REFEREE-2's report did not flag it; REFEREE-2's §C accepts it and re-derives the case-B argument.) The same citation (NHN-N1) is to be carried into P-N5-NHN's fixes file when that packet's reports are in; it is already corrected in docs/new/N5-XOUT-box41.md §2. |
| RHO-N3 (REFEREE) | §8 | data | The parts not reached by any data (FREEZE-F (b); HAT-FREEZE (c) and RHO-TAIL past the freeze at |U| ≥ 4) rest on their proofs. Recorded; no repair. |
| N-RHO-1 (REFEREE-2) | §6 RHO-HN | wording | The proof gives the sharper ρ_HN ≤ (N_HN + |U| − 3)(|U| + deg(o) − 3) + deg(o); the stated (N_HN + |U| − 2)(…) + deg(o) is weaker and stands. |
| N-RHO-2 (REFEREE-2) | §8 | data | FREEZE-F (b) and the post-freeze regime at |U| ≥ 4 are reached by no data (lane, REFEREE, REFEREE-2). Target for L-RED (routed by the Lead with P-N5-FBPOLY's FREEZE-EXIT / THETA-AFTER, 18:37Z). |
- §C lines. REFEREE §C 06d6e6d and REFEREE-2 §C e6bccdf: verdicts identical (all SIGNED / SIGN; HN-POLY through BRK-POLY′ (i′) and (ii)'s
  first inequality; §7, §8 not signed); joint gap map EMPTY; N-RHO-1 = REFEREE's §6 sharper count; REFEREE-2 accepts RHO-N1 and RHO-N2;
  RHO-N3 = N-RHO-2 (same thin spots on both engines: post-freeze only at |U| ≤ 3, FREEZE-F (b) vacuous, RHO-TAIL 0 changes past the
  freeze). REFEREE-2's PFZ §C (C.2) also signs BRK-POLY′ (i) as stated with REFEREE's repair; HN-POLY does not need it.
