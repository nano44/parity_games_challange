# N5-HEADS (box 52): Theorem RUN-SETTLE (PROVED, lane). Inside a W-run, every stretch with no σ̄-flip, no W-cycle-node switch and no Ξ-change at an upward head has ≤ n − 1 transitions. A Bellman–Ford front in W-length proves it, so |F| ≤ n(E_F + 1) − 1. Hence polynomial W-runs ⟺ polynomial per-vertex counts of σ̄-flips, CN switches and HEAD Ξ-changes (Theorem HEAD-RED); with CONJECTURE FLIP-EV, only cycle-node σ̄-flips stay. Odd side of SEG-XCH PROVED (lane)
L-SI successor 34 (Opus 5.5), D18. Lead 2026-10-30 16:59Z, BOX 52: «XI-CH-POLY via heads … Try to prove HX_F ≤ p(n) per W-run, or the
exact obstruction with an instance. D18 angle: heads are where the two players' strategies disagree (σ̄ ≠ τ) … Queue item 3: the Odd-side
dual proof of SEG-XCH». Written 2026-10-30 from 17:00Z (date -u). This is a working note: unrefereed, and not a TARGET.md claim.
G-N5-TIME stays OPEN. HX_F ≤ p(n) is NOT proved.
Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.

## 0. Setting, sources opened, tools
- Setting and symbols as in docs/si/N5-GATE-box51b.md:
  - W-run F: τ fixed, λ_W constant, no S4c fallback, σ moves at every transition. si/gate/heads.py's definition, kept verbatim in every
    tool here.
  - W_k := val(σ_k, τ); Ξ_k := val(σ_k, σ̄_k); D_k := {Odd o : σ̄_k(o) ≠ τ(o)}; C := {v : λ_W(v) = v} (fixed on F).
  - ℓ_k(x) := the length component of W_k(x), i.e. the length of the (σ_k, τ)-path from x to its W-cycle node.
  - H_k := S4a's arena at state k: Even v restricted to {σ_k(v)} ∪ Iσ_k(v), Odd fixed to τ. ⊕ is the prefix operation.
- L-RED R143's events, verbatim (docs/red/R143-settle.md §0, l-red 717f407a, opened):
  - «UPWARD HEADS: U_k := {σ̄_k(g) : g Odd, σ̄_k(g) ≠ τ(g)} ∪ {the Ξ-successor of c (σ_k(c), or σ̄_k(c) if c is Odd) : c ∈ C}».
  - «EVENT: a transition k → k + 1 … at which (i) σ̄ changes, or (ii) σ changes at some Even c ∈ C (a CN switch), or (iii) Ξ changes at
    some vertex of U_k ∪ U_(k+1)».
  - R143 applies them inside one W-constant interval. Here they are applied over a whole W-run F, unchanged.
  - E_F := the number of event transitions of F. A WINDOW is a maximal run of event-free transitions of F.
- Opened and used:
  - R143 §0-§1: the events, and the play argument of (A).
  - L-RED R140 §2 (docs/red/R140-friedmann-port.md), Lemma ARENA-MAX: «for every vertex v and every Even strategy ρ of H_t:
    W_(t+1)(v) ⊵ val(ρ, τ_t)(v)».
  - L-LIT T54 §4.1-§4.2 (docs/lit/T54-stalling.md): IDX-MONO, LEX-BFS, and the key «key_σ(x) := (x_{ℓ−1}, …, x_1, x_0)» of the (σ, τ)-path
    x = x_0 → … → x_ℓ = c.
  - RESULTS R15 (a), (d) (docs/RESULTS.md l. 624): any non-empty set of improvements improves weakly, on G and on G^d. N5 switches σ or τ
    at every iteration.
  - L-NEW box 88 §1 (docs/new/N5-ONEP-box88.md): the one-player picture.
  - My predecessor's box 51b §10.1 (Claim RG) and §11 (RETURN-CHARGE′, SEG-XCH).
- Tools, new, in experiments/si/heads52/. All read-only users of n5x.py / si.py / pg.py, all with W-runs as heads.py:
  - dset.py (the defect set D_k);
  - rwin.py (R143 events and windows over whole W-runs);
  - bffront.py (Bellman–Ford fronts; MUT=1 control);
  - swcase.py (the cases of the proof in §1);
  - wdiag.py (window shape);
  - flipc.py (σ̄-flip causes);
  - bi1p.py (a two-one-player model, §6).
  - Corpus = box 50b's lists (new/box59/sbcg.lst, 719 runs; si/root/logs/alt_all.lst, 413 runs) plus latew_K16_m32 and fx_K8_m32. That
    is 1,134 runs, 300 s cap each. Outputs: <tool>_{sbcg,alt,red}.txt.
  - Shell scripts: run{dset,rwin,bff,swc,flip}.sh.

## 1. Theorem RUN-SETTLE (PROVED, lane; case 3a uses Claim RG′ and T54's LEX-BFS / IDX-MONO, see §1.4)
- Statement. Let F be a W-run and [k0, k1] a window of F: the transitions k0, …, k1 − 1 are event-free. For k0 ≤ k < k1 put j := k − k0.
  - (S_j) every Even y with σ_(k+1)(y) ≠ σ_k(y) has ℓ_(k+1)(y) ≥ j + 1;
  - (X_j) every vertex x with Ξ_(k+1)(x) ≠ Ξ_k(x) has ℓ_(k+1)(x) ≥ j + 1.
  - Hence k1 − k0 ≤ max_x ℓ(x) ≤ n − 1: every window of a W-run has at most n − 1 transitions.
- Corollary RUN-COUNT (PROVED, lane). |F| ≤ E_F + (E_F + 1)(n − 1) = n(E_F + 1) − 1.
  - This extends R143's SETTLE (|I| ≤ (D + 1)(E_I + 1) − 1, one W-constant interval) to the whole W-run, with D replaced by n − 1.
  - W-changing transitions are now covered too. Inside a window most transitions change W (obs_K12_m24: 24 of 24 in its longest window).

### 1.1 Lemma PLAY-CAUSE (PROVED, lane; R143 (A)'s play argument, restated for a W-run): X_j follows from S_j
- Let k → k + 1 be event-free, and let x = y_0, y_1, … be the (σ_(k+1), σ̄_(k+1))-play. Let i be the least index with y_i ∈ D_(k+1) ∪ C.
  - i exists. Before D, Odd vertices follow τ, so the play is the (σ_(k+1), τ)-play, which reaches λ_W(x) ∈ C.
  - y_(i+1) ∈ U_(k+1).
- Every VJ value on a play is (cycle node w, the relevant vertices of the path to w, the distance to w). The eventual cycle of x's play is
  that of y_(i+1)'s play. So Ξ_(k+1)(x) is a function of y_0 … y_i and Ξ_(k+1)(y_(i+1)):
  - x ⊕ … ⊕ y_i ⊕ Ξ(y_(i+1)) if w ∉ {y_0, …, y_i};
  - otherwise the path y_0 … y_j to w = y_j, with w read off Ξ(y_(i+1)).
- Suppose no Even y_t (t ≤ i) switches at k. y_i ∈ C does not switch: no CN switch.
  - With σ̄_k = σ̄_(k+1) and D_k = D_(k+1) (no event (i)), the (σ_k, σ̄_k)-play from x has the same y_0 … y_(i+1).
  - Ξ_k(y_(i+1)) = Ξ_(k+1)(y_(i+1)) (no event (iii)).
  - So Ξ_k(x) = Ξ_(k+1)(x).
- So a Ξ-change at x needs a switched Even y_t, t < i. y_t lies on x's (σ_(k+1), τ)-path before C, so ℓ_(k+1)(x) = t + ℓ_(k+1)(y_t). □

### 1.2 Two facts used below (PROVED, lane; immediate)
- (W-MON) W_(k+1) ⊵ W_k pointwise in a W-run. σ_k is a strategy of H_k, so this is ARENA-MAX with ρ = σ_k.
- (PATH) If no Even vertex on the (σ_(k+1), τ)-path from b to c = λ_W(b) switches at k, then:
  - b's k-path is the same path, so W_k(b) = W_(k+1)(b) and ℓ_k(b) = ℓ_(k+1)(b);
  - W(b) = (c, relevant vertices of the path, length), and c is a cycle node at both states.

### 1.3 Proof of S_j, by induction on j
- j = 0. A switched y is not in C (no CN switch), so ℓ_(k+1)(y) ≥ 1.
- j ≥ 1, assuming S_(j−1) and hence X_(j−1).
  - Suppose S_j fails at k = k0 + j. Among the switched Even y with ℓ_(k+1)(y) ≤ j, choose one with the least L := ℓ_(k+1)(y). Write
    a := σ_k(y), b := σ_(k+1)(y), c := λ_W(y), so ℓ_(k+1)(b) = L − 1.
  - By minimality, no Even vertex u with ℓ_(k+1)(u) < L switches at k: such a u would be a violator with a smaller ℓ (L ≤ j).
  - Every vertex on the (σ_(k+1), τ)-path of b has ℓ_(k+1) ≤ L − 1. So by (PATH): W_k(b) = W_(k+1)(b), ℓ_k(b) = L − 1, and b's k-path
    avoids y. (b's (k+1)-path does: y → b → … → c is simple.)
- Case 2: b ∉ H_(k−1)(y).
  - b ∈ H_k(y) and b ≠ a, so Ξ_k(b) ▷ Ξ_k(a).
  - Ξ_k(a) ⊵ Ξ_(k−1)(a) (R15 (a)), and Ξ_(k−1)(a) ⊵ Ξ_(k−1)(σ_(k−1)(y)): equal if y did not switch at k − 1, strictly if it did,
    because a ∈ Iσ_(k−1)(y).
  - If Ξ_k(b) = Ξ_(k−1)(b), then Ξ_(k−1)(b) ▷ Ξ_(k−1)(σ_(k−1)(y)), so b ∈ H_(k−1)(y), a contradiction. Hence Ξ(b) changes at k − 1 → k,
    which is offset j − 1 of the window.
  - X_(j−1) gives ℓ_k(b) ≥ j > L − 1 = ℓ_k(b). Contradiction.
- Case 3: b ∈ H_(k−1)(y).
  - ρ := σ_k with y ↦ b is a strategy of H_(k−1). Its play from y is y, then b's k-path, which avoids y.
  - ARENA-MAX at k: W_k(y) ⊵ y ⊕ W_k(b) = y ⊕ W_(k+1)(b) = W_(k+1)(y) ⊵ W_k(y) (W-MON).
  - So W_(k+1)(y) = W_k(y) = y ⊕ W_k(a) = y ⊕ W_k(b): b is W_k-tight at y, and a is too.
  - Case 3a: a is W_(k+1)-tight at y, so ℓ_(k+1)(a) = L − 1. By minimality and (PATH), a's and b's (k+1)-paths are their k-paths. Hence
    key_(σ_k) = key_(σ_(k+1)) on a and on b (keys read the path; T54 §4.2).
    - Both edges are tight arena edges at both steps (a ∈ H_k(y) as σ_k(y); b ∈ H_(k−1)(y)). LEX-BFS at k − 1 → k and at k → k + 1 gives
      key(a) < key(b) and key(b) < key(a) (EVEN branch, Ω(c) even).
    - IDX-MONO gives index(a) < index(b) and index(b) < index(a) (ODD branch).
    - Contradiction either way. (y ∉ C, so the CN branch does not arise.)
  - Case 3b: a is not W_(k+1)-tight, and a's (σ_(k+1), τ)-path avoids y.
    - Then ρ′ := σ_(k+1) with y ↦ a is in H_k (a = σ_k(y)), and its play from y is y, then a's (k+1)-path.
    - ARENA-MAX at k + 1: y ⊕ W_(k+1)(a) ⊴ W_(k+1)(y) = y ⊕ W_k(a) ⊴ y ⊕ W_(k+1)(a).
      - The last step is W-MON, plus the fact that y ⊕ · preserves ⊴ on values with the one cycle node c.
    - So a is tight. Contradiction.
  - Case 3c: a is not W_(k+1)-tight, and a's (σ_(k+1), τ)-path contains y (the "re-route" case).
    - a's k-path avoids y (it is y's k-path minus y). Let u be the first vertex on a's k-path that switches at k. u exists, u ∉ C, u ≠ y.
    - a's (k+1)-path follows a's k-path to u, then u's (k+1)-path, which reaches y.
    - Let P := u's (k+1)-path from u up to y, y excluded. Let Q := y's k-path from y up to u, u excluded (Q = y, a, …). The walk
      Z := P then Q is a simple cycle: both pieces lie on a's simple (k+1)-path, and y ∉ P. c ∉ Z.
    - Values, all with cycle node c: W_(k+1)(u) = P ⊕ W_(k+1)(y), W_(k+1)(y) = W_k(y) (Case 3), and W_k(y) = Q ⊕ W_k(u).
    - The path sets are disjoint where they are joined: P avoids y's (k+1)-path, whose set equals W_k(y)'s. Hence
      W_(k+1)(u) = (c, S_k(u) ⊔ R, ℓ_k(u) + |Z|), with S_k(u) the path set of W_k(u) and R := {z ∈ Z : z more relevant than c}.
    - By W-MON, W_(k+1)(u) ⊵ W_k(u). The VJ set order is decided by the most relevant vertex of the symmetric difference R, and then by
      length: for even c a longer path is worse, for odd c better (si.Engine.key).
    - So either R ≠ ∅ and max R is even, or R = ∅ and c is odd (|Z| ≥ 2).
    - Now take ρ′ := σ_(k+1) with y ↦ a, in H_k. The play from y runs y, a, …, u, P, y: it closes the cycle Z. Its cycle node z* is the
      most relevant vertex of Z.
      - If R ≠ ∅: z* = max R is even with p′(z*) > p′(c), so its reward exceeds c's.
      - If R = ∅ and c is odd: reward(c) = −p′(c) < −p′(z*) ≤ reward(z*).
    - Either way val(ρ′, τ)(y) ▷ W_(k+1)(y), contrary to ARENA-MAX at k + 1. Contradiction.
- All cases fail, so S_j holds. The window bound: the last transition of a window of length L_w switches some Even y. S_(L_w − 1) gives
  ℓ(y) ≥ L_w, and ℓ ≤ n − 1. □

### 1.4 What the proof uses, exactly
- SPEC S2: offers are the Ξ-improving edges. S4a: the pointwise W-optimum of H_k (ARENA-MAX, R140; R57's premise that S4a computes it).
  R15 (a): Ξ only rises.
- Case 3a only: S1's tie-break.
  - The choice is the lex-least key (EVEN branch) or the least index (ODD branch) among the W_(k+1)-tight edges of H_k(y). That is
    T54's LEX-BFS / IDX-MONO.
  - Their premise is Claim RG′ := §10.1's Claim RG with W := W_(k+1) at ANY S4a step of a W-run, not only at a W-flat one.
  - READING (checked here line by line, not refereed): §10.1's proof of (A) and (B) uses only that the computed values (c, path, dist)
    are W_(k+1) (R57). It never uses W_(k+1) = W_k, so RG′ has the same proof.
- Nothing about σ̄ beyond the events. Nothing about Odd's arena. τ only has to stay fixed.

### 1.5 DATA (the theorem's predictions, and two controls)
- rwin.py, 1,134 runs: no window reaches n − 1 transitions. Largest window / (n − 1) is 0.936 (red/xing/instances/x32_rand48.pg, n 48,
  one event-free W-run of 44 transitions). Largest window: 67 (gate_K64_n581).
- bffront.py, the front of (X_j):
  - 36,834 in-window Ξ-changes; BADW 0 (no Ξ-change at x with ℓ_(k+1)(x) ≤ j). The bound is attained: MINW1 = 1, e.g. gci2_n12 with its
    start.
  - Control MUT=1 (test ℓ ≤ j + 1 instead) gives BADW 2 on gci2_n12. The test bites.
- swcase.py, every switch at offset j ≥ 1:
  - classes: NE 13,998, WR 186, TT 13, RR 0, OT 0;
  - violations in every class: 0;
  - switches at offset 0: 5,781.
  - RR (Case 3c) and OT (Case 3b) never occur, as the proof says. TT occurs (u23sw64_n32: 5) but never at a violator.
- wdiag.py on obs_K12_m24 (L-RED R139's funnel): the longest window has 24 transitions and all 24 change W.
  - Vertex 247 switches 23 times inside that window while a wave climbs the chain 175, 178, …, 241.
  - So per-vertex Ξ-changes inside one window can be Θ(window). The window length is capped by the front, not by per-vertex counts.

### 1.6 DEAD: the same front measured along the Ξ-play
- Hypothesis: (X_j) with δ_(k+1)(x) := the number of steps of x's Ξ-play before its first vertex of D ∪ C, in place of ℓ_(k+1)(x).
- DEAD. Instance experiments/red/ul/instances/ladderd0_k12_n48.pg with its .start: 11 violations, MINF1 = −10. The family is linear:
  ladderd0_k24_n84 has 23 violations, ladderd0_k48_n156 has 47. reader_L10/L20/L40 have 2 each.
- Obstruction: an Even vertex is pulled to a gate g by a W-rise BEYOND g. That rise sits in τ(g)'s continuation, which Ξ does not read
  (swcase class WR). The Ξ-distance to g is small, the W-distance is not. That is why the theorem has to use W-lengths.

## 2. Theorem HEAD-RED (PROVED, lane): polynomial W-runs ⟺ polynomial σ̄-flips, CN switches and head Ξ-changes, per vertex
- Per W-run F, define:
  - SB_F(o): the σ̄(o)-changes of Odd o;
  - CN_F(c): the switches of Even c ∈ C;
  - HXU_F(u): the transitions k → k + 1 of F with u ∈ U_k ∪ U_(k+1) and Ξ(u) changing.
- Statement. E_F ≤ Σ_o SB_F(o) + Σ_c CN_F(c) + Σ_u HXU_F(u). Hence, by RUN-COUNT,
  |F| ≤ n(1 + n·max SB_F + n·max CN_F + n·max HXU_F) − 1.
  - Every event transition has an event of kind (i), (ii) or (iii), and each is counted at least once on the right.
- Converse. Each count is ≤ |F| per vertex. So polynomial W-runs ⟺ the three per-vertex counts are polynomial.
- Against XI-RUN / SEG-XCH (which need per-vertex Ξ-changes at EVERY vertex): only the heads U, the σ̄-flips and the CN switches count
  now. On obs_K12_m24:
  - max XX_F = 301 (a non-head vertex, quadratic);
  - max HX = 24 (= m);
  - σ̄ flips once (dset SBF 1); CN 0.
- DATA (rwin.py, all W-runs of the corpus, transitions with an event of each kind): (i) 4,625, (ii) 37, (iii) 4,741.
  - latew_K16_m32: E_F = 528 of |F| = 560, with (i) 513 and (iii) 512. Its events are quadratic in number but linear per vertex:
    SB ≤ 32 per vertex (dset), HX ≤ 32 per head (§13 of box 51b).

## 3. The defect set D_k (Lead's D18 angle): σ̄-flips follow head changes up to cycle-node tie-breaks. FLIP-CAUSE″ DEAD, CONJECTURE FLIP-EV
- DATA (dset.py, 1,134 runs). D_k is NOT monotone inside a W-run.
  - latew_K16_m32: one vertex enters D 16 times and re-enters after an exit 15 times. Its σ̄ flips 32 times in one W-run.
  - Corpus maxima: re-entries 30, σ̄-flips per vertex 62.
- DEAD: «every deviation edge (g, σ̄(g)) is W*-non-improving for Odd», i.e. σ̄ avoids I_τ (W* := Ξ^U, constant on F). Instance
  experiments/n5-epoch/instances/lend107_n32.pg with its .start: 106 deviation-state pairs use an edge of I_τ (INIT 106 = WSB 106). Other
  instances: lend39f_n32 (92), nep22f_n64 (100), counter_symsi_3 (6).
  - Ties occur too: WSE 511 (W*(σ̄g) = W*(τg); u23sw64's 27 → 20 is one, as R143 §3 says).
  - So a deviation is not a "W*-uphill" edge in general. τ's stability in a W-run (S4a for Odd keeps τ against σ_k) constrains W_k on I_τ
    edges, not Ξ.
- σ̄-flip causes (flipc.py, 1,134 runs, 7,525 flips). Kinds:
  - ENT, o enters D: 1,879;
  - EXI, o leaves D: 2,581;
  - MOV, D → D with a new target: 3,065.
  - NONE 0: no flip where neither the old nor the new target's Ξ changes.
  - NOX 1: the old target's Ξ is unchanged at exactly one flip.
    - Instance n5-epoch/instances/nep13_n24.pg with its .start, transition 11 → 12. o = 15 is its own Ξ-cycle node and re-picks its
      cycle edge 0 → 12 because Ξ(12)'s length fell 4 → 1.
    - That target is a head at state 12, so the flip is still a head event.
  - So the plain form «a σ̄-flip needs a Ξ-change at the old target» is DEAD (nep13_n24, one MOV flip).
  - Every EXI flip has a Ξ-change at its old target, a head of U_k (2,581 / 2,581). Every ENT flip has one at τ(o) (NOXENT 0).
- CONJECTURE FLIP-CAUSE″ (as first stated, on the corpus data): at a σ̄(o)-flip k → k + 1, Ξ changes at the old target σ̄_k(o)
  (EXI), at the old or the new target (MOV), or at τ(o) (ENT). Corpus: 0 violations in 7,525 flips.
- FLIP-CAUSE″ is DEAD, by random search (17:5xZ). Every instance below is in experiments/si/heads52/inst/ with its .start. A second engine
  agrees on each: L-COMP's n5b SPEC (si/heads52/flipx.py computes σ̄ by SpecSI.evaluate_choice), and red/seg/xeng.py gives identical
  states.
  - flipnone_n14, transition 1 → 2. Odd 12 is its OWN Ξ-cycle node (Ξ(12) = (12, ∅, 0), priority 13). It leaves D: 6 → τ(12) = 1, with
    Ξ(6), Ξ(1) fixed (lengths 5, 3), while σ switches at 2, 8, 9.
    - S1's choice at an Odd own Ξ-cycle node is the first cycle-closing successor of a DFS, so the arena below re-orders it. This is the
      Odd analogue of the CN branch (box 51b §10.2).
    - No event (iii) occurs at that transition (rwin EIII 0). flipnone_n10 (o = 7) and nep13_n24 (o = 15) are the same kind of vertex.
  - flipnonex_a_n10, transition 1 → 2, Odd 8: NOT its own cycle node (Ξ(8) = (5, ∅, 4), cycle node 5 odd, so S1's BFS branch).
    - 8 leaves D: 9 → τ(8) = 4, with Ξ(9) = Ξ(4) = (5, ∅, 3) tied and fixed.
    - The cause sits one level down. 9 itself flips 0 → 6 (Ξ(0) rose; 6 is tied with the old value), so 9's BFS-tree path changes,
      8's keys re-order, and the first-discovered tied candidate changes.
    - flipnonex_b_n10 (o = 8, cycle node 0 odd) is the same.
    - Here the transition DOES carry a head event: 9's old target 0 is a head. flipc.py: NONEX 1, EVX 0 on both instances.
- READING (proof sketch from si.Engine.evaluate, not refereed). For o not its own Ξ-cycle node, in its cycle node's round:
  - EVEN cycle node (longest()): σ̄(o) is the least-index remaining successor of maximal dist. If the Claim RG-type statement for this
    Odd-side computation holds (remaining edges = the Ξ-tight ones), that is the least-index Ξ-tight successor.
  - Ξ only rises. While Ξ(o) is fixed, the tight set can only lose members, so a flip needs the old target to leave it, i.e. Ξ(old)
    changes. FLIP-CAUSE holds in this branch.
  - ODD cycle node (BFS): the first-discovered tied successor. The kill above sits in this branch.
- CONJECTURE FLIP-EV (the form the count needs). Every EXI or MOV flip at an Odd o that is not its own Ξ-cycle node (at k or k + 1)
  occurs at a transition with an event (iii).
  - DATA, corpus re-run (flipc.py, 1,134 runs, 7,525 flips): EVX 0. NONE 0 on the corpus; own-node flips OWNCN 5.
  - DATA, random search (scratch search, the flipc criteria in-process: random games n 8 / 10 / 12 / 14 / 16, random owners,
    priorities, out-degree 1-4, random starts; 100,000 games each; W-runs as heads.py): 0 non-own-node EXI / MOV flips without an event
    (iii).
  - Not proved.
- Corollary FLIP-RED (PROVED, lane, from FLIP-EV). Let XCN_F := the σ̄-flips of F at Odd vertices that are their own Ξ-cycle node at k or
  k + 1.
  - (i)-only transitions carry only ENT flips or own-node flips.
  - ENT and EXI alternate per o, so ENT_F(o) ≤ EXI_F(o) + 1. Also Σ_o EXI_F(o) ≤ n_O·E⁽ⁱⁱⁱ⁾_F + XCN_F.
  - Hence E_F ≤ (n_O + 1)·E⁽ⁱⁱⁱ⁾_F + n_O + CN_F + 2·XCN_F, and |F| ≤ n(E_F + 1) − 1, with E⁽ⁱⁱⁱ⁾_F ≤ Σ_u HXU_F(u).
  - So, given FLIP-EV, polynomial W-runs ⟸ per-head Ξ-changes polynomial ∧ cycle-node choices polynomial: CN_F for Even, XCN_F for Odd.
  - The defect dynamics D_k is then slaved to the head values, up to the cycle-node tie-breaks. This is the exact sense in which «heads
    are where the strategies disagree» carries the whole W-run.
- READING (D18, cross-field; no source opened, nothing imported). A W-run is distance-vector routing in the one-player τ-arena:
  - W is the routing metric. The heads' Ξ-values are boundary costs that the routing does not control.
  - Between boundary changes, offers only improve (Ξ only rises), and RUN-SETTLE is the "good news travels in diameter rounds" bound of
    Bellman–Ford.
  - The open question HX-POLY asks how often the boundary can change. In routing terms: can the network's own convergence feed back
    into its boundary costs exponentially often? R143 §2's «UPWARD FEEDBACK loop» is the same object.

## 4. What is open, exactly (HX_F ≤ p(n) NOT proved)
- HX-POLY: per W-run and per vertex u, the Ξ-changes of u at times when u is an upward head are polynomial.
  - DATA: linear on every family (2K on mkrw; m = 24 on obs_K12_m24; 16 on fx_K8_m32); corpus max 32.
- By HEAD-RED, HX-POLY ∧ SB-POLY ∧ CN-POLY ⟺ polynomial W-runs. With FLIP-EV, SB-POLY reduces to XCN-POLY (Odd own-cycle-node flips).
- CN-POLY per W-run: data 37 CN-switch transitions in the whole corpus (cw11_n24 has 11).
- Kill target for L-RED (READING). Make one head change Ξ super-polynomially often inside one W-run.
  - Requirement from RUN-SETTLE: between two head events, everything settles within n − 1 transitions.
  - So the clock must be the heads' own feedback (R143 §2): a head h = σ̄(g) whose Ξ-play passes through the region its own change
    re-opens.
  - The chain-propagation cost of a window is already paid (≤ n − 1).

## 5. Queue item 3: the Odd side of SEG-XCH (PROVED, lane)
- Lemma RETURN-CHARGE′-O. In any stretch of an N5 run, let Odd o leave d at k1 (τ_(k1)(o) = d ≠ τ_(k1+1)(o)) and re-adopt d at k2 > k1.
  Then Ξ^U_(k2)(d) ◁ Ξ^U_(k1)(d), i.e. strictly better for Odd. Here Ξ^U_j := val(Even's optimal reply to τ_j, τ_j), the valuation
  si.Engine computes on G^d, ordered by Even's ⊴.
  - (a) Ξ^U_j depends on τ_j alone. So it changes only at τ-changing transitions.
  - (b) Every Odd switch goes to an edge of Iτ_j.
    - S4a for Odd takes τ_(j+1)(v) ∈ {τ_j(v)} ∪ Iτ_j(v).
    - The S4c fallback, when Iσ_j = ∅, picks from Iτ_j (n5x.py step()).
  - (c) R15 (a) on G^d (R15 (d): «Switch_I with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d)»): Ξ^U_(j+1) ⊴ Ξ^U_j pointwise.
  - So j ↦ Ξ^U_j(τ_j(o)) is non-increasing in ⊴. Without a switch at o this is (c). With a switch a → b: Ξ^U_(j+1)(b) ⊴ Ξ^U_j(b) ◁ Ξ^U_j(a)
    by (b).
  - Chain: Ξ^U_(k2)(d) ◁ Ξ^U_(k2)(τ_(k2)(o)) ⊴ Ξ^U_(k1+1)(τ_(k1+1)(o)) ◁ Ξ^U_(k1)(d). □
- Corollary SEG-XCH-O. For a segment [p, q], the τ-switching transitions number at most
  Σ_(Odd o)(deg(o) − 1) + Σ_d d_O(d)·XCH^U_[p,q](d).
  - d_O(d) := the number of Odd predecessors of d; XCH^U(d) := the transitions of [p, q] changing Ξ^U(d). The argument is §11's: return
    windows of one (o, d) are disjoint and each contains a change of Ξ^U(d).
- Corollary T-XCH (PROVED, lane; this turns box 51b §11 (iii)'s READING into a lane statement). Every N5 iteration changes σ or τ
  (R15 (d)). So, over a whole run,
  T ≤ Σ_(Even v)(deg v − 1) + Σ_d d_E(d)·XCH(d) + Σ_(Odd o)(deg o − 1) + Σ_d d_O(d)·XCH^U(d) ≤ m_E(1 + XE) + m_O(1 + XO).
  - XE / XO are the most changes of one vertex's Ξ / Ξ^U over the run.
  - G-N5-TIME ⟺ XE and XO polynomial; the converse holds because each is ≤ T. A reformulation, not progress on the bound.
- DATA: box 51b §11 (retx.py): ORCV 0, OMONO_V 0, OIMP_V 0, TB_V 0 over 1,134 runs. These are the checks of exactly these statements.

## 6. Model BI1P (DATA only): σ̄ frozen at ρ, both Odd strategies fixed
- bi1p.py runs S2 / S4a with σ̄ replaced by a fixed ρ. The N5 constraints «ρ = Odd's best reply» and «τ = Odd's arena optimum» are
  dropped, so every σ̄-frozen W-run of N5 is a BI1P run.
- Random search (n 8 / 12 / 16, 3,000 tries each): longest runs 4 / 5 / 5. No claim. A frozen-σ̄ W-run of N5 is one window plus head
  events, and RUN-SETTLE already bounds the windows.

## DONE / FINDINGS / NEEDS
- DONE:
  - this note;
  - experiments/si/heads52/ (dset, rwin, bffront, swcase, wdiag, flipc, bi1p, run*.sh, outputs);
  - pins in si/check.sh «box 52»;
  - dead ends in docs/si/DEAD.md «box 52»;
  - notes/L-SI.md.
- FINDINGS:
  1. PROVED (lane; case 3a needs Claim RG′, the §10.1 proof read with W_(k+1)): Theorem RUN-SETTLE. In a W-run, a change at window
     offset j sits at W-length ≥ j + 1, so every event-free window has ≤ n − 1 transitions, and |F| ≤ n(E_F + 1) − 1. This extends
     R143's SETTLE from one W-constant interval to the whole W-run.
  2. PROVED (lane): Theorem HEAD-RED. Polynomial W-runs ⟺ polynomial per-vertex σ̄-flips, CN switches and Ξ-changes at upward heads.
     Only heads count, not every vertex (obs_K12_m24: 301 at a non-head vertex against 24 at heads).
  3. DATA: windows ≤ 0.936(n − 1) (x32_rand48); front BADW 0 over 36,834 changes, attained (MINW1 1), MUT control bites; proof cases RR 0,
     OT 0.
  4. DEAD: the Ξ-distance front (ladderd0_k12_n48, 11 violations; family linear).
  5. DEAD: «σ̄ avoids I_τ» (lend107_n32 + start, 106); «D only shrinks» (latew_K16_m32, re-entries 15 per vertex); «a σ̄-flip needs an
     old-target Ξ-change» (nep13_n24 + start, o = 15 at 11 → 12).
  6. DEAD: FLIP-CAUSE″ (flipnone_n14: own Ξ-cycle node, no head event; flipnonex_a_n10: BFS-branch tie, a head event present).
     CONJECTURE FLIP-EV. With it (Corollary FLIP-RED, PROVED from it), polynomial W-runs ⟸ HX-POLY ∧ CN-POLY ∧ XCN-POLY.
  7. PROVED (lane): Odd side of SEG-XCH (RETURN-CHARGE′-O, SEG-XCH-O, T-XCH). G-N5-TIME ⟺ XE, XO polynomial.
  8. OPEN: HX-POLY (data linear). Kill target in §4.
- NEEDS: none from the owner. Lead:
  - route RUN-SETTLE + HEAD-RED (with Claim RG′) to the referees if it is useful;
  - L-RED: the §4 target (a head feedback clock), and an attack on FLIP-EV;
  - L-NEW: compare HEAD-RED with XI-RUN's table.
