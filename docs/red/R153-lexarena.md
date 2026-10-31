# R153: the width-2 LEX-ARENA counter is NOT realised inside one N5 W-run, and the exact obstruction is Ξ supply. (1) In T54's abstract model one top vertex alone runs through ALL 2^(L−1) keys (exhaustive, L = 2-6: 1, 3, 7, 15, 31 strict key decreases), so CONJECTURE KEYCH-POLY is false under adversarial arenas and any proof must use S2's Ξ-improvement. (2) PROVED (lane): in N5 the lex structure cannot amplify Ξ. KEYCH_I(v) ≤ (switching transitions in I) ≤ m_E + Σ over Even edges (u, w) of XICH_I(w) (Lemma SW-XI, Corollary KEY-XI). So the counter needs as many Ξ-changes in ONE W-constant interval as it has key decreases, and KEYCH-POLY ⇐ XI-CH-POLY ⇔ WRUN-POLY (R95): the TIE face adds no new hardness and no new leverage. (3) DATA: corpus max KEYCH 8 = |F| (u23sw64_n32); the long (quadratic) one-W-run families have KEYCH 0 (odd cycle nodes, where ties cannot return: R152 O1-ODD); climbs reach KEYCH 9-10 at n 32-48
L-RED successor 36 (Opus 5.5; D1/D18). Lead 2026-10-31 01:56Z: «GO for your proposed R153: realise T54's width-2 LEX-ARENA counter inside one
N5 W-run, with the arena schedule fed by Ξ-improvement. Score it as KEYCH_I(X) in ONE W-constant interval (the KEYCH-POLY target) and the
W-run length; super-linear KEYCH in n kills KEYCH-POLY. If it cannot be realised, give the exact obstruction and the instance that blocks
it.» Written 2026-10-31 from 02:20Z (date -u).
- Labels: DEAD / PROVED (lane) / DATA / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.
- Sources opened:
  - l-lit 0ee955c7 docs/lit/T54-stalling.md §4.2-§4.4 and docs/lit/T54-lexarena.py (the model and its step rule, reused verbatim);
  - this lane's R152 (TIE-W, KEY-MON, XI-PAY; aefe261c).
  - Not opened: l-new 8591166d docs/new/N5-TIE-box106.md (TIE-RED, CONJECTURE KEYCH-POLY). I use only the Lead's 01:56Z summary of it.
- A correction to the brief's scoring. A super-LINEAR KEYCH kills only a linear bound. KEYCH-POLY is killed only by a family with KEYCH
  super-polynomial in n. Below, «KEYCH-LIN» is the linear form, which no N5 instance here kills either.

## 1. The abstract model: one vertex, all keys (DATA, exhaustive)
- red/lex/lexone.py is T54-lexarena.py's model and step rule, unchanged. The adversary picks the set of vertices with a full arena; the
  others keep σ(v); the new σ is the lex-BFS choice layer by layer. The score is the number of strict key decreases of ONE top vertex
  (layer L, first vertex), maximised over all schedules by DP.
  | L | n | max key decreases of one top vertex | distinct keys 2^(L−1) |
  | --- | --- | --- | --- |
  | 2 | 5 | 1 | 2 |
  | 3 | 7 | 3 | 4 |
  | 4 | 9 | 7 | 8 |
  | 5 | 11 | 15 | 16 |
  | 6 | 13 | 31 | 32 |
- So one vertex passes through every key, 2^(L−1) − 1 decreases at n = 2L + 1. KEYCH-POLY, stated for adversarial arenas ⊇ {σ(v)}, is
  false. Any proof of KEYCH-POLY must use the constraint that the arena is {σ(v)} ∪ Iσ(v), the Ξ-improving edges (T54 §4.4 says the same
  for run length; this is the per-vertex form).

## 2. Why N5 cannot run the counter for free (PROVED, lane; L-RED successor 36)
Fix a τ-stretch (in particular a W-run F) and an interval I of it. XICH_I(w) := number of transitions of I at which Ξ(w) changes.
- Lemma SW-XI. If Even u switches s times in I, at k_1 < … < k_s, then s ≤ Σ_(w ∈ succ(u)) (1 + XICH_I(w)).
  - Proof. Let w_i := σ_(k_i + 1)(u), w_0 := σ_(k_1)(u). Each switch goes into Iσ (step-2 arena {σ(u)} ∪ Iσ(u); fallback switches are
    improving too), so Ξ_(k_i)(w_i) ▷ Ξ_(k_i)(w_(i−1)). Ξ is monotone in a τ-stretch ([R15], as in RUN-SETTLE Case 1), so
    Ξ_(k_i)(w_(i−1)) ⊵ Ξ_(k_(i−1))(w_(i−1)). Hence the values Ξ_(k_i)(w_i), i = 1 … s, strictly increase. The map i ↦ (w_i, Ξ_(k_i)(w_i))
    is therefore injective. Its image lies in the set of pairs (w, a value of Ξ(w) in I), which has Σ_w (1 + XICH_I(w)) elements. □
  - This is R152's XI-PAY in counting form: every re-opening of an edge is paid by a Ξ-rise at its head.
- Lemma KEY-SW. If key_(k+1)(v) ≠ key_k(v), then some Even vertex on v's (σ_(k+1), τ)-path switches at k. (Otherwise the path, hence the
  key, is unchanged; τ is fixed.) □
- Corollary KEY-XI. For every v and every interval I of a τ-stretch,
  KEYCH_I(v) ≤ #{k ∈ I : some Even vertex switches at k} ≤ Σ_(u Even) s_I(u) ≤ m_E + Σ_((u, w) ∈ E, u Even) XICH_I(w),
  with m_E the number of Even edges. In particular KEYCH_I(v) ≤ |I|.
- Consequences.
  - No amplification: a lex counter with K key decreases at one vertex in one W-constant interval forces Ω(K / m) Ξ-changes in that
    interval at the heads of Even edges. T54's exponential schedule needs an exponential Ξ supply, i.e. a super-polynomial XICH in one
    W-run. That is the R95 residual (WRUN-POLY ⇔ XI-CH-POLY), not something the lex structure provides.
  - KEYCH-POLY ⇐ XI-CH-POLY (per W-run), and KEYCH ≤ |F| gives KEYCH-POLY ⇐ WRUN-POLY. With L-NEW's TIE-RED (tie returns ≤ KEYCH, as
    the Lead states it), the TIE face sits under the same premise. A proof of WRUN-POLY through TIE-RED must bound KEYCH WITHOUT bounding
    Ξ-changes first. Otherwise it is circular. §1 shows it cannot bound KEYCH from the lex structure alone.
- The exact obstruction to the brief's realisation: a gadget that runs the width-2 counter for K steps at one top vertex must, by SW-XI,
  supply ≥ K − m_E Ξ-changes at the heads of Even edges inside ONE W-constant interval of the top vertex. The known Ξ supplies are:
  - the Odd observer (R148-hxs: HXS at one source K(m + 1));
  - the quadratic one-W-run families (sbq2, obs, latew).
  Both are quadratic, and in all of them the W-cycle nodes are ODD (KEYCH 0, §3). There, R152's O1-ODD shows ties strictly lower the
  successor index, so no lex stall can run. (READING from here on, not proved:) To couple an even-c tie DAG to such a supply, the supply's Ξ-rises must reach DAG successor
  heads as LEAPFROGS between the two W-tied successors of each DAG vertex. One observer vertex h feeds every gate the same value Ξ(h), so
  two gates hung on h never leapfrog each other. A width-2 counter of depth L needs ~2L independently scheduled supplies.

## 3. DATA
- red/lex/keych.py: for every W-run, every vertex v ∉ C with Ω(λ_W(v)) even, and every maximal interval with W(v) constant, the strict key
  decreases of v (key as red/tie/o1key.py, = T54's key). It also counts key RISES at fixed W (KEY-MON says 0).
- Corpus (red/lex/runkeych.sh; sbcg 719 + alt 413 + casc / xcn pins; distinct lines): max KEYCH 8 (u23sw64_n32, = |F| = 8);
  key rises at fixed W 0. Nonzero only on the tie games (u23sw64_n32 8, u1t_cex_n32 7, u1t_own6_n32 6, …).
- Quadratic one-W-run pins: sbq2_K8_m16 (n 261, |F| 152), obs_K12_m24 (n 272, |F| 324), latew_K8_m32 (n 370, |F| 280), latew_K16_m32
  (n 482, |F| 560): KEYCH 0 in all four (their cycle nodes are odd).
- red/lex/swxi.py checks SW-XI and its strict chain at every Even vertex of every W-run. Pins: u23sw64_n32 94 switches, tie_n32 102,
  cedge_n32 98, sbq2_K8_m16 513; violations 0, chain failures 0. Corpus (red/lex/runswxi.sh, 812 distinct games): 37,718 switches,
  violations 0, chain failures 0.
- Climbs (red/lex/kclimb.py = red/tie/tclimb.py with score (max KEYCH, longest W-run), seeded from tie_n32, 60 min, PAD 0 / 16). Final (170,401 / 95,442
  steps): best KEYCH 10 with longest W-run 19 (PAD 0, n 32; kept as lex/instances/keych10_n32, sha1 586f57c4…, «KEYCH keych10_n32.pg n 32
  iters 22 maxL 19 maxKEYCH 10 (v 15 from 0 to 12) keyrises_at_fixed_W 0», xeng identical, Oink OK); KEYCH 9, W-run 15 (PAD 16, n 48;
  xeng identical, Oink OK). KEYCH stays below |F| < n. No growth.

## 4. READING
- The tie face is real (O1 is dead, the abstract model is exponential), but in N5 it is not a separate source of length. Every key
  decrease is a switch, and every switch is a Ξ-rise at an edge head. The open question stays R95's XI-CH-POLY.
- For L-RED's next kill attempt, the target is a super-polynomial Ξ-change count in one W-run, with either parity of c. The ODD branch
  needs W-changes per return (O1-ODD, NONTIE-RET). The EVEN branch can use ties, but SW-XI makes them cost the same Ξ-rises.

## 5. Pins (experiments/red/check.sh «R153»)
- red/lex/lexone.py L = 4 (7) and L = 5 (15).
- keych.py on tie/instances/u23sw64_n32 (maxKEYCH 8) and flipev/instances/sbq2_K8_m16 (0).
- swxi.py on tie/instances/tie_n32 (violations 0, chainbad 0).

## DONE / FINDINGS / NEEDS
- DONE: this note; red/lex/ (lexone.py, keych.py, swxi.py, kclimb.py, runkeych.sh, runswxi.sh, corpus outputs); check.sh «R153». SHA: see
  the commit.
- FINDINGS:
  - Not realised. The obstruction is PROVED (lane): SW-XI / KEY-XI give KEYCH_I(v) ≤ m_E + Σ XICH_I. The lex counter needs a Ξ supply as
    long as itself, and KEYCH-POLY ⇐ XI-CH-POLY ⇔ WRUN-POLY.
  - DATA: in the abstract model one vertex makes 2^(L−1) − 1 key decreases (exhaustive L ≤ 6), so KEYCH-POLY needs S2.
  - DATA: corpus KEYCH ≤ 8 = |F|; quadratic families KEYCH 0 (odd c).
  - Scoring correction: super-linear KEYCH kills KEYCH-LIN, not KEYCH-POLY.
- NEEDS: none.
