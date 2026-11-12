/-
Runs of IDEAL-CYC(G) exist and stop: `run_exists : G.RunExistsStatement`
(`PGLemmas/GenomeRunStatement.lean`).  No premise.

* `exists_best`      a finite non-empty set of vertices has a vertex of ⊴-largest value.
* `howardNext`       Howard's choice at a vertex: the current successor if it is ⊴-best, otherwise a
                     ⊴-best one; `howardNext_spec`: it is a Howard step (`HowardAt`).
* `runSeq`           the sequence of pairs (σ_t, σ̄_t): the genome's start with an optimal
                     counterstrategy (`optCounter_exists`), then Howard's choice at every mover and
                     an optimal counterstrategy against the new σ.
* `run_prefix`       as long as no state has stopped, the sequence is a run (`IdealCycRun`).
* `run_exists`       some state stops: otherwise `run_prefix` gives runs of every length, against
                     `all_tcyc`.
-/
import PGLemmas.GenomeRunStatement
import PGLemmas.GenomeAllTCyc
import PGLemmas.OptExists

namespace PG

open Classical

noncomputable section

section Generic

variable {V : Type*} [Fintype V] {pr : V → ℕ}

omit [Fintype V] in
/-- A finite non-empty set has an element of ⊴-largest value. -/
theorem exists_best (hpr : Function.Injective pr) (f : V → Val V) {S : Finset V}
    (hne : S.Nonempty) : ∃ w ∈ S, ∀ w' ∈ S, Val.le pr (f w') (f w) := by
  induction hne using Finset.Nonempty.cons_induction with
  | singleton a =>
    exact ⟨a, Finset.mem_singleton_self a, fun w' hw' => by
      rw [Finset.mem_singleton.mp hw']
      exact Val.le_refl _⟩
  | cons a S ha hS ih =>
    obtain ⟨b, hb, hbest⟩ := ih
    rcases Val.lt_trichotomy hpr (f a) (f b) with hlt | heq | hgt
    · refine ⟨b, Finset.mem_cons.mpr (Or.inr hb), fun w' hw' => ?_⟩
      rcases Finset.mem_cons.mp hw' with e | hw'
      · rw [e]
        exact Val.le_of_lt hlt
      · exact hbest w' hw'
    · refine ⟨b, Finset.mem_cons.mpr (Or.inr hb), fun w' hw' => ?_⟩
      rcases Finset.mem_cons.mp hw' with e | hw'
      · rw [e]
        exact Or.inr heq
      · exact hbest w' hw'
    · refine ⟨a, Finset.mem_cons_self a S, fun w' hw' => ?_⟩
      rcases Finset.mem_cons.mp hw' with e | hw'
      · rw [e]
        exact Val.le_refl _
      · exact Val.le_trans hpr (hbest w' hw') (Val.le_of_lt hgt)

/-- Howard's choice at `v` under the state `s`: the current successor if it is ⊴-best among the
successors `E v`, otherwise a ⊴-best successor. -/
def howardNext (pr : V → ℕ) (E : V → Finset V) (s : V → V) (v : V) : V :=
  if s v ∈ E v ∧ ∀ w ∈ E v, Val.le pr (val pr s w) (val pr s (s v)) then s v
  else if h : ∃ w ∈ E v, ∀ w' ∈ E v, Val.le pr (val pr s w') (val pr s w) then Classical.choose h
  else s v

/-- Howard's choice is a Howard step. -/
theorem howardNext_spec (hpr : Function.Injective pr) {E : V → Finset V} {s s' : V → V} {v : V}
    (hne : (E v).Nonempty) (hs' : s' v = howardNext pr E s v) : HowardAt pr E s s' v := by
  have hex := exists_best hpr (val pr s) hne
  unfold HowardAt
  rw [hs']
  unfold howardNext
  by_cases hc : s v ∈ E v ∧ ∀ w ∈ E v, Val.le pr (val pr s w) (val pr s (s v))
  · rw [ite_eq_left hc]
    exact ⟨hc.1, hc.2, fun _ => rfl⟩
  · rw [ite_eq_right hc, dite_eq_left hex]
    have hsp := Classical.choose_spec hex
    exact ⟨hsp.1, hsp.2, fun h => absurd h hc⟩

end Generic

namespace Genome

variable {G : Genome}

/-- Every vertex of Γ(G) has a successor. -/
theorem E_nonempty (v : G.Vertex) : (G.E v).Nonempty := ⟨G.start0 v, start0_mem_E v⟩

/-- One step on pairs (σ, σ̄): Howard's choice at every mover, the start elsewhere, and an optimal
counterstrategy against the new σ. -/
def runStep (G : Genome) (hne : ∀ σ, ∃ τ, OptCounter G.pr G.E G.V0 σ τ)
    (st : (G.Vertex → G.Vertex) × (G.Vertex → G.Vertex)) :
    (G.Vertex → G.Vertex) × (G.Vertex → G.Vertex) :=
  (fun v => if ∃ x, v = Vertex.mover x then howardNext G.pr G.E (pair G.V0 st.1 st.2) v
      else G.start0 v,
    Classical.choose (hne (fun v => if ∃ x, v = Vertex.mover x then
      howardNext G.pr G.E (pair G.V0 st.1 st.2) v else G.start0 v)))

/-- The sequence of pairs (σ_t, σ̄_t) from the genome's start. -/
def runSeq (G : Genome) (hne : ∀ σ, ∃ τ, OptCounter G.pr G.E G.V0 σ τ) :
    ℕ → (G.Vertex → G.Vertex) × (G.Vertex → G.Vertex)
  | 0 => (G.start0, Classical.choose (hne G.start0))
  | n + 1 => runStep G hne (runSeq G hne n)

/-- As long as no state has stopped, the sequence is a run of IDEAL-CYC(G) from the start. -/
theorem run_prefix (h : G.WF) (hne : ∀ σ, ∃ τ, OptCounter G.pr G.E G.V0 σ τ) (T : ℕ)
    (hT : ∀ t, t < T →
      ¬ G.Stopped (fun t => (runSeq G hne t).1) (fun t => (runSeq G hne t).2) t) :
    G.IdealCycRun (fun t => (runSeq G hne t).1) (fun t => (runSeq G hne t).2) T ∧
      G.FromStart (fun t => (runSeq G hne t).1) := by
  have hpr := pr_injective h
  have hopt : ∀ t, OptCounter G.pr G.E G.V0 (runSeq G hne t).1 (runSeq G hne t).2 := by
    intro t
    cases t with
    | zero => exact Classical.choose_spec (hne G.start0)
    | succ n => exact Classical.choose_spec (hne _)
  have hfrozen : ∀ t, ∀ v ∈ G.V0, (∀ x, v ≠ Vertex.mover x) →
      (runSeq G hne t).1 v = G.start0 v := by
    intro t v _ hv
    cases t with
    | zero => rfl
    | succ n =>
      show (if ∃ x, v = Vertex.mover x then _ else G.start0 v) = G.start0 v
      rw [ite_eq_right (fun ⟨x, e⟩ => hv x e)]
  have hstep : ∀ t x, (runSeq G hne (t + 1)).1 (Vertex.mover x) =
      howardNext G.pr G.E (pair G.V0 (runSeq G hne t).1 (runSeq G hne t).2) (Vertex.mover x) := by
    intro t x
    show (if ∃ x', Vertex.mover x = Vertex.mover x' then _ else _) = _
    rw [ite_eq_left ⟨x, rfl⟩]
  have hhow : ∀ t x, HowardAt G.pr G.E
      (nxt G.V0 (fun t => (runSeq G hne t).1) (fun t => (runSeq G hne t).2) t)
      (nxt G.V0 (fun t => (runSeq G hne t).1) (fun t => (runSeq G hne t).2) (t + 1))
      (Vertex.mover x) := by
    intro t x
    apply howardNext_spec hpr (E_nonempty _)
    rw [nxt_mover]
    exact hstep t x
  have hlegal : ∀ t x, (runSeq G hne t).1 (Vertex.mover x) ∈ G.E (Vertex.mover x) := by
    intro t x
    cases t with
    | zero => exact start0_mem_E _
    | succ n =>
      have hm := (hhow n x).1
      rw [nxt_mover] at hm
      exact hm
  refine ⟨⟨fun t _ => hfrozen t, fun t _ => hlegal t, fun t _ => hopt t, fun t _ => hhow t,
    fun t ht => ?_⟩, fun _ => rfl⟩
  have hns := hT t ht
  unfold Stopped at hns
  push Not at hns
  exact hns

/-- **Runs exist and stop.** -/
theorem run_exists : G.RunExistsStatement := by
  intro h
  have hpr := pr_injective h
  have hne : ∀ σ, ∃ τ, OptCounter G.pr G.E G.V0 σ τ := fun σ =>
    optCounter_exists G.pr hpr G.E G.V0 σ (fun u _ => E_nonempty u)
  -- some state has stopped: otherwise there are runs of every length
  have hstop : ∃ t, G.Stopped (fun t => (runSeq G hne t).1) (fun t => (runSeq G hne t).2) t := by
    by_contra hno
    have hR := (run_prefix h hne (2 * G.M * (G.N + 2 * G.M) * (G.N + 2 * G.M + 6) + G.N + 1)
      (fun t _ ht => hno ⟨t, ht⟩)).1
    have hb := all_tcyc h _ _ _ hR
    omega
  have hrun := run_prefix h hne (Nat.find hstop) (fun t ht => Nat.find_min hstop ht)
  exact ⟨_, _, Nat.find hstop, hrun.1, hrun.2, Nat.find_spec hstop⟩

end Genome

end

end PG
