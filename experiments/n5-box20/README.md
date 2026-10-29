# Box 20: SBC of L-NEW's N5-SF, exhaustive and random small-n tables (L-COMP successor 7)
Lead brief 2026-10-29 15:20Z (D18). N5-SF is defined in docs/new/N5-SF-box54.md on claude/l-new 56a42d4f. By Theorem SF-RED (lane),
N5-SF is polynomial IFF SBC is polynomial. All numbers below are DATA. CONJECTURE SF-POLY stays OPEN.

## Tools and cross-check
- lnew_box54/n5sf.py, sfrun.py: VERBATIM copies of claude/l-new experiments/new/box54/{n5sf,sfrun}.py @ 56a42d4f. Its engine,
  experiments/new/box21/n5x.py, is identical on trunk and on 56a42d4f.
- Cross-check: my run of sfrun.py reproduces L-NEW's logged sf_alt.txt rows exactly on ffin12_n32, lend107_n32, theta_thf16 and
  long121_n40 (n, N5 it, N5 phases, SF it, SF fb, cycle, SBC, LAM, SEG, SEGMAX).
- sf20.py: enumerates games as box 17 does (model C(n), every start pair; or uniform random C(n)) and steps N5-SF and N5 once per state
  (cached). SBC_σ = transitions at which σ̄ changes (= sfrun's SBC). SBC_τ = the mirror (τ̄ = Even's best reply to τ on G^d).
  SBC = SBC_σ + SBC_τ.
- Kill checks per start: CYCLE (a state repeats); REGION (the final S5 regions differ from harness/zielonka.py); OPT (the final σ still
  has an improving edge).
- pin20.py: pins the max-SBC and max-iteration game of each table, reruns N5-SF from the stored start and checks against Oink zlk.

## DATA (0 violations of CYCLE / REGION / OPT in every table)
| table | games | start pairs | max SBC (σ̄; τ̄) | max SBC/n | max SF it | max N5 it | max (SF − N5) | max SF fallbacks | SF it total / N5 it total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C(2) exhaustive | 144 | 256 | 1 (1; 1) | 0.50 | 2 | 1 | 1 | 1 | 116 / 112 |
| C(3) exhaustive | 21,952 | 110,592 | 2 (2; 2) | 0.67 | 3 | 3 | 1 | 1 | 99,968 / 101,292 |
| C(4), every 16th game (exhaustive slice) | 810,048 | 17,032,640 | 4 (4; 4) | 1.00 | 6 | 6 | 3 | 2 | 20.8M / 22.4M |
| random C(5), seed 17 | 5,000 | 576,352 | 5 (3; 3) | 1.00 | 5 | 6 | 3 | 2 | 854,896 / 959,078 |
| random C(6), seed 17 | 5,000 | 4,004,109 | 7 (4; 4) | 1.17 | 7 | 9 | 4 | 2 | 6.87M / 7.92M |
| random C(7), seed 17, ≤ 4,096 starts | 1,000 | 1,952,280 | 7 (4; 4) | 1.00 | 6 | 9 | 4 | 2 | 3.57M / 4.11M |
| random C(8), seed 17, ≤ 4,096 starts | 1,000 | 2,548,783 | 7 (5; 5) | 0.88 | 6 | 8 | 3 | 1 | 4.74M / 5.44M |
- n = 4 in full was not run: it would take ≈ 10.5 h on two cores alongside box 17. The every-16th slice is C(4)'s games with global
  index ≡ 0 mod 16 (all start pairs of each).
- Pinned (instances/, pin20.py: rerun from the stored start, regions = Oink zlk):
  - SF_C3_all_sbc (sha1 4fdbf068…, SBC 1 + 1 in one iteration)
  - SF_C4_every16_sbc (b01665c7…, SBC 1 + 3) and SF_C4_every16_sf_it (ffb1fc89…, 6 SF iterations)
  - SF_R5_s17_sbc (f8e51973…), SF_R6_s17_sbc (2b4e61fc…, SBC 4 + 3 = 7 at n 6), SF_R7_s17_sbc (524f34dc…), SF_R8_s17_sbc (92241975…)
  - the max-iteration games of each table
- READING: on small games SBC ≤ 1.17n and SF iterations ≤ N5's + 4. In total, N5-SF takes 7-13 % fewer iterations than N5.
  SBC can exceed the SF iteration count, because σ̄ and τ̄ can both change in one transition.
- For the structured families (friedmannsubexp, fearnleysubexp) see experiments/n5-box21/README.md.

## DONE / FINDINGS / NEEDS
- DONE: tables results/SF_*.json; pins instances/SF_*; tools sf20.py, pin20.py.
- FINDINGS: N5-SF never cycles, errs or stops early on any of ≈ 26M start pairs (n ≤ 8). Max SBC/n is 1.17.
- NEEDS: none.
