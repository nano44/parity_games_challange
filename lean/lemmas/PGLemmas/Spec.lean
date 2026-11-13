/-
DEFINITIONS: N5's step as SPEC S1-S5 states it (L-FORMAL successor 4, 2026-11-13; Lead 23:53Z item (b)).  No theorem in
this file.  Nothing here proves N5 or says anything about its running time.
STATUS: the Lead's diff of the text at 0ee5b8bc (sha1 9156c048…) against SPEC blob 81e966da, si.py blob 0747733e and n5x.py
blob 21c3201f: «ACCEPTED WITH FIXES» (Lead 03:58Z), with REFEREE-2 40's reading (docs/referee-2/R2-SPEC-LEAN.md) as a second
reader.  THIS TEXT = that text with the fixes U1-U4 and, as ruled by the Lead 03:46Z, (1) every loop of the procedure
written as a named step function run by `loopFuel`, (2) `bad` split into `fuelOut` (a fuel bound was reached) and `fault`
(si.py would raise, read a missing key or carry a None choice on), (3) the parent walk of FIX 2 kept literal (option (a)),
under `loopFuel` with its own `fuelOut`.  «Semantics unchanged» is checked, not asserted: check/speccheck.py re-run on all
101 + 25 instances and the controls (check/out/speccheck*.out).  The map from the accepted text's blocks to the functions
below is in the commit message.

Sources (opened; line numbers checked by check/speccite.py against the blobs above, output check/out/speccite.out):
* [SPEC] docs/new/N5-ssi-global.md l. 24-127: S1-S5, FIX 1-4 (l. 77-91) and «Four further SPEC points» Q1-Q4 (l. 93-127).
* [SI]   experiments/si/si.py `Engine` (si.py l. 29-52 setup; `evaluate` si.py l. 78-203): SPEC S1 says «σ̄ is computed by
         Vöge-Jurdziński's procedure exactly as si.py Engine.evaluate».
* [N5X]  experiments/new/box21/n5x.py `step` (n5x.py l. 15-45), `start_pair` (n5x.py l. 47-59), `trace` (= n5v.py
         experiments/new/box190, mode «spec»); experiments/new/n5.py `dual` (n5.py l. 18).
* [R24]  docs/RESULTS.md R24 (a) Lemma R, (b) Lemma TB; docs/new/P-N5-U1-box31.md §2.

Layout, as SPEC: «V = {0..n-1}, Even = owner 0»; a game is four arrays (`SGame`; well formed: `SGame.WF`), strategies are
arrays of successor indices (entries at the other player's vertices are ignored, as si.py's −1 entries), a path set P is a
bit mask over RANKS (si.py's `bit[u] = 1 << rank(u)`, si.py l. 45).  The deviation list (D1)-(D11) at the end of the file names
every place where this text departs from SPEC's wording.
-/
import Mathlib.Data.List.Dedup
import Mathlib.Data.Int.Notation
import Mathlib.Data.Nat.Notation

namespace PG.Spec

/-! ## Games, well-formedness and the dual (SPEC «Input», S1 «Odd's side») -/

/-- SPEC «Input: parity game G = (V, E, Ω, owner), V = {0..n-1}, Even = owner 0».  `prio v` = Ω(v), `owner v` ∈ {0, 1},
`succ v` = the successor list of v (any order, duplicates allowed: the engine sorts and deduplicates, as
si.py l. 33 `sorted(set(s))`). -/
structure SGame where
  n : ℕ
  prio : Array ℕ
  owner : Array ℕ
  succ : Array (List ℕ)
  deriving Inhabited, Repr

/-- A WELL-FORMED input (Lead 03:58Z U1; deviation (D10)): arrays of length n, owners in {0, 1}, every vertex has a
successor, every successor is a vertex.  The procedure does not check this; every theorem about it takes `SGame.WF`. -/
structure SGame.WF (g : SGame) : Prop where
  prio_size : g.prio.size = g.n
  owner_size : g.owner.size = g.n
  succ_size : g.succ.size = g.n
  owner_le : ∀ v, v < g.n → g.owner[v]! ≤ 1
  succ_ne : ∀ v, v < g.n → g.succ[v]! ≠ []
  succ_lt : ∀ v, v < g.n → ∀ w ∈ g.succ[v]!, w < g.n

/-- A strategy of player `who` (0 = Even) in `g`: an array of length n choosing a successor at each of who's vertices. -/
def SGame.StratWF (g : SGame) (who : ℕ) (s : Array ℕ) : Prop :=
  s.size = g.n ∧ ∀ v, v < g.n → g.owner[v]! = who → s[v]! ∈ g.succ[v]!

/-- SPEC S1: «Odd's side: everything on the DUAL game G^d (owner swapped, Ω + 1)»; n5.py l. 18
`dual(h) = Game([p + 1 for p in h.prio], [1 - o for o in h.owner], [list(s) for s in h.succ])`. -/
def SGame.dual (g : SGame) : SGame :=
  ⟨g.n, g.prio.map (· + 1), g.owner.map (1 - ·), g.succ⟩

/-! ## S1: ranks, injective priorities, rewards, valuations and their order -/

/-- The precomputed data of si.py's `Engine.__init__` (si.py l. 29-52) for one game. -/
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

/-- si.py `Engine(g)` (si.py l. 29-52), written with folds. -/
def Eng.ofGame (g : SGame) : Eng :=
  let n := g.n
  let succ : Array (List ℕ) := (Array.range n).map fun v => (g.succ[v]!.dedup).mergeSort (fun a b => a ≤ b)
  let pred : Array (List ℕ) := (List.range n).foldl (fun a v => (succ[v]!).foldl (fun a w => a.modify w (· ++ [v])) a)
    (Array.replicate n [])
  let sorted := (List.range n).mergeSort (lexPrioLe g.prio)
  let rank : Array ℕ := (sorted.foldl (fun (p : Array ℕ × ℕ) v => (p.1.set! v p.2, p.2 + 1)) (Array.replicate n 0, 0)).1
  let par : Array ℕ := (Array.range n).map fun v => g.prio[v]! % 2
  let pp : Array ℕ := (Array.range n).map fun v => 2 * rank[v]! + par[v]!
  let rew : Array ℤ := (Array.range n).map fun v => if par[v]! == 0 then ((pp[v]! : ℕ) : ℤ) else -((pp[v]! : ℕ) : ℤ)
  let rankpar : Array ℕ := (List.range n).foldl (fun a v => a.set! rank[v]! par[v]!) (Array.replicate n 0)
  let order := (List.range n).mergeSort (fun a b => rew[a]! ≤ rew[b]!)
  { n, prio := g.prio, owner := g.owner, succ, pred, rank, par, pp, rew, rankpar, order }

/-- si.py `bit[u] = 1 << rank[u]` (si.py l. 45): the path-set bit of u. -/
def Eng.bit (E : Eng) (u : ℕ) : ℕ := 1 <<< E.rank[u]!

/-- A valuation (c, P, ℓ) of SPEC S1: c the cycle node, P the path set as a bit mask over ranks, ℓ the length. -/
structure SVal where
  c : ℕ
  mask : ℕ
  len : ℕ
  deriving DecidableEq, Inhabited, Repr

/-- SPEC S1 «P by the signed weight Σ_{u∈P} (+2^rank(u) if Ω(u) even else −2^rank(u))» (si.py `weight`, si.py l. 54-65). -/
def Eng.weight (E : Eng) (mask : ℕ) : ℤ :=
  (List.range E.n).foldl (fun acc r =>
    if mask.testBit r then acc + (if E.rankpar[r]! == 0 then (2 : ℤ) ^ r else -((2 : ℤ) ^ r)) else acc) 0

/-- The valuation key, larger = better for Even (si.py `key`, si.py l. 68-70): SPEC S1 «compare reward of c …; then P by the
signed weight …; then ℓ: if c is odd, longer is better for Even; if c even, shorter is better». -/
def Eng.key (E : Eng) (x : SVal) : ℤ × ℤ × ℤ :=
  (E.rew[x.c]!, E.weight x.mask, if E.par[x.c]! == 1 then (x.len : ℤ) else -(x.len : ℤ))

/-- Python's tuple order on keys (lexicographic, strict). -/
def keyLt (a b : ℤ × ℤ × ℤ) : Bool :=
  a.1 < b.1 || (a.1 == b.1 && (a.2.1 < b.2.1 || (a.2.1 == b.2.1 && a.2.2 < b.2.2)))

/-- si.py `extend(u, val)` (si.py l. 72-75): the valuation of u when u steps to a vertex of valuation `x`. -/
def Eng.extend (E : Eng) (u : ℕ) (x : SVal) : SVal :=
  ⟨x.c, x.mask ||| (if E.rank[u]! > E.rank[x.c]! then E.bit u else 0), x.len + 1⟩

/-! ## S1: Vöge-Jurdziński's procedure, exactly as si.py `Engine.evaluate` (si.py l. 78-203) -/

/-- FUEL LOOP: iterate `step` until it returns `none`, at most `k` times; the Bool is `true` iff the fuel ran out (another
step would still have been possible).  Stands for one of si.py's `while` loops (D2). -/
def loopFuel {S : Type} (step : S → Option S) : ℕ → S → S × Bool
  | 0, s => (s, (step s).isSome)
  | k + 1, s => match step s with
    | none => (s, false)
    | some s' => loopFuel step k s'

/-- The state of si.py's explicit-stack DFS loops: marks (`seen` / `R` / `s` / `par`), the LIFO stack, the marked vertices
(newest first), the vertex whose scan met the stop vertex (si.py's `found` / `cyc`), and the parent of each pushed vertex
(si.py's `par`; the root's entry is the root). -/
structure DS where
  seen : Array Bool
  st : List ℕ
  marked : List ℕ
  hit : Option ℕ
  parent : Array ℕ

/-- The scan of the popped vertex `x` (si.py l. 102-106, 113-115, 124-126, 187-191): successors in list order; stop at the
first successor equal to `stop` (recording x); push every eligible (`ok`) unmarked successor, marking it when pushed. -/
def scan (stop : Option ℕ) (ok : ℕ → Bool) (x : ℕ) : List ℕ → DS → DS
  | [], d => d
  | y :: ys, d =>
    if some y == stop then { d with hit := some x }
    else if ok y && !d.seen[y]! then
      scan stop ok x ys { d with seen := d.seen.set! y true, st := y :: d.st, marked := y :: d.marked,
                                 parent := d.parent.set! y x }
    else scan stop ok x ys d

/-- One round of si.py's `while st and not found` / `while st` (si.py l. 100, 111, 122, 185): pop, then scan. -/
def dfsStep (g : Array (List ℕ)) (stop : Option ℕ) (ok : ℕ → Bool) (d : DS) : Option DS :=
  if d.hit.isSome then none else
  match d.st with
  | [] => none
  | x :: rest => some (scan stop ok x (g[x]!) { d with st := rest })

/-- A DFS from `root` over the successor lists `g`, n + 1 rounds of fuel; the Bool = fuel ran out. -/
def dfs (n : ℕ) (g : Array (List ℕ)) (root : ℕ) (stop : Option ℕ) (ok : ℕ → Bool) : DS × Bool :=
  loopFuel (dfsStep g stop ok) (n + 1)
    ⟨(Array.replicate n false).set! root true, [root], [root], none, Array.replicate n root⟩

/-- si.py `restrict(x, M)` (si.py l. 129-134): x keeps only its edges into M (order kept); the predecessor lists lose the
removed edges (`hp[y].remove(x)` = the first occurrence). -/
def restrict (hs hp : Array (List ℕ)) (x : ℕ) (M : Array Bool) : Array (List ℕ) × Array (List ℕ) :=
  (hs.set! x ((hs[x]!).filter fun y => M[y]!),
   (hs[x]!).foldl (fun hp y => if !M[y]! then hp.modify y (·.erase x) else hp) hp)

/-- si.py l. 136-143 (Ω(u) even), the restrictions after the path update: «delete edges from u and from every q ∈ M to
vertices outside M». -/
def evenFold (M : Array Bool) (Rl : List ℕ) (a : Array (List ℕ) × Array (List ℕ)) : Array (List ℕ) × Array (List ℕ) :=
  Rl.foldl (fun (a : Array (List ℕ) × Array (List ℕ)) q => if M[q]! then restrict a.1 a.2 q M else a) a

/-- si.py l. 144-149 (Ω(u) odd): «add u to path[q] for q ∈ M; delete edges from every q ∈ M \ {u} to vertices outside
M». -/
def oddFold (E : Eng) (u : ℕ) (M : Array Bool) (Rl : List ℕ) (a : Array (List ℕ) × Array (List ℕ) × Array ℕ) :
    Array (List ℕ) × Array (List ℕ) × Array ℕ :=
  Rl.foldl (fun (a : Array (List ℕ) × Array (List ℕ) × Array ℕ) q =>
    if M[q]! then
      if q != u then ((restrict a.1 a.2.1 q M).1, (restrict a.1 a.2.1 q M).2, a.2.2.modify q (· ||| E.bit u))
      else (a.1, a.2.1, a.2.2.modify q (· ||| E.bit u))
    else a) a

/-- One u of si.py's loop «for u in R with rank(u) > rank(v), in decreasing rank» (si.py l. 135-149): (hs, hp, path, fuel
flag).  `M` = si.py's `reach` (si.py l. 120-127) as a DFS over `hp`, not entering the excluded vertex. -/
def phaseU (E : Eng) (n v : ℕ) (Rl : List ℕ) (x : Array (List ℕ) × Array (List ℕ) × Array ℕ × Bool) (u : ℕ) :
    Array (List ℕ) × Array (List ℕ) × Array ℕ × Bool :=
  if E.par[u]! == 0 then
    let D := dfs n x.2.1 v none (fun y => y != u)
    let path := Rl.foldl (fun p q => if !D.1.seen[q]! then p.modify q (· ||| E.bit u) else p) x.2.2.1
    let r := evenFold D.1.seen Rl (restrict x.1 x.2.1 u D.1.seen)
    (r.1, r.2, path, x.2.2.2 || D.2)
  else
    let D := dfs n x.2.1 u none (fun y => y != v)
    let r := oddFold E u D.1.seen Rl (x.1, x.2.1, x.2.2.1)
    (r.1, r.2.1, r.2.2, x.2.2.2 || D.2)

/-- State of si.py's memoised `longest` (si.py l. 153-169): `d` the memo («state[x]»), `busy` = «state[x] is None», `tau`
the choices, `fuelOut`, and `fault` = si.py's `RuntimeError("cycle in restricted graph")`. -/
structure LSt where
  d : Array (Option ℤ)
  busy : Array Bool
  tau : Array (Option ℕ)
  fuelOut : Bool
  fault : Bool

/-- si.py `longest(x)` (si.py l. 154-169), SPEC S1 (iv) for Ω(v) even: «Odd takes the LONGEST path to v in the restricted
graph (recursion over successors in list order, first strict maximum wins)»; FIX 4: «"first strict maximum" … = smallest
index among the successors of maximum length».  Explicit state passing; the first argument is the fuel (the recursion
depth, D2). -/
def longest (v : ℕ) (hs : Array (List ℕ)) : ℕ → ℕ → LSt → ℤ × LSt
  | 0, _, s => (0, { s with fuelOut := true })
  | f + 1, x, s =>
    if x == v then (0, s) else
    match s.d[x]! with
    | some dx => (dx, s)
    | none =>
      if s.busy[x]! then (0, { s with fault := true }) else
      let r := (hs[x]!).foldl (fun (p : (ℤ × Option ℕ) × LSt) y =>
          let q := longest v hs f y p.2
          (if q.1 > p.1.1 then (q.1, some y) else p.1, q.2)) ((-1, none), { s with busy := s.busy.set! x true })
      (r.1.1 + 1, { r.2 with d := r.2.d.set! x (some (r.1.1 + 1)), tau := r.2.tau.set! x r.1.2 })

/-- si.py l. 170-171 «for x in R: dist[x] = longest(x)», fuel n + 1 per call. -/
def longestAll (n v : ℕ) (hs : Array (List ℕ)) (Rl : List ℕ) : Array (Option ℕ) × LSt :=
  Rl.foldl (fun (p : Array (Option ℕ) × LSt) x =>
    (p.1.set! x (some (longest v hs (n + 1) x p.2).1.toNat), (longest v hs (n + 1) x p.2).2))
    (Array.replicate n none, ⟨Array.replicate n none, Array.replicate n false, Array.replicate n none, false, false⟩)

/-- The BFS state of SPEC S1 (iv) for Ω(v) odd (si.py l. 172-180). -/
structure BS where
  dist : Array (Option ℕ)
  tau : Array (Option ℕ)
  layer : List ℕ

/-- One scanned predecessor y of x: «first discovery sets Odd's choice». -/
def bfsInner (x : ℕ) (a : BS) (y : ℕ) : BS :=
  if a.dist[y]!.isNone then
    { a with dist := a.dist.set! y (some (a.dist[x]!.getD 0 + 1)), tau := a.tau.set! y (some x), layer := a.layer ++ [y] }
  else a

/-- One layer of the BFS (si.py l. 174-180); FIX 4 «layers in FIFO order, each layer's vertices scanned in discovery order,
predecessor lists in increasing index». -/
def bfsStep (hp : Array (List ℕ)) (b : BS) : Option BS :=
  if b.layer.isEmpty then none else
  some (b.layer.foldl (fun acc x => (hp[x]!).foldl (bfsInner x) acc) { b with layer := [] })

/-- (iv) (si.py l. 150-180): lengths and choices on R; (dist, tau, fuelOut, fault). -/
def lengths (E : Eng) (n v : ℕ) (Rl : List ℕ) (hs hp : Array (List ℕ)) :
    Array (Option ℕ) × Array (Option ℕ) × Bool × Bool :=
  if E.par[v]! == 0 then
    let L := longestAll n v hs Rl
    (L.1, L.2.tau, L.2.fuelOut, L.2.fault)
  else
    let B := loopFuel (bfsStep hp) (n + 1) ⟨(Array.replicate n none).set! v (some 0), Array.replicate n none, [v]⟩
    (B.1.dist, B.1.tau, B.2, false)

/-- (v) FIX 2 / Q2, the parent walk of si.py l. 192-195, literal (Lead 03:46Z: option (a)): from the vertex `cy` whose scan
met v, «while par[x] is not v and par[x] is not None: x = par[x]» (`par[v]` is None: the walk stops at v), under fuel; then
«tau[v] = x if x != v else cyc».  Returns (choice, fuel-out). -/
def walk (n v : ℕ) (parent : Array ℕ) (cy : ℕ) : ℕ × Bool :=
  let W := loopFuel (fun x => if x == v || parent[x]! == v then none else some parent[x]!) (n + 1) cy
  (if W.1 != v then W.1 else cy, W.2)

/-- The state of the outer loop of si.py `evaluate` (si.py l. 91-93): alive, val, tau_full, and the two flags. -/
structure ES where
  alive : Array Bool
  val : Array (Option SVal)
  tau : Array (Option ℕ)
  fuelOut : Bool
  fault : Bool

/-- (vi) (si.py l. 196-200): «Every x in R gets valuation (v, path[x], length[x]) and Odd's choice from (iv)/(v); R becomes
dead»; a missing length or an Odd vertex without a choice is a `fault` (si.py: KeyError / a None carried on). -/
def assign (E : Eng) (v : ℕ) (Rl : List ℕ) (path : Array ℕ) (dist tau : Array (Option ℕ)) (s : ES) : ES :=
  Rl.foldl (fun (s : ES) x =>
    let s := match dist[x]! with
      | none => { s with fault := true }
      | some dx => { s with val := s.val.set! x (some ⟨v, path[x]!, dx⟩) }
    let s := { s with alive := s.alive.set! x false }
    if E.owner[x]! == 1 then { s with fault := s.fault || tau[x]!.isNone, tau := s.tau.set! x tau[x]! } else s) s

/-- One candidate cycle node v of si.py's outer loop (si.py l. 94-200): (i) cycle test, (ii) R, (iii) restricted graph and
path sets, (iv) lengths, (v) the cycle node's own choice (a second DFS, as si.py l. 184-191, and the walk; computed for every
v, but its choice and flags are used only when v is Odd's, as si.py l. 182), (vi). -/
def procNode (E : Eng) (gs gp : Array (List ℕ)) (s : ES) (v : ℕ) : ES :=
  let n := E.n
  if !s.alive[v]! then s else
  -- (i) «v is a cycle node iff DFS from v over Gσ-successors, visiting only alive vertices of rank < rank(v), returns to v»
  let C := dfs n gs v (some v) (fun y => s.alive[y]! && E.rank[y]! < E.rank[v]!)
  if C.1.hit.isNone then { s with fuelOut := s.fuelOut || C.2 } else
  -- (ii) «R = alive vertices that reach v in Gσ»
  let R := dfs n gp v none (fun y => s.alive[y]!)
  let Rl := R.1.marked
  -- (iii) «Restricted graph on R; path[x] = ∅»
  let hs0 : Array (List ℕ) := Rl.foldl (fun a x => a.set! x ((gs[x]!).filter fun y => R.1.seen[y]!)) (Array.replicate n [])
  let hp0 : Array (List ℕ) := Rl.foldl (fun a x => a.set! x ((gp[x]!).filter fun y => R.1.seen[y]!)) (Array.replicate n [])
  let us := (Rl.filter fun x => E.rank[x]! > E.rank[v]!).mergeSort (fun a b => E.rank[a]! ≥ E.rank[b]!)
  let P := us.foldl (phaseU E n v Rl) (hs0, hp0, Array.replicate n 0, false)
  -- (iv)
  let Ln := lengths E n v Rl P.1 P.2.1
  -- (v)
  let isOdd := E.owner[v]! == 1
  let D := dfs n gs v (some v) (fun y => s.alive[y]! && E.rank[y]! < E.rank[v]!)
  let Wk : Option (ℕ × Bool) := match D.1.hit with
    | some cy => some (walk n v D.1.parent cy)
    | none => none
  let tau := if isOdd then
      match Wk with
      | some w => Ln.2.1.set! v (some w.1)
      | none => Ln.2.1
    else Ln.2.1
  let fo := s.fuelOut || C.2 || R.2 || P.2.2.2 || Ln.2.2.1 || (isOdd && (D.2 || (Wk.map (·.2)).getD false))
  let fa := s.fault || Ln.2.2.2 || (isOdd && Wk.isNone)
  -- (vi)
  assign E v Rl P.2.2.1 Ln.1 tau { s with fuelOut := fo, fault := fa }

/-- The result of one evaluation: `val v` = Ξ(v) (SPEC S1 «valuation of every vertex under σ and Odd's OPTIMAL
counterstrategy σ̄»), `tau v` = σ̄(v) at Odd's vertices (`none` at Even's), `fuelOut`, `fault` (see the header). -/
structure EvalOut where
  val : Array (Option SVal)
  tau : Array (Option ℕ)
  fuelOut : Bool
  fault : Bool
  deriving Inhabited

/-- SPEC S1, «σ̄ is computed by Vöge-Jurdziński's procedure exactly as si.py Engine.evaluate (lines 78-205)», steps
(i)-(vi) with FIX 2 / Q2 and FIX 4 (si.py l. 78-203).  `strat v` is used at Even's vertices only.  A vertex left without
a valuation is a `fault` (si.py's `improving` would fail on it). -/
def Eng.evaluate (E : Eng) (strat : Array ℕ) : EvalOut :=
  let n := E.n
  -- «graph Gσ = Even vertices keep only σ(v), Odd vertices keep all edges» (si.py l. 86-90)
  let gs : Array (List ℕ) := (Array.range n).map fun v => if E.owner[v]! == 0 then [strat[v]!] else E.succ[v]!
  let gp : Array (List ℕ) := (List.range n).foldl (fun a v => (gs[v]!).foldl (fun a w => a.modify w (· ++ [v])) a)
    (Array.replicate n [])
  -- «For v in V in increasing order of reward(v) …, skipping dead v» (si.py l. 94-96)
  let s := E.order.foldl (procNode E gs gp)
    ⟨Array.replicate n true, Array.replicate n none, Array.replicate n none, false, false⟩
  ⟨s.val, s.tau, s.fuelOut, s.fault || s.val.any (·.isNone)⟩

/-- The valuation of `w` (`default` where the procedure gave none; then `fault` is set). -/
def EvalOut.valOf (o : EvalOut) (w : ℕ) : SVal := o.val[w]!.getD default

/-! ## S2: improving edges -/

/-- SPEC S2 «Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v), Ξσ(w) strictly better than Ξσ(σ(v))}» (si.py `improving`,
si.py l. 220-228); in increasing (v, w). -/
def Eng.improving (E : Eng) (strat : Array ℕ) (o : EvalOut) : List (ℕ × ℕ) :=
  (List.range E.n).flatMap fun v =>
    if E.owner[v]! == 0 then
      (E.succ[v]!).filterMap fun w =>
        if w != strat[v]! && keyLt (E.key (o.valOf strat[v]!)) (E.key (o.valOf w)) then some (v, w) else none
    else []

/-! ## S3: the best-reward start -/

/-- FIX 1 / si.py `initial("best")` (si.py l. 236-240): Even's v takes the successor maximising (r(w), w if r(w) even else
−w), r(w) = Ω(w) if even else −Ω(w).  Entries at Odd's vertices: 0 (si.py: −1; never read). -/
def Eng.initialBest (E : Eng) : Array ℕ :=
  (Array.range E.n).map fun v =>
    if E.owner[v]! == 1 then 0 else
      let k : ℕ → ℤ × ℤ := fun w =>
        if E.prio[w]! % 2 == 0 then (((E.prio[w]! : ℕ) : ℤ), (w : ℤ)) else (-((E.prio[w]! : ℕ) : ℤ), -(w : ℤ))
      (E.succ[v]!).foldl (fun b w => if (k b).1 < (k w).1 || ((k b).1 == (k w).1 && (k b).2 < (k w).2) then w else b)
        (E.succ[v]!.headD 0)

/-! ## S4: one iteration -/

/-- One iteration's outputs, as n5x.py `step` (n5x.py l. 15-45): the new pair, Iσ, Iτ, the fallback flag, and the flags. -/
structure StepOut where
  sigma : Array ℕ
  tau : Array ℕ
  Is : List (ℕ × ℕ)
  It : List (ℕ × ℕ)
  fb : Bool
  fuelOut : Bool
  fault : Bool
  deriving Inhabited

/-- SPEC S4a «A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ}» for Even v, sorted (n5x.py l. 23-25, `sorted(opt[v])`). -/
def improvSet (owner : Array ℕ) (who : ℕ) (cur : Array ℕ) (I : List (ℕ × ℕ)) (v : ℕ) : List ℕ :=
  if owner[v]! == who then ((cur[v]! :: (I.filterMap fun p => if p.1 == v then some p.2 else none)).dedup).mergeSort
    (fun a b => a ≤ b)
  else []

/-- SPEC S4a's arena H: «Even v keeps only edges to A(v); Odd v keeps only the edge to τ(v)» (n5x.py l. 25). -/
def arenaH (g : SGame) (sigma tau : Array ℕ) (Is : List (ℕ × ℕ)) : SGame :=
  ⟨g.n, g.prio, g.owner, (Array.range g.n).map fun v =>
    if g.owner[v]! == 0 then improvSet g.owner 0 sigma Is v else [tau[v]!]⟩

/-- SPEC S4b's arena H': «Odd v keeps only edges to A(v); Even v only the edge to σ(v)» (n5x.py l. 33). -/
def arenaH' (g : SGame) (sigma tau : Array ℕ) (It : List (ℕ × ℕ)) : SGame :=
  ⟨g.n, g.prio, g.owner, (Array.range g.n).map fun v =>
    if g.owner[v]! == 1 then improvSet g.owner 1 tau It v else [sigma[v]!]⟩

/-- SPEC S4a «σ_new = Odd's optimal counterstrategy (S1 procedure) in the dual of H to the dual-Even strategy τ, read as an
Even strategy of G» (n5x.py l. 26-29).  Returns (σ_new, fuelOut, fault). -/
def s4a (g : SGame) (sigma tau : Array ℕ) (Is : List (ℕ × ℕ)) : Array ℕ × Bool × Bool :=
  let o := (Eng.ofGame (arenaH g sigma tau Is).dual).evaluate tau
  ((Array.range g.n).map fun v => if g.owner[v]! == 0 then o.tau[v]!.getD sigma[v]! else sigma[v]!,
   o.fuelOut, o.fault || (List.range g.n).any fun v => g.owner[v]! == 0 && o.tau[v]!.isNone)

/-- SPEC S4b «τ_new = Odd's optimal counterstrategy (S1 procedure on H', not dual) to σ» (n5x.py l. 34-37). -/
def s4b (g : SGame) (sigma tau : Array ℕ) (It : List (ℕ × ℕ)) : Array ℕ × Bool × Bool :=
  let o := (Eng.ofGame (arenaH' g sigma tau It)).evaluate sigma
  ((Array.range g.n).map fun v => if g.owner[v]! == 1 then o.tau[v]!.getD tau[v]! else tau[v]!,
   o.fuelOut, o.fault || (List.range g.n).any fun v => g.owner[v]! == 1 && o.tau[v]!.isNone)

/-- S4a's part of the step: σ itself (no flags) if Iσ = ∅ (n5x.py l. 22). -/
def stepA (g : SGame) (sigma tau : Array ℕ) (Is : List (ℕ × ℕ)) : Array ℕ × Bool × Bool :=
  if Is.isEmpty then (sigma, false, false) else s4a g sigma tau Is

/-- S4b's part of the step: τ itself if Iτ = ∅ (n5x.py l. 30). -/
def stepB (g : SGame) (sigma tau : Array ℕ) (It : List (ℕ × ℕ)) : Array ℕ × Bool × Bool :=
  if It.isEmpty then (tau, false, false) else s4b g sigma tau It

/-- SPEC S4c / FIX 3 / A7: «for every Even v with an improving edge set σ_new(v) = the w with (v, w) ∈ Iσ maximising
(Ξσ(w), w) (best valuation, ties: larger index)» (n5x.py l. 42); the same for Odd with G^d's valuations (n5x.py l. 44). -/
def fallbackAt (E : Eng) (o : EvalOut) (I : List (ℕ × ℕ)) (cur : Array ℕ) : Array ℕ :=
  (Array.range cur.size).map fun v =>
    match I.filterMap (fun p => if p.1 == v then some p.2 else none) with
    | [] => cur[v]!
    | w0 :: rest =>
      rest.foldl (fun b w =>
        if keyLt (E.key (o.valOf b)) (E.key (o.valOf w)) || (E.key (o.valOf b) == E.key (o.valOf w) && b < w) then w
        else b) w0

/-- SPEC S4 «one iteration = one pass with Iσ ∪ Iτ ≠ ∅; both steps computed from the SAME (σ, τ), applied together»;
`none` = SPEC S5 «Stop when Iσ = Iτ = ∅» (n5x.py `step`, n5x.py l. 15-45). -/
def specStep (g : SGame) (E Ed : Eng) (sigma tau : Array ℕ) : Option StepOut :=
  let ov := E.evaluate sigma
  let Is := E.improving sigma ov
  let od := Ed.evaluate tau
  let It := Ed.improving tau od
  if Is.isEmpty && It.isEmpty then none else
  let A := stepA g sigma tau Is
  let B := stepB g sigma tau It
  let fo := ov.fuelOut || od.fuelOut || A.2.1 || B.2.1
  let fa := ov.fault || od.fault || A.2.2 || B.2.2
  if A.1 == sigma && B.1 == tau then
    if !Is.isEmpty then some ⟨fallbackAt E ov Is sigma, tau, Is, It, true, fo, fa⟩
    else some ⟨sigma, fallbackAt Ed od It tau, Is, It, true, fo, fa⟩
  else some ⟨A.1, B.1, Is, It, false, fo, fa⟩

/-- n5x.py `start_pair` (n5x.py l. 47-59): the best-reward start of S3 for both players (Odd's on G^d), overwritten by a
given start pair (lists of (v, w)). -/
def startPair (E Ed : Eng) (start : Option (List (ℕ × ℕ) × List (ℕ × ℕ))) : Array ℕ × Array ℕ :=
  let s0 := E.initialBest
  let t0 := Ed.initialBest
  match start with
  | none => (s0, t0)
  | some (ss, ts) => (ss.foldl (fun a p => a.set! p.1 p.2) s0, ts.foldl (fun a p => a.set! p.1 p.2) t0)

/-- The iterations from (σ, τ), at most `cap` of them; the Bool = S5's stop was reached (n5x.py `trace`: «while
len(states) - 1 < cap»: no step is computed once `cap` iterations are done, D11). -/
def specIter (g : SGame) (E Ed : Eng) : ℕ → Array ℕ → Array ℕ → List StepOut × Bool
  | 0, _, _ => ([], false)
  | cap + 1, sigma, tau =>
    match specStep g E Ed sigma tau with
    | none => ([], true)
    | some r => ((r :: (specIter g E Ed cap r.sigma r.tau).1), (specIter g E Ed cap r.sigma r.tau).2)

/-- A run of N5 (n5x.py `trace`, n5v.py `run(g, "spec")`): the states (σ_0, τ_0), (σ_1, τ_1), …, the step records, and
whether S5 stopped it within `cap` iterations. -/
structure RunOut where
  states : List (Array ℕ × Array ℕ)
  steps : List StepOut
  stopped : Bool
  deriving Inhabited

/-- SPEC S1-S5 on `g` from the start of S3 (or the given start pair), at most `cap` iterations. -/
def specRun (g : SGame) (start : Option (List (ℕ × ℕ) × List (ℕ × ℕ))) (cap : ℕ) : RunOut :=
  let E := Eng.ofGame g
  let Ed := Eng.ofGame g.dual
  let p := startPair E Ed start
  let it := specIter g E Ed cap p.1 p.2
  ⟨p :: it.1.map (fun r => (r.sigma, r.tau)), it.1, it.2⟩

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
(R24 (a)), i.e. extend(x, Ξ(w)) = Ξ(x) (n5v.py l. 35 `Er.extend(v, vh[w]) == vh[v]`). -/
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
(D2) Fuel: si.py's `while` loops are `loopFuel` loops of n + 1 rounds, and the recursion of `longest` has depth n + 1;
     reaching a bound sets `fuelOut` (the parent walk of FIX 2 included: its silent fuel spot in the text of 0ee5b8bc was
     found by L-FORMAL 4 and recorded by the Lead 03:46Z).  `fault` is set where si.py raises
     (`RuntimeError("cycle in restricted graph")`, a KeyError on a missing length or choice, a missing DFS cycle at a cycle
     node, a vertex without a valuation) or stores None as an Odd vertex's choice (si.py carries the None on; here the old
     choice is kept).  On every run of the check tool both flags are 0.  (`longest` tests the fuel before the x = v and
     memo tests: a call at v with fuel 0 sets `fuelOut`; noted for the diff, Lead 03:46Z (3).)
(D3) si.py iterates over Python SETS (R, M, `{v for v, _ in Is}`) where the order cannot change the result (the memoised
     lengths, the commutative path / restrict updates, independent fallback assignments); here lists in a fixed order.
(D4) si.py's `par[x] is not v` (si.py l. 193, object identity) is read as value equality.  Lead 02:06Z asked whether this
     is a defect of the reference for n > 256 (CPython caches only the ints −5..256).  ANSWER: NO DEFECT, by construction.
     `par = {v: None}; st = [v]` (si.py l. 184) puts the loop object v on the stack; every value stored by `par[y] = x`
     (si.py l. 191) is an object popped from the stack; a successor y equal to v is never pushed (si.py l. 188-189 test
     `y == v` first and break), so the only stack object equal to v is v itself, and `par[x] is not v` ⟺ `par[x] != v` for
     non-None values.  PROBE (check/d4probe.py, a line tracer on si.py's own code path, si.py unmodified; output
     check/out/d4probe.out): on box113 w_re3_1, box72 latew_K20_m32 (n = 538), box97 obs_K12_m24 (n = 272), box189
     REC_d12_mu42_norm (Γ3, n = 370), 200 iterations or to the stop, 612 executions of si.py l. 193, eq_not_id 0 (no value
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
     for every call of the procedure; SPEC defines the choice by the procedure only.  A PREDICATE checked on the
     procedure (Lead 02:06Z (3)); no other definition references it.
(D9) Counting: SPEC's «one iteration = one pass with Iσ ∪ Iτ ≠ ∅» = the length of `steps`; `cap` bounds it.
(D10) No input validation (Lead 03:58Z U1): si.py rejects empty successor lists and owners other than 0 / 1; this text
     accepts every `SGame` and computes something (instance: Ω = [0, 1], owner = [0, 1], succ = [[], [1]]: initialBest
     gives σ(0) = 0, not an edge; an owner 2 is read inconsistently and `dual` maps it to 0).  Every theorem about the
     procedure takes `SGame.WF`.
(D11) The cap (Lead 03:58Z U2): the text of 0ee5b8bc computed one extra `specStep` at the cap and could report
     `stopped = true` where n5x.py's `trace` («while len(states) - 1 < cap») makes no call (n5.py reports capped = 1);
     the states were identical.  This text follows n5x.py: `specIter` makes no call once `cap` iterations are done.
-/

end PG.Spec
