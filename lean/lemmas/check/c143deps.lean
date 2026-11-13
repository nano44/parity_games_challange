/-
C143 notes tool (L-FORMAL): for every theorem named in Axioms.lean, does its TYPE depend (transitively through
PG definition bodies, not through theorems; the same closure as check/manifest.lean) on
  `PG.OptCounter` (C143 note N-1: «OptCounter = VJ00 Ω_σ is a paper step»),
  `PG.Genome.IdealCycRun` (note N-2: «A run is any IdealCycRun»),
  `PG.Genome.pr` (note N-7: «The pr tie-break»)?
Run from lean/lemmas:  lake env lean check/c143deps.lean
Output lines: DEP <theorem> | OptCounter <bool> | IdealCycRun <bool> | pr <bool>
-/
import PGLemmas
open Lean Meta

def namesOfAxioms : IO (Array Name) := do
  let s ← IO.FS.readFile "Axioms.lean"
  let mut out := #[]
  for l in s.splitOn "\n" do
    if l.startsWith "#print axioms " then
      let n := String.ofList ((l.toList.drop "#print axioms ".length).filter (fun c => !c.isWhitespace))
      out := out.push n.toName
  return out

def isPGName (n : Name) : Bool := (`PG).isPrefixOf n

partial def pgClosure (env : Environment) (root : Array Name) : NameSet := Id.run do
  let mut seen : NameSet := {}
  let mut todo := root.toList
  while !todo.isEmpty do
    match todo with
    | [] => pure ()
    | n :: rest =>
      todo := rest
      if seen.contains n then continue
      seen := seen.insert n
      match env.find? n with
      | some ci =>
        let used := match ci with
          | .defnInfo d => d.type.getUsedConstants ++ d.value.getUsedConstants
          | .inductInfo i => i.type.getUsedConstants ++ (i.ctors.toArray)
          | .ctorInfo c => c.type.getUsedConstants
          | _ => ci.type.getUsedConstants
        for m in used do
          if isPGName m && !seen.contains m then todo := m :: todo
      | none => pure ()
  return seen

#eval show MetaM Unit from do
  let env ← getEnv
  for n in (← namesOfAxioms) do
    let some ci := env.find? n | IO.println s!"MISSING {n}"
    let c := pgClosure env (ci.type.getUsedConstants.filter isPGName)
    IO.println s!"DEP {n} | OptCounter {c.contains `PG.OptCounter} | IdealCycRun {c.contains `PG.Genome.IdealCycRun} | pr {c.contains `PG.Genome.pr}"
