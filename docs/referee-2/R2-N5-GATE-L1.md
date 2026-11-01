# R2-N5-GATE-L1: word-diff of P-N5-GATE line L-1 (REFEREE-2 successor 25, Opus 5.5, D15; written 2026-11-01 01:56Z by date -u)
- Object: claude/l-new afb8b99e, docs/new/P-N5-GATE-line-L1.txt, sha1 d677161c4123dd184db14c17d26630e037b51027 (re-hashed: match).
  - Base: the draft line 245ce9fe (l-new 516717da). 577 → 610 words. The packet is unchanged at afb8b99e (sha1 ac88915d).
  - Written without opening REFEREE's GATE files.

## Token diff: every change, nothing else
1. R18 (d): «used on every game{+: its proof uses no 𝒞^1O hypothesis: VJ00 (11), Lemma R, R15 (a), (d)+})».
2. «SET grows (B rises)» → «SET_k grows (B_k rises)» in the SG / BG definition.
3. CONSISTENT-RED: «{+with τ := τ_(k0),+} if τ_j = τ for k0 ≤ j ≤ k1 and every transition j → j + 1 with k0 ≤ j < k1 is consistent».
   Previously k was the local index.
4. DEAD instances pinned:
   - «experiments/new/box116/inst/fbg_K12_m6_m24.pg (sha1 2f035ca0…) with its repaired start fbg_K12_m6_m24_fixed.start (9f03f81f…, L-NEW
     box 116b)»;
   - «experiments/n5-epoch/instances/lend107_n32.pg (ab4c9811…) with lend107_n32.start (9df4ea2c…), n = 32, 106 > 31».
5. «docs/new/P-N5-GATE-box120.md{+ with its fixes entry 1, docs/new/P-N5-GATE-fixes-box120.md+}» and «successors 43-44».

## Checks
- **GATE-L1 is closed.** «106 > 31» is the count under the line's own λ_W-phase definition (unchanged: «consecutive transitions at whose
  states the map … is constant»).
  - My R2-N5-GATE/logs/lend107_phases.txt has in-phase transitions 2-107, all W-changing.
  - fbg's «403 > 289» stays right (my pins.txt: 403, λ_W constant on the stretch).
- The four pinned sha1 prefixes match my own hashes in R2-N5-GATE.md §4.
- P-1 and P-2 are met by item 1:
  - R15 (d) is now cited.
  - The no-𝒞^1O statement is accurate: box 21 §2.2 (a) is VJ00 (11) on G and on G^d through Lemma R, and (b) is R15 (a) with (d).
  - It uses landed labels, which is better than my lane-file pointer.
  - Its formal acceptability as a citation of a subclass R-line item stays the Lead's reading, as before.
- P-3 is met by item 3. τ is now defined, j is local, and k0, k1 stay bound by the binder («all states k0 < k1»). No free symbol.
- No new claim and no asymptotic word. The scope tail and the L41 premise clause are unchanged. The TARGET.md scope words are unchanged.

## Verdict
**MATCHES** (Opus 5.5, D15). All my GATE line items are closed.

## DONE / FINDINGS / NEEDS
- DONE: this file, the token diff, and the hashes.
- FINDINGS: GATE L-1 MATCHES; GATE-L1, P-1, P-2 and P-3 are met.
- NEEDS: none.
