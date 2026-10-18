# Draft RESULTS R15 (Lead, 2026-10-18 23:27Z by date -u) — DRAFT, not landed; awaits CHECKER C17 re-diff (rev. 23:36Z: REFEREE-2 §C fd5abd8; rev. 23:53Z: CHECKER C17 E-1..E-3, N-2..N-4)

### R15 [refereed-only] Termination of N5 (SSI-GLOBAL), and of every VJ00 strategy-improvement step sequence, by the potential (Ω, φ) (2026-10-18) — correctness half of gauntlet step 4 for N5 (not M3, not a step-4 pass; no running-time bound)
- Object: N5 "SSI-GLOBAL" as specified in docs/new/N5-ssi-global.md, sections "Exact pseudocode" and "SPEC (EXACT ...)" S1-S5
  (L-NEW, (c) lane under D14/L35); reading docs/new/G-N5-TERM-reading.md pinned at trunk 812ecba (L-NEW successor 2). Source:
  Vöge-Jurdziński, "A Discrete Strategy Improvement Algorithm for Solving Parity Games", BRICS RS-00-48 (Dec 2000), pdf sha256
  485a12de… (opened independently by L-NEW and by both referees). Notation as there: Ωσ = (Λσ, Πσ), ⊴ on play values (§4.2),
  R+ / R− the priorities of ⊕ / ⊖, k_σ(u) the length component of Πσ(u).
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}. This is VJ00 Lemma
      5.7 as stated (VJ00's Improve already allows any non-empty I); both referees checked VJ00's unproved Prop. 5.4 clause 2.
  (b) Lemma B: if moreover Ω_{Switch_I(σ)} = Ωσ, then every (v, w) ∈ I is a length-only switch at a cycle node: Λσ(v) = v,
      Λσ(w) = Λσ(σ(v)) = v, Πσ(w) ∩ V>v = Πσ(σ(v)) ∩ V>v = ∅, and k(w) > k(σ(v)) if v ∈ R−, k(w) < k(σ(v)) if v ∈ R+.
      (The cancellation uses "=_ℓ on pairs includes equal lengths": REFEREE G-B1 = REFEREE-2's reading of =_ℓ; closed.)
  (c) Theorem: with φ(σ) = Σ_{v ∈ M⊕, Λσ(v) = v} ε(v)·k_σ(σ(v)) (ε = +1 on R−, −1 on R+) and σ ≺ σ⁺ iff Ωσ ◁ Ωσ⁺ or
      (Ωσ = Ωσ⁺ and φ(σ) < φ(σ⁺)), ≺ is a strict partial order on strategies and every non-empty switch of improvements goes
      strictly up in ≺. Consequence: no strategy repeats in any VJ00 strategy-improvement run with any non-empty selection
      rule; φ is an integer with |φ| ≤ n(n−1).
  (d) N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d), and
      changes at least one of them (S4a/S4b, or the S4c fallback, a switch-all); Iσ depends on σ alone (Ωσ is against ⊖'s
      optimal reply, not against τ). Hence no (σ, τ) state repeats and N5 terminates within h(≺_G) + h(≺_{G^d}) iterations; at most 4n(n−1)
      consecutive N5 iterations leave both Ωσ and Ωτ unchanged (two potentials φ, φ^d).
- Honest limits: (i) termination only. h(≺) can be exponential; NO polynomial or other useful iteration bound follows, and the
  running-time half of G-N5-TERM and gauntlet step 4 for N5 stay open. (ii) G-N1 = G-N5T-1 (DATA, code link): (d) applies to
  experiments/new/n5.py to the extent that si.py computes VJ00's Ωσ and improvements; REFEREE: 0 mismatches in 22,969 vertex
  valuations (G and G^d); REFEREE-2: 0 mismatches on Even's side (3,000 random games, 23,943 strategies); improving() on Odd's
  side: REFEREE-2 §C (fd5abd8, si_vs_bf.py dual mode, G^d built as n5.py's dual()): 3,000 games, 21,205 strategies, 0
  valuation and 0 improvement-set mismatches; so si.py agrees with a VJ00 brute force on both sides (still DATA, not proof). (iii) G-N5T-3 (outside the packet): N5's output correctness at S5 rests on VJ00 Lemma 5.8 "1 ⇒ 2", which uses VJ00's
  unproved Lemma 5.9 and Prop. 5.10; not re-derived by either referee (every N5 output in the fleet's runs is verified
  independently: regions against Oink zlk, or Oink tl where zlk hit its cap (labelled per row), or harness Zielonka on random
  games; strategies by experiments/harness/verify.py).
- Side finding (signed as CONFIRMED by both referees; literature check L-LIT T21): VJ00 BRICS RS-00-48 Lemma 5.8's direction
  "Improve(σ) ≠ σ ⇒ σ not maximum" and postulates I1 and I2 FAIL at cycle nodes (instances: G-N5-TERM-reading.md §0; one-player
  prio [0,2,4], succ 0→{1}, 1→{0,1}, 2→{0,1}, σ = (0→1, 1→0, 2→0): switching (1,1) leaves Ω unchanged though σ is not
  maximal). The CAV 2000 version's p.13 sentence "in every strategy improvement step the current valuation strictly improves
  in at least one vertex" fails on L-NEW's instance (even for its own switch-all step) and, under p.12's arbitrary-subset switching, on REFEREE-2's
  (L-LIT T21, docs/lit/T21-VJ00-check.md, l-lit 9281eb5; CAV text quoted from T21, not opened by CHECKER). Not found in the
  literature checked; the strict-improvement claim is restated without exception in Friedmann arXiv 1106.0778 Thm 3.2,
  Fearnley-Savani arXiv 1507.04500 Lemma 2.3, van Dijk-Loho-Maat arXiv 2309.02223 p.6. Unaffected: "no improvement ⇒
  optimal" and weak monotonicity. (c) restores termination of VJ00-based strategy improvement. Fleet-internal (D1/D11).
- Data: REFEREE docs/referee/scratch/n5t_probe.py (from VJ00 §4 only): 83,472 switches, 3,855 flat, 0 failures of A, B, T;
  negative control fails on every flat switch (113/113). REFEREE-2 docs/referee-2/R2-N5T/vjbf.py (all-plays oracle): all
  3-vertex games (up to relabelling) + 5,000 random 4-7-vertex games and their 5,000 duals, 936,826 switches, 33,103 flat, 0 failures; mutation tests fail as they should.
  L-NEW: no repeated (σ, τ) state found (n5_lock.py, all start pairs, 1,600 games with n ≤ 8; all climbs; every step-2 run,
  12,000 random games and the M1 families, terminated).
- Signatures: REFEREE docs/referee/R-N5T.md (referee 87839f2 + 1cdcdc1; §C 368a7a7): SIGNED WITH GAPS (G-B1, G-B2, G-N2 closed;
  G-N1 DATA). REFEREE-2 docs/referee-2/R2-N5T.md (referee-2 0fb5fd2; §C §8 fd5abd8): SIGNED WITH GAPS (G-N5T-1 DATA, G-N5T-2 scope,
  G-N5T-3 outside; notes N1-N4). Both §C: no disagreement; joint gap list G-B1, G-B2, G-N2 (closed), G-N1 = G-N5T-1 (DATA, both sides), G-N5T-2 (scope), G-N5T-3 (outside), notes N1-N4 (applied by L-NEW as wording, e7157417 + 110a2228; statement unchanged from 812ecba). I1 counts agree: one-player n = 3, 2,270 triples, both referees independently.
- Gauntlet: N5 has passed step 2 (data; second implementation in progress, L-COMP) and step 3 (L-LIT T20, signed with caveats).
  This entry is a partial step-4 lemma (termination). GAPS G-N5-TERM: termination half closed by this entry on landing;
  running-time half open.
