# Owner-supplied source for Q5: Imperial DTR 2015/4 (OWNER-DESK reading; not a referee or L-LIT verdict)
Received from the owner 2026-10-15 ~07:40Z (upload "DTR15-4.pdf", 18 pages, sha256
a7b61fe3a72926a94a3019e34620339f38aa653fe8aeed9ab4210187763e9cd6). Byte-identical public copy (same sha256, fetched 07:47Z):
https://www.doc.ic.ac.uk/research/technicalreports/2015/DTR15-4.pdf

## What it is
M. Huth, J. H.-P. Kuo, N. Piterman, "Static analysis of parity games: alternating reachability under parity", Technical Report
2015/4, Department of Computing, Imperial College London, ISSN 1469-4174, dated 9 August 2015 (footnote 1, p.1). Same title as
the LNCS 9560 (2016) chapter, and it calls itself a "chapter" (p.3 "Outline of chapter"). Most likely the pre-publication text of
that chapter. It is NOT the Springer version: the published pages 159-177 remain unopened, and edits after August 2015 cannot be
excluded.

## Contents (section, numbered statement, page)
- §3 alternating reachability under parity: Def 1 (p.4), Lemma 1 determinacy (p.5), Def 2 game graph G^p_X (p.5), Thm 1 (p.6),
  Cor 1 O(|E|·|C(G)|) (p.6).
- §4 monotone functions F^p_G: Lemma 2 (greatest fixed points are won by p), Lemma 3 monotone; new partial solver psolC (Fig. 5),
  Thm 2 running time O(|E|·|C(G)|·|V|^2), Thm 3 (finite memory needed in general), Examples 2-3 (Fig. 6: psolC solves no node).
- §5 fatal attractors: MA(X) eq. (3); psolB reproduced as Fig. 7 ("reproduction of Fig. 3 in [13]"); Thm 4 (p.12): psolC decides
  every node psolB decides. Proof uses "Theorem 5 in [13]" (order of fatal-attractor detection does not matter) as a black box.
  Fig. 8 (= Fig. 5 in [13]): psolC solves completely, psolQ solves nothing.
- §6 experiments (psolB vs psolC on random games; Zielonka regression); §7 related work (incl. lift(ρ) of [14]); §8 conclusions.
- [13] = HKP, "Fatal attractors in parity games", FoSSaCS 2013, LNCS pp. 34-49 (the conference version of arXiv 1405.0386).

## What it says about the fleet's open points (desk reading; for the Lead, L-LIT and referees to confirm)
1. Novelty of T-A1 (RESULTS R2): this text gives no characterisation of the games psolB solves completely, and no condition like
   PA**. Its only psolB theorem is Thm 4 (psolC dominates psolB). Searched: whole text (pdftotext), terms "psol", "complete",
   "Solved", "fatal". So on this version no KNOWN verdict for T-A1 arises.
2. G10 (T-A1's dependence on HKP's proofs of Thm 7, Thm 8, Lemma 5 of arXiv 1405.0386v2): this text does not restate or re-prove
   those results; it cites [13] for psolB facts. It cannot close G10. (Lead reading needed: Q5 assumed the chapter bears on G10.)
3. HKP Thm 4 strategy flaw (REFEREE-2 side finding, about psolQ in arXiv 1405.0386): not addressed here; psolQ appears only in §5's
   comparison and Fig. 8. This text's "Theorem 4" is a different statement (psolC vs psolB).
4. New for the fleet: psolC, a stronger polynomial partial solver than psolB (Thm 4). Possibly relevant to L-ATTR follow-up work
   (e.g. whether an exact class like PA** exists for psolC). Not assessed by the desk.
