# Box 86: the Q1 LAG TOWER (L-SI successor 45; Lead 07:12Z 2026-11-08)
Written 2026-11-08 (date -u in the commit). Labels: PROVED (lane) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD (instance) / READING.
Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1).
Tools: experiments/si/box86/ (lag86.py builder from cfg/*.json; latch86.py; climb86.py; check86.sh, wired). Measured with box85's
ana85 / dec85 / flipu85 / pool85 and box84's lb84 / priv84 (pinned in box85/pins.sha1).
Before the box (Lead 07:12Z): L-RED R223-q2 (claude/l-red 77b8946b) Lemma P-QUIET read; no hole found. (a) uses only DOM, CN2 and
quietness of the step; (b), (c) are QUIET / T-QUIET counting. Q2 reduces to Q1 as stated there (conditional on QUIET, now signed).

## 0. Answer
- The lag tower is DEAD as a counter at h = 2 and h = 3 (§3): with the w_l → real B_(l+1) access the bit LATCHES (sets once, never
  resets: LT2_1_1, LT3_1_1); without it the tower is MIRROR again (h = 2: 00 01 11 10 11, CNT 4; h = 3: CNT ≤ 3, one re-arm at most).
  Climbs: CLIMB_LINE.
- Exact obstruction (PROVED, lane):
  - **Lemma SAME-E-MERGE** (§1): an e-vertex has one in-edge, from its gate, whose one in-edge is from its mover. So two plays that
    contain the same e at the same time pass the same mover and coincide from there on. «The same upper e's, one count behind»
    must therefore be a copy prefix that MERGES into the real chain.
  - **Lemma ACCESS-LATCH** (§2): if B is on its SET option S and E_t(w) ≥lex E_t(g_o) for every other option o with B's cycle node
    (no play from g_o passing B), then B keeps S at t + 1. A merge of w_l into the real B_(l+1) gives exactly this (E(w_l) = E(B_(l+1))
    = E(g_UP)), so a merged waiting hub latches the bit.
  - **Corollary LEAPFROG** (§2): every OFF of B_l needs some other option's play to be STRICTLY above w_l's (lex) at that step, and every
    later ON needs {e_l} ∪ E(w_l) above all of them again. With w_l merged, the first never happens; so each re-arm needs w_l to sit on
    a copy route that is overtaken by the real chain and then overtakes it back (at the U-level, FLIP-U). The overtakes alternate
    between the copy pool and the real pool: POOL-ALT (box 85 §3) caps them by the pool sizes unless shared e's decide, and shared e's
    are post-merge (SAME-E-MERGE), equal on both sides at one time.
- CONJECTURE TWO-COPY-RED updated (§4): Q2 is closed by P-QUIET (L-RED R223 item 4, conditional on QUIET); Q1 now needs a waiting hub
  that leapfrogs the real chain 2^(h−l) times, and neither high, low nor merging copies do it on the data.

## 1. Lemma SAME-E-MERGE (PROVED, lane; structure of Γ(G), R104 §3.1 / gamma3.build)
- In Γ(G) the e-vertex e_(x,k) has the single in-edge g_(x,k) → e_(x,k), and the gate g_(x,k) has the single in-edge x → g_(x,k)
  (gamma3.py: succ[x] = the gates of x; succ[g] = {e, β}; no other vertex has an edge to g or e). A play is a path following σ and σ̄,
  so a play containing e_(x,k) contains x → g_(x,k) → e_(x,k), and from x on it follows the same edges as any other play at the same
  state that contains x. ∎
- Consequence: at one state, E_t(w) ∩ E_t(g_o) ≠ ∅ implies the two plays merge at a mover, and E_t(w) Δ E_t(g_o) lies on the parts before
  the merge. A lag can only live in a prefix of copies (different e-vertices), not in «the same e's».

## 2. Lemma ACCESS-LATCH and Corollary LEAPFROG (PROVED, lane; premises those of Lemma FLIP, L-RED R222 §4)
Setting: FLIP's (B, S, g_S, e_S, w, interval I with Λ(B) = λ ∈ {K1, K2} and constant cycle nodes).
**ACCESS-LATCH.** If σ_t(B) = S, no play from any other gate g_o of B passes B at t, every o ≠ S has Λ(g_o) = λ or reward(Λ(g_o)) <
reward(λ), and E_t(g_o) ≤lex E_t(w) for every o ≠ S with Λ(g_o) = λ, then σ_(t+1)(B) = S.
Proof. By FLIP (1), w's play does not pass B, so it does not pass g_S, and e_S ∉ E_t(w); likewise e_S ∉ E_t(g_o). Adding an element
raises a set in lex order, so {e_S} ∪ E_t(w) >lex E_t(w) ≥lex E_t(g_o). With FLIP (1) (Λ(w) = λ) and the
node hypothesis, FLIP's P_t holds, and FLIP (4) keeps S. ∎
- Instance of the hypothesis: w is on an option whose β-route enters X with a dead e-face, and every other option of B reaches X with
  dead e-faces only (UP and the RS2 lanes of pair84 / two85 / lag86). Then E_t(w) = E_t(X) = E_t(g_o).
**Corollary LEAPFROG.** On I, every OFF of S at t has some o with Λ(g_o) = λ and E_t(g_o) >lex E_t(w) (or a play from g_o passing B).
Every ON at t′ has {e_S} ∪ E_t′(w) >lex E_t′(g_o) for all such o (FLIP (5)). So between two ONs the alternative overtakes w strictly,
and before the next ON w (with e_S) overtakes back. By FLIP-U only the U-projections matter. ∎
- Machine check (latch86.py): at every OFF step, the hypothesis of ACCESS-LATCH fails (§3).

## 3. DATA
Unit: one Howard run of IDEAL-CYC(G) from the stored start; scope: box81/ref idealcyc; counters as box85 §4 (ana85: tog, CNT, REARM,
hubH, U(G), PRIV-FLIP excess) plus latch86 (OFF events; OFF events with w_l on its 'real' option; ACCESS-LATCH violations).
Hand instances (lag86 cfg: L = 1, 3, 6; copy lanes 2j + 2(h − l) + 1; cexit C; merge 1), set = the 8 below:
HAND_TABLE
CLIMB_DATA

## 4. CONJECTURE TWO-COPY-RED, updated
**CONJECTURE TWO-COPY-RED (box 86 form).** On IDEAL-CYC under [E-LEV], an exponential counter for N5′-xi needs, at some level l, a
waiting hub w_l and an alternative of B_l that leapfrog each other (LEAPFROG) about 2^(h−l) times in U-projection. Copies placed at
fixed relevance offsets (high mirrors, low copies, box 85) or merging into the real chain (lag tower, this box) do not leapfrog
more than O(h) times.
- PROVED parts: FLIP, FLIP-A / FLIP-ALL, P-QUIET (L-RED; P-QUIET conditional on QUIET); FLIP-U, LOW-NULL, POOL-ALT (box 85);
  SAME-E-MERGE, ACCESS-LATCH, LEAPFROG (here); LOWER-BLIND (keep), LIVE-BREAK, LOCK-UP (boxes 83-84).
- Strongest DATA: box 85 §4 (11 frozen instances, 882 sweep genomes, 4 climbs) and §3 here: CNT ≤ 5 at h = 3, re-arms ≤ 2, hub heights
  linear (8 / 11 / 15 at h = 3 / 4 / 5), 0 lemma exceedances.
- Open (not excluded by anything proved): a waiting hub whose leapfrogs are decided by SHARED e's in different positions across
  time (POOL-ALT's open case). A proof would need a potential on (pre-merge prefix, merge point) pairs; not found.
