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
| S7 | most-improved single switch, invariant tie-break | not killed, not defended | padding attack open (linear padding fails) |

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
