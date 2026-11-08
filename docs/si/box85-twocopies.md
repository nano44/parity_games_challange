# Box 85: TWO COPIES PER LEVEL (L-SI successor 45; Lead GO 05:06Z 2026-11-08)
Written DRAFT (date -u in the commit). Labels: PROVED (lane) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD (instance) / READING.
Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1).
Tools: experiments/si/box85/ (two85.py builder; ana85.py; dec85.py; flipu85.py; climb85.py; sweep85.py; check85.sh, wired).

## 0. Answer
(filled below)

## 2. Lemma FLIP-U (PROVED, lane): FLIP counts only e's at least as relevant as e_S
Setting and premises exactly as L-RED's Lemma FLIP (R222 §4, claude/l-red 5fdb96b3): B a mover, S a SET-type option of B (Ξ-target B,
any β-parity), gate g_S, e-vertex e_S, w = succ(e_S); I an interval with Λ(B) = λ ∈ {K1, K2} and Λ(w), Λ(g_o) constant for o ≠ S.
For a set X of e-vertices let π(X) := {v ∈ X : v is at least as relevant as e_S} (the U-projection). D_U,I(v) := number of distinct
π(E_t(v)), t ∈ I.

Claim: #flips of [σ(B) = S] on I ≤ 1 + (D_U,I(w) − 1) + Σ_(o ≠ S) (D_U,I(g_o) − 1). Since D_U ≤ D_E, this sharpens FLIP.

Two order facts (lex order on finite sets of e's = compare at the most relevant element of the symmetric difference):
- (PROJ) If e_S ∈ X and e_S ∉ Y, then X >lex Y ⟺ π(X) >lex π(Y). Proof: e_S ∈ X Δ Y, so z := max(X Δ Y) is at least as relevant
  as e_S; hence z ∈ π(X) Δ π(Y) = π(X Δ Y) and is its maximum, on the same side. ∎
- (PROJ-MON) X ≤lex Y ⇒ π(X) ≤lex π(Y). Proof: if max(X Δ Y) is at least as relevant as e_S, it is also max(π(X) Δ π(Y)); otherwise
  π(X) = π(Y). ∎

Proof of the claim. Define P^U_t := [Λ(w) = λ, and for every o ≠ S: reward(Λ(g_o)) < reward(λ), or (Λ(g_o) = λ and
π({e_S} ∪ E_t(w)) >lex π(E_t(g_o)))]. FLIP's P_t is the same with π dropped.
- (4′) on → off forces ¬P^U_t. Let σ_t(B) = S and P^U_t. For each o with Λ(g_o) = λ:
  - if g_o's play does not pass B, it does not pass g_S (only in-edge from B), so e_S ∉ E_t(g_o); by (PROJ), P^U's clause for o equals
    P's clause for o;
  - if g_o's play passes B, it continues B g_S e_S w …, so E_t(g_o) ⊇ {e_S} ∪ E_t(w), π(E_t(g_o)) ⊇ π({e_S} ∪ E_t(w)), and the clause
    for o fails, so P^U_t fails: excluded.
  So P^U_t ⇒ P_t, and FLIP (4) gives σ_(t+1)(B) = S.
- (5′) off → on forces P^U_t. If σ_t(B) ≠ S, FLIP (2) gives e_S ∉ E_t(g_o) for every o, so by (PROJ) P^U_t ⟺ P_t, and FLIP (5) applies.
- (6′) P^U_t changes only where some π(E_t(w)) or π(E_t(g_o)) changes. By E-MON each E_t(v) is lex-nondecreasing on I, so by
  (PROJ-MON) each π(E_t(v)) is too, and it changes at most D_U,I(v) − 1 times. FLIP (6)'s counting finishes the proof. ∎

**Corollary LOW-NULL (PROVED, lane).** An e-vertex less relevant than e_S never enters the bound for S. Under [E-LEV] (e's ordered by
level, R104 packet 3.1) this covers every e of a level below lev(B), and a copy of bit l whose e lies at level l BELOW e_SET_l (the
two-copies LOW copy). So the low copy of bit l and the whole lower counter cannot raise the number of flips of B_l's SET by even one:
B_l's flips are bounded by the distinct UPPER parts of the plays of w_l and of B_l's other gates.
- The low copy of bit l is visible only to bits j < l (there it lies above e_SET_j): to them it is one more e at level l, i.e. one more
  digit value, as box 84's CYC option was.

## 3. Lemma POOL-ALT (PROVED, lane; order fact) and what it asks of a counter
**Lemma POOL-ALT.** Let c_1 <lex c_2 <lex … <lex c_m be finite sets of e-vertices, c_i ⊆ P_A for odd i and c_i ⊆ P_B for even i, with
P_A ∩ P_B = ∅. Then m ≤ |P_A| + |P_B| + 1.
Proof. For consecutive c_i <lex c_(i+1) from disjoint pools, c_i Δ c_(i+1) = c_i ∪ c_(i+1), so its maximum lies in c_(i+1):
max c_(i+1) is more relevant than max c_i (max ∅ := −∞). The maxima strictly increase and lie in P_A ∪ P_B ∪ {−∞}. ∎
Use (READING, from FLIP-U's proof): between two consecutive ON events of S, P^U fails at least once, and each ON event needs
a_t := π({e_S} ∪ E_t(w)) >lex b_t := max_o π(E_t(g_o)) (over the o with node λ), each OFF event needs b_t ≥lex a_t. Both chains are
monotone (PROJ-MON). Under PRIV (no play from w or from the g_o passes B), e_S ∈ a_t \ b_t at every t, so b_t ≠ a_t. Then for
ON events t_1 < t_3 < … with OFF events t_2, t_4, … between them: b_(t1) < a_(t1) ≤ a_(t2) < b_(t2) ≤ b_(t3) < a_(t3) < …, so k ON
events give a strict interleaved chain of length ≥ 2k − 1, alternating between a's (pool: e_S and the e's above it reachable from w)
and b's (pool: the e's above e_S reachable from the other gates). By POOL-ALT, if the e's above e_S reachable from w and
from the other gates form disjoint pools, k is at most linear in the number of e's. So an exponential bit needs plays from w and from
another gate of B that reach COMMON e's above e_S, with a's reaching each new common value one step later than b's: a lagging copy
of the upper counter that merges into the same upper e's.
