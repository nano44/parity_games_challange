# R241: KEY-TAU (box 213) and KEYSIDE-ALL (box 215) against L-RED's own engine — KEY-TAU (i), (ii), (iii) SURVIVE; box 215 as stated DEPENDS ON NUMBERING (its e-index form SURVIVES)
L-RED successor 69 (session_01V5yGRZMU6zgaX7o1n7CQzP, Opus 5.5 high), D1 / D18 / D21 (L53). Lead «go» 06:22Z 2026-11-13. Written 2026-11-13T08:18Z (date -u).
Labels: VERDICT (this lane's, on the data named; not a proof, not a referee signature), DATA, READING. Nothing here is a RESULTS entry, M3 or
M4; no bound for N5 or N5′-xi is claimed or attacked. **G-N5-TIME stays OPEN.** Box 213 / 215 tools were NOT read before this verdict was
written (the brief's rule); only their docs, and the instance files named below (inputs).

## 0. Verdicts
| claim (object) | verdict | evidence (counts from out/summ241.txt) |
| --- | --- | --- |
| KEY-TAU (i) (box 213 §3) | **SURVIVES** | kp, kpf, kpa = 0 on 8,047 runs (41,097 non-fallback steps), every numbering tried, + 76,650 climb evals; n5v xdiff 0 on 1,227; controls fire |
| KEY-TAU (ii) | **SURVIVES** | mukappa, muinc, muflat, mulen, unreach = 0 on the same runs |
| KEY-TAU (iii) | **SURVIVES** | kviol = 0; nomove ([NE]) = 0 |
| premises [STD], TAU3, W3-ALL as box 213 uses them | hold on every run | std, tau3, w3 = 0 |
| box 215 KEYSIDE-ALL, as stated (gate-index keys of P-IDEAL-KEYS) | **DEPENDS ON NUMBERING** | 0 on Γ3 as built (box 189 numbering: e-vertices in gate order, eord 0); on an isomorphic renumbering of Γ3 [M] (kpg) and KEYFLIP′ (kflip) fail and KEYFLIP's bound moves(x) ≤ 1 + KF_x fails (kflipm); 14 instances saved (§4), n5v xdiff 0 on all |
| box 215 with e-index keys (the numbering-free form) | **SURVIVES** | every *_e counter 0 under every numbering, incl. the 14 instances |

KEY-TAU is stated with e-indices («the e-indices of its τ-path to c_W read from c_W», box 213 §3) and is therefore numbering-free as
stated: it held unchanged on every renumbering. Box 215 identifies the e-index key with the gate-index key through box 189's numbering
(box 215 §1: «The e-vertices of Γ3 are indexed in gate order …, so box 213's root-first e-index key orders options as this key does»);
that identification is the only place the numbering enters, exactly R240's pattern for FLAT-IDX. The repair is one word: read every key
of box 215 §2 with the e-vertex index instead of the gate index g(x, k) (or state «on Γ3(G) numbered as box 189 numbers it»).

## 1. The statements attacked (quoted) and their premises
- Box 213 (claude/l-new 14340979, docs/new/N5-KEYWIN-box213.md, sha1 3d3726596b636b0361cd46595db669ce8d890078; identical at cd4f7f4d and at
  the l-new head ad64c6a8 when read), §3 «**Statement.** (i) σ_(t+1)(x) = the first option of x's least-key τ-path in X_t, for every mover x.
  (ii) μ_(t+1)(x) = κ_t(x) ≤ μ_t(x) for every mover x, with strict inequality whenever σ_(t+1)(x) ≠ σ_t(x). (iii) Hence every mover switches at
  most |K(x)| − 1 times before the first fallback, K(x) the set of keys of τ-paths of x in the W-graph, and T_key ≤ Σ_x (|K(x)| − 1).»
  Setting (§3): «G any genome; N5 from S3 on Γ3(G); t any state before the first fallback; [STD]. A_t(x) := {σ_t(x)} ∪ {w : (x, w) ∈ Iσ_t}.
  X_t := the arena of S4a at t (Even v keeps A_t(v), Odd v keeps τ_t(v)).» Keys: «the tuple of its e-vertices' indices read from c_W».
- Box 215 (cd4f7f4d, docs/new/N5-KEYSIDE-box215.md, sha1 1d130f9a0a22d3996208381e7bfa427b9062626a): [M] «s_(t+1)(x) is the option of A_t(x)
  with the least key under s_(t+1)»; LOCAL-KP, PAIR-KF, KEYFLIP′ «Let deg(x) = 2. If x ∈ Mv_t, then s_t(x) is the option of x with the least
  key under s_t: KP_(s_t)(x).» with «Hence moves(x) ≤ 1 + KF_x», PAIR-MOVES, CASCADE, F ≤ T, LADDER (§2, quoted there from R111 /
  P-IDEAL-KEYS b302bbf5). Keys: P-IDEAL-KEYS's key_s(x, k) = key_s(wt(x, k), s(wt(x, k))) followed by g(x, k), g the gate index.
- Premises (as box 213 §1 quotes them; landed): R125 ESC3-ALL and W3-ALL («every option of a level-ℓ mover has arena value (c_W, ∅, 5ℓ + 4),
  no mover is its own arena cycle node and TIE(x) = A(x)»), R117 TAU3, R122 BETA-ACYC / LAMBDA-CONST (used by box 213's G-2 only, not attacked
  here), [STD] (READING: N5 from S3 visits only standard states before its first fallback), [NE] (every pre-fallback step moves a mover).
- READING (mine, before the data): with W3-ALL every key of one mover has one length, R contains no vertex above c_W, and S1 (iv)'s BFS from c_W
  over predecessors in increasing index discovers a mover y's options in the order (discovery rank of wt, index of e): (i) is S1 (iv) read on
  X_t. The ONLY order the BFS uses is the vertex index of the e-vertices, so (i)/(ii) cannot depend on the numbering when stated in e-indices,
  and box 215's gate keys agree with it exactly when the e-vertices are numbered in gate order. The data test this reading; they do not prove it.

## 2. Engine, counters, controls (experiments/red/r241/)
- Engine: n5s237.py mode spec (L-RED 67; SPEC-exact, written from the SPEC text, state-by-state equal to box 190's n5v on 8,900 games, R237),
  from S3 on Γ3(G) = box 189 gamma3.build(G, all pads) (OBJECT, l-new fcba92fc), states 0 .. F1 − 1 (F1 = first fallback).
- kt241.py computes, independently of S1's BFS: A_t from Ξσ_t (SPEC S2 values, n5s237.vjproc); κ_t by a level-order DP over the genome's
  W-graph (least root-first e-index key over A_t at every mover below); μ_t by following x's play vertex by vertex under (σ_t, τ_t); box 215's
  key_s / KP_s / KF / flips with gate indices AND with e-indices (*_e); S4a's own arena values W and choice (for w3 and kpa).
- 24 must-0 counters + 9 e-key twins (definitions in kt241.py's docstring): std, tau3, w3, lenvar, kp, kpf, kpa, unreach, mukappa, muinc,
  muflat, mulen, kviol, nomove (KEY-TAU and premises); eord, kpg, lkp, pkf, pkfa, kflip, kflipm, casc, ftt, ladder (box 215 as stated); *_e.
- Controls (each must fire; out/summ241.txt, kt_rand2.out rows ctrl_*; 100 genomes each): KT_MODE=xi (N5′-xi, Howard's tie rule) on gen dense:
  kp 655, mukappa 1,067, muinc 736, kviol 26, kpg 638, kpg_e 638; on gen deep: kp 1,031, mukappa 2,721, muinc 1,950, kviol 56, kflip 344,
  kflipm 165 and kflip_e 344, kflipm_e 165 (so the e-key form also has a firing control); KT_CTRL=1 (κ = the MOST key): kp 523, kpf 245,
  kpa 768; KT_CTRL=2 (μ read leaf-first): mukappa 613, muinc 106; KT_CTRL=3 (gate indices permuted): kpg 370; climb control (ctlxi, KT_MODE=xi,
  300 evals): 69 candidates (out/climbs241.txt).
- Second engine: box 190's n5v mode spec from box 21's S3 pair (OBJECTS), σ compared state by state up to F1 (xdiff); on every json input
  and every 10th / 20th generated genome, and on every saved instance.
- Numberings (KT_PERM): none (box 189's), e (the e-vertices permuted among themselves), all (every vertex permuted); seeds named per row.
  A renumbering is an isomorphic copy of Γ3(G); SPEC's tie-breaks (FIX 1-4) read indices, so N5's run may change; KEY-TAU's statement is then
  read with the new e-indices.

## 3. DATA
Every number is from out/summ241.txt (summ241.py) or out/climbs241.txt; out/SHA1SUMS pins them. TAU = the 14 KEY-TAU / premise counters;
GATE = box 215 as stated (10); EKEY = box 215 with e-index keys (9). Original numbering = box 189's.
| set (file) | runs | numbering | TAU | GATE | EKEY | Σ T | n5v (xdiff) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| hard: L-COMP box 46 bests (12 climb46 + 3 climb46e, incl. BEST_B3_WU151_NM163), TAUESC ×2, towers ×5, seeds46 ×8 (kt_hard_none) | 30 | original | 0 | 0 | 0 | 3,666 | 30 (0) |
| L-NEW's 81 frozen genomes (box 212 run212.sh ALL; kt_frz_none) | 81 | original | 0 | 0 | 0 | 1,721 | 81 (0) |
| L-COMP's 224 Ξ-cyclic tower variants (box 46 inst/xtower; kt_xtower_none) | 224 | original | 0 | 0 | 0 | 25,252 | 224 (0) |
| hard, renumbered (kt_hard_e1/e2/e3/all1/all2) | 150 | e ×3, all ×2 | 0 | 5,403 (kflip 1,260, kflipm 39, ladder 8) | 0 | 436 | 150 (0) |
| frozen, renumbered (kt_frz_e1/all1) | 162 | e, all | 0 | 3,070 (kflip 447) | 0 | 285 | 162 (0) |
| generated, original (kt_rand: own ×3, eg195 rand/dense/deep/noesc/esc/lvl0, Ξ-cyclic ladders ×500) | 3,200 | original | 0 | 0 | 0 | 3,844 | 160 (0) |
| generated, renumbered (kt_rand2: 14 sets × 300, seeds 7/8/9) | 4,200 | e, all | 0 | 25,129 (kflip 2,246, kflipm 12, ladder 5) | 0 | 5,893 | 420 (0) |
| climbs (climb241.py; OBJ nlk, slack, mu, T, cyc; 3 under KT_PERM with CL_ONLY=nf; 2 SHAPE ladder climbs from DBL4 / H5) | 76,650 evals | both | 0 | — | 0 | — | — |
- BEST_B3_WU151_NM163_e934d333 (sha1 e934d33351b78751106faec9e8fd32794da4fb6b, claude/l-comp 4756cb19): original numbering T 151 (= L-COMP's
  T_key), 537 switches, 410 (mover, state) pairs on a Ξ-cycle option, every counter 0, n5v xdiff 0. Under the five renumberings: TAU 0, EKEY 0,
  GATE kpg 22-43 and kflip 5-10 (kflipm 0), T 2-5, xdiff 0 (kt_hard_*.out).
- Towers on the original numbering (KEY-TAU (iii) read): maxsw 15 / 31 / 63 / 127 on DBL4 / H5 / H6 / HIT7 (box 213's kcount213 numbers
  reproduced by an independent count), kviol 0; LADDER checked on all five (they are 𝓛^R_d-shaped), 0.
- Side DATA (not a claim): N5's run on the long instances is tuned to box 189's numbering: renumbering the e-vertices alone shortens it
  (BEST_B3_WU151_NM163 151 -> 2-5; HIT7 299 -> 4; frozen Σ T 1,721 -> 143), consistent with the reading that S1's BFS order IS the key order.

## 4. The numbering dependence of box 215 (instances)
- Mechanism (READING, then DATA): S1 (iv)'s BFS orders a mover's candidate options by (rank of the W-target, index of the e-vertex); box 215's
  keys order them by (key of the W-target, gate index). The two agree iff the e-vertices are numbered in gate order (eord 0). On an isomorphic
  renumbering N5 still follows the e-index key (KEY-TAU (i): kp 0), so wherever the gate order and the e-index order of two options disagree,
  [M] in gate keys fails (kpg), a moving degree-2 mover need not take its gate-least option (kflip), and the bound moves(x) ≤ 1 + KF_x can fail
  (kflipm); on renumbered 𝓛^R_d towers LADDER's moves(x) ≤ 1 + F(l − 1) fails (ladder). LOCAL-KP, PAIR-KF, CASCADE, F ≤ T stay 0 in gate keys too:
  they are statements about key sequences only (no step rule), as box 215 says.
- Instances (experiments/red/r241/inst, .json = {genome, perm, pseed}, .pg = the renumbered Γ3 in pgsolver format, inst/SHA1SUMS; numb241.py
  check re-runs each: out/numbcheck241.out): original numbering every counter 0; renumbered TAU + EKEY 0; n5v xdiff 0 on both runs of all 14.
  | instance | renumbering | kpg | kflip | kflipm | ladder | T | n |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | NUMB_e1_HIT7_d28_F254 (tower) | e, seed 1 | 25 | 13 | 1 | 1 | 4 | 850 |
  | NUMB_e3_H6_d24_F126 (tower) | e, seed 3 | 35 | 6 | 2 | 2 | 4 | 730 |
  | NUMB_e3_RECF4_d20_F60 (tower) | e, seed 3 | 24 | 9 | 1 | 1 | 3 | 610 |
  | NUMB_e1_BEST_B3_WU151_NM164_5fdc0426 (L-COMP best) | e, seed 1 | 67 | 14 | 2 | 0 | 5 | 822 |
  | NUMB_e1_H6_x0_glo_blo_p0 (L-COMP seed) | e, seed 1 | 31 | 11 | 1 | 0 | 3 | 737 |
  | NUMB_e1_deep2452_416 / _471 / _517 (eg195 deep) | e, seed 1 | 5 / 12 / 15 | 3 / 4 / 4 | 1 / 1 / 1 | 0 | 2 / 4 / 3 | 190 / 280 / 220 |
  | NUMB_all2_deep2453_64 / _303 / _466 | all, seed 2 | 4 / 15 / 13 | 3 / 7 / 5 | 1 / 1 / 1 | 0 | 3 / 4 / 2 | 250 / 220 / 220 |
  | NUMB_e1_deep2451_0 / _1 / _3 | e, seed 1 | 17 / 4 / 14 | 0 / 2 / 6 | 0 | 0 | 3 / 1 / 2 | 318 / 100 / 280 |
- SPEC-line trace (trace241.py, out/trace241.out), NUMB_e1_deep2452_416 (190 vertices): mover 10 (level 5), options 0 / 1 with gate indices 21 / 11
  and e-vertex indices 62 / 67 (81 / 71 in Γ3 as built). N5: s(10) = 0, 1, 0 at states 0, 1, 2 (2 moves). Gate keys: option 1 least at every
  state (KF 0), so «moves ≤ 1 + KF» = 1 fails; e-index keys: option 1, 1, 0 least (KF_e 1), 2 ≤ 2 holds, and state 2's move back to option 0 is
  exactly the e-key flip. NUMB_e1_HIT7_d28_F254: mover 43 (level 21) moves 3 times, KF 1 in gate keys, KF_e 2.

## 5. What survives, stated numbering-free
- KEY-TAU (i)-(iii) exactly as box 213 states them (keys = e-vertex indices).
- Box 215 §2 with every key read as P-IDEAL-KEYS's key with g(x, k) replaced by the index of e_(x,k) in the game N5 is run on: [M], LOCAL-KP,
  PAIR-KF, KEYFLIP′ (and moves(x) ≤ 1 + KF_x), CASCADE, F ≤ T, LADDER — every *_e counter 0 under every numbering. Equivalent for box 189's Γ3
  (eord 0 there). The proofs of box 215 §2 use nothing about g but that it is an injective index per option, so the e-index form needs no new proof.

## 6. Not claimed; kill criteria for others
- No bound; T_key may be exponential (towers: maxsw 2^k − 1). Nothing after the first fallback. G-2 (box 213 §4) and MERGE / RETURN / RENEW
  not attacked. KEY-TAU is a reformulation with a monotone potential, not a running-time result (box 213 §8). **G-N5-TIME stays OPEN.**
