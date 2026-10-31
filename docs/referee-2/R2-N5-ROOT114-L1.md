# R2-N5-ROOT114-L1: word-diff of P-N5-ROOT line L-1 (REFEREE-2 successor 25, Opus 5.5, D15; written 2026-10-31 20:00Z by date -u)
- Object: claude/l-new be131555, docs/new/P-N5-ROOT-line-L1.txt, sha1 a41df25be547e603582ebdf6a06e1070e1f02e95 (re-hashed: match).
  - Base: the draft line 954af7be (l-new ed2fdaf2), 697 → 837 words.
  - The packet is unchanged at be131555 (sha1 f06f493e).
- My items: ROOT114-L1 (REQUIRED, bind k), ROOT114-L2 (REQUIRED, the STAIR line version), P-1 to P-3 (optional), from
  R2-N5-ROOT114.md (d1c493fb).

## Token diff (git diff --word-diff on non-space tokens): every change, nothing else
1. STAIR premise: «as in its line L-1, docs/new/P-N5-STAIR-line-L1.txt)» → «as in its line L-2: l-new 6903f1b3,
   docs/new/P-N5-STAIR-line-L2.txt, sha1 44f56e96d41d45653c4b7bc2f140c587e8e407e6)». Re-hashed: match.
   «β … DESC_F as in P-N5-STAIR's line L-1» → «… line L-2».
2. ODD premise: «(Corollary FUEL-COUNT))» → «(Corollary FUEL-COUNT: l-si 0afc0d70a, docs/si/P-N5-ODD-box57.md §6, sha1 03eec41d, with its
   fixes entries 1-2))». Re-hashed 03eec41d: match.
3. ROOT CHANGE: «a pair (y, k) with {+k → k + 1 a transition of F,+} y switching at k and W(y) changing at k».
4. KEY added: «(2, 0) if the cycle node changes, else (1, r) with r the top rank of the difference of the path sets, else (0, 0), ordered
   (0, 0) < (1, r) < (1, r′) < (2, 0) for r < r′». The key of a fuel re-route at k is the key of Ξ_(k−1)(z) → Ξ_k(z).
   This is P-N5-ODD §6's definition, the same in substance.
5. HC_F: «:= the number of transitions u of F at which Ξ(z) changes with a key strictly greater than the key of the last fuel re-route of
   (y, z) at a transition ≤ u». This is FUEL-COUNT's HC verbatim in substance, and it meets P-3.
6. Binder: «every W-run F = [p, q] of it{+, every vertex v, every Even y, every vertex z and every transition k → k + 1 of F+}:».
7. DESC-ROOT: «previous change {+of W(v)+} at k′».
8. NEW-FUEL: «if [-Even-] y switches …». y is Even by the binder.
9. ROOT-SPLIT: «[-every root change (y, k) with-] {+if (y, k) is a root change and+} k − 1 ∈ F{+, then (y, k)+} is a fuel re-route or a
   relay …».
10. Tail: {+DESC*-LIN DEAD in the weak form (L-RED R163);+} and «L-NEW successor 42{+; fixes docs/new/P-N5-ROOT-fixes-box114.md entries
   1-2+})».

## Checks
- **ROOT114-L1 is closed.**
  - A root change now carries «k → k + 1 a transition of F», and the binder ranges k over transitions of F.
  - The w_re3_1 boundary case is therefore excluded: F = [2, 6], k = 6, and 6 → 7 is the S4c fallback, not a transition of F. So are all
    2,977 corpus boundary cases (BND_*).
  - ORIGIN-NEW and ROOT-SPLIT now say exactly what I signed (k → k + 1 in F, k − 1 ∈ F).
  - On the bound range my root_check.py has ONEW 0 and RSPLIT 0 violations (R2-N5-ROOT114/logs).
- **ROOT114-L2 is closed** (STAIR line L-2, pinned by commit and sha1).
- P-3 is met (item 5). P-1 and P-2 were not taken. They are optional, and nothing is lost: NEW-FUEL is now stated only on transitions of
  F, where the packet's own proof applies.
- Binder pass:
  - v, y, z and k are bound. k′ is bound in DESC-ROOT's clause, and x_j by its definition.
  - The Σ_(y,z) sums rebind (y, z) over Even edges with N_F ≥ 1, a harmless shadowing.
  - The KEY clause's a → b are dummy letters, local to the clause.
  - No free symbol.
- No new overclaim:
  - The added clauses are definitions (KEY, HC), pins, the binder, and one DEAD clause naming its source (R163, as packet §1 states).
  - No asymptotic word, no bound beyond the packet, and no referee-originated proof (L41 tag not needed).
  - Every statement is equal to or narrower than the signed packet statements. The scope tail is unchanged except the DEAD clause and the
    fixes pointer.
- TARGET.md scope words unchanged: «not M3, not a step-4 pass, not a TARGET.md claim», «G-N5-TIME stays OPEN», REDUCTIONS / EQUIVALENCES.

## Verdict
**MATCHES** (Opus 5.5, D15). All my ROOT line items are closed.

## DONE / FINDINGS / NEEDS
- DONE: this file; the token diff; sha1 checks of L-1, the packet, STAIR L-2 and the ODD packet.
- FINDINGS: ROOT L-1 MATCHES. The binder excludes ROOT114-L1's k = q case. No new overclaim.
- NEEDS: none.

## Addendum 1 (2026-10-31 20:28Z by date -u): Lead ruling L43 (relayed 20:29Z)
- My verdict above was written before the ruling reached me. Under L43 a lane DEAD of an asymptotic statement does not enter a RESULTS line
  as «DEAD». The ROOT L-1 tail clauses «DESC-LIN DEAD (L-RED R162)» and «DESC*-LIN DEAD in the weak form (L-RED R163)» are such.
- So I agree with REFEREE's ROOT-L4 / L5 (74025e44): drop both, or restate them as DATA with numbers.
- The clause «every root descent is a fuel re-route» DEAD (frz32) is a universal statement refuted by one instance, not an asymptotic one.
  I read it as allowed under L43 as worded (Lead decides).
- The rest of L-1 MATCHES as stated above. I will word-diff L-2.
