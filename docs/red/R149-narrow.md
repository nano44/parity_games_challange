# R149: CONJECTURE NARROW (L-NEW 40, box 100) is DEAD in both clauses, and the per-(X, root) form is DEAD. narrow_n10 (topfix_n10 plus one passive clone of each of its 27 returning Even vertices, n 237): every one of the 225 return nodes with a child has exactly 2 children, along a chain of 49 = 6N − 11 consecutive branching return nodes (25 at N = 6). casctf_n10_N210: one return node with 211 children. On topfix_N one Even X returns 2N − 3 times inside ONE root's subtree. All roots FRESH; xeng, Oink OK. Every kill uses passive clones or topfix as it stands; |F| is unchanged
L-RED successor 35 (Opus 5.5; D1/D18). Lead 2026-10-30 22:17Z: «R149, yes: shape (ii) plus NARROW. A return node with many children at depth
≥ 2, or a topfix-like path whose nodes branch. Equivalently, make one Even X return super-constantly often inside ONE root's subtree. That
kills both NARROW and per-(X, root). … topfix_N already has depth 6N − 11 with width 1. Branching it is the obvious first try.» Written
2026-10-30 from 22:20Z (date -u).
- Labels: DEAD (with instances) / DATA / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.
- Sources opened: l-new 2311683e docs/new/N5-CASC-box100.md (§1 FRESH-ROOT with the Even root map, §2.1 Lemma CHILD, §2.2 Corollary TREE,
  §2.3 depth correction, §2.4 CONJECTURE NARROW: «every return node has O(1) children, and a chain of return nodes with ≥ 2 children has
  length O(1)»); experiments/new/box99/retcause.py at 2311683e (EROOT map, relative-depth memo, children per node).
- Tool: experiments/red/casc/retcause_br.py, a COPY of L-NEW's retcause.py at 2311683e changed only to add one output line BRCHAIN: the
  longest chain of consecutive RETURN nodes (parent to child in L-NEW's forest) that each have ≥ 2 children, and how many return nodes
  have ≥ 2 children. Run with LNEW_BOX21 = a git archive of l-new 2311683e's experiments/new/box21. Output: casc/narrow_out.txt.

## 1. The kills
- (a) Clause 2, «a chain of return nodes with ≥ 2 children has length O(1)»: DEAD.
  - Instance casc/instances/narrow_n10 (n 237): L-NEW's new/box52/out/topfix_n10 (n 210, default start) plus ONE clone (casc/clone.py) of
    each of the 27 Even vertices that return in its W-run. The 27 are listed by casc/retx.py ALL=1: 120-122, 129-131, …, 192-194. The
    start file is the default start, written by casc/defstart.py.
  - retcause_br.py: «max children per node 2 max children per return node 2» and «BRCHAIN longest chain of consecutive return nodes with
    ≥ 2 children 49 return nodes with ≥ 2 children 225 of 225».
  - topfix_n6 with the same construction (n 141): BRCHAIN 25. So the length grows as 6N − 11, topfix's own depth, while topfix_n10
    unchanged has BRCHAIN 0 (width 1, as box 100 says).
  - Mechanism. A clone X′ of a returning X has X's successors, priority and start, and no in-edges. So it re-enters the same g in the same
    transition, with the same first window change, and is a SIBLING of X under X's parent node. X′ itself has no children, because no play
    passes through it. Every chain node therefore gets exactly one extra (leaf) child.
- (b) Clause 1, «every return node has O(1) children»: DEAD.
  - casc/instances/casctf_n10_N210 (n 420, R148 §3): «max children per return node 211». It is the node above Even 193's returns, and
    the 210 clones of 193 are its children.
  - On a W-run of length 58, against the corpus maximum of 6 (box 100).
- (c) Per-(X, root) («make one Even X return super-constantly often inside ONE root's subtree»): DEAD on topfix_N as it stands.
  - R148 §3 / casc/xr_corpus.txt: one Even X returns 2N − 3 times with the same root (topfix_n10: Even 193, 17 times, root ('FRESH', 194,
    195, 9); topfix_n12: Even 235, 21 times).
  - No clone is needed for (c).
- All roots are FRESH in every instance (EROOT kinds {'FRESH': …}).
- Checks: narrow_n10 has xeng state sequences identical and Oink 8fbf0a7 --zlk OK (rel2/oinkcmp.sh); casc/retx.py counts 504 returns
  (2 × 252). casctf_n10_N210 as in R148.

## 2. CORRECTION of R148
- R148's chain depths («chain depth {0: 780, 1: 18}», «depth 0» on topfix) were read from retcause.py at l-new b376575c. That version has
  the relative-depth memo bug that box 100 §2.3 corrects.
- The ROOTS and the per-root counts (121, 321, 3,620, XROOT) do not depend on the memo's depth value, so R148's kills stand.
- The depth figures in R148 and in casc/retcause_out.txt are void. casc/retcause_xr.py (R148's copy) keeps the old depth bug, and is
  used only for XROOT.

## 3. Reading: what the clone kills say about the cascade programme
- Every kill in R148-R149 except (c) uses passive clones. They add Even edges, returns and children, but no transitions: |F| is the base
  family's.
- So any bound stated on return ENTRIES (CASC, children per node, per-(X, root)) can be inflated without touching |F|. CASCADE-EQ remains
  a valid reduction, but CASC-POLY is no sharper than the trivial CASC ≤ n_E·|F|.
- A target that clones cannot inflate must charge something a clone does not have. Two candidates (CONJECTURES, not tested):
  - ACTIVE returns only: a return of X counts if X's switch changes Ξ at some other vertex, i.e. it is a node with ≥ 1 child. Clones are
    inactive leaves. NARROW-ACT: a return node has O(1) ACTIVE children. On narrow_n10 every node has 1 active child (the original chain).
  - TRANSITIONS: RETT per root (box 98's unit), the number of transitions containing a return rooted at e. It is ≤ |F| whatever clones do.
- (c) is clone-free: topfix_N gives one active vertex returning 2N − 3 times per root. So per-(X, root) needs ≥ linear even for active
  vertices. topfix's |F| stays linear (58 at n 210), so this does not threaten polynomiality.
- Shape (ii) proper (a COUNTER: chains whose depth grows faster than n, or super-polynomially many returns) is not built. topfix's depth
  6N − 11 is linear.

## 4. Pins (experiments/red/check.sh «R149»)
- casc/instances/narrow_n10: regenerated from new/box52/out/topfix_n10 with clone.py and defstart.py and compared (cmp); retx.py 504
  returns; xeng; Oink.
- L-NEW's tool is not on claude/l-red, so check.sh does not run retcause_br.py. Its output is kept as data in casc/narrow_out.txt.
