/-
PROPOSED DEFINITIONS, not yet diffed by the Lead.
N5's step as SPEC S1-S5 states it: DEFINITIONS ONLY (L-FORMAL successor 4, 2026-11-13; Lead 23:53Z item (b)).  No theorem in this file.  Nothing here proves N5 or says anything about its
running time: it fixes, as computable Lean functions, the objects that later statements about N5 would talk about.

Sources (opened):
* [SPEC] docs/new/N5-ssi-global.md l. 24-127: S1-S5, FIX 1-4 (l. 77-91) and «Four further SPEC points» Q1-Q4 (l. 93-127).
* [SI]   experiments/si/si.py `Engine` (l. 29-265): rank, p', rew, weight, key, extend, evaluate (l. 78-205), improving,
         initial("best").  SPEC S1 says «σ̄ is computed by Vöge-Jurdziński's procedure exactly as si.py Engine.evaluate».
* [N5X]  experiments/new/box21/n5x.py `step`, `start_pair`, `trace` (= experiments/new/box190/n5v.py mode «spec»);
         experiments/new/n5.py `dual` (l. 18).
* [R24]  docs/RESULTS.md R24 (a) Lemma R, (b) Lemma TB; docs/new/P-N5-U1-box31.md §2 (pk(v), «the root-first sequence of
         vertex indices of v's play, from c (excluded) back to v»).

Layout, as SPEC: «V = {0..n-1}, Even = owner 0»; a game is four arrays (`SGame`), strategies are arrays of successor
indices (entries at the other player's vertices are ignored, as si.py's −1 entries), a path set P is a bit mask over
RANKS (si.py's `bit[u] = 1 << rank(u)`).  Every `for _ in List.range (n + 1)` below is a FUEL bound standing for one of
si.py's `while` loops; each such loop pops a vertex that was pushed at most once, so it ends within n + 1 rounds; if
a bound were ever reached, or if si.py would raise or read a missing key, the result carries `bad = true` (the check
tool counts it; it is 0 on every run so far).  The deviation list (D1)-(D9) at the end of the file names every place
where this text departs from SPEC's wording.
-/
import Mathlib.Data.List.Dedup
import Mathlib.Data.Int.Notation
import Mathlib.Data.Nat.Notation

namespace PG.Spec

/-! ## Games and the dual (SPEC «Input», S1 «Odd's side») -/

/-- SPEC «Input: parity game G = (V, E, Ω, owner), V = {0..n-1}, Even = owner 0».  `prio v` = Ω(v), `owner v` ∈ {0, 1},
`succ v` = the successor list of v (any order, duplicates allowed: the engine sorts and deduplicates, as si.py
l. 33 `sorted(set(s))`). -/
structure SGame where
  n : ℕ
  prio : Array ℕ
  owner : Array ℕ
  succ : Array (List ℕ)
  deriving Inhabited, Repr

/-- SPEC S1: «Odd's side: everything on the DUAL game G^d (owner swapped, Ω + 1)»; n5.py l. 18
`dual(h) = Game([p + 1 for p in h.prio], [1 - o for o in h.owner], [list(s) for s in h.succ])`. -/
def SGame.dual (g : SGame) : SGame :=
  ⟨g.n, g.prio.map (· + 1), g.owner.map (1 - ·), g.succ⟩

/-! ## S1: ranks, injective priorities, rewards, valuations and their order -/

/-- The precomputed data of si.py's `Engine.__init__` (l. 30-52) for one game. -/
structure Eng where
  n : ℕ
  prio : Array ℕ
  owner : Array ℕ
  /-- sorted, deduplicated successor lists (si.py l. 33) -/
  succ : Array (List ℕ)
  /-- predecessor lists, increasing (si.py l. 34-37) -/
  pred : Array (List ℕ)
  /-- SPEC S1 «rank(v) = position of v in V sorted by (Ω(v), v)» (si.py l. 38-41) -/
  rank : Array ℕ
  /-- Ω(v) mod 2 (si.py l. 42) -/
  par : Array ℕ
  /-- SPEC S1 «p'(v) = 2·rank(v) + (Ω(v) mod 2)» (si.py l. 43) -/
  pp : Array ℕ
  /-- reward: p'(v) if even, −p'(v) if odd (si.py l. 44) -/
  rew : Array ℤ
  /-- parity of the vertex of each rank (si.py l. 46-48) -/
  rankpar : Array ℕ
  /-- V in increasing reward (si.py l. 94: «Odd's preferred cycle nodes first») -/
  order : List ℕ
  deriving Inhabited

/-- `(Ω(a), a) ≤ (Ω(b), b)` lexicographically. -/
def lexPrioLe (prio : Array ℕ) (a b : ℕ) : Bool :=
  prio[a]! < prio[b]! || (prio[a]! == prio[b]! && a ≤ b)

/-- si.py `Engine(g)`. -/
def Eng.ofGame (g : SGame) : Eng := Id.run do
  let n := g.n
  let succ : Array (List ℕ) := (Array.range n).map fun v => (g.succ[v]!.dedup).mergeSort (fun a b => a ≤ b)
  let mut pred : Array (List ℕ) := Array.replicate n []
  for v in List.range n do
    for w in succ[v]! do
      pred := pred.modify w (· ++ [v])
  let sorted := (List.range n).mergeSort (lexPrioLe g.prio)
  let mut rank : Array ℕ := Array.replicate n 0
  let mut r := 0
  for v in sorted do
    rank := rank.set! v r
    r := r + 1
  let par : Array ℕ := (Array.range n).map fun v => g.prio[v]! % 2
  let pp : Array ℕ := (Array.range n).map fun v => 2 * rank[v]! + par[v]!
  let rew : Array ℤ := (Array.range n).map fun v => if par[v]! == 0 then ((pp[v]! : ℕ) : ℤ) else -((pp[v]! : ℕ) : ℤ)
  let mut rankpar : Array ℕ := Array.replicate n 0
  for v in List.range n do
    rankpar := rankpar.set! rank[v]! par[v]!
  let order := (List.range n).mergeSort (fun a b => rew[a]! ≤ rew[b]!)
  return { n, prio := g.prio, owner := g.owner, succ, pred, rank, par, pp, rew, rankpar, order }

/-- si.py `bit[u] = 1 << rank[u]`: the path-set bit of u. -/
def Eng.bit (E : Eng) (u : ℕ) : ℕ := 1 <<< E.rank[u]!

/-- A valuation (c, P, ℓ) of SPEC S1: c the cycle node, P the path set as a bit mask over ranks, ℓ the length. -/
structure SVal where
  c : ℕ
  mask : ℕ
  len : ℕ
  deriving DecidableEq, Inhabited, Repr

/-- SPEC S1 «P by the signed weight Σ_{u∈P} (+2^rank(u) if Ω(u) even else −2^rank(u))» (si.py `weight`, l. 54-65). -/
def Eng.weight (E : Eng) (mask : ℕ) : ℤ :=
  (List.range E.n).foldl (fun acc r =>
    if mask.testBit r then acc + (if E.rankpar[r]! == 0 then (2 : ℤ) ^ r else -((2 : ℤ) ^ r)) else acc) 0

/-- The valuation key, larger = better for Even (si.py `key`, l. 68-70): SPEC S1 «compare reward of c …; then P by the
signed weight …; then ℓ: if c is odd, longer is better for Even; if c even, shorter is better». -/
def Eng.key (E : Eng) (x : SVal) : ℤ × ℤ × ℤ :=
  (E.rew[x.c]!, E.weight x.mask, if E.par[x.c]! == 1 then (x.len : ℤ) else -(x.len : ℤ))

/-- Python's tuple order on keys (lexicographic, strict). -/
def keyLt (a b : ℤ × ℤ × ℤ) : Bool :=
  a.1 < b.1 || (a.1 == b.1 && (a.2.1 < b.2.1 || (a.2.1 == b.2.1 && a.2.2 < b.2.2)))

/-- si.py `extend(u, val)` (l. 72-75): the valuation of u when u steps to a vertex of valuation `x`. -/
def Eng.extend (E : Eng) (u : ℕ) (x : SVal) : SVal :=
  ⟨x.c, x.mask ||| (if E.rank[u]! > E.rank[x.c]! then E.bit u else 0), x.len + 1⟩

/-! ## S1: Vöge-Jurdziński's procedure, exactly as si.py `Engine.evaluate` (l. 78-205) -/

/-- si.py `reach(start, excl)` (l. 117-124): the vertices reaching `start` in the current restricted graph (predecessor
lists `hp`) without passing `excl`, as a membership array; the Bool is `true` if the fuel ran out. -/
def reach (n : ℕ) (hp : Array (List ℕ)) (start excl : ℕ) : Array Bool × Bool := Id.run do
  let mut s : Array Bool := (Array.replicate n false).set! start true
  let mut st : List ℕ := [start]
  for _ in List.range (n + 1) do
    match st with
    | [] => break
    | x :: rest =>
      st := rest
      for y in hp[x]! do
        if y != excl && !s[y]! then
          s := s.set! y true
          st := y :: st
  return (s, !st.isEmpty)

/-- si.py `restrict(x, M)` (l. 126-131): x keeps only its edges into M; the predecessor lists lose the removed edges
(`hp[y].remove(x)` = the first occurrence). -/
def restrict (hs hp : Array (List ℕ)) (x : ℕ) (M : Array Bool) : Array (List ℕ) × Array (List ℕ) := Id.run do
  let keep := hs[x]!.filter fun y => M[y]!
  let mut hp := hp
  for y in hs[x]! do
    if !M[y]! then
      hp := hp.modify y (·.erase x)
  return (hs.set! x keep, hp)

/-- State of si.py's memoised `longest` (l. 148-168): `d` the memo («state[x]»), `busy` = «state[x] is None»,
`tau` the choices, `bad` = si.py would raise («cycle in restricted graph») or the fuel ran out. -/
structure LSt where
  d : Array (Option ℤ)
  busy : Array Bool
  tau : Array (Option ℕ)
  bad : Bool

/-- si.py `longest(x)` (l. 149-163), SPEC S1 (iv) for Ω(v) even: «Odd takes the LONGEST path to v in the restricted graph
(recursion over successors in list order, first strict maximum wins)»; FIX 4: «"first strict maximum" … = smallest index
among the successors of maximum length».  `fuel` bounds the recursion depth (D2). -/
def longest (v : ℕ) (hs : Array (List ℕ)) : ℕ → ℕ → StateM LSt ℤ
  | 0, _ => do
    modify fun s => { s with bad := true }
    return 0
  | fuel + 1, x => do
    if x == v then return 0
    let s ← get
    match s.d[x]! with
    | some dx => return dx
    | none =>
      if s.busy[x]! then
        modify fun s => { s with bad := true }
        return 0
      modify fun s => { s with busy := s.busy.set! x true }
      let mut best : ℤ := -1
      let mut arg : Option ℕ := none
      for y in hs[x]! do
        let dy ← longest v hs fuel y
        if dy > best then
          best := dy
          arg := some y
      modify fun s => { s with d := s.d.set! x (some (best + 1)), tau := s.tau.set! x arg }
      return best + 1

/-- The result of one evaluation: `val v` = Ξ(v) (SPEC S1 «valuation of every vertex under σ and Odd's OPTIMAL
counterstrategy σ̄»), `tau v` = σ̄(v) at Odd's vertices (`none` at Even's), `bad` (see the header). -/
structure EvalOut where
  val : Array (Option SVal)
  tau : Array (Option ℕ)
  bad : Bool
  deriving Inhabited

/-- SPEC S1, «σ̄ is computed by Vöge-Jurdziński's procedure exactly as si.py Engine.evaluate (lines 78-205)», steps
(i)-(vi) with FIX 2 / Q2 (the cycle node's own choice) and FIX 4 (tie rules).  `strat v` is used at Even's vertices
only. -/
def Eng.evaluate (E : Eng) (strat : Array ℕ) : EvalOut := Id.run do
  let n := E.n
  -- «graph Gσ = Even vertices keep only σ(v), Odd vertices keep all edges» (l. 86)
  let gs : Array (List ℕ) := (Array.range n).map fun v => if E.owner[v]! == 0 then [strat[v]!] else E.succ[v]!
  let mut gp : Array (List ℕ) := Array.replicate n []
  for v in List.range n do
    for w in gs[v]! do
      gp := gp.modify w (· ++ [v])
  let mut alive : Array Bool := Array.replicate n true
  let mut val : Array (Option SVal) := Array.replicate n none
  let mut tauFull : Array (Option ℕ) := Array.replicate n none
  let mut bad := false
  -- «For v in V in increasing order of reward(v) …, skipping dead v» (l. 94-96)
  for v in E.order do
    if !alive[v]! then continue
    let rv := E.rank[v]!
    -- (i) «v is a cycle node iff DFS from v over Gσ-successors, visiting only alive vertices of rank < rank(v), returns
    -- to v» (l. 98-106)
    let mut seen : Array Bool := (Array.replicate n false).set! v true
    let mut st : List ℕ := [v]
    let mut found := false
    for _ in List.range (n + 1) do
      if found then break
      match st with
      | [] => break
      | x :: rest =>
        st := rest
        for y in gs[x]! do
          if y == v then
            found := true
            break
          if alive[y]! && E.rank[y]! < rv && !seen[y]! then
            seen := seen.set! y true
            st := y :: st
    if !found && !st.isEmpty then bad := true
    if !found then continue
    -- (ii) «R = alive vertices that reach v in Gσ» (l. 108-113)
    let mut inR : Array Bool := (Array.replicate n false).set! v true
    let mut Rl : List ℕ := [v]
    st := [v]
    for _ in List.range (n + 1) do
      match st with
      | [] => break
      | x :: rest =>
        st := rest
        for y in gp[x]! do
          if alive[y]! && !inR[y]! then
            inR := inR.set! y true
            Rl := y :: Rl
            st := y :: st
    if !st.isEmpty then bad := true
    -- (iii) «Restricted graph on R; path[x] = ∅» (l. 114-116)
    let mut hs : Array (List ℕ) := Array.replicate n []
    let mut hp : Array (List ℕ) := Array.replicate n []
    for x in Rl do
      hs := hs.set! x ((gs[x]!).filter fun y => inR[y]!)
      hp := hp.set! x ((gp[x]!).filter fun y => inR[y]!)
    let mut path : Array ℕ := Array.replicate n 0
    -- «For u in R with rank(u) > rank(v), in decreasing rank» (l. 132)
    let us := (Rl.filter fun x => E.rank[x]! > rv).mergeSort (fun a b => E.rank[a]! ≥ E.rank[b]!)
    for u in us do
      if E.par[u]! == 0 then
        -- «Ω(u) even (Even likes u): M = vertices of R reaching v without passing u; add u to path[q] for q ∉ M; delete
        -- edges from u and from every q ∈ M to vertices outside M» (l. 133-140)
        let (M, b) := reach n hp v u
        if b then bad := true
        for q in Rl do
          if !M[q]! then path := path.modify q (· ||| E.bit u)
        (hs, hp) := restrict hs hp u M
        for q in Rl do
          if M[q]! then (hs, hp) := restrict hs hp q M
      else
        -- «Ω(u) odd (Odd likes u): M = vertices of R reaching u without passing v; add u to path[q] for q ∈ M; delete
        -- edges from every q ∈ M \ {u} to vertices outside M» (l. 141-146)
        let (M, b) := reach n hp u v
        if b then bad := true
        for q in Rl do
          if M[q]! then
            path := path.modify q (· ||| E.bit u)
            if q != u then (hs, hp) := restrict hs hp q M
    -- (iv) lengths (l. 147-180)
    let mut dist : Array (Option ℕ) := Array.replicate n none
    let mut tau : Array (Option ℕ) := Array.replicate n none
    if E.par[v]! == 0 then
      let init : LSt := ⟨Array.replicate n none, Array.replicate n false, Array.replicate n none, false⟩
      let act : StateM LSt (List (ℕ × ℤ)) := Rl.mapM fun x => do
        let dx ← longest v hs (n + 1) x
        return (x, dx)
      let (ds, s) := act.run init
      for (x, dx) in ds do
        dist := dist.set! x (some dx.toNat)
      tau := s.tau
      if s.bad then bad := true
    else
      -- «if Ω(v) odd, the SHORTEST (BFS from v over predecessors in list order; first discovery sets Odd's choice)»;
      -- FIX 4: «layers in FIFO order, each layer's vertices scanned in discovery order» (l. 170-180)
      dist := dist.set! v (some 0)
      let mut layer : List ℕ := [v]
      for _ in List.range (n + 1) do
        if layer.isEmpty then break
        let mut nxt : Array ℕ := #[]
        for x in layer do
          for y in hp[x]! do
            if dist[y]!.isNone then
              dist := dist.set! y (some (dist[x]!.getD 0 + 1))
              tau := tau.set! y (some x)
              nxt := nxt.push y
        layer := nxt.toList
      if !layer.isEmpty then bad := true
    -- (v) FIX 2 / Q2: «explicit-stack DFS from v over the successors of the fixed-strategy graph Gσ (NOT the restricted
    -- graph), successors scanned in increasing index, each unvisited alive y of rank < rank(v) marked visited and pushed
    -- when scanned, last pushed popped first; the scan stops at the first successor equal to v; v's choice = the first
    -- vertex after v on the DFS tree path to that vertex (v itself for a self-loop)» (l. 182-195)
    if E.owner[v]! == 1 then
      let mut inPar : Array Bool := (Array.replicate n false).set! v true
      let mut parent : Array ℕ := Array.replicate n v
      let mut st2 : List ℕ := [v]
      let mut cyc : Option ℕ := none
      for _ in List.range (n + 1) do
        if cyc.isSome then break
        match st2 with
        | [] => break
        | x :: rest =>
          st2 := rest
          for y in gs[x]! do
            if y == v then
              cyc := some x
              break
            if alive[y]! && E.rank[y]! < rv && !inPar[y]! then
              inPar := inPar.set! y true
              parent := parent.set! y x
              st2 := y :: st2
      match cyc with
      | none => bad := true
      | some cy =>
        let mut x := cy
        for _ in List.range (n + 1) do
          if x == v then break
          if parent[x]! == v then break
          x := parent[x]!
        tau := tau.set! v (some (if x != v then x else cy))
    -- (vi) «Every x in R gets valuation (v, path[x], length[x]) and Odd's choice from (iv)/(v); R becomes dead»
    -- (l. 196-201)
    for x in Rl do
      match dist[x]! with
      | none => bad := true
      | some dx => val := val.set! x (some ⟨v, path[x]!, dx⟩)
      alive := alive.set! x false
      if E.owner[x]! == 1 then
        if tau[x]!.isNone then bad := true
        tauFull := tauFull.set! x tau[x]!
  -- every vertex lies in some R (VJ00); a vertex without a valuation would make si.py's `improving` raise
  if val.any (·.isNone) then bad := true
  return ⟨val, tauFull, bad⟩

/-- The valuation of `w` (`default` where the procedure gave none; then `bad` is set). -/
def EvalOut.valOf (o : EvalOut) (w : ℕ) : SVal := o.val[w]!.getD default

/-! ## S2: improving edges -/

/-- SPEC S2 «Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v), Ξσ(w) strictly better than Ξσ(σ(v))}» (si.py `improving`,
l. 220-228); in increasing (v, w). -/
def Eng.improving (E : Eng) (strat : Array ℕ) (o : EvalOut) : List (ℕ × ℕ) :=
  (List.range E.n).flatMap fun v =>
    if E.owner[v]! == 0 then
      let kc := E.key (o.valOf strat[v]!)
      (E.succ[v]!).filterMap fun w =>
        if w != strat[v]! && keyLt kc (E.key (o.valOf w)) then some (v, w) else none
    else []

/-! ## S3: the best-reward start -/

/-- FIX 1 / si.py `initial("best")` (l. 234-240): Even's v takes the successor maximising (r(w), w if r(w) even else −w),
r(w) = Ω(w) if even else −Ω(w).  Entries at Odd's vertices: 0 (si.py: −1; never read). -/
def Eng.initialBest (E : Eng) : Array ℕ :=
  (Array.range E.n).map fun v =>
    if E.owner[v]! == 1 then 0 else
      let k : ℕ → ℤ × ℤ := fun w =>
        if E.prio[w]! % 2 == 0 then (((E.prio[w]! : ℕ) : ℤ), (w : ℤ)) else (-((E.prio[w]! : ℕ) : ℤ), -(w : ℤ))
      (E.succ[v]!).foldl (fun b w => if (k b).1 < (k w).1 || ((k b).1 == (k w).1 && (k b).2 < (k w).2) then w else b)
        (E.succ[v]!.headD 0)

/-! ## S4: one iteration -/

/-- One iteration's outputs, as n5x.py `step`: the new pair, Iσ, Iτ, the fallback flag, and `bad`. -/
structure StepOut where
  sigma : Array ℕ
  tau : Array ℕ
  Is : List (ℕ × ℕ)
  It : List (ℕ × ℕ)
  fb : Bool
  bad : Bool
  deriving Inhabited

/-- SPEC S4a «A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ}» for Even v, sorted (n5x.py l. 25-27 `sorted(opt[v])`). -/
def improvSet (owner : Array ℕ) (who : ℕ) (cur : Array ℕ) (I : List (ℕ × ℕ)) (v : ℕ) : List ℕ :=
  if owner[v]! == who then ((cur[v]! :: (I.filterMap fun p => if p.1 == v then some p.2 else none)).dedup).mergeSort
    (fun a b => a ≤ b)
  else []

/-- SPEC S4a's arena H: «Even v keeps only edges to A(v); Odd v keeps only the edge to τ(v)» (n5x.py l. 27). -/
def arenaH (g : SGame) (sigma tau : Array ℕ) (Is : List (ℕ × ℕ)) : SGame :=
  ⟨g.n, g.prio, g.owner, (Array.range g.n).map fun v =>
    if g.owner[v]! == 0 then improvSet g.owner 0 sigma Is v else [tau[v]!]⟩

/-- SPEC S4b's arena H': «Odd v keeps only edges to A(v); Even v only the edge to σ(v)» (n5x.py l. 35). -/
def arenaH' (g : SGame) (sigma tau : Array ℕ) (It : List (ℕ × ℕ)) : SGame :=
  ⟨g.n, g.prio, g.owner, (Array.range g.n).map fun v =>
    if g.owner[v]! == 1 then improvSet g.owner 1 tau It v else [sigma[v]!]⟩

/-- SPEC S4a «σ_new = Odd's optimal counterstrategy (S1 procedure) in the dual of H to the dual-Even strategy τ, read as an
Even strategy of G» (n5x.py l. 28-30).  Returns the choices at G's Even vertices and `bad`. -/
def s4a (g : SGame) (sigma tau : Array ℕ) (Is : List (ℕ × ℕ)) : Array ℕ × Bool :=
  let Er := Eng.ofGame (arenaH g sigma tau Is).dual
  let o := Er.evaluate tau
  let ns := (Array.range g.n).map fun v => if g.owner[v]! == 0 then o.tau[v]!.getD sigma[v]! else sigma[v]!
  (ns, o.bad || (List.range g.n).any fun v => g.owner[v]! == 0 && o.tau[v]!.isNone)

/-- SPEC S4b «τ_new = Odd's optimal counterstrategy (S1 procedure on H', not dual) to σ» (n5x.py l. 36-38). -/
def s4b (g : SGame) (sigma tau : Array ℕ) (It : List (ℕ × ℕ)) : Array ℕ × Bool :=
  let Er := Eng.ofGame (arenaH' g sigma tau It)
  let o := Er.evaluate sigma
  let nt := (Array.range g.n).map fun v => if g.owner[v]! == 1 then o.tau[v]!.getD tau[v]! else tau[v]!
  (nt, o.bad || (List.range g.n).any fun v => g.owner[v]! == 1 && o.tau[v]!.isNone)

/-- SPEC S4c / FIX 3 / A7: «for every Even v with an improving edge set σ_new(v) = the w with (v, w) ∈ Iσ maximising
(Ξσ(w), w) (best valuation, ties: larger index)» (n5x.py l. 43-44); the same for Odd with G^d's valuations. -/
def fallbackAt (E : Eng) (o : EvalOut) (I : List (ℕ × ℕ)) (cur : Array ℕ) : Array ℕ :=
  (Array.range cur.size).map fun v =>
    let ws := I.filterMap fun p => if p.1 == v then some p.2 else none
    match ws with
    | [] => cur[v]!
    | w0 :: rest =>
      rest.foldl (fun b w =>
        let kb := E.key (o.valOf b); let kw := E.key (o.valOf w)
        if keyLt kb kw || (kb == kw && b < w) then w else b) w0

/-- SPEC S4 «one iteration = one pass with Iσ ∪ Iτ ≠ ∅; both steps computed from the SAME (σ, τ), applied together»;
`none` = SPEC S5 «Stop when Iσ = Iτ = ∅» (n5x.py `step`, l. 15-46). -/
def specStep (g : SGame) (E Ed : Eng) (sigma tau : Array ℕ) : Option StepOut :=
  let ov := E.evaluate sigma
  let Is := E.improving sigma ov
  let od := Ed.evaluate tau
  let It := Ed.improving tau od
  if Is.isEmpty && It.isEmpty then none else
  let (ns, ba) := if Is.isEmpty then (sigma, false) else s4a g sigma tau Is
  let (nt, bb) := if It.isEmpty then (tau, false) else s4b g sigma tau It
  let bad := ov.bad || od.bad || ba || bb
  if ns == sigma && nt == tau then
    if !Is.isEmpty then some ⟨fallbackAt E ov Is sigma, tau, Is, It, true, bad⟩
    else some ⟨sigma, fallbackAt Ed od It tau, Is, It, true, bad⟩
  else some ⟨ns, nt, Is, It, false, bad⟩

/-- n5x.py `start_pair`: the best-reward start of S3 for both players (Odd's on G^d), overwritten by a given start pair
(lists of (v, w)). -/
def startPair (E Ed : Eng) (start : Option (List (ℕ × ℕ) × List (ℕ × ℕ))) : Array ℕ × Array ℕ :=
  let s0 := E.initialBest
  let t0 := Ed.initialBest
  match start with
  | none => (s0, t0)
  | some (ss, ts) => (ss.foldl (fun a p => a.set! p.1 p.2) s0, ts.foldl (fun a p => a.set! p.1 p.2) t0)

/-- A run of N5 (n5x.py `trace`, n5v.py `run(g, "spec")`): the states (σ_0, τ_0), (σ_1, τ_1), …, the step records,
stopped by S5 or after `cap` iterations. -/
structure RunOut where
  states : List (Array ℕ × Array ℕ)
  steps : List StepOut
  stopped : Bool
  deriving Inhabited

/-- SPEC S1-S5 on `g` from the start of S3 (or the given start pair), at most `cap` iterations. -/
def specRun (g : SGame) (start : Option (List (ℕ × ℕ) × List (ℕ × ℕ))) (cap : ℕ) : RunOut := Id.run do
  let E := Eng.ofGame g
  let Ed := Eng.ofGame g.dual
  let (s0, t0) := startPair E Ed start
  let mut sigma := s0
  let mut tau := t0
  let mut states : Array (Array ℕ × Array ℕ) := #[(s0, t0)]
  let mut steps : Array StepOut := #[]
  let mut stopped := false
  for _ in List.range (cap + 1) do
    match specStep g E Ed sigma tau with
    | none =>
      stopped := true
      break
    | some r =>
      if steps.size == cap then break
      sigma := r.sigma
      tau := r.tau
      states := states.push (sigma, tau)
      steps := steps.push r
  return ⟨states.toList, steps.toList, stopped⟩

/-! ## The root-first key and the key rule (R24 (a), (b); the object L-NEW 74's box 212/213 reduces O1′ to)

SPEC states S4a's choice through the procedure.  R24 (refereed-only) reads that choice as a rule on values: Lemma R «every
FULLY optimal successor of x … survives, so the length step chooses among exactly the fully optimal edges (FIX 4 order)»,
and TB's proof step 5 «the queue order of a layer is the lex order of the root-first index sequences of the BFS-tree
paths».  The two definitions below state that rule for ANY call of the procedure, as a checkable property of its output.
That SPEC's procedure satisfies it is NOT claimed here (it is DATA in check/speccheck.py, and a theorem to state later). -/

/-- The play from `x` under the successor map `s`, before its first visit of `c` (c excluded); at most `n` vertices. -/
def playTo (s : Array ℕ) (c n : ℕ) (x : ℕ) : List ℕ := Id.run do
  let mut out : Array ℕ := #[]
  let mut y := x
  for _ in List.range n do
    if y == c then break
    out := out.push y
    y := s[y]!
  return out.toList

/-- P-N5-U1 §2 (R24 TB): «pk(v) is the root-first sequence of vertex indices of v's play, from c (excluded) back to v». -/
def rootKey (s : Array ℕ) (c n : ℕ) (x : ℕ) : List ℕ := (playTo s c n x).reverse

/-- Lexicographic order on index sequences (Python's list order). -/
def lexLe : List ℕ → List ℕ → Bool
  | [], _ => true
  | _ :: _, [] => false
  | a :: as, b :: bs => a < b || (a == b && lexLe as bs)

/-- The TIED successors of x for the values `o` of game `E`: «FULLY optimal (equal in cycle node, path set and length)»
(R24 (a)), i.e. extend(x, Ξ(w)) = Ξ(x) (n5v.py l. 34 `Er.extend(v, vh[w]) == vh[v]`). -/
def Eng.tied (E : Eng) (o : EvalOut) (x : ℕ) : List ℕ :=
  (E.succ[x]!).filter fun w => decide (E.extend x (o.valOf w) = o.valOf x)

/-- THE KEY RULE at the chooser's vertex `x` (an Odd vertex of the game of `E`, which is not its own cycle node), for the
output `o` of the procedure on strategy `strat`: the choice is a tied successor, and
* if the cycle node c has EVEN Ω in this game (SPEC S1 (iv) longest-path mode): the tied successor of least index;
* if c has ODD Ω (BFS mode): a tied successor of lexicographically least root-first key, keys read from the final
  successor map (strat at Even's vertices, the choices at Odd's).
For S4a the game is the dual of H (so c's parity in G is flipped: TB-odd / TB-even), for S4b it is H'. -/
def Eng.keyRuleAt (E : Eng) (strat : Array ℕ) (o : EvalOut) (x : ℕ) : Bool :=
  let c := (o.valOf x).c
  if E.owner[x]! != 1 || c == x then true else
  match o.tau[x]! with
  | none => false
  | some t =>
    let T := E.tied o x
    let s : Array ℕ := (Array.range E.n).map fun y =>
      if E.owner[y]! == 0 then strat[y]! else (o.tau[y]!).getD y
    T.contains t &&
      (if E.par[c]! == 0 then T.all (fun w => t ≤ w)
       else T.all (fun w => lexLe (rootKey s c E.n t) (rootKey s c E.n w)))

/-- The key rule at every vertex. -/
def Eng.keyRule (E : Eng) (strat : Array ℕ) (o : EvalOut) : Bool :=
  (List.range E.n).all (E.keyRuleAt strat o)

/-! ## Deviation list (every place where this text departs from SPEC's wording)

(D1) Representation: V = {0..n-1} as `ℕ` with arrays (SPEC's own «V = {0..n-1}»); a strategy is an array with ignored
     entries at the other player's vertices (si.py: −1; here 0 or the current value); P is a bit mask over ranks (si.py),
     compared through SPEC S1's signed weight; SPEC Q1's symmetric-difference rule is equivalent and not used here.
(D2) Fuel: si.py's `while` loops and the recursion of `longest` are bounded by n + 1 rounds / depth n + 1; reaching a
     bound sets `bad`.  Also `bad` where si.py raises (`RuntimeError("cycle in restricted graph")`, a KeyError on a
     missing length or choice, a missing DFS cycle at a cycle node, a vertex without a valuation) or stores None as an
     Odd vertex's choice (si.py would carry the None on; here the old choice is kept).  On every run of the check tool
     `bad` = 0.
(D3) si.py iterates over Python SETS (R, M, `{v for v, _ in Is}`) where the order cannot change the result (the memoised
     lengths, the commutative path / restrict updates, independent fallback assignments); here lists in a fixed order.
(D4) si.py's `par[x] is not v` (l. 193, object identity) is read as value equality.  Lead 02:06Z asked whether this is a
     defect of the reference for n > 256 (CPython caches only the ints −5..256).  ANSWER: NO DEFECT, by construction.
     `par = {v: None}; st = [v]` (l. 184) puts the loop object v on the stack; every value stored by `par[y] = x`
     (l. 191) is an object popped from the stack; a successor y equal to v is never pushed (l. 187-189 test `y == v`
     first and break), so the only stack object equal to v is v itself, and `par[x] is not v` ⟺ `par[x] != v` for
     non-None values.  PROBE (check/d4probe.py, a line tracer on si.py's own code path, si.py unmodified; output
     check/out/d4probe.out): on box113 w_re3_1, box72 latew_K20_m32 (n = 538), box97 obs_K12_m24 (n = 272), box189
     REC_d12_mu42_norm (Γ3, n = 370), 200 iterations or to the stop, 612 executions of l. 193, eq_not_id 0 (no value
     equal to v that is not v); there no Odd cycle node has index > 256; on the synthetic check/d4/d4_big_odd_cycle_n400.pg
     (Odd cycle node 350 → 351 → 352 → 350, a two-step walk), 399 executions with 142 at v > 256, eq_not_id 0, and the
     walk stops at v = 350 by identity (eq_id 1).  A separate probe confirms that v from `sorted(range(600))` at 300 is
     not the object of an independent int 300, so identity would matter if equal non-identical objects could reach par.
(D5) SPEC's «both steps computed from the SAME (σ, τ)»: `specStep` evaluates both from the old pair (as n5x.py); the
     fallback test is equality of the whole arrays (as n5x.py's list equality).
(D6) The output of SPEC S5 (regions, Odd's strategy σ̄ of the final σ) is not defined here; `specRun` returns the states.
(D7) Start: n5x.py `start_pair` = S3's best-reward start overwritten by a given pair; the start validation of n5x.py
     (box 113) is not performed.
(D8) The key rule (`keyRuleAt`) is NOT SPEC's wording: it is R24's reading of SPEC's choice (Lemma R + TB step 5), stated
     for every call of the procedure; SPEC defines the choice by the procedure only.
(D9) Counting: SPEC's «one iteration = one pass with Iσ ∪ Iτ ≠ ∅» = the length of `steps`; `cap` bounds it.
-/

end PG.Spec
