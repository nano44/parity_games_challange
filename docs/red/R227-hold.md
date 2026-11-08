# R227 own item: the HOLD GADGET (L-RED successor 61, Opus 5.5, D1 / D18 / D14; 2026-11-08, date -u)
Brief (Lead 15:52Z): between a designed tower (HP_mup / HP-b) and GROW7's replaying low race, build a gadget that holds each tower value
for ≥ 2 steps, aiming at A ~ 2K for a K-valued High. Measure A, T3 and N + M at two or three tower heights on both engines (own.py and
L-NEW's asc197 at f98e93ee), freeze every instance, and decide: linear A in K, or an exact obstruction.
Labels: PROVED (lane) / CONJECTURE / DATA / DEAD. This is not a TARGET.md claim. G-N5-TIME stays OPEN, and N5′-xi stays a CANDIDATE (D1).
Engines:
- own.py: R221's IDEAL-CYC Howard run, [E-LEV], with the A score from experiments/red/r226/ascore226.py (A = max(1, maxalt)).
- asc197.py: L-NEW's Γ3 engine, claude/l-new f98e93ee, run from a detached scratchpad worktree (removed after use).

Part 1 (pushed 2564c6fa) covered h = 2 and the lemma. Part 2 adds h = 3 (§5) and the GROW7 second carry (§4).

## 0. Verdict
| item | label | basis |
| --- | --- | --- |
| Lemma ALT-H: A ≤ 2·H + 3, where H = #tops strictly more relevant than the pair, in the same (v, I) | PROVED (lane), given E-MON3 on (v, I) | §1. On data: 0 violations on 17 frozen instances. Tight on CX4_n21 (A 5, H 1) |
| Stepping stone «A ~ 2K from a K-valued High» | its CEILING is linear: A ≤ 2K + 3 | ALT-H. So linear A in K is the most a held High can give, and it decides nothing about ALT-POLY |
| Hold gadget at h = 2 / 3 (HP2_mup / HP3_mup under GROW7): template HOLD, 4 × 288 builds | NOT achieved: A ≤ 5 at h 2, ≤ 7 = GROW7 at h 3 (race only; tower entries come after it) | §3, §5 (DATA). Both engines agree |
| Second carry above e8 (CX4 12,000 + GROW7 8,000 random builds) | NOT achieved: A ≤ base (5 / 7) | §4 (DATA) |
| What a working hold must do | EXACT REQUIREMENT, not an obstruction proof | §2. Each High entry must EXPEL w (the more relevant letter of the pair), then w and x must re-enter before the next High entry. Towers change mostly in β-faces (HP2: max 3 e-tops at any (v, I) in T 11), so they give few e-entries at the race |

## 1. Lemma ALT-H (PROVED, lane)
Setting:
- Fix a vertex v and a maximal interval I on which Λ(v) is constant.
- E_t := the e-vertices of Π_t(v), for t ∈ I.
- tops(v, I) := the most relevant e of E_(t−1) Δ E_t, one per change, in time order.
- Premise E-MON3 on (v, I): every top lies in the new set E_t. This is L-NEW's E-MON3 (box 197 §7), counted as lexdec. It is needed:
  - The full Π-difference may be topped by a β-node, so the e-only top could leave.
  - lexdec = 0 on every instance below, on both engines.

Statement. Let y be a letter. Then
- (ii) #(tops = y) ≤ 1 + #(tops strictly more relevant than y, strictly between the first and the last y-top);
- (iii) for letters x ≠ y with w := the more relevant of x and y: alt(x, y) ≤ 2·(1 + H_w) + 1, where H_w := #(tops ≻ w) in tops(v, I).

Proof.
- (ii): Let y be the top at changes i < j, two consecutive y-tops. By E-MON3, y ∈ E_i, and y ∉ E_(j−1), since at change j the letter y
  enters.
  - So y leaves at some change k with i < k < j.
  - At change k, y lies in the difference, so the top z_k of change k satisfies z_k ⪰ y. And z_k ≠ y, because by E-MON3 z_k enters while y
    leaves. So z_k ≻ y.
  - Distinct consecutive pairs (i, j) give distinct changes k. Summing over the consecutive pairs gives (ii).
- (iii): An alternation x y x y … of length L uses w at least ⌊L/2⌋ times, so ⌊L/2⌋ ≤ #(tops = w) ≤ 1 + H_w by (ii). Hence L ≤ 2·(1 + H_w) + 1. ∎

Remarks.
- (ii) iterates to n_y ≤ 2^(#letters above y), which is Lemma BIN's shape. ALT-H is therefore NOT a polynomial bound. It says only that
  alternation is paid for by entries strictly above the pair.
- L-NEW 65's BOX 198 (Lead brief: «charge alternations to High changes») may contain the same statement. I have not read any BOX 198 SHA;
  this lemma was derived independently.

DATA: tool experiments/red/r227/alth227.py. Unit: one (v, I). Set: every frozen instance in experiments/red/r226/inst plus r225 CX4_n21 and
OFFUP_n4 (17 genomes). Scope: own.py, cap 3000.
- Violations of (i), (ii) and (iii): 0 / 0 / 0.
- H at a max-alt pair (min over pairs): CX4 1, GROW7 6, GROW8 7, DSALT9 10, HP6b-8b 2.
- CX4_n21 is TIGHT: A = 5 = 2·(1 + 1) + 1. GROW7 (A 7 vs bound 15) and DSALT9 (A 9 vs bound 23) are not tight.

## 2. What the stepping stone needs (READING from ALT-H and CX4's trace)
- GROW7's A 7 is the pair (e10.0, e15.1) at x10. The tops are e13 e10 e14 e15.1 e10 e15.1 e16.3 e8 e13 e10 e14 e15.1 e10. Here e10 is the
  race bonus, entered at every even step; e15.1 is the digit that re-enters.
- CX4 holds x17 for 2 steps because x17's next counter value becomes its best option only after the race tick (x9 / x14 have Ξ → x18, and
  e10 enters there). The hold is a FEEDBACK of the race into the High's options, not a delay line.
- By ALT-H, A ~ 2K needs K entries above w inside ONE (v, I). Each of those entries must expel w; then w, and after it x, must re-enter before
  the next High entry.
- HP_mup towers change mainly in β-faces. The top mover x6 of HP2 changes its option at every step from t = 1 to t = 10, yet its own e-set changes
  once (t 10). The most e-tops at any (v, I) of HP2 is 3, over T 11. So a tower hands the race few e-entries per step of its own run. A hold must turn tower steps into e-entries above w AND
  expel w at each one.

## 3. Hold template at h = 2 (DATA)
Tool: experiments/red/r227/hold227.py. Build:
- Base: union(GROW7_n34, HP2_mup), with tower gates placed below or above.
- u := the tower's top mover (HP2: x6, K = 10 options, Ξ-targets z_k).
- Hold movers: for each k, a NEW level-1 mover h_k with option (W → w, Ξ → z_k) and, if two = 1, a second option (W → w, Ξ → x18: the race,
  CX4's x9 / x14 pattern).
- Variant REPLACE (KEEP = 0): x17's options become K options Ξ → h_k, with ascending gates.
- Variant KEEP (KEEP = 1): x17 keeps its options and gets the K hold options added.
- Sweep: tower placement (2) × w ∈ GROW7's level-0 movers (18) × two (2) × gate place (2) × beta order (2) = 288 builds per variant.

Counter: A = max(1, maxalt). Unit: one genome. Scope: own.py ([E-LEV], cap 3000). Cross-check: asc197 at f98e93ee on the frozen best.
| variant | builds | A histogram (own.py) | best (A, #tops, T) | frozen (sha1) | N, M, N + M | asc197: maxalt, maxtops, T3 |
| --- | --- | --- | --- | --- | --- | --- |
| REPLACE | 288 | 3: 288 | (3, 10, 13) | inst/HOLD2_n84.json (0b08705f…) | 84, 181, 265 | 3, 13, 13 |
| KEEP | 288 | 3: 144, 5: 144 | (5, 13, 13) | inst/HOLD2K_n84.json (423a4a88…) | 84, 175, 259 | 5, 13, 13 |
| GROW7 alone (control) | 1 | 7 | (7, 13, 13) | r226/inst/GROW7_n34.json | 34, 86, 120 | 7, 13, 13 |

- REPLACE removes x17's own low-digit routes, so the low race no longer replays: A 3.
- KEEP keeps the race, but the hold options lower it to A ≤ 5.
- In neither variant does the tower's run reach the race as e-entries above w. ALT-H's H at the best pair is 0 (REPLACE) and 2 (KEEP).
- VERDICT h = 2: the hold gadget is NOT realized by this template. This is a failed construction, not an obstruction proof. Both engines
  agree on maxalt for all three genomes.

## 4. Second carry above e8 (DATA)
Tool: experiments/red/r227/carry2_227.py. Each random build adds to the base:
- a level-1 mover c whose gate is the global top (its e is more relevant than CX4's carry e8);
- c's W-target: either an existing level-0 mover, or a NEW level-0 mover with one random Ξ option;
- c's Ξ-target: random;
- one new option at a random mover m with Ξ → c.

| base | builds | A histogram | best | frozen |
| --- | --- | --- | --- | --- |
| CX4_n21 (A 5) | 12,000 | 1: 221, 2: 1,963, 3: 1,207, 4: 231, 5: 8,378 | (5, 11, 11), N 23, M 38 | inst/C2CX4_n23.json (57b895ff…); asc197: maxalt 5, maxtops 11, T3 11 |
| GROW7_n34 (A 7) | 8,000 | 1: 67, 2: 1,263, 3: 487, 4: 182, 5: 1,401, 6: 9, 7: 4,591 | (7, 13, 13) = base; no gain, nothing frozen | out/c2_g7_2712.log |

Also run (no gain, logs in out/):
- BLOCK COPY of CX4's carry chain {x7, x8, x9} plus up to 2 other movers, copy gates at the top or just under x8, entry at x17 (or x17 + x18):
  - on CX4: 1,376 builds, best A 5;
  - on GROW7 (up to 1 extra mover): 256 builds, best A 7.
  - Tool: blockcopy227.py.
- Greedy self-loop growth on GROW7: 1,500 samples, no gain. Tool: selfgrow227.py.
- Unit: one genome. Scope: own.py.

## 5. h = 3 (DATA) and next
Same template, base union(GROW7_n34, HP3_mup), u = HP3's x9, K = 14. Counter, unit and scope as in §3.
| variant | builds | A histogram (own.py) | best (A, #tops, T) | frozen (sha1) | N, M, N + M | asc197: maxalt, maxtops, T3 |
| --- | --- | --- | --- | --- | --- | --- |
| REPLACE | 288 | 4: 288 | (4, 7, 17) | inst/HOLD3_n125.json (ba7a6276…) | 125, 248, 373 | 4, 7, 17 |
| KEEP | 288 | 4: 144, 7: 144 | (7, 15, 17) | inst/HOLD3K_n125.json (2c3e610b…) | 125, 252, 377 | 7, 15, 17 |
- The max-A interval of HOLD3K is GROW7's race VERBATIM: tops at x18's β-node, t 1-13, are those of GROW7 (§2). The tower's e-entries
  (e124.0, e43.13) come at t 15-16, AFTER the race is finished. The tower and the race run in SEQUENCE and do not interleave.
- A against tower height (best of the template): h 2 → 5, h 3 → 7; GROW7 alone 7. Neither height exceeds the race alone. So there is NO
  growth in K (K 10 → 14) from the tower. This is a failed construction (DATA), not an obstruction.

Next:
- A High whose every entry expels w. Candidate: chain CX4's threshold. Carry k fires when the race value at x18 crosses θ_k = val(the e-route
  of the carry gate g8_k). That needs K thresholds crossed in order, one per full low replay, i.e. a W-route of carry k that contains carry
  k − 1's state.
- The nested version waits for a linear one.
