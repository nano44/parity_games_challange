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

## §C. Comparison with REFEREE's R-N5-RL (written 2026-10-25 12:46Z by date -u, after my report 30dc5f54 was pushed)
Read: docs/referee/R-N5-RL.md at trunk (report b7419da, §8.1 257c3d8; REFEREE successor 8). Nothing else in docs/referee/ was read.
### C.1 Joint gap map
| REFEREE | mine | item | reconciled verdict (Opus 5.5, D15) |
| --- | --- | --- | --- |
| RL-1 | G-RL-1 | TEV-RED (1): "the last Ev vertex" / f's play in F_{k0} need no Ev vertex on x_t's (= c's) cycle | same gap. Label CHANGED, see C.2: TEV-RED NOT SIGNED as stated; TEV-RED′ SIGN CONDITIONAL ON (P) |
| RL-2 | — (my miss) | MERGE stated for "ℓ ≥ −1", which includes ∞; at ℓ = ∞, (c) has no common vertex and "both plays end in c's cycle" is false | ACCEPTED. MERGE: SIGN WITH GAP RL-2 (scope: −1 ≤ ℓ < ∞). Every use (EV, EV+) is at a finite L, so §6 is unaffected. My rl_check.py skipped level-∞ gates silently (`l >= INF: continue`), and I did not flag the statement. I re-checked with my own N5: inr2_n32, state 0, gate (6, 29) has level ∞, with the plays of 29 ([29, 16]) and x0 = 27 ([27, 31, 18, 2]) disjoint; my deterministic library runs have 168 level-∞ window gates at (h) states, all with disjoint plays |
| RL-3 | G-RL-2 | TEV-RED (3) and the Consequence's third bullet: "before e" → "up to and including e" | same. L-RED 16's tevlast_cex_n40 (my N5: e = 15 ∈ H, B_t ∖ A = {e}) shows the worded form fails outside the ENT setting. REFEREE: e ∈ H at 0 of 607 meeting states in its data |
| RL-4 | — (my miss) | EV: the level-L window gate's EXISTENCE is P-N5-NJB §3's Corollary to NO-RF-OLD (FB step (2) + FBL), not ENT-SHAPE, which assumes the gate | ACCEPTED (citation). I checked ENT-SHAPE's first line ("Let (y, z) be a level-L gate at k with …") and the Corollary ("If M_k = L, a level-L tail exists … and it is an entrant") |
| remark | N-RL-2 | EV's "Ξ_k(z) = ρ ⊕ Ξ_k(q)" if q is on the cycle after c: the conclusion holds on H-parts (A = π_q ∩ H = ∅) | same argument in both |
| remark (EQ-END) | — | S's end state has (h), not only H2, when θ = w | accepted (true; not needed for the statement) |
| — | N-RL-1 | MERGE (c): read plays as paths up to the first visit of c | mine only (wording); compatible with RL-2 |
| — | N-RL-3 | "top of A Δ B even and in B" only after EV | mine only (wording) |
| — | FREE-FREEZE note | "(h) at t" is not needed | mine only |
### C.2 Verdict changes in this report
- TEV-RED: from "SIGN CONDITIONAL ON (P) WITH GAPS (G-RL-1, G-RL-2)" to NOT SIGNED as stated. I adopt REFEREE's form.
  - With G-RL-1 the stated lemma has a case its proof does not cover, and nothing excludes it.
  - With G-RL-2 its clause (3), as worded, is false whenever e ∈ H.
  - A gap of that kind is not a signature with gaps (D1: never soften a verdict); my draft label was too soft.
- TEV-RED′ (TEV-RED plus the hypothesis "no Ev vertex lies on the cycle of x_t's σ_t-play", with (3) read "up to and including e"):
  SIGN CONDITIONAL ON (P). My §6.2 check of (1)-(5) covers exactly this form.
- Consequence (the reduction): NOT SIGNED as stated. It holds when TEV-RED′'s hypothesis holds at t = k.
- MERGE: from SIGN to SIGN WITH GAP RL-2 (scope −1 ≤ ℓ < ∞).
- All other verdicts are unchanged and agree with REFEREE's: R-SAME, BL-FORM, BL (a), (d), CONF-MONO SIGN; BL (b), (c), (e),
  FREE-FREEZE, EV (with RL-4), EV+ SIGN CONDITIONAL ON (P); EQ-END SIGN CONDITIONAL ON CN-LAST.
- Labels: both reports find every packet label exact.
- REFEREE adds that the labels depend on R35 landing with ENT-SHAPE (1)-(4) and the NO-RF-OLD Corollary as signed. I accept this.
### C.3 DATA comparison (different engines: REFEREE's own SPEC N5, which reproduces n5.py's counts; mine = any arena optimum)
- Both see 0 cases of an Ev vertex on c's cycle, and 0 ENT settings, in batch and climbs: REFEREE 3 × 1,500 s; mine 4 × 1,200 s with
  1,583,748 runs.
- The RL-1 precondition A = ∅:
  - REFEREE: 37 of 376 NAMED and 95 of 526 LIB in-scope fallbacks;
  - mine: 0 in my batch (my N5's traces), 507,929 in climbs.
  - The second step (c switched into R̄_{k0}, or a later switch of C_t into Ev) was reached by neither.
- FREE-FREEZE on LIB: REFEREE 177,919, the packet's figure. Mine is 640,338 over a different input set and starts.
- Oink: REFEREE 234 + 75 + 3 climb bests; mine 552 (SCOPE library) + 8 climb bests + tevlast_cex_n40.
### C.4 Joint fixes lines for L-SI (one per gap; union of both reports)
- RL-1 = G-RL-1 (TEV-RED (1), Consequence): prove Ev ∩ C_t = ∅ for t ∈ (k0, k], or carry the hypothesis (TEV-RED′), or treat the
  cycle case (A = ∅) separately.
- RL-2 (MERGE): "level −1 ≤ ℓ < ∞".
- RL-3 = G-RL-2 (TEV-RED (3), Consequence bullet 3): "up to and including e".
- RL-4 (EV): cite P-N5-NJB §3's Corollary for the gate's existence.
- Wording, mine: N-RL-1 (MERGE paths up to c), N-RL-2 (EV, q after c), N-RL-3 (top of A Δ B after EV), FREE-FREEZE's unused "(h) at t".

## Addendum A: the new proof text in docs/si/P-N5-RL-fixes-box10.md (sha1 ac0274586a3b715d8725bc5226e3b32572edf017, l-si 1f107bfb, on trunk), checked 12:54Z by date -u
Read at the Lead's request (12:49Z). I did not read docs/si/N5-TEV-box11.md beyond what the fixes file quotes; the fixes file's proof
is self-contained and I checked that text.
| item | verdict (Opus 5.5, D15) | notes |
| --- | --- | --- |
| Lemma CYC-EV (ENT setting: no vertex of Ev ∩ F_k lies on C_k, the σ_k-cycle of c) | SIGN | no (P); the case is vacuous in data (no ENT setting) |
| replacement Proposition TEV-RED (t < k: TEV-RED′'s added hypothesis; t = k: by CYC-EV; e the last Ev vertex on the pre-c prefix; (3) as RL-3) | SIGN CONDITIONAL ON (P) | closes RL-1 = G-RL-1 at t = k; t < k stays TEV-RED′ |
| Consequence (the reduction, at t = k, with RL-3's wording) | SIGN CONDITIONAL ON (P) | via EV+, CYC-EV and the replacement TEV-RED (5) |
| RL-2, RL-3, RL-4 lines | accepted as written | same as my §C.4 |
| §7 TEV / TEV-LAST FALSE, k0-quantifier section | not signed (record) | consistent with my §6.3 (tevlast_cex_n40 reproduced with my N5) |
CYC-EV proof check, line by line:
- (Σ) gives (A_s), no leave at the S4a steps of (k0, k) (NL (ii)), and M_k ≤ L (CLS2).
- FZ. v ∈ F_k is in F_s for s ∈ [k0+1, k] (no leave). COARSE_L(Ξ v) is frozen across k0 (FLAT-ALL (iii), every vertex) and at each S4a
  step (NL (i), v ∉ R̄_{s+1}). ✓
- BF. For Even v ∈ R_{k0} ∩ F_k: v ≠ c (c ∈ F_{k0}) and λ(v) = c, so Ξ(v) = v ⊕ b(v) at k0 and at k (P2). v is not on its successor's
  pre-c path: a repeat of v before c would be a cycle through v without c. So by (C4), COARSE_L(b v) is COARSE_L(Ξ v) with v removed, at
  both states. FZ then gives COARSE_L(b_k v) = COARSE_L(b_{k0} v) = COARSE_L(Ξ_{k0} σ_{k0} v). ✓
- RB. If COARSE_L(Ξ_k a) ≠ COARSE_L(Ξ_{k0} a) for a = σ_{k0}(v), then R15 (a) and (C1) give Ξ_k(a) ▷ b_k(v) at a level > L. So
  a ≠ σ_k(v), and (v, a) is a gate at k of level > L ≥ M_k. Contradiction. (The hypothesis a ∈ R̄_k is not even needed for this step.) ✓
- WALK.
  - The first vertex a_j ∈ R̄_k on v0's k0-route exists, since o ∈ R̄_k.
  - Its predecessor is in F_k. If it were Odd (≠ o), its only successor in R̄_k would put it in R̄_k, so it is Even.
  - RB, and Lemma G at k0 and at k ((h) at both), give the H-part identity (π^k_{a_j} ∩ H) ⊔ B = (π^{k0}_{a_j} ∩ H) ⊔ A, since P(θ) ⊆
    V_{>c} makes P(θ) ∩ V_{>L} = P(θ) ∩ H. ✓
- CYC-EV. A vertex v ∈ Ev ∩ F_k on C_k has Ξ_k(v) = (c, ∅, ·), since c tops C_k and v ≠ c. FZ and Lemma G at k0 give A = ∅ and a low route
  for v. WALK from v gives B ⊆ A = ∅, against B ≠ A (the rise). ✓ C_k ⊆ F_k, so no Ev vertex at all lies on C_k. x_k's cycle is C_k
  (cycle node c). ✓
- The replacement statement takes e on the pre-c prefix. With no Ev vertex on the cycle, every vertex of f's whole play lies in F_t ∖ Ev
  ⊆ F_{k0}, which is what (1) and FREE-FREEZE need. (2)-(5) are as I checked them in §6.2. ✓
- The lane's reason why CYC-EV is not claimed for t < k is right: RB needs "no gate of level > L at t", which holds at the fallback state k
  (M_k = L) but not at S4a states. tevlast_cex_n40's gate (15, 21) of level 33 > L at t = 7 is exactly such a state.
- DATA (cycev_probe.py, own N5, logs_cycev/; DATA, not proof):
  - In setting (Σ) (k0 < k consecutive fallbacks of S, L = M_{k0} ≥ 0, r > L on [k0+1, k]; the rise not required): 836 settings on the
    280-file library × 4 starts.
  - FZ held at 21,720 vertices, BF at 1,869, RB and the WALK identity at 1,950 route walks, and M_k ≤ L everywhere; 0 failures.
  - Ev ∩ C_k ≠ ∅: 0 times. Settings with B ≠ A (the rise): 0, so CYC-EV's own case is vacuous here as well.
  - Random 𝒞^1O (20,000 games, n 6-16): 0 settings (vacuous).
Status after this addendum, P-N5-RL §6:
- TEV-RED, in the replacement statement: SIGN CONDITIONAL ON (P). The original packet text is still NOT SIGNED as stated (§C.2); it is
  replaced, not repaired in place.
- The Consequence: SIGN CONDITIONAL ON (P). CYC-EV: SIGN.
- With P1 (R2-N5-P1, signed by both referees), all three become unconditional.
