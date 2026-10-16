# Notes on instances kept from L-ALG climbs (2026-10-16, produced on Opus 5.5)
One line each; "stable" = order datum (priority, id) of dtl_pyref; "oink" = Oink's own order (exact against pinned Oink).
- flat_dead_carries_n20.pg: C6, stable order; 11 of 12 dead-top cap carries in one phase raise no Φ_idx record (GAP-A-M §11d-§11e); Oink 5 iterations, verified.
- flat_dead_carries_n32.pg: C6, stable order; 9 of 11 flat dead-top cap carries in one phase; Oink 6 iterations, verified.
- fresh_fixed_n24.pg: A_DTL stable order, fixed tracer; 4 fresh contexts (dtl_pieces.fresh_contexts), 15 searches; Oink 15 iterations, verified.
- fresh_fixed_n32.pg: A_DTL stable order, fixed tracer, from nest_nest_s81; best of climb seed 112 at commit time (fresh 7 reached 13:21Z), see GAP-A-M §13b; Oink-verified.
- h4_def4_oink_n20.pg: A_DTL OINK order (exact; Oink 8 iterations, verified); 4 deficit-triggered changes at one context (piece 0, R = G') with the ideal result stable throughout (GAP-A-M §13b).
- h4_def5_stable_n20.pg: A_DTL stable order only; 5 deficit-triggered changes at one context with the ideal stable; in Oink order 0 deficits (§13b).
- phi_idx_flat_n20.pg, phi_idx_cutrec_n20.pg: Φ_idx counterexamples (GAP-A-M §11d, docs/alg/DEAD.md).
- h4_def6_oink_n28.pg: A_DTL OINK order (exact; Oink 9 iterations, verified); 6 deficit-triggered changes at one context (piece 0, |R| 26, after the first dominion) with the ideal stable throughout (GAP-A-M §13b).
