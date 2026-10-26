# Packet P-N5-FBK (box 44): in-phase fallbacks per phase are polynomial whenever every honest class has boundedly many Odd choice vertices (ROUTE-k, SAT-k, Theorem FB-kT; on 𝒞^kO with k fixed, f = O(n^{k+1}) per phase), and Odd's alternations at Q raise Ξ (Lemma ALT)
L-NEW successor 23 (Opus 5.5), D14 / D18, Lead reading L40; Lead's order 04:19Z (Lead's stamp). Written 2026-10-26 04:22Z (date -u).
STATUS: DRAFT until P-N5-2T's sha1 is in; FROZEN at the push that fills it (later text goes into a fixes file).
Source: docs/new/N5-FBF-box44.md §10, §11 (working doc; this packet governs). Labels: PROVED (L-NEW 23, unrefereed) / READING / OPEN /
DATA. Not a TARGET.md claim: FB-kT bounds in-phase fallbacks only; nothing here bounds N5's running time on any class beyond 𝒞^1O ∪ 𝒞^1E.
G-N5-TIME stays open.

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | Lemma ROUTE-k | PROVED |
| §2 | Lemma SAT-k | PROVED |
| §3 | Theorem FB-kT and Corollary FB-kO | PROVED |
| §4 | Lemma ALT and its corollary (N_ep reduction) | PROVED |
| §5 | the model obstruction to a sum bound; data; the missing pieces for 𝒞^kO | READING / DATA (not to sign) |
- Premises:
  - LANDED: RESULTS R56 (P-N5-FBRED with its fixes file): (a) facts (Aκ), (M2κ), (SP′), (YB as used there), κ-FB-ROUND_D; (b) κ-HAT-FREEZE_D;
    (d) κ-Y-FORM_D with Y^q_t := {y ∈ succ(q) ∩ U_c : y's honest play at t avoids q} (fixes N-FBRED-2); (f) Theorem FB-RED, late form
    f ≤ 1 + (n − 1) + (n − 1)·N_late. RESULTS R54 (e) Corollary Φ-kO (phases). R15 (a).
  - IN REVIEW (L-SI successor 11): packet P-N5-2T, docs/si/P-N5-2T-box16.md, sha1 P2T_SHA1: Lemma PFZ-q (κ-PFZ needs only its own
    terminal's run constant) and Lemma DIR (a direct terminal's κ lies in A_q after g_{|U_c|−1}). This packet is CONDITIONAL on those two.
- Notation (R56 §0): phases, g_j (source states), Q, C, T, U_c, κ, κwt_c, G_c, G_c^q, κopt_c, κopt^q, Q-runs; and from P-N5-2T: Q_c :=
  (Q ∩ U_c) ∖ {c}, m_c := |Q_c|, w_c := |U_c| − 1, d_q := |succ(q) ∩ U_c|, DIRECT (q on its own honest cycle, or q's honest play visits c
  before any other terminal of Q_c), A_q (|A_q| ≤ d_q + w_c), q-run (maximal run with κ(q) constant), f^Θ_j. N_late := the number of
  Q-runs holding a fallback g_j with j ≥ n (R56 (f)). Late fallbacks i = 1, 2, … are those g_j with j ≥ n, with source states k_1 < k_2 < …;
  x_i(q) := κ_{k_i}(q).

## 1. Lemma ROUTE-k (PROVED, every game)
For a state t and q ∈ Q_c not direct at t, let par_t(q) := the first vertex of Q_c ∖ {q} on q's honest play at t (it exists, before c,
since q is not direct). Then the relation q → par_t(q) has no cycle. So every chain ends at a direct terminal, and the DEPTH of q (the
number of steps to a direct terminal) is ≤ m_c − 1.
Proof. If par_t(q) = p, then from its visit of p on, q's honest play is p's honest play (positional strategies). A cycle q = p_0 → p_1 →
… → p_r = q (r ≥ 1) puts p_1, p_2, …, p_r = q on q's play in this order, so q's play visits q again: q lies on the cycle of its own honest
play, i.e. q is on its own honest cycle, so q is direct, against the assumption. □

## 2. Lemma SAT-k (PROVED, every game; uses PFZ-q)
Let t > g_{w_c} be a state of the phase, q ∈ Q_c not direct at t, p := par_t(q), Θ_p the p-run containing t, and t > f^{Θ_p}_{w_c}. Then
κ_t(q) ∈ S_{q,p} + κ_t(p), where S_{q,p} := {κwt_c(q) + κopt^p(y) : y ∈ succ(q) ∩ U_c ∖ T, κopt^p(y) defined} ∪ {κwt_c(q) : p ∈ succ(q)};
|S_{q,p}| ≤ d_q.
Proof. Let y := next_t(q) = σ̄_t(q). By (Aκ), y ∈ U_c and κ_t(q) = κwt_c(q) + κ_t(y). y's honest play is the rest of q's play; it avoids q
(q is not on its own cycle), and its first vertex of Q_c is p, which comes before c.
- If y = p: κ_t(q) = κwt_c(q) + κ_t(p).
- Otherwise y ∉ T (it is neither c, since p precedes c, nor a terminal, since p is the first one).
  - "≤": the prefix of y's play up to p is a simple path ((SP′)) avoiding T ∖ {p}, with Even edges σ_t's and forced Odd vertices, i.e. a
    path of G_c^p; (Aκ) along it gives κ_t(y) = κwt_c(prefix ∖ {p}) + κ_t(p) ≤ κopt^p(y) + κ_t(p).
  - "≥": PFZ-q (P-N5-2T) at t ∈ Θ_p with t > f^{Θ_p}_{w_c}: simple paths of G_c^p have ≤ w_c edges, so κ_t(y) ≥ κopt^p(y) + κ_t(p). □

## 3. Theorem FB-kT and Corollary FB-kO (PROVED, every game; conditional on P-N5-2T's PFZ-q and DIR)
Theorem FB-kT. In every phase, with D_c := max_{q ∈ Q_c} d_q + w_c (≤ 2n) and V_q := the number of distinct values x_i(q) over the late
fallbacks:
  N_late ≤ 1 + Σ_c Σ_{q ∈ Q_c} (V_q − 1), and V_q ≤ Σ_{h=0}^{m_c − 1} D_c·((m_c − 1)·D_c)^h ≤ m_c·D_c·((m_c − 1)·D_c)^{m_c − 1}.
With R56 (f) (late form): f ≤ 1 + (n − 1)(1 + N_late).
Proof.
1. Outer count. Two late fallbacks lie in one Q-run iff their tuples (x_i(q))_{q ∈ Q} are equal: by (M2κ) every coordinate is
   non-decreasing along the phase, so equal tuples at k_i < k_{i′} force all κ(q) constant in between, and conversely. The tuple
   sequence is coordinatewise non-decreasing, so each change of tuple raises at least one coordinate to a value that coordinate never had
   before. So N_late = #distinct tuples ≤ 1 + Σ_q (V_q − 1). (Cycle nodes c ∈ Q have κ(c) = (0, 0) constant and contribute 0.)
2. Values by depth. Let V_{q,h} := the number of distinct x_i(q) over the indices i at which q has depth h at k_i (ROUTE-k). Every k_i
   satisfies k_i > g_{n−1} ≥ g_{w_c}.
   - h = 0 (q direct at k_i): x_i(q) ∈ A_q by DIR (P-N5-2T); V_{q,0} ≤ |A_q| ≤ D_c.
   - h ≥ 1: let p := par_{k_i}(q), of depth h − 1 at k_i. Fix p and a value α. The indices with x(p) = α are consecutive and their source
     states lie in one p-run Θ ((M2κ)). Every index of that block after its first w_c indices has k_i > f^Θ_{w_c} (the first w_c indices are
     fallbacks of Θ with earlier source states), so SAT-k gives x_i(q) ∈ S_{q,p} + α. So the indices with parent p and x(p) = α give ≤
     w_c + d_q ≤ D_c values of x(q). The values α that occur here are values of x(p) at indices where p has depth h − 1: at most
     V_{p,h−1}. Hence V_{q,h} ≤ Σ_{p ∈ Q_c ∖ {q}} D_c·V_{p,h−1}.
   - Induction on h: max_q V_{q,h} ≤ D_c·((m_c − 1)·D_c)^h; and h ≤ m_c − 1 (ROUTE-k).
3. V_q ≤ Σ_{h=0}^{m_c−1} V_{q,h}. □
Corollary FB-kO. On 𝒞^kO (exactly k Odd choice vertices, so Σ_c m_c ≤ k), every phase of every N5 run from every start pair has
N_late ≤ 1 + k·(2n)·k·(2(k − 1)n)^{k−1} and f ≤ 1 + (n − 1)(1 + N_late) = O(k^{k+1}·2^{k}·n^{k+1}); for fixed k, f = O(n^{k+1}). With R54 (e)
(phases ≤ n(n − 1) + ∏_q deg(q) ≤ n(n − 1) + n^k), the in-phase fallbacks of a whole run are O(n^{2k+1}) for fixed k.
Proof. m_c ≤ k and D_c ≤ 2n in the theorem; the sum over terminals has ≤ k terms. All statements used are per phase and start-free
(R56's are; ROUTE-k and SAT-k are statewise or run-internal). □
- Check against L-SI's FB-2T (P-N5-2T): for k = 2, FB-kT gives N_late ≤ 1 + 2(V − 1) with V ≤ D + D², i.e. O(n²), the same order.

## 4. Lemma ALT (PROVED, every game) and the N_ep reduction
Let t → t+1 be an in-phase transition, q ∈ Q_c with q ≠ c, y1 := σ̄_t(q) ≠ y2 := σ̄_{t+1}(q). Call the change CLEAN if q lies on no honest
cycle at t and at t + 1, and y2's honest play at t avoids q. Then for a clean change κ_{t+1}(q) ≥ κ_t(q), with equality only if
κ_t(y2) = κ_t(y1) and κ_{t+1}(y2) = κ_t(y2) (a TIE at t).
Proof. κ-Y-FORM_D (R56 (d)) at t + 1: κ_{t+1}(q) = κwt_c(q) + κ_{t+1}(y2), with y2 ∈ U_c. (M2κ): κ_{t+1}(y2) ≥ κ_t(y2). y2 ∈ Y^q_t (clean),
so κ-Y-FORM_D at t gives κ_t(y2) ≥ min_{y ∈ Y^q_t} κ_t(y) = κ_t(y1) = κ_t(q) − κwt_c(q). Equality throughout is the tie. □
Corollary (N_ep). An EPOCH of a phase is a maximal run with σ̄|Q constant; N_ep := their number. Then N_ep ≤ 1 + Σ_{q ∈ Q}(ρ_q + tie_q +
nc_q + cyc_q), where ρ_q counts the transitions of the phase changing Ξ(q), tie_q the clean ties at q, nc_q the non-clean changes at q,
and cyc_q the changes at q while λ(q) = q. Proof: an epoch ends only at a transition where some σ̄(q) changes; classify it by ALT. □
- Reading: by ALT, counting σ̄-changes at Q (epochs) and counting Ξ-changes at Q (ρ, R56 (f)) are the same up to ties and non-clean
  changes; there is no separate potential for Odd's alternations.

## 5. Not to sign
### 5.1 Model obstruction to a SUM bound (a statement about the lemmas used, not about N5)
- Where FB-kT is nested: step 2, per value α of the parent the child may take up to d_q values (one per shift in S_{q,p}); step 1 already
  sums over terminals, only V_q is a product over depth.
- Claim (PROVED as stated): the constraints used in §3 (ROUTE-k, DIR, SAT-k, (M2κ), and the w_c-saturation rule) admit abstract tuple
  sequences with Π over a chain of d values per level, i.e. V_q of order D^{depth}. Construction: a chain q_1 (direct, values α_1 < … < α_a in
  A_{q_1}) ← q_2 ← … ← q_h (par(q_{r+1}) = q_r), shift sets S_r = {s_{r,1} < … < s_{r,d}} chosen so that s_{r,d} + (any value of q_r) <
  s_{r,1} + (the next value of q_r); list the tuples lexicographically (q_1's value first, then the shifts of q_2, …, q_h), inserting w_c
  filler indices after each new value of each parent; every coordinate is non-decreasing, every direct value lies in A, every saturated
  index satisfies SAT-k, and the routing is a fixed chain (ROUTE-k). So no sum bound follows from these lemmas alone.
- Candidate extra ingredient (OPEN): Odd's minimum at q (κ-Y-FORM_D). Inside a block with the parent's value fixed and its run saturated,
  the successors of q routed through p have frozen values κopt^p(y) + α, so x(q) can rise only when some successor of q changes its first
  terminal (an Even switch on that successor's play). A sum bound would need "no rise of x(q) inside a parent block"; not shown, and no
  N5 instance either way.
### 5.2 Data
- None new for FB-kT: the late regime (j ≥ n) is vacuous in every sample and climb of both lanes and both referees (R56 fixes N-FBRED-4:
  max f − n = −2 in the library, −4 in climbs); ROUTE-k, SAT-k and FB-kT rest on their proofs.
- ALT (experiments/new/box44/altcheck.py, canonical S3 start): lib41 2,051 in-phase σ̄(q) changes, 1,910 clean strict, 75 clean ties, 65
  non-clean (9 with q on an honest cycle at an end, 56 with y2 routed through q), 1 at a cycle node; box-43/44 instances + lap_n6 36;
  2,000 random 𝒞^kO games 33; 0 violations.
- σ̄|Q repeats inside a phase (so N_ep has no ∏ deg bound): experiments/new/box25/laps/lap_n6_s1_110421.pg (n 6, Q = {2}, sha1
  4f4fe69c51e1c6f170c9c732feca025da70e7edb), σ̄(2) = 0, 4, 0 in one phase (P-N5-ACCEL §4).
### 5.3 What N5 on 𝒞^kO (k fixed, k ≥ 2) still needs (READING)
phases (R54 (e), landed) × fallbacks per phase (this packet, conditional on P-N5-2T) are polynomial; still OPEN: (i) crossings per phase
(R30 (c) / R34 (f) on 𝒞^1O; needs R-STICK in set form); (ii) transitions per phase given f (R50 (h) on 𝒞^1O; blocked at LEN / Δ-RT on the
frontier); (iii) Lemmas BIT and OUT beyond 𝒞^1O (R51; OUT's proof read as game-general by REFEREE's §C on DUAL; BIT is game-free).
