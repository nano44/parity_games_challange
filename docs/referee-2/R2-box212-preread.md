# R2-box212-preread: PRE-READ (NOT A SIGNATURE) of L-NEW 74's box 212 RF-LEVEL (§2 READING, RF-A, RF-B, RF-C, RF-D, kill criteria) with its Addendum A
REFEREE-2 successor 40 (session_01V5yGRWQ1pY9BpJ6WvVvBoi; Opus 5.5 under D1 / D21 / L53). D1: «A claimed polynomial algorithm is far
more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.»
Date -u at writing: 2026-11-13T03:32Z. Lead brief item C (the form of R-box209-preread / R-WRAP-preread).
This is a read to find errors early and to list what a packet would need. It is NOT a referee signature: nothing is frozen as a packet,
the lane labels RF-A, RF-B, RF-C CANDIDATE and RF-D CONDITIONAL, and a packet review, if one comes, is a separate signature.

## 0. Verdict (pre-read)
| statement | what I did | finding |
| --- | --- | --- |
| §2 READING (ten landed static lemmas hold at every state / standard state; CN2, CN2-3 at every positional pair) | read each proof at its pinned lines | AGREE for all ten (§3). For a packet: the extended forms are NEW statements (to sign), not landed ones (item K-1) |
| RF-A (i)-(iv) | re-derived | no gap found (§4) |
| RF-B (P1), (P2), (P4), (P5′) | re-derived | no gap found (§5); note N-1 (H_Y is a game) |
| RF-C and its approved form (A1) | arithmetic re-derived | both valid (§6); note N-2 (the Howard remark: ALL-TCYC needs the two separate bounds, not W in T ≤ P + (P + 1)·W) |
| RF-D (CONDITIONAL on [IMP3], [L3]) | hypotheses traced; SPEC read; own N5 engine | the inequality is RF-C on Γ3 (valid under [L3]); GAP G-1: «each window a run of the KEY rule on a closed one-player sub-game» does not follow from RF-B, and in the reading «SPEC run on the window game» it is FALSE on all five towers at every state (DBL4 state 0 first; §7); G-2 (side claim «O1 … the whole run is one window» unproved) |
| kill criteria (A2) and the (iii) evaluation (A3) | own re-count with my own Ξ-feedback search | numbers equal (§8); note N-3 ((iii) is weak by design) |
| DATA | own replay, own engines, seven rules + controls; second engine for N5 on Γ3 | rule-free counters 0 on 4,766 checked runs (frozen, mutants, random × 7 rules), every control fires; T_key = F − 1 on 86 of 86; box 213's counters equal on 86 of 86; note N-4 (§9) |
Labels I would keep: RF-A, RF-B, RF-C CANDIDATE (no gap found by this pre-read); RF-D CONDITIONAL for its inequality only; its window
clause is not a consequence (G-1: false in the «SPEC on the window game» reading, open in a τ-arena form that nobody has stated). Not N5, not N5′-xi, not M3, not M4; **G-N5-TIME stays OPEN.**

## 1. Object, inputs, independence
- Object: claude/l-new be167574 (on origin/claude/l-new, checked with merge-base --is-ancestor), docs/new/N5-RFLEVEL-box212.md, sha1
  a08432e0956fa13061781cad9ef72fa79c9ad310, 37,215 B, 315 lines (body l. 1-268, Addendum A l. 270-315). Tools experiments/new/box212/
  (read, never imported): kill212.py and the frozen lines out/rfd212_frozen.out, out/rfd212_tower_spec.out; inst/ (5 towers, sha1s equal
  to inst/SHA1SUMS, checked).
- Read for this pre-read: the box; P-N5-LEVEL (l-new 1e6df499, sha1 7c956df443cfddbf23bfbaa18a26a98369b176ec: §2-§5, §7, §8; my
  predecessor's R2-P-N5-LEVEL.md is my lane's second review of it); at trunk 7fa6aff4 docs/new/P-N5-QUIET.md (sha1 066dfc7d…), P-N5-QUIET-
  fixes.md (cd3581f7…), P-N5-CHAIN.md (6e613ba7…), all three equal to the box's pins; RESULTS R15, R118, R123 at trunk e8b6abf0; box 209
  (l-new 3f896099) §3 statement lines (L1′)-(L5′) only; SPEC docs/new/N5-ssi-global.md at trunk e8b6abf0 (sha1 66fde9ef…), l. 8-9, 32,
  47, 50-57; with the Lead's leave (02:52Z), lane DATA of box 213 (claude/l-new 565b6d28): notes/L-NEW.md «BOX 213» and «Dead ends
  (successor 74, box 213 start)», experiments/new/box213/arena213.py and out/arena213_frozen.out (read, not imported).
- NOT read before this pre-read is on origin: L-RED 68's R239 (claude/l-red 2cc894f2, docs/red/R239-rflevel.md), any docs/referee/ file
  on box 212, L-RED-B's records on box 212, the lane's rf212.py / rfd212.py (my counters are written from the box's text). Agreement
  section to follow (Addendum 1) after the push.

## 2. Premises, landed or not (by script: R2-box212/r2prem212.py at trunk e8b6abf0, output r2prem212.out; quotes: r2q212.py)
| premise | used by | status (script) |
| --- | --- | --- |
| R15 (a) Lemma A (F1 for ANY non-empty unambiguous set of improvements) | RF-A (K1), every rule | LANDED |
| R118 (a) IDEAL-CYC (the game), (i) BR-SEG-G | setting; Howard remark of RF-C only | LANDED |
| R121 E-DOM | (K2) | LANDED |
| R123 CN2, B-ONLY, NO-TIE, LOC-GATE, LOC-K2 | (K2)-(K4), (L2), (L3), (P4), tail clause | LANDED as stated; the every-state form is §2's READING (§3 below) |
| R126 QUIET-N | Howard remark of RF-C only | LANDED |
| R117 Γ3, R124 standard states, R125 CN2-3 … NO-TIE3, (Core) | RF-D | LANDED; every-standard-state form = §2's READING |
| P-N5-LEVEL (l-new 1e6df499): (K1)-(K4), (L1)-(L3), (L5), (C1), (C2), PLATEAU (P1), (P2), (P4) | RF-A, RF-B, RF-C (proofs re-used line by line) | NOT LANDED (highest trunk id R127; two referee verdicts on the packet, landing routed by CHECKER as R129) |
| box 209 (l-new 3f896099) (K0′)-(K4′), LEVEL3 (L1′)-(L3′), (L5′) | RF-D [L3] | NOT LANDED (lane CANDIDATE; REFEREE 33 pre-read only) |
| box 104 W-FLAT and §8 «τ never changes» (claude/l-si 26704e01) | RF-D [IMP3] | NOT LANDED (lane, «PROVED there», not refereed) |
| Lean, claude/l-formal 78c32d90 (IdealImpRun, ImpNonStall, ImpK5New, …) | cited only | lane («Lean-checked (lane)»), CONDITIONAL on F1 per its INDEX; never the proof of record (the box says so) |
- Quotes: every «…» on a [Q …] bullet or paragraph of the box (30) found verbatim (whitespace-normalised, «…» elisions as pieces) in the
  named R-entry at trunk 7fa6aff4 and again at e8b6abf0, or in the named file at its pinned commit: «quotes 30 missing 0»; control (one
  character altered per piece): «quotes 30 missing 30». Same count as the lane's quotes212.out. The verbatim Lead / successor-73 texts
  of Addendum A (A1, A2, A4) are in no file and cannot be checked by script (the box says so).

## 3. The §2 READING, re-read (each proof at the box's pinned lines, trunk 7fa6aff4)
I re-read the ten proofs and agree with every row of the box's table, with the deciding lines as quoted:
- CN2 (P-N5-QUIET l. 79-86): shape only (a cycle through a mover passes a gate, through a gate a face of priority ≥ 6, else all ≥ 2). It
  never names a state or a strategy; it holds for every positional pair of Γ(G) (the box's «narrower than its proof» is right; RF-A needs
  only the states of IDEAL-CYC, which the landed text covers).
- LOC-GATE (l. 89-111): one positional pair (σ_t, σ̄_t), the switched Odd strategy τ, [OPT] at that state, F3, F4′, CN2. Cases 1, 2-i-a,
  2-i-b, 2-ii-a/b/c compare plays of ONE pair. The words «of a run» in the statement are not used.
- LOC-K2 (l. 113-116): the freeze of K1 and [OPT] at the state. B-ONLY (fixes l. 11-25): τ_β, [DEF]'s shape, E-DOM, «K0 → K3 → K2
  frozen», [OPT] at the state, [VJ] rewards first. NO-TIE (l. 26-29): B-ONLY at the state and the shape of plays.
- CN2-3, LOC-GATE3, LOC-K2-3, B-ONLY3, NO-TIE3 (P-N5-CHAIN §2 (P), (Core) l. 93-97, §5 l. 170-212): the same arguments on Γ3 with pads;
  (Core) is stated «In standard states and in HOW3». A HOW3 state is «the frozen part plus a choice at every mover», with the frozen part
  the standard state's (R125 §2) — so «every state» there = every mover choice with the non-movers at S3's standard choice.
- Where I would be careful (item K-1): R123's own header defines IDEAL-CYC with «Howard steps at the movers», and LOC-GATE says «a state
  of a run of IDEAL-CYC(G)». A reading of a proof does not change what a landed entry states. A packet should STATE the ten lemmas in the
  every-state form as its own statements (e.g. «STATIC-10»), with the reading as their proof («the landed proof at <lines> uses no
  property of the run: …»), so that referees sign the extension; it should not cite R123 / R125 for more than they state.

## 4. RF-A, re-derived
Setting checked against the box: an improving run changes σ at a non-empty set I_t of movers, each to a gate y with Ω_t(y) ▷ Ω_t(σ_t(x)).
- F1: I_t is non-empty and unambiguous (one switch per mover); each switch is to a successor of strictly larger value, which is VJ00
  §4.4's improvement at a mover (a mover has priority 0 and is never a cycle node, CN2, so comparing the successors' values is the same
  as comparing ext(x, ·) of them, F4′). R15 (a) then gives Ω_t ⊴ Ω_(t+1). This is the reading P-N5-XICYC already uses for Howard's set
  («so I is non-empty and unambiguous (one switch per vertex).»); nothing in it uses Howard's choice.
- (K2): the proof (P-N5-LEVEL §3) uses (VJ-1), (VJ-2), E-DOM, the c_W self-loop, (D3) and LOC-K2 at each of the two states separately;
  «As Λ = Λ′, K0 and K3 are in both of Π, Π′ or in neither» is decided at each state by «enters the core iff cycle node K1». Valid for
  any two states of any run, hence of an improving run. (K3) (a)-(e) and (K4): static at one state (B-ONLY, NO-TIE, LOC-GATE, LOC-K2,
  (K2) at one state). The box's «weak point (K2) at two different states of a non-Howard run»: I find nothing that depends on the rule.
- (K1) from F1 + (K2) outside the core, (K3 (e)) on the core: correct; it is the packet's own remark, and Lean's ImpK1Statement (lane).
- (ii) (L1) uses only (K1); (L2) (K3 (c)-(e)); (L3) (K3), (K4) at b, CN2, (D4); (L5) (L2), (L3). Re-read: none uses (K5), (L4) or the rule.
- (iii): with t_1 < … < t_q the non-stall steps with t_i < b, LAG_(t_i) ≠ ∅: LAG_(t_(i+1)) ≠ ∅ and LAG only shrinks give LAG_(t_i + 1) ≠ ∅
  for i < q, so Φ_(t_i + 1) > Φ_(t_i) (L1), and stalls keep Φ: Φ_(t_(i+1)) ≥ Φ_(t_i + 1) > Φ_(t_i). q distinct values, q ≤ P (L5): every
  m_t is class_b of one of the M gates (α) or (c, ∅) for one of the M β-vertices (β), and 1 ≤ |FRONT_t| ≤ N + 2M (movers N, gates M,
  β-vertices with a mover successor ≤ M). P = 2M(N + 2M). Correct.
- (iv) K5-NEW: class_(t+1)(x) = class_(t+1)(σ_(t+1)(x)) ((K3 (c)) at t + 1; x is not an e-vertex) ≥ class_t(σ_(t+1)(x)) ((K1) at the
  gate). Correct; it uses no improvement beyond (K1), and it is weaker than (K5) exactly as the box says (one gate, the new one).
- The box's list of where Howard enters ((K5) for every gate, (L4), (P3), (P6), (P7)) is complete for §3-§5 and §7 of P-N5-LEVEL; also
  Howard-only, and not used by RF-A: (C3)'s Ξ-cycle (from (L4)), (C4) (QUIET-N), WIN, R-HEIGHT, K1-TCYC, FVS-TCYC, ALL-TCYC.

## 5. RF-B, re-derived ((P1), (P2), (P4), (P5′))
Setting: an improving run, reference b, a maximal interval [u, v], u < v, of constant Φ = (m, −|J|); every step inside is a stall (a
non-stall step raises Φ or empties LAG, (L1)), so FRONT_s = J and class_s = m on J for s ∈ [u, v]; LAG_v ≠ ∅ so v < b. Y := {x :
class_u(x) ≤ m}.
- (P1) x ∈ Y lagging at u: m ≤ class_u(x) ≤ m, so x ∈ J, class m on [u, v]. x ∈ Y not lagging at u: class_u(x) = class_b(x), and (K1)
  squeezes class_s(x) = class_u(x) for u ≤ s ≤ b. x ∉ Y: class_u(x) > m and (K1). Rule-free (uses (K1) and (L1) only).
- (P2) class_s(s_s(x)) ≤ class_s(x) for every x ((K3 (c)) non-e-vertices; (K3 (d)) e-vertex with mover successor; (K3 (e)) e-vertex
  with successor c_W: equal), so s_s(x) has class ≤ m at s, i.e. s_s(x) ∈ Y by (P1). For a mover, s_s(x) = σ_s(x). Rule-free.
- (P4) gate g ∈ Y: the chosen face has g's class ((K4); NO-TIE + LOC-GATE make the choice the unique strictly ◁-smaller face, so ANY
  pointwise-optimal reply chooses it), hence lies in Y. Case (1) one face outside Y: by (P1) outside at every s, class > m ≥ class_s(g),
  never chosen. Case (2) both in Y, classes different: constant (P1), lower one chosen. Case (3) equal classes: e_g's successor is not
  c_W (else class (c_W, ∅) > m, the largest class, and m is a lagging class, below some class_b), so it is a mover; e_g ∈ E_s(e_g) =
  E_s(β_g); β_g's play passes e_g, enters it only from g (D1), so σ̄_s(g) = e_g. K2: LOC-K2. Rule-free.
- (P5′) H_Y: movers of Y keep their gates IN Y, every other vertex of Y keeps s_u(x). Note N-1: H_Y is a game (every vertex of Y has a
  successor in Y): a mover x ∈ Y has σ_u(x) ∈ Y (P2); a non-mover has s_u(x) ∈ Y (P2). For s ∈ [u, v] the non-movers of Y have s_s(x) =
  s_u(x) (gates (P4), K2 LOC-K2, the rest frozen), and σ_s(x) ∈ Y for movers of Y, so the play of x ∈ Y under (σ_s, σ̄_s) uses only H_Y's
  edges; relevance order and parities are Γ(G)'s, so the VJ value of x in H_Y under σ_s|Y (Odd has one strategy) is Ω_s(x). For u ≤ s <
  v, a mover x ∈ Y with σ_(s+1)(x) ≠ σ_s(x): σ_(s+1)(x) ∈ Y ((P2) at s + 1 ≤ v), and Ω_s(σ_(s+1)(x)) ▷ Ω_s(σ_s(x)) (the run is improving);
  both gates are in Y, so these are H_Y values at σ_s|Y: a strictly improving switch of H_Y. Correct.
- What (P5′) gives and what it does not: the steps of the run restricted to the movers of Y are identity steps or non-empty sets of
  strictly improving switches of H_Y. It does NOT say that they are the steps of the SAME rule run on H_Y. For three rules whose choice
  at a mover is fixed by the order of the Ω_s values of its gates (Howard / all-switch best, «every improvable mover to its least better
  gate», «the least-index improvable mover to its least better gate») it is true modulo idle steps, by a two-line argument: a choice
  made in Γ(G) inside a plateau lies in Y ((P2)), and among the gates in Y it is the same extremum (and a lower-index mover of Y that
  is not improvable in Γ(G) is not improvable in H_Y). My replay checks exactly this (rec_restrict_diff, §9). For a rule whose choice
  depends on vertices outside Y, it is open; this is what G-1 (§7) is about.

## 6. RF-C: the arithmetic, re-derived
Reference b := T, a := 0. Let the states with LAG ≠ ∅ form the q maximal intervals [u_i, v_i] of constant Φ (one per value of Φ, which
never falls) and b′ the first state with LAG = ∅. (C2) (rule-free: (L1)): b′ = q + Σ_i (v_i − u_i), the q steps v_i → v_i + 1 being the
non-stall steps; q ≤ P (RF-A (iii)). Put λ := max_i (v_i − u_i) (the longest plateau; 0 if none) and tail := T − b′.
- Body form: with W := max(λ, tail), T = q + Σ_i (v_i − u_i) + tail ≤ q + qλ + tail ≤ P + P·W + W = P + (P + 1)·W. Valid.
- Form of record (A1), «T ≤ (P + 1)(λ* + 1) + (tail)»: T ≤ P + Pλ + tail ≤ (P + 1)(λ + 1) + tail (slack λ + 1). Valid whether λ* is read
  as the longest plateau or, as in the body, the longest window including the tail.
- Tail clause (classes constant on [b′, T] by (K1) squeezed between b′ and T; every gate keeps its face: different face classes →
  (K4); equal classes → e_g's successor is a mover (else β_g has class (c_W, ∅), Λ(β_g) = c_W, against B-ONLY, β_g not excepted) →
  P-N5-LEVEL (P4) case (3)'s argument, which is static; K2 by LOC-K2): correct. So the tail is RF-B's kind of window with Y := V.
- Howard (note N-2, wording): plateaus ≤ N + 2M + 5 (PLATEAU) and tail ≤ N ((C4) / QUIET-N) give T ≤ P + P(N + 2M + 5) + N = P(N + 2M +
  6) + N = ALL-TCYC. Substituting W = N + 2M + 5 into the body's displayed form gives P(N + 2M + 6) + N + 2M + 5, and (A1) gives P(N + 2M
  + 6) + N + 2M + 6: «the same count is ALL-TCYC's» holds of the decomposition with the two bounds kept apart, not of the displayed
  formulas. Check at M = N = 1: P = 6, ALL-TCYC 55 (= P-N5-LEVEL §8's value), body formula 60, (A1) 61.
- RF-D's constant P3 = 2M(N + 4M): from box 209's (L2′) (FRONT ⊆ movers N, m-pads M, gates M, pads pβ_g M, β-vertices with mover
  successor ≤ M: |FRONT| ≤ N + 4M) and (L3′) (m_t is class_b of an m-pad, M values, or (c, ∅) for a β-vertex c, M values). Correct from
  those statement lines; box 209 is not landed.

## 7. RF-D: the hypotheses, and gap G-1
- [IMP3], traced: «visits only standard states» and «takes R's pick in A(x)» are W-FLAT (box 104 §7, lane, not refereed); «non-empty»
  is R15 (d) (landed) with box 104 §8 «τ never changes» (lane). The box's READING «Ξσ's order on Γ3 is Ω_t's» is SPEC's definition: SPEC
  (trunk e8b6abf0) l. 32 «Ξσ = valuation of every vertex under σ and Odd's OPTIMAL counterstrategy σ̄ (minimising this order at every
  vertex at once).» and S2, l. 47 «Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v), Ξσ(w) strictly better than Ξσ(σ(v))}», with R125 §2's «Ω_t
  := the [VJ] value against σ̄_t ([OPT])». A packet can cite these instead of a reading. Non-movers do not change: ESC3-ALL (R125, P-N5-
  CHAIN §3: «every pointwise optimum of H agrees with σ at every Even vertex that is not a mover»).
- [L3]: box 209 (not landed); the box says box 209's (K1′) is proved from F1 + (K2′) «(box 209 notes; E-MON3 not used)». A packet must
  carry that proof in a file it pins (box 209's text or its own), not in notes.
- The inequality T_key ≤ P3 + (P3 + 1)·W_key: RF-C's arithmetic on Γ3, valid under [IMP3] and [L3]; «O1′ iff W_key ≤ poly» is then
  immediate (⇐ by the inequality, ⇒ since W_key ≤ T_key ≤ F). No gap there.
- **GAP G-1 (the window clause), with DATA that decides it in one reading.**
  - Claimed: «where every window is a run of SPEC's key rule on a closed one-player sub-game of Γ3(G) whose classes are frozen», and
    from it §0.5 / §6 «So O1′ (KEY-CYC) is equivalent, up to the polynomial factor P3 + 1, to a bound on the key rule inside such
    windows», «a generalised O1».
  - What carries over (under [IMP3], [L3]): RF-B on Γ3 — on a window [u, v] the set Y is closed, classes on Y are frozen, Odd's choice on
    Y is σ̄_u's, and N5's steps restricted to the movers of Y are identity steps or strictly improving switch sets of the one-player
    game H_Y (Odd's single strategy σ̄_u|Y, non-movers at s_u). RF-C's inequality and «O1′ iff W_key ≤ poly» need nothing more.
  - The step that fails: the identification of those steps with «SPEC's key rule» run on that sub-game. SPEC run on H_Y has τ = σ̄_u|Y
    (Odd has no other strategy) and Iσ = N5's Iσ restricted to Y (same values, SPEC l. 32, 47), so its Even step is S4a with Odd fixed
    at σ̄_u. N5's Even step is S4a (SPEC l. 51-53) with Odd fixed at N5's own τ: «σ_new = Odd's optimal counterstrategy (S1 procedure)
    in the dual of H to the dual-Even strategy τ, read as an Even strategy of G. (Even's one-player optimum against τ among "keep or
    take an improving edge".)», and on Γ3 before the first fallback τ is TAU3 (P-N5-CHAIN §3: «In H, Odd plays τ: pe at every gate,
    K2 → K2»), not σ̄_u. Two arenas, two optima; nothing in the box relates them.
  - DATA (own engine r2keywin.py on REFEREE-2's R2-P-N5-END SPEC primitives; §9): on the five towers the whole run before the first
    fallback is one window with Y = V (the box's own rfd212 lines: «tail» = T, no Φ value), so H_V is Γ3 with Odd fixed at σ̄_u = σ̄_t
    (tail clause) and the non-movers at σ_t. SPEC's S4a on H_V differs from N5's step at EVERY state: 741 of 741 states, 7,358 (state,
    mover) differences; first instance DBL4_d20_F30.json (box212/inst, sha1 a0cde809…), state 0, mover vertex 8 of r2end.build's
    indexing: σ_0 = gate 549, N5 → 548, SPEC on H_V keeps 549. Per tower: DBL4 30/30 states (178), RECF4 67/67 (478), H5 136/136 (1,152),
    H6 209/209 (1,627), HIT7 299/299 (3,923). Control (the same arena with Odd at τ): 0 differences on all 741 states. So in the reading
    «SPEC run on the window game» the clause is FALSE, instances named; the box's towers, offered as the vacuous control of RF-D, are
    where it fails. (On the 81 frozen genomes the windows are at most 1 step and the tails at most 4; there N5's step differs from the
    σ̄-arena step at 1,641 of 1,721 states, but I did not cut those runs into windows, so I give that number as context only.)
  - Repair options. (a) A τ-arena version of RF-B, with its own statements: H^τ_Y := the movers of Y with A(x) ∩ Y, Odd fixed at τ|Y;
    (P2^τ) τ(g) ∈ Y for every gate g ∈ Y (closure of Y under τ-plays; not implied by (P2), since τ's face can be the face outside Y of
    case (1)); (P5^τ) N5's step at the movers of Y = Even's optimum of H^τ_Y among «keep or improve», with improving sets still from
    H_Y. Then a window would be «a run of a two-arena rule (improving sets from the σ̄-game H_Y, the choice from the τ-arena)», as box
    213 frames N5 (L-NEW notes, claude/l-new 565b6d28: «TWO value systems»), not SPEC's key rule on a one-player game. (b) Or reword RF-D
    to the part that is proved: «each window is class-frozen and closed, and N5's own steps restricted to it are improving steps of H_Y
    (interleaved with idle steps)»; the open question is then «bound the length of N5's class-frozen windows», and «the key rule on
    one-player windows» / «a generalised O1» go.
  - DATA that would decide (a): on the windows of N5's run with Y ≠ V (the lane's rfd212 has the class machinery on Γ3): a counter
    tauclos [(window, s, gate g ∈ Y) with τ(g) ∉ Y] and a counter keytau [(window, s, mover of Y) N5's choice ≠ the optimum of H^τ_Y];
    both 0 on every window would support (P2^τ), (P5^τ); one non-zero kills that form (instance named). On the towers (Y = V) (P2^τ) and
    (P5^τ) hold trivially, so the towers cannot decide (a).
  - The same wording issue, weaker, in §4's last bullet («the rule's own run on the one-player game H_Y») and in (A1) («for another rule
    λ* is that rule's count on one-player frozen windows»): true for rules fixed by the order of the gates' Ω values (§5: Howard,
    «every improvable mover to its least better gate», «the least-index improvable mover to its least better gate»; my DATA §9:
    rec_restrict_diff 0), not shown for a general rule, and false for N5's own rule in the reading above.
- **G-2 (side claim, wording).** «(O1 is the Ξ-acyclic case, where the whole run is one window: the reduction says nothing new there)»
  is asserted, not proved; the support is DATA on the five towers (no vertex lags against the last state). Prove it or label it DATA.
- READING «F(G) … is T_key(G) plus a constant»: DATA with my second engine (§9): F − T_key = 1 on every genome I ran.

## 8. Kill criteria
- Of record: (A2) (verbatim Lead text; not checkable by script). The body's §8 points stay as additional points of attack; my §3 found no
  landed static lemma whose proof compares two states (body (ii)).
- (A3), re-counted with my own code (r2kill3.py: the lane's frozen rfd212 spec rows read by column name, MY Ξ-feedback search r2lv.min_fvs
  in place of fvs202): «Xi-cyclic 81 of 81 (Xi-acyclic 0); lam*_key >= T/2 on 17 (largest T among them 4); lam*_key < T/2 on 64; T >= 10
  on 31, of which lam*_key >= T/2 on 0; largest lam*_key 4; largest T 196; kill (iii) fires: 0»; own k: 33 with k = 1, 20 with k = 2,
  2 with k = 3, 26 with k ≥ 4 (not searched further). Equal to the lane's line. Control (λ* := T): «kill (iii) fires: 1».
  Also from the same rows: 1,721 steps, 2 stalls, longest plateau 1, longest tail 4, rule-free must-0 sum 0 (= §7 of the box).
- Note N-3: (iii) fires only if EVERY Ξ-cyclic genome of the sets has λ*_key ≥ F/2, so one short run prevents it; on the frozen set every
  Ξ-cyclic key run is short (T_key ≤ 196, windows ≤ 4) and the long key runs (towers, T_key up to 299) are Ξ-acyclic, where λ* = T by
  design. So «does not fire» shows the reduction is not vacuous on short Ξ-cyclic runs; it does not yet show anything about long ones. A
  packet's DATA would be stronger with Ξ-cyclic genomes on which N5's key run is long (e.g. towers with one Ξ-cycle added).

## 9. DATA: the box's DATA clauses, and my own replay (not to sign)
### 9.1 The box's DATA, by the DATA rule
- Each DATA clause of §0.6, §6, §7 and (A3), (A4) names its counters (the must-0 list of §7; tail, maxlen, T, stalls; K5how, platexit,
  platidle, plat_gt_movers, tail_gt_N, NSP), its sets (with seeds) and its source file (out/summ212.txt). Units are given only by
  reference («the tools' doc strings»): a packet should print each unit in the text (item K-8). The 9 timeouts and 1 OOM pair are named
  as not checked. Nothing asymptotic is supported or killed by DATA (L43); «at most 5 % of P» is descriptive.
- Re-counted from the lane's frozen lines with my code (§8): 1,721 steps, 2 stalls, longest plateau 1, longest tail 4, must-0 sum 0, and
  (A3)'s line: equal.
- The lane's weak point «no cross-check of the other rules' runs against a second engine»: §9.2 is one (own engine, own rule
  definitions), for the rule-free counters on Γ(G). For N5 on Γ3: §9.3.
### 9.2 Own replay of RF-A, RF-B, RF-C under seven improving rules (R2-box212/r2rf.py; engine R2-P-ACYC/r2acyc.py via successor 39's
R2-P-N5-LEVEL/r2lv.py, whose counters are reused unchanged; no lane code; outputs summed by sumrf.py into sweep_sum.out)
- Rules (own definitions, §3's setting): howard (r2lv's, tie max), allleast, allrand, subrand, onebest, oneleast, onerand. Rule-free
  must-0 counters: r2lv's cn2, bonly, notie, locgate, lock2, f1, opt, pistart, k1, k2, k3a-k3e, k4, l1, l2, l3, l3then, l5, c2, p1, p2,
  p4, and new: impfail (a step that is not improving), k5newfail (RF-A (iv)), nspfail (> P non-stall steps for one b), p5pvalfail and
  p5pimpfail (RF-B (P5′): H_Y's own valuation ≠ Ω_s on Y; a switch at a mover of Y leaving Y or not strictly H_Y-improving), tailfail
  (the tail clause), rfcfail (body RF-C), rfa1fail ((A1)). References b: every b when n·T² ≤ 3·10^7, else T and 6 random b.
| set | runs | rule-free FAILS | descriptive (records) |
| --- | --- | --- | --- |
| frozen 81 genomes (get_inst.py) × 7 rules, seed 4011 | 567 (566 checked: CW16_n under oneleast capped at T = 5,000) | 0 | max T 199 (howard, allleast, allrand), 547 (onebest), 462 (onerand), 301 (subrand); longest window W 13 (howard, allleast), 10, 51, 111 (oneleast), 47, 21; non-stall steps for one b at most 368 (oneleast) |
| own mutants (r2split.mutate) of BLKX26, CFI3, CW4_n, K1F21, K1L10, K1L7, MWR4_2, RINT, 25 each, seed 4031, × 7 rules | 1,400 | 0 | max T 115 (onerand); W ≤ 45 |
| random r2end.gen «any» seeds 4021-4023 (100 each) + «self» seed 4024 (100), × 7 rules | 2,800 | 0 | max T 27; W ≤ 12 (random genomes are tiny: my lane's trap, so they test little) |
| controls on the 20 smallest frozen genomes: --rule worsen; --rctrl k5t, nsp0, tailshift, rfc, hval (each must FIRE) | 6 × 20 | worsen 1,275 (f1 623, k1 375, k5new 71, p5pimp 78, l1 73, c2 32, impfail 18, l3 3, l5 2); k5t: k5new 175; nsp0: nsp 234; tailshift: tail 18; rfc: rfc 18; hval: p5pval 53,666, p5pimp 216 | all fire |
- Howard-only facts (descriptive under the other rules, as RF-A / RF-B predict; frozen set, units of r2lv): K5 (for every gate) 0 under
  howard and 192 (allrand) to 134,344 (oneleast); DOM 0 / 745 to 190,885; (P3) 0 / 2 to 916,561; (P6) 0 / 0 (allleast, allrand) to
  1,656 (onerand); (L4)'s map 0 / 1 to 189,511. QUIET-N's bound on the tail: 0 under howard; 1 run (onebest) on the frozen set.
- rec_restrict_diff (§5's claim for value-ordered rules: a non-idle plateau step on the movers of Y = the same rule on H_Y): 0 under
  howard (1,075 steps compared), allleast (841) and oneleast (26,995; 55,671 idle steps skipped) on the frozen set; also 0 on the mutants (howard 6,587, allleast 6,878, oneleast 92,935 steps) and random sets; under
  the hval control it fires (346): the comparison can see a difference.
- Not checked: CW16_n.json under oneleast (T ≥ 5,000, my cap; the lane also lost this pair to memory). Every other (genome, rule) pair
  of the frozen set ran to the end (no timeout at 1,500 s).
### 9.3 N5 itself on Γ3, second engine (R2-box212/r2tkey.py, r2keywin.py on R2-P-N5-END/r2end.py's SPEC primitives, e-order lev)
- T_key: my first-fallback iteration F equals the lane's T + 1 on all 81 frozen genomes and all 5 towers (r2tkey_*.out: «F-T distribution
  {1: 81}», «{1: 5}»). So «F(G) = T_key(G) + constant» holds with constant 1 on every genome checked (DATA for RF-D's READING).
- Box 213's arena probe, second engine: (T, moved, notbest) equal to the lane's arena213_frozen.out (claude/l-new 565b6d28) on all 86
  genomes; τ ≠ σ̄_t at every gate at every state of the towers (72,192 of 72,192 (state, gate) pairs) and at 596,317 of 608,455 on the
  frozen set. Note N-4: the lane's file has notbest > 0 on 38 genomes, not the «12 genomes» named in L-NEW's notes (the twelve named
  sum to 84 of the 187; the other 103 are on 26 more genomes, the largest DHIB18_2805 18, DSALT9_n416 12, DHIB26_2804 11, C6G8_n54 10,
  K1C16_n400 9). The dead end's conclusion («FALSE») is unaffected; its instance list is incomplete.
- G-1 (§7): N5's step versus SPEC's S4a on the window game (Odd at σ̄_t, non-movers kept): towers 741 of 741 states differ, 7,358 (state,
  mover) differences; control (Odd at τ): 0 of 741, and 0 of 1,721 frozen states (the frozen comparison: 1,641 of 1,721 states, 4,547 differences, context only, §7).

## 10. Genome-only steps, scope, TARGET.md diff
- Steps that use the genome's shape ([DEF] / R104), so RF-A..RF-D are statements about IDEAL-CYC / HOW3 on genome games only (the box
  says so, §9): CN2 / CN2-3 (priorities of movers, gates, faces); B-ONLY / B-ONLY3 (e-vertices even and above every β; c_W's in-edges;
  an e-vertex's only in-edge from its gate); E-DOM; (D1) (P4 case (3), tail clause); (D3) core entry at K0 ((K2)); (D4) c_X ((L3));
  (K3 (e)) the fixed classes; (L2)'s kinds and (L5)'s count «M gates, M β-vertices»; RF-D's pads and (Core).
- TARGET.md (v1.0, trunk e8b6abf0) §2 (M4) is not claimed; no algorithm and no running time is claimed (§3's bit-cost rule does not
  arise); §4's «a bound on a restricted class is not M4» applies to RF-A..RF-C (IDEAL-CYC on genome games) and RF-D is a conditional
  reduction between two OPEN questions. The box's §9 says the same. **G-N5-TIME stays OPEN** (GAPS row «open» at trunk e8b6abf0).
- §9 «Not proposed»: the W-FLAT argument (a rule-free window bound would bound one-sided strategy improvement with that rule on every
  game, through box 104's wrappers) is a lane reading of a lane lemma; it is a reason not to propose, not a statement, and needs no sign.

## 11. For a packet (what it would need, by statement)
- K-1 (§2 READING) The ten static lemmas restated in the every-state / every-standard-state form (CN2 / CN2-3 for every positional pair)
  as the packet's own statements, with «the landed proof at <file, lines> uses no property of the run» as their proof, each deciding
  line quoted by script. Do not cite R123 / R125 for the extended forms.
- K-2 (RF-A..RF-C) P-N5-LEVEL landed first (R129), or the re-used proofs ((K1)-(K4), (L1)-(L3), (L5), (C1), (C2), (P1), (P2), (P4), (P4)
  case (3)) written out in the packet. Quote pins at the landing commit.
- K-3 (RF-A) The definition of an improving run, and the F1 step written as in §4 (VJ00 §4.4 improvement at a priority-0 non-cycle-node
  vertex = a successor of strictly larger value), citing R15 (a) and P-N5-XICYC's reading.
- K-4 (RF-B) H_Y defined with the movers' gates IN Y; note N-1 (H_Y is a game). Claim only «identity or improving steps of H_Y»; a «same
  rule on H_Y» clause only for the rules fixed by the order of gate values, with §5's argument.
- K-5 (RF-C) The form of record (A1) and the body's form; N-2's wording for the Howard remark.
- K-6 (RF-D) Hypotheses as named items: [IMP3] = W-FLAT + box 104 §8 (lane; they must be refereed or stay hypotheses) + SPEC l. 32, 47
  and R125 §2 for the order (no reading needed) + ESC3-ALL; [L3] = box 209 with (K1′) from F1 + (K2′) and its (L1′)-(L3′), (L5′) re-read
  for an improving run (not done in this pre-read: I read box 209's statement lines only). G-1 closed by KEY-RESTRICT or by the
  rewording of §7; G-2 proved or labelled DATA; «F = T_key + const» proved or labelled (DATA: 1).
- K-7 (kill criteria) (A2) of record, the body's §8 as additional points; (iii)'s evaluation with units; N-3.
- K-8 (DATA) every clause names its counter and its unit in the text (not only in the tools' doc strings); the 9 timeouts and 1 OOM
  named (they are); the «no second engine for the other rules» weak point can cite this replay (own engine, own rule definitions).
- K-9 Labels: RF-A..RF-C CANDIDATE → PROVED (lane) only in a packet; RF-D CONDITIONAL; not N5, not N5′-xi, not M3 / M4; G-N5-TIME OPEN.

## 12. Tools and outputs (docs/referee-2/R2-box212/; own code; run with R2DIR=docs/referee-2; inputs by get_inst.py from be167574)
- get_inst.py (81 frozen genomes by name from the lane's rfd212 spec rows, duplicates compared by sha1: «frozen 81 towers 5 bad 0»;
  the 5 towers checked against box212/inst/SHA1SUMS).
- r2q212.py (+ r2q212.out, r2q212_e8b6abf0.out, r2q212_ctrl.out): §2's quote check. r2prem212.py (+ .out, _ctrl.out): premises landed or
  not. r2kill3.py (+ .out, _ctrl.out): (A3) re-count with my Ξ-feedback search.
- r2rf.py (RF-A / RF-B / RF-C replay, seven rules, --rule worsen and --rctrl k5t | nsp0 | tailshift | rfc | hval controls), sweep.sh
  (one process per (rule, file); resumable), sumrf.py → sweep_sum.out; sweep_totals.out keeps the TOTAL line and exit code of
  every one of the 771 output files (the per-file logs are not committed).
- r2tkey.py (+ r2tkey_towers.out, r2tkey_frozen.out): T_key against my engine's first fallback. r2keywin.py (+ keywin_towers.out,
  keywin_towers_ctrl.out, keywin_frozen.out, keywin_frozen_ctrl.out): G-1's probe and box 213's counters, second engine.
- Engines reused, unchanged: R2-P-ACYC/r2acyc.py, R2-P-N5-LEVEL/r2lv.py (successor 39), R2-P-N5-END/r2end.py (successor 34),
  R2-P-N5-SPLIT/r2split.py (mutate), R2-P-N5-END r2end.gen (random genomes).

## 13. Next
Push; message the Lead; then read L-RED 68's R239 (claude/l-red 2cc894f2) and write the agreement section as Addendum 1. The Lead says
R239 measured [IMP3] (in Ξσ), not the window clause; my [IMP3] trace is §7's first bullet.
