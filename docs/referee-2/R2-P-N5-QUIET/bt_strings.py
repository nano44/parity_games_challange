#!/usr/bin/env python3
"""REFEREE-2 succ. 33: my required strings for P-N5-QUIET line L-1 (W-1, W-2, W-3, D-1 (b), D-2): each old string once in L-1, spans
disjoint; prints L-1 + all of them (sha1, bytes, parens). D-1 (a) (tool fix) changes no string. Usage: bt_strings.py L1.txt"""
import sys, hashlib
L = open(sys.argv[1], encoding='utf-8').read()
S = [
 ("W-1",
  "«T bounds IDEAL-CYC iterations; on Γ3 this bounds N5′-xi only up to its first fallback, and only under REACH3-CYC; nothing is claimed about post-fallback iterations, N5′-xi's total count, N5 or general games» (witnesses that the restriction is needed: L-RED R221 §7 DIV_2_493, DIV_2_583, DIV_3_717, claude/l-red d49b9f0c, experiments/red/r221q/inst/SHA1SUMS, where N5′-xi on Γ3 changes movers after its first fallback)",
  "nothing is PROVED about N5′-xi on Γ3(G): T_CYC is the Howard count on Γ(G), while RESULTS R118 (k), (l) (PROVED-CONDITIONAL on [REACH-L]) put N5′-xi's first fallback on Γ3(G) at iteration T3 + 1 with T3 the Howard count ON Γ3(G); that QUIET, T-QUIET, ASC-T and UP-T carry over to Γ3(G), which would bound T3, is a READING, not claimed; nothing is claimed about iterations after the first fallback, N5′-xi's total count, N5 or general games (L-RED R221 §7 DIV_2_493, DIV_2_583, DIV_3_717, claude/l-red d49b9f0c, experiments/red/r221q/inst/SHA1SUMS: N5′-xi on Γ3 changes movers after its first fallback)"),
 ("W-2",
  "[OPT] = RESULTS R57 (b)'s standing SPEC premise as landed in R104 («that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance», «used in two forms: S1's σ̄, and τ̄ on the dual game, are pointwise optima»; Lead reading 00:36Z that this covers IDEAL-CYC's σ̄_t, for the referees), optionally RESULTS R21 (a);",
  "[OPT] (σ̄_t is optimal at every vertex at once) = RESULTS R118's setting «σ̄ is Odd's optimal counterstrategy, chosen by a fixed deterministic rule» read with R118's premise VJ00 / Friedmann arXiv 1106.0778 §3, where «A strategy τ is an optimal counterstrategy w.r.t. σ iff for every opponent strategy τ′ and for every node v» its value is ⊴ the value under τ′ (existence: Friedmann Lemma 3.1, [VJ00]);"),
 ("W-3",
  "[E-LEV] is R104 (vi)'s packet §3.1 order (docs/red/P-N5-REALIZE.md l. 88) by Lead reading 23:54Z, else a hypothesis",
  "[E-LEV] is a HYPOTHESIS, not a landed premise (it is the order of R104's packet §3.1, docs/red/P-N5-REALIZE.md l. 88, but R104 (vi) leaves the exact e-priorities to that packet and calls them immaterial to R104's statements, and RESULTS R121 states UP-B under HYPOTHESIS [E-LEV])"),
 ("D-1b-i", "QUIET: wfail 0 (unit: quiet windows)", "QUIET: wfail 0 (unit: quiet steps more than L + 1 steps into their window)"),
 ("D-1b-ii", "T-QUIET: Tfail 0 (unit: runs with T > Q + (Q + 1)L; same set as QUIET)", "T-QUIET: Tfail 0 (unit: runs with T > Q + (Q + 1)(L + 1); same set as QUIET)"),
 ("D-2", "LOC-K2: k2fail 0 (unit: states; same runs)", "LOC-K2: k2fail 0 (unit: states with σ̄_t(K2) ≠ K1, the first conjunct only; same runs)"),
]
spans = []
for k, o, nw in S:
    c = L.count(o); i = L.find(o); spans.append((i, i + len(o), k)); print(k, "old in L-1:", c, " new in L-1:", L.count(nw))
spans.sort(); print("disjoint:", all(a[1] <= b[0] for a, b in zip(spans, spans[1:])))
for tag, sel in (("L-1 + W-1, W-2, W-3, D-1 (b), D-2", S), ("L-1 + W-1, W-2, W-3, D-2 (D-1 by tool fix (a))", [s for s in S if not s[0].startswith("D-1")])):
    X = L
    for k, o, nw in sel: X = X.replace(o, nw)
    b = X.encode(); print(tag, ": sha1", hashlib.sha1(b).hexdigest(), len(b), "B", X.count("("), "( =", X.count(")"), ")", "« »", X.count("«"), X.count("»"))
