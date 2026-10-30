# N5-REPCH (box 44): cause chains of REPEAT late adoptions. Depth 1 on the corpus: the W-rise behind every repeat is caused by plain switches
L-SI successor 31 (Opus 5.5), D15 / D18, Lead reading L40. Lead 2026-10-30 00:23Z step (2): «Try to break that circle with a well-founded
order: for example, a W-rise of c charged to a late adoption at a vertex strictly lower in some rank (priority, attractor depth, or the λ_W
order). Then measure the depth of that recursion on the corpus. Both outcomes count.» Working note, unrefereed, not a TARGET.md claim.
G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Tool: experiments/si/odd/repchain.py (W-runs, BLOCKED and late adoptions as in L-NEW's box64/late.py; same late totals: 1,141 / 41
  repeats on the corpus, = odd/laterep.py). Output odd/out/repchain_corpus.txt (719 games). Pinned in si/check.sh «box 44».

## 1. The circle and the chain measured
- The circle (P-N5-CUT §6-§7): inside a W-run, W-changing transitions ≤ (n − 1)(R*_T + 1) (GP*-RUN), R*_T ≤ m_E + REP, and each REPEAT
  of (y, z) needs a change of W(z) after y's leave of z, or is W-silent (LATE-SPLIT (ii)).
- Chain. For a REPEAT of (y, z) at u, let t* be the last transition in [k + 1, u] at which W(z) changes (k → k + 1 = y's last leave of z).
  Its CAUSES are the Even x on z's new W-play (z included) that switch at t*: by [S1-val] a change of W(z) at a transition with τ fixed needs
  σ to change on z's new or old play; the tool takes the new play. PARENT: a REPEAT among the causes if any, else a FIRST late adoption, else
  a plain switch (not a late adoption). DEPTH: 1 + the parent's depth for a REPEAT parent, else 1.
- DATA (corpus): 41 REPEATs, 0 W-silent; parents: REPEAT 0, FIRST 0, plain switch 41. Maximum depth 1.
- So the circle does not close in the data: no W-rise that enables a repeat is driven, at that transition, by a late adoption. The waves
  that re-enable an edge come from plain (never-blocked, Ξ-improving) switches downstream of the target.
- Candidate rank "W-length to the cycle node": the parent switch x has ℓ_W(x) < ℓ_W(z) at t* + 1 in 31 of 41; it fails in 10
  (switchbestexp_5: 3, so_th_n32: 2, long121_n40, ueonce_n27, runfam_K10, runfam_K40). DEAD as a strictly decreasing rank along the chain.
  (x on z's play can sit on the cycle part, where the length does not decrease.)

## 2. CONJECTURE REP-PLAIN, and why it does not yet give a proof (READING)
- CONJECTURE REP-PLAIN: in every W-run, the last change of W(z) before a REPEAT of (y, z) is not caused by a late adoption (causes as in
  §1, any choice of play). DATA: 41 / 41, depth 1.
- REP-PLAIN alone does not break the counting circle. GP*-RUN bounds all W-changing transitions together, (n − 1)(R*_T + 1). It does not
  separate those driven by plain switches from those driven by late adoptions. A proof would need a GP*-type lemma for the plain part:
  "W-changes driven only by never-blocked edges number ≤ (n − 1) per W-run", or a count of how often a plain wave can re-enable an edge.
- Both outcomes per the Lead: no growing chain depth found (depth 1 on every game). So there is no lead for L-RED from depth. The open
  quantity stays [P-REP] (REP* per W-run).

## 3. Composition toward G-N5-TIME
- §1: DATA only. The REP circle has depth 1 on the corpus; the length rank is DEAD.
- §2: CONJECTURE REP-PLAIN. With a "plain-wave" GP* lemma it would give REP ≤ (number of plain waves) × d_E, a route to [P-REP] and so to
  P-N5-CUT's Corollary CUT-POLY's [P-REP] premise.

## DONE / FINDINGS / NEEDS
- DONE: odd/repchain.py; corpus; si/check.sh «box 44»; this note.
- FINDINGS: 1. DATA: every REPEAT's enabling W-rise has a plain-switch parent; depth 1. 2. DEAD: W-length as a decreasing rank (10 / 41).
  3. CONJECTURE REP-PLAIN.
- NEEDS: none from the owner.
