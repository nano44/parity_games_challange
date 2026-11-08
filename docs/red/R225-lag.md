# R225 item 1: adversary on L-SI 45's BOX 86 lemmas (L-RED successor 59, Opus 5.5, D1 / D18 / D14; 2026-11-08, date -u)
Target (Lead 08:47Z): claude/l-si 2123ae7adacdeb68278afbfc5b9cd699a84284d2, docs/si/box86-lagtower.md §1-§2 (read in full, §0-§4), 11 frozen
instances (experiments/si/box86/inst, pins.sha1). Asked:
- attack SAME-E-MERGE, ACCESS-LATCH and Corollary LEAPFROG;
- check the in-edge claim against R104's genome definition, for every vertex class, pads and K-vertices included;
- check that the latch hypothesis fails at each of the OFF steps.
Labels: SURVIVES / BROKEN; DATA (unit, set, scope, counter). Not a TARGET.md claim; G-N5-TIME stays OPEN.
Tools: experiments/red/r225/latch225.py, my own code on R221's independent IDEAL-CYC Howard run own.py and my Γ3 builder r223/own3.py.
No L-SI code is used.

## 0. Verdict
| statement | verdict | basis |
| --- | --- | --- |
| SAME-E-MERGE (§1) | SURVIVES. Wording slip on Γ3: the in-edges there come through pads (§1) | proof re-derived; in-degree table on Γ and Γ3; mergeviol 0 |
| ACCESS-LATCH (§2) | SURVIVES | proof re-derived step by step from FLIP (1), (3), (4); latchviol 0 on the 11 instances and on 3,000 random genomes |
| Corollary LEAPFROG (§2) | SURVIVES for OFFs with t, t + 1 ∈ I (FLIP's convention). W-1: if «OFF at t ∈ I» also allows t + 1 ∉ I, the stated alternatives are incomplete; witness OFFUP_n4 (§3) | OFF classes on 11 + 3,000 genomes: 0 unexplained |
| latch hypothesis at the OFF steps | FAILS at every OFF step, as L-SI's latch86 says (0 of 14): mine finds 16 OFFs on the 11 instances, all of class «over» | §4 |
No break.

## 1. SAME-E-MERGE and the in-edge claim
- R104 [DEF] (P-N5-ASC §1 quotes it from trunk RESULTS l. 9864):
  - movers' edges go to their gates;
  - gate → {e, β};
  - β → {Ξ-target mover, u} or u alone;
  - e → W-target mover or c_W;
  - c_X and c_W are self-loops;
  - the core is K0 → {K1, K3}, K1 → {K0, K1}, K2 → {K1, K2}, K3 → {K1, K2}, with IDEAL-CYC freezing K0 → K3 and K1 → K1.
  No edge ends at a gate except its mover's, and none ends at an e except its gate's. So on Γ(G) the claim is literally true.
- Γ3 (P-N5-REACH §3 pads; gamma3.py l. 45-56 at trunk; my own3.py) inserts pads: x → m_q → g_q → {pe_q, pβ_q}, pe_q → e_q,
  pβ_q → β_q, β_q → {xt, pb_q}, pb_q → K0.
  - There the gate's in-edge comes from m_q, not from x, and e's in-edge comes from pe_q, not from g_q.
  - L-SI's citation «gamma3.py: succ[x] = the gates of x» holds only without pads (gamma3.py l. 45: m-pads when "m" in pads).
  - The conclusion is unchanged: m_q, g_q, pe_q and e_q each have in-degree 1, so a play through e_q passes x → m_q → g_q → pe_q → e_q.
  - WORDING SLIP (not a break): on Γ3, read «its gate» and «its mover» through the pads.
- In-degree by vertex class (DATA; unit: vertex; set: LT3_1_1 and CB3_61; counter: in-degree; own.build = Γ(G) with IDEAL-CYC's frozen core edges only, own3.build3 = Γ3):

  | class | Γ(G) | Γ3 |
  | --- | --- | --- |
  | mover x | 0-33 | 0-33 |
  | gate g, e, β | 1 | 1 |
  | m, pe, pβ, pb | — | 1 |
  | c_X | 1 (its own loop) | 1 |
  | c_W | 128 / 139 (every level-0 e + loop) | same |
  | K0 | 7 (X-exits) | 191 / 203 (every pb + q) |
  | K1 / K2 / K3 | 2 / 2 / 1 | 4 / 2 / 1 |
  | pA, s, q, r | — | 1 |

  The lemma needs only the e, gate (and, on Γ3, pe, m) rows, and those are 1 on all 11 instances in both builds (indeg1_G, indeg1_G3 =
  True). Movers, c_W and K0 have many in-edges, and the lemma does not claim otherwise.
- The consequence «E_t(w) ∩ E_t(g_o) ≠ ∅ ⇒ the plays merge, and the symmetric difference lies before the first common vertex» also holds:
  - plays are positional paths, so after a common vertex they coincide;
  - they then have the same cycle node, so membership in Π is the same on the common part.
  DATA: mergeviol 0 (unit: pairs of plays whose Π share an e but whose tails from that e differ; checked every third state; set: 11
  instances + 3,000 random genomes).

## 2. ACCESS-LATCH and LEAPFROG: proof read
- ACCESS-LATCH, step by step:
  - FLIP (1) needs only σ_t(B) = S and Λ_t(B) = λ ∈ {K1, K2}. It gives Odd's e at g_S, w's play not passing B, Λ(w) = λ, and e_S ∉ E_t(w).
  - e_S ∉ E_t(g_o) uses the hypothesis «no play from g_o passes B» plus the in-degree-1 chain of §1. OK.
  - {e_S} ∪ E(w) >lex E(w) ≥lex E(g_o), so FLIP's P_t holds; the reward clause is the hypothesis. FLIP (4) keeps S (unique best,
    via FLIP (3)'s lex reading of values with node λ). OK.
  - The «instance of the hypothesis» bullet (all routes enter X with dead e-faces, so all e-sets are ∅) is consistent. «E_t(X)» stands for
    the play through u, which has E = ∅.
- LEAPFROG is the contrapositive of ACCESS-LATCH plus FLIP (5). In FLIP's convention a flip «on I» has t, t + 1 ∈ I. Then an OFF to an
  option whose node has higher reward than λ is impossible: Howard would move B to a node ≠ λ, so t + 1 ∉ I. So the two listed alternatives
  (an overtaking g_o with node λ, or a g_o play passing B) are complete. OK.
- W-1 (wording): the corollary says «every OFF of S at t» without «t + 1 ∈ I». Read with only t ∈ I, there is a third cause: some
  other option reaches a node of higher reward, and B leaves λ. This needs no e-set overtaking at all. Such OFFs are bounded by the
  changes of Λ(B) (≤ 2M + 3, R118 (e)), so nothing downstream changes, but the corollary should say «t, t + 1 ∈ I» or list the third
  cause.

## 3. Witness for W-1: OFFUP_n4 (frozen experiments/red/r225/inst/OFFUP_n4.json, sha1 dd6a12215ffa397b26a92d35e44ae8e2c14b7395)
- Movers:
  - B (level 1): S = SET (W-target w, Ξ-target B, β even), start; o (W-target w′, Ξ-target z, β odd).
  - w, w′ (level 0): w exits to X; w′ goes to z.
  - z (level 0): EXIT (start) and SET (Ξ-target z, β even).
- Run (own.py, 3 states):
  - t 0: Λ(B) = Λ(g_o) = Λ(w) = K1.
  - t 1: z has switched to SET, so Λ(g_o) = β_z, an even node of higher reward than K1 (Odd cannot escape: both faces of g_o reach z).
  - t 2: B is on o and Λ(B) = β_z.
- The OFF at t = 1 has no overtaking g_o with node λ and no play passing B. latch225 classifies it «cross» (Λ_(t+1)(B) ≠ λ).

## 4. DATA: OFF classes and lemma counters (latch225.py)
Unit: (mover B, SET option S, state t) with Λ_t(B) ∈ {K1, K2}. Scope: IDEAL-CYC Howard (own.py, [E-LEV], cap 3000). Counters:
- on / off: σ_t(B) = S, and σ_(t+1)(B) = S / ≠ S;
- hyp: ACCESS-LATCH's hypothesis at an on-state;
- latchviol: hyp and OFF;
- OFF classes, first match: cross (Λ_(t+1)(B) ≠ λ), pass (a g_o play passes B), over (a g_o with node λ and E >lex E(w)), high, none;
- onev / onviol: ON with Λ(B) = λ at t and t + 1 / an o with node λ and E(g_o) ≥lex {e_S} ∪ E(w).

| set | states | on | off | cross | pass | over | none | hyp | latchviol | onev | onviol | mergeviol |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L-SI's 11 instances (inst86/, sha1 = pins.sha1, matched) | 145 | 283 | 16 | 0 | 0 | 16 | 0 | 283 | 0 | 60 | 0 | 0 |
| random Ξ-cyclic genomes, seed 2254 (latch225 rgen: levels 2-4, width 1-3, degree 2-3, 30 % SET options) | 10,754 | 1,697 | 319 | 235 | 56 | 28 | 0 | 776 | 0 | 325 | 0 | 0 |

- Per instance (out/latch86.txt), OFF counts: CB2_63 1, CB3_61 3, CB3_62 3, LT2_1_0 1, LT2_1_1 0, LT2_m1_0 1, LT2_m1_1 0, LT3_1_0 3,
  LT3_1_1 2, LT3_m1_0 2, LT3_m1_1 0. L-SI's table has 14 OFFs and differs at LT3_1_0 (2) and LT3_1_1 (1). My counter takes every SET option
  of every mover, while L-SI's takes the bits B_l only. The excess is 2, and both excess OFFs are also «over».
- Run lengths agree with L-SI's T (states = T + 1): LT2_1_x 11, LT2_m1_x 10, LT3_1_x 16, LT3_m1_x 14, CB2_63 9, CB3_61 18, CB3_62 16.
- On random genomes most OFFs are «cross» (235 of 319): there, cycle-node changes, not e-set overtaking, drive bit resets. That is
  TWO-COPY-RED's own «NOT excluded» case (cycle-node changes), and it is bounded by 2M + 3 per vertex.
