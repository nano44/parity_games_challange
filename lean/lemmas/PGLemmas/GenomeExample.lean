/-
A genome with a step: `Genome.tiny` (one mover of level 0 with two options) satisfies `WF`, and
IDEAL-CYC(tiny) has a run of length 1 from the genome's start (`tiny_run`).  So the hypotheses of
the statements about `Genome.IdealCycRun` are satisfiable with T ≥ 1.  No premise.

How the step arises.  At every state Odd is at the Ξ-face of each gate: the W-face leads to c_W
(cycle node c_W, even, the largest reward), the Ξ-face β leads through u = K0 into the core (cycle
node K1, odd), and LOC-GATE (`OptCounter.le_succ`) picks the smaller.  So the value of the gate of
option k is (K1, {β_k} ∪ Π(K0), ·), and the two gates differ exactly by their β: β_1 is more
relevant than β_0 and even, so the gate of option 1 is strictly better than the start's gate.

* `setLt_insert_of_lt`, `ext_ext_lt`   the comparison of two such values, for any game.
* `core_closed`, `core_iterate`        the core is closed under every state.
* `tiny`, `tiny_wf`, `tiny_better`, `tiny_run`.
-/
import PGLemmas.GenomeRun

namespace PG

open Classical
open scoped symmDiff

noncomputable section

section Generic

variable {V : Type*} {pr : V → ℕ}

/-- Two sets that differ by one vertex each: the one with the more relevant vertex, if that
vertex is even, is the larger. -/
theorem setLt_insert_of_lt {X : Finset V} {b0 b1 : V} (h1 : b1 ∉ X)
    (hlt : pr b0 < pr b1) (hev : Even (pr b1)) : setLt pr (insert b0 X) (insert b1 X) := by
  have hne : b1 ≠ b0 := fun e => by
    rw [e] at hlt
    exact lt_irrefl _ hlt
  refine ⟨b1, ?_, ?_, Or.inl ⟨Finset.mem_insert_self _ _, hev⟩⟩
  · rw [Finset.mem_symmDiff]
    refine Or.inr ⟨Finset.mem_insert_self _ _, fun hm => ?_⟩
    rcases Finset.mem_insert.mp hm with e | e
    · exact hne e
    · exact h1 e
  · intro x hx
    rw [Finset.mem_symmDiff] at hx
    rcases hx with ⟨hx0, hx1⟩ | ⟨hx1, hx0⟩
    · rcases Finset.mem_insert.mp hx0 with e | e
      · rw [e]
        exact hlt.le
      · exact absurd (Finset.mem_insert_of_mem e) hx1
    · rcases Finset.mem_insert.mp hx1 with e | e
      · rw [e]
      · exact absurd (Finset.mem_insert_of_mem e) hx0

/-- Two plays that share everything but one vertex `b0` / `b1` more relevant than the cycle node,
each entered from a vertex less relevant than the cycle node. -/
theorem ext_ext_lt {x : Val V} {g0 g1 b0 b1 : V} (hg0 : ¬ pr x.top < pr g0)
    (hg1 : ¬ pr x.top < pr g1) (hb0 : pr x.top < pr b0) (hb1 : pr x.top < pr b1)
    (h1 : b1 ∉ x.set) (hlt : pr b0 < pr b1) (hev : Even (pr b1)) :
    Val.lt pr (ext pr g0 (ext pr b0 x)) (ext pr g1 (ext pr b1 x)) := by
  have s0 : (ext pr g0 (ext pr b0 x)).set = insert b0 x.set := by
    unfold ext
    simp only [hg0, hb0, ↓reduceIte]
  have s1 : (ext pr g1 (ext pr b1 x)).set = insert b1 x.set := by
    unfold ext
    simp only [hg1, hb1, ↓reduceIte]
  refine Or.inr (Or.inl ⟨rfl, ?_⟩)
  rw [s0, s1]
  exact setLt_insert_of_lt h1 hlt hev

end Generic

namespace Genome

section Core

variable {G : Genome} {s : G.Vertex → G.Vertex}

/-- The core is closed under every state. -/
theorem core_closed (hs : G.IsState s) (hk : s Vertex.K2 = Vertex.K1) {v : G.Vertex}
    (hv : G.isCore v = true) : G.isCore (s v) = true := by
  rcases v with x | o | o | o | _ | _ | _ | _ | _ | _ <;> simp [isCore] at hv
  · rw [hs.K0]
    rfl
  · rw [hs.K1]
    rfl
  · rw [hk]
    rfl
  · rw [hs.K3]
    rfl

theorem core_iterate (hs : G.IsState s) (hk : s Vertex.K2 = Vertex.K1) {v : G.Vertex}
    (hv : G.isCore v = true) (n : ℕ) : G.isCore (s^[n] v) = true := by
  induction n with
  | zero => exact hv
  | succ n ih =>
    rw [Function.iterate_succ_apply']
    exact core_closed hs hk ih

end Core

/-- The genome with one mover of level 0 and two options, both with Ξ-target X; the β of option k
has rank k and parity 0, the gate of option k has index k; the start is option 0. -/
def tiny : Genome where
  N := 1
  lev := fun _ => 0
  deg := fun _ => 2
  wt := fun _ => none
  xt := fun _ => none
  gate := fun o => o.2.val
  brank := fun o => o.2.val
  bpar := fun _ => 0
  start := fun _ => ⟨0, by decide⟩

/-- The option `k` of the mover of `tiny`. -/
def tinyOpt (k : Fin 2) : tiny.Opt := ⟨⟨0, Nat.one_pos⟩, k⟩

theorem tiny_M : tiny.M = 2 := by
  rw [M_eq]
  rfl

theorem tiny_inj : Function.Injective (fun o : tiny.Opt => (o.2 : ℕ)) := by
  rintro ⟨x, k⟩ ⟨x', k'⟩ e
  have h1 : (x : ℕ) < 1 := x.isLt
  have h2 : (x' : ℕ) < 1 := x'.isLt
  have hx : x = x' := Fin.ext (by omega)
  subst hx
  have hk : k = k' := Fin.ext e
  rw [hk]

theorem tiny_wf : tiny.WF where
  one_le_N := le_refl 1
  graded0 := fun _ _ => rfl
  graded := fun _ hl => absurd hl (lt_irrefl 0)
  gate_inj := tiny_inj
  gate_lt := fun o => by
    rw [tiny_M]
    exact o.2.isLt
  brank_inj := tiny_inj
  brank_lt := fun o => by
    rw [tiny_M]
    exact o.2.isLt
  bpar_le := fun _ => Nat.zero_le 1

/-- At a state of IDEAL-CYC(tiny) with K2 → K1 and LOC-GATE at every gate, the gate of option 1
has a strictly larger value than the gate of option 0. -/
theorem tiny_better {s : tiny.Vertex → tiny.Vertex} (hs : tiny.IsState s)
    (hk : s Vertex.K2 = Vertex.K1)
    (hloc : ∀ o, Val.le tiny.pr (val tiny.pr s (s (Vertex.gate o))) (val tiny.pr s (Vertex.beta o))) :
    Val.lt tiny.pr (val tiny.pr s (Vertex.gate (tinyOpt 0)))
      (val tiny.pr s (Vertex.gate (tinyOpt 1))) := by
  have h := tiny_wf
  have hpr := pr_injective h
  have hβ : ∀ o, s (Vertex.beta o) = Vertex.K0 := fun o => by
    rw [hs.beta o]
    rfl
  have hlβ : ∀ o, lam tiny.pr s (Vertex.beta o) = Vertex.K1 := fun o => by
    have e := lam_succ (s := s) hpr (Vertex.beta o)
    rw [hβ o, lam_K0 h hs hk] at e
    exact e.symm
  -- Odd is at the Ξ-face of every gate
  have hA : ∀ o, s (Vertex.gate o) = Vertex.beta o := by
    intro o
    rcases hs.gate o with e | e
    · exfalso
      have hle := Val.rew_top_le (hloc o)
      rw [e] at hle
      have h1 : rew tiny.pr (lam tiny.pr s (Vertex.eface o)) ≤
          rew tiny.pr (lam tiny.pr s (Vertex.beta o)) := hle
      have hcW : lam tiny.pr s (Vertex.eface o) = Vertex.cW :=
        congrArg Prod.fst (cls_eface_none h hs (o := o) rfl)
      rw [hcW, hlβ o] at h1
      have hev : Even (tiny.pr Vertex.cW) := even_pr.mpr (Nat.even_iff.mpr top_even)
      have hodd : ¬ Even (tiny.pr Vertex.K1) := fun he => by
        have h5 : Even 5 := even_pr.mp he
        exact absurd h5 (by decide)
      rw [rew_of_even hev, rew_of_odd hodd] at h1
      have hpos : tiny.pr Vertex.K1 ≠ 0 := fun e0 => hodd (by rw [e0]; exact ⟨0, rfl⟩)
      omega
    · exact e
  have hneβ : ∀ o, lam tiny.pr s (Vertex.beta o) ≠ Vertex.beta o := fun o => by
    rw [hlβ o]
    exact fun e => by cases e
  have e1 : ∀ o, val tiny.pr s (Vertex.beta o) =
      ext tiny.pr (Vertex.beta o) (val tiny.pr s Vertex.K0) := fun o => by
    rw [val_step hpr (hneβ o), hβ o]
  have e2 : ∀ o, val tiny.pr s (Vertex.gate o) =
      ext tiny.pr (Vertex.gate o) (val tiny.pr s (Vertex.beta o)) := fun o => by
    rw [val_step hpr (lam_ne_gate h hs _ o), hA o]
  have htop : (val tiny.pr s Vertex.K0).top = Vertex.K1 := lam_K0 h hs hk
  have hnotin : ∀ o, Vertex.beta o ∉ (val tiny.pr s Vertex.K0).set := by
    intro o hm
    have hm' : Vertex.beta o ∈ pset tiny.pr s Vertex.K0 := hm
    obtain ⟨-, j, -, hj⟩ := mem_pset.mp hm'
    have hc := core_iterate hs hk (v := Vertex.K0) rfl j
    rw [hj] at hc
    simp [isCore] at hc
  rw [e2, e2, e1, e1]
  apply ext_ext_lt
  · rw [htop]
    exact not_lt.mpr (pr_lt_of_prio_lt h (by decide)).le
  · rw [htop]
    exact not_lt.mpr (pr_lt_of_prio_lt h (by decide)).le
  · rw [htop]
    exact pr_lt_of_prio_lt h (by decide)
  · rw [htop]
    exact pr_lt_of_prio_lt h (by decide)
  · exact hnotin _
  · exact pr_lt_of_prio_lt h (by decide)
  · exact even_pr.mpr (by decide)

/-- **IDEAL-CYC(tiny) has a run of length 1 from the genome's start.** -/
theorem tiny_run : ∃ σ τ : ℕ → tiny.Vertex → tiny.Vertex,
    tiny.IdealCycRun σ τ 1 ∧ tiny.FromStart σ := by
  have h := tiny_wf
  have hpr := pr_injective h
  have hne : ∀ σ, ∃ τ, OptCounter tiny.pr tiny.E tiny.V0 σ τ := fun σ =>
    optCounter_exists tiny.pr hpr tiny.E tiny.V0 σ (fun u _ => E_nonempty u)
  refine ⟨_, _, run_prefix h hne 1 (fun t ht hst => ?_)⟩
  obtain rfl : t = 0 := by omega
  have R0 := (run_prefix h hne 0 (fun t ht => absurd ht (Nat.not_lt_zero t))).1
  have hs := R0.isState (le_refl 0)
  have hbetter := tiny_better hs (R0.k2 h (le_refl 0)) (fun o =>
    OptCounter.le_succ hpr (R0.opt 0 (le_refl 0)) (gate_notMem_V0 o)
      (mem_E_gate.mpr (Or.inr rfl)) (lam_ne_gate h hs _ o))
  exact hst ⟨0, Nat.one_pos⟩ (Vertex.gate (tinyOpt 1)) (mem_E_mover.mpr ⟨(1 : Fin 2), rfl⟩) hbetter

end Genome

end

end PG
