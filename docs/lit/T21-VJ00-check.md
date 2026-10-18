# T21: Vöge-Jurdziński (VJ00): do the two fleet findings hold against the CAV 2000 text, and are they known? (L-LIT, 2026-10-18)

Asked by the Lead at 23:09Z. Two fleet findings, both made against BRICS RS-00-48:
- **(1) L-NEW**, docs/new/G-N5-TERM-reading.md §0: VJ00 Lemma 5.8 "2 ⇒ 1" (Improve(σ) ≠ σ ⇒ σ not maximum) and postulate I2 fail at cycle nodes. The 4-vertex instance is given there.
- **(2) REFEREE-2**, docs/referee-2/R2-N5T.md §4 (branch claude/referee-2): postulate I1 fails as well. Instance: prio [0,2,4], all vertices Even's, succ 0→{1}, 1→{0,1}, 2→{0,1}, σ = (0→1, 1→0, 2→0). Switching the single edge (1,1) is an improvement but leaves Ω unchanged, although (2,1) shows σ is not maximum.

Fleet-internal only (D1/D11): nothing here leaves the fleet. N5's correctness does not use the failing direction (R2-N5T §3).

## Sources opened (sha256 prefixes in notes/L-LIT.md)
- **CAV 2000 version.**
  - Vöge, Jurdziński, "A Discrete Strategy Improvement Algorithm for Solving Parity Games (Extended Abstract)", CAV 2000, LNCS 1855, pp. 202–215 (Crossref 10.1007/10722167_18).
  - Author copy: dcs.warwick.ac.uk/~mju/Papers/VJ00-CAV.pdf, 14 pp., sha256 64d1143b9e5f95fb…. Its text layer is unreadable (Type-3 fonts), so pages 1, 4–10, 12–13 were rendered and read as images.
  - The Springer PDF URL returns HTML (paywall). No journal version or erratum was found: author page, Crossref and web search.
- **BRICS RS-00-48** (Jurdziński, Vöge, Dec 2000), www.brics.dk/RS/00/48/BRICS-RS-00-48.pdf, sha256 485a12de432a2a8c… (the same file L-NEW and REFEREE-2 opened). Read: §3 (P1, P2, I1, I2, Theorem 3.1), §4.2–4.4.
- A wrong guess, discarded: BRICS DS-00-6 is Henriksen's thesis, not Jurdziński's.

## (a) What the CAV text says. It differs in form, and the failure carries over to other sentences
The CAV extended abstract has **no postulates P1/P2/I1/I2, no Lemma 5.8 and no non-deterministic Improve operator**, and it contains no proofs. The relevant CAV statements, quoted from the rendered pages:
- **Order on play profiles (§3.1, p.6).** "(u, P, e) ≺ (v, Q, f) ⟺ u ≺ v ∨ (u = v ∧ P ≺ Q) ∨ (u = v ∧ P = Q ∧ v ∈ V− ∧ e < f) ∨ (u = v ∧ P = Q ∧ v ∈ V+ ∧ e > f)". This is the same order as BRICS §4.2: lengths count, shorter is better for V+ and longer is better for V−.
- **Optimal valuation (§3.3, p.7).** "a weaker requirement is made if x is the most relevant vertex associated to x via φ (i.e., φ0(x) = x). In this case we discard the distance component φ2; formally, we replace ⪯ by ⪯x." So at cycle nodes, CAV's optimality ignores lengths.
- **Algorithm (Fig. 1, p.9), lines 7–9.** "for each v ∈ V0 … if φ(σ(v)) ≺ max≺{…φ(v′)} then select σ(v) … with φ(σ(v)) = max≺{…}". The switch test uses the full order ≺, lengths included. The main loop stops when σ = σ′.
- **p.5:** "The key lemma says that φ′ will majorize φ … This will be the basis for the termination proof because equality φ = φ′ will imply that φ is already optimal for both players."
- **Lemma 5 (p.8):** "Then for all v ∈ V, we have φ(v) ⪯ φ′(v)". This is weak monotonicity only.
- **p.12:** "Note that switching an arbitrary non-empty subset of the set of switchable vertices in every strategy improvement step gives a correct strategy improvement algorithm for parity games."
- **p.13:** "Note that in every strategy improvement step the current valuation strictly improves in at least one vertex." Also on p.13: Prop. 9, "terminates after ∏_{v∈V0} out-deg(v) many strategy improvement steps", stated without proof.

**Check of the instances against these sentences** (by hand from the CAV definitions; the vertex numbers are ranks).

*L-NEW's instance, finding (1).* Dual game: priorities [3,7,1,2], and only vertex 1 belongs to the improver.
- With τ(1) = 1: φ(1) = (1, ∅, 0) and φ(3) = (1, ∅, 1). Vertex 1 has odd priority, so it is in V−, where longer is better. So vertex 1 is switchable by Fig. 1 line 8, and it is the only switchable vertex.
- After the switch, φ is unchanged at every vertex.
- So **Fig. 1's own step (switch-all) makes a step in which the valuation does not strictly improve anywhere.** This contradicts p.13.
- p.5's "equality ⇒ optimal" is NOT contradicted: by §3.3's ⪯x rule this φ is already optimal.

*REFEREE-2's instance, finding (2).*
- Vertex 1 (priority 2, V+): φ(0) = (1, ∅, 1) ≺ φ(1) = (1, ∅, 0), so vertex 1 is switchable. Vertex 2 is switchable as well.
- Switching only vertex 1 is allowed by p.12 ("an arbitrary non-empty subset"). It leaves φ unchanged although σ is not optimal.
- This contradicts p.13 for the arbitrary-subset algorithm of p.12. Under Fig. 1's switch-all, vertex 2 also switches and the step is strict, so (2) needs the arbitrary-subset reading, exactly as I1 does in BRICS.

**What remains true (L-LIT reading).**
- p.12's "correct" holds for the output: a stop with no switchable vertex is optimal.
- Termination and Prop. 9's bound hold if no strategy repeats. That is what L-NEW's Theorem (Ω, φ) supplies. It is unrefereed in this task, but REFEREE-2 marked it CORRECT in R2-N5T §3.
- CAV's coarser notion of "optimal" (lengths dropped at cycle nodes) is consistent with the failure: the flat steps happen exactly at cycle nodes, on lengths.

## (b) Is the failure known? Places checked
| place (opened) | what it says | notes the exception? |
| --- | --- | --- |
| Friedmann, LMCS 7(3:19), arXiv 1106.0778 v2, §3 p.5–6 | same order with lengths ("assuming we have an even-priority dominating cycle node, it is better to reach the cycle fast"). p.6: "Jurdziński and Vöge proved in their work that every strategy that is improved by an improvement policy can only result in strategies with valuations strictly better than the valuation of the original strategy." Thm 3.2 ([VJ00]): Ξσ ◁ Ξ_IG(σ), where ◁ is defined with "Ξ ≠ Ξ′" | **no**; restates strictness. His improvement policies (condition (2): some v with σ(v) ≺σ I_G(σ)(v)) admit the L-NEW instance's single switch |
| Friedmann PhD thesis (LMU 2011), Ch. 4 (PDF p.105: "some authors define strategy iteration this way right from the start [VJ00]"; Lemma 4.26) | VJ00 as the canonical switch-all source | **no** remark found (grep "strict", "VJ00") |
| Fearnley-Savani, LMCS 14(4:9), arXiv 1507.04500 v4, §2 p.6–8 | same order (p.7). Lemma 2.3 ([43] = VJ00): for any set W of switchable edges, "• For every vertex v we have Val^σ(v) ⪯ Val^σ[W](v). • There exists a vertex v for which Val^σ(v) ≺ Val^σ[W](v)." p.2: "switching any subset of these edges produces a strictly better strategy"; p.8: "each iteration of this algorithm produces a strictly better strategy" | **no**; the second bullet of Lemma 2.3 is contradicted by both instances (L-LIT reading) |
| Luttenberger, arXiv 0806.2923 v4, §5 p.10 | an "optimized" VJ valuation (cycle value, path profile, path length; Even-won vertices get z = ∞) | **no** remark on flat length steps found (grep "length", "strict") |
| Canavoi-Grädel-Rabinovich, arXiv 1210.2459 v1 | lower bounds on VJ's algorithm and graph measures | **no** (grep) |
| van Dijk-Loho-Maat 2309.02223 (p.6: "By [22], for any choice of improving edges, we have Ξσ′(v) ⊵ Ξσ(v) for every v ∈ V, and Ξσ′(v) ▷ Ξσ(v) for at least one node v") | restates strictness for VJ valuations | **no**; same claim. Their families are sink games (see below) |
| Schewe-Trivedi-Varghese 1501.06484 (§2) | a generic SI template | no remark |
| Oink README @ 8fbf0a7 (l.116–118), src/solvers/psi.cpp header | PSI/SSI implementations; "considering only finite paths simplifying the valuation" | no remark |
| web search ("Vöge Jurdziński … erratum … length component … strict improvement") | VJ00 pages, FS, Luttenberger, CGR | no erratum found |
| NOT opened / NOT checked | Vöge's PhD thesis (RWTH Aachen 2000, German); Luttenberger's PhD thesis; Schewe CSL 2008; PGSolver documentation and source (not checked in this box) | — |

**Why the lower-bound literature would not meet it (L-LIT reading).**
- Friedmann, DLM and Fearnley-Savani build their families as **sink** parity games: the only cycle is the sink's self-loop, so its out-degree is 1.
- A flat step needs an improver-owned cycle node with an alternative edge back into its own cycle. That cannot occur when the only cycle node is the sink.
- In general games it occurs (both instances). The strictness claims above are stated for general games.

## (c) Verdicts
| finding | verdict | basis |
| --- | --- | --- |
| (1) L-NEW: a maximum element can still have an improvement (BRICS Lemma 5.8 "2 ⇒ 1", I2) | **NEW as far as checked (NOT FOUND in the places above); the CAV text carries the failure in a different sentence** | CAV has no Lemma 5.8/I2. Its p.13 sentence "in every strategy improvement step the current valuation strictly improves in at least one vertex" fails on L-NEW's instance under Fig. 1's own switch-all step. CAV's §3.3 "optimal" (lengths dropped at cycle nodes) makes p.5's "equality ⇒ optimal" consistent, so CAV's optimality notion already matches the repair. Restated without exception in Friedmann 1106.0778 p.6 / Thm 3.2, Fearnley-Savani Lemma 2.3, DLM p.6 |
| (2) REFEREE-2: a non-maximum σ has an improvement whose switch is flat (BRICS I1) | **NEW as far as checked; the CAV text carries it (p.12 with p.13)** | p.12 allows "an arbitrary non-empty subset" of switchable vertices; p.13 claims strict improvement at every step; REFEREE-2's instance (switch only vertex 1) is a flat step. It directly contradicts Fearnley-Savani Lemma 2.3's second bullet |
| either finding | **not "NOT A FAILURE"** | the CAV order on profiles is the same as BRICS (lengths count at cycle nodes), and the switch test (Fig. 1 l.8) uses that order |

Unaffected (both versions):
- a stop with no improvement is optimal: BRICS Lemma 5.8 "1 ⇒ 2"; CAV Theorem 4 with §3.3;
- weak monotonicity: BRICS Lemma 5.7; CAV Lemma 5.

Termination and the counting bounds (BRICS P1; CAV Prop. 9) need a no-repetition argument, which L-NEW's (Ω, φ) Theorem supplies (REFEREE-2: CORRECT).

## DONE / FINDINGS / NEEDS
- FINDINGS:
  - CAV 2000 opened (Warwick author copy, rendered). It has no I1/I2/Lemma 5.8, but p.13 claims strict improvement at every step. That fails on L-NEW's instance even for Fig. 1's switch-all, and on REFEREE-2's instance for the arbitrary-subset algorithm of p.12.
  - Both findings are NOT FOUND in the literature checked: Friedmann LMCS and thesis, Fearnley-Savani, Luttenberger, Canavoi-Grädel-Rabinovich, DLM, STV, Oink, web. Friedmann 1106.0778 Thm 3.2, Fearnley-Savani Lemma 2.3 and DLM p.6 restate the strictness claim without the exception.
  - Plausible reason it went unnoticed: the lower-bound papers use sink games, where no flat step can occur.
  - CAV's own "optimal" notion (§3.3, lengths dropped at cycle nodes) is consistent with the repair.
- NEEDS:
  - Lead: PGSolver docs and Vöge's thesis were not checked; say if wanted.
  - owner: nothing (fleet-internal, D1/D11).
