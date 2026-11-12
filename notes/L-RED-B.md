# L-RED-B notebook (second, independent adversary lane; target: L-NEW 72's box 208)
Session 1 (model and effort: see the roster in docs/NOW.md; D1 / D18 / D21, L51) started 2026-11-12 12:52Z (date -u). Start check: docs/agents/handover-checks/L-RED-B.md.
Lead session: session_014FBi6o334DvwT5Uw2kDfoN. Branch claude/l-red-b (from trunk 471aba45).
Files I own: docs/red-b/, experiments/red-b/, notes/L-RED-B.md, docs/agents/handover-checks/L-RED-B.md.

## Resume point
- Object: claude/l-new 8db300fe, docs/new/N5-LEVEL-box208.md (sha1 55e65381…, 502 lines): Lemma LEVEL, WIN, R-INT, R-HEIGHT, K1-TCYC,
  FVS-TCYC (body), Addendum A: Lemma PLATEAU, Theorem ALL-TCYC. All CANDIDATE, scope IDEAL-CYC on Γ(G).
- Report: docs/red-b/B1-box208.md. INTERIM verdict sent to the Lead 13:23Z: every lemma SURVIVES my read and my engine; one write-up GAP
  G-1 in PLATEAU (P6) step (ii) (plays from Y beyond v; repair = F3 + injective ext(g, ·) + NO-TIE); notes N-1, N-2. No DEAD.
- Tools (experiments/red-b/): eng.py (own engine), lev.py (27 must-0 counters + coverage), gen.py (random shapes, exhaustive
  enumerator with part / parts), mut.py, sweep.py, climb.py (resumable, work/), xcheck.py, cmpT.py, requote.py, run_b1.sh (sets A-H),
  check.sh (gate self-check, ~2 s). Outputs out/.
- State of the runs (2026-11-12 14:10Z): sets A, B, W, X, T, C, D, E, G done (outputs in out/, pinned in out/SHA1SUMS). G (5.8M random
  genomes) ran as short single-core chunks while the first push was in the gate, before any «go»; said so in the report §5.
  NOT started: F (exhaustive (1,5), (3,4), (1,6)) and H (climbs): ONLY after the Lead's «go», at most 2 at once, as tracked tasks
  (`bash run_b1.sh F`, `bash run_b1.sh H`; restart-safe, finished chunks skipped; climbs resume from work/climb_*.json).
- Pushes: start check d81ff541 is on origin (push ended 14:06Z, VERIFY PASS). Second commit (report + tools + outputs): see git log.
- After the runs: fill §5.1 of the report, write out/SHA1SUMS (`cd out && sha1sum *.out > SHA1SUMS`), commit by explicit path, push with
  scripts/push.sh (pgrep first; never two pushes), message the Lead with the final verdict.
- Independence rule: do not read L-RED 66, REFEREE 32, L-COMP 19 on box 208 before the FINAL verdict is sent.

## Queue
1. Second push (report + tools + outputs) through scripts/push.sh; tell the Lead the SHA.
2. «go» from the Lead → run_b1.sh F and H (two tracked tasks).
3. Fill the report's §5.1 and final verdict; message the Lead.
4. If asked: the Γ3 form (box 209) is NOT my object; ask the Lead before touching it.

## Sources opened
- trunk docs/RESULTS.md R104 (l. 9864), R118 (l. 13607): read 2026-11-12 (title lines; definitions of the genome, Γ(G), IDEAL-CYC).
- docs/new/P-N5-XICYC.md §1-§5 and docs/new/P-N5-XICYC-fixes.md entries 1-3 (R118's packet: IDEAL-CYC, Howard step, F1-F6, DOM, STRICT,
  PATH, BR-SEG, BR-SEG-G with its repaired proof STRICT-G / PATH-G): read 2026-11-12.
- docs/red/P-N5-REALIZE.md §1-§3.3 (R104's packet: genome, Γ(G) vertex by vertex, priorities, start): read 2026-11-12.
- claude/l-new 8db300fe docs/new/N5-LEVEL-box208.md, all 502 lines: read 2026-11-12.
- No external source (arXiv / DOI) opened yet. VJ00 and Friedmann arXiv 1106.0778 are cited by R118 as premise [VJ]; I use the order
  as R118's packet states it and have not opened the papers myself.

## Dead ends
- None yet (no statement of box 208 killed; attacks tried and why each fails: docs/red-b/B1-box208.md §5).

## Things only I know
- My engine's e-priority order is P-N5-REALIZE §3.1's (by (lev(owner), gate index)). The optional genome key "eorder" (mine, tests only)
  replaces it by an arbitrary order; box 208 says [E-LEV] is not used, and 30,000 such genomes gave 0 violations.
- Exhaustive tiers with M = N are vacuous for LEVEL (every mover has one option, T = 0). The first non-trivial tiers are M ≥ N + 2.
- A gen.py bug I made and fixed before any output used it: the loop variable `part` shadowed the chunk parameter (chunks came out
  empty after the first group). The outputs out/exh_* of set D were produced by the unchunked code (checked: counts equal the formula).
- Howard ties (several best gates, current one not best) are rare on the frozen genomes (2 in 78 runs) and common on small random
  genomes; the tie rule is a parameter of eng.howard_run ("keep-low", "high", "rand").
- The Python engine does about 6,000-7,000 tiny genomes per second with all reference states; (N, M) = (2,5) has 294,865,920 genomes
  and is not run exhaustively.
