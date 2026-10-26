# L-SI notebook (strategy-improvement design loop toward M4 / M4-R)
Overwrite the top sections; append to "Sources opened" and "Dead ends". Lane brief: Lead 2026-10-15 10:10Z, 12 h box to 22:10Z.

## Resume point (successor 11, box 16; GO 02:21Z 2026-10-26 (Lead); session_01FchPxfEZ9Fo56WrCZTvnXS)
- Handover check 5/5 (Lead 02:21Z): docs/agents/handover-checks/L-SI.md succ. 11 section, l-si d272652a. R51 (P-N5-1O) LANDED, trunk 249ad7e3.
- FROZEN (sha1 sent to Lead 02:29Z): docs/si/P-N5-FX-fixes-box14.md 4253d51e (l-si cfadaee9). Both §Cs (referee 9f736349, referee-2
  253fe5c5) were read from the referee branches; they were not on trunk 249ad7e3.
- FROZEN at the Lead's freeze word 03:2xZ (R54 landed, trunk e54d8a48): docs/si/P-N5-1E-box16.md (sha1 and commit in the Lead message;
  R54 quotes re-checked verbatim by script against RESULTS). Before: draft de8775a2, Lead's checks 53b5fd73.
  - Lemma OUT-G: every game; Iσ = ∅ ⇒ S5 correct; premise (VJ) = VJ00 (11), opened by me; R36 (c). Iτ not used.
  - Lemma BIT-G: R51 (c) class audit.
  - Theorem 1E-POLY: ITER ≤ (n(n−1)+d_e)(T*(n,m,Δ,d_e)+1) = O(mΔd_e n¹³) ⊆ O(n¹⁷), via MIRROR (a)-(c) and R51 step 3.
  - Corollary 1E-TIME.
  - §6 READING: OUT-G would close R15's G-N5T-3 on every game.
- DATA: experiments/si/out16/ (outcheck.py, README, logs): 7,824 runs, 0 violations; MUT control fails (773/1,000).
- Things only I know:
  - Lemma DUAL's SECOND sentence (DUAL-1) is not used; only the first sentence and MIRROR (a)-(c).
  - The parameter form of 1E-POLY re-runs MIRROR (b), (c)'s per-game proofs with L := T*(n, m, Δ, d_e). The uniform form is MIRROR as signed.
  - (VJ) for ANY pointwise-optimal σ̄: Θσσ̄′ = Ωσ, so S1's tie-breaks do not matter.
- 03:38Z Lead: P-N5-1E pinned trunk 7fef9699 (REFEREE-2 now; REFEREE succ. 12 later). Fixes file only on the Lead's word, after both.
- 03:38Z Lead task: 𝒞^2O, is ρ per phase polynomial? Lane note docs/si/N5-2O-box16.md (NOT frozen):
  - PROVED (unrefereed; conditional on FBRED): PFZ-q (κ-PFZ needs only its own terminal constant), ROUTE-2, DIR, SAT-2,
    Theorem FB-2T (N_late ≤ 12n² under (2T): ≤ 2 terminals per class), Corollary FB-2O (f ≤ 1 + (n−1)(1+12n²) on 𝒞^2O).
  - ρ itself: OPEN; it is not needed for f.
  - Still OPEN for 𝒞^2O polynomial: X and T per phase (R50 (h) analogue).
  - DATA experiments/si/fb2o/ (fb2o.py arithmetic κ; climb2o.py; lib2o.txt = 43 repo games with exactly 2 Odd choice vertices).
- Things only I know (box 16):
  - The lemmas' κ sums are ARITHMETIC: a vertex on the path and in P(Ξ(q)) counts twice. A checker composing values by set union
    (S1's ⊕) reports false PFZ violations (60 on fts_best24.pg).
  - FBRED HAT-FREEZE (c)'s wording is "play avoids Q∖{c}"; DIR uses only the prefix to c, via (a) plus (SP′).
- NEXT: P-N5-1E fixes on the Lead's word; the 𝒞^2O T-per-phase question (R50 analogue) if the Lead routes it.

## HANDOVER (successor 10, box 15; written 2026-10-26 01:05Z (date -u); session_01PBqfsNWMhTPn7yNJ8C18HP)
Reason: context past the Lead's ~450k line. The session's remaining-token figure fell by ~575k since the start (it is not exposed directly).
Lead: session_014FBi6o334DvwT5Uw2kDfoN.
### DONE (every sha1 below went to the Lead, so these files are FROZEN; new text goes in NEW files)
- Handover check 5/5: l-si ffc341ca.
- docs/si/N5-KW-box15.md 5ebbb3b6 (lane note).
- docs/si/P-N5-PHI-fixes-box14.md 29936b3d. P-N5-PHI LANDED as R47.
- docs/si/P-N5-KW-box15.md c0b0111f, with addendum 8d6bfb3c (K units) and fixes c65f4c1e. LANDED as R50, trunk f41fcf0a.
- docs/si/P-N5-NEEDB-fixes-box13.md 0e5f24af. NEEDB LANDED as R49.
- docs/si/P-N5-1O-box15.md 2cf5e672 (l-si 058e5aee). PINNED at trunk 291c110d; both referees, top priority.
  - Theorem 1O-POLY (any start pair; audit R-N5-START 4e440bd5).
  - Lemma BIT (SPEC sections only).
  - Lemma OUT (closes G-N5T-3 on 𝒞^1O from R36 (c) + R21 (a)).
  - Corollary 1O-TIME.
- DEAD box 15: "in scope, THR ⇒ M ≥ 0" is FALSE on block_9501 from its saved start. Own repro: experiments/si/needb5/. The S3 form is
  kept only as a WEAK conjecture. Ledger line: docs/si/N5-LEDGER-update-box15.md.
- DATA:
  - experiments/si/kw15/ (kwcheck, kwclimb, logs);
  - experiments/si/itergrowth/ (README: N5 iterations on 𝒞^1O, max 115 at n 48, exponent ≈ 1.2 adversarial, ≈ 0.5 random).
- Not frozen, sha1 not sent: docs/si/N5-FRONTIER-box15.md (l-si 0bd6fb23).
  - PAR_D and Lemma CR-D: R20 CR on any game under (i) COARSE_L Ξ = W and (ii) a constant W cycle-node map.
  - Corollary CR-D′: under (h_D), (h3_D), via L-NEW 22's G_D.
  - The first failing link of the KW chain is LEN (Δ-RT).
  - CONJECTURE TC-SWITCH.
### IN FLIGHT
- Nothing running.
### NEEDS
- P-N5-1O SIGNED by both; fixes docs/si/P-N5-1O-fixes-box15.md FROZEN 647deab5 (l-si 90f93566, 01:35Z). RESULTS R51 follows (Lead).
- Lead: FX fixes after REFEREE-2 13's FX report and both §Cs. REFEREE signed FX at 843ba1f8, notes FX-N1..N3. File:
  docs/si/P-N5-FX-fixes-box14.md (NEW).
### Things only I know
- Lemma OUT's two referee checks:
  - R21 (a)'s parenthetical must cover EVERY positional τ′, not only τ_k. Its source P-N5-X proves XW through VJ00 (11).
  - Whether R21 (a) uses 𝒞^1O. If not, S5 is correct on every game.
- P-N5-1O §1's table quotes R50 (h) verbatim, and the start-free audit caveat (R32/R33 at structure level) is quoted twice.
- The KW proof's core is FRZ-U Case B (coarse-strict ⇒ gate by Fact B, then (F1)); cycles are excluded because w is constant. CR-D
  generalises exactly this.
- Traps this box:
  - `until ! pgrep -f X` matches its own shell. Use `while kill -0 PID`, or ps | grep -v grep.
  - Lead messages crossed my freezes twice: the K-unit note became an addendum, and PHI was already done. ReadNotifications before freezing.
  - The kwcheck freeze-delay maximum is over runs that reach k0 + r − 1 only (KW-N5).
### NEXT (for a successor)
1. P-N5-1O fixes when the reports land.
2. FX fixes.
3. Frontier (Lead's optional item 3): data on terminal changes per run (TC-SWITCH) on L-NEW 22's frontier instances and lib41's frontier
   games; then try the ≼_D order on D_k (N5-FRONTIER §4).

## Resume point (successor 10, box 15; GO 19:23Z 2026-10-25 (Lead); session_01PBqfsNWMhTPn7yNJ8C18HP)
- Handover check 5/5 (Lead 19:23Z): docs/agents/handover-checks/L-SI.md succ. 10 section, l-si ffc341ca.
- Box 15 items (Lead 19:23Z): (0) NEEDB fixes on arrival (wait for R2-N5-NEEDB + both §Cs; Lead relays SHAs; NEW file
  docs/si/P-N5-NEEDB-fixes-box13.md with REFEREE NEEDB-N1..N4, R71 INTO wording (Iσ_t ≠ ∅), REFEREE-2's items). (1) MAIN: K = (E) + (K_W).
  L-NEW succ. 21 attacks K via κ / Bellman-Ford (κ-FREEZE-F S4a length obstruction); I attack from the W side; write-ups in docs/si/.
- Work: docs/si/N5-KW-box15.md (lane note). PROVED (L-SI 10, unrefereed): W-ONCE (any game), FRZ-U (κ-freeze above m* on EVERY
  stretch), LEN, KIND-MONO, CASC-B, CW-INT, Theorem RUN (Ξ-changes on R per fallback-free run of a stretch O(Δ r⁴)), Corollary PHASE
  (T per phase poly given f). So (K_W), (E), K closed per stretch; assembly READING: N5 on 𝒞^1O poly IF FBPOLY + PHI + this note are signed.
- FROZEN (sha1 sent to Lead): docs/si/N5-KW-box15.md 5ebbb3b6 (l-si 2685ea67, 20:51Z); docs/si/P-N5-PHI-fixes-box14.md 29936b3d
  (l-si dfa14399, 20:59Z); docs/si/P-N5-KW-box15.md c0b0111f (l-si bf1ed0f7, 21:46Z; packet, Lead GO 21:22Z); docs/si/P-N5-KW-addendum-box15.md 8d6bfb3c (l-si 47c4e7a2, 21:55Z; K units); docs/si/P-N5-NEEDB-fixes-box13.md 0e5f24af (l-si 863ca636, 22:57Z).
- DONE 22:57Z: DEAD box 15 ("THR ⇒ M ≥ 0" FALSE, block_9501 saved start; repro experiments/si/needb5/); ledger line docs/si/N5-LEDGER-update-box15.md. P-N5-KW pinned trunk d9291be0, with REFEREE 11 + REFEREE-2 12. New text goes in NEW files.
- 23:41Z: P-N5-KW SIGNED by both (REFEREE 56ac6538 + Add. 1d6cbf32, KW-1 one-line gap; REFEREE-2 8a47fd92). DRAFTS at l-si f4cb4bc3 (not
  frozen): docs/si/P-N5-KW-fixes-box15.md (freeze on Lead go after both §Cs; add §C items), docs/si/P-N5-1O-box15.md (assembly packet;
  freeze after Lead says R50 landed; replace 'R50' wording with the landed entry text).
- 00:12Z: docs/si/P-N5-KW-fixes-box15.md FROZEN c65f4c1e (l-si 1d33a337). R50 (P-N5-KW) and R49 (NEEDB) LANDED at trunk f41fcf0a.
- 00:49Z: docs/si/P-N5-1O-box15.md FROZEN 2cf5e672 (l-si 058e5aee): Theorem 1O-POLY (any start; audit R-N5-START 4e440bd5), Lemma BIT,
  Lemma OUT (closes G-N5T-3 on 𝒞^1O from R36 (c) + R21 (a)), Corollary 1O-TIME. Sent to Lead for pin/route.
- NEXT: P-N5-1O referee items → NEW docs/si/P-N5-1O-fixes-box15.md. FX fixes when routed. FX fixes (REFEREE signed R-N5-FX 843ba1f8; REFEREE-2 next) → NEW docs/si/P-N5-FX-fixes-box14.md.
- DATA: experiments/si/kw15/kwcheck.py (library + extras), kwclimb.py (random, climbs kind / wonce / long); logs in kw15/logs/.

## Cross-read of L-NEW 21's docs/new/N5-KW-box42.md (v3, l-new b9ee6918, on trunk) against my N5-KW-box15 (5ebbb3b6); written 21:01Z (date -u)
Lead request 20:49Z item (2). Adversarial read: each step re-derived; READING labels mine. The two notes were written independently
(theirs started 20:05Z by their stamp; my W-ONCE / FRZ-U were drafted 19:35-20:30Z, pushed in 823b8773 at ~20:15Z).
### (a) Lemma by lemma
| theirs | mine | verdict (L-SI 10) |
| --- | --- | --- |
| §1 WLAG | §2 W-ONCE | RELY. Steps 2-4 checked. WLAG is slightly stronger (it names z ∉ H_{k−1}(y) with Ξ_k(z) ▷ Ξ_{k−1}(z)); W-ONCE is its contrapositive with "Ξ-flat". Same arena-shrink idea. |
| §2 ABOVE-h | §3 Fact A | RELY. Same case analysis. The honest ¬H1 case rests on "c_θ's σ-route is C_Ξ's return arc" (Odd vertices but o forced); c_θ = o falls under ¬H1 with K_Ξ = ∅, consistent with mine. |
| §2 CSTRICT | §3 Fact B | RELY (theirs restricts to successors of one x; that is all P^c needs). |
| §3 KW-FREEZE (a) | §3 FRZ-U | RELY, with one wording point. Their paths end at the first W-terminal (o or c_w); mine end at o only. Both work. In their B1 "x on C_W, (β) main case": under COARSE_h-strictness (β) cannot occur, since σ(x) on C_W has an empty path set above h, so coarse-strict forces (α). So (β) is vacuous, not "the main case". Harmless. Mine writes B2 / B3 out explicitly; a referee may use either. |
| §3 (b), (c) | §4 LEN, §7 (K_W) | RELY. Same counts (theirs < 2n per vertex, mine r − 2). (b)'s c_θ ≻ c_w branch is WLAG + (c) + F1°, as mine. |
| §3 (d) (c_w ≻ c_θ, c_w odd: TB-odd lowers σ(y)'s index at W-flat switches) | not in mine | RELY. TB (R24 (b)) applies: y ≠ c_w, W cycle node c_w odd, S4a without fallback. A nice shortcut; my E-SEG covers both parities without it. |
| §4 Corollary KW per phase | §7 | RELY per stretch. The per-phase line cites #stretches ≤ n²(2X + 2 + f^O) from P-N5-NH-box42 STR-COUNT (IN REVIEW). Mine counts stretches by landed results only: N_st ≤ 1 + X + Θ + W_ch (R27 (g) TH; R24 (e) WC; H2: w = o ⊕ Ξ(τ(o)) and F1°). |
| §5 H-PATH | §5 KIND-MONO step 1 | RELY. |
| §5 DIR (no change away from P at W-flat transitions) | §5 KIND-MONO (≤ 1 kind change per vertex post-freeze, any transition) | RELY on both. They are different proofs. DIR needs W-flatness and no freeze. KIND-MONO needs the freeze and no W-flatness. DIR step 2's cancellation of "⊕ x" is fine also when x is below c_w (only lengths move). |
| §5 KC | — | RELY (counting from DIR). |
| §5 CASC-B | §5 CASC-B | RELY: same lemma, same justification. |
| §5 CW | §5 CW-INT | RELY: same lemma (theirs adds f_S for fallback switches of c_w, correct). |
| §5 E-HI | §5 E-SEG | RELY. |
| §6 assembly via Theorem NH (P-N5-NH-box42, IN REVIEW) | §8 Corollary PHASE via Theorem LP (R27 (d), LANDED) + (SG) + F1° | Both READINGs are correct as far as I checked. Mine needs no in-review packet besides FBPOLY (f), and FX is not needed either (X from R30 (c) given f). |
- Doubts with an exact step: none of substance. Only (i) the (β) wording in KW-FREEZE (a) B1, and (ii) the in-review dependency of their
  per-phase assembly (STR-COUNT / Theorem NH), which my LP route avoids.
- Data: theirs exercise kind changes (820 kind-change transitions, 6 c_w switches on evstress) where mine were vacuous. The c_w odd
  branch is unexercised in both.
  - My kwcheck on their 10 qualifying games × 150 random starts (experiments/si/kw15/logs/qual10_r150.txt, list qual10.lst):
    - 1,510 traces, 313 runs with c_w ≻ c_θ under ¬H2, 0 failures.
    - Only 18 of those runs reach the freeze point (most are shorter than |R| − 1), and 0 post-freeze kind changes or c_w switches.
    - So their kind changes happen BEFORE my freeze index. DIR covers them; KIND-MONO is vacuous there. That is no contradiction:
      KIND-MONO claims nothing before the freeze.
### Addendum for v3.2 (l-new 31776c5c, sha1 349d553c checked with git show | sha1sum); written 21:10Z (date -u), Lead 21:00Z
- Lemma PAR (c_w ≻ c_θ ⇒ c_w even): RELY. Re-derived: R21 (a) XW gives θ ⊴ w. The cycle nodes differ, so reward(c_θ) < reward(c_w)
  (rewards are injective). An odd c_w ranked above c_θ has reward below c_θ's for either parity of c_θ.
  - Effect on my §5:
    - KIND-MONO: the direction is always B → A. The "A → B if Ω(c_w) is odd" clause is vacuous.
    - CW-INT and CASC-B: parity-free, so unaffected.
    - E-SEG: unaffected.
    - kwcheck's "KIND FAIL direction" odd branch and kwclimb's kind3 odd-c_w terms are vacuous; that is consistent with 0 odd cases in
      all data.
  - Effect on theirs: KW-FREEZE (d) and DIR's odd branch are vacuous (they say so).
- Their Lemma CW correction (cc2de675): correct. My CW-INT already has the corrected shape. Its cut transitions include those with a
  kind change or a kind-B switch, and c_w switches AT cuts are counted separately (E-SEG: E_cw ≤ N_cut + (deg − 1)(N_cut + 1)).
  W-flat segments contain no fallback, so no f term is needed there.
- Freeze index: CONSISTENT. Both are CR's closing step over simple admissible paths. Their paths lie inside R as well, so ≤ |R| − 1
  edges; their n − 1 is the weaker but valid index (|R| ≤ n). Mine states |R| − 1. Data: the largest observed delay is 1 transition
  (mine), 0.83·(n − 1) (theirs), both within either index.
- DATA (21:37Z): 4 seeded kind3 climbs (30 min each, from u3ev_n16, nr_u23_n32, u23sw64_n32, oc16_s2; logs/climb_kind3_154*.txt):
  ≈ 4.5M AGREE states, ≈ 2.1M freeze checks, 248k post-freeze KIND runs, 0 failures. Again 0 post-freeze kind changes or c_w switches.
  OBSERVATION (DATA, not proved): kind changes happen only before the freeze index. Not needed for any bound.
### (b) Do the two notes together close K on U1 / U2 / U3 / U23?
- Yes, per stretch, given f (READING; both lane-proved, unrefereed):
  - U1: R24 Theorem U1 (landed), or FRZ-U + LEN-W + CASC;
  - U2: CASC-U2 (landed) + KW / LEN-W;
  - U3 / U23 with c_θ ⪰ c_w: LEN-Ξ / KW-FREEZE (c);
  - U3 / U23 with c_w ≻ c_θ: E-SEG / E-HI (+ R26 (d)).
- K itself ≤ T_rel, which Corollary PHASE bounds.
- Left (all outside both notes):
  - f per phase: P-N5-FBPOLY in review; FB-PHASE is the second, lane-only proof;
  - phases: P-N5-PHI, signed by both, fixes 29936b3d;
  - referee signatures on the KW lemmas and on one assembly.
  - Nothing left inside a stretch.
### (c) Which packet first
- Recommendation (READING): ONE packet built from L-NEW's §1-§5 (P-N5-KW).
  - It has the exercised data (kind changes, c_w switches).
  - It has the c_w-odd TB shortcut.
- My N5-KW-box15 goes with it as the independent second proof (as FB-PHASE did for FB-POLY), for a referee's cross-check of the freeze
  (B2 / B3 written out) and of KIND-MONO vs DIR.
- My §8 Corollary PHASE (Theorem LP route, landed premises + FBPOLY only) as a short second packet, or as an appendix to theirs. It
  makes the per-phase assembly independent of P-N5-NH-box42.
- If the Lead prefers mine first: it is frozen (5ebbb3b6) and self-contained except for R26 (c) (ii), (iii).

## HANDOVER (successor 9, box 14; written 2026-10-25 19:05Z (date -u); session_018jN1MJkw56F58G3qcfcuZA)
Reason: the session token counter is at ~430k (15M budget, ~14.59M left), near the Lead's ~450k line, at a natural pause after the Lead's
items (c), (a) and (b). Lead: session_014FBi6o334DvwT5Uw2kDfoN.
### DONE (every sha1 below went to the Lead, so these files are FROZEN; new text goes in NEW files)
- Handover check 5/5: docs/agents/handover-checks/L-SI.md (succ. 9 section), l-si 6918233d.
- docs/si/N5-LEDGER-box14.md, c54e8560 (l-si 6195e45f). G-N5-TIME ledger v1 (READING).
- docs/si/N5-FBPHASE-box14.md, f7aaa624 (l-si 858c7dd5). PROVED (L-SI 9):
  - Theorem FB-PHASE: in-phase fallbacks per phase ≤ 2n², no X term;
  - Corollary FX: X ≤ n(f + X_SN) + n − 1 per phase;
  - READING T-K.
  - It is a SECOND proof: L-NEW 20's FB-POLY (docs/new/N5-FBPOLY-box41.md, 7a7087f7) came first, at 18:37Z, with a better constant.
    FB-PHASE §8 corrects ledger v1 §4 1 (b): level −1 F → R̄ gates at EQ (h) states exist.
- docs/si/P-N5-PHI-box14.md, 35e79ec1 (l-si af3a3b5a). Packet, at the Lead's request.
  - Lemma Φ: λ rewards only rise; ≤ n(n − 1) λ-changes and ≤ n(n − 1) λ^U-changes; ≤ 2n(n − 1) + 1 joint λ-runs.
  - Corollary Φ-1O: τ-changes ≤ d − 1; #phases ≤ n(n − 1) + d.
  - From LANDED R15 (a), (c), (d), R18 (d) Lemma S (b), R38 KEY. DATA: experiments/si/phi14 (0 failures).
- docs/si/N5-LEDGER-v2-box14.md, 8ab27359 (l-si 7f76709c). Ledger v2 (READING):
  - with f bounded, X closes (t_Q ≤ T per phase, no X);
  - TH gives θ; SCOPE-COUNT is polynomial;
  - K (wakes at U2 / U3 / U23 states: (K_W), (E)) is the SINGLE open count on 𝒞^1O;
  - "S4a steps" are not a separate link (Theorem LP).
- DATA scripts: experiments/si/fb14/hfb.py (switch classes at in-phase fallbacks), fbphase.py (FB-PHASE ingredients), logs in
  experiments/si/fb14/logs/. All OK. The post-freeze hypotheses are thin.
### IN FLIGHT
- Nothing running.
### NEEDS
- None from the owner.
- Lead:
  - route P-N5-PHI (35e79ec1) to both referees;
  - decide whether FB-PHASE goes to the referees as a cross-check of P-N5-FBPOLY;
  - (0) of box 14 is still pending: the P-N5-NEEDB fixes file once both referees report, with L-RED R71's INTO wording note (restrict
    INTO to Iσ_t ≠ ∅ or to fallback states). It goes to a NEW file docs/si/P-N5-NEEDB-fixes-box13.md.
### Things only I know
- FB-PHASE's key step compares v's κ with ITSELF across a fallback: (SG) is strict, and the freeze makes κ constant. No path
  concatenation, so N5-FBCAP-route's "cycle case" never arises.
  - Route changes inside R̄ are frozen by the θ-run freeze, because terminal o carries κ(θ).
  - λ-classes without o freeze over the whole phase, with the single terminal c.
- θ-SET: after g_{|U|−2}, at H1 states θ = o ⊕ (frozen optimum at σ̄(o)) with σ̄(o) ∈ F (H1 + (HP)); at ¬H1 states P(θ) = ∅. So θ takes
  ≤ d_o + n − 1 values there.
- Wakes cannot occur at (h) states: Lemma WAKE + BAND need c_θ ≠ c_w. They live at Q states (U1 pieces, now polynomial) and at
  ¬H1 / HN states (U2 / U3, open).
- K attack idea (ledger v2 §3): a W-round at S4a steps under ¬H2, with arena-entry (wake) charging to θ-changes or to earlier route
  changes. Also an L-MONO analogue for c_w (unproved), for the c_w switches in (E).
- REFEREE-2's tracer: docs/referee-2/R2-N5-OUT/out_check.py run_trace(g, o, s, t, rng, "spec"). State fields: Xi, W, theta, w, fh, sg,
  tu, Rbar, Rr, F, H1, H2, H3, hh, r, gates, Is. g.key(x) orders valuations; OC.reward(g, c).
- hfb.py prints "fb − (|U| − 2)" up to 2. That comes from |U| ≤ 2 phases (max(1, ·)) and is NOT an FB-CAP violation; checked with U at
  phase start, 0 violations.
- Traps (box 14):
  - I once wrote an estimated header time and fixed it before the push. Stamp from date -u in the same command.
  - Lead messages crossed twice: FB-POLY arrived while I proved FB-PHASE. Read notifications before starting a proof.
### NEXT (for a successor)
1. Referee items on P-N5-PHI → a NEW fixes file.
2. NEEDB fixes (above).
3. K, if the Lead routes it: start at HN states (U3). There BF-F gives the F-side rounds and SPLIT makes R monotone between evictions.
4. (Lead 18:57Z, item (3)) What is left of R26's reading "(NH') ⇐ (X), NFB-O, (E), (K_W)", now that X is bounded (P-N5-FX, given
   FB-POLY):
   - (X): closed by P-N5-FX, CONDITIONAL on P-N5-FBPOLY.
   - NFB-O (fallbacks at OTHER states): closed. FB-POLY bounds every in-phase fallback, OTHER states included (CONDITIONAL on
     P-N5-FBPOLY).
   - LEFT: (E), events per W-flat run of U3 / U23 stretches (kind changes of R-vertices and switches of c_w); an L-MONO analogue for c_w
     would bound the c_w switches. And (K_W), non-fallback W-changes on R in U2 / U3 / U23 stretches.
   - These two are exactly what K (wakes) needs outside route form. Route-form wakes are at Q states (U1 pieces, R24 (d)) and are
     polynomial given f and X.
- Box 14 sha1s also include docs/si/P-N5-FX-box14.md (packet; sha1 in the Lead message of 19:1xZ). FB-PHASE is NOT to be packeted
  (Lead 18:57Z): it is a lane cross-check of P-N5-FBPOLY.

## HANDOVER (successor 8, box 13; written 2026-10-25 18:04Z (date -u); session_013kZp65x9TKU9AqPZdMYGpm)
Reason: session token counter at ~390k used (15M budget, ~14.61M left) after the Lead's "climb report, then hand over" (17:55Z), at a
natural pause. Lead: session_014FBi6o334DvwT5Uw2kDfoN.
### DONE (every sha1 below went to the Lead, so these files are FROZEN; new text goes in NEW files)
- docs/si/P-N5-LV-fixes-box11.md, b75ab1fc (l-si 6480a0f0). RESULTS R41 (P-N5-LV) LANDED d0cc0ab.
- docs/si/P-N5-LV2-fixes-box12.md, f76fd1d1 (l-si 680c0294). REFEREE b454ca3 + Add. 46a8030 + §C ed8bc207; REFEREE-2 a551deb.
- Packet docs/si/P-N5-NEEDB-box13.md, 7471aef3 (l-si 3ea0f5f9). Contents:
  - XG, ANTI, NEED-β (all cases, A2* by me);
  - OLD-THREAT;
  - the reduction INTO ⇒ no case (i) fallback.
  - Not routed to referees yet at handover.
- Lane write-ups: docs/si/N5-RISE-box13.md (3b8fea13), docs/si/N5-A2STAR-box13.md (2a85601d). docs/si/DEAD.md box-13 entries:
  - RISE-DROP: tevlast7_n32;
  - GATE-ABOVE: rise_thin51_n40;
  - FEED: tevlast11_n40;
  - NONE-LAST / M = −1-last: beta2_n11, L-RED 16's.
- Handover check 5/5: docs/agents/handover-checks/L-SI.md (succ. 8 section).
- Scripts in experiments/si/lv13/:
  - none_count.py, none_climb.py (v2 fitness);
  - oldthreat.py (OLD-THREAT, GATE-ABOVE, FEED, INTO counters);
  - rise_climb.py, rise_show.py, a2star.py.
  - Logs in experiments/si/lv13/logs/.
- Item (1) DATA (LV-NONE / SCOPE-FB from REFEREE-2's start pairs):
  - 8 climbs (1301-1304 v1, 1501-1504 v2): 0 failures, max 1 u* = none fallback per scope run;
  - v2 1501/1502: 347,110 u* = none fallbacks, 346,653 later in-scope transitions, 0 fallbacks after one;
  - beta2_n11 (L-RED, hand-built) has 2 in one scope run (none_count: max 2 vs bound 67; log logs/none_beta2.txt). My climbs never found
    that shape.
### IN FLIGHT
- Nothing running (no background jobs).
### NEEDS
- None from the owner. Lead: route P-N5-NEEDB (7471aef3) to the referees. Referee items go to a NEW file P-N5-NEEDB-fixes-box13.md.
### Things only I know
- The rise question has two halves.
  - Case (i), r > L up to a later fallback: reduced to CONJECTURE INTO by FBL. INTO says Even always keeps a gate into R̄ after a rise;
    the gates are absorption chains or R → R̄ route improvements.
  - Case (ii), r ≤ L before the next fallback: untouched.
  - L-RED box 41 is attacking both (Lead 17:25Z).
- OLD-THREAT's proof is FZ's proof with the fallback k replaced by any post-rise state t. FZ never uses that k is a fallback. Reuse
  that, whenever a "freeze since k0" is needed at a non-fallback state.
- beta2_n11's mechanism is an eviction cascade: the evicted vertex 5 becomes a (β) target for its R-predecessor 10 at the next state,
  with λ_Ξ and COARSE_{−1}(Ξ) fixed. Any sharpening of LV-NONE must count cascade layers (≤ depth of R), not "one per scope run".
- REFEREE-2's tracer (docs/referee-2/R2-N5-OUT run_trace + R2-N5-FRZ analyse) exposes:
  - S.fh (honest successor; σ̄(o) = S.fh[o]);
  - S.Rbar;
  - S.gates (with levels);
  - S.lamX, S.tu.
  The lv13 scripts import it read-only.
- Traps (box 13):
  - `until ! pgrep -f X` matches its own command line and never exits. Wait with `while kill -0 PID`, and never put `exit` inside a
    while-condition.
  - A multi-line Bash call runs in the shell's current cwd, which can differ from the repo root (environment notes). Use absolute paths
    for every redirect and script.
  - `ls a b | head` cuts listings, so a directory looked empty when it was not.
  - Lead messages cross often. Re-read NOW / notifications before acting on an older ask (A2* was asked after it was already done).
### NEXT (for a successor)
1. Referee items on P-N5-NEEDB → NEW fixes file.
2. Ask the Lead. The candidates:
   - a proof of INTO (case (i));
   - case (ii) of the rise question;
   - a cascade-depth bound for r = −1 fallbacks (sharper LV-NONE);
   - "THR ⇒ M ≥ 0" (its counterexample shape is now pinned by NEED-β: (β) gates on every reply).
   - G-N5-TIME items not this lane's alone: θ_ph, HN stretches for τ(o) ≠ o, OTHER states, REL(S).

## Resume point (successor 8, box 13; GO 15:59Z 2026-10-25 (Lead); session_013kZp65x9TKU9AqPZdMYGpm)
Handover check 5/5 (docs/agents/handover-checks/L-SI.md, 03c69372). Lead box-13 order: (0) LV fixes file; (1) LV-NONE / SCOPE-FB from
REFEREE-2's start pairs; (2) NL= FALSE (L-RED nleq_cex_n48, e72e4034), off the board; (3) "no fallback after a rise" unconditional, else
A2*. Hand over at ~450k, read from the session counter.
- (0) DONE: docs/si/P-N5-LV-fixes-box11.md FROZEN sha1 b75ab1fc (l-si 6480a0f0). The Lead drafted R41 = P-N5-LV from it (CHECKER C50).
- (1) DATA (docs/si/N5-RISE-box13.md §4; experiments/si/lv13/none_count.py, none_climb.py):
  - max 1 u* = none fallback per scope run (131,558 of them in climb 1301), max 17 fallbacks per scope run, 0 failures;
  - CONJECTURE NONE-LAST: an r = −1 THR fallback is the last transition of its scope run;
  - v2 climbs 1501-1504 (gradient: transitions after the none fallback) launched 17:21Z, 40 min; logs logs/climb_150*.txt.
- (3) docs/si/N5-RISE-box13.md (sha1 3b8fea13, reported to the Lead 17:20Z):
  - PROVED Lemma OLD-THREAT, and the reduction "case (i) ⇐ CONJECTURE INTO" via FBL;
  - FALSE: RISE-DROP (tevlast7_n32), GATE-ABOVE (rise_thin51_n40), FEED (tevlast11_n40); recorded in DEAD.md;
  - INTO: 425 / 425 library states. Case (ii) (r ≤ L) OPEN. Asked the Lead to give INTO to L-RED box 41.
- A2*: docs/si/N5-A2STAR-box13.md. PROVED (succ. 8): m′ is odd by (F-a) lengths; then c = m′ or c odd above m′; σ″ then contradicts.
  So NEED-β is complete. DATA: 0 A2* shapes (vacuous).
- Things only I know (box 13):
  - REFEREE-2's tracer (docs/referee-2/R2-N5-OUT out_check.run_trace + FRZ analyse) gives S.fh (honest successor, so σ̄(o) = S.fh[o]),
    S.Rbar, S.gates; my lv13 scripts import it read-only.
  - A watcher `until ! pgrep -f X` matches its own command line and never ends. Wait with `while kill -0 PID`.
  - A Bash call whose cwd moved (environment notes) runs later lines of a multi-line command in the old cwd: use absolute paths.

## HANDOVER (successor 7, box 12; written 2026-10-25 ~15:35Z (date -u); session_01Nosb1KbEcKX2yMZfBES2sA)
Reason: the session token counter passed ~450k (the Lead's handover line), at a natural pause after packet P-N5-LV2.
### DONE (every sha1 below was sent to the Lead, so these files are FROZEN; new text goes in NEW files)
- docs/si/P-N5-ENT-fixes-box11.md (72d052b5, l-si b6b8f85b): both ENT reports and both §Cs, N-ENT-1..3, the R36 lift line. Lead drafting
  R40 from it.
- Packet docs/si/P-N5-LV2-box12.md (3b23a41f, l-si ed936af1), queued behind P-N5-LV. Contents:
  - STALE-GATE (every game); EV-G; ENT-X_{−1}; LV-PL′ (≤ n·n_E + 1 level −1 fallbacks with r ≥ 0 per scope run);
  - SAND; FLAT-ALL_{−1}^{none}; LV-NONE (≤ n·n_E + 1 u* = none fallbacks per scope run);
  - SCOPE-FB (≤ 4·n·n_E + 3 fallbacks per scope run; conditions (C-ENT), (C-LV), (C-PKT)).
- Lane write-ups:
  - docs/si/N5-LV3-box12.md (20ba05d7): XG, ANTI, NEED-β; "THR ⇒ M ≥ 0" obstruction;
  - docs/si/N5-LV4-box12.md (9d1b90f4) and N5-LV5-box12.md (e2cb0703): the sources of P-N5-LV2.
- Handover check 5/5: docs/agents/handover-checks/L-SI.md.
- Scripts in experiments/si/lv/ (betasearch.py, xg.py, probe.py, hand9.py, stale.py, scopefb.py), logs in experiments/si/lv/logs/.
### IN FLIGHT
- Nothing running (no background jobs).
### NEEDS
- None from the owner. Lead: route P-N5-LV2 behind P-N5-LV. Referee items go to NEW files (P-N5-LV2-fixes-box12.md).
### Things only I know
- STALE-GATE is the cheap replacement for every "rank-L bit" argument (ENT-SHAPE (2)-(4)). Any later "z changed since k0" step should use
  it (with FREE-FREEZE for free z).
- At r = −1 nothing needs NL. SAND plus U-loc plus OR kills every COARSE_{−1}(Ξ) change.
- "THR ⇒ M ≥ 0" (N5-LV3) is now only of interest for its own sake. LV-PL′ already counts (β)-fallbacks.
  - Its open case A2*: Even's best reply's cycle runs through o, topped after o, above all of λ ∪ {o}.
  - A first idea, not checked: ANTI-W on that cycle K′ forces a blocked edge on K′, unless m′ = c.
- Random 𝒞^1O games give no in-scope THR fallback. Use the corpus, or perturbed start pairs (betasearch.py corpus mode).
- Traps:
  - `pkill -f <pattern>` with the pattern in the calling command kills the shell (exit 144; it bit me at ~15:22Z). Kill by PID from
    `ps aux | grep "[x]"`.
  - Lead messages arrive only through ReadNotifications. I missed two relays for ~35 min. Call it after every push.
  - The session token counter, not my own estimate, is the context measure. I under-reported (~255k) to the Lead at 15:28Z; corrected
    in the handover message.
  - `git log -- <path>` takes more than 120 s here.
### NEXT (for a successor)
1. Referee items on P-N5-LV2 (and P-N5-LV) → NEW fixes files.
2. Lead 15:34Z (crossed my handover): P-N5-LV2 PINNED at trunk 283bcb6, queued after P-N5-LV. A2* is approved as the next item. If A2*
   stalls within ~45 min, switch to the Lead's D18 suggestion: prove REFEREE-2's DATA observation unconditionally ("after a rise with
   r > L the scope run has no further fallback"; 62 library + 26,665 climb cases). That would make ENT-X independent of EV+ and
   FREE-FREEZE.
3. With CL-S closed up to the reviews (SCOPE-FB), the G-N5-TIME gaps that remain are not this lane's alone: scope runs per phase,
   out-of-scope fallbacks, S4a steps, phases and X. Ask the Lead which one to take.

## Resume point (successor 7, box 12; GO 14:18Z 2026-10-25 (Lead); session_01Nosb1KbEcKX2yMZfBES2sA)
Handover check 5/5 (docs/agents/handover-checks/L-SI.md). Trunk 7fc7ac9 merged (R36, R37, R38 landed). Lead order: (0) P-N5-ENT fixes
file when REFEREE-2 9's R2-N5-ENT SHA is relayed (priority); (1) level −1: (c) exclude a (β)-fallback, else the exact obstruction; then
(b) a length-based ENT-SHAPE to drop REL(S); then (a) u* = none; (2) NL= only if cheap. Box ~3 h or ~450k.
- (c) done as a lane write-up: docs/si/N5-LV3-box12.md. PROVED: Lemma XG, Lemma ANTI (via R36 P1), Corollary NEED-β (cases B, A1, A2′,
  A2″). OPEN: case A2*; "THR ⇒ M ≥ 0" stays CONJECTURE. DATA: 3,936 in-scope THR fallbacks (run + perturbed start pairs), all M ≥ 0.
  Scripts experiments/si/lv/ (betasearch.py, xg.py, probe.py, hand9.py), logs experiments/si/lv/logs/.
- (b) done as a lane write-up: docs/si/N5-LV4-box12.md. PROVED: Lemma STALE-GATE (every game: a gate's target changed its Ξ since the
  last Even fallback), Corollary EV-G (FREE-FREEZE + STALE-GATE), Theorem ENT-X_{−1} and Corollary LV-PL′ (≤ n·n_E + 1 THR fallbacks
  with M = −1, r ≥ 0 per scope run; no REL, no d_o), CONDITIONAL on P-N5-LV §1-§4 (in review). STALE-GATE replaces ENT-SHAPE (4)'s bit.
  DATA: STALE-GATE 72,589 checks, EV-G 39,406, 0 failures (experiments/si/lv/stale.py).
- (a) done as a lane write-up: docs/si/N5-LV5-box12.md. PROVED: Lemma SAND (COARSE_{−1}(θ) frozen once r = −1), FLAT-ALL_{−1}^{none}
  (LV-SHAPE + H1 at k+1 replace FBL), Theorem LV-NONE (≤ n·n_E + 1 u* = none fallbacks per scope run), Corollary SCOPE-FB (≤ 4·n·n_E + 3
  fallbacks per scope run; CONDITIONAL on P-N5-ENT PL-S″, P-N5-LV, N5-LV4).
- (0) DONE: docs/si/P-N5-ENT-fixes-box11.md FROZEN sha1 72d052b5 (l-si b6b8f85b). Lead drafting R40.
- Packet P-N5-LV2 (docs/si/P-N5-LV2-box12.md; Lead GO 15:16Z/15:19Z): LV4 + LV5 in one packet. The one-part draft P-N5-LV4-box12.md
  (79281d48) was never reported; removed in the LV2 commit.
- Things only I know (box 12): random 𝒞^1O games (n ≤ 18) give NO in-scope THR fallback; only the corpus instances do. A THR fallback
  needs (o, x0) ∉ Iτ, i.e. Even's best reply to τ from x0 is at least as good as from t (R37 BL Step 0/1). That is the lever: ANTI-Ξ
  turns "Even's best reply avoids (β) gates" into "U(x0) ⊴ Ξ(x0)", against THR.
  - Trap (bit me again at ~15:22Z): `pkill -f scopefb.py...` killed my own shell (exit 144). Kill by PID from `ps aux | grep "[x]"`.
  - Trap: Lead messages arrive only via ReadNotifications; I missed two relays (14:33Z, 14:46Z) for ~35 min. Call ReadNotifications after
    every push.

## Handover check (successor 6)
Session session_01WZRciyMqz1LNWwdFoeq2AP (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~12:05Z (date -u).
1. Branch claude/l-si. Commands: `git fetch origin`; `git status` showed local head 0d48da2 (the box-0 Fable head), and
   `git rev-list --left-right --count HEAD...origin/claude/l-si` gave 0 / 4179. `git merge --ff-only origin/claude/l-si` then gave
   head 84d11cd (successor 5's handover). `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` gave
   0 ahead / 41 behind trunk 48a8a4c. `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` gave 5c97049 (1 ahead / 0 behind
   before this commit). Trunk is claude/vibrant-johnson-nxvvxo (`git remote show origin` → HEAD branch); there is no `main`.
2. Open work (from successor 5's resume point below, `ls docs/si docs/referee docs/referee-2`, and the trunk log):
   - P-N5-RL (docs/si/P-N5-RL-box10.md, sha1 0a3c70cb; pinned trunk 2fb698d per NOW): in review. REFEREE succ. 8 is WORKING on
     R-N5-RL (NOW roster); no R-N5-RL / R2-N5-RL file exists yet on trunk or on origin/claude/referee(-2). Next step: wait for
     relayed items; they go to a NEW file docs/si/P-N5-RL-fixes-box10.md (does not exist yet).
   - P-N5-P1 (docs/si/P-N5-P1-box10.md, sha1 b98ca794; pinned trunk 48a8a4c "Lead: P-N5-P1 pinned"): unrefereed. Next step: same,
     items to docs/si/P-N5-P1-fixes-box10.md (does not exist yet).
   - TEV / NJB = ENT: CONJECTURE. Next step (box 11 (a)): exclude TEV-RED's configuration (P-N5-RL §6 Consequence), starting with
     the sub-case "e is an evicted tail with target f", or give the exact obstruction and an instance shape for L-RED 16.
   - Successor 5's NEXT 2 (RISE-LAST at levels < L / after r ≤ L) and NEXT 3 (two-player VJ00 Lemma 5.8, R15's G-N5T-3): not started.
   - Nothing running (fresh container).
3. GAPS (docs/GAPS.md row 11, read with python, last part): G-N5-TIME, major, owner L-NEW, OPEN. Update 11:51Z: R35 (P-N5-NJB +
   fixes, fixes2; CHECKER C44) LANDED: RDROP, PL (c′), PL-S′, MINSET (survivor form), NO-RF-OLD, ENT-SHAPE (1)-(4), (5′); literal MINSET
   (c) and ENT-SHAPE (5) NOT signed. "Open: NJB = ENT (CONJECTURE; lane reductions EV/EV+/TEV-RED in review as P-N5-RL), REL(S), level
   −1 fallbacks, out-of-scope fallbacks (P-N5-SCOPE in review; lane NO-ENTRY-A), θ-changes per HN stretch. Lane (unrefereed): Lemma P1
   = (P) for one-player games." L-SI owns no GAPS row.
4. Rulings (docs/DECISIONS.md, verbatim; status from docs/DECISIONS-INDEX.md):
   - D1 (index: active; full text docs/decisions/D001-launch-brief.md). Key lines: "A claimed polynomial algorithm is far more likely
     to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below." and
     "Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision."
   - D16 (index: active): "Then keep working as I told you to"
   - D18 (index: active): "Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from
     areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed,
     state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open
     problems."
5. Traps found:
   - `pkill -f <pattern>` run from a Bash call whose own command line contains <pattern> kills that shell (exit 144). The same
     family as successor 5's pgrep trap. Never pkill by a pattern that is in the calling command.
   - `git log -- <path>` on this repo did not finish within 120 s (big history); read the file itself, or use a bounded
     `git log -n 1 <commit>`.
   - Still live: the fresh clone's local branch is the old box-0 head (4179 behind); fetch + fast-forward before reading notes.

## Handover check (successor 5)
Session session_018GWc3YukyLgRhrrYJdrzHm (Opus 5.5, D15/D18, L37/L40). Written 2026-10-25 ~09:25Z (date -u).
1. Branch claude/l-si. Commands: `git fetch origin`; `git status` (local branch was 3924 behind origin/claude/l-si);
   `git pull --ff-only origin claude/l-si` → head 72ecba6 (= successor 4's handover head); `git rev-list --left-right --count
   HEAD...origin/claude/vibrant-johnson-nxvvxo` → 0 ahead / 94 behind trunk 2edf33e; `git merge-base` → 72ecba6.
   Then `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` → a719414 (1 ahead / 0 behind before this commit).
2. Open work (from the HANDOVER above, `docs/si/`, trunk `docs/referee/R-N5-NJB.md`):
   - P-N5-NJB (docs/si/P-N5-NJB-box9.md, sha1 f43a8823 on both branch and trunk, pinned trunk a7d85b3): FROZEN. REFEREE succ. 7
     report R-N5-NJB.md (trunk) has NJB-1 (MINSET wording) and NJB-2 (ENT-SHAPE (5) not signed; (5′) signed). Next step:
     new file docs/si/P-N5-NJB-fixes-box9.md (does not exist yet). R2-N5-NJB: not on trunk nor on origin/claude/referee-2
     (`git ls-tree -r origin/claude/referee-2 --name-only | grep -i njb` → nothing in docs/referee-2/).
   - NJB = ENT (MINSET form) CONJECTURE: next step a proof or the exact obstruction, using (5′); read L-RED 15 (climbs) and
     L-NEW 15 PF-THETA (docs/new/N5-DROP-box35.md §8) without editing them.
   - Successor 4's NEXT 2: level −1 fallbacks per scope run; REL per scope run. Not started.
   - Nothing running (successor 4: no climbs; scratchpad was session-local).
3. GAPS (trunk docs/GAPS.md, `git show <trunk>:docs/GAPS.md | grep -n G-N5`): G-N5-TIME, major, owner L-NEW, OPEN. Its last
   update (08:50Z): R31 LANDED (P-N5-FBW + fixes, CHECKER C40); "Open: NJB (D_M = 0; = ENT/MINSET, CONJECTURE), REL, level −1
   fallbacks. In review: P-N5-FRZ, P-N5-L2, P-N5-NJB, P-N5-TOG. ONE-DROP, DROP-LEN FALSE." G-N5-TERM closed (R15).
   L-SI owns no GAPS row.
4. Rulings (trunk docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md):
   - D1 (index: active), key lines verbatim: "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every
     such claim, including the fleet's own, as wrong until it passes the gauntlet below." and "Never publish, post, email, submit
     or contact anyone outside the fleet. Anything external is my decision."
   - D16 (index: active): "Then keep working as I told you to"
   - D18 (index: active): "Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from
     areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed,
     state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open
     problems."
5. Trap found: the fresh clone's local claude/l-si was 3924 commits behind origin (an old head 0d48da2 of the Fable session);
   reading notes/L-SI.md before `git fetch` + fast-forward would have given the box-0 handover. Check: `git rev-list --count
   HEAD..origin/claude/l-si` = 0 before reading. Second trap (inherited, still live): successor 4's .git/info/exclude for
   experiments/si/xing/out/ does NOT exist in this container (`cat .git/info/exclude` shows only the template); so never
   `git add -A`, add files by name.

## HANDOVER (successor 6, box 11; written 2026-10-25 ~13:50Z (date -u) at ~440k; session_01WZRciyMqz1LNWwdFoeq2AP)
### DONE (every sha1 below was sent to the Lead, so these files are FROZEN; new text goes in NEW files)
- docs/si/N5-TEV-box11.md (58a0b3cf): lane write-up of ENT-X.
- docs/si/P-N5-RL-fixes-box10.md (ac027458), docs/si/P-N5-RL-fixes2-box10.md (b3e3cd93), docs/si/P-N5-P1-fixes-box10.md (83ef83b0),
  docs/si/P-N5-RL-P1-addendum-box10.md (5c29d93d). Both referees signed CYC-EV + TEV-RED′ in their addenda (Lead 13:13Z). P1 → R36,
  RL → R37 at CHECKER.
- Packet P-N5-ENT docs/si/P-N5-ENT-box11.md (4fd22be7). No (P): FZ, BF, RB, WALK, CYC-EV, TEV-FB. CONDITIONAL on (P) via EV+ only:
  ENT-X, NJB-A, D1 (D_M ≤ 1), PL-S″ (≤ 2·n·n_E fallbacks of level ≥ 0 per scope run). With P1 landed, the condition goes once ENT is
  signed. Status when I left: with REFEREE-2 9 (Lead 13:54Z); no report seen yet.
- docs/si/N5-STR-box11.md (c7b9c671), N5-STR2-box11.md (b6ed9476): straddle obstruction (NL's (K*) at r = L), CONJECTURE NL= (0 failures
  in 743 steps), reading NJB ⇐ (P) ∧ NL=, and an NL= kill shape (passed to L-RED 16 by the Lead). Off the critical path (Lead agrees).
- docs/si/N5-LV-box11.md (407c5520), N5-LV2-box11.md (94ac2469); packet P-N5-LV docs/si/P-N5-LV-box11.md (d0d797f0): LV-SHAPE;
  LV-CN / LV-COUNT (CN-LAST); FLAT-ALL_{−1}, STRETCH_{−1}, PL_{−1}, LV-PL ≤ n·n_E·(d_o + REL(S)). The packet supersedes LV2's "+1".
- Dead ends: TEV, TEV-LAST (docs/si/DEAD.md).
- Scripts: experiments/si/tev/ rb.py, straddle.py, nleq.py, lvm1.py; logs in experiments/si/tev/logs/.
### IN FLIGHT
- Nothing running.
### NEEDS
- None from the owner. Lead: route P-N5-ENT and P-N5-LV to the referees; referee items go to NEW fixes files.
### Things only I know
- The device behind ENT-X: a free vertex that was in R at k0 and whose old successor is back in R̄ at the next fallback cannot see a
  COARSE_L change there (Lemma RB). Otherwise that edge is a gate of level > L, which CLS2 forbids at a fallback. Walking the old route
  to the first R̄ vertex turns this into "B ⊆ A" whenever the walked route is low. At S4a states the same gate is allowed. That is
  exactly why TEV fails at S4a states (tevlast_cex_n40: v = 15, gate (15, 21) of level 33, re-enters R at 8) and holds at fallbacks.
- P-N5-RL's §6 silently assumed the Ev vertex is on the pre-c path. CYC-EV fixes it at t = k only.
- R31's level-≥0 proofs use M ≥ 0 only through "THR with u* ≠ none". That is how the level −1 count came for free. The rank-L bit (STRETCH
  step 2, ENT-SHAPE (4)) is the part that does not transfer; lengths replace it in STRETCH, but nothing replaces it in ENT-SHAPE.
- Traps:
  - `pkill -f <pattern>` kills the calling shell when the pattern is in its own command line;
  - `git log -- <path>` takes > 120 s here;
  - several Lead messages crossed with my files: always check whether a sha1 was already sent before deciding "same file or new
    file".
### Update 14:01Z (date -u)
- P-N5-LV (d0d797f0) PINNED at trunk 601df6e, queued for both referees after P-N5-NEB. Its addendum
  docs/si/P-N5-LV-addendum-box11.md (a15a8871, l-si 84974fe) holds the NL= material as not to sign. The (β) bound is already in packet §4.
- R36 (P-N5-P1) LANDED at 601df6e (CHECKER C45 PASS). (P) is discharged for one-player games. So P-N5-ENT's conditions go away once ENT
  and P-N5-RL (R37) land.
- Trap (mine): the P-N5-LV header stamp "~14:00Z" was ahead of date -u (13:48Z). Stamp headers with `date -u` at writing time, never with
  an estimate.
### NEXT (for a successor; Lead's queue 13:54Z)
1. docs/si/P-N5-ENT-fixes-box11.md (NEW) when REFEREE-2 9 reports on P-N5-ENT (4fd22be7). P-N5-LV fixes (NEW file) when referee items
   arrive.
2. Research: REL(S) at level −1 (a length analogue of ENT-SHAPE), the u* = none THR fallbacks, and NJB / ENT (straddle; NL=).
(older numbering below kept for context)
1. Referee items on P-N5-ENT / P-N5-LV → NEW fixes files.
2. Level −1: (a) u* = none THR fallbacks (r = −1; NL at L = −1 unavailable); (b) a length-based ENT-SHAPE to drop REL(S) at level −1;
   (c) or kill "THR ⇒ M ≥ 0" via a (β)-fallback (P-N5-LV §1/§5).
3. NL= (straddle) only if cheap; it buys a factor 2.

## Resume point (successor 6, box 11; GO 12:12Z 2026-10-25; session_01WZRciyMqz1LNWwdFoeq2AP)
Write-up: docs/si/N5-TEV-box11.md. Code: experiments/si/tev/rb.py (logs/rb_named.txt, logs/rb_lib.txt).
### DONE
- Theorem ENT-X (PROVED CONDITIONAL on (P), only via P-N5-RL EV+): the ENT setting is empty, i.e. TEV-RED's configuration cannot occur.
  The device is Lemma RB + Corollary WALK (unconditional): walk e's k0-route to the first vertex back in R̄_k; the predecessor carries a gate
  of level > L unless the walked part of the route is high; e's route after e is low (TEV-RED (2), re-proved without FREE-FREEZE).
- Lemma CYC-EV (no (P)): in (Σ) after a rise, c's cycle at k has no Ev vertex. This fills the "first/last Ev vertex is on the pre-c path"
  point that P-N5-RL §6 uses silently. If a referee raises it, it goes in P-N5-RL-fixes-box10.md.
- TEV at fallback states: PROVED, no (P). Corollaries (CONDITIONAL on (P)): NJB-A, D1 (D_M ≤ 1 for every block), PL-S″ (≤ 2·n·n_E
  fallbacks of level ≥ 0 per scope run, with no REL(S)).
- DATA: rb.py NAMED 262 pairs / LIB 377 pairs, 0 violations of RB, BF, WALK, CLS2. The ENT setting occurs 0 times (vacuous, as before).
### OPEN
- The straddling interval of a block (r drops to M inside it): full NJB. TEV at S4a states. Level −1 fallbacks.
### Since 12:34Z
- TEV and TEV-LAST are FALSE (L-RED 16: tev_cex_n40, tevlast_cex_n40; Lead re-run). Recorded in docs/si/DEAD.md. They fail at an S4a
  state; the walk's v = 15 carries the gate (15, 21) of level 33 and enters R at 8. TEV at fallback states stands (ENT-X needs only that).
- docs/si/P-N5-RL-fixes-box10.md (REFEREE 8's RL-1..RL-4, TEV dead ends, k0-quantifier point). REFEREE-2's items go to fixes2.
- Next: packet P-N5-ENT (docs/si/P-N5-ENT-box11.md), then the straddling interval.
### Since 12:45Z (all pushed; every sha1 below was sent to the Lead, so the files are FROZEN)
- P-N5-ENT packet 4fd22be7. RL fixes2 b3e3cd93; P1 fixes 83ef83b0; RL/P1 addendum 5c29d93d. Lead 13:13Z: both referees signed CYC-EV +
  TEV-RED′ in addenda; P1 at CHECKER as R36, RL next as R37.
- Straddle: N5-STR-box11 (c7b9c671: obstruction = NL's (K*) at r = L; CONJECTURE NL=, 0 failures in 743 steps; reading NJB ⇐ (P) ∧ NL=),
  N5-STR2-box11 (b6ed9476: bypass gate (p, e*) of level L admissible at r = L; kill shape for L-RED). Off the critical path (Lead agrees).
- Level −1 (Lead GO 13:13Z): docs/si/N5-LV-box11.md. LV-SHAPE (PROVED): an in-scope THR M = −1 fallback has only (α) F→F own-cycle-node
  gates, (γ) F→R̄ at y = c (r = −1 only), or (β) R→F level −1 gates (need rank o < rank c). LV-CN (CONDITIONAL on CN-LAST): no (β) ⇒ the
  fallback is the phase's last transition. DATA: 1,032 THR in scope, all M ≥ 0; 0 with u* = none.
- docs/si/N5-LV2-box11.md (13:50Z): R31's FLAT-ALL uses M ≥ 0 only to get THR u* ≠ none, so it holds at level −1 with r ≥ 0; STRETCH_{−1}
  (PROVED: ≤ n repeats per tail per constant-COARSE_{−1} stretch, lengths). READING LV-PL: level −1 THR fallbacks with r ≥ 0 per scope
  run ≤ n·n_E·(d_o + 1 + REL(S)). OPEN: u* = none fallbacks (r = −1), a length-based ENT-SHAPE (to drop REL at level −1).
### NEXT (for a successor)
0. Turn LV-PL into a packet: re-prove FLAT-ALL / PL (a)-(b) / RDROP / PL (c′) at M = −1 line by line (U-loc at L = −1 first).
1. "THR ⇒ M ≥ 0" in scope: exclude a (β)-fallback (N5-LV §3 kill shape), or count (β)-fallbacks per scope run (needs a level −1 STRETCH /
   FLAT-ALL).
2. If L-RED kills RB / WALK / ENT-X, re-examine §2 of P-N5-ENT first (Lemma BF's "v not on its successor's pre-c path").

## Resume point (successor 5, box 10; PARKED 2026-10-25 ~11:50Z per Lead 11:44Z; LANE-RESTART step 1; session_018GWc3YukyLgRhrrYJdrzHm)
Handover check 6be8831 (Lead 5/5). Write-ups: docs/si/N5-RL-box10.md (box 10 b), docs/si/N5-P1-box10.md (box 10b). Code:
experiments/si/riselast/ (rlprobe, rltrace, blocked, blf, ffreeze, threv, rlclimb; logs/; instances/rl_{a,b,c}.pg) and
experiments/si/p1/ (p1check.py; logs/).
### DONE (all sha1s cited to the Lead, so FROZEN: further text goes in NEW files)
- (a) P-N5-NJB fixes:
  - part 1: docs/si/P-N5-NJB-fixes-box9.md, sha1 6a337748 (NJB-1, NJB-2, NJB-L1);
  - part 2: docs/si/P-N5-NJB-fixes2-box9.md, sha1 647386fb (G-NJB-1 survivor form, which supersedes part 1's (b) and (c) texts;
    N-NJB-1 withdrawn; (5′) with both branches; concordance).
  - Both referees' §Cs agree. R35 (NJB) cites 647386fb, at CHECKER C44 (Lead 11:30Z).
- Packet P-N5-RL: docs/si/P-N5-RL-box10.md (l-si 01d69ac), sha1 0a3c70cb. Unrefereed; the Lead routes it.
  - PROVED: BL-FORM (+ R-SAME), BL (a) and (d), CONF-MONO, MERGE.
  - CONDITIONAL on (P): BL (b), (c), (e), FREE-FREEZE, EV, EV+, TEV-RED.
  - EQ-END is CONDITIONAL on CN-LAST (P-N5-SCOPE §6, in review).
  - Not to sign: TEV, RISE-LAST, NJB / ENT, and BL-X (FALSE).
- Packet P-N5-P1: docs/si/P-N5-P1-box10.md (l-si 6ba9a69), sha1 b98ca794. Lemma P1 = (P) for one-player games, PROVED (L-SI succ. 5),
  unrefereed.
  - Contents: Lemma B (the set/multiset bridge), Lemma M, Steps 1-6, the hypothesis match with R18 (§4), and a READING on what it
    discharges (R18 G-1OA-4; P-N5-RL's conditional items; NOT the two-player G-N5T-3).
  - DATA: 0 violations over 136,286 strategies.
### IN FLIGHT
- Nothing running. Climbs finished. The scratchpad is session-local.
### NEEDS
- None from the owner. The Lead routes P-N5-RL and P-N5-P1 to both referees. L-RED 16 has TEV and the one configuration (TEV-RED) as
  its item (5).
### Things only I know
- The angle that worked: inside a phase Odd is fixed (e* = τ(o)), so Even plays a one-player game G_τ.
  - W are the nominal values and Ξ the robust ones. S4a = nominal optimisation restricted to robust gates.
  - A fallback = the gated optimisation is stuck. A blocked edge is W-improving but not a gate, and it always runs F → R̄.
  - Odd's side does the work in BL: if σ_k were nominally optimal, then (o, x0) ∈ Iτ and S4b would move τ.
- The free values at a THR fallback are Even's optimum CONFINED to F (BL (c)). So after the fallback, the only free values that can
  move are those whose play passes through R̄_k0 (FREE-FREEZE). Every NJB reduction comes from this.
- Remaining configuration for NJB (TEV-RED (5)), at the second fallback k:
  - e and u_e = σ_k0(e) are both evicted at k0 and both free at k;
  - e is re-routed to a frozen f ∈ F_k0 of class (c, A);
  - the threat collects B ∖ A before e.
  - Natural sub-case: e is an evicted TAIL with target f. Not attempted yet.
- The BL climbs (score = window gate + blocked edge + no W-improving gate after a rise) stalled at 7. A blocked edge is always present
  after a rise; a window gate never appears. So the TEV / ENT side is the obstruction, not the blocked-edge side.
- Lemma P1's device: path MULTISETS make prefixing monotone (sets are not: x on top of P Δ P′). The referees will check Lemma B.
- Process trap: once a sha1 is sent, the file is frozen (Lead 11:30Z). I had to make fixes2 additive once (8ceee866 → 647386fb).
- Script traps:
  - `pgrep -f pattern` inside an until-loop matches the loop's own command line and never exits. Wait on files.
  - experiments/si/xing/reverify.sh writes to xing/out/, which is not ignored in a fresh container. Write solutions to the scratchpad
    instead (as in riselast/logs/climb_bests_verify.txt).
### NEXT (for a successor)
1. Exclude TEV-RED's configuration, starting with the sub-case "e is an evicted tail with target f". Or take L-RED 16's counterexample
   if one lands.
2. RISE-LAST at levels ℓ < L, or after r ≤ L (no ENT-SHAPE bit argument there).
3. The two-player VJ00 Lemma 5.8 (R15's G-N5T-3). P1's Step 5 does not transfer as it stands: Odd chooses, so Step 1 fails at Odd
   vertices.
4. Referee items on P-N5-RL / P-N5-P1 go in NEW fixes files. Never edit the packets.

## Resume point (successor 4, box 9; PARKED 2026-10-25 ~07:55Z per Lead 07:10Z; LANE-RESTART step 1; session_019zCLqPUCjkJxMD4vZoJ8TA)
Handover check 1cef5052 (Lead 5/5). Box 9 write-up: docs/si/N5-C-box9.md §1-§13. Code: experiments/si/coarse/ fbw.py, reltrace.py,
norf.py, minset.py, frzblk.py, abso.py, ffprobe.py, levcheck.py; jclimb.py modes HEQ / REP / NORF / MINSET. Logs: coarse/logs/box9/.
Climb bests (all re-verified with xing/reverify.sh, Oink zlk OK): coarse/instances/box9/cl9_{heq_b,rep_a,rep_b,norf_a,norf_b,mn_a,mn_b}.pg.
### DONE (PROVED by L-SI succ. 4)
- Tool fix bf8be06f: level ∞ = mono.INF = 10**6 (mono, fbcount, xing/carries). 15 logs re-run byte-identical; levcheck in check.sh.
- Packet P-N5-FBW (docs/si/P-N5-FBW-box9.md, sha1 88337bd6; pinned trunk e69772b), SIGNED by both referees:
  - FBW (every game): a fallback gate's level ≤ max(Ξ/W gap at its ends, −1).
  - FBW-S, CLS2 (fallback levels non-increasing along every scope run; (H-EQ) closed), FLAT-ALL, STRETCH, PL (a)-(c), PL-S.
  - Fixes file docs/si/P-N5-FBW-fixes-box9.md, sha1 91ff4216 (FBW-1: H1 not H2; FBW-2 = N-FBW-1: "k ≤ e"), sent 07:09Z.
  - The Lead's 07:13Z ask (REFEREE §C wording) arrived after the sha1 had gone out. The file already has the H1 wording and the
    same-row line, and it was NOT edited afterwards. If more §C text is wanted, put it in a NEW addendum file.
- Packet P-N5-NJB (docs/si/P-N5-NJB-box9.md, sha1 f43a8823, l-si 5c949ec0) FROZEN, unrefereed; the Lead pins it and routes it after
  FBW and FRZ.
  - Contents: RDROP, PL (c′) (D_M ≤ d_o − 1 + REL_M for EVERY block), PL-S′, MINSET, NO-RF-OLD, ENT-SHAPE.
  - NJB and ENT are CONJECTURES there. The packet rests on P-N5-FBW (refereed) and landed R-items only, not on FRZ.
- Lane only (N5-C-box9.md):
  - §7 PL-I, CONDITIONAL on P-N5-FRZ (25fda0f): the per-level count inside L-NEW's frozen r = ℓ blocks. NJB ⇒ (L1) polynomial.
  - §3b ABS-O (true, a dead end for NJB).
  - ONE-RISE, CONSEC, FB-RE.
- Referee items on P-N5-FBW are CLOSED (fixes file 91ff4216). R31 is waiting on CHECKER.
- P-N5-NJB is PINNED at trunk a7d85b3 (sha1 f43a8823). Referee queue: FRZ → L2 (L-NEW) → NJB. Referee items on it go to a NEW file,
  docs/si/P-N5-NJB-fixes-box9.md. Never edit the packet.
### IN FLIGHT
- Nothing running. No climbs. The scratchpad is session-local.
### NEEDS
- None from the owner. The Lead decides whether a successor or L-NEW continues ENT / NJB, depending on L-RED 15.
### Things only I know
- NJB ⇔ (MINSET) the sole minimiser σ̄(o) is never absorbed inside a level block.
  - DATA: |Mn| reaches 1 in 275 intervals and is never emptied. cl9_mn_a has 56 absorptions of Mn members and none of the last member.
- The proof attempts stop at F→F switches of level exactly L (allowed by (A) and common: 1,451). See P-N5-NJB §5 for the 5-step shape.
- Rises of θ above L after a fallback (54 in data) are never followed by another fallback in the same scope run.
  - Ideas not yet working:
    - the entry gate of an absorption, compared with FBL at the previous drain;
    - Odd's choice at o versus the cycle A that the absorption closes (rew(t_A) > rew(c_θ)).
- Scope definitions: the packet's scope run is (h) at k, H2 at k+1, w constant. reltrace.runs_of uses (h) at both ends. Same data
  either way.
- experiments/si/xing/out/ is excluded via .git/info/exclude in THIS container only. Never git add -A.
### NEXT (for a successor)
1. Prove NJB in the MINSET form, or take L-RED 15's counterexample if it lands. A refutation would need P-N5-NJB §5 (i)-(v).
2. Level −1 fallbacks per scope run; REL(S) per scope run (the remaining additive term).

## Resume point (successor 3, box 8; superseded by box 9; PARKED 2026-10-25 ~02:35Z at ~500k context after freezing P-N5-CLS; LANE-RESTART step 1)
IN FLIGHT: nothing running (all climbs finished; outputs in experiments/si/xing/out/jclimb/, local only).
NEEDS: none. Lead pinned P-N5-FB (R25 landed trunk 40ef7ed); fixes1 8548c3fc / fixes2 4d5b3716 are cited by sha1: never edit them.
(Box 8 header: Lead GO 00:18Z 2026-10-25; R25 LANDED trunk 40ef7ed from P-N5-FB.)
Box 8 write-up: docs/si/N5-C-box8.md. Code: experiments/si/coarse/cls2.py, rfinv.py (+ jclimb modes CLS2, RF).
### DONE (PROVED by L-SI succ. 3, unrefereed)
- OFFGATE (gates into F never exceed M_k, at every in-phase transition incl. jumps); CN (in-phase cycle-node switches have level -1);
  switched-edge classification at in-scope fallbacks (§3: (a)(b) flat, (c) none at THR u*≠none, (d) CLU; (c) at EQ / THR u*=none
  and (e) F→F non-cycle-node OPEN).
- TRANSFER; FRZ/LV from (A)+(B1); (A)-step; Theorem CL-S-RED: the first half of (CL-S) under (H-B1), (H-KIND), (H-EQ).
  (B1) PROVED at THR(u*≠none) and EQ fallbacks; OPEN at arena-step leaves and THR u*=none fallbacks.
- Lemma AL: after a fallback, arena leaves need rank u* <= L (given (A), FRZ).
### DATA
- OFFGATE 7,134/0; CN 7/0; (A) 0; FRZ 28,311/0; R-ROUTE 10,293/0; LV 588/0; (B1) 588/0; AL 4/0; in-scope fallbacks 260 THRu, 4 EQ,
  0 THR u*=none. OG' (MF form) FALSE on x31_re24 1->2 (mass arena leave carries a level-22 gate into F).
- Arena reversals of (Z): 39/45 occur before the first fallback at the current w (box 8 §7).
- Box 8 later: P-N5-SO check (socheck.py unmodified, 0 failures, box 8 §8); adversarial climbs vs (CL-S) 0 violations (§9);
  Lemma EQ-STRETCH (EQ runs < n+m transitions, from R17) + EQ-PERSIST (§10); (Z) map (§11): fallbacks (FB + CL-S/SO), EQ runs
  (PROVED poly), out-of-scope (O, w-changes), THR arena reversals (all within n-1 of a θ-change: reduce to Θ_scope).
- Box 8b (Lead go 02:00Z): Lemma NL + Theorem CLS1 PROVED (c47be183): fallback levels non-increasing at THR u*≠none fallbacks
  of a scope run, with no (H-B1) (minimal-counterexample induction along new plays + WM + Lemma G). (H-B1) is no longer needed there.
  Per-level count reduced to θ-changes above the level; item 2 = box 3's multiplicative recursion (box 8 §13).
### NEXT (for a successor)
1. Packet P-N5-CLS FROZEN: docs/si/P-N5-CLS-box8.md, sha1 5bbfd872, l-si 04ca0b8c (CLU, TRANSFER, OFFGATE, CN, NL, CLS1; logs
   experiments/si/coarse/logs/cls_*.txt via run_cls.sh). NEVER edit it; referee items go to docs/si/P-N5-CLS-fixes-box8.md.
   SIGNED by both referees (REFEREE a0b92ec, REFEREE-2 ffe10e1 §C 848839e). Fixes record docs/si/P-N5-CLS-fixes-box8.md
   (CLS-1..4, N-CLS-1); REFEREE §C pending. Lead note: L-NEW 13 ABS-L / per-level count via releases of absorbed exits
   (docs/new/N5-K-box33.md §8-§9) bears on open item 2.
2. Additive bound on tame θ-changes below M (box 8 §13); the per-level count and Θ per scope run hang on it.
3. EQ / THR u*=none fallbacks: their non-R->F switched edges (H-EQ incl. §3 (e)).

## Resume point (successor 3, box 7; superseded by the box 8 point above; Opus 5.5 D18/L40; started 21:31Z 2026-10-24; end-of-box ~23:45Z)
Handover check 78a764d8 (Lead 5/5). Box 7 = proof side of (C). Lane write-up: docs/si/N5-C-box7.md §0-§13. Code: experiments/si/coarse/
(mono, fbcount, tame, jump, jumpeq, dpot, ju2, clscope, eng1, jclimb; run_all.sh regenerates the packet logs; named.txt = 53 one-o files).
Climb output: experiments/si/xing/out/jclimb/ (local only, excluded via .git/info/exclude; never git add -A).
### DONE (PROVED by L-SI succ. 3 unless marked)
- Packet P-N5-FB (docs/si/P-N5-FB-box7.md, sha1 9ece9994; pinned trunk 348393b), SIGNED by both referees (§C no disagreement),
  R25 drafted by Lead. Contents: (T), COARSE-SI (a)/(b) TAME, MONO, NOINF, Theorem FB (#fallbacks per phase <= n_E(2n-1)(J+1)+J,
  +1 phase-exit), J1/OFF/CAP on 1O; (JUMP-EQ) FALSE (x31_rx32 53->54); A: L <= M signed, L >= M OPEN.
- Fixes: part 1 docs/si/P-N5-FB-fixes-box7.md (8548c3fc, REFEREE items), part 2 docs/si/P-N5-FB-fixes2-box7.md (4d5b3716, REFEREE-2
  items + concordance). Never edit the packet or a fixes file whose sha1 was sent.
- Box doc only (not refereed): §9 MIN, D1', D2, D3, NOREL-A, Corollary JD (J_in(S) <= |succ(o)| + releases into D at fallbacks).
- FALSE (own conjectures): (JU2) on jcl_x31_cu32i; (REL-NJ) naive form (4/18).
- CONJECTURE (CL-S) (§13): fallback M-levels non-increasing across a whole scope run, <= n_E per level. DATA 67 runs / 246 fb / 0.
  Reduction (READING): (CL-S) => J <= (1+N_out)|succ(o)|(1+n_E(2n-1)) + N_out => (C) <= poly(n)(1+N_out), N_out <= O + #w-changes + ...
- Pinned climb bests (all reverify.sh OK, one o): experiments/si/coarse/instances/jcl_* (J 5-17), rel_* (release-paid jumps 10-16).
- SCOPE CORRECTION (CHECKER C34 Addendum 1, Lead 23:40Z; R25 scopes it): fixes2 G-FB-3 says "the Corollary of §4 holds on every game".
  That is right for W-lowerings and WRONG for (C), which is 𝒞^1O-only (R and (C) are defined through o). fixes1/fixes2 are cited by
  sha1 in R25: never edit them; carry this scope in every later lane file.
### NEXT
1. Prove (CL-S) (box 7 §13 ideas: FBL + CLU bound THR fallback levels by rank u*; need: jumps do not undo β-flips). Then a packet.
2. Rest of (Z): arena '−' reversals and '±' (box 7 §10 split).
3. Last climbs done (box 7 §14): release-paid jumps 18 at n 48; adversarial CLS climb 0 violations of (CL-S). Nothing running.

## Previous resume point (successor 2, Opus 5.5 D15/D18; PARKED 2026-10-24 ~21:30Z at ~500k context; LANE-RESTART step 1)
Boxes done this session: handover check f0bbb5e0; box 4 (docs/si/N5-X-box4.md); box 5 (a) packet P-N5-Z (docs/si/P-N5-Z-box5.md v1,
pinned trunk fba7177, sha1 a027638f; R23 with CHECKER as C32; lane fixes docs/si/P-N5-Z-fixes-box5.md incl. referee items Z-1..Z-3,
N-Z-2); box 5 (b) + box 6 (docs/si/N5-C-box5.md §1-§6). Code: experiments/si/xing/ (every script asserts n5.run equality and
one-Odd-choice). Climb output experiments/si/xing/out/ is excluded locally via .git/info/exclude (NOT .gitignore; never git add -A).
### DONE (box 6)
- (CL) reduced (READING) to Step 1 COARSE-SI (write out the telescoping) + A (carry changes ≤ its level; DATA 198/0) + CONJECTURE
  (JUMP-EQ) (an INR jump above the last carry level lands in θ = w; DATA 4/4 first failures, 19/20 post-carry jumps).
- Step 2 PROVED: COARSE_L(Ξ) constant at k->k+1 and G(L) at k => G(L) at k+1.
- DATA: I(L) 784/0, FREEZE(L) scoped 638/0, G(L) fails at 11 states (all F->R entries, after INR jumps).
### NEXT (for a successor), in order
1. Write Step 1 (COARSE-SI) as a full proof: L-coarse super-solution in G_{σ̄_k}, telescoping, simple-path bookkeeping (VAL), and
   the exact cycle-closing exclusion.
2. Look at the one post-carry jump landing in THR (find it with freeze.py's pre-scope variant: ex entries 'F' after lastc), then try
   to prove (JUMP-EQ).
3. Prove A (carry changes Ξ only at levels ≤ L): evictees ≤ their eviction level (CLU), passive vertices inherit, F-switches flat
   (R21 (c) FBL-N (ii)), θ via exits.
4. Then (C) needs "carries per level": refills are θ-changes strictly below the level (data §3).
L-RED box 34 is nesting carries with '+−' fallback reversals as fitness (Lead 21:1xZ).

### Box 5 (GO 20:2xZ): (a) packet P-N5-Z v1 pinned (trunk fba7177, sha1 a027638f), referee items answered in
docs/si/P-N5-Z-fixes-box5.md (Z-1, Z-2, Z-3, N-Z-2; s_rt32_final OUT OF CLASS, two Odd choice vertices). (b) docs/si/N5-C-box5.md:
Lemma CLU PROVED; CONJECTURE (CL) carry levels non-increasing while w constant (0 violations, 118 carries + 3 adversarial climbs, carries
up to 33/phase in drains); (H-VL) and per-vertex CL FALSE. Next: prove (CL) (§3b: only o-free progress and entries can raise the pending
level) and bound carries per level. Pinned bests: experiments/si/xing/instances/zcl_*, ccl_*.
- Never edit a file after sending its sha1 for pinning: the Lead pins at once; corrections go to a separate fixes file.
### DONE in box 4 (PROVED by L-SI successor 2, UNREFEREED)
- Lemma ACT: every crossing transition has an active crosser (entry: switched F_k -> R̄_k edge; leave: switched R_k -> F_k edge or a new
  cycle inside R_k). Lemma LOOP: no such cycle inside a joint λ-phase when H1 holds at k.
- Fallbacks: NOFE (a switched F_k -> R̄_k edge at a fallback starts on o's W-play or on a cycle; first form "fallbacks never enter" FALSE,
  nofe_cyc_n8); NOFL-E (from Ξ = W with H2: no R_k -> F_k switch at a fallback); GAP (THR fallback leaves land in the trust gap
  Ξ_k(σ_k y) ◁ Ξ_k(z) ⊴ W_k(σ_k y)).
- Lemma LV': X ≤ (n−1)(Z+1) + Z, Z = reversals of R; |R| is the amortized ("number of ones") potential; (X) <=> (Z) up to n.
- Lemma WM: W never decreases at an arena transition; W-lowerings = carries = fallbacks (data: exactly the evicting fallbacks).
- Lemma TROP (terminal-parameter one-player game: one breakpoint per vertex) PROVED but inapplicable: N5's θ is o's own play (NG4).
- READING with box 28 §5c: O(n^5 (1 + Z + O)) transitions per joint λ-phase.
### FALSE in box 4 (own conjectures, never sent as lemmas)
- NOFE first form (nofe_cyc_n8, sha1 f3868b39 + .start). (U*-DROP): 19/19 violations. (W-LAY) ≤ n−1 W-changes between W-lowerings:
  thclimb_n16_s12 (16 at n 16). Φ(R,θ,w) potentials: x31_re24/ru24. Φ(R-side only): lev_l_sc (R = ∅ at states 8 and 32).
### OPEN
- (Z) reversals of R per joint λ-phase, hard part (C) carries = evicting fallbacks (data: Z ≤ 7 on 31 named instances; climbs Z 18 /
  carries 13 at n 32, Z 22 at n 48 with 0 carries; box 4 §6, §10); (NH'); (ELIM-poly), (LEVEL-poly), (CYC-u*) as
  before. G-N5-TIME OPEN.

## Previous resume point (successor 1, Opus 5.5 D15; PARKED 2026-10-24 ~17:35Z at ~563k context, Lead 17:3xZ; LANE-RESTART step 1)
Boxes done this session: handover check (96469356), box 1 OR lens (docs/si/N5-OR-lens.md), box 2 (N5-OR-lens-box2.md), box 3
(N5-OR-lens-box3.md). Last box SHA 8314ce9c. Code: experiments/si/orlens/ (README-level docstrings in each script); pinned instances
in experiments/si/orlens/instances/ (all Oink zlk OK, strategies verified). Oink must be rebuilt in a new container
(scripts/setup_oink.sh) before check_sol2.py / the verify Oink smoke.
### DONE — statements and status (all PROVED by L-SI successor 1, UNREFEREED unless noted)
- Box 1 (N5-OR-lens.md §2-§3): Lemma U (lev ultrametric); E1 (gap level monotone in a joint lambda-phase vs target T = Xi at phase
  end); E2/E3 (a used Even edge certifies its slack; gone for the phase once g < s); E4 (Odd best-reply exits, same); E5 (gap <= max
  slack on the play); E6 (<= n(n+1) non-flat transitions per phase, any SI rule); Lemma D + Corollary D1 (switch-all satisfies
  Howard >= VI in VJ valuations, yet exponential in one phase on switchallexp: no lexicographic contraction); (ELIM-poly) =>
  N5 < (2n(n-1)+1)(m+1)w(n); recursive depth D => < (n(n+1)+1)^D value-changing transitions.
- Box 2 (N5-OR-lens-box2.md): Lemma VIS (in a (w,u*)-run, a self-elimination (INR) of the argmin exit whose loop rho+{o} adds a
  vertex above u* retires that exit from sbar(o) for the run; <= d visible INRs per run) and VIS' (general form: after e enters R
  with loop top-new vertex t, e is sbar(o) again only if theta changed at level >= t). Data checks 0 violations.
- Box 3 (N5-OR-lens-box3.md): Lemma LEN (<= n-1 length-only theta-changes between path-set changes); Lemma CH (a SELF/OVER
  theta-change at level r is paid by a rise of the argmin exit's o-free value at level >= r); counter bound m_r <= 1 + sum_{r'>r}
  m_{r'}; hence #theta-changes <= n(1 + sum_r m_r).
### FALSE / refuted (instances pinned)
- (ELIM-n): L-RED elimn_cex_n48 (window 49 at n 48). (CYC-ELIM) with constant d: cycelim_cex_n32, s_tp32_final. 'every sbar-lap
  retires an edge': theta_tp32 states 4-9. 'one INR per exit per run': inr2_n32. 'RISE <= 2 per exit per run': rise3_n32,
  run_x_inr2 (4). PIECE does not give phase-sense elimination: fts_best16 7->8, theta_tp32 9-19. HMZ max-slack elimination:
  returns_rt48 (77/78). N5 satisfies Howard >= VI: i4_hand z = 9.
### The multiplicative obstruction (box 3 §3) and the potential a successor should look for
- SELF/OVER are paid (CH) by o-free progress of exits, a one-player resource (R17 layering in G[F]) that only holds inside a PIECE
  (R constant). Every INR is a theta-change AND a crossing, so it ends the piece and resets that resource (layering fails at
  trust-routed vertices, box 21 §3.6 (ii)). VIS' charges repeated INRs to higher theta-changes, up to d exits per change.
  => T(>=r) <= poly*(1+T(>r)): multiplicative, depth = levels used.
- Additive would need (i) a potential that RISES AT EVERY INR / crossing and is NOT restored by o-free progress, or (ii) m_r <=
  poly without the '+T(>r)' term. Lead's box 4 for the successor: (i) for crossings (X) (L-NEW box 28 §5c: transitions per phase
  O(n^4(1 + X + O))).
### OPEN
- (ELIM-poly), (LEVEL-poly) (data: max m_r 11 at n 32, lev_l_sc/lev_l_x: two nested counter digits, no third), (CYC-u*).
- Kill design (routed to L-RED): a carry above 24/21 in lev_l_sc that replays the two-digit block.

## Queue (for a successor)
1. Rerun `python3 experiments/si/families.py --engine fast --rules zadeh,cunningham --families fhz_padded --sizes 2..12`
   and the adversarial/famsearch for S5/S6 with --engine fast if S5/S6 stay live.
2. Keep check.sh green: it compiles vjfast_check and re-checks the pinned killer instances (instances/pinned.txt).

## Things only I know
- (successor 3) pgrep -f with a pattern from the same command line never ends (it matches its own shell): wait on a log line instead.
- (successor 3) Bitten again 22:0xZ by `for p in $(pgrep -f "jclimb.py 95")`: it killed my own shell (exit 144). List with
  `ps -eo pid,args | grep "[j]climb"` (the bracket stops self-match), then `kill <pid>` by number in a separate command.
- (successor 3) The predecessor's carry level L (leavers) equals M_k (max gate level) at every carry seen; use M_k, it is the one with
  proofs (MONO, FB).
- (successor 2) Never edit a file after sending its sha1 for pinning; corrections go to a separate fixes file (Lead rule, 20:4xZ).
- (successor 2) Background watchers: wait on a file condition (e.g. 'FINAL' in logs), never on pgrep -f of a pattern in the same command line.
- (successor 2) pkill -f with a pattern that occurs in the same bash command line kills that shell (exit 144): start/stop climbs with
  setsid in their own command; stop them by PID.
- (successor 2) experiments/new/box28/fbre.profile does NOT assert equality with n5.run; xclass.assert_run does (use it).
- (successor 2) xclass.py label LL = "leave through a target that was in R_k and left in the same transition", not a loop (Lemma LOOP).
- (successor 1) orlens conventions: phase = maximal run of STATES with equal (cycle-node map of Xi_sigma, of Xi_tau on G^d); a phase
  of k states has k-1 transitions (box 21's phases.py counts may differ by 1). Phase target T = Xi at the phase's last state, not
  the global optimum (earlier phases have other cycle nodes, so g would be stuck at level n+1). lev levels: -1 equal, 0 length,
  1+rank, n+1 cycle node. 'eliminating' = an edge of sigma (or tau, noelimrun_st) abandoned at that transition and absent from
  every later state of the phase; transitions where only tau moves count as non-eliminating in the sigma-only column.
- (successor 1) ortrace.run_states copies n5.run's loop; gaps.analyse asserts (iterations, fallbacks) == n5.run's; climb.py and
  sweep.py call elim_g without that assert (speed). Re-check any climb best with gaps.py before citing it.
- (successor 1) The name trace.py shadows the stdlib module 'trace': keep ortrace.py.
- Engine conventions: priorities made injective by rank (p' = 2·rank + parity, rank by (pr, index)); path component a bitmask
  over ranks; comparison key = (reward of cycle node, signed weight Σ ±2^rank, ±length). Odd's final strategy = the
  restricted-graph counterstrategy recorded during evaluation (the argmin-over-successors shortcut is WRONG: it fails
  verify.py on 3/600 random games and on switchallexp, because a successor's path may pass through the vertex itself).
- The port counts the final non-improvable evaluation as an iteration: port K = my iterations + 1.
- Family generators: Oink tools in tools/oink/build (tc, tc+, counter_*), pgsolver_port.py for recursiveladder,
  switchallexp, switchbestexp. Sizes: switchallexp n = 14N + 7, switchbestexp n = 25N + 10, tc+ grows fast (N=8: 624).
- Hansen's 2012 thesis: pure.au.dk/portal/files/52906897/thesis.pdf → HTTP 403; www.cs.au.dk/~tdh/papers/dissertation.pdf
  (the URL the errata gives) → HTTP 404 (both 2026-10-15 ~10:10Z). Not opened. What it contains, per the errata 1410.7871
  p.2: an alternative 2^Ω~(m^{1/3}) lower bound for the original Random-Facet on MDPs (the published form is 1410.7530).

## Sources opened (arXiv id or DOI, theorem/section)
- (successor 3) Vöge-Jurdziński, "A Discrete Strategy Improvement Algorithm for Solving Parity Games", BRICS RS-00-48, pdf from
  www.brics.dk/RS/00/48/BRICS-RS-00-48.pdf, sha256 485a12de… (same file as R15), opened 2026-10-24 21:35Z: p. 13-14 Remark (closed
  semiring), (6)-(10); p. 14 definition of σ̄ (minimises Ω_σ over successors) and of Prog (conditions 1-3); p. 15 Lemma 5.2
  (locally progressive ⟺ Θ_στ; cycle node = max of the cycle); p. 16 (11) Ω_σ = Θ_σσ̄ and Θ_σσ̄ ⊴ Θ_στ for all τ.
- Friedmann, "An exponential lower bound for the latest deterministic strategy iteration algorithms", LMCS 7(3:19) 2011,
  arXiv 1106.0778 (PDF opened 2026-10-15). Section 3: valuations, arena A_{G,σ}, improvement policy (conditions (1),(2)),
  Thm 3.2 (strict improvement), Thm 3.3 (regions from a non-improvable σ). Section 4: Lemma 4.1 (locally optimizing policy in
  poly time), Thm 4.2 (globally optimizing, [Sch08]), Lemma 4.3 ([Vög00]) with proof p.7: policy I^lin from a ≺-optimal σ*,
  at most |V_0| iterations; p.7 remark on intransitivity of optimal updates. Section 5: 1-sink games (definition). Thm 6.14:
  switch-all needs ≥ 2^n steps on G_n from ι_{G_n}; Thm 8.4: switch-best ≥ 2^n on H_n from ι_{H_n}.
- Zwick, "Improved subexponential analysis of the Random-Action-Removal algorithm for 2-player turn-based games and
  non-binary AUSOs", arXiv 2607.06334 v1. Section 4 (algorithm, steps 1-5), Appendix D Fig. 1 (pseudocode Rand-Act-Rem),
  Thm 8.2 (F(n,k) ≤ U(n,k), subexponential), section 3 (SI as AUSO on strategies with VAL_a ≺ VAL_b orientation).
- Friedmann-Hansen-Zwick, "Errata for: A subexponential lower bound for the Random Facet algorithm for Parity Games",
  arXiv 1410.7871 v1: abstract and p.1-2 (the RF = RF* claim is false; "The main result of [1] is thus flawed"; RF* bound
  stands; [5] Hansen thesis gives 2^Ω~(m^{1/3}) for RF on MDPs; [3] transfers it to shortest paths); section 2 (RF on
  shortest paths pseudocode).
- Friedmann-Hansen-Zwick, "Random-Facet and Random-Bland require subexponential time even for shortest paths",
  arXiv 1410.7530: Thm 6.3 (Random-Facet: ≥ e^Ω(√n) = e^Ω(M^{1/3}/log M) expected switches on G_{n,r,s,t}); p.1-2 (the SODA
  2011 bound was for parity games; the corrected bounds are for shortest paths / MDPs).
- van Dijk-Loho-Maat, "The worst-case complexity of symmetric strategy improvement", arXiv 2309.02223: Def. 2 (sink parity
  game), the generalisation J_σ(τ), J_τ(σ) (p.9, local valuation comparison), conclusion p.19-20 ("more than only local
  information", robustness against preprocessing).
- Disser-Loho-Maat-Mosis, "Lower bounds for ranking-based pivot rules", arXiv 2512.16684 v2: Thm 1.1 (informal: index-based,
  o(N/log N) memory, N^ω(1) on SI), Thm 1.2 (informal: MDP/LP rules ranking by index, reduced cost and objective improvement:
  2^Ω(√N); NOT stated for parity games), Thm 4.3 (ℓ-index-based rules, m^ω(1) on sink parity games), Lemma 4.6, Def. 3.4
  (neighbour ranking), p.3 "every deterministic memoryless pivot rule can be formulated as a ranking-based rule", Obs. 4.1
  (an N-memory rule solves a given game in linear time).
- Disser-Friedmann-Hopp, "An exponential lower bound for Zadeh's pivot rule", arXiv 1911.01074 v2: title page only (B8 source;
  not needed beyond the barrier table).
- Fearnley-Savani, LMCS 14(4:9) 2018, arXiv 1507.04500: title page only (B12).
- Fleet docs: TARGET.md v1.0; docs/DECISIONS.md D1-D6, L18-L19; docs/RESULTS.md DE1-DE3; docs/lit/RANKING.md §4;
  docs/lit/BARRIERS.md B8-B14; experiments/hard-families/README.md and pgsolver_si.py (port, stratimpralgs.ml line map).

- (successor 1, 2026-10-24) Hansen-Miltersen-Zwick, "Strategy iteration is strongly polynomial for 2-player turn-based stochastic
  games with a constant discount factor", arXiv 1008.0530 v1 (pdf sha256 f53a6b51...): Lemma 3.7 (optimality), 4.2 (contraction of
  T), 4.8, 5.1-5.2 (SI monotone), 5.3 (T v^{pi0} >= v^{pi1}: Howard >= VI), 5.4, 5.5 (||v^k - v*|| <= gamma^k ...), 6.1 (used action =>
  gap >= reduced cost), 6.2 (l1 gap <= n/(1-gamma) max reduced cost), 6.3, 6.4 (every sigma^k has an action absent after k+L,
  L = log_{1/gamma} n^2/(1-gamma); only player-1 actions are eliminated), Thm 6.5 ((m+1)(1+L)), §7 (Friedmann: exponential when
  gamma is part of the input or undiscounted).
- (successor 1) Scherrer, "Improved and generalized upper bounds on the complexity of policy iteration", arXiv 1306.0386 v4 (pdf
  sha256 391b6481...): Thm 1 (quotes Ye 2011: O(mn/(1-gamma) log n/(1-gamma))), Thm 2 (HMZ), Thm 3-4, Thm 5 (Post-Ye), Lemmas 4-5
  (= Post-Ye Lemmas 3.4, 3.5: new cycle every O(n^2 m log n) iterations; progress per new cycle), Def. 1 (tau_t, tau_r), Thm 6,
  Assumption 1 + Thm 7 (Howard PI O~(m(n^2 tau_t + n tau_r)) for MDPs only), §2 remark: removing 1/(1-gamma) impossible for Howard's
  PI (Fearnley 2010).
- (successor 1) Post-Ye, "The simplex method is strongly polynomial for deterministic MDPs", arXiv 1208.5083 v2 (pdf sha256
  c51876eb...): abstract (O(n^3 m^2 log^2 n), any discount; "layers" measure of progress), Lemmas 3.4, 3.5.
- NOT opened: Ye 2011, Math. Oper. Res. 36(4):593-603, DOI 10.1287/moor.1110.0516 (cited only through Scherrer Thm 1).
- (successor 11, 2026-10-26 02:34Z by date -u) Vöge, Jurdziński, BRICS RS-00-48 (Dec 2000), www.brics.dk/RS/00/48/BRICS-RS-00-48.pdf,
  sha256 485a12de432a2a8c… (the fleet's file; downloaded into the scratchpad, pdftotext). Read: §2 p. 3 (finite game graphs, every vertex
  has an out-going edge; no other restriction), §4.3 (Ωσ(v) = min⊴ {Θ(P) : P ∈ Playsσ(v)}), §5.1 (3), (4), (6)-(10), §5.2 (σ̄ := a successor
  minimiser of Ωσ; Prop. 5.1; Lemma 5.2 with proof; (11) Ωσ = Θσσ̄ and "Θσσ̄ ⊴ Θστ, for all strategies τ for player ⊖", p. 16). Used for
  premise (VJ) of Lemma OUT-G (docs/si/P-N5-1E-box16.md §2).

## Dead ends (details in docs/si/DEAD.md)
- TEV / TEV-LAST (succ. 5 conjecture): FALSE, tev_cex_n40 (17078f78), tevlast_cex_n40 (ff1e9cb4); transient absorption at an S4a state.
- (box 9, succ. 4) ABS-O as a route to NJB: vacuous, since every block has M >= rank o when o counts in θ's path set (abso.py fb_hi = 0 of 778;
  obstruction: R→F gates differ at o). docs/si/N5-C-box9.md §3b.
- (successor 3, box 8) OG′ ("gates into F at k+1 never exceed MF_k = the max level of the gates INTO F at k") FALSE:
  experiments/red/xing/instances/x31_re24.pg (sha1 49eaf50e, 𝒞^1O), transition 1 -> 2: MF_1 = -1, while gate (4, 8) at state 2
  has level 22. At state 1, 4 and 8 are in R (the level-22 gate is (8, 14), R -> R); at the arena step R collapses from 21 vertices
  to {12}, carrying the high level into F. The true form is OFFGATE (bound M_k, all gates). Box 8 §1.
- (successor 3) CONJECTURE (JUMP-EQ) (box 6 §6.2) FALSE: experiments/red/xing/instances/x31_rx32.pg (sha1 4fe9ec0e), transition
  53 -> 54: w constant since the carry at level 24, σ̄(o) 24 -> 31 (INR), θ rises at level 25, lands THR with θ ≠ w; θ = w only at 55.
  Re-verified n5 55/3, Oink zlk OK, strategies verified. Not needed: Theorem FB (box 7 §4).
- (successor 2, 2026-10-24) Parametric/tropical lens for (X): o as a terminal of value θ is ill-posed for N5 (optimal routes run through
  θ's own play: 247 vertex-states on lev_l_sc; switch-all on the abstract game does not converge on fbref_cex_n32). Gadget version
  (frozen copy of θ's play) has a rank artefact (copies rank differently from originals): its "R* constant" output is void.
- (successor 2) (U*-DROP) "rank(u*) drops between consecutive evicting fallbacks with w fixed": FALSE, 19/19 (ustar.py; fbref_cex_n32,
  lev_l_x, run_x_inr2, x31_lem_t32, s_rt32_final). u* stays at the top rank through every carry.
- (successor 2) (W-LAY) "≤ n−1 W-changing transitions between W-lowerings": FALSE, thclimb_n16_s12 (16 at n 16; θ gates entries).
- (successor 1, 2026-10-24) HMZ-literal elimination for N5 ("the max-slack action of sigma_k is gone within L transitions"): fails on
  returns_rt48 (experiments/red/n5inj/instances; a max-slack edge survives 77 of 78 phase transitions; hmzL.py). Obstruction: the
  gap level max_v g stays constant for ~ the whole phase (gaps.py gmaxrun 77/78, 102/103 on returns_ph64).
- (successor 1) Lexicographic contraction (HMZ Lemma 4.8/5.5 with VJ valuations): impossible. switch-all satisfies Howard >= VI (Lemma
  D, PROVED) yet is exponential in one lambda-phase on switchallexp; VI from Xi_0 stalls at a spurious (c,P) fixed point (switchallexp
  N 3: 45/49 wrong after 300 rounds). Instance: si/instances/switchallexp_N3.pg.
- (successor 1) N5 satisfies Howard >= VI: FALSE (i4_hand + start, vertex z = 9, states 0-2: trust mode; vi.py).
- (successor 1) "abandoned edge => eliminated for the phase": FALSE (fts_g43: 67 returns to positive-slack edges; returns.py).
- S4 subgame-optimal start: switchallexp, counts identical to switch-all (2486 at N=8, doubling).
- S2b LSF: zadehexp 33..15301 (N=2..10, doubling); DLMM Bland counter 2^n - 1; M_L port 2^(L+1) - L - 2.
- S3 steepest: M_L port, identical run to LSF, 2^(L+1) - L - 2.
- S2a MSF (+ msfa, msfc): L-RED's gated Bland counter, 2^N - 1 exactly (reproduced on si.py); the gate decouples level from
  effect through an escaped cycle-creating switch; my obstruction (b) was wrong.
- S1 Random-Action-Removal: FHZ 1410.7530 Thm 6.3 transferred by L-RED (conditional on the transfer lemma).
- Obstruction (a) still stands: Disser-Mosis B_n does not port faithfully to lexicographic valuations (arithmetic rewards).
- Claim F as first stated (bit notion) was false (L-RED's cf1, cf2); F' (play notion, cycle included) holds in the data.

## Freezing observation for MSF (2026-10-15 11:00Z; data + proof sketch, UNREFEREED, not a result)
Setting: VJ valuations, lexicographic order (cycle node first, then path set by rank, then length). Level of an improving edge
(v, w) = rank of the first difference between Ξσ(w) and Ξσ(σ(v)) (docs/si/candidates/S2.md). Call the switch cycle-creating
if v lies on the path set of Ξσ(w).
Claim F: a NON-cycle-creating single improving switch at level r changes no vertex's cycle node and no path bit of rank > r.
Data: experiments/si/freeze_test.py: 0 violations over ~6000 MSF switches on 6000 random games and ~6000 on 6000 1-sink
games (n ≤ 9), same for msfa and msfc; every observed violation is a cycle-creating switch (2-3 per 6000 games) or a
cycle-node change (all of them cycle-creating switches, to be re-checked).
Proof sketch: let τ be Odd's optimal counterstrategy for σ. Under (σ', τ) with σ' = σ[v→w], the play from any u either avoids v
(value unchanged) or runs P·v·(τ-path from w); the τ-path from w cannot re-enter P∪{v} (it would then reach v, contradicting
v ∉ path(w)), so its value is P ∪ {v} ∪ path(w) with the old cycle node, which agrees with the old value P ∪ {v} ∪ path(σ(v))
above rank r. Ξσ'(u) lies between Ξσ(u) (Friedmann Thm 3.2) and this value; two valuations agreeing above r sandwich only
valuations agreeing above r. Gap: the "cannot re-enter" step needs the τ-path from w under σ' to equal the one under σ,
true because the only changed edge is at v and the path avoids v.
Consequence (if F holds): in a run with no cycle-creating switches, MSF makes ≤ n switches at the top level, and level r is
revisited only after a higher-level switch; this gives only an exponential bound by itself (S_r ≤ n(1 + S_{>r})). The
adversary's tool is a high-level improving edge that is cycle-creating until low-level switches change the paths; then it
fires late and unfreezes everything below. Variants: msfa (prefer non-cycle-creating edges), msfc (prefer cycle-creating).

## Refinement (11:20Z, unrefereed): where MSF's iteration count can hide
Under Claim F and Friedmann Thm 3.2, in a stretch of an MSF run with no cycle-creating switch: a level-r switch at v makes
bit r of Ξ(v) good and bits above r never change (F) while Ξ(v) only improves, so bit r of v stays good until a switch at a
level > r; MSF takes the highest level available, and lower switches never create higher-level improving edges (F), so once
level k is exhausted it never recurs; hence at most n switches per level: ≤ n(n+1) switches in the stretch (sketch only; the
DLMM Bland counter shows the mechanism: MSF needs 1 switch, Bland/LSF 2^n - 1).
A cycle-creating switch (v on the path of w; the new cycle through v is even-dominated, level = rank of its dominator) either
changes some cycle node (at most n^2 such events in a run: each vertex's cycle node improves ≤ n times) or is "escaped" (Odd
reroutes, cycle nodes unchanged, high bits may change arbitrarily). So: MSF switches ≤ (n^2 + 1)·(n^2 + X + 1) with X = the
number of escaped cycle-creating switches. MSF is polynomial iff X is (modulo the sketch). The adversarial search now has an
objective "escapes" (adversarial.py --objective escapes) to maximise X directly.

## T12 section 4 follow-up (11:25Z): D_n with Odd gates, why not built as a port
Sources opened: Disser-Mosis arXiv 2309.14034 (ISAAC 2023): section 3 B_n (Table 1: travel/enter/skip/board/stay/leave,
rewards 2^l for enter, 0.75 for stay, -2^l+1.25 for board), Definition 6 (canonical policies), section 4 D_n (Fig. 4: every
edge (v,w) replaced by v -> x_{v,w} -> y_{v,w} (randomisation, p_v to z_{v,w} -> w, 1-p_v back to v)), Thm 28
(p_v = 2^{-N_V(v)(n+5)}; Dantzig prefers small vertex numbers). DLMM 2512.16684 Lemma 5.4 and M_L (Fig. 5.1).
(a) B_n's reward bookkeeping is arithmetic (three 0.75-stays beat one enter(1) = 2); the VJ set order is lexicographic, so
B_n does not port faithfully for n >= 3; M_L does (rewards L^l, see gens.py dlmm_ML) and its port behaves as Lemma 5.4
predicts for the least-preferred rule (LSF 2^(L+1)-(L+2)); the same run kills steepest (S3).
(b) The D_n trick decouples a switch's reduced-cost magnitude (scaled by p_v) from its effect. In the VJ order the sign
and the level of an improving edge are both read at the first-difference position, so I found no gate that gives
"level decreasing in l while the sign follows B_n": an even designer vertex on one route makes the edge always improving,
an odd one never, and a loop back to v makes it cycle-creating with the dominator's parity deciding. Not built; the
gadget-chain search (famsearch.py --seed-template dlmm) and the escapes objective stand in for it.

## MSF bound argument, step by step (for L-RED and referees; 11:35Z). Each step is marked PROVED (here), CITED, or OBSERVED.
Setting. G a parity game, priorities made injective by rank (p' = 2·rank + parity; the game's winner on every cycle is
unchanged: PROVED, since the max-priority vertex of a cycle keeps its parity and order). VJ valuations Ξσ(v) = (c, P, ℓ):
cycle node c (the most relevant vertex on the cycle Odd's optimal counterstrategy τσ reaches from v), path set P (vertices
on the path more relevant than c), length ℓ. Order ≺ as Friedmann 1106.0778 section 3 (CITED). Sink game: Friedmann
Definition 5 (1-sink, sink-seeking) (CITED); in a sink-seeking run every cycle node is the sink.
S1 (CITED, Friedmann Thm 3.2 = [VJ00]): if σ' = I(σ) for an improvement policy I (in particular a single improving switch),
    then Ξσ(u) ⪯ Ξσ'(u) for every u, with strict inequality somewhere.
S2 (definition). An improving edge (v, w) of σ has level r = the rank of the first difference between Ξσ(w) and Ξσ(σ(v)):
    if the cycle nodes differ, the level class is (3, max rank of the two cycle nodes); else (2, max rank in P(w) Δ P(σ(v)));
    else (1, 0). MSF switches one improving edge of maximal level (ties: smallest v, then w). The switch is cycle-creating
    if v ∈ P(w).
S3 (Claim F, OBSERVED, proof sketch): let (v, w) be a non-cycle-creating improving edge of level (2, r) (same cycle node c
    for w and σ(v); path sets agree above r), σ' = σ[v→w]. Then for every u: Ξσ'(u) has cycle node c(u) unchanged and
    P'(u) agrees with P(u) on all ranks > r.
    Sketch. (i) Let τ = τσ (optimal counter for σ). Under (σ', τ) the play from u is either the old play (if it never
    visits v: value unchanged) or P_u · v · (play from w under (σ, τ)) where P_u is the old play prefix from u to v; the
    play from w under (σ, τ) does not visit v (v ∉ P(w) and v is more relevant than ... [GAP G1: v ∉ P(w) says v is not on
    w's path AMONG THE VERTICES MORE RELEVANT THAN c; if rank(v) < rank(c) the vertex v could lie on w's path without
    appearing in P(w). In a sink game every non-sink vertex is more relevant than the sink, so G1 is void there; in general
    the claim must be stated with "v not on w's play" instead of v ∉ P(w)]; and it does not re-enter P_u (else it would
    reach v along P_u). So the (σ', τ)-value of u is P_u ∪ {v} ∪ P(w) with cycle node c: it agrees with the old value
    P_u ∪ {v} ∪ P(σ(v)) above r. (ii) Odd's optimum for σ' is ≤ this value (τ is one Odd strategy; needs: the (σ',τ) play
    value is ≥ Ξσ'(u) by optimality of τσ' [PROVED by definition of the optimal counterstrategy]). (iii) Ξσ'(u) ≥ Ξσ(u) by S1.
    (iv) In a lexicographic order, a value between two values that agree above r (same cycle node, same bits above r)
    agrees with them above r [PROVED: the first difference of the bounds, if any, is at rank ≤ r]. Lengths are below all
    path bits in the order [CITED, definition of ≺]. Data: 0 violations in ~24,000 non-cycle-creating MSF switches
    (freeze_test.py; random and 1-sink games, n ≤ 9).
S4 (PROVED from S1, S3): in a stretch of a run with no cycle-creating switch, no cycle node changes (S3 with the cycle
    component), and a switch at level (2, r) changes no bit above r of any vertex.
S5 (PROVED from S3, S4, S1): in such a stretch, after a level-(2, r) switch at v, bit r of Ξ(v) is the good value (the
    first difference of Ξσ(w) over Ξσ(σ(v)) is at r in Even's favour; Ξσ'(v) = ext_v(Ξσ'(w)) with Ξσ'(w) ⪰ Ξσ(w) agreeing
    above r, so its bit r is at least as good; v itself has rank ≠ r [PROVED in sink games: rank(v) = r would put v on
    one of the two paths, i.e. on its own play, a cycle through v other than the sink, contradicting sink-seeking;
    OBSERVED only in general]) and it stays good until a switch at a level > (2, r): lower switches do not touch bit r
    (S4); same-level switches elsewhere change Ξ(v) only upward (S1) with bits above r fixed (S4), so bit r cannot
    worsen.
S6 (PROVED from S4): a switch at a level < (2, r) never creates a level-(2, r) improving edge: the improving status at
    level (2, r) of (v, w) depends only on bits ≥ r of Ξ(w) and Ξ(σ(v)) [PROVED: by S2, with agreement above r required
    and the comparison at r], which lower switches do not change (S4); σ(v) changes by a lower-level switch at v only to a
    w'' agreeing with σ(v) at all ranks ≥ r [PROVED: that is what level < (2, r) means].
S7 (PROVED from S5, S6 and the MSF order): in a stretch with no cycle-creating switch, MSF exhausts level (2, R) (R the
    top rank) with at most n switches (each vertex at most once, S5), never returns to it (S6), then exhausts (2, R-1)
    with at most n switches, and so on: at most n per level, at most n(n+1) + (level-(1,0) switches) in the stretch.
    [GAP G2: level (1, 0) switches (length only). OBSERVED small; PROVED bound: none written. Sketch: with all path sets
    frozen (S4 with r = -1), a length-only switch at v strictly improves ℓ(v) in Even's direction, ℓ ∈ [0, n], and other
    vertices' lengths move monotonically by S1 with path sets fixed, so ≤ n per vertex, ≤ n² in the stretch.]
S8 (PROVED): a cycle-creating switch at v is improving iff the most relevant vertex d of (P(w) \ P(σ(v))) ∪ {v} ... more
    precisely of the cycle C through v and w under (σ', τσ), is even [sketch: P(w) = C-part ∪ P(v)-part disjointly, the
    comparison with P(σ(v)) is decided at the max of the cycle part]. After it either some vertex's cycle node changes
    (CYCLE EVENT) or none does (ESCAPE).
S9 (PROVED): cycle events ≤ n·(number of distinct cycle nodes) ≤ n²: a vertex's cycle node strictly improves in the
    reward order at each change (S1).
S10 (PROVED from S7-S9, modulo G1, G2): #switches ≤ (n(n+1) + n² + 1) · (n² + X + 1), X = number of escapes.
    [Lead/REFEREE wording: MSF is polynomial iff X is polynomially bounded.]
OBSERVED about X: hill-climb maxima of X: 2, 5, 5, 7, 10, 14 (n = 5..10, small search), 14 at n = 8 with a larger search;
one vertex escaped 7 times in an 8-vertex game (out/adv_msf-esc2_n8.pg), so repeated escapes at one vertex are possible.
No argument bounds X. This is the open point.

## CORRECTION (2026-10-15 11:50Z, credit L-RED via the Lead 11:47Z): "cycle-creating" must be the play notion
L-RED found that si.py's test "(val[w][1] >> rank[v]) & 1" checks membership of v in the path SET of Ξ(w), which holds
only vertices more relevant than w's cycle node; a v on Odd's play from w but less relevant than the cycle node was
wrongly classed non-cycle-creating, and Claim F fails for such switches (L-RED: 6 violations in 11,795 switches on 20,000
random games under the bit notion, 0 under the play notion; 2,649 of 3,563 cycle-creating switches were misclassified).
Counterexamples reproduced with si.py (instances/red_cf1.pg, red_cf2.pg, start sigma(2)=1): cf1's edge (2,3) has level
(1,0), bit-notion 0, play-notion 1, and changes the cycle nodes of 2 and 3; cf2's edge (2,3) has level (2,5), bit-notion 0,
play-notion 1, and changes 2, 3, 6. This is exactly gap G1 of the step-by-step argument above.
Fix (si.py Engine.cycle_creating): v is cycle-creating for (v, w) iff v lies on Odd's (σ, τσ)-play from w before that
play first reaches w's cycle node. msfa / msfc now use it (their docstrings were wrong before; the earlier msfa/msfc sweep
numbers measured the bit-notion rules and are withdrawn). freeze_test.py now also checks level-(1,0) switches (must
change no cycle node and no path bit at all) and reports cycle-node changes by non-cycle-creating switches separately.
Claim F' (restated): a NON-cycle-creating (play notion) single improving switch at level (2, r) or (1, 0) changes no
vertex's cycle node and no path bit of rank > r (all path bits, for level (1, 0)). Data after the fix: 0 violations of
either kind over 8,000 random and 8,000 1-sink games (n ≤ 9), msf; 0 for msfa on 4,000.
Second slip (12:05Z, found by freeze_test after the first fix: 34 of 4,154 random-game switches and 13 of 4,015
sink-game switches classed non-cycle-creating still changed a cycle node): the play from w must be followed INTO its final
cycle, not stopped at the cycle node; v on that cycle after the cycle node also closes a cycle. cycle_creating now walks the
(σ, τ)-play from w until a vertex repeats and reports whether v was visited.
Sandwich argument with the play notion (closes G1): the (σ, τ)-play from w never visits v (definition, cycle included), so
after the switch the (σ', τ)-play from any u is either the old play (never visits v) or P_u · v · (the old play from w),
which does not re-enter P_u ∪ {v} (it would reach v): its value is P_u ∪ {v} ∪ P(w) with cycle node c(w) = c(σ(v)); the
rest is S3 (ii)-(iv). Data after both fixes: see the freeze_test lines below.
Every X measured before this correction (escapes objective) is an undercount; re-measured with the play notion in
out/adv_msf_esc3.log.
freeze_test.py after both fixes (12:10Z): msf, 8,000 random games n ≤ 9, 4,154 switches: cycle-node changes by
cycle-creating switches 1,447, by non-cycle-creating 0; path bits above the level changed (cycle nodes fixed) by
cycle-creating 6, by non-cycle-creating 0; level-(1,0) switches included. Same on 8,000 1-sink games (4,015 switches:
1,130 / 0 / 7 / 0) and for msfa on 4,000 random games (2,065 switches: 717 / 0 / 2 / 0). F' holds in the data.
Consequence for the bound S10: X now counts play-notion escapes, and cycle-creating switches are about a third of all MSF
switches on random small games (1,447 of 4,154), so X is of the order of the iteration count itself there; the bound
(n(n+1) + n² + 1)(n² + X + 1) is correct but says nothing until X is bounded. Re-measured X: out/adv_msf_esc3.log.
The msfa/msfc family sweep (out/fam_msfvar.log, bit notion) is withdrawn; rerun with the play notion: out/fam_msfvar2.log.
