# Packet P-N5-FBCK (box 49): fallbacks per phase are bounded by configurations of the gates an Even choice can reach, f ≤ n_K·|𝒞^K_f(P)| (Theorem FB-C^K); this form ignores every Odd vertex no Even choice vertex reaches (plain readers), and n_K replaces n — every game
L-NEW successor 30 (Opus 5.5), D14 / D18, Lead reading L40. Lead's GO of 23:21Z (message to L-NEW): "a proof attempt on FB-C°, f ≤ n·|𝒞°_f| per
phase, by re-running FB-RISE_C / SAT_C (RESULTS R71) and SAT-FB / SAT-FB1 (RESULTS R73) in the read frame. Keep it packet-sized. If it holds,
freeze a packet." Written 2026-10-28 from 23:25Z (date -u). FROZEN at push: later text goes into a fixes file.
What this is and is not, plainly:
- It proves FB-C° for ONE reader-proof frame: K, the vertices reachable from an Even vertex of out-degree ≥ 2. A gate outside K (a plain
  reader, a reader behind forced Even vertices, any Odd structure no Even choice reaches) is dropped from the configuration, and n becomes n_K.
- It does NOT prove FB-C° for the read frame of docs/new/N5-READER-box49.md §8. A reader that an old Even CHOICE vertex points at by a
  never-used edge lies in K. On l121_cf_emb12 |𝒞^K_f| = 8 = f (§4). That case stays OPEN.
- It bounds f by a count of configurations; it does not bound that count (FB-LIN stays OPEN). Not a TARGET.md claim; no running-time bound;
  G-N5-TIME stays open.
Labels: PROVED (L-NEW 30, unrefereed) / DATA / OPEN / READING.
Source: docs/new/N5-READER-box49.md §7-§8 (working note). This packet governs.
Tools: experiments/new/box49/fbconf.py (the K-configurations and the check of the theorem; KVIOL must be 0); outputs experiments/new/box49/out/fbconf_*.txt, fbck_named.txt.

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §0 | Facts K1-K3 | PROVED (to sign; elementary) |
| §1 | Lemma FB-RISE^K | PROVED (to sign) |
| §1 | Lemma SAT^K, Lemma SAT-FB^K, Corollary SAT-FB1^K | PROVED (to sign) |
| §2 | Theorem FB-C^K and Corollary (i) (it implies RESULTS R73's FB-C′) | PROVED (to sign) |
| §2 | Corollary (ii) (plain readers leave 𝒞^K_f, n_K and f unchanged) | PROVED (to sign), under REFEREE's (R) as stated |
| §3 | what K does not cover | READING / OPEN (not to sign) |
| §4 | data | DATA (not to sign) |
- Premises (LANDED unless marked):
  - SPEC docs/new/N5-ssi-global.md S1-S5 with FIX 3 (an in-phase fallback is Even's); S2's Iσ; S4c's rule. Standing premise 1E-N3 (RESULTS
    R57), form P1, as in RESULTS R71.
  - RESULTS R71 (P-N5-FBC-box47, sha1 32d3776c…): the setting (configuration, C-state, H_C, LEV_C, B_C, 𝒞_f), (a) Lemma FB-RISE_C and its proof,
    (b) Lemma SAT_C and its proof (first part and the (MON) sandwich only). R71's premises: (MON) (RESULTS R15 (a) with R15 (d)); RESULTS R17
    (a) (V1), (V2); RESULTS R17 (b) Lemma P, Case A, with Ω := Ξ_t (question Q-A, YES by both referees of R70 / R71); R38 (a).
  - RESULTS R73 (P-N5-EPC-box48, sha1 9f48ded7…): Lemma SAT-FB and its proof, Corollary SAT-FB1, Theorem FB-C′.
  - For Corollary (ii) only: REFEREE's Theorem READER-INV under (R) (docs/referee/R-N5-READER.md at e83fd19d, §1; refereed by one referee,
    NOT landed). Corollary (ii) is stated as an implication from it.

## 0. Setting and Facts K1-K3 (every game)
As RESULTS R71: a phase P (λ and τ constant), Ξ_k the honest valuation, λ its cycle-node map, Q the Odd vertices of out-degree ≥ 2,
value(r) := (u, P(r), |r|) for a simple path r ending at a cycle node u of λ.
- K := the vertices reachable in G, by a path with ≥ 0 edges, from an Even vertex of out-degree ≥ 2. n_K := |K|; Q_K := Q ∩ K.
- Fact K1. K is closed under successors (if x ∈ K and y ∈ succ(x), y is reachable from the same Even vertex). Hence the honest play from
  x ∈ K stays in K at every state, and λ(x) ∈ K.
- Fact K2. Every Even vertex outside K has out-degree 1 (an Even vertex of out-degree ≥ 2 is in K by definition, with the path of 0 edges).
  So Iσ_k(x) = ∅ at every state for Even x ∉ K (S2: Iσ(x) ⊆ succ(x) ∖ {σ(x)}).
- Fact K3. If K = ∅ there is no in-phase fallback. An in-phase fallback is Even's (FIX 3) and needs Iσ ≠ ∅, which by K2 needs K ≠ ∅.
- A K-CONFIGURATION is C = σ̄|Q_K, and k is a K-C-STATE if σ̄_k|Q_K = C. H^K_C := G[K] with every Odd v ∈ K cut to its one edge σ̄_C(v)
  (C(v) for v ∈ Q_K, the unique successor otherwise). By K1, at a K-C-state the honest play from every x ∈ K is a play of H^K_C.
- LEV^K_C(k) := the largest j ≤ n_K − 1 such that Ξ_k(x) ⪰ value(r) for every x ∈ K and every simple path r of H^K_C with ≤ j edges from x
  to a cycle node of λ. B^K_C(x) := the maximum of value(r) over the simple H^K_C-paths r from x ∈ K to a cycle node of λ.
  LEV^K_C is defined at every state of P and is non-decreasing along P (H^K_C and λ fixed on P; (MON)). LEV^K_C ≥ 0: a 0-edge path has
  x = u a cycle node, and Ξ_k(u) = (u, ∅, 0) throughout the phase (as RESULTS R71's N-FBC-1).
- 𝒞^K_f(P) := the K-configurations of the sources of P's in-phase S4c fallbacks. It is the image of R71's 𝒞_f(P) under restriction to Q_K,
  so |𝒞^K_f(P)| ≤ |𝒞_f(P)|.

## 1. Lemmas FB-RISE^K, SAT^K, SAT-FB^K (PROVED, every game)
Lemma FB-RISE^K. Let t → t + 1 be an in-phase S4c fallback of P whose source t is a K-C-state. Then LEV^K_C(t + 1) ≥ min(LEV^K_C(t) + 1, n_K − 1).
Proof. RESULTS R71 (a)'s proof (P-N5-FBC-box47 §1), read with x ∈ K, H^K_C for H_C and n_K for n. Let x ∈ K, u a cycle node of λ, and r a
simple H^K_C-path from x to u with 1 ≤ |r| ≤ min(LEV^K_C(t) + 1, n_K − 1); r = x → z → r′, z ∈ K (K1), r′ avoiding x, |r′| ≤ LEV^K_C(t), so
Ξ_t(z) ⪰ value(r′).
- x Odd. If x ∈ Q_K, then z = C(x) = σ̄_t(x) because t is a K-C-state. Otherwise x has one successor. This is the only use of the configuration,
  and it is used only at vertices of K. The rest of R71's Odd case is verbatim: (V1), (V2), the subcase λ(x) = x, and (MON). Every vertex it
  names is x, z or a vertex of r′, all in K.
- x Even. R71's Even case, which is items 2 and 3 of FB-RISE (a)'s proof (P-N5-HONFF-box47), verbatim. It uses the edge (x, z) of G, the bound
  Ξ_t(z) ⪰ value(r′), S4c's rule at x, Lemma P's Case A at x with Ω := Ξ_t, (MON), (V1)/(V2) at t + 1, and λ_{t+1} = λ. Case A uses Ω only at
  x, at ρ(x) = σ_t(x) and at z (question Q-A of P-N5-HONFF §"Premises"). All these vertices lie in K by K1, and none of the steps uses the frame
  of r′.
So Ξ_{t+1}(x) ⪰ value(r) for every such x and r. □
Lemma SAT^K. If t is a K-C-state with LEV^K_C(t) = n_K − 1, then Ξ_t = B^K_C on K. If t < t′ are K-C-states of P with LEV^K_C(t) = n_K − 1, then
Ξ is constant on K on the states t, …, t′.
Proof. RESULTS R71 (b)'s proof, first part. At a K-C-state the honest play from x ∈ K follows a simple H^K_C-path r_x to its first visit of λ(x)
(K1), so Ξ_t(x) = value(r_x) ⪯ B^K_C(x). Every simple path in G[K] has ≤ n_K − 1 edges, so LEV^K_C(t) = n_K − 1 gives Ξ_t ⪰ B^K_C on K. For t′:
on K, Ξ_t = B^K_C ⪰ Ξ_{t′} (t′ a K-C-state) ⪰ Ξ_t (MON). So Ξ_{t′} = Ξ_t on K, and Ξ, being non-decreasing, is constant on K on t, …, t′. □
Lemma SAT-FB^K. Let t be a K-C-state of P with LEV^K_C(t) = n_K − 1 whose transition t → t + 1 is an in-phase S4c fallback. Then t + 1 is the last
state of P, or P has no K-C-state after t.
Proof. RESULTS R73's proof of Lemma SAT-FB (P-N5-EPC-box48 §3), with K. Let t′ > t be a K-C-state of P. By SAT^K, Ξ_{t+1} = Ξ_t on K.
- Iσ_{t+1} = ∅. For Even x ∉ K, by K2. For Even x ∈ K, succ(x) ⊆ K (K1), so S2 reads Iσ_{t+1}(x) from Ξ_{t+1} = Ξ_t on succ(x). Then R73's two
  cases follow verbatim. If Iσ_t(x) = ∅, x keeps its edge and Iσ_{t+1}(x) = ∅. If Iσ_t(x) ≠ ∅, σ_{t+1}(x) is the (Ξ_t(w), w)-maximum of
  Iσ_t(x), and nothing in succ(x) is Ξ_t-above it.
- The rest is R73's text verbatim: S4a keeps σ, then S4b changes τ, or S4c fires for Odd (FIX 3) and changes τ, or N5 stops. τ is constant
  on P, so t + 1 is the last state of P. □
Corollary SAT-FB1^K. For every phase P and K-configuration C, at most one in-phase fallback of P has a saturated K-C-state as its source (as R73's
SAT-FB1: a second one would be a K-C-state after the first, and would be the source of an in-phase transition after the last state).

## 2. Theorem FB-C^K and corollaries (PROVED, every game)
Theorem FB-C^K. In every phase P of N5 on every game, f ≤ n_K·|𝒞^K_f(P)|.
Proof. If K = ∅, f = 0 (K3). Otherwise fix C ∈ 𝒞^K_f(P) and let t_1 < … < t_N be the fallback sources of P that are K-C-states.
- Unsaturated sources (LEV^K_C(t_i) ≤ n_K − 2): by FB-RISE^K, LEV^K_C(t_i + 1) ≥ LEV^K_C(t_i) + 1, and LEV^K_C is non-decreasing on P. So
  consecutive unsaturated sources have strictly rising LEV^K_C in {0, …, n_K − 2}: at most n_K − 1 of them.
- Saturated sources: at most 1 (SAT-FB1^K).
So N ≤ n_K. Sum over C. □
- Corollary (i). n_K ≤ n and |𝒞^K_f(P)| ≤ |𝒞_f(P)|, so FB-C^K implies RESULTS R73's Theorem FB-C′ (f ≤ n·|𝒞_f(P)|).
- Corollary (ii) (an IMPLICATION from REFEREE's Theorem READER-INV under (R), which is not landed). Let G′ be G plus new vertices H such that:
  - no old vertex has an edge into H;
  - no Even vertex of H has out-degree ≥ 2;
  - the run on the old vertices, the fallbacks and the phases are unchanged (READER-INV gives this for a reader satisfying (R)).
  Then K(G′) = K(G): no new Even choice vertex is added, and no new vertex is reachable from an old one. So n_K, 𝒞^K_f(P) and f are the same
  for G′ as for G. The counts of Theorem FB-C^K cannot be inflated by such dressings. RESULTS R71 / R73's |𝒞_f(P)| can be inflated
  (N5-READER §7: l121_cf35_39, |𝒞_f| 5 → 8 = f).

## 3. What K does not cover (READING / OPEN; not to sign)
- An Even CHOICE vertex puts everything it reaches into K, even along an edge it never uses. The embedded reader of N5-READER §7
  (l121_cf_emb12: the old Even vertex 12 gets an edge to o) has o ∈ K, and |𝒞^K_f| = 8 = f there. The read frame of N5-READER §8 (gates on
  another vertex's honest play at some fallback source) drops o and gives 5. The CONJECTURE FB-C° in that frame stays OPEN.
  - Obstruction to the same proof: LEV in the read frame quantifies over H-paths 12 → o → …. To keep FB-RISE's Odd case at o one needs
    z = σ̄_t(o) at every source, which the read configuration does not fix.
- FB-LIN (f ≤ n per phase) is not implied: |𝒞^K_f| reaches 7 in data (§4).

## 4. DATA (not to sign; experiments/new/box49/fbconf.py, KVIOL = sources of one K-configuration above n_K, must be 0)
| set | runs | KVIOL | Σ |𝒞_f| / Σ |𝒞^K_f| | max fallbacks per K-configuration / n_K |
| --- | --- | --- | --- | --- |
| named (l121_* dressings, long121, si/root/instances incl. swlin_kill_n26) (out/fbck_named.txt) | 17 | 0 | 74 / 71 | 0.12 (swlin_kill_n26: 3 of n_K 26) |
| lib41, n ≤ 48, own start or S3 + 2 random, seed 7 (out/fbconf_lib41.txt) | 1,047 | 0 | 303 / 301 | 0.75 (box25/instances/wd16_s2: 12 of n_K 16) |
| L-RED instances, n ≤ 200, own start or S3 (out/fbconf_red.txt) | 311 | 0 | 125 / 123 | 0.78 (red/so/instances/farrise25_n32: 25 of n_K 32) |
- KVIOL = 0 everywhere (the counter is printed only when non-zero; it is absent from all three outputs). The most fallbacks from one
  K-configuration is 0.78 n_K, so the theorem's n_K is not approached; max |𝒞^K_f| is 4 (lib41, zcl_rx_n32) and 5 (L-RED, long121_n40).
- The dressings: |𝒞^K_f| = 5 on long121 and on its dressings l121_a, l121_b, l121_e100 and l121_cf35_39 (whose |𝒞_f| is 8). It is 8 on
  l121_cf_emb12 (§3).

## 5. Quotes and pins (checked by script)
Every «…» is verbatim at the tagged revision and lines; `python3 -I experiments/new/box49/quotecheck3.py docs/new/P-N5-FBCK-box49.md` prints
QUOTES PASS (pinned in experiments/new/check.sh with a shifted-line control that must fail).
- R71 (a): [Q docs/RESULTS.md@6d863a4d:3712] «(a) Lemma FB-RISE_C: if t → t + 1 is an in-phase S4c fallback whose source t is a C-state, then LEV_C(t + 1) ≥ min(LEV_C(t) + 1, n − 1).»
- R71 (b): [Q docs/RESULTS.md@6d863a4d:3715] «(b) Lemma SAT_C: if t is a C-state with LEV_C(t) = n − 1, then Ξ_t = B_C»
- R71's Odd case: [Q docs/new/P-N5-FBC-box47.md@6d863a4d:51] «x Odd. Then z = σ̄_C(x) = σ̄_t(x) (t is a C-state; outside Q, x has one successor)»
- R71's Even case: [Q docs/new/P-N5-FBC-box47.md@6d863a4d:55] «x Even. Items 2 and 3 of FB-RISE (a)'s proof verbatim: they use only the edge (x, z) of G»
- Q-A: [Q docs/new/P-N5-HONFF-box47.md@6d863a4d:33-34] «As I read box 10 §2, Case A uses only: Ω(z) ⪯ Ω(ρ(x)) with ρ := σ_t; the bound Ω(z) ⪰ value(r′); (V1) for Ω at the Even x»
- R73's SAT-FB: [Q docs/new/P-N5-EPC-box48.md@6d863a4d:97-98] «Lemma SAT-FB. Let t be a C-state of P with LEV_C(t) = n − 1 whose transition t → t + 1 is an in-phase S4c fallback. Then t + 1 is the last state of P, or P has no C-state after t.»
- R73's step for Even x: [Q docs/new/P-N5-EPC-box48.md@6d863a4d:100-101] «An Even x with Iσ_t(x) = ∅ keeps its edge, so Iσ_{t+1}(x) = Iσ_t(x) = ∅.»
- S2: [Q docs/new/P-N5-HONFF-box47.md@6d863a4d:23] «S2 (Iσ(x) = {w ∈ succ(x) : Ξ(w) ≻ Ξ(σ(x))})»
- READER-INV: [Q docs/referee/R-N5-READER.md@e83fd19d:14] «Theorem READER-INV (REFEREE; PROVED, every game): the same with the hypothesis (R)»
- Pins: P-N5-FBC-box47.md sha1 32d3776cf4090fb15c1d0cb4c8b4f59276f64e21; P-N5-EPC-box48.md 9f48ded742d7f44bbf82ae8ec9e0e88c46457700; fbconf.py:
  sha1 in the push message.
