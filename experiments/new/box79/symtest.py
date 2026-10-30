#!/usr/bin/env python3
"""L-NEW box 79: STRICT symbol test for the P-N5-WCH line file. Every symbol token of the line (a token holding a Greek letter, a math
operator, a subscript/superscript mark, a prime, a star, or an all-caps/mixed-case identifier) must appear in BIND below, and its binding
phrase must occur verbatim in the line (in-line binding) or the RESULTS item it names must be cited in the line (landed binding).
Unlisted tokens FAIL. Usage: symtest.py LINEFILE  (prints a table and PASS/FAIL; exit 1 on FAIL)"""
import re, sys
line = open(sys.argv[1]).read()
# token -> (kind, evidence that must occur in the line)
BIND = {
 "N5": ("in", "N5 on EVERY game (SPEC S1-S5"), "SPEC": ("in", "SPEC S1-S5"), "S1-S5": ("in", "SPEC S1-S5"), "S1": ("in", "SPEC S1"),
 "S2": ("in", "(SPEC S2)"), "S4a": ("in", "SPEC S1-S5"), "S4c": ("in", "SPEC S1-S5"), "RESULTS": ("in", "RESULTS R57"),
 "R57": ("in", "RESULTS R57"), "1E-N3": ("in", "1E-N3: S1's procedure realises the pointwise optimum"), "R15": ("in", "R15 (a), (d)"),
 "R17": ("in", "R17 (a) (F1)"), "F1": ("in", "R17 (a) (F1)"), "R56": ("in", "R56"), "R86": ("in", "R86"), "R88": ("in", "R88 (f)"),
 "R89": ("in", "R89"), "R90": ("in", "R90 (a)-(e), (g)"), "R91": ("in", "R91 (a)-(c), (h), (i), (k), (m)"), "R38": ("in", "RESULTS R38 (a)"),
 "σ_new": ("in", "σ_new is the pointwise optimum of the one-player arena H_t"), "H_t": ("in", "H_t := S4a's arena at t"),
 "σ_t": ("in", "the sequence of states (σ_t, τ_t)"), "τ_t": ("in", "the sequence of states (σ_t, τ_t)"), "Iσ_t": ("in", "Iσ_t the improving edges of σ_t (SPEC S2)"),
 "⊴": ("in", "⊴, ◁, ⊵, ▷ the SPEC S1 order"), "◁": ("in", "⊴, ◁, ⊵, ▷ the SPEC S1 order"), "⊵": ("in", "⊴, ◁, ⊵, ▷ the SPEC S1 order"), "▷": ("in", "⊴, ◁, ⊵, ▷ the SPEC S1 order"),
 "n": ("in", "n the number of vertices of the game"), "n_E": ("in", "n_E the number of its Even vertices"),
 "m_E": ("in", "m_E the number of edges leaving Even vertices"), "d_E": ("in", "d_E(e) the number of Even vertices with an edge to the vertex e"),
 "t": ("in", "a transition is written t → t + 1"), "→": ("in", "a transition is written t → t + 1"), "σ_{t+1}": ("in", "v is switched at t if σ_{t+1}(v) ≠ σ_t(v)"),
 "Ξ_t": ("in", "Ξ_t := Ξ_{σ_t} (SPEC S1)"), "Ξ_{σ_t}": ("in", "Ξ_t := Ξ_{σ_t} (SPEC S1)"), "λ_Ξ": ("in", "λ_Ξ its cycle-node map"),
 "W_t": ("in", "W_t := the [S1-val] valuation of the (σ_t, τ_t)-plays"), "[S1-val]": ("in", "SPEC S1"), "λ_W": ("in", "λ_W its cycle-node map"),
 "Z_t": ("in", "Z_t := {v : Ξ_t(v) ≠ W_t(v)} the gap set"), "τ-stretch": ("in", "a τ-stretch, a W-run and, for a W-run F, |F| (its transitions) as in RESULTS R89"),
 "W-run": ("in", "a W-run and, for a W-run F"), "F": ("in", "for a W-run F, |F|"), "|F|": ("in", "|F| (its transitions)"),
 "f_P": ("in", "f_P, ZF_P and WCH^S4a_P(v) as in RESULTS R91"), "ZF_P": ("in", "f_P, ZF_P and WCH^S4a_P(v) as in RESULTS R91"),
 "WCH^S4a_P": ("in", "f_P, ZF_P and WCH^S4a_P(v) as in RESULTS R91"), "P": ("in", "of the phase P"), "S4c fallbacks": ("in", "in-phase Even S4c fallbacks"),
 "Z_{k+1}": ("in", "those k → k + 1 with Z_{k+1} = Z_k"), "Z_k": ("in", "those k → k + 1 with Z_{k+1} = Z_k"), "k": ("in", "those k → k + 1"),
 "λ-run": ("in", "a λ-run as in RESULTS R86"), "B_R": ("in", "B_R (the boundaries inside the λ-run R)"), "R": ("in", "the λ-run R"),
 "SIL_R": ("in", "class-S re-entries and SIL_R as in RESULTS R90 (e)"), "class-S": ("in", "class-S re-entries and SIL_R as in RESULTS R90 (e)"),
 "REPEAT": ("in", "late adoptions, REPEATs, REP_F and REP* := max_F REP_F as in RESULTS R88 (f) and R90 (g)"),
 "REP_F": ("in", "REP_F and REP* := max_F REP_F"), "REP*": ("in", "REP* := max_F REP_F"), "max_F": ("in", "REP* := max_F REP_F"),
 "ρ_P": ("in", "ρ_P := RESULTS R56's ρ of the phase P"), "ρ": ("in", "RESULTS R56's ρ"),
 "TIE": ("in", "(Lemma TIE) at an S4a step"), "σ⁺": ("in", "for any pointwise-optimal Even strategy σ⁺ of H_t"),
 "W′": ("in", "W′ the [S1-val] valuation of the (σ⁺, τ_t)-plays"), "d": ("in", "d := σ_t(v)"), "⊕": ("in", "the prefix operation x ⊕ (c, Q, ℓ) := (c, Q ∪ {x if x is more relevant than c}, ℓ + 1)"),
 "ℓ": ("in", "length ℓ)"), "c": ("in", "cycle node c,"), "x": ("in", "x ⊕ (c, Q, ℓ) :="), "Q": ("in", "path set Q,"), "∪": ("in", "Q ∪ {x if"),
 "RET-WCH": ("in", "(Theorem RET-WCH)"), "u": ("in", "transitions u → u + 1 of F"), "σ_{u+1}": ("in", "σ_{u+1}(v) = e ≠ σ_u(v)"), "σ_u": ("in", "σ_{u+1}(v) = e ≠ σ_u(v)"),
 "WCH_F": ("in", "WCH_F(e) the transitions of F at which W(e) changes"), "W": ("in", "W(v) := W_t(v) at the state in question"), "TT_F": ("in", "TT_F(v, e) the transitions k → k + 1 of F at which v leaves e"),
 "σ_k": ("in", "(σ_k(v) = e ≠ σ_{k+1}(v))"), "σ_{k+1}": ("in", "(σ_k(v) = e ≠ σ_{k+1}(v))"), "W_{k+1}": ("in", "with W_{k+1}(v) = W_k(v)"), "W_k": ("in", "with W_{k+1}(v) = W_k(v)"),
 "TIE_F": ("in", "TIE_F the pairs (v, t), t → t + 1 a transition of F and v switched at t with W_{t+1}(v) = W_t(v)"), "W_{t+1}": ("in", "W_{t+1}(v) = W_t(v)"),
 "NEW-BOUND": ("in", "(Lemma NEW-BOUND"), "RUN-WCH": ("in", "Corollaries RUN-WCH and REP-WCH"), "REP-WCH": ("in", "Corollaries RUN-WCH and REP-WCH"),
 "Σ_e": ("in", "Σ_e d_E(e)·WCH_F(e)"), "Σ_v": ("in", "Σ_v WCH^S4a_P(v)"), "·": ("in", "d_E(e)·WCH_F(e)"), "≤": ("in", "≤"), "≥": ("in", "≥"),
 "SIL-Z": ("in", "(Lemma SIL-Z"), "SC-GXC": ("in", "Corollary SC-GXC)"), "GXC_R": ("in", "GXC_X the GXC events with t, t + 1 in X"), "GXC_P": ("in", "GXC_X the GXC events with t, t + 1 in X"),
 "GXC_X": ("in", "GXC_X the GXC events with t, t + 1 in X"), "X": ("in", "with t, t + 1 in X"), "GXC": ("in", "a GXC event is a pair (v, t)"),
 "max_P": ("in", "max_P GXC_P + NC_R + NT_R (P over the phases inside R)"), "NC_R": ("in", "NC_R (NT_R) the class-S re-entries j − 1 → j of R"), "NT_R": ("in", "NC_R (NT_R) the class-S re-entries j − 1 → j of R"),
 "τ_{t+1}": ("in", "τ_{t+1} = τ_t"), "Ξ_{t+1}": ("in", "Ξ_{t+1}(v) ▷ Ξ_t(v)"), "j": ("in", "re-entries j − 1 → j of R"), "τ_j": ("in", "τ_j ≠ τ_{j−1}"), "τ_{j−1}": ("in", "τ_j ≠ τ_{j−1}"),
 "GXC-CLOSE": ("in", "(Lemma GXC-CLOSE"), "GXC-SPLIT": ("in", "Theorem GXC-SPLIT)"), "Z_a": ("in", "every phase P with first state a"), "a": ("in", "with first state a"),
 "TIE_P": ("in", "TIE_P the pairs (v, t) with t → t + 1 an in-phase S4a transition of P"), "FBO_P": ("in", "FBO_P the GXC events of P at in-phase fallbacks with v ∈ Z_{t+1}"),
 "Z_{t+1}": ("in", "with v ∈ Z_{t+1}"), "LEVEL-MON": ("in", "(Lemma LEVEL-MON"), "DROP-PAID": ("in", "Corollaries DROP-PAID"), "FBO-R56": ("in", "FBO-R56"), "FBO-SPLIT": ("in", "FBO-SPLIT"), "ZF-SPLIT": ("in", "ZF-SPLIT)"),
 "LEV_t": ("in", "with LEV_t(v), for v ∈ Z_t, the position of the first coordinate at which Ξ_t(v) and W_t(v) differ"), "LEV": ("in", "with LEV_t(v), for v ∈ Z_t"),
 "LEV_{t′}": ("in", "LEV_{t′}(v) ≥ LEV_t(v) for states t < t′ of a phase P"), "t′": ("in", "for states t < t′ of a phase P"), "Z_{t′}": ("in", "v ∈ Z_t ∩ Z_{t′}"), "∩": ("in", "Z_t ∩ Z_{t′}"),
 "r": ("in", "for each rank r from n − 1 down to 0"), "LEV_{k+1}": ("in", "LEV_{k+1}(v) > LEV_k(v)"), "LEV_k": ("in", "LEV_{k+1}(v) > LEV_k(v)"),
 "DROP_P": ("in", "number at most (n + 1)(1 + WCH^S4a_P(v)) (DROP_P(v))"), "FBOS_P": ("in", "FBOS_P the FBO events of P with LEV_{t+1}(v) = LEV_t(v)"), "LEV_{t+1}": ("in", "LEV_{t+1}(v) = LEV_t(v)"),
 "FBO": ("in", "FBO_P the GXC events of P at in-phase fallbacks"), "NZ_P": ("in", "NZ_P the Z-flat in-phase fallbacks of P all of whose switched Even vertices"),
 "ZFS_P": ("in", "ZFS_P the other Z-flat in-phase fallbacks of P"), "Z-flat": ("in", "those k → k + 1 with Z_{k+1} = Z_k"),
 "WCH-RED": ("in", "(Theorem WCH-RED"), "WCH-ONE": ("in", "Corollary WCH-ONE)"), "S": ("in", "every τ-stretch S"), "w": ("in", "at most w(n) S4a steps inside S changing W(e)"),
 "[P-WCHτ]": ("in", "(premise [P-WCHτ](w), not proved here)"), "TIE*": ("in", "TIE* := max_F TIE_F"),
 "N5-LZC": ("in", "for the labelled VARIANT N5-LZC (N5 with S4a's output σ* replaced by σ′"), "σ*": ("in", "S4a's output σ*"), "σ′": ("in", "replaced by σ′, which keeps σ_t(v)"),
 "W*": ("in", "W*, the [S1-val] valuation of the (σ*, τ_t)-plays"), "LZ-OPT": ("in", "(Lemma LZ-OPT"), "LZ-STRICT": ("in", "Theorem LZ-STRICT"),
 "RUN-WCH_LZ": ("in", "Corollaries RUN-WCH_LZ, REP-WCH_LZ)"), "REP-WCH_LZ": ("in", "Corollaries RUN-WCH_LZ, REP-WCH_LZ)"),
 "LZ-NOSIL": ("in", "(Corollary LZ-NOSIL, under ASSUMPTION OPT-ONLY"), "OPT-ONLY": ("in", "ASSUMPTION OPT-ONLY that RESULTS R90 Fact B and (a) (ii), (b), (c), (d) hold verbatim for N5-LZC runs"),
 "G-N5-TIME": ("in", "G-N5-TIME stays open"), "M3": ("in", "not M3"), "TARGET.md": ("in", "not a TARGET.md claim"), "REDUCTION": ("in", "a REDUCTION"),
 "VARIANT": ("in", "labelled VARIANT"), "ASSUMPTION": ("in", "ASSUMPTION OPT-ONLY"), "EVERY": ("in", "on EVERY game"), "Even": ("in", "Even vertices"), "Odd": ("in", "Odd follows τ_t"),
 "Lemma": ("word", ""), "Theorem": ("word", ""), "Corollary": ("word", ""), "Corollaries": ("word", ""), "Fact": ("in", "R90 Fact B"), "B": ("in", "R90 Fact B"),
 "(a)": ("word", ""), "≠": ("in", "≠"), "∈": ("in", "∈"), "+1": ("in", "+1, −1 or 0"), "−1": ("in", "+1, −1 or 0"), "−": ("in", "−"), "=": ("word", ""), ":=": ("word", ""),
 "<": ("in", "t < t′"), ">": ("in", ">"), "e": ("in", "for every Even v and successor e"),
 "Ξ-cycle": ("in", "v is its own Ω-cycle node if the cycle node of Ω(v) is v"), "W′-cycle": ("in", "for a valuation Ω (Ξ_t, W_t, or W′ below)"),
 "Ω-cycle": ("in", "v is its own Ω-cycle node if the cycle node of Ω(v) is v"), "Ω": ("in", "for a valuation Ω"), "|Z_a|": ("in", "every phase P with first state a"),
 "REPEATs": ("in", "REPEATs, REP_F and REP*"), "τ_{j−1}": ("in", "τ_j ≠ τ_{j−1}"), "Ξ_{σ_t}": ("in", "Ξ_t := Ξ_{σ_t} (SPEC S1)"), "v": ("in", "v is switched at t"),
}
GREEK = "αβγδεζηθικλμνξοπρστυφχψωΞΣΩΛΔΓΠΦΨℓ"
OPS = "⊴◁⊵▷⊕∪∩≤≥≠∈→·<>"
line_t = re.sub(r"'s\b", "", line)
line_t = re.sub(r"\(([a-m]|i{1,3}|iv)\)", " ", line_t)       # item labels (a)-(m), (ii) of cited RESULTS items
line_t = re.sub(r"\{([^{}]*)\}", lambda m_: " " + m_.group(1) + " " if " " in m_.group(1) else "{" + m_.group(1) + "}", line_t)  # set braces
toks = re.findall(r"\[P-WCHτ\]|\[S1-val\]|[A-Za-z" + GREEK + r"0-9_^*′⁺{}\-−+|.]+|[" + OPS + "]", line_t)
def is_symbol(tok):
    if any(ch in GREEK for ch in tok) or any(ch in OPS for ch in tok): return True
    if any(ch in "_^*′⁺{}|" for ch in tok): return True
    if re.fullmatch(r"[A-Z][A-Z0-9\-]*[A-Z0-9]|[A-Z]", tok): return True     # all caps / single capital
    if re.fullmatch(r"[a-z]", tok): return True                              # single-letter variable
    if re.fullmatch(r"[A-Z][a-z]*[A-Z][A-Za-z0-9\-_*]*", tok): return True   # mixed case like REP-WCH_LZ
    if tok in BIND: return True
    return False
def norm(tok):
    tok = tok.strip(".,;:()")
    tok = re.sub(r"\(.*$", "", tok)
    return tok
seen = {}; fails = []
for raw in toks:
    t = norm(raw)
    if not t or not is_symbol(t): continue
    if re.fullmatch(r"[0-9+]+", t): continue
    seen[t] = seen.get(t, 0) + 1
rows = []
for t in sorted(seen):
    b = BIND.get(t)
    if b is None:
        # composite tokens like W_t(v) normalised away; try stripping trailing argument
        rows.append((t, seen[t], "UNBOUND", "")); fails.append(t); continue
    kind, ev = b
    ok = kind == "word" or (ev in line)
    rows.append((t, seen[t], "OK" if ok else "EVIDENCE-MISSING", (kind + ": " + ev)[:90]))
    if not ok: fails.append(t)
print("| symbol | uses | status | binding (verbatim phrase in the line) |"); print("| --- | --- | --- | --- |")
for t, k, st, ev in rows: print(f"| {t} | {k} | {st} | {ev} |")
print(f"\nsymbols {len(rows)}, failures {len(fails)}: {fails}")
print("SYMTEST", "PASS" if not fails else "FAIL"); sys.exit(1 if fails else 0)
