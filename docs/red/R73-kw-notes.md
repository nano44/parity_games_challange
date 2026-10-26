# R73: the two K notes red-teamed (L-NEW 21 N5-KW-box42, L-SI 10 N5-KW-box15): no kill; FRZ-U's |R| − 1 and CW-INT are attained; post-freeze kind changes and W-flat kind-B switches stay unreached (L-RED successor 18, box 43; Lead route 21:00Z, date -u)
Targets (Lead 21:00Z):
- docs/new/N5-KW-box42.md (L-NEW 21, sha1 349d553c): ABOVE-h, CSTRICT, KW-FREEZE (a)-(c), WLAG, DIR, H-PATH, CASC-B, CW, PAR.
- docs/si/N5-KW-box15.md (L-SI 10, sha1 5ebbb3b6): W-ONCE, Fact A, FRZ-U, LEN, KIND-MONO, CASC-B, CW-INT.
- Order: (1) CSTRICT / KW-FREEZE (a) n − 1 / FRZ-U |R| − 1; (2) KIND-MONO, DIR; (3) CW, CW-INT; (4) PAR.
𝒞^1O only (one Odd vertex of out-degree > 1, asserted). Labels per L40. Nothing here is a running-time bound. G-N5-TIME stays OPEN.

## 0. Result
- **No kill.** 0 FAIL of every check on:
  - lib41: 253 runs at S3, then 1,012 runs at S3 + 3 random start pairs;
  - 4,267,132 random runs (n 6-18, S3 + 3 random start pairs);
  - all climbs (about 1 h each, §3).
- Bounds attained (DATA, not kills):
  - FRZ-U's freeze index |R| − 1 is reached exactly: a κ-change at run index |R| − 1 (frzu_tight_n14).
  - CW-INT's deg(c_w) − 1 is reached; 11 c_w-switches occur in one game (cw11_n24, CW slack −1).
  - KW-FREEZE (a)'s n − 1: best margin −1 (random runs), −2 (climbs), −3 (library).
- Regimes NOT reached (both lanes report the same vacuity):
  - a post-freeze kind change (KIND-MONO's content), 0 everywhere;
  - a kind-B switch at a W-flat, kind-stable transition of a U3 / U23 stretch with c_w ≻ c_θ (CASC-B's content), 0 everywhere,
    including a 2,700 s climb aimed at it.
- PAR: 0 states with c_w ≻ c_θ and c_w odd, among 1,241,086 + 925 + 2,375 qualifying states (random, lib41 S3, lib41 × starts).
- **Engine check against the lanes (Lead's precondition).** On lib41 at S3, my counts equal L-NEW's §7 numbers exactly:
  - 253 runs; 424 fallback-free runs; 1,061 COARSE_h-strict CSTRICT cases;
  - 34 kind-change transitions and 2 c_w-switches on U3 / U23 stretches with c_w ≻ c_θ.
  - My "qualifying stretches" count (107) is larger than L-NEW's 20. I count stretches of any length, including single states.

## 1. Tools (experiments/red/kw/; written from the note texts; not the lanes' kwfreeze2.py / evcheck.py / kwcheck.py)
- kw18.py. Ξ comes from si.py's Engine (read-only). W, the (σ, τ)-play valuation, is computed in this file from the play, and Lemma
  G (a) (off R, Ξ = W) is checked at every state as a sanity test of that code (ENG_G: 0 failures).
  - Trace: sox.trace (= n5.run, SPEC S3) or ex16.trace from a start pair.
  - Objects as in the notes: stretch (R, θ, w constant in a phase), run (maximal fallback-free run inside a stretch), h = m*, π_v, kinds.
- Checks:
  - PAR at every state;
  - W-ONCE; WLAG (the H_{k−1} membership test written out);
  - ABOVE-h / Fact A for both frames at every state of every stretch (with the constant sets K_W, K_Ξ), and the cycle nodes c_w, c_θ on R;
  - H-PATH; CSTRICT for every Even x ∈ R ∖ {o} and successor z ∈ R;
  - KW-FREEZE (a): the last COARSE_h change of W or Ξ on R, against n − 1;
  - FRZ-U: the last κ(π_v) change, against |R| − 1;
  - KW-FREEZE (b), (c) and LEN's (r − 1)² counts;
  - KIND-MONO (count and direction, post-freeze part);
  - CW-INT (per maximal interval with no kind change and no kind-B switch);
  - DIR (at W-flat transitions); CW (deg(c_w)(1 + B_S + κ_S + f_S));
  - CASC-B (step index inside Γ against |π_v| − 2).
- kwclimb18.py: climb modes frzu / kwf / km / cw / cascb, S3 start, fitness (#FAIL, objective, secondary).
- kwst18.py: library × start pairs and random games × start pairs. per18.py / per18b.py: per-file margins (seed selection).

## 2. Data (0 FAIL in every row)
| space | runs | stretches | runs (fallback-free) | CSTRICT cases | WLAG / W-ONCE checks | PAR states | U3/U23 c_w ≻ c_θ stretches | kind-change transitions there | c_w-switches |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lib41, S3 | 253 | 5,391 | 424 | 1,061 | 4,661 / 2 | 925 | 107 | 34 | 2 |
| lib41, S3 + 3 random starts (seed 43) | 1,012 | 14,735 | 978 | 3,413 | 11,160 / 2 | 2,375 | 411 | 52 | 2 |
| random n 6-18, S3 + 3 random starts (seed 44, 2,700 s) | 4,267,132 | 10,644,416 | 624,464 | 732,246 | 91,689 / 9 | 1,241,086 | 224,733 | 101 | 4 |
- Margins (max over runs with at least one change):
  | space | FRZ-U: last κ-change − (\|R\| − 1) | KW-FREEZE (a): last COARSE_h change − (n − 1) | longest run |
  | --- | --- | --- | --- |
  | lib41, S3 | −2 (p3long_n14, oneodd_c16) | −3 (kw_n16, kw_n24, obr_n32, …) | 40 |
  | lib41 × start pairs | −2 | −3 | 40 |
  | random | −1 | −1 | 6 |
- KM_postfreeze_kindchanges = 0 in every row. CASC-B switches = 0 in every row. DIR's W-flat kind changes: 7 / 7 / 3, all toward
  kind A (P = A by PAR).
- The WLAG count of 4,661 equals L-NEW's §1 count (4,661 W-changing S4a steps after an S4a step on lib41).

## 3. Climbs (kwclimb18, S3; 0 FAIL among all evaluated games)
| mode (objective) | seed | evaluations | best | instance |
| --- | --- | --- | --- | --- |
| frzu (FRZ-U margin) | p3long_n14 | 362,780 (stopped at plateau) | **0**: change at index \|R\| − 1 = 2 | instances/frzu_tight_n14.pg |
| frzu | oneodd_c16 | 1,333,005 | −1 | – |
| kwf (KW-FREEZE (a) margin vs n − 1) | kw_n24 | 48,421 (stopped) | −2 | – |
| km (post-freeze kind changes; then kind-change transitions) | kwm_cex_n24 | 437,805 | 0 post-freeze; 18 kind-change transitions in one U3 run | instances/kc18_n24.pg |
| cw (CW-INT margin; then c_w-switches) | fbrestart_cex_n24 | 1,074,144 | CW-INT margin **0**, 11 c_w-switches, CW slack −1 | instances/cw11_n24.pg |
| cascb (CASC-B slack) | u3ev_n16 | 4,599,950 | regime never reached | – |
- Pins (sha1; n5.py run = (iterations, fallbacks) from n5.run; Oink `--zlk --verify`):
  - frzu_tight_n14.pg 46503678642ea13826c46e23bca7caa91f3d190c; n5 (4, 0); Oink exit 0, solution verified.
  - cw11_n24.pg 5c6dcf2d96681ee5127d33ece86970c94da1961f; n5 (17, 4); Oink exit 0, solution verified.
  - kc18_n24.pg b0d34a312fc9fb2fc2c62a72dcf2b9dd55c30417; n5 (23, 1); Oink exit 0, solution verified.
- Budget: about 1 h per mode, not the 2 h the Lead allowed. The climbs plateaued at the bounds within 15-40 min, so I stopped.

## 4. READING (adversarial, of the proofs I could attack)
- FRZ-U (L-SI §3). The final step needs every state's route π_x to be a simple path inside R with ≤ |R| − 1 edges, which holds because R
  is constant. It also needs κ to be monotone, which follows from WM, Fact A and (C1). Given Claim P^c, the index |R| − 1 cannot be
  beaten, and frzu_tight_n14 shows it is attained. I found no gap in Case B2 / B3.
- CW-INT / CW. Over an interval with no kind change and no kind-B switch, the Ξ-values of kind-B vertices and of o are fixed. The
  reasons: routes are unchanged and θ is constant; and under ¬H1 a kind-B route misses C_Θ, as both notes show. Every c_w switch is
  Ξ-strict at a gate target. So there are ≤ deg(c_w) − 1 switches, tight in cw11_n24. No gap.
- DIR / KIND-MONO. Both rest on H-PATH, which holds at every checked state, and on ABOVE-h equality above c_w. In DIR it comes from
  W-flatness; in KIND-MONO from FRZ-U. With PAR, P = A, and every observed kind change goes B → A. A change A → B at a W-flat or
  post-freeze transition would kill them. None occurs, and the post-freeze regime is never reached.
- CASC-B. Both notes transfer R26 (c) step 2 to sub-runs where c_w and kind-A vertices may switch. L-SI lists this as its own weak
  point 3: A1 can change between steps, and with it the TB-even prefix. I could not test it, because a kind-B switch at a W-flat,
  kind-stable U3 / U23 transition never occurred (§0). This is the least-tested lemma of the two notes, and it is the one I would
  ask the referees to read first.
- PAR is a 3-line consequence of R21 XW. Data agrees.

## 5. Dead ends of this box (each with its obstruction and instance)
- Late freeze at small |R| (frzu climb): the margin stops at 0 (frzu_tight_n14, |R| = 3). Obstruction: every route is a simple path
  of ≤ |R| − 1 edges inside the constant R, so the induction of Claim P^c caps the change index at |R| − 1.
- Many c_w-switches in one interval (cw climb): capped at deg(c_w) − 1 (cw11_n24). Obstruction: kind-B Ξ-values are fixed between
  kind-B moves, and each c_w-switch is Ξ-strict.
- Climbs into CASC-B and post-freeze KIND-MONO: the regime is never entered from S3 (4.6 M evaluations).

## 6. Open (for the Lead to route)
- CASC-B's TB-even prefix under A1 re-routing: either a construction that enters the regime (a W-flat, kind-stable U3 transition with
  a kind-B switch), or a referee reading.
- A post-freeze kind change (KIND-MONO / DIR content): no instance from any search.

## 7. Addendum (22:52Z-23:32Z, date -u; Lead 21:46Z items 2 and 5)
- Theorem RUN (L-SI §6): the max over fallback-free runs of (Ξ-changes on R) / (Δ·|R|⁴) is:
  - 0.0011 on lib41 (S3; longest run 40, max 40 Ξ-changing transitions);
  - 0.0123 on 2,879,100 more random runs (seed 45, n 6-18, S3 + 3 random starts).
  - Against |R|²: 0.16 (lib41), 0.22 (random); a climb on this ratio (kw_n24 seed, 52,040 evaluations to its best) reached 0.11.
  - Far below the bound. Since L-SI's LEN gives ≤ (r − 1)² in the m* = c_θ case, the r² ratio is the sharper probe.
- That random run (seed 45): 0 FAIL. It also reached three bounds and regimes:
  - FRZ-U margin 0, the bound attained again (from S3 or a start pair);
  - CW-INT margin 0;
  - the CASC-B regime, ONCE: 1 kind-B switch at a W-flat, kind-stable U3 / U23 transition, with slack −2 (step index = |π_v| − 4).
    So §0's "CASC-B never reached" holds for lib41 and the first random run only. Not pinned: the saver keeps failures only.
- KIND-MONO (post-freeze), with a climb on the longest post-freeze part of a U3 / U23 c_w ≻ c_θ run:
  - from kc18_n24: post-freeze parts up to 17 transitions, 0 kind changes there (344,652 evaluations);
  - from kt6_n58: no U3 / U23 c_w ≻ c_θ run (580,029 evaluations).
  - From kchain4 (the first km climb): no such run either.
  So the post-freeze kind-change regime stays VACUOUS, even with long post-freeze runs present.
- PAR: 838,491 more states with c_w ≻ c_θ, all with c_w even.

## 8. Addendum (23:40Z, date -u; Lead 23:22Z): REFEREE 11's CASC-B witness
- kw18.py on docs/referee/scratch/kw_logs/cascb_witness.pg (sha1 3bda89ced249b28823a3c275eec5d01a18d502e9), SPEC S3:
  - CASCB_switches 1 with slack −1. The kind-B switch happens at step 0 of its W-flat, kind-stable run, against the bound |π_v| − 2.
  - Stretch type U23. c_θ = o (θ = (2, ∅, 0)). w = (14, ∅, 2), so c_w = 14, which is even and above c_θ.
  - DIR_wflat 1, 0 FAIL.
  - So my checker SEES the regime. This is case (a): R73 §0's "0 everywhere" is a statement about my corpus and climbs, and those never
    reached it. lib41 does not contain this file.
  - The U3x filter is "¬H2, c_w ≠ o, rank(c_w) > rank(c_θ)"; it does not exclude c_θ = o.
- Rows that change: none. §0's wording "0 everywhere" is corrected to "0 in lib41, the first random run and the climbs". §7 already
  reports one occurrence in the second random run (slack −2), and this file is a second, at slack −1. CASC-B is tested on these two
  instances and holds on both.
