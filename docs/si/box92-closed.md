# Box 92: does box 85's TWO-COPIES kill transfer to the waiting-High class? (L-SI successor 48; Lead 00:14Z 2026-11-09)
Written 2026-11-09 (date -u in the commit). Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD /
READING. Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1). No counterexample candidate.
Setting: box 91 (docs/si/box91-expel.md; WAIT-TRIGGER: an unlock of h_k is paid by its β-face, by a Λ-change or by a letter entering the
β-face's play). Box 85 (docs/si/box85-twocopies.md: FLIP-U, LOW-NULL, POOL-ALT), box 84 m3 (LOWER-BLIND keep form, SELF-MIRROR DICHOTOMY),
box 84 m2 (LIVE-BREAK), box 86 (SAME-E-MERGE, ACCESS-LATCH, LEAPFROG; LAG TOWER DEAD at h = 2, 3), L-RED R222 §3 (PRIV-FLIP).
Tools: experiments/si/box92/ (gate92.py on box 91's engines and frozen instances; run92.sh; check92.sh, wired; out/own92.out, g392.out,
ctrl92.out). Engines as box 91 (own = L-RED R221 own.py at claude/l-red 4b309716; g3 = L-NEW's Γ3 N5′-xi from S3 at claude/l-new fcba92fc).

## 0. Answer
- (1) YES, box 85's obstruction TRANSFERS, for every gate whose β-face does not return through the gate (PRIV_g), by one new lemma:
  **Lemma GATE-LOW-NULL (PROVED, lane; §1)**, the gate form of FLIP-U / LOWER-BLIND: while both faces of a gate o have the same Λ and
  PRIV_g holds, Odd's choice at o is decided by the part of the two faces' e-sets at least as relevant as o's own e-vertex e_o, and o flips
  only at steps where that part changes. So for the waiting-High class:
  - the race's letters (h_(k−1), z ≺ h_k) and ANY copy whose letter lies below h_k cannot unlock h_k at all (LOW-NULL, as for box 85's low
    copy);
  - a second vertex that unlocks h_k must put a letter ABOVE h_k onto h_k's β-face play at the right time: a HIGH copy (box 84's MIRROR);
  - a High that must unlock again after a re-lock alternates two monotone projection chains (GATE-RACE, box 91 §3); with disjoint pools
    POOL-ALT (box 85 §3) caps the alternations linearly, and a shared pool needs copies that MERGE into the same upper e's (SAME-E-MERGE),
    which latch (ACCESS-LATCH): box 86's LAG TOWER, DEAD at h = 2, 3.
- Not covered by a lemma: gates whose β-face play RETURNS through the gate (non-PRIV). There the decision is made by the β-route's own
  prefix before the gate (READING, §2), which can be low. This is exactly how MW's race gate flips (34 of 34 equal-Λ flips on MW8_2
  are non-PRIV) and how WC cascades; it is box 84's LIVE-BREAK / SELF-MIRROR case at a gate. DATA: linear on every instance.
- (2) Not built: the kill transfers, so per the brief no second-vertex design is built.
- (3) **CONJECTURE WAIT-CLOSED (§3)**: no waiting-High design in the classes below gives C (or A*, T3) super-linear in N + M; each class
  with the lemma or DATA that kills it.
- DATA (§4; two engines IDENTICAL on all 11 instances): GATE-LOW-NULL's counters 0 (glnfail, decfail); changes BELOW a gate's e-vertex on
  equal-Λ PRIV steps are frequent (lowch up to 599 on DHIB26_2804) and NEVER flip the gate (lowflip 0). Control (π := the part below e_o):
  glnfail 26 on C6G8_n54. On FW, MW, WC no flip is decided by the upper projection: FW's are all Λ-flips (the clock), MW's and WC's are
  Λ- or non-PRIV flips. The only families with growing counts here use the two routes the lemma leaves open, and they are linear.

## 1. Lemma GATE-LOW-NULL (PROVED, lane; premises [OPT], F3, (E-DOM), (Core), LOC-GATE3, NO-TIE3, E-MON3)
Let o be a gate with e-vertex e_o and faces p_e (whose play is p_e, e_o, wt(e_o), …) and p_b. For a set X of e-vertices let
π(X) := {f ∈ X : f is at least as relevant as e_o}. Call t a LAM step if Λ_t(p_e) = Λ_t(p_b) and a PRIV step if e_o ∉ E_t(p_b) (PRIV_g: p_b's play does not pass e_o).
(a) At a LAM ∧ PRIV step with e_o ∈ E_t(p_e): Ω_t(p_e) ▷ Ω_t(p_b) ⟺ π(E_t(p_e)) >lex π(E_t(p_b)), and π(E_t(p_e)) ≠ π(E_t(p_b)).
(b) If t − 1 and t are LAM ∧ PRIV steps and o flips at t, then π(E(p_e)) or π(E(p_b)) changes at t.
Proof.
- (a): e_o ∈ E_t(p_e) \ E_t(p_b), so the symmetric difference of the two e-sets is non-empty and its most relevant element z is at least as
  relevant as e_o; z is also the most relevant element of π(E_t(p_e)) Δ π(E_t(p_b)), on the same side (box 85 (PROJ)). With equal Λ,
  [VJ] decides by the most relevant vertex of the symmetric difference of the plays; vertices more relevant than an e-vertex are e-vertices,
  c_W, K0, K3 (E-DOM), c_W is in no play's set, and K0 / K3 lie on both plays or on neither ((Core), equal Λ). So that vertex is z, even:
  the side holding z wins. That is the π comparison.
- (b): Odd plays the ◁-smaller face (LOC-GATE3, NO-TIE3). Add the hypothesis that e_o is more relevant than Λ at t − 1 and t (then
  e_o ∈ E_s(p_e), since p_e's play starts with e_o). By (a), Odd's choice at s ∈ {t − 1, t} is a function of (π(E_s(p_e)), π(E_s(p_b))).
  If neither changes, the choice does not, so o does not flip. ∎
- Scope note: (b) is PROVED with «e_o above Λ»; the tool's LAM ∧ PRIV test does not require it (it is weaker), and glnfail is 0 on that
  larger set too (DATA). If e_o lies below Λ, non-e vertices (β's, lengths) can decide, and the lemma says nothing.
- Corollary GATE-LOW-NULL for designs: a letter less relevant than e_o, entering or leaving either face's play, never flips o on LAM ∧ PRIV
  steps. With box 91's TRIGGER: an unlock of h_k is a Λ-change of p_b, or (PRIV) the entry of a letter ABOVE h_k on p_b's play, or (non-PRIV)
  a change on a β-route that returns through qh_k.
- DATA (gate92.py; unit: (gate, t) over the whole run; set: box 91's 11 frozen instances; scope: own to the end, cap 3000; g3 to the first
  fallback, cap 20000; TOTALS): decfail 0, glnfail 0 on both engines; control CTRL=low (π := the part strictly below e_o) glnfail 26 on
  C6G8_n54 (fires).

## 2. The non-PRIV gate (READING; the case the lemma leaves open)
- Non-PRIV at t means p_b's play passes e_o, i.e. it passes o itself with Odd on p_e (e_o's only in-edge comes from o's e-face). Then p_b's
  play is A · o · (p_e's play), where A is the β-route from p_b back to o, and E_t(p_b) = E(A) ⊔ E_t(p_e). The two faces differ by A
  alone: Odd stays on p_e while A carries an e-letter above Λ, and the comparison is decided inside A otherwise, i.e. by letters that can
  be BELOW e_o. To flip to p_b, Odd closes the cycle A · o · p_b: Λ of p_b becomes that cycle's top (box 84 LIVE-BREAK: Odd breaks the
  returning cycle when it can).
- For the waiting High: a non-PRIV β-route of qh_k returns through qh_k, so the trigger route carries h_k itself; if it runs through the
  race at u into qh_(k−1) it carries h_(k−1) as well (box 91 WAIT-TRIGGER). MW's race gate is non-PRIV on all its equal-Λ flips and is
  linear (maxflip 4n + 2, box 91 §3). I have no lemma for this case: it stays inside the CONJECTURE's scope with DATA only.

## 3. CONJECTURE WAIT-CLOSED (and the lemma or DATA that kills each class)
CONJECTURE WAIT-CLOSED: on N5′-xi runs from S3 on Γ3 (and IDEAL-CYC from the genome's start), no genome whose counter is built from
waiting Highs (letters h_1 ≺ … ≺ h_n at gates, unlocked by a trigger reading a lower race) has A* (box 91), C or T3 super-linear in
N + M. Its scope is the union of the classes below; outside them (e.g. counters at movers with SET options, boxes 83-89) it says nothing.
| class | what unlocks h_k | killed by | status |
| --- | --- | --- | --- |
| K1 clock | a Λ-change of the β-face (Even-winning cycle reached) | box 91 TRIGGER (α): ≤ n − 1 Λ-changes per face per run, never undone | PROVED bound; FW, MW linear (DATA) |
| K2 own continuation | a vertex on h_(k−1)'s W-continuation | box 90 SUPERSET / box 91 PARALLEL: cascade, h_(k−1) never expelled | DEAD (WC, DATA) |
| K3 the race's own route | u's switch reaching h_(k−1), seen through u's play | box 91 WAIT-TRIGGER: the trigger route carries h_(k−1); plus GATE-LOW-NULL: h_(k−1) ≺ h_k cannot unlock h_k on PRIV steps | PROVED (lane) |
| K4 low copy | a second vertex with a letter below h_k | GATE-LOW-NULL (this box) = box 85 LOW-NULL at a gate | PROVED (lane) |
| K5 high copy (fixed offset) | a second vertex with a letter above h_k | box 84 MIRROR (too-early resets), box 85 §5; re-unlocks need alternation: GATE-RACE + POOL-ALT (disjoint pools ⇒ linear) | linear (DATA, box 84-85); POOL-ALT PROVED |
| K6 lagging merged copy | a copy that merges into the same upper e's one count behind | SAME-E-MERGE + ACCESS-LATCH (box 86): a merged waiting hub latches | DEAD at h = 2, 3 (DATA); open at h ≥ 4 |
| K7 non-PRIV gate | a β-route returning through qh_k (decided by its own prefix A) | none; LIVE-BREAK picture (§2) | DATA only: MW, WC linear |
| K8 β / P-decided (non-SET) re-arm | switches decided by β's or lengths, not e-sets | L-RED R223-q2 P-QUIET (closed the Q2 route, box 86 header) | closed by L-RED (cited, not re-checked here) |
- Weight: K3, K4 PROVED; K1 a PROVED bound; K2, K5, K6 (h ≤ 3), K7 DATA; K8 cited. The CONJECTURE is as strong as its weakest rows:
  K6 at h ≥ 4 and K7 are the places a waiting-High counter could still hide. A kill needs a family there; a proof needs a lemma for the
  non-PRIV gate (a gate-level LIVE-BREAK bound) and one for merged copies at every height.

## 4. DATA table (gate92.py; both engines IDENTICAL on every row; TOTALS over (gate, t); out/own92.out, out/g392.out)
Columns: gates = Odd vertices with an e-face; flips; f_lam (a Λ of the two faces differs at t − 1 or t); f_np (non-PRIV at t − 1 or t);
f_up (LAM ∧ PRIV flips, decided by a π change: the lemma's case); lowch (LAM ∧ PRIV steps where a face's e-set changes only below e_o);
lowflip (flips at those steps; must be 0); decfail, glnfail (must be 0).
| instance | N + M | gates | flips | f_lam | f_np | f_up | lowch | lowflip | decfail | glnfail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WC4_2 | 60 | 40 | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| WC16_2 | 216 | 148 | 15 | 0 | 15 | 0 | 0 | 0 | 0 | 0 |
| FW8_2 | 371 | 248 | 8 | 8 | 0 | 0 | 0 | 0 | 0 | 0 |
| FW16_2 | 787 | 528 | 16 | 16 | 0 | 0 | 0 | 0 | 0 | 0 |
| MW8_2 | 261 | 177 | 42 | 8 | 34 | 0 | 0 | 0 | 0 | 0 |
| MW32_2 | 957 | 657 | 162 | 32 | 130 | 0 | 0 | 0 | 0 | 0 |
| C6G8_n54 | 204 | 150 | 73 | 19 | 13 | 41 | 112 | 0 | 0 | 0 |
| RWX_n95 | 328 | 233 | 69 | 5 | 7 | 57 | 87 | 0 | 0 | 0 |
| DWT20_2803 | 364 | 262 | 79 | 0 | 26 | 53 | 275 | 0 | 0 | 0 |
| DHIB26_2804 | 400 | 292 | 148 | 3 | 41 | 104 | 599 | 0 | 0 | 0 |
| DHIB18_2805 | 400 | 301 | 158 | 24 | 27 | 107 | 396 | 0 | 0 | 0 |
- Instances: box 91's frozen copies (experiments/si/box91/inst/SHA1SUMS). Control (own, CTRL=low): MW8_2 glnfail 0 (it has no f_up flips);
  C6G8_n54 glnfail 26, lowflip 26.
- READING: the hand-built families (FW, MW, WC) flip gates only by Λ (clock) or non-PRIV routes, never by the upper projection; the climbed
  genomes do use upper-projection flips (41-107), but their counts stay small (A* ≤ 6, box 91). The low parts change hundreds of times
  without flipping a gate: the lower race is invisible to the gates above it, as the lemma says.

## Addendum 1 (appended 2026-11-09, date -u in the commit; L-RED 62 R228-box91 findings F1, F2, relayed by the Lead 00:25Z)
### A1.1 (γ) at a second vertex: a LENGTH-ONLY trigger (F2; the design the Lead asked to try first)
- Design question: a second vertex u2 whose switch changes h_k's β-face play only in its length or in low (non-e) vertices, timed to the race
  at u, so that h_k unlocks without any letter (case (γ) of box 91 TRIGGER).
- Lemma GATE-LOW-NULL (b) (§1) excludes it on every PRIV step with e_(h_k) above Λ, and the proof covers (γ) directly: Odd's choice is a
  function of the two projections π(E(p_e)), π(E(p_b)), and a length-only or low-vertex change leaves both unchanged, so the gate does not
  flip. With equal Λ that is every step of the waiting design in which h_k's β-face does not return through qh_k.
- What is left: (γ) on a non-PRIV gate (the β-route returns through qh_k; §2), i.e. class K7, and (γ) where e_(h_k) lies below Λ (then
  h_k is in no e-set above Λ, so it is not a letter of any counted high part: no counter). So (γ)-at-a-second-vertex adds no new open
  class; it is K7 again. I did not build it: on PRIV steps it cannot fire by a PROVED lemma, and its non-PRIV form is K7's open case.
- DATA: box 91 counter fl_len (flips whose left face changed only below every e-letter; unit: flip, TOTAL) = 0 on all 11 instances, both
  engines; box 92 glnfail 0 (it counts (γ) flips on LAM ∧ PRIV steps as failures too).
- Row added to §3's table: | K9 length-only trigger at a second vertex | a change of the β-face below every e-letter | GATE-LOW-NULL (b) on
  PRIV steps; non-PRIV ⇒ K7 | PROVED (lane) on PRIV; K7 otherwise |. CONJECTURE WAIT-CLOSED's scope now includes K9.
### A1.2 A*_all (F1)
- Box 91's «maxa» is A*_route (route vertices only); the corollary's A* is A*_all (all vertices). Tool experiments/si/box92/astar92.py
  (unit (v, I, z); per-tuple MAXIMUM; cfail = #(v, I, y) with c_y > a_y, must be 0). Records out/astar92_own.out, out/astar92_g3.out (both
  engines IDENTICAL). Table and restated claims: box 91 Correction 1.
- Effect on WAIT-CLOSED: the conjecture is stated for A*, C, T3; with A* := A*_all it must read «A*_all super-linear» for the counter's
  growth — but A*_all ≥ C can grow linearly with C bounded (FW: A*_all = d, C = 3), so the meaningful targets stay C and T3; A*_all is
  listed as an upper quantity only.
