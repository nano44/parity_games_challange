# R2-N5-SETTLE-L1: word-diff of the P-N5-SETTLE line, revision L-1 (REFEREE-2 successor 23, Opus 5.5, D15)
Object: docs/si/P-N5-SETTLE-line-L1.txt @ l-si a0970d36, sha1 997e39eee8d72ae94be4764bb1e3841914ffc78e (re-hashed: match), against the
frozen line 6aa094e3 (l-si 6a70a520). Token diff (difflib over whitespace tokens), mapped to the joint required set of R2-N5-SETTLE-C.md C.2:
| item | L-1 text | check |
| --- | --- | --- |
| F unquantified (SETTLE-L1 = my L-1) | «…): for every N5 run on every game and every W-run F of it: (Claim RG′) …» | ✓ RUN-SETTLE, RUN-COUNT, HEAD-RED now bound |
| T unbound (SETTLE-L2 = my L-3) | «every N5 run, with T its number of transitions (N5 iterations), has T ≤ …» | ✓ |
| k free in RG′ (SETTLE-L3) | «at every S4a step k → k + 1 of F»; «for a state k of F: … H_k …»; «for a transition k → k + 1 of F: (y, z) is W_(k+1)-tight …» | ✓ every k bound |
| Iσ_k (my L-2, Lead: REQUIRED) | «Iσ_k := Even's improving edges at k (SPEC S2: {(y, z) : Ξ_k(z) ▷ Ξ_k(σ_k(y))})» | ✓ |
| precision: ⊕, event-free, Σ / max ranges, «for every family of games» (SETTLE-L4) | ⊕ «as in RESULTS R93 TIE»; «a transition is EVENT-FREE iff it is not an EVENT»; Σ_(Odd o), Σ_(c ∈ C), Σ_(u ∈ V), max_(…) with arguments; «for every family of games every W-run has polynomially many transitions iff … over all W-runs F» | ✓ |
| precision: ℓ_(k+1)(v) (my L-4) | «every Even vertex v switching at k and every vertex v whose Ξ changes at k has ℓ_(k+1)(v) ≥ k − k0 + 1» | ✓ |
| precision: status of ARENA-MAX / T54 (my L-5) | «ARENA-MAX (L-RED R140, l-red 47000632; the S4a half of the R57 premise above) and L-LIT T54's LEX-BFS / IDX-MONO as signed in this packet's review, read at one S4a evaluation with W_(k+1)» | ✓ |
| precision: closing clause (my L-6) | «(2026-10-30) — a REDUCTION (no count is bounded here; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim; …)» | ✓ |
| also | premises «RESULTS R15 (a), (d) and R86 (a)» listed; run / transition / switch / values / order bound up front; FLIP-EV marked «DEAD, fixes F0»; header removed (L41 convention) | ✓ |
Second binder pass, clause by clause: RG′'s (x, y) and the tightness definition's (y, z) are local and separate; RUN-SETTLE's v is bound in
both halves; HEAD-RED's sums and maxima have ranges; T-XCH re-quantifies «every N5 run» (harmless under the global binder). No free symbol.
Content unchanged against the packet's §3, §5-§7.

## Correction to my own SETTLE texts
REFEREE noted, and the fixes file (E1.9-E1.13) records, that my «gate_K64_n581 + start» label for the longest event-free block (67) was a
slip: the 67 is on gate_K64_n581 from the DEFAULT best-reward start (my sbcg run, «gate_K64_n581.pg#0»). R2-N5-SETTLE.md §4 N-3 and
R2-N5-SETTLE-C.md C.4 say «+ start»; read «default start». The reconciliation is unchanged.

## Verdict
L-1 (997e39ee): **MATCHES** (Opus 5.5, D15). No required change.
