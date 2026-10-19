# T22: VJ00 Proposition 7.4 (O(n³) steps on one-player parity games): reading, proof search, verdict (L-LIT, 2026-10-19)

Asked by the Lead (23:58Z, 2026-10-18). L-NEW's K9 reduction (docs/new/N5-oneplayer-box7.md, claude/l-new) rests on this proposition. Fleet-internal only.

**Sources.** All opened in this session; sha256 prefixes are in notes/L-LIT.md.
- **BRICS RS-00-48**, sha256 485a12de…. Printed page numbers are given; the PDF page is printed + 2.
- **VJ00 CAV 2000** author copy (Warwick), sha256 64d1143b…; pages read as rendered images.
- **Friedmann PhD thesis** (LMU 2011), sha256 68748f53…; PDF pages given.

## (1) What Prop. 7.4 says: which player, which steps
Verbatim, BRICS §7, printed p.27 (PDF p.29): "Proposition 7.4 The discrete strategy improvement algorithm terminates after O(n3) strategy improvement steps for one-player parity games." There is no proof; the next paragraph moves on to Prop. 7.5.

The context, printed p.26–27: "Examples of Melekopoglou and Condon [14] are Markov decision processes, i.e., one-player simple stochastic games [3]. It is an open question whether the strategy improvement algorithm using the standard policy, i.e., switching all switchable vertices in every strategy improvement step, works in polynomial time for one-player simple stochastic games [14]. In contrast, our discrete strategy improvement algorithm terminates in polynomial time for one-player parity games."

**Which player: the improving player ⊕ (the one whose strategies are improved), with ⊖ having no choice. L-LIT reading, from four pieces of text:**
- (a) The contrast is with MDPs, where the single player is the optimizer whose policy is improved.
- (b) If ⊖ were the only player with choices, ⊕ would have exactly one strategy. The algorithm (§3, printed p.8: "while σ ≠ Improve(σ) do σ := Improve(σ)") would then make zero steps, and the proposition would be vacuous.
- (c) VJ00 uses "(one-player) game" for the game with one side fixed: printed p.26, "in the (one-player) game Gσ′ we have fσ = Θσ′σ", where Gσ′ fixes ⊕'s strategy. So the phrase names "only one side has choices" and does not by itself fix the side. (b) fixes it.
- (d) Friedmann's restatement (below) puts the choices with player 0, the improver, under SWITCH-ALL.

**Which steps: NOT settled by the text. The safe reading is the standard switch-all policy.**
- For the any-policy reading: "The discrete strategy improvement algorithm" is §3's loop with the non-deterministic Improve of §4.4 ("SwitchI(σ) for some set I ≠ ∅ of improvements"). Prop. 7.5 ("terminates after ∏ out-deg(v) many strategy improvement steps") holds for every policy.
- Against it:
  - Where VJ00 means every policy, it says so: Prop. 7.6, "for which all policies have length O((n/d)^d)". Prop. 7.4 does not.
  - The sentence that introduces 7.4 contrasts it with "the standard policy, i.e., switching all switchable vertices".
  - Problem 7.7 (printed p.28) leaves open whether the switch-all policy is polynomial in GENERAL games.
- CAV 2000 has the same statement as Proposition 8 (p.12), after the same contrast sentence and with no proof. The CAV paper's "algorithm" is Fig. 1 (p.9), which switches every switchable vertex to a ≺-maximal successor. p.12 adds that "switching an arbitrary non-empty subset … gives a correct strategy improvement algorithm", but says nothing about its step count.
- Friedmann's thesis restates it ONLY for SWITCH-ALL (below).
- **Consequence for K9.** K9 applies the bound to N5's Even moves, which are arbitrary subsets of improvements chosen by N5, "whatever τ does". That is the any-policy reading, and **no source states it**. The any-subset version also has to count the flat steps found in T21 (REFEREE-2's I1 instance is itself a one-player ⊕ game). This adds a burden; it is not a contradiction.

## (2) Search for a proof
| place | finding |
| --- | --- |
| BRICS RS-00-48 §7 (printed p.25–28) | stated, no proof. Prop. 7.1 (≤ n steps for SOME policy) is proved; 7.4 is not |
| VJ00 CAV 2000 (LNCS 1855), Prop. 8, p.12 | stated, no proof (extended abstract, no proofs at all) |
| Friedmann PhD thesis, §4.1, PDF p.100 | "We conclude this paragraph with the question whether we can solve single-player parity games in a polynomial number of iterations. To answer that question, we define the most natural multi-switch rule, called SWITCH-ALL …" then "Theorem 4.9 ([Vög00]). Let G be an one-player parity game. Policy iteration with the SWITCH-ALL rule requires polynomially many iterations in the worst case." No proof; [Vög00] = "J. Vöge. Strategiesynthese für Paritätsspiele auf endlichen Graphen. PhD thesis, University of Aachen, 2000." So **Friedmann attributes a proof to Vöge's thesis, for SWITCH-ALL only, with no explicit bound** |
| Vöge PhD thesis (RWTH Aachen 2000, German) | **NOT OPENED.** The publications page old.automata.rwth-aachen.de/publications/pub-Voege.html.en lists a PDF, but it gives 403 to curl and 503 to WebFetch; guessed download paths give 403; the Wayback Machine is blocked by egress policy; publications.rwth-aachen.de timed out. This is the most likely place for the proof |
| Friedmann LMCS 1106.0778 | no one-player statement (grep) |
| Fearnley 1705.02313, Lemma 3 (p.9) | related, NOT equivalent. All-switches one-player SI for a best response in SINK games (shortest-path valuations, admissible σ) takes O(\|V\|\|E\|) iterations, citing Cochet-Terrasson-Gaubert [3] (not opened). VJ valuations coincide with these only on sink games (2309.02223 p.15: "in sink parity games, the valuations from the literature are equivalent"); a general one-player parity game is not a sink game |
| Luttenberger 0806.2923 v4 | non-deterministic SI bound O(1.724^\|V0\|) (p.1), exponential; no one-player statement |
| Björklund-Vorobyov DAM 2007; Schewe CSL 2008; Luttenberger's PhD thesis | NOT opened in this task |
| DLM 2309.02223, STV 1501.06484, Fearnley-Savani 1507.04500, Canavoi-Grädel-Rabinovich 1210.2459 | grep "one-player"/"single player": no statement or proof |
| web search ("one-player parity games" strategy improvement Vöge Jurdziński polynomial) | no proof found; only the sources above |

## (3) Verdict
**STATED ONLY. Not contradicted; no published proof was opened.**
- It is stated three times without proof: BRICS Prop. 7.4, CAV Prop. 8, and Friedmann thesis Thm 4.9.
- Friedmann attributes a proof to Vöge's PhD thesis, for **SWITCH-ALL only**. That thesis could not be reached from this container.
- For K9:
  - (i) The player is ⊕, the improver, in the source's evident sense.
  - (ii) The any-subset version that K9 uses is stated nowhere. The sources support at most switch-all (Friedmann explicitly; VJ00 by context).
  - (iii) Any proof must count T21's flat steps.

## DONE / FINDINGS / NEEDS
- FINDINGS:
  - Prop. 7.4 is stated without proof in BRICS (printed p.27) and CAV (Prop. 8, p.12). Friedmann's thesis Thm 4.9 restates it for SWITCH-ALL, attributing it to Vöge's PhD thesis, which is unreachable here.
  - The "one player" is the improver ⊕; otherwise the statement is vacuous.
  - "Steps" is unsettled by the text, and the safe reading is switch-all. K9's any-subset use is stronger than every source.
  - The nearest proved relative is Cochet-Terrasson-Gaubert O(\|V\|\|E\|) for all-switches on shortest paths (via Fearnley 1705.02313 Lemma 3). It holds only for sink games.
  - Verdict: STATED ONLY.
- NEEDS:
  - owner: a copy of Vöge's thesis (RWTH Aachen 2000; the automata.rwth-aachen.de publications page lists a PDF), only if the fleet wants the proof. The host blocks this container (403).
  - Lead: K9 needs either a proof for arbitrary subsets or a restriction to switch-all segments.
