/-
MANIFEST tool (L-FORMAL): reads the compiled environment of `PGLemmas` and prints, for every theorem
named in Axioms.lean, its module, line, the head constant of its type (the Statement, if any), and the
PG definitions that type depends on (transitively), grouped by module.  Run from lean/lemmas:
  lake env lean check/manifest.lean
-/
import PGLemmas
open Lean Meta

/-- the names in Axioms.lean, in order -/
def manifestNames : IO (Array Name) := do
  let s ← IO.FS.readFile "Axioms.lean"
  let mut out := #[]
  for l in s.splitOn "\n" do
    if l.startsWith "#print axioms " then
      let n := String.ofList ((l.toList.drop "#print axioms ".length).filter (fun c => !c.isWhitespace))
      out := out.push n.toName
  return out

def isPG (n : Name) : Bool := (`PG).isPrefixOf n

/-- PG constants used (transitively through PG definitions, not through theorems) by `n`'s type
and, for a definition, its value. -/
partial def pgDeps (env : Environment) (root : Array Name) : NameSet := Id.run do
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
          if isPG m && !seen.contains m then todo := m :: todo
      | none => pure ()
  return seen

def modOf (env : Environment) (n : Name) : String :=
  match env.getModuleIdxFor? n with
  | some i => toString (env.header.moduleNames[i.toNat]!)
  | none => "?"

#eval show MetaM Unit from do
  let env ← getEnv
  let names ← manifestNames
  let mut statementRoots : Array Name := #[]
  IO.println s!"THEOREMS {names.size}"
  for n in names do
    let some ci := env.find? n | IO.println s!"MISSING {n}"
    let line ← match (← findDeclarationRanges? n) with
      | some r => pure (toString r.selectionRange.pos.line)
      | none => pure "?"
    let headName ← forallTelescope ci.type fun _ b => pure (match b.getAppFn with
      | .const h _ => toString h
      | _ => "(other)")
    statementRoots := statementRoots.push n
    let own := pgDeps env (ci.type.getUsedConstants.filter isPG)
    let mods := (own.toList.filterMap fun d => match env.find? d with
      | some (.thmInfo _) => none
      | some _ => some (modOf env d)
      | none => none).eraseDups
    let mods := (mods.toArray.qsort (· < ·)).toList
    IO.println s!"THM {n} | {modOf env n} | line {line} | type head {headName} | defmods {mods}"
  -- definitions every offered theorem's TYPE depends on
  let typeRoots := names.foldl (fun acc n => match env.find? n with
    | some ci => acc ++ ci.type.getUsedConstants.filter isPG
    | none => acc) #[]
  let deps := pgDeps env typeRoots
  let mut byMod : Std.HashMap String (Array Name) := {}
  for d in deps.toList do
    match env.find? d with
    | some (.thmInfo _) => pure ()
    | some _ =>
      let m := modOf env d
      byMod := byMod.insert m ((byMod.getD m #[]).push d)
    | none => pure ()
  IO.println s!"DEFINITION MODULES {byMod.size}"
  for (m, ds) in byMod.toList.toArray.qsort (fun a b => a.1 < b.1) do
    IO.println s!"MOD {m} | {ds.size} | {(ds.qsort (fun a b => toString a < toString b)).toList}"
