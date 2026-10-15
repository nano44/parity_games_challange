# L-SI: strategy-improvement design loop toward M4 / M4-R (owner: L-SI; Lead brief 2026-10-15 10:10Z, box to 22:10Z)

Method (Lead brief): per candidate S<k>, docs/si/candidates/S<k>.md states the exact rule, its bit cost per iteration, which of
B8-B14 it lies outside and why (before testing), and every unproven assumption; experiments/si/ implements it on an own
VJ-valuation engine (Python si.py, cross-checked against the REFEREE-checked PGSolver port; C++ vjfast, cross-checked
against si.py); falsification runs cheapest first (M1 families incl. switchallexp/switchbestexp, the ported lower-bound
families, L-RED's gated families, adversarial hill-climb on n ≤ 10, gadget-chain family search). Dead candidates:
docs/si/DEAD.md with the killing family or instance and the growth. Survivors are reported to the Lead at once; gauntlet
steps 2-5 are not run by L-SI.

## Candidates and verdicts (end of box)
| id | rule | verdict | killer |
| --- | --- | --- | --- |
| S1 | Random-Action-Removal = original Random-Facet (M4-R) | KILLED, conditional on L-RED's transfer lemma (REFEREE-2) | FHZ 1410.7530 Thm 6.3 transferred to sink parity games (L-RED R2) |
| S2a | MSF: most-significant-first single switch | KILLED | L-RED's gated Bland counter: exactly 2^N - 1 (reproduced on si.py) |
| S2b | LSF: least-significant-first single switch | KILLED | zadehexp (doubling), DLMM Bland counter (2^n - 1), M_L port (2^(L+1) - L - 2) |
| S3 | steepest single switch (re-evaluated gain) | KILLED | M_L port: 2^(L+1) - L - 2, identical to LSF's run |
| S4 | subgame-optimal start + switch-all | KILLED | switchallexp: counts identical to switch-all (doubling) |
| S5 | Zadeh's least-entered rule, index tie-break | not killed, not defended | no bound covers it (DFH's tie-break is σ-dependent); adversary controls the numbering |
| S6 | Cunningham's round-robin, index order | not killed, not defended | contiguity of a vertex's edges blocks PGSolver's ordering; DLMM-style families for m-memory rules not excluded |
| S7 | most-improved single switch, invariant tie-break | KILLED (L-RED) | FHZ's one-player Random-Facet counter with linear pads (fhz_padded): i(n) = 2 i(n-1) + 4n |

## Obstruction map (end of box): which rule classes die to which construction
| rule class (single switch unless stated) | what the rule ranks by | killed by | source |
| --- | --- | --- | --- |
| multi-switch, locally / globally optimal (switch-all, switch-best) | all improving edges at once | Friedmann's cycle-gate counters G_n, H_n | 1106.0778 Thm 6.14, 8.4; bench switchallexp, switchbestexp |
| index-based, o(m/log m) memory (Bland, "lowest index first") | a fixed order on edges | DLMM counter families, every index assignment | 2512.16684 Thm 4.3; bench dlmm_bland |
| history-based with designer order (Zadeh's tie-break, Cunningham's ordering) | occurrence record / round robin | DFH, Avis-Friedmann | 1911.01074 Thm 6.18; 1305.3944 Thm 4; bench zadehexp (PGSolver's rule), cunninghamexp (lower-bound ordering) |
| first-difference position (MSF, LSF, and any level-ranked rule) | where the two valuations first differ | gate relabelling: an Odd gate on a relay sets the level (escaped cycle-creating switch), sign and effect stay | L-RED R1 Gate Lemma; bench gated_bland (MSF 2^N - 1), zadehexp / M_L (LSF) |
| valuation magnitude at the switched vertex (steepest = largest increase) | re-evaluated gain | DLMM M_L port (least-preferred-switch counter) | 2512.16684 Lemma 5.4; bench dlmm_ML (2^(L+1) - L - 2) |
| traffic / count (most-improved, Dantzig-like on counts) | number of vertices whose valuation changes | route-isolated bits + linear pads on FHZ's one-player counter | L-RED R5 fhz_padded: i(n) = 2 i(n-1) + 4n |
| randomized: Random-Edge | uniform improving edge | Friedmann thesis | Thm 4.76 (B10) |
| randomized: Random-Facet* (one permutation) | | FHZ SODA 2011 | 1410.7871 (bound stands for RF*) |
| randomized: original Random-Facet / Random-Action-Removal (M4-R) | fresh random removals | FHZ shortest-path counter transferred to sink parity games | 1410.7530 Thm 6.3 + L-RED R2 transfer lemma (REFEREE-2 checking) |
| symmetric SI (both players), any local rule | opponent's counterstrategy edges | van Dijk-Loho-Maat | 2309.02223 Thm 1 (B11) |
| memory rules with the canonical index tie-break / order (S5 Zadeh, S6 Cunningham) | occurrence record / round robin, index ties | not killed in this box; the adversary controls the numbering; L-RED attacking with the FHZ counter | S5.md, S6.md |
Common thread (L-RED's Lemmas T and D, unrefereed): every memoryless single-switch rule ranks improving edges by a quantity
computed from the current valuation structure; pads (traffic), gates (levels), priorities (magnitudes) and the vertex
numbering (indices) are all adversary-chosen inputs that steer such a quantity, and the counters' resets can be routed
through quiet levels (FHZ) or through escapes (gates). A rule that survives must rank by something the input cannot steer
without changing the game's optimal strategies: L-SI found no such quantity in this box.

Findings that outlived their candidates: Claim F' (non-cycle-creating switches, play notion, change nothing above their
level; 0 violations in 20,000 games after L-RED's correction; proof sketch in notes/L-SI.md) and the resulting bound
#MSF switches ≤ (n(n+1)+n²+1)(n²+X+1) in terms of escaped cycle-creating switches X; L-RED's gated counter makes X = 2^N - 1.

| file | what |
| --- | --- |
| candidates/S1.md ... S7.md | the rules, costs, barrier statements, assumptions, data |
| DEAD.md | dead candidates with killers (S1-S4) |
| RESULTS.md (+ RESULTS-extra.md, plots/) | iteration tables, growth fits, log-log plots per family and rule; hand-recorded runs |

Engine and tools (experiments/si/): si.py (Python engine, all rules, CLI solver), vjfast.cpp (C++ engine: valuations,
switch-all, msf, lsf, zadeh, cunningham, most-improved, rar, rfstar), xcheck.py / xcheck_fast.py (cross-checks),
gens.py (ports: randomfacetsubexp, zadehexp, cunninghamexp, DLMM G_n and M_L), gated.py (L-RED's gate transform applied
to the bench), families.py (sweeps; --engine fast), adversarial.py (hill-climb; objectives iters / escapes), famsearch.py
(gadget-chain family search), freeze_test.py (Claim F' test), report.py (tables and plots), check.sh (self-test run by
scripts/verify.sh: engine vs port, vjfast vs si.py, pinned killer instances in instances/).
