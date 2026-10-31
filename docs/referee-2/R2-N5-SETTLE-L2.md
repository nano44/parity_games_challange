# R2-N5-SETTLE-L2: SETTLE-L5 and word-diff of the P-N5-SETTLE line, revision L-2 (REFEREE-2 successor 24, Opus 5.5, D15)
Object: docs/si/P-N5-SETTLE-line-L2.txt @ l-si 86becaa0, sha1 1fcb33c5d96a20eb70abe06c29154ef343b33ae0 (re-hashed: match).
It is compared with L-1 (a0970d36, sha1 997e39ee, re-hashed). The fixes file docs/si/P-N5-SETTLE-fixes.md @ 86becaa0 has sha1 42d9a381…
(re-hashed), and its entry 2 quotes REFEREE 20's SETTLE-L5 verbatim (claude/referee aa5adfd4, R-N5-SETTLE-C.md §4 l. 69-77).

## (a) Is SETTLE-L5 required? YES, I agree.
- In L-1, «U := Odd's valuation of τ on G^d (RESULTS R86)» sits after «with τ and C := … fixed on F». There τ is the W-run's fixed τ.
- T-XCH counts «XE (XO) the most changes of one vertex's Ξ (U) over the whole run».
- Read literally, U is one fixed function, so XO = 0. The bound would then read T ≤ m_E(1 + XE) + m_O. That is wider than what was
  signed: the Odd half of R86 (a) SW-RETURN, R = the whole run, counts changes of Odd's valuation at each state, under τ_k. My SETTLE report
  §2.6 l. 87 signed T-XCH in that per-state reading («R86 (a) on both sides, R = the whole run»).
- The letter U also collides with U_k (R143's upward heads), defined in the same line.
- This is a REQUIRED line item of the C99 / R92-F16 / C105-E-1 class: the literal line is wider than the signed statement.
- Correction (my side): successor 23's L-1 report (b521c191) said MATCHES and missed this. It noted only «T-XCH re-quantifies "every N5
  run"».

## (b) Word-diff L-1 → L-2 (difflib over whitespace tokens: 793 → 805 tokens; one line each)
| change | entry | check |
| --- | --- | --- |
| «U := Odd's valuation of τ on G^d (RESULTS R86)» → «Ξ^d_k := Odd's valuation of τ_k on G^d at state k (RESULTS R86's U)» | E2.1 (REQUIRED) | ✓ verbatim REFEREE's fix; τ_k is the run's state-k τ (the line's «a run is the sequence of states (σ_k, τ_k)»); this is R86's U at every state |
| T-XCH «Ξ (U)» → «Ξ_k (Ξ^d_k)» | E2.1 | ✓ Ξ_k is defined «for a state k» (Ξ_{σ_k}); both now range over the whole run |
| «and T is polynomial iff XE and XO are» → «and, for every family of games, T is polynomial over all runs iff XE and XO are» | E2.2 (optional, applied) | ✓ same form as HEAD-RED's «for every family of games …»; the content is what was signed |
| «entry 1)» → «entries 1-2)» | E2.3 | ✓ bookkeeping |
Nothing else changed.
The letter U now occurs only in «RESULTS R86's U» and in U_k / U_(k+1). I counted every token containing U, as entry 2 says.

## Strict symbol test (changed text)
| symbol | binder |
| --- | --- |
| k in Ξ^d_k, τ_k | «at state k», a definition parameter over the run's states, like «for a state k: Ξ_k := …» |
| G^d | RESULTS R86, cited in the parenthesis («Odd's valuation U of τ on G^d») |
| XE, XO, T | as in L-1 (T is bound by «with T its number of transitions») |
No symbol is free. I found no other point in the line.

## Verdict
(a) SETTLE-L5 is REQUIRED: I agree.
L-2 (1fcb33c5): **MATCHES** (Opus 5.5, D15). No required change.
