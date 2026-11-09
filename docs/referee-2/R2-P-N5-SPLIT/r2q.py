#!/usr/bin/env python3
"""REFEREE-2 successor 36: premise check for P-N5-SPLIT (l-new 399cda07). Every P-N5-CHAIN fact SPLIT names (its §1 list) must be
defined in P-N5-CHAIN (93531b03, sha1 6e613ba7) in the section SPLIT says, and every content SPLIT restates (pairs below: SPLIT's words,
CHAIN's words) must be found verbatim (whitespace collapsed) in the respective text. Inputs by `git show` (run from the repo root).
Also: every «…» of SPLIT is looked up in SPLIT's own sources (CHAIN, CHAIN fixes, L-4, TARGET.md); misses are listed for hand check."""
import subprocess, re, sys
def show(rev, path): return subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, text=True, check=True).stdout
def norm(s): return re.sub(r"\s+", " ", s)
SP = show("399cda07", "docs/new/P-N5-SPLIT.md"); CH = show("93531b03", "docs/new/P-N5-CHAIN.md")
CF = show("63515442", "docs/new/P-N5-CHAIN-fixes.md"); L4 = show("63515442", "docs/new/P-N5-CHAIN-line-L4.txt")
TG = show("63515442", "TARGET.md")
nSP, nCH = norm(SP), norm(CH)
# section of CHAIN where each anchor is defined
CHn = norm(CH)
secs = [(m.start(), m.group(1)) for m in re.finditer(r" ## (\d+)\. ", " " + CHn)]
def sec(pos): return max([s for p, s in secs if p <= pos] or ["0"])
ANCH = {  # name: (anchor in CHAIN, section SPLIT §1 gives)
 "HOW3(G)": ("- HOW3(G): Γ3(G) with every non-mover Even vertex frozen", "2"), "T3": ("T3 := the first state at which no mover has a strictly better successor", "2"),
 "n3": ("n3 := N + 7M + 10", "2"), "[OPT]": ("- [OPT] σ̄_t is optimal at every vertex at once", "1"), "[G3]": ("- [G3] RESULTS R117", "1"),
 "[DEF]": ("- [DEF] RESULTS R104", "1"), "(R)": ("- (R) Rank order", "2"), "(P)": ("- (P) PAD (a)", "2"), "(E-DOM)": ("- (E-DOM) Every vertex", "2"),
 "(Core)": ("- (Core) In standard states and in HOW3", "2"), "F1": ("- F1. Ω_t ⊴ Ω_(t+1) pointwise", "4"), "F2": ("- F2. If Ω(v) ⊴ Ω′(v)", "4"),
 "F3": ("- F3. If Λ_t(v) ≠ v", "4"), "F4′": ("- F4′. If v ∉ Π(A) ∪ Π(B)", "4"), "F5": ("- F5. σ_(t+1)(x) is ⊴-best", "4"), "F6": ("- F6. No mover", "4"),
 "DOM": ("- DOM. For every mover x", "4"), "STRICT": ("- STRICT. If σ_(t+1)(x) ≠ σ_t(x)", "4"), "CYC": ("- CYC. Λ_t(v) takes values", "4"),
 "CN2-3": ("**Lemma CN2-3.**", "5"), "LOC-GATE3": ("**Lemma LOC-GATE3.**", "5"), "LOC-K2-3": ("**Lemma LOC-K2-3.**", "5"),
 "B-ONLY3": ("**Lemma B-ONLY3.**", "5"), "NO-TIE3": ("**Corollary NO-TIE3.**", "5"), "T-QUIET3": ("**Corollary T-QUIET3.**", "6"),
 "L3": ("L3 := (M + 1)(2M + 1)(N + 1) + N(n3 − 1)", "6"), "E-MON3": ("**Lemma E-MON3.**", "7"), "CHAIN-DECOMP3": ("**Lemma CHAIN-DECOMP3.**", "7"),
 "[E-LEV]": ("- HYPOTHESIS [E-LEV]", "1"), "seq/E/lex": ("seq_t(v) := the e-vertices of Π_t(v) in play order", "7")}
print("== anchors (name: found, CHAIN section, SPLIT's section)")
bad = 0
for k, (a, s) in ANCH.items():
    p = CHn.find(norm(a)); ok = p >= 0 and sec(p) == s
    if not ok: bad += 1
    print(f"{k}: {'OK' if ok else 'MISS'} §{sec(p) if p >= 0 else '-'} (SPLIT: §{s})")
# restated contents: (SPLIT words, CHAIN words)
PAIRS = [
 ("By F1 and F2, Λ_t(v) changes only to a vertex of strictly larger reward", "by F1 and F2 it changes only to a vertex of strictly larger reward"),
 ("by CYC there are at most 2M + 3", "Λ_t(v) takes values among at most 2M + 3 vertices"),
 ("Vertices more relevant than an e-vertex are e-vertices, c_W, K0, K3 (E-DOM)", "Every vertex more relevant than some e-vertex is an e-vertex, c_W, K0 or K3"),
 ("c_W is in no Π", "c_W is never in Π"),
 ("e-priorities are even, [DEF]", "«e of even priority above every β with one edge to the W-target or to the top even self-loop c_W»"),
 ("Non-mover Even vertices and pads have one successor in HOW3 (F6, [G3])", "Every non-mover Even vertex has one successor in HOW3."),
 ("σ̄_s(K2) = r at every state (LOC-K2-3)", "At every state σ̄_t(K2) = r"),
 ("F5: σ_t(u) is ⊴-best under Ω_(t−1) and strictly better than σ_(t−1)(u) when they differ", "σ_(t+1)(x) is ⊴-best among x's successors under Ω_t, and Ω_t(σ_(t+1)(x)) ▷ Ω_t(σ_t(x)) when they differ"),
 ("LOC-GATE3: Odd's chosen face is the ◁-smaller one where the values differ; NO-TIE3: they never tie", "If Ω(a) ≠ Ω(b), then Ω(a) ◁ Ω(b)."),
 ("NO-TIE3: they never tie", "At every state and gate g, Ω_t(pe_g) ≠ Ω_t(pβ_g)."),
 ("F1 (Ω_(t−1)(new) ⊴ Ω_t(new))", "F1. Ω_t ⊴ Ω_(t+1) pointwise"),
 ("By F3 and F6, Ω_r(u) = ext(u, Ω_r(σ_r(u))) at every r", "If Λ_t(v) ≠ v then Ω_t(v) = ext(v, Ω_t(nx_t(v)))"),
 ("Ω_s(u) (F1) ▷ Ω_(s−1)(u) (STRICT)", "If σ_(t+1)(x) ≠ σ_t(x), then Ω_(t+1)(x) ▷ Ω_t(x)"),
 ("F4′ gives X ⊴ Y ⇒ ext X ⊴ ext Y", "A ⊴ B ⇒ ext(v, A) ⊴ ext(v, B)"),
 ("u is in no Π, CN2-3", "no mover, gate or pad is ever a cycle node or in a set Π"),
 ("On J_b, E(b) ∩ U_y is lex-nondecreasing (E-MON3)", "If Λ_t(v) = Λ_(t+1)(v) then E_t(v) ≤ E_(t+1)(v)."),
 ("Mover edges go to the M pads m_(x,k), one per option; gate edges go to the 2M face pads pe_g, pβ_g ([G3])", "pe_g and pβ_g on both faces of every gate g, pb_g on every β_g → u, and m_(x,k) on every mover edge x → (x, k)"),
 ("Sum D^tot_E(v) − 1 over the n3 vertices and apply T-QUIET3", "T3 ≤ Q + (Q + 1)·L3 ≤ (1 + Σ_v (D^tot_E(v) − 1))·(L3 + 1), the sum over the n3 vertices of Γ3(G)."),
 ("Under [E-LEV], f more relevant than f′ implies lev(f) ≥ lev(f′)", "lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′))"),
 ("y is a mover of level lev(c_i) − 1 (CHAIN-DECOMP3)", "then f's successor y_f is a mover, Λ_t(y_f) = Λ_t(v) and E_t(v) = {f} ∪ E_t(y_f)"),
 ("e_(g1), which is more relevant than w (B-ONLY3)", "Λ_t(v) is less relevant than every e-vertex"),
 ("distinct vertices have distinct rewards (F2)", "distinct vertices have distinct rewards ([VJ])"),
 ("K0 and K3 lie on both plays or on neither, since a play passes K0 iff it passes K3 iff its cycle node is in the closed core ((Core))", "So a play passes K0 iff it passes K3, iff it enters the core through some pb_g; K0 and K3 lie on no cycle."),
]
print("== restated contents (SPLIT side / CHAIN side found verbatim, whitespace collapsed)")
for a, b in PAIRS:
    fa, fb = norm(a) in nSP, norm(b) in nCH
    if not (fa and fb): bad += 1
    print(f"{'OK ' if fa and fb else 'MISS'} SPLIT {fa} CHAIN {fb}: {a[:70]}")
print("== «…» quotes of SPLIT looked up in CHAIN, CHAIN fixes, L-4, TARGET.md, SPLIT's own fixes")
SF = show("63515442", "docs/new/P-N5-SPLIT-fixes.md")
src = norm(CH + CF + L4 + TG + SF)
qs = re.findall(r"«([^»]*)»", SP)
for q in qs:
    print(("FOUND " if norm(q) in src else "NOT-IN-SOURCES ") + q[:110])
print(f"anchors+pairs misses: {bad}; quotes: {len(qs)}")
# the CHAIN fixes entry 3 W-1 sentence and L-4's R-W clause
for s in ("(Core)'s «a play passes K0 iff it passes K3» (plays from pA or K3 pass K3, not K0)", "(F-cls3)'s convexity and E-MON3's reason hold for non-core vertices"):
    print("CHAIN fixes/L-4:", norm(s) in norm(CF + L4), s[:80])
