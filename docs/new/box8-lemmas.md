# Box 8 statements, for a referee packet (L-NEW successor 3; all are L-NEW READINGS, unrefereed; 2026-10-19 by date -u ~01:51Z)
Each entry: statement, where the proof is, the computer check. Source for VJ00: BRICS RS-00-48, as in RESULTS R15.

| id | statement | proof | check |
|---|---|---|---|
| CDAG | One-player game CDAG_n (n+1 vertices, all ⊕) has a chain of 2^n − n − 1 single VJ00 improvements, every one Ω-strict. So (P*) and (P_strict) of R-N5K9 are false | N5-K9-Pstrict-counter.md "Proof (reading)" | p_strict/cdag.py: si.py engine checks every step, n ≤ 12; Lead re-run n = 4..10 |
| S | Switch-best on an acyclic one-player game is optimal after ≤ h steps (h = depth of an optimal tree) | N5-K9-Pstrict-counter.md §5 | sb_sink_check.py: 0/2,000 violations |
| F | With τ frozen, N5's Even moves are V_τ-monotone in G_τ | N5-K10-box8.md §1 | (follows from VJ00 §5 arena optimality) |
| G | Frozen τ + direct gifts ⇒ ≤ Σ(deg − 1) V_τ-strict Even moves | N5-K10-box8.md §1 | gift-gadget climb 5/7 iterations |
| NR | Along N5's run, σ and τ never return to an earlier strategy (from R15 (c)+(d)) | N5-K8-box8.md §1 | n5_noreturn.py: 0 returns in 329 runs |
| K8-2 | K8's 2-periodic case cannot be followed by N5, except for an edge effect at the start (from NR) | N5-K8-box8.md §2 | sbalt_n16 + sb_alt_diag.py |
| T | One-player switch-best: if ρ*(x) is settled and x ≠ λ*(x), then x is settled one step later | N5-K8-box8.md §3c | consistent with sb_settle.py and with the SB1 counterexample traces |
| SB1 | "switch-best on one-player games takes ≤ n steps": FALSE (11 at n = 10, 17 at n = 16; instances/sb1p/sb1_counter_n*.pg) | — | n5.py reproduces |
| SB1' | CONJECTURE: O(n) steps (data ≤ n + 1) | open (cycle tops) | all-start n ≤ 7; climbs to n = 64; SB2 (a weaker potential) is false |
