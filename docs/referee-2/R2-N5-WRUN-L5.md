# R2-N5-WRUN-L5: word-diff of the P-N5-WRUN line, revision L-5 (REFEREE-2 successor 24, Opus 5.5, D15)
Object: docs/new/P-N5-WRUN-box92-line-L5.txt @ l-new 57dff7b2, sha1 e0b4f4a74ac0a0470100af947026aedaa02588e1 (re-hashed: match).
It is compared with L-4 (5462315f, sha1 98d9a50c, re-hashed). The fixes file docs/new/P-N5-WRUN-fixes-box92.md @ 57dff7b2 has sha1 94f6133f…
(re-hashed), and its entry 6 quotes C105 §5 (E-1).

## 1. Diff (difflib over whitespace tokens, plus a byte test)
- L-4 has 1,352 tokens and L-5 has 1,356. Each file is one line. The byte counts are 7,596 and 7,610.
- The token diff has exactly two inserts: «a state» before «s» and «of Φ» after it.
- Byte test: L-4 with «y leaves z at s and (y, z) is blocked again at q2 > s in Φ» replaced by «y leaves z at a state s of Φ and (y, z) is
  blocked again at q2 > s in Φ» equals L-5 byte for byte (True).
- The old clause occurs once in L-4 and 0 times in L-5. The new clause occurs once in L-5.
- No heading marker was added (L41).
- Nothing else changed.

## 2. Does the replacement match the proof (packet §10, l-new 7668bc9b l. 316-324)?
The proof reads «In a frozen stretch Φ … y leaves z at s > t1 … blocked again at q2 > s». With t1 ∈ Φ this gives s ∈ Φ. L-5 now states
s ∈ Φ.
Φ is a run of consecutive states. With s, q2 ∈ Φ and q2 > s, s + 1 ∈ Φ too, so s → s + 1 is a step of Φ: τ_s is Φ's τ, it is an S4a step,
and there is no S4c. Hence:
- ARENA-MAX at s holds, used in step (i): σ_{s+1} is optimal in H_s against τ.
- R91 W-SUCC on [s + 1, q2] holds, used in step (ii): the interval lies inside one piece.
- The parenthetical «a special case of RESULTS R91 Lemma LATE-W» is now true: R91 (f) needs the leave s → s + 1 inside the piece.
Dropping «s > t1» is the reading both referees signed: the proof never uses the release (R2-N5-WRUN.md l. 131; REFEREE l. 226-227). It is
still the reading signed in L-4.

## 3. Strict symbol test (changed clause)
| symbol | binder |
| --- | --- |
| Φ | «a frozen stretch Φ», earlier in the same REL2-WRISE clause |
| s | «a state s of Φ» (new) |
| q2 | «q2 > s in Φ» |
| y, z | «(y, z) is adopted …» |
No symbol is free.

## 4. Correction (my side)
Successor 23's L-4 report (9784fde6) said MATCHES without noticing that s had no range. REFEREE missed it too. CHECKER C105 caught it as
E-1. The class is the one in my notebook: «a variable defined but not quantified».

## Verdict
L-5 (e0b4f4a7): **MATCHES** (Opus 5.5, D15). No required change. C105 E-1 is closed on my side.
The GAPS UPDATE (C105 l. 548) takes the same replacement. That text is the Lead's draft, and I did not word-diff it.
