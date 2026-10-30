# N5-TXCD (box 52): a tied Ξ-climb descends along its Ξ-play to a GXC event, a λ_Ξ-change, an own W-cycle node, or an Odd GATE (σ̄ ≠ τ). The descent breaks at gates, not at τ-changes, and in the data gates carry 95 %
L-SI successor 32 (Opus 5.5), D15 / D18, Lead reading L40. Lead 2026-10-30 05:49Z: «BOX 52: attempt (i), TXC ≤ poly·(GXC + 1) … Write the
descent along z's Ξ-play to a switching vertex, and state exactly where Odd vertices break it. If it breaks only at τ-changes, those are O*,
a landed premise, which is fine to accept.» Working note, unrefereed, not a TARGET.md claim. G-N5-TIME OPEN. Labels as usual.
- Tool: experiments/si/odd/txcd.py (docstring). Output odd/out/txcd_corpus.txt (719 games). Pins: si/check.sh «box 52».
- Symbols as in box 51 (docs/si/N5-LATEP-box51.md): a W-run F (R89: τ constant, λ_W constant, no fallback), Ξ_t / σ̄_t ([S1-Xi]), W_t, XW,
  W-MON, Z_t. D_t := {Odd u : σ̄_t(u) ≠ τ(u)} (P-N5-GP §2). TXC event (z, s): s → s + 1 in F, Ξ_{s+1}(z) ▷ Ξ_s(z), W_{s+1}(z) = W_s(z).
  GXC event: L-NEW box 70 §3 (v Even switching at s, τ and λ_Ξ unchanged at s, v ∈ Z_s, Ξ climbs, W_{s+1}(v) ⊴ W_s(v)). [V1] / [V2]:
  RESULTS R17 (a) (a vertex that is not its own cycle node has value v ⊕ value(successor); v ⊕ · is strictly monotone on values whose
  paths avoid v).

## 1. Lemma TXC-DESCENT (PROVED, lane)
- Statement. Let (z, s) be a TXC event of F. Let x_0 = z, x_1, … be z's (σ_{s+1}, σ̄_{s+1})-play. Let j be the least index such that x_j is
  TERMINAL, of one of four kinds:
  - (T1) λ_Ξ(x_j) changes at s;
  - (T2) x_j is Even and switches at s (σ_{s+1}(x_j) ≠ σ_s(x_j));
  - (T3) x_j is Odd and x_j ∈ D_s ∪ D_{s+1} (a GATE: Odd's best response at x_j differs from τ before or after s);
  - (T4) x_j is its own W-cycle node (λ_W(x_j) = x_j).
- Then j exists, x_0, …, x_j are distinct, and every (x_i, s), i ≤ j, is a TXC event. In particular:
  - a T2 terminal is a GXC event whenever λ_Ξ is unchanged at s;
  - a T3 terminal is a tied Ξ-climb at a gate.
- Proof. Induction along the play. Suppose (x, s) = (x_i, s) is a TXC event and x is not terminal. Let c := λ_Ξ(x), the same at s and
  s + 1 (not T1).
  - x ≠ c. Otherwise Ξ_s(c) = Ξ_{s+1}(c) = (c, ∅, 0) and there is no climb.
  - Let y := σ_{s+1}(x) = σ_s(x) if x is Even (not T2). If x is Odd, let y := τ(x) = σ̄_s(x) = σ̄_{s+1}(x) (not T3).
  - Then y is x's successor on both Ξ-plays, at s and at s + 1, and on both W-plays (Even: σ unchanged at x; Odd: τ).
  - x is not its own Ξ-cycle node, so [V1] gives Ξ_t(x) = x ⊕ Ξ_t(y) for t = s, s + 1.
  - y's Ξ_t-path to c avoids x:
    - if x is not on the cycle, the play is simple up to c;
    - if x is on the cycle, then c ≠ x is reached from y before x.
  - [V2] then turns Ξ_{s+1}(x) ▷ Ξ_s(x) into Ξ_{s+1}(y) ▷ Ξ_s(y).
  - The same argument with W (not T4: x ≠ λ_W(x), constant on F) turns W_{s+1}(x) = W_s(x) into W_{s+1}(y) = W_s(y). So (y, s) is a TXC
    event.
  - Termination. The x_i follow one lasso. If the descent reached the Ξ-cycle node c of its lasso without a terminal, (c, s) would be a TXC
    event with λ_Ξ(c) = c fixed: impossible, as above. So a terminal occurs before any vertex repeats.
  - T2 and GXC. x_j is Even and switches, Ξ climbs, W is fixed (so W_{s+1} ⊴ W_s), and x_j ∈ Z_s, because
    Ξ_s ◁ Ξ_{s+1} ⊴ W_{s+1} = W_s by XW. τ is constant on F. If λ_Ξ is unchanged at s, this is L-NEW's GXC event verbatim. □

## 2. Corollary TXC-RED (PROVED, lane): TXC reduces to GXC, gate climbs, W-cycle nodes and λ_Ξ-changes
- Per W-run: TXC_F ≤ n·(GXC_F + GATE_F + CNW_F) + n²·LCT_F, where:
  - GATE_F := the pairs (o, s), s in F, with o Odd, o ∈ D_s ∪ D_{s+1}, and (o, s) a TXC event (tied gate climbs);
  - CNW_F := the TXC events (x, s) of F with λ_W(x) = x;
  - LCT_F := the transitions of F at which λ_Ξ changes anywhere.
- Over a whole run, Σ_F LCT_F ≤ n(n − 1): Ξ is non-decreasing along the run (R15: S4a and S4c steps apply improving switches; τ-steps do
  not change Ξ_σ), so the reward of λ_Ξ(v) strictly increases at each change, at most n − 1 changes per vertex.
- Proof. At one transition s there are at most n TXC events. Each one has a terminal (x, s) on its own play.
  - If λ_Ξ is unchanged at s: the terminal is a GXC event (T2), a gate climb (T3), or a CNW event (T4). Each (x, s) is the terminal of at
    most n TXC events.
  - If λ_Ξ changes at s: charge all ≤ n events to s. □
- With box 51's Lemma GAP-CLIMB (LATE′_F ≤ Σ_z d_E(z)·(TXC_F(z) + WZ_F(z))):
  LATE′_F ≤ n_E·[n·(GXC_F + GATE_F + CNW_F) + n²·LCT_F] + Σ_z d_E(z)·WZ_F(z).

## 3. Where Odd vertices break the descent (the Lead's question)
- Exactly at GATES: Odd o with σ̄_s(o) ≠ τ(o) or σ̄_{s+1}(o) ≠ τ(o). τ is constant on a W-run, so the descent never meets a τ-change: O* is
  not the obstruction.
- At a gate the Ξ-play leaves the W-play. Ξ(o) = o ⊕ Ξ(σ̄ o), while W(o) = o ⊕ W(τ o) stays fixed. The climb continues below σ̄(o), but W
  there is no longer tied, so the descent can only continue as a ZXC / WZ descent, which brings back the circle.
- Even vertices never break it: a non-switching Even vertex passes the tie down unchanged, and a switching one is a GXC event.
- So (i) as posed (TXC ≤ poly·(GXC + 1)) is NOT proved. The remainder is GATE (plus CNW), not O*.

## 4. DATA (txcd.py; corpus 719 games; sums over W-runs)

| set | TXC | → T1 (λ_Ξ change) | → T2 GXC | → T2 at a λ_Ξ-changing transition | → T3 gate | → T4 | descent failures | GXC events | distinct gate terminals | most TXC per terminal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| corpus | 14,526 | 356 | 292 | 0 | 13,878 | 0 | 0 | 227 | 2,333 | 83 |
| so_th_n32 | 63 | 0 | 0 | 0 | 63 | 0 | 0 | 0 | 15 | 13 |
| wdepth_K4_m16 (R130) | 184 | 0 | 0 | 0 | 184 | 0 | 0 | 0 | 93 | 32 |
| tiedmut_so_th_n32_11 (box 51) | 66 | 0 | 0 | 0 | 66 | 0 | 0 | 0 | 9 | 14 |

- Descent failures (DESC_V, CYC_V, TERM_V) are 0 everywhere, as §1 proves. txcd.py does not test T4 separately: a T4 vertex that is not
  also T1-T3 would appear as a failure, and there are none.
- 95.5 % of tied climbs end at a gate. On wdepth and so_th there are no GXC events in any W-run, yet 184 and 63 TXC events. So the
  bound TXC ≤ poly·(GXC + 1) can only hold through the polynomial, not through GXC: the gate count is what carries TXC.

## 5. What this leaves (READING)
- The composition lever the Lead asked for exists, but its live term is GATE_F: tied Ξ-climbs at Odd gates inside one W-run. With τ fixed,
  a gate climb is Ξ(o) rising toward the fixed W(o) through Odd's best-response branch σ̄(o) ≠ τ(o).
  - This is Even making progress against Odd's best response at a vertex where Odd's actual strategy τ is not that best response. It is
    the two-player content of the W-run, now localised at gates.
- A bound on GATE would need either:
  - a potential at gates: the gap W(o) − Ξ(o) shrinks at each gate climb, but values are exponentially many;
  - or a link to the Odd side: o ∈ D means τ(o) is not σ̄(o). Odd's own improvement step uses Ξ_τ against τ̄ (R89 FRAME-τ), not σ̄, so no
    link is proved.
- Proposed next premise, if the Lead wants a single named one: [P-GATE] GATE_F ≤ p(n) per W-run. Together with box 51 and §2 it gives
  LATE′ polynomial ⇐ [P-GATE] ∧ [GXC per W-run] ∧ [CNW per W-run] ∧ [WZ per W-run]. WZ is still the circle; CNW is 0 in all data.

## DONE / FINDINGS / NEEDS
- DONE: odd/txcd.py; corpus; si/check.sh «box 52»; this note.
- FINDINGS:
  1. PROVED (lane): Lemma TXC-DESCENT. A tied Ξ-climb descends along its Ξ-play, staying tied, to a terminal of four kinds: λ_Ξ change,
     switching Even (= GXC when λ_Ξ is fixed), Odd gate (σ̄ ≠ τ), or own W-cycle node.
  2. PROVED (lane): Corollary TXC-RED. TXC_F ≤ n(GXC_F + GATE_F + CNW_F) + n² LCT_F, with Σ LCT ≤ n(n − 1) per run.
  3. READING: Odd vertices break the descent exactly at gates, never at τ-changes (τ is fixed on a W-run). So O* does not absorb the
     remainder, and (i) TXC ≤ poly·(GXC + 1) is not proved.
  4. DATA: 13,878 of 14,526 corpus TXC events end at gates, 292 at GXC events and 356 at λ_Ξ changes; 0 descent failures. wdepth: 184
     TXC events, 0 GXC events.
- NEEDS: none from the owner.
