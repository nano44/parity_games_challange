# P-IDEAL-CUBE fixes (append-only)
L-NEW successor 50, 2026-11-04 (date -u: see the commit). Packet docs/new/P-IDEAL-CUBE.md at d97555d4 (sha1 366afedcf7cd04a31302e25cec47c7fb3df455bb,
186 lines), NOT edited. Referees: REFEREE 23 5ef7bf47, REFEREE-2 26 0787732b. Both SIGN all 4 statements, no math gap. Routed by the Lead
03:36Z. Line L-1 (sha1 99ae8face50615b4ce1ce5cd5e69f223f17208e1) is unchanged; line L-2 is the new file docs/new/P-IDEAL-CUBE-line-L2.txt.

## Entry 1 (packet precision, REFEREE-2 P-1; optional, taken)
- Old (packet l. 30-31, §0):
  - C_s(x) (x ∈ D2): the option of x whose Ξ-value is strictly better at s. Two faces never tie (P-IDEAL-RED ENC, signed; R105 when
  - landed: distinct options carry distinct β's, so their β-sets differ).
- New:
  - C_s(x) (x ∈ D2): the option of x whose Ξ-value is strictly better at s. Two faces never tie: face k's β-set contains β(x, k) and
  - not β(x, 1 − k), because by acyclicity neither chain returns to x, so the two β-sets differ; ENC (P-IDEAL-RED, RESULTS R105) then
  - makes them unequal in the order.
- Reason: «distinct β's» alone does not separate the sets; the chain of face k could in principle contain β(x, 1 − k) only by
  passing through x again, which acyclicity excludes. No proof in the packet changes.

## Entry 2 (line L-2; REQUIRED 1-2: REFEREE CUBE-L1 = REFEREE-2 LC-2, REFEREE-2 LC-1; OPTIONAL 3-6: both / CUBE-L3 / LC-P1 / LC-P2)
- Taken: 1 (READING stated as a reading), 2 (DATA with the packet's gate order: gate indices increasing in the option index, as in
  box154/ladder.py g(x, k) = 2x + k), 3 (arXiv:2207.05985v1), 4 (L_K: all movers of degree 2, distinct gate indices), 5 (π bound
  at first use, in the premises list), 6 (LOCAL (c) dropped: unused; only LOCAL (b) is used). Also «signed, RESULTS R105 when landed»
  → «RESULTS R105» (R105 landed 02:59Z, 91c1464f).
- Word diff L-1 → L-2 (every change; nothing else differs):
  - [delete] after «… and Lemma LOCAL (b),»: «(c), signed,» → «»
  - [replace] after «… (b), (c), signed, RESULTS»: «R105 when landed;» → «R105; π a topological order of the Ξ-graph;»
  - [replace] after «… of Weber and Widmer,»: «arXiv:2207.05985,» → «arXiv:2207.05985v1,»
  - [delete] after «… coordinate of largest π»: «(π a topological order of the Ξ-graph)» → «»
  - [insert] after «… the explicit genome L_K»: «» → «(all movers of degree 2, distinct gate indices)»
  - [replace] after «… itself give a polynomial»: «bound, and» → «bound (READING: a polynomial bound on T must use»
  - [replace] after «… bound, and the W-key»: «rule must carry any such bound;» → «rule);»
  - [insert] after «… LP (DATA: on L_K»: «» → «with gate indices increasing in the option index,»
