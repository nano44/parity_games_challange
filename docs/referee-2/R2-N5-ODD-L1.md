# R2-N5-ODD-L1: word-diff of the P-N5-ODD line, revision L-1, and the fixes file (REFEREE-2 successor 24, Opus 5.5, D15)
- Objects:
  - docs/si/P-N5-ODD-line-L1.txt @ l-si ab0baf919, sha1 3e25138b9e7ef228ddba306d35ae3897cb797ea2 (re-hashed: match);
  - docs/si/P-N5-ODD-fixes.md @ ab0baf919, sha1 67fbe3a4ce37aa31bd819ce2b22a30c185443a85 (re-hashed: match; F0 and entries 1-4).
- Base: cd121dff. Written without opening REFEREE's verdict on L-1.

## 1. Word-diff cd121dff → L-1 (difflib over whitespace tokens, 626 → 792 tokens)
Every change maps to an entry-3 item. Nothing else changed.
| change | entry | my item | check |
| --- | --- | --- | --- |
| R57 gloss «… ρ» → «… ρ and every vertex x» | E3.4 | — (REFEREE's) | ✓ |
| «Q1)» → «Q1; «rank» is SPEC Q1's)» | E3.9 | — | ✓ binds the rank in the key |
| Φ source «(RESULTS R97, …)» → «(P-N5-SRC §2, the signed proof of RESULTS R97 PLAY-CAUSE^S)» | E3.6 | — | ✓ |
| «W-run F, …» → «W-run F of a run, …»; «for a W-run F,» before the FS and fuel definitions | E3.3 | ODD-L1 (F) | ✓ |
| fuel re-route + «its rise transition := k − 1 → k» | E3.2 | **ODD-L2** | ✓ met |
| OLD-PLAY «at every transition k → k + 1 and for every vertex x» | E3.5 | **ODD-L1** (x) | ✓ met |
| ODD-STEP «at every transition k → k + 1» | E3.5 | ODD-L1 | ✓ |
| ODD-RELAY «at every transition k → k + 1, for every Odd o with x := σ̄_k(o) and every vertex u on x's (σ_k, σ̄_k)-play, if …» | E3.5 | **ODD-L1** (u) | ✓ met |
| ODD-ADD: «for every Odd o, every set I of transitions and every set U of vertices such that at every k ∈ I at which Ξ(o) changes ODD-RELAY's hypothesis holds for some u_k ∈ U, \|{k ∈ I : Ξ_(k+1)(o) ≠ Ξ_k(o)}\| ≤ \|{k ∈ I : Ξ_(k+1)(u) ≠ Ξ_k(u) for some u ∈ U}\|» | E3.1 | **ODD-L3** | ✓ met, exactly the packet's ODD-ADD |
| «and for every W-run F of the run,» before SRC-ROOT; SRC-ROOT «at every transition k → k + 1 of F» | E3.3, E3.5 | **ODD-L1** (k, F) | ✓ met. F now scopes SRC-ROOT, FUEL-LEX and FUEL-COUNT |
| SRC-ROOT «every o_j's Ξ changing at k», «(possibly o_0)» | E3.8 | — | ✓ both are in the signed statement (o_0 stops at once if (o_0, k) is a prefix event) |
| FUEL-LEX «for every pair (y, z) and consecutive fuel re-routes of (y, z) in F» | E3.3 | ODD-L1 | ✓ |
| tail «the polynomiality of max HXS_F in RESULTS R97's SRC-COUNT» | E3.7 | — | ✓ |
| tail + «the proofs of FUEL-LEX and FUEL-COUNT carry referee-originated repairs (G-ODD-1, …; G-ODD-2 = N-ODD-2; … entries 1-2)» | E3.11 | ODD-L5 | ✓ met (L41) |
| DATA «of every statement checked in packet §7, and of all seven statements in both referees' own checks» | E3.10 | ODD-L4 | ✓ met; see the note |
| source «… with docs/si/P-N5-ODD-fixes.md; L-SI successors 36, 37» | bookkeeping | — | ✓ |
- Note on ODD-L4's wording, my side: my odd_check.py checks OLD-PLAY, ODD-STEP, ODD-RELAY, SRC-ROOT, FUEL-LEX and FUEL-COUNT directly.
  ODD-ADD is checked through ODD-RELAY: ODD-ADD is the per-transition matching of ODD-RELAY, so a RELAY failure is the only way it can
  fail. «All seven» is acceptable on that reading.
- Strict symbol test of the changed text: x, u, o, k, F, I, U, u_k, o_j, o_t, (y, z) and «rank» are each bound in their clause or by the
  new preamble. No new free symbol. The scope words are unchanged. ✓

## 2. Fixes file
- E1 (G-ODD-1): the adopted repair is my wording (R2-N5-ODD §3). The replacement proof is correct:
  - u := the first change in (t, t′] with key ≥ (1, r). It exists, because t′ has key (1, r).
  - Before u, every change has key < (1, r), so the cycle node and the bits at ranks ≥ r are fixed, with bit r = β.
  - If EQHI fails, u's key is (1, r). Then u moves r away from β: a fall, against [R15a].
  - **Acceptable: I SIGN E1's repair** (Opus 5.5, D15). Its labelling as referee-originated and written independently by both is correct
    under L41.
- E2 (G-ODD-2): «ASC, else EQHI, else REP; only PURE REP (0, 0) boundaries are chained» is my repair. ✓ SIGNED.
- E3: the mapping covers every REQUIRED item of mine (ODD-L1, ODD-L2, ODD-L3) and my precisions ODD-L4 and ODD-L5. ✓
- E4 (F-1 = D-ODD-1), re-run with my own code on experiments/si/src54/inst/sbq2_K8_m16_fix.start @ ab0baf919 (sha1 83a57866; the only
  token change is «242:243» → «242:244»):
  - the start is valid; the run has 153 states;
  - W(242) = W(259) at 0 states (the original: 153), and σ̄(260) flips 128 times. That equals E4's «Wtie 0, sbflips 128».
  - odd_check.py on it: 0 violations. Fuel re-routes 496 (over all y) equal E4's anc «FUELEV 496».
  - So the withdrawal of the box-54 W-rank DEAD («OPEN, not dead») is right. ✓

## Verdict
L-1 (3e25138b) with fixes 67fbe3a4: **MATCHES** (Opus 5.5, D15). No required change. ODD-L1, ODD-L2 and ODD-L3 are met, and ODD-L4 and
ODD-L5 are applied. E1 and E2 are SIGNED, and E4 is confirmed.
