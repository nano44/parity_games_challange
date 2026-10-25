# R2-N5-RL: second-referee check of packet P-N5-RL (L-SI box 10: BL-FORM, BL, CONF-MONO, FREE-FREEZE, EQ-END, MERGE, EV, EV+, TEV-RED). REFEREE-2 (successor 8), 2026-10-25 12:35Z (drafts 592128a4, fa0273de) (date -u)
Signature: (Opus 5.5, D15). Packet P-N5-RL (Lead 12:01Z). Object docs/si/P-N5-RL-box10.md, sha1 0a3c70cbf873b2e011a5a00be54d38926f7861f1.
I checked it with `git show 2fb698d:docs/si/P-N5-RL-box10.md | sha1sum` and on my tree. The pin is trunk 2fb698d, an ancestor of my
merged trunk 48a8a4c.
Background read: P-N5-FBW §1-§3 (RESULTS R31: P-OPT, FBW with Step 2, FBW-S, FLAT-ALL); P-N5-NJB §3-§4 (NO-RF-OLD, ENT-SHAPE; sha1
f43a8823, signed by both referees); RESULTS R15 (a), R17 (a) F1 (unconditional), R18 (d) Lemmas R and S, R19 (a), R21 (a), R29 (a)-(e);
P-N5-SCOPE §6 CN-LAST (I signed it in R2-N5-SCOPE, 6d6e4bcf; the packet cites sha1 c3f5ed37 "at trunk 70b0f05", where the blob is the same).
Independence: no REFEREE report on this packet is on my tree, and I read none. I did not run or import any experiments/si/riselast script
or any REFEREE probe. Lane .pg files are inputs only.
Tools: docs/referee-2/R2-N5-RL/ (own code on my lane's R2-N5-FRZ/frz_check.py): rl_check.py, rl_climb.py, run_all.sh, run_climbs.sh,
files.lst, logs/, climb/, totals_logs.txt, totals_climb.txt. One Odd choice vertex is asserted on every game. W* is Even's best response
to τ (pointwise maximum by SI); Opt(G_τ[F]) is the same on the arena of Even edges inside F.
Attribution: every count is on MY N5's traces (S4a = any arena optimum; deterministic or --rand). No SPEC trace was run.
Labels (D18 / L40): the packet's PROVED / CONDITIONAL labels are its own; I check that each is exact. §7 is not signed. Nothing here is a
running-time bound, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN.

## Verdicts (Opus 5.5, D15)
| statement | packet label | verdict | label exact? | gaps / notes |
| --- | --- | --- | --- | --- |
| §1 Lemma R-SAME, BL-FORM | PROVED | SIGN | yes (Lemma G, XW, (C7); no (P)) | — |
| §2 BL (a), (d) | PROVED | SIGN | yes (Step 0-1: R18 Lemmas R, S (a); F1; no (P)) | — |
| §2 BL (b), (c), (e) | CONDITIONAL on (P) | SIGN CONDITIONAL ON (P) | yes ((b): (P) in G_τ at Step 2b; (c): (P) in G_τ[F_k]; (e) through (c)) | — |
| §3 CONF-MONO | PROVED | SIGN | yes (F1 only) | not used later in the packet |
| §3 FREE-FREEZE | CONDITIONAL on (P) | SIGN CONDITIONAL ON (P) | yes (via BL (c)) | (h) at t is not used |
| §4 EQ-END | CONDITIONAL on CN-LAST | SIGN CONDITIONAL ON CN-LAST | yes (XW, FBW-S, FBW (b), CN-LAST (iii); no (P)) | — |
| §5 MERGE | PROVED | SIGN | yes | N-RL-1 (wording): read "plays" in (c) as the paths up to the first visit of c; then "first common vertex" is a merge point of both, and the prefixes are disjoint |
| §6 EV | CONDITIONAL on (P) | SIGN CONDITIONAL ON (P) | yes (via FREE-FREEZE; also ENT-SHAPE (4), signed in P-N5-NJB) | N-RL-2: "Ξ_k(z) = ρ ⊕ Ξ_k(q)" assumes q comes before c on z's play; in the other case (q on c's cycle after c) the conclusion still holds (§6.1). N-RL-3: "the top of A Δ B is even and in B" (Facts) is only true after EV gives A ⊆ B |
| §6 EV+ | CONDITIONAL on (P) | SIGN CONDITIONAL ON (P) | yes | — |
| §6 TEV-RED | CONDITIONAL on (P) | SIGN CONDITIONAL ON (P) WITH GAPS | yes | G-RL-2 (statement): (3) says "before e", but the proof shows "up to and including e", and e ∈ H is not excluded. My N5 reproduces L-RED 16's tevlast_cex_n40 (sha1 ff1e9cb4, on l-red, not on trunk): k0 = 3, L = 32, t = 7, e = 15 ∈ H, B_t ∖ A = {e}. That instance has one fallback, so it lies outside the ENT setting. But nothing in the setting excludes e ∈ H, so (3) as worded is unproved. (4)-(5) use only A ⊆ B_t ≠ A and survive. The Consequence's last bullet needs the same fix. G-RL-1 (proof): "let e be the LAST Ev vertex on x_t's play" exists only if c's honest cycle at t avoids Ev. (1) needs f's whole play in F_{k0} (FREE-FREEZE's hypothesis) and (3) needs e before c. Neither is proved when c's cycle at t passes Ev. The case is not refuted: 0 occurrences in 8,771 batch states and 851,022 climb states. Fix: add "c's honest cycle at t lies in F_{k0}" as a hypothesis (the Consequence then needs it at t = k), or prove it |
| §7 | — | not signed (as briefed) | — | BL-X's FALSE status is the lane's data; not re-checked |
No item is NOT SIGNED. No counterexample in 45,680 batch runs and 1,583,748 climb runs. The ENT setting (§6's hypothesis) never
occurred in my data either (0 batch, 0 climb), so EV, EV+ and TEV-RED rest on the proofs alone.

## 1. BL-FORM and R-SAME: SIGN
- R-SAME. P(π ⊕ a) = (π ∩ V_{>c}) ⊔ P(a), because P(θ), P(w) ⊆ {o} ∪ F are disjoint from routes ⊆ R (Lemma G under (h)). The
  symmetric difference is the same for a = θ and a = w; if it is empty, the lengths differ by |π| − |π′| both times. ✓
- BL-FORM case analysis on (s, u) = (σ_k v, u):
  - F/F: Ξ = W, so a W-improving edge is a gate.
  - R̄/F: W(s) = π_s ⊕ w ⊵ π_s ⊕ θ = Ξ(s) (XW through (C7)), so again a gate.
  - R̄/R̄: R-SAME.
  - F/R̄ remains, and it is (b). v ∈ F, since v ∈ R would put s ∈ R̄. (c): both ends of (b) have cycle node c. ✓
- DATA: 172,334 blocked edges at (h) states; (a)-(c) held at all of them.

## 2. BL: (a), (d) SIGN; (b), (c), (e) SIGN CONDITIONAL ON (P)
- Step 0. U_τ = W* by R18 Lemma S (a). Its order on G^d is the reverse of G's (Lemma R). So (o, x) ∈ Iτ ⟺ W*(x) ◁ W*(e*). ✓ No (P).
- Step 1. If (o, x) ∈ Iτ_k with x ∈ F_k and o ⊕ Ξ_k(x) ◁ w_k, then x is an option of S4b's arena. There V_{σ_k,τ_new}(o) ⊴
  V_{σ_k,x}(o) = o ⊕ W_k(x) ◁ w_k (x's play avoids o; Lemma G). So τ_new(o) ≠ e*, and S4c does not fire. ✓
- (a). If W_k = W*, then θ_k ◁ w_k gives W*(x0) ◁ W*(e*) ((P2) at o under H1, (C7)). So (o, x0) ∈ Iτ_k, against Step 1. ✓ No (P).
- (b).
  - Step 2a is R31 FBW Step 2 with V := W_k, applied to σ_k[y ↦ z] ∈ A(σ_k), against P-OPT. Its only non-strict case is P(V z) = ∅,
    y = c (y its own cycle node, level −1). ✓
  - Step 2b switches every exceptional tail to a W-best target. W is unchanged: the CN-LAST (i) argument, re-proved for the fixed-τ
    valuation. No improving edge remains. (P) in G_τ then gives optimality, against (a). ✓
  - This is the only use of (P) in (b), so the label is exact.
- (c). G_τ[F_k] is closed: σ_k(F) ⊆ F, and Odd vertices of F are forced into F. Its improving edges are gates (BL-FORM, F/F case),
  hence exceptional. Step 2b inside F, then (P) in G_τ[F_k]. ✓
- (d). Step 1 gives (o, x) ∉ Iτ. So W*(x) ⊵ W*(e*) ⊵ W_k(e*) (F1) ▷ W_k(x) ((C7)). x ≠ e*, since o ⊕ Ξ(e*) = w. ✓ No (P).
- (e). A G_τ-strategy whose play from x0 stays in F_k is matched by a G_τ[F_k]-strategy on that play. So its value is
  ⊴ Opt(G_τ[F_k])(x0) = W_k(x0) ((c), hence (P)) ◁ W*(x0) ((d)). The exit is an Even edge, since Odd vertices of F are forced. ✓
- DATA (2,144 in-phase THR fallbacks with (h)): (a)-(e) held at all of them. For (e) I checked the computed optimal strategy's play; for
  (d), every free exit with o ⊕ Ξ(x) ◁ w.

## 3. CONF-MONO: SIGN. FREE-FREEZE: SIGN CONDITIONAL ON (P)
- CONF-MONO: extend a G_τ[F′] strategy by σ inside F ∖ F′ (F is closed), then apply F1 in G_τ[F]. ✓
- FREE-FREEZE.
  - σ′ := σ_t on z's play, and σ_{k0} on the rest of F_{k0}. This is a G_τ[F_{k0}] strategy, since the play is closed and inside F_{k0},
    and its play from z has value W_t(z) = Ξ_t(z).
  - F1 and BL (c) at k0 give Ξ_t(z) ⊴ W_{k0}(z) = Ξ_{k0}(z). R15 (a) gives ⊵. ✓
  - The hypothesis "(h) at t" is not needed: Lemma G (a) holds without (h).
- DATA: 640,338 (k0, t, z) checks, 0 failures.

## 4. EQ-END: SIGN CONDITIONAL ON CN-LAST
- θ_t ⊴ θ_s ⊴ w_s = w for s ≥ t in S (R15 (a), XW). So every later state is EQ. ✓
- At an EQ fallback, δ = ⊥ (Lemma G; lev(π ⊕ θ, π ⊕ w) = r = ⊥) and every gate has level −1 (FBW-S). FBW (b) (ℓ = −1 > δ) makes
  every tail its own Ξ-cycle node. So CN-LAST's hypothesis holds for all gates, and (iii) ends the phase at k + 1. ✓
- DATA: 5,991 scope runs reach θ = w; 52 fallbacks follow such a t, never 2 in one run, and each is the last transition of its phase.

## 5. MERGE: SIGN (N-RL-1)
- (a). lev(b_k y, Ξ_k z) = ℓ gives equal COARSE_ℓ. P(Ξ_k z) ⊆ F_k and π ⊆ R_k, so π ∩ H = ∅. ✓
- (b). If o ∈ H, then o ∈ P(θ) ∩ H ⊆ P(Ξ z) ⊆ F. Contradiction. ✓
- (c). Both values have the cycle node c, so P(Ξ z) ∩ H = P(θ) ∩ H = P(Ξ x0) ∩ H (o ∉ H).
  - N-RL-1: take the paths of z and x0 up to their first visit of c. In a functional graph two such paths share a common suffix from
    their first common vertex m on. So the prefixes before m are disjoint, and their H-parts are equal (from the equality above), hence
    empty. ✓
- DATA: 40,974 window gates at (h) states; (a)-(c) held (prefix disjointness and H-emptiness checked explicitly).

## 6. EV, EV+: SIGN CONDITIONAL ON (P). TEV-RED: SIGN CONDITIONAL ON (P) WITH GAPS (G-RL-1)
- Setting facts, checked:
  - the ENT setting is P-N5-NJB §3-§4's (k0 < k consecutive fallbacks of S, M_{k0} = M_k = L ≥ 0, r > L on [k0+1, k], a rise in
    (k0, k));
  - (h) holds at k0 + 1 (it starts a transition of S);
  - FLAT-ALL's (h)-at-k0+1 premise therefore holds;
  - (A_s) holds by OFFGATE and NL (iii), and NL (ii) gives F_s ⊆ F_{k0+1} at the S4a steps between the fallbacks;
  - COARSE_L(θ_k) ≠ COARSE_L(θ_{k0}) by monotonicity, (C1) and (C3).
  - N-RL-3: "the top of A Δ B is even and in B" needs A ⊆ B, which is EV's conclusion. Before EV only "even in B or odd in A" follows.
    The statement is used only after EV (EV+), so this is wording.
- EV. If z's whole play lay in F_{k0}, FREE-FREEZE would freeze Ξ(z) from k0 to k, against ENT-SHAPE (4). The play lies in
  F_k ⊆ F_{k0+1}, so it meets Ev. ✓
### 6.1 EV's bookkeeping and N-RL-2
- If q (the first Ev vertex) comes before c on z's play, then Ξ_k(z) = ρ ⊕ Ξ_k(q). The packet's computation then gives
  B = (ρ ∩ H) ⊔ (π_q ∩ H) ⊔ A. ✓
- If q lies on c's cycle after c, the prefix equation fails, but the conclusion survives:
  - P(Ξ_k q) = ∅, while q ∈ F on [k0+1, k] (FLAT-ALL (iii), NL (i)). So (π_q ∩ H) ⊔ A = ∅.
  - B = P(Ξ_k z) ∩ H = ρ′ ∩ H, with ρ′ the path before c. The vertices of ρ between c and q are below c.
  - So B = (ρ ∩ H) ⊔ (π_q ∩ H) ⊔ A again. ✓
- EV+. Case h ∈ ρ: MERGE (c) puts every H-vertex of z's play on the shared suffix, and q follows h. Case h ∈ π_q: h ∈ P(θ_k) ∖ {o} lies on
  x_k's play, in F_k ∩ R_{k0} ⊆ Ev. ✓
### 6.2 TEV-RED and G-RL-1
- (2)-(5) check line by line, GIVEN (1) and (3).
  - In (2), "NL (i) for b(e)" passes through Ξ(e) = e ⊕ b(e): e ≠ c (c ∈ F_{k0}) and e ∉ P(b(e)), so COARSE_L(b(e)) is recovered from
    COARSE_L(Ξ(e)). This step is implicit; it is fine.
  - (4): H-part(Ξ_t u_e) = π′_H ∪ B_t ⊋ A, and the lift through R15 (a) gives a gate of level > L. ✓
  - (5): M_k = L. ✓
- G-RL-1. The proof of (1) takes "the last Ev vertex e on x_t's σ_t-play" and concludes "every vertex after e … lies in F_{k0}", hence
  f's play ⊆ F_{k0} (FREE-FREEZE).
  - If c's honest cycle at t contains an Ev vertex, the full play meets Ev infinitely often. Then no last Ev vertex exists.
  - Taking the last Ev vertex before the first visit of c does not help: f's play then still runs around a cycle through Ev, so
    FREE-FREEZE does not apply.
  - (3)'s decomposition Ξ_t(x_t) = (prefix up to e) ⊕ Ξ_t(f) also needs e before c.
  - I could not rule the case out. It needs (i) A = ∅ (FLAT-ALL (iii) and NL (i) at an Ev vertex q on the cycle) and (ii) c's cycle at t
    to differ from its cycle at k0, which lies in F_{k0}.
  - (ii) is reachable in principle: a flat switch of c at k0 into R̄_{k0} whose route is cut by a level −1 R → F switch.
  - It is NOT a counterexample: TEV-RED is silent in that case rather than false. But the packet's Consequence ("if NJB fails in the ENT
    setting, then at k …") uses TEV-RED at t = k with no such hypothesis.
  - Fix: add the hypothesis "c's honest cycle at t lies in F_{k0}" to TEV-RED and the Consequence, or prove it.
- DATA:
  - The CYC probe ran after every in-scope fallback with M ≥ 0, at every state of S up to the next fallback: c's cycle met Ev 0 times
    in 8,771 states.
  - Its preconditions: P(θ_{k0}) = ∅ 0 (batch) / 507,929 (climbs; FIT cyc reaches it easily) times; c switched into R̄_{k0} at k0 0 (batch) / 0 (climbs) times.
  - The threat's play met Ev at 3,576 of those states, never only on the cycle.
  - Climbs FIT cyc: 395,937 evaluations (1,583,748 runs), 0 violations; c's cycle never met Ev in 851,022 states; the second precondition (c switched into R̄_{k0}) was never reached; 0 ENT settings.

### 6.3 L-RED 16's findings (Lead 12:27Z, re-run by the Lead; checked here with my own N5, tev_probe.py)
- TEV-RED (3) "before e": as G-RL-2 above. My draft (592128a4) missed this: I checked (3) against its proof line, not its stated form. My N5 gives the same trace on tevlast_cex_n40: 11 iterations, 1 fallback, as the Lead's n5
  run. Oink zlk matches my regions (2 / 2).
- "No vertex leaves R in (k0, t] needs k0 to be the last fallback before t." The packet's EV, EV+ and TEV-RED quantify k0 < k as
  CONSECUTIVE fallbacks of S, with t ∈ (k0, k]. So every transition in (k0, t) is an S4a step of S, and NL (ii) applies. The quantification
  is right as written. A reading with an arbitrary earlier k0 would not be.
- CONJECTURE TEV (§7, not signed) is FALSE by L-RED's two instances. That is the lane's data, re-run by the Lead and not by me, except for
  tevlast_cex_n40: my N5's threat meets Ev at t = 7. My probe restricts k0 to the last fallback before t, so it does not reproduce
  tev_cex_n40's any-earlier-k0 case.

## 7. Batch and climbs (DATA, my N5)
- Batch: files.lst lists the 280 tracked experiments/**/*.pg on 𝒞^1O with n ≤ 64 (includes experiments/si/riselast/instances rl_a/b/c,
  experiments/si/coarse/instances/box9, cl9_rep_b, cl9_norf_a/b, x31_rx32, x31_lem_e24, elim24_p52), 3 starts × {det, --rand}. Random:
  4 × 10,000 games at n 4-14 and 2 × 2,000 at n 15-30. 566 logs, all RESULT OK, 0 violations; 45,680 runs, 94,886 transitions, 3,449
  fallbacks.
- Climbs (rl_climb.py FIT cyc, 4 × 1,200 s; seeds 61-62 random, 63 from cl9_norf_a, 64 from rl_a): 
| seed | start | best n | best fitness | note |
| --- | --- | --- | --- | --- |
| 61 | random 8-14 | 11 | 208 | P(θ_{k0}) = ∅ at 4 fallbacks |
| 62 | random 10-18 | 12 | 1,248 | P(θ_{k0}) = ∅ at 24 fallbacks |
| 63 | cl9_norf_a | 32 | 80 | threat meets Ev at 40 states |
| 64 | rl_a | 32 | 30 | threat meets Ev at 24 states |
- Totals: 604,087 THR fallbacks, 12,800,229 FREE-FREEZE checks, 213,037 threat-meets-Ev states (never only on the cycle); 0 violations.
- Oink: my 𝒞^1O N5 is the one validated in R2-N5-SCOPE (552 / 552 on the library); the climb bests are cross-checked below.
- Climb bests (climb/best_cyc_61..64.pg, sha1 0729c507, 028d5399, e1f1e7a4, 173fbff1): oink_xcheck 8 / 8 OK. tevlast_cex_n40: 2 / 2 OK.

## 8. Notes for the lane (none blocks a signature; G-RL-1 and G-RL-2 are the gaps on TEV-RED)
- G-RL-2: TEV-RED (3) and the Consequence: "before e" → "up to and including e".
- G-RL-1: TEV-RED needs c's honest cycle at t inside F_{k0} (or a proof of it) for its "last Ev vertex" and for (1), (3).
- N-RL-1: MERGE (c): say "paths up to the first visit of c".
- N-RL-2: EV: add the case "q after c on the cycle" (the conclusion holds, §6.1).
- N-RL-3: EV setting facts: "top of A Δ B even and in B" only after A ⊆ B.
- FREE-FREEZE: the hypothesis "(h) at t" can be dropped.
