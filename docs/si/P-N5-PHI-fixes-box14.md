# P-N5-PHI fixes (box 14 packet; repairs only)
L-SI successor 10 (Opus 5.5; D15, D18, L37, L40). Written 2026-10-25 20:56Z (date -u), at the Lead's request of 20:49Z (Lead's stamp).
- Object: docs/si/P-N5-PHI-box14.md, sha1 35e79ec1a91d0213b2b673779b69eb58a3e76b39 (L-SI successor 9, l-si af3a3b5a; pinned trunk
  02ad3f88). FROZEN, not edited.
- Repairs only. This file adds no new statement and no new proof.
- Sources, all on trunk 2954e090. File sha1s by `git show <commit>:<path> | sha1sum`:
  - REFEREE successor 10, docs/referee/R-N5-PHI.md:
    - report at referee 843ba1f8 (file sha1 1df761ea…);
    - §C at 37608e06 (d90c476c…);
    - §C count fix at 92628d03 (162f7908…).
  - REFEREE-2 successor 11, docs/referee-2/R2-N5-PHI.md:
    - report at referee-2 b621f9af (file sha1 a62f4aef…);
    - §C at f8cb3ef3 (8da8baef…).
- Verdicts (both reports): Lemma Φ (a)-(c) and Corollary Φ-1O (a), (b) SIGNED, with no gaps. §2 "Use" and §3 are not signed (not to sign).
  The joint gap map is EMPTY (REFEREE §C).
- Items: PHI-N1, PHI-N2 (REFEREE); N-PHI-1, N-PHI-2 (REFEREE-2). PHI-N1 and N-PHI-2 are the same item; both §Cs accept it.

## 1. PHI-N1 = N-PHI-2 (citation of §1 (b); answers the packet's §1 Remark)
- The packet asked whether R18 (d) Lemma S's gaps S1, S2 touch the monotonicity of U. Both referees answer (independently, both quoting
  docs/referee/R-N5-1OA.md l. 48):
  - S1 does not touch it. It concerns Lemma S (a), the sandwich identities.
  - S2 is exactly the citation of (b)'s monotonicity. It is a citation item, not open mathematics.
  - G-1OA-6 concerns Lemma S (c)-(d) and is not used.
- Repair. In §1 (b)'s proof, read the citation as: "R15 (a), (d) on G^d with R18 (d) Lemma R (= R18 (d) Lemma S (b), whose citation gap
  S2 names this route)". In words:
  - N5's τ-changes are Switch_I with ∅ ≠ I ⊆ Iτ on G^d (R15 (d));
  - VJ00 Lemma A (R15 (a)) on G^d gives U_{τ_k} ⊴^d U_{τ_{k+1}} pointwise;
  - Lemma R makes ⊴^d the exact reverse of ⊴;
  - if τ is unchanged, U_τ is unchanged.
- The Remark's conditional "If they do, …" is dropped (N-PHI-2). Its content, the G^d route, IS the cited proof.

## 2. N-PHI-1 (precision; §2 Corollary Φ-1O (a))
- Φ-1O (a) uses only "no τ repeats": the successive τ's form a chain in the strict partial order ≺_{G^d} (R15 (c) on G^d). It uses no
  height bound. The packet states it so; no text change. Recorded as a precision.

## 3. PHI-N2 (data)
- The packet's §3 says "Not checked: λ^U, which the tracer does not expose". That line is superseded by both referees' data, which check
  §1 (b) directly:
  - REFEREE (docs/referee/scratch/phifx_probe.py, logs scratch/phifx_logs/): 278,285 (library) + 57,066 (random) λ^U checks, 0 failures.
  - REFEREE-2: 3,219,607 checks, 0 rises. Its mutation control bites (2,385), so the check can fail.
- REFEREE-2 also reports that Φ-1O (a)'s bound d − 1 is reached in data, so it is tight. This is a note, not a change.

## 4. Nothing else
- No statement, label or proof step of P-N5-PHI changes beyond §1's citation line and the dropped conditional.
