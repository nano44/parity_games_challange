# N5 stand-down note (Lead, 2026-10-24 08:20Z by date -u)
Lead reading under L37 (autonomy), per the reassessment logged in docs/agents/LEAD-STATE.md at trunk 04a6f0e: L-RED box 29 was the last
adversary box; it ended without a super-linear in-phase family, so the N5 line stands down. Nothing here is a claim; READING and DATA
labels are the lanes'.

## State of N5 (SSI-GLOBAL, docs/new/N5-ssi-global.md)
- Correctness and termination: RESULTS R15 [refereed-only] (output correctness rests on VJ00 Lemma 5.8 "1 ⇒ 2", G-N5T-3).
- Running time, proved pieces: R17 [refereed-only] (one-player games, < (n²−n+1)(n+m)); R18 [refereed-only] (one Odd choice vertex o,
  o on no cycle, < (C_X + d)(B + 1) from any start, conditional on (P) for one-player games; Prop X).
- Running time, OPEN (GAPS G-N5-TIME): o-cyclic 𝒞^1O; games with ≥ 2 Odd choice vertices; the general case.
- Not killed: no family with super-polynomial (or even super-linear) growth inside one joint λ-phase has been found.

## Data envelope (all Oink zlk OK, strategies verified; Lead re-ran each named instance)
| class | best instance | n | longest joint λ-phase (Lead phases.py; lane count may differ by 1) |
| --- | --- | --- | --- |
| 𝒞^1O o-cyclic | returns_ph64 (experiments/red/n5inj/instances, sha1 562f3e36…) | 64 | 104 (≈ 1.6n) |
| 𝒞^1O o-cyclic | returns_rt48 (7e7ee1b3…) | 48 | 79 |
| 𝒞^1O o-cyclic | fts_best16 (experiments/new/box21/instances, 5534245f…) | 16 | 27 |
| K = 2 Odd choices | returns_rt64 (04c2f308…) | 64 | 89 |
| K = 8, frozen τ* | fts_g43 (53689242…) | 43 | 121 (≈ 2.8n) |
Local growth exponent of the 𝒞^1O envelope from n 48 to 64: 0.97 (L-RED R58 §12). Linear on every climb.

## Why the proof side stopped (docs/new/N5-1O-box22.md, N5-1Ocyc-box25.md)
- Four inductive invariants for the stretch bound (I1-I4) are false; every failure is the trust-mode deadlock: a vertex z in R routed
  through o because the selection values o at w while its honest value π_z ⊕ θ is below an o-free route.
- Fallbacks can lower W on o-cyclic games (box 22 (WF) false; smallest wdrop_cyc n 4); W is not a potential inside a τ-stretch.
- Prop Z (DATA-exact): o-cyclic 𝒞^1O reduces to G[X ∪ Reach(o)]; the part above Z is not one-player (zfrozen_thr).
- Sharpest open statement: (TRUST) — transitions with a trust event per joint λ-phase are poly(n); with box 21's (SEG-1O) this would
  bound N5 on 𝒞^1O (READING).

## Why the attack side stopped (docs/red/R58-n5-width.md §8-§12)
- Theorem W / W2 (PROVED given (P), unrefereed): bounded gate width ⇒ polynomial; long runs must be wide — and climbed runs are wide.
- Composition of the known return mechanisms fails (§12d, READING with data):
  (i) a hub re-root is a one-player move (Lemma G (c)); smallest: rootsearch template L 8, k 4 (n 27);
  (ii) re-entry R → F → R inside a phase came from route improvement in 20/20 cases, never from θ overtaking w; route improvement inside
      R is a one-player resource;
  (iii) per-vertex returns climb (12 at one vertex, returns_rt48) but the in-phase count stays ≈ 1.6n.

## The most promising lead if the line is reopened (Lead reading)
§12d (ii) suggests a proof shape for (TRUST): inside a τ-fixed phase, every return to R is paid by an improvement of a one-player
quantity (routes inside R, bounded by R17's machinery), and θ-driven returns did not occur. A proof attempt should start by trying
to prove "every re-entry into R inside a joint λ-phase is a route improvement in G[R] against τ", then count those by R17.
A kill attempt should look for a θ-driven re-entry (none seen in 20 cases); that is the one mechanism no climb has produced.

## What stands down
- L-NEW successor 9 (session_01EnPXboLL7nw4CKpAwqSDkm) and L-RED successor 13 (session_01GhyuHegkNZEo8bet84n56c): parked; both keep
  their notebooks' resume points.
- No new N5 boxes until a new idea (from a lane, the literature, or the owner) addresses the lead above.
