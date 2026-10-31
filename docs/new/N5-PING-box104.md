# N5-PING (box 104 (a)): the «self-fed» split does NOT rescue CASC-EDGE. In L-RED's kill cedge_n32 the excess returns of vertex 7 are NOT self-fed (X is not on its target's play when it returns). The feedback runs through a time-varying loop {7, 20, 26}. Self-fed returns are rare (545 of 10,313 corpus returns), at most 2 per (X, root), and change W(X) in 543 of 545 cases. So CASC-EDGE restricted to non-self-fed returns is DEAD (cedge_n32, ratio 2.0)
L-NEW successor 40 (Opus 5.5), D14 / D18, Lead reading L40. Lead 23:41Z: «BOX 104 … (a) The ping-pong as a lemma … Show that returns with X on
its own target's play are charged to something already counted … If the self-fed returns charge cleanly, CASC-EDGE may hold for non-self-fed
returns.» Written 2026-10-30 23:42Z-23:5xZ (date -u). Working note, unrefereed. Labels: DEAD / DATA / READING. Not a TARGET.md claim.

## 0. Sources and tools
- L-RED R150 (l-red 916dac49, docs/red/R150-cedge.md; read from origin/claude/l-red): CASC-EDGE killed on cedge_n32.
  - cedge_n32 is copied read-only to experiments/new/box104/inst/ (sha1 .pg 5282f02d, .start caf49899).
- Tool: experiments/new/box99/retcause.py, SELFFED line.
  - A return of X to g at k → k + 1 is SELF-FED iff X lies on g's (σ_k, σ̄_k)-play at the state k just before the return.
  - The line reports, for self-fed returns: whether X is the first switching Even vertex, whether X lies on its own Ξ-cycle afterwards,
    and whether λ(Ξ(X)), W(X) or λ_W(X) change at the return. It also gives the max of self-fed returns per (X, root), and the
    NON-self-fed max of RET(X; e) / deg X.
- A first variant tested «X on g's OLD play at the window's first rise». It gives 0 self-fed returns everywhere, including cedge, so it is
  not the ping-pong.
- Corpus: box99/runcause.sh (now keeps the SELFFED line), box101/cause_cascl.txt, box104/cause_cedge.txt. Pin: new/check.sh «box 104 PING».

## 1. cedge_n32: the mechanism (one W-run, states 5-31)
- Vertices (owner Even, priority, successors): 7 (25; {20, 26}), 20 (14; {3, 7, 19}), 26 (19; {10, 27}).
- σ(7) by state: 26 (5), 20 (6-8), 26 (9-14), 20 (15-17), 26 (18-20), 20 (21-22), 26 (23).
- σ(20) by state: 19 (5-9), 7 (10-13), 3 (14-18), 7 (19), 19 (20-23).
- Plays:
  - 20's play passes 7 at states 10-13 and 19;
  - 26's play passes 20 at states 7 and 15-16 (26 → 27 → 20).
- Returns of 7 (XTRACE=7):
  - k 8 (20 → 26), root (26 → 27 @ 6);
  - k 14 (26 → 20), k 17 (20 → 26), k 20 (26 → 20), k 22 (20 → 26): all four rooted at the fresh entry (20 → 7 @ 9), at depths 0, 1, 2, 3.
- So RET(7; e) = 4 > deg 7 = 2. None of these four is self-fed: at each return state, 7 is not on the play of the target it enters.
- The coupling is a LOOP OF PLAYS that switches on and off over time: 7 feeds 20 (while σ(20) = 7), 20 feeds 26 (while 26 → 27 → 20), and 7
  chooses between 20 and 26. The wave from 20's fresh entry into 7 circulates through this loop. Each pass re-opens one of 7's two edges.
- READING: this is the counter shape in miniature: one root, growing depth, one X re-entering its two successors alternately. The loop
  {7, 20, 26} is never a Ξ-cycle at any single state. It is a cycle only in the union of the plays over time.

## 2. DATA (corpus + cascl + cedge)
- 10,313 returns. Self-fed: 545.
  - X is the first switching Even vertex: 0.
  - λ(Ξ(X)) changes: 0.
  - W(X) changes at the return: 543 (the 2 exceptions are both tog6b_n32, one return, counted in both list runs).
  - X on its own Ξ-cycle afterwards: 2.
  - Max self-fed returns per (X, root): 2.
- NON-self-fed max RET(X; e) / deg X: 2.0 on cedge_n32, ≤ 1.0 on every other game (runfam_K40, runfam_K10, sbq2, … at 1.0).

## 3. Results
- DEAD: «CASC-EDGE for non-self-fed returns», i.e. the Lead's split. Instance: cedge_n32, vertex 7, 4 non-self-fed returns under root
  (20 → 7 @ 9).
- DEAD: «every self-fed return changes W(X)» as a universal statement. Instance: tog6b_n32 (1 return). DATA: 543 / 545.
- DATA: self-fed returns are ≤ 2 per (X, root) and never change λ(Ξ(X)). The R47 Φ / cycle-node charge does not apply to them in this
  form.
- Not attempted: a lemma for the time-varying play loop. The natural object is the union over a root's window of the play graphs. A
  bound would need the loop to be traversed O(1) times per root, and cedge_n32 already traverses it 2 times (4 returns).
- The cascade line, after R148-R150, is a reformulation of XI-CH-POLY with mechanism data. It holds no standalone statement that is both
  true on the corpus and strong enough to close W-runs: CASC-EDGE is DEAD and LEVEL-ONCE needs a depth bound (box 103).

## DONE / FINDINGS / NEEDS
- DONE: this note; retcause.py SELFFED line; runcause.sh keeps SELFFED; corpus re-run; box104/ (inst/cedge_n32 copied, cause_cedge.txt);
  new/check.sh «box 104 PING». SHA: see the commit.
- FINDINGS:
  - DEAD: the self-fed split (cedge_n32's excess returns are not self-fed; the loop {7, 20, 26} is time-varying).
  - DEAD: self-fed ⇒ W(X) change (tog6b_n32; 543 / 545).
  - DATA: self-fed ≤ 2 per (X, root).
- NEEDS: none. Synthesis and parking: N5-CORE-SYNTH-box104.md.
