/-
Further statements (proposed to the Lead after the first five; same convention: each
`…Statement` is the exact type of the theorem proving it).

* `TwoCrossStatement`   claude/l-si docs/si/box100-scclin.md §2, Lemma TWO-CROSS, from its three
                        premises (F1, NO-TIE, LOC-GATE) over any preorder of values.
* `LamCountStatement`   the Λ part of DEPTH-COUNT3 (box 100 §3) = the per-vertex count behind
                        RESULTS R118 (i)(b) «C ≤ n(n − 1)»: a ⊴-non-decreasing sequence of node
                        valuations changes its cycle node at most n − 1 times.
* `HowardRunStatement`  Corollary L1-POLY (box 101 §3) in abstract form: a Howard run on which
                        only `Ch` moves makes at most n(n−1) + (n(n−1) + 1)·|Ch| steps, given (M).
-/
import PGLemmas.Defs

namespace PG

open Classical

noncomputable section

/-- Lemma TWO-CROSS (box 100 §2).  A gate with faces `a`, `b`; `face t` is the face taken at state
`t ≤ T`; `Ω t x` the value of face `x` at state `t`, in any preorder.
(i) a flip away from a face strictly raises that face's value at the same step;
(ii) `flips ≤ ch(a) + ch(b)` and `flips ≤ 2·min(ch(a), ch(b)) + 1`, where `ch(x)` counts the
steps at which the value of face `x` changes. -/
def TwoCrossStatement (α : Type*) [Preorder α] (F : Type*) : Prop :=
  ∀ (a b : F) (T : ℕ) (face : ℕ → F) (Ω : ℕ → F → α),
    -- the gate takes one of its two faces
    (∀ t, t ≤ T → face t = a ∨ face t = b) →
    -- F1 at both faces: `Ω_t ⊴ Ω_(t+1)`
    (∀ t, t < T → Ω t a ≤ Ω (t + 1) a ∧ Ω t b ≤ Ω (t + 1) b) →
    -- NO-TIE
    (∀ t, t ≤ T → Ω t a ≠ Ω t b) →
    -- LOC-GATE: the face taken has the smaller value, if the values differ
    (∀ t, t ≤ T → (face t = a → Ω t a ≠ Ω t b → Ω t a < Ω t b) ∧
                  (face t = b → Ω t b ≠ Ω t a → Ω t b < Ω t a)) →
    -- (i)
    (∀ t, t < T → (face t = a → face (t + 1) = b → Ω t a < Ω (t + 1) a) ∧
                  (face t = b → face (t + 1) = a → Ω t b < Ω (t + 1) b)) ∧
    -- (ii)
    (let flips := ((Finset.range T).filter (fun t => face (t + 1) ≠ face t)).card
     let chA := ((Finset.range T).filter (fun t => Ω t a ≠ Ω (t + 1) a)).card
     let chB := ((Finset.range T).filter (fun t => Ω t b ≠ Ω (t + 1) b)).card
     flips ≤ chA + chB ∧ flips ≤ 2 * min chA chB + 1)

/-- A sequence of node valuations that never falls (`x t ⊴ x (t+1)` for `t < T`) changes its
cycle component at most `n − 1` times, `n` the number of vertices.  (Box 100 §3: «Λ(v) changes at
most n3 − 1 times»; stated as `changes + 1 ≤ n`.) -/
def LamCountStatement (V : Type*) [Fintype V] : Prop :=
  ∀ (pr : V → ℕ), Function.Injective pr → ∀ (x : ℕ → Val V) (T : ℕ),
    (∀ t, t < T → Val.le pr (x t) (x (t + 1))) →
    ((Finset.range T).filter (fun t => (x t).top ≠ (x (t + 1)).top)).card + 1 ≤ Fintype.card V

/-- A Howard run `s 0, …, s T` on which only the vertices of `Ch` move (one-player: every other
vertex has one successor or is frozen), with premise (M) at every step and every step changing
the state, has `T ≤ n(n − 1) + (n(n − 1) + 1)·|Ch|` steps, `n` the number of vertices.
(Box 101 §3 Corollary L1-POLY, with SHARP's window length `|Ch|`.) -/
def HowardRunStatement (V : Type*) [Fintype V] : Prop :=
  ∀ (pr : V → ℕ), Function.Injective pr →
  ∀ (E : V → Finset V) (Ch : Finset V) (s : ℕ → V → V) (T : ℕ),
    -- only `Ch` moves
    (∀ t, t ≤ T → ∀ v, v ∉ Ch → s t v = s 0 v) →
    -- Howard steps at `Ch`
    (∀ t, t < T → ∀ v ∈ Ch, HowardAt pr E (s t) (s (t + 1)) v) →
    -- premise (M)
    (∀ t, t < T → ∀ v, Val.le pr (val pr (s t) v) (val pr (s (t + 1)) v)) →
    -- every step changes the state (the run has not stopped before `T`)
    (∀ t, t < T → s (t + 1) ≠ s t) →
    T ≤ Fintype.card V * (Fintype.card V - 1) +
      (Fintype.card V * (Fintype.card V - 1) + 1) * Ch.card

end

end PG
