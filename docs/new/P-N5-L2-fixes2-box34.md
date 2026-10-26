# P-N5-L2 fixes file 2 (box 34): REFEREE-2's items
L-NEW successor 15 (Opus 5.5, D15/D18). Written 2026-10-25 09:1xZ by date -u, at the Lead's request (09:16Z).
- Object: packet docs/new/P-N5-L2-box34.md (pinned trunk 04b3f48, sha1 cbea07392521bcdfbce137ba361bb581f9df11d7). It is never edited.
- The first fixes file, docs/new/P-N5-L2-fixes-box34.md (sha1 7a110bca8d52b532d531c0836547b2d22b7437cd), is cited by the Lead and FROZEN,
  and is not edited either. This file adds to it.
- Report answered: REFEREE-2 docs/referee-2/R2-N5-L2.md (referee-2 388caf6). All seven statements are signed, with notes N-L2-1..3.

## 1. Map of REFEREE-2's notes
| note | kind | where it is answered |
| --- | --- | --- |
| N-L2-1 (§2 H2-STICK: τ(o) = o, "τ(o) ∈ R_s" false) | wording | = REFEREE L2-1. The repair line is in fixes 7a110bca §1 (L2-1). No new text. |
| N-L2-2 (§7 X-RUN′ (a): X-RUN is applied to H1 runs P_i, not literally to "the SN prefix of a run") | wording | NEW text, §2 below: X-RUN restated once as a lemma on consecutive (h) states of one fallback-free run. |
| N-L2-3 (§4 FREEZE′: its new content is never exercised in data) | DATA thin | Accepted. The lane said the same (packet §4, DATA: none). The claim rests on its proof. No text. |

## 2. N-L2-2: Lemma X-RUN° (the form X-RUN's proof actually gives)
**Lemma X-RUN°.** Let Q be a fallback-free run of a phase, and let I be a set of CONSECUTIVE states of Q at all of which (h) holds. Then the
transitions with both ends in I include at most 13(d_o + 1)n³ crossing transitions.
- Proof: P-N5-FRZ §6 (X-RUN), read with I in place of the SN prefix P. Every step uses only that I consists of consecutive (h) states of
  one fallback-free run of the phase (REFEREE-2 R2-N5-L2 §7 lists them):
  - the windows and the first-freeze points F(ℓ) inside I;
  - RATCHET (c) restricted to I;
  - BLOCK's intervals inside I;
  - the after-F(⊥) argument at transitions with both ends in I.
  Fixes 168de464 FRZ-3's accounting of the transition leaving I is not part of this count: it is added where the lemma is used. □
- X-RUN (P-N5-FRZ §6) is X-RUN° with I = P (the SN prefix, (h) throughout under H1), together with FRZ-3's extra transition.
**Replacement lines for the packet §7 (X-RUN′), proof (a), lines 145-147.** Replace "An H1 run P_i consists of consecutive (h) states of a
fallback-free run: … So it gives ≤ 13 (d_o + 1) n³ crossing transitions with both ends in P_i." with:
- "An H1 run P_i consists of consecutive (h) states of Q: H1 ∧ H3 ⇒ (h) by R30 (d), and every state of P has H3. By Lemma X-RUN°
  (P-N5-L2-fixes2 §2) it has ≤ 13 (d_o + 1) n³ crossing transitions with both ends in P_i."
- The rest of the proof is unchanged: ¬H1 runs have no crossing (R-CONST), and the ≤ t_Q transitions between runs are counted separately.

## 3. REFEREE-2's §8 data finding (record only; §8 was not to sign)
- A second witness of the fallback (h)-restart via τ(o) leaving R: experiments/red/xing/instances/j5_n16.pg (sha1 9ae9df5e…), under
  REFEREE-2's N5 with randomized S4a optima (fallback 6 → 7, τ(o) = 12, |R| 8 → 3). The SPEC witness is fbrestart_cex_n12
  (docs/new/N5-DROP-box35.md §5). Both agree that this open item is FALSE as an impossibility. The count is unaffected (packet P-N5-TOG §6).
