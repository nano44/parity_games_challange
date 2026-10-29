# T39: τ-changes (phases) per λ-run — what the repo has, and what the literature bounds about the opponent's strategy changes (L-LIT, 2026-10-29)

Asked by the Lead at 12:01Z (date -u). Count (2) of the new open core: **phases (τ-changes) per λ-run on general games** (L-SI 390d2d8a
§13: carries arise in τ-quiet λ-runs, i.e. inside phases).

**Labels.**
- PROVED (Rxx) = landed.
- PROVED (lane, SHA).
- PROVED (L-LIT, unrefereed) = composition written here.
- DATA, READING, CONJECTURE, OPEN, DEAD.

Every line carries its source.

## 0. Answer in short
- **Count (2) is already REDUCED, by the τ-side of L-SI's COMPOSE (b), to the Odd-side carry count NM*^U.**
  - Every τ-change is an Odd switch. Odd switches are bounded exactly like Even switches, on G^d.
  - #τ-changes over a whole run ≤ n(n − 1) + m_O·n·(n(n − 1) + 1)·(P*^U + 1), with P*^U ≤ (n²/2)(NM*^U + 1) + NM*^U by MΦ on G^d.
  - So phases per λ-run ≤ that + 1.
  - Status: PROVED (L-LIT, unrefereed) as a reading of COMPOSE (b)'s proof (lane, l-si f372bc6b) + MΦ (P-N5-MPGS (A), under review).
- **So the open core is again the two carry counts NM* and NM*^U.**
  - Item (1), carries per vertex per phase, is ≤ NM* restricted to a phase.
  - Item (2) reduces to NM*^U.
  - No new count appears. READING.
- **Landed results bound τ-changes only on few-Odd-choice classes.** R47 Φ-1O: one Odd choice. R54 Φ-kO: phases ≤ n(n − 1) + ∏ deg(o_i),
  exponential in the number of Odd choice vertices.
- **The literature bounds the OPPONENT's best-response changes (σ̄, τ̄ in N5 terms) only through a discount (HMZ) or a forward-game
  hypothesis (Mei-Sun-Ye).** Both are BLOCKED for N5. In Friedmann's families the best response changes exponentially often.
  - N5's τ is not a best response. It is Odd's own improving strategy, so the right literature for τ-changes is symmetric strategy
    improvement. There, Schewe-Trivedi-Varghese give no bound, and van Dijk-Loho-Maat give an exponential lower bound for rules N5 does
    not follow.

## (a) The repo

| # | statement | status | source |
| --- | --- | --- | --- |
| 1 | λ changes ≤ n(n − 1); λ^U (Odd's dual cycle nodes) only fall, ≤ n(n − 1) changes; ≤ 2n(n − 1) + 1 joint λ-runs | PROVED (R47 (a), Lemma Φ, every game) | docs/RESULTS.md R47 |
| 2 | one Odd choice vertex o: τ changes ≤ deg(o) − 1 over the whole run; phases ≤ n(n − 1) + deg(o) | PROVED (R47, Corollary Φ-1O) | R47 |
| 3 | every game: phases ≤ n(n − 1) + ∏ deg(o_i) (τ never repeats); one Even choice: σ changes ≤ d_e − 1 | PROVED (R54, Corollary Φ-kO; mirror results) | R54 |
| 4 | in-phase fallbacks on one-Odd-choice games ≤ 1 + (n − 2)(2n − 1) (a per-phase count, not a phase count) | PROVED (R48) | R48 |
| 5 | inside an epoch of Odd's BEST RESPONSE (σ̄ constant within a phase), honest values freeze after n − 1 fallbacks: f ≤ 1 + n·N_ep. Epochs count σ̄-changes, not τ-changes | PROVED (R60, Lemma EPOCH) | R60 |
| 6 | K9 reading: #iterations ≤ C·n³·(2 + σ̄-changes + τ̄-changes) | SIGNED CONDITIONAL on (P*)/(P_strict), which are FALSE (CDAG_n, l-new de4b588); the route is CLOSED | docs/GAPS.md G-N5-TIME row |
| 7 | **τ-changes ≤ n(n − 1) + m_O·n·(n(n − 1) + 1)·(P*^U + 1) on every game.** A τ-changing transition either changes λ^U (≤ n(n − 1), item 1) or carries an Odd switch inside a λ^U-run. Those are bounded by SW-RETURN + LEN-MONO on G^d (Odd's S4b and S4c switch along Iτ; R15 (a), (d) hold on G^d) | PROVED (L-LIT, unrefereed; the τ-half of COMPOSE (b)'s proof, lane, l-si f372bc6b, docs/si/N5-CHG-box28.md §9) | COMPOSE (b) |
| 8 | with MΦ on G^d: P*^U ≤ (n²/2)(NM*^U + 1) + NM*^U, so phases per λ-run ≤ poly(n)·(NM*^U + 1) | PROVED (composition of item 7 + MΦ, P-N5-MPGS (A), under review) | item 7; docs/lit/P-N5-MPGS.md |
| 9 | Odd-side data: Odd-side PCH ≤ 13 on the corpora; at most 28 λ^U-runs in one run | DATA | N5-CHG-box28 §9 (f372bc6b) |
| 10 | H_n (Friedmann's switch-best family): τ changes n times from start F (one gate per iteration, then fixed), n from S3; at most 2 changes at any gate over 1,612 starts | DATA | claude/l-comp experiments/friedmann-hn/README.md §2, §4 |
| 11 | dual(H_n), where Odd is the counting player: τ changes at every iteration, phases = iterations + 1 (F start: 35 phases for 34 iterations at n = 3); τ re-flips at one Odd vertex up to 14-18 times; all linear | DATA | same, §5 |
| 12 | L-SI §13: carries occur in τ-quiet λ-runs (no Odd switch, no open Odd gate on the vertex's plays) on runquad, s3quad, dlsep_kill_n70. T37 §3's multiplicative conjecture (carries ≤ poly × gate reopenings) is DEAD there | DATA; DEAD | claude/l-si 390d2d8a, N5-CHG-box28 §13 |

- Item 7 in one line: τ-changes are Odd's carries in disguise. By N5's mirror symmetry (R54 Lemma DUAL), the τ-side of the run is an
  "Odd first" N5 run on G^d. Its switches are paid by rises of its successors' dual valuations, as Even's are.
- READING: the reduction of count (2) to NM*^U needs nothing beyond what COMPOSE (b) already uses. A separate phase-count lemma is not
  needed for polynomiality, only for sharper exponents.

## (b) The literature on the opponent's strategy changes

| # | source (opened; sha256 in notes/L-LIT.md) | what changes, what bounds it | N5 object | verdict |
| --- | --- | --- | --- | --- |
| 13 | Hansen-Miltersen-Zwick, arXiv 1008.0530 v1, Def. 2.6 (optimal counter strategies), Thm 6.5 (p.11) | Player 2 always plays an optimal counter strategy τ2(π1); iterations ≤ (m + 1)(1 + log_{1/γ}(n²/(1 − γ))). So Player 2's best response changes ≤ iterations | σ̄ (Odd's best response to σ) | BLOCKED by the constant discount γ: needs the contraction (T30 §1, ALTLIT §3); N5's order is the γ → 1 lexicographic limit |
| 14 | Mei-Sun-Ye, arXiv 2606.29568 v1, Def. 7 (TBDFG: "no directed cycle involving actions from both players"), Lemma 10 (p.15), Lemma 11 (p.15) | Player 2 exact best reply; after O(n log n) Player-1 cycle-creating rounds some Player-1 action is eliminated; strongly polynomial | σ̄ inside one-Odd-choice o-acyclic games | BLOCKED by the forward hypothesis (no mixed cycle). R18 already covers N5's o-acyclic 𝒞^1O case (T30 §3) |
| 15 | Mei, arXiv 2610.27386 v1 (T31) | the best reply cancels every created mixed 2-cycle, and changes at every pivot: 2^h − 1 changes | σ̄ | NEGATIVE: best-response changes can be exponential, even for a single-switch Player-1 rule |
| 16 | Friedmann, arXiv 1106.0778 v2, §6.1 Lemma 6.1, §6.5 | τ_σ(e_i) flips d_i ↔ h_i with every set / reset of bit i: exponentially many best-response changes along I^loc / I^glo runs (GAPS K9 data: 2^N distinct replies along switch-best) | σ̄ | NEGATIVE for σ̄. For N5's τ the flips do not occur: τ shuts the gates and GATE-SHUT keeps them shut (T34; box 16 item 10) |
| 17 | Schewe-Trivedi-Varghese, arXiv 1501.06484 v1, Algorithm 3 (p.2-3), §4.1 (p.9) | both players improve, each restricted to switches agreeing with the other's optimal counter strategy; "symmetric strategy improvement can beat this mechanism" (Friedmann's traps), but no iteration bound, and no bound on either player's strategy changes. Naïve symmetric update (Algorithm 2, p.2): "repeated application of this update can lead to cycles" (Condon) | τ as an improving strategy | NO BOUND; the escape from traps is the same effect as N5's τ shutting gates (T34) |
| 18 | van Dijk-Loho-Maat, arXiv 2309.02223 v1, Thm 1 (p.2), Thm 13 (p.14) | symmetric SI (and its generalization) needs exponentially many iterations for every improvement rule; both players' strategies change exponentially often | τ | NEGATIVE for SSI as defined. N5 is outside both algorithms (SPEC docs/new/N5-ssi-global.md "Why N5's step is NOT covered by 2309.02223") and runs their families in 1-13 iterations (same file, "First test") |

- READING on the literature.
  - Bounds on the opponent's best-response changes exist only where the iteration count itself is bounded (HMZ via the discount;
    Mei-Sun-Ye via the forward property).
  - Exponential best-response changes are the engine of every counter (Friedmann, Mei).
  - No source bounds the changes of an IMPROVING opponent strategy (N5's τ) in a two-player symmetric scheme. STV leave it open; DLM is
    exponential for a different rule.
  - So for count (2) the repo's own reduction (item 7-8) is stronger than anything in the literature.

## DONE / FINDINGS / NEEDS
- DONE: this note; 3 sources re-opened (HMZ, STV, Mei-Sun-Ye), others cited from T30, T31, T34, T35, T37.
- FINDINGS:
  1. τ-changes (phases) per λ-run reduce to Odd's dual carries: #τ-changes ≤ n(n − 1) + m_O·n·(n(n − 1) + 1)(P*^U + 1), and
     P*^U ≤ (n²/2)(NM*^U + 1) + NM*^U. This is the τ-half of COMPOSE (b) (lane) with MΦ (under review). Count (2) is not a new open
     count: the core stays {NM*, NM*^U}.
  2. Landed results bound τ-changes only for one Odd choice (Φ-1O) or by ∏ deg(o_i) (Φ-kO).
  3. The literature bounds the opponent's best-response changes only under a discount (HMZ) or a forward hypothesis (Mei-Sun-Ye); both
     are blocked. Best-response changes are exponential in Friedmann's and Mei's families. No source bounds an improving opponent's
     changes in a symmetric scheme.
  4. My T37 §3 conjecture (carries ≤ poly × reopenings) is DEAD by L-SI's measurement (390d2d8a §13: carries occur with no reopening).
     Recorded in the notebook's dead ends.
- NEEDS (Lead; nothing for the owner): L-SI to state item 7 explicitly in its COMPOSE packet (P-N5-COMPOSE, routed), so that the
  τ-side bound is signed together with the Even side.
