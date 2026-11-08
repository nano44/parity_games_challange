# Box 87: the leapfrog bound in POOL-ALT's shared-e case (L-SI successor 45; Lead 08:47Z 2026-11-08)
Written 2026-11-08 (date -u in the commit). Labels: PROVED (lane) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD (instance) / READING.
Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1).
Tool: experiments/si/box87/leap87.py (census; check87.sh, wired). Inputs: the frozen instances of boxes 84-86 (pinned there).

## 0. Answer
- PARTIAL. **Lemma LEAPFROG-ASC (PROVED, lane, §2)**: on an interval of FLIP-type with PRIV, the flips of a SET option S number at
  most |E_U| + 2k, where |E_U| = the number of e-vertices at least as relevant as e_S and k = the number of flips decided BELOW an
  e shared by both compared plays (type II). The potential is M_t := the most relevant e in a_t ∪ b_t; type-I flips (decided at the
  top) strictly raise it between opposite flips.
- Every type-II flip needs an ASCENT in the deciding play (it visits the decider z before a more relevant shared e s): this is
  SAME-E-MERGE (box 86 §1) applied to s.
- So the shared-e case of POOL-ALT is reduced, not closed: a SET bit's re-arms beyond |E_U| are all decided under a shared head by
  ascending plays. The potential on (pre-merge prefix, merge point) pairs does NOT bound k (§3, exact obstruction): with the shared
  head fixed, the residual parts below it are again a pair of monotone chains, so type-II flips NEST, and the nesting depth is
  bounded by nothing proved here. That is the e-set-height recursion of HUB-ASC-G with unbounded ascents (ASC-EXP), not a new
  obstruction. Witness: HP4_mup (box 84, frozen) has 7 type-II flips over its 4 bit units, up to k = 4 in one unit (§4).
- Scope (what it does and does not cover): SET-type bit options only, one Λ-interval with constant cycle nodes, PRIV, and the node
  hypothesis below. It says nothing about cycle-node changes, non-SET options (closed separately by P-QUIET, conditional on QUIET),
  or e-set changes at vertices that are not a bit's w or other gates.
- CONJECTURE TWO-COPY-RED's SET-counter branch therefore stays a CONJECTURE, now in the sharper form of §5.

## 1. Setting
FLIP's (L-RED R222 §4): B a mover, S a SET-type option (Ξ-target B), e-vertex e_S, w = succ(e_S); I an interval with Λ(B) = λ ∈
{K1, K2} and every cycle node constant. Hypotheses: (PRIV) on I no play from w or from any other gate g_o of B passes B; (NODE) every
o ≠ S has Λ(g_o) = λ or reward(Λ(g_o)) < reward(λ). π = U-projection onto e's at least as relevant as e_S (box 85 §2).
a_t := π({e_S} ∪ E_t(w)) (the e-face of S); b_t := max_lex over o ≠ S with Λ(g_o) = λ of π(E_t(g_o)). An EVENT is a step t → t + 1
in I where [σ(B) = S] changes; ON if it switches on, OFF if off.

## 2. Lemma LEAPFROG-ASC (PROVED, lane)
Facts used:
- (F1) a_t and b_t are lex-nondecreasing on I (E-MON + PROJ-MON; a maximum of nondecreasing chains is nondecreasing).
- (F2) ON at t ⇒ a_t >lex b_t (FLIP (5), U-form, box 85 §2 (5′)). OFF at t ⇒ b_t >lex a_t: by FLIP-U (4′) P^U_t fails; by NODE it
  fails at some o with Λ(g_o) = λ and π(E_t(g_o)) ≥lex a_t, and equality is impossible because e_S ∈ a_t while e_S ∉ E_t(g_o) (PRIV:
  g_o's play does not pass B, hence not g_S).
- (F3) Events alternate ON, OFF, ON, … (they are the changes of one 0/1 status).
At an event t let z_t := max(a_t Δ b_t) (it lies on the winning side by (F2)) and M_t := max(a_t ∪ b_t). The event is TYPE I if no
e of a_t ∩ b_t is more relevant than z_t (then z_t = M_t), TYPE II otherwise. k := #type-II events on I.

**Claim A.** M_t is nondecreasing on I. (F1: max a_t and max b_t are nondecreasing.)
**Claim B.** If t < t′ are type-I events of opposite directions, M_t′ is more relevant than M_t.
Proof (t OFF, t′ ON; the other order is symmetric with a and b exchanged). m := M_t = z_t ∈ b_t \ a_t, so max b_t = m. Suppose
M_t′ = m. By (F1), max b_t′ ≥ max b_t = m, and max b_t′ ≤ M_t′ = m, so m ∈ b_t′. But t′ is type I and ON, so M_t′ = z_t′ ∈ a_t′ \ b_t′:
m ∉ b_t′. Contradiction; with Claim A, M_t′ > m. ∎
**Claim C (type II ⇒ ascent).** At a type-II event t, let s ∈ a_t ∩ b_t be more relevant than z_t. Then s ≠ e_S (e_S ∉ b_t), so s lies
on w's play and on the play of the maximising g_o*. By SAME-E-MERGE both plays pass the mover of s and coincide from there; z_t lies
on exactly one of seq_t(e_S) = (e_S, seq_t(w)) and seq_t(g_o*), not on the common part, so that sequence visits z_t before s. As s is
more relevant than z_t, that e-sequence has an ascent between them. ∎
**Lemma.** #events on I ≤ |E_U| + 2k.
Proof. Delete the k type-II events from the event sequence. The type-I events fall into at most k + 1 maximal runs of consecutive
events. Inside a run consecutive events alternate (F3), so by Claim B the values M_t strictly increase along the run; by Claim A they
do not decrease from one run to the next. All values lie in E_U. So the type-I events number at most |E_U| + (number of runs − 1)
≤ |E_U| + k, and all events at most |E_U| + 2k. ∎
**Corollary LEAPFROG-NOASC.** If on I no play seq_t(e_S), seq_t(g_o) (o ≠ S, Λ(g_o) = λ) has an ascent at any event state, then S flips at
most |E_U| times on I.

## 3. Where the proof stalls (exact obstruction)
- A potential on (pre-merge prefix, merge point) pairs would have to bound k. At a type-II event the shared head H_t := {v ∈ a_t ∩ b_t :
  v more relevant than z_t} lies after the merge, identical on both plays, and the comparison is decided by the parts below it.
- If two consecutive events have the same head H and the same minimum θ of H, then by PROJ-MON the parts of a and b at or above θ are
  constant between them, so the parts below θ are again two lex-monotone chains, and Claims A-C apply to them with heads of their own.
  Type-II events thus NEST: the count is a recursion in the number of nested heads, the same recursion as the e-set heights of HUB-ASC-G
  (F′_B with B ascents per play). With unbounded ascents the abstract heights are exponential (L-NEW box 193 ASC-EXP), and nothing in
  SAME-E-MERGE or E-MON bounds the nesting depth. So the shared-e case reduces to «ascents of the bit's compared plays», i.e. to UP-B /
  U(G), not to a polynomial bound.
- This is an obstruction to the PROOF method, not a counterexample: no instance with super-polynomial k is known (§4: k ≤ 5).

## 4. DATA (leap87.py; out/leap87.out)
Unit: (real bit B_l, SET, maximal constant-node interval with Λ(B_l) ∈ {K1, K2}) with at least one event; set: HP2-HP5_mup (box 84),
the 11 box 85 and the 11 box 86 instances (all frozen, sha1 in their notes / pins); scope: box81/ref idealcyc. Counters: type-I and
type-II events; maxk = max k per unit; ascfail = type-II events whose deciding play has no ascent after z_t (Claim C predicts 0);
boundfail = units with #events > |E_U| + 2k + 1 (the machine check tests this slightly weaker form; the Lemma says |E_U| + 2k).
| instances | units | type I | type II | maxk | ascfail | boundfail |
| --- | --- | --- | --- | --- | --- | --- |
| HP2 / HP3 / HP4 / HP5_mup (h = 2-5) | 2 / 3 / 4 / 5 | 4 / 6 / 7 / 7 | 0 / 3 / 7 / 12 | 0 / 3 / 4 / 5 | 0 | 0 |
| TC2, TC2d, TC3, TC3d, TC3m, TC4m, TC5m | 21 | 39 | 24 | 4 (TC4m, TC5m) | 0 | 0 |
| CL2_21, CL2_22, CL3_31, CL3_32 | 9 | 13 | 13 | 5 (CL2_21) | 0 | 0 |
| box 86: LT* (8), CB2_63, CB3_61, CB3_62 | 28 | 47 | 2 | 1 | 0 | 0 |
| all 26 | 72 | 123 | 61 | 5 | 0 | 0 |
- Claim C and the bound hold everywhere. Type-II flips are a third of all flips; in the MIRROR family maxk grows with h
  (0, 3, 4, 5 at h = 2-5): linear, as the hub heights. The box 86 lag towers have almost no type-II flips (2 of 49): the merge
  makes the compared plays coincide above the bit (ACCESS-LATCH), so their flips are decided at the top.

## 5. CONJECTURE TWO-COPY-RED (box 87 form)
PROVED residue (unchanged): by T-QUIET / P-QUIET (L-RED, conditional on QUIET), an exponential run of N5′-xi on IDEAL-CYC needs
Σ_v D^tot_E(v) super-polynomial or many cycle-node changes. For SET bit counters, now PROVED: re-arms beyond |E_U| per interval are
type-II leapfrogs, each with an ascending compared play (LEAPFROG-ASC).
**CONJECTURE (READING, SET-counter branch only).** On IDEAL-CYC under [E-LEV], type-II leapfrogs of one SET bit within one interval
are polynomially many in N + M. Strongest DATA: maxk ≤ 5 on the 26 frozen instances of boxes 84-86 (h ≤ 5); no climb so far found a
counter (CNT ≤ 5 of 8 at h = 3). Not covered: cycle-node changes, non-hub e-set changes, non-SET options beyond P-QUIET.

## 6. Addendum: L-RED 59 on box 86 (claude/l-red 65ffc396, docs/red/R225-lag.md; Lead 09:31Z)
- SAME-E-MERGE, ACCESS-LATCH and LEAPFROG SURVIVE.
- Γ3 wording (box 86 §1): «gamma3.py: succ[x] = the gates of x» is true only without pads (gamma3.py l. 45). On Γ3 the edges into g and
  e come through the pads: x → m_(x,k) → g → pe_g → e. Each of m, g, pe, e has in-degree 1 (L-RED gives the table per vertex class), so
  SAME-E-MERGE and Claim C (§2) hold on Γ3 unchanged.
- Event convention: in LEAPFROG and here, an event is a step t → t + 1 with BOTH t and t + 1 in I (FLIP's convention). Read with only
  t ∈ I, a third kind of OFF exists: another option reaches a node of higher reward, so B leaves λ with no e-set overtaking (witness
  L-RED inst/OFFUP_n4.json, sha1 dd6a1221…). Those OFFs end the interval and are bounded by the Λ(B) changes (≤ 2M + 3). LEAPFROG-ASC
  (§2) is stated per interval with (NODE) and both endpoints in I, so it is not affected; the run total adds one per interval boundary.
- Counts: L-RED counts 16 OFFs on the 11 box 86 instances over EVERY SET-type option; latch86 counts 14 over the real bits' SET only.
