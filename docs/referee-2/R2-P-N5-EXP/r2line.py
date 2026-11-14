#!/usr/bin/env python3
"""REFEREE-2 successor 42: line L-6 of P-N5-EXP rebuilt from line L-3 by its nine named replacements (Addendum 5 of R2-P-N5-EXP.md).
Own code. Reads the lines with `git show COMMIT:docs/red-b/P-N5-EXP-line-L<n>.txt` (run from inside the repository).
Per replacement: once = [the old text occurs exactly once in the line it is applied to] (must 1). Then: L-4, L-5, L-6 rebuilt from
L-3 against the files (rebuilt_equals_file must 1 for each); brackets of L-6; the six quotations inside L-6 against their sources
(found must 1 each). Control --ctrl: the replacements applied in L-6's order but with the OLD rank gloss kept: L-6 must NOT be
reproduced (rebuilt_equals_file 0).
Usage: r2line.py COMMIT TRUNK [--ctrl]"""
import sys, subprocess, hashlib, re
norm = lambda t: " ".join(t.split())
def show(spec): return subprocess.run(["git", "show", spec], capture_output=True, text=True, check=True).stdout
REPS = [
 (4, "N-5e", "RESULTS R124's Corollary EXACT-L as landed", "RESULTS R124's Corollary EXACT-L and Theorem ENDGAME-3-N5 as landed"),
 (4, "L-g", "with fixes entries 1-7", "with fixes entries 1-9"),
 (5, "F-L3-1 (1) = my L3-1", "β-ranks by Ξ-depth with ties broken by β-id",
     "β-ranks depth-major (a smaller Ξ-depth outranks a larger one), inside a Ξ-depth by the rule's local δ, the remaining ties (wire options only) by β-id"),
 (5, "F-L3-1 (2) = my L3-4", "so R104's IDEAL-ACYC-POLY («", "so IDEAL-ACYC-POLY (named in RESULTS R104 and R117; in the words of R104's packet docs/red/P-N5-REALIZE.md: «"),
 (5, "L-h", "with fixes entries 1-9", "with fixes entries 1-10"),
 (6, "L3-3", "(premise R117 (f), under SPEC's S1 tie-breaks, same standing premises)",
     "(with R124's premises as landed, all under the standing SPEC premise 1E-N3, among them RESULTS R117 (f) for EXACT-L, SPEC's S1 tie-breaks through REACH3's [RULE] choice, and RESULTS R15 (c) for Lemma TERM-XI)"),
 (6, "L3-2", "DATA for k ≤ 12: winners = Zielonka's", "DATA for k ≤ 13, k = 13 on one engine: winners = Zielonka's"),
 (6, "L3-5", "CAUSAL and LEMMA′ of fixes entry 4 (4.3, 4.4) are referee-originated, stated and proved by REFEREE 36 (",
     "STABLE's step form, CAUSAL and LEMMA′ of fixes entry 4 (4.2, 4.3, 4.4) are referee-originated, stated by REFEREE 36, which also proved CAUSAL and LEMMA′, the proof of STABLE being the frozen one read in step form ("),
 (6, "L-i", "with fixes entries 1-10", "with fixes entries 1-11"),
]
def main(a):
    ctrl = "--ctrl" in a; a = [x for x in a if x != "--ctrl"]; C, T = a[0], a[1]
    L = {n: show(f"{C}:docs/red-b/P-N5-EXP-line-L{n}.txt") for n in (3, 4, 5, 6)}
    for n in (3, 4, 5, 6): print(f"L-{n} bytes {len(L[n].encode())} sha1 {hashlib.sha1(L[n].encode()).hexdigest()}")
    cur = L[3]; bad = 0
    for stage in (4, 5, 6):
        for (st, name, old, new) in REPS:
            if st != stage: continue
            once = int(cur.count(old) == 1); bad += 1 - once
            if not (ctrl and name.startswith("F-L3-1 (1)")): cur = cur.replace(old, new)
            print(f"  {name}: once {once} bytes {len(old.encode())} -> {len(new.encode())}")
        eq = int(cur == L[stage]); print(f"L-{stage} rebuilt_equals_file {eq}"); bad += 1 - eq
    t = L[6]
    print("L-6 brackets ( %d ) %d [ %d ] %d « %d » %d" % (t.count("("), t.count(")"), t.count("["), t.count("]"), t.count("«"), t.count("»")))
    R = show(f"{T}:docs/RESULTS.md").split("\n")
    def entry(name):
        j = [i for i, l in enumerate(R) if re.match(r"#+\s*" + name + r"\b", l)][0]; e = j + 1
        while e < len(R) and not re.match(r"#+\s*(R|DE)\d+\b", R[e]): e += 1
        return norm("\n".join(R[j:e])), norm(R[j])
    r104, _ = entry("R104"); r117, h117 = entry("R117"); r124, _ = entry("R124")
    Q = [("«stuck» in RESULTS R104", "«stuck»", r104),
         ("the IDEAL-ACYC-POLY sentence in R104's packet", "there is a polynomial q such that L(G) ≤ q(N + M) for every G ∈ IDEAL-ACYC", norm(show(f"{T}:docs/red/P-N5-REALIZE.md"))),
         ("R117's premises in R117's title line", "with R104's premises as landed (1E-N3 = RESULTS R57 (b) in its two forms; RESULTS R24 (a) Lemma R and R24 (b)'s choice rule with RESULTS R103's bridge B and (R1) ruling; RESULTS R36 (c) Lemma P1 on the dual game) and RESULTS R15 (d) for termination only", h117),
         ("REFEREE 36's verdict at c881709b", "NOT SIGNED AS WRITTEN; SIGNED in the form LEMMA′ of §5.3 below", norm(show("c881709b:docs/referee/R-P-N5-EXP.md"))),
         ("REFEREE 36's stage 4 at 78515253", "RESPONSE LEMMA SIGNED as restated in fixes entry 4 (= LEMMA′ of §5.3 with CAUSAL and STABLE in step form).", norm(show("78515253:docs/referee/R-P-N5-EXP.md"))),
         ("REFEREE-2's signature at f17a2708", "REFEREE-2 signs 4.1 (S1)-(S4), 4.2 STABLE, 4.3 CAUSAL, 4.4 LEMMA′ with their proofs (4.2, 4.3, 4.5) and 4.6, as printed in docs/red-b/P-N5-EXP-fixes.md at claude/l-red-b 24f4d436 (sha1 9dc9179f…), (R3)'s range read as t − 1 ≤ τ < last (F-1).", norm(show("f17a2708:docs/referee-2/R2-P-N5-EXP.md")))]
    for name, q, src in Q:
        ok = int(q in t and q in src); bad += 1 - ok; print(f"quotation {name}: in_L6 {int(q in t)} found {int(q in src)}")
    W = [("IDEAL-ACYC-POLY named in RESULTS R104", "IDEAL-ACYC-POLY", r104), ("IDEAL-ACYC-POLY named in RESULTS R117", "IDEAL-ACYC-POLY", r117),
         ("R124: Corollary EXACT-L", "Corollary EXACT-L", r124), ("R124: Theorem ENDGAME-3-N5", "Theorem ENDGAME-3-N5", r124),
         ("R124: all under the standing SPEC premise 1E-N3", "all under the standing SPEC premise 1E-N3", r124),
         ("R124: RESULTS R117 (f) for EXACT-L", "RESULTS R117 (f) for EXACT-L", r124),
         ("R124: SPEC's S1 tie-breaks, through REACH3's [RULE] choice", "SPEC's S1 tie-breaks, through REACH3's [RULE] choice", r124),
         ("R124: RESULTS R15 (c)", "RESULTS R15 (c)", r124), ("R124: for TERM-XI", "for TERM-XI", r124), ("R124: (Lemma TERM-XI) both runs terminate", "(Lemma TERM-XI) both runs terminate", r124)]
    for name, w, src in W:
        ok = int(w in src); bad += 1 - ok; print(f"words of the landed entry — {name}: {ok}")
    print(f"TOTAL failed {bad} ctrl {int(ctrl)}")
if __name__ == "__main__":
    main(sys.argv[1:])
