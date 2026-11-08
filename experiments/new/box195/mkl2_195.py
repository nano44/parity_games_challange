#!/usr/bin/env python3
# P-N5-END line L-2 generator (L-NEW successor 64). From the repo root: python3 experiments/new/box195/mkl2_195.py
# L-2 = L-1 + the replacements R1-R12 below (fixes entry 2: REFEREE 29 R-P-N5-END §7 LN-1..LN-8 and §6 EN-1, EN-3; claude/referee
# e4cb208a). Asserts L-1's sha1, each old string exactly once in L-1, the LN-4 quote verbatim in trunk docs/new/P-N5-XICYC.md
# (git show c8f42538f), one line, no «|», balanced parentheses.
import hashlib, subprocess
L = open("docs/new/P-N5-END-line-L1.txt", encoding="utf-8").read()
assert hashlib.sha1(L.encode()).hexdigest() == "68a691764c57ef16bb8a8c294925954a3c71fb1b", "L-1 changed"
XI = " ".join(subprocess.run(["git", "show", "c8f42538f:docs/new/P-N5-XICYC.md"], capture_output=True, text=True, check=True).stdout.split())
T3Q = "T3 is the first state at which no mover has a strictly better successor in Γ3"
assert T3Q in XI, "LN-4 quote"
R = [
 ("R1 LN-2", "for N5 (SPEC S1-S5) and N5′-xi", "for N5 (SPEC S1-S5 with FIX 1-4) and N5′-xi"),
 ("R2 LN-1", "for every genome G: (Lemma E0)", "for every genome G, each PROVED (every genome): (Lemma E0)"),
 ("R3 LN-2", "have exactly one fallback, at an iteration F ≥ 1, and make exactly F + 2 iterations",
             "have exactly one fallback, at an iteration F ≥ 1, and exactly F + 2 iterations"),
 ("R4 LN-1, LN-3, EN-1", "(Corollary EXACT-L, for G ∈ IDEAL-ACYC: «Ξ-graph is ACYCLIC (self-loops count as cycles)», premise RESULTS R117 (f)) N5 from S3",
  "(Corollary EXACT-L, PROVED for G ∈ IDEAL-ACYC (R104: the Ξ-graph is acyclic; self-loops count as cycles; «Ξ-graph is ACYCLIC (self-loops count as cycles)»), premise RESULTS R117 (f); it uses SPEC's S1 tie-breaks, through REACH3's [RULE] choice: with another pointwise-optimal S4a choice the identity can fail, F = 1 on 382 of 382 IDEAL-ACYC genomes with L ≥ 1, REFEREE 29's counter, R-P-N5-END §4 (C), claude/referee e4cb208a, docs/referee/scratch/end_logs/tiedep.out, cited, not re-run) N5 (SPEC S1-S5 with its FIX 1-4 tie-breaks) from S3"),
 ("R5 EN-3", "so on {Γ3(G) : G ∈ IDEAL-ACYC} N5's count is polynomial in n iff L(G) is polynomial in N + M",
             "so on {Γ3(G) : G ∈ IDEAL-ACYC} N5's iteration count is polynomial in n iff L(G) is polynomial in N + M (a statement about iteration counts; the cost per iteration at bit cost is a separate gauntlet step-4 item)"),
 ("R6 LN-1", "(Corollary END-T3, PROVED-CONDITIONAL on RESULTS R118 (k)'s Theorem REACH3-CYC, which is itself «",
             "(Corollary END-T3, PROVED-CONDITIONAL on REACH3-CYC, RESULTS R118 (k), itself PROVED-CONDITIONAL on [REACH-L]: «"),
 ("R7 LN-4", "makes exactly T3 + 3 iterations, T3 + 1 being REACH3-CYC's first fallback",
             "makes exactly T3 + 3 iterations, with T3 as in R118 (k) (P-N5-XICYC §7: «" + T3Q + "»), T3 + 1 being the first fallback"),
 ("R8 LN-5", "Lemma S3-START and, for E0, TAU3 («", "Lemma S3-START and, for E0, [TAU3] (RESULTS R117 / P-N5-REACH §6.4: «"),
 ("R9 LN-5", "(R118 (b)'s [OPT] is not used)", "(REFEREE 29 rules [OPT] = [1E-N3] for SPEC runs; R118 (b)'s [OPT] is not used)"),
 ("R10 LN-6", "plus the 14 R117 corpus genomes and every pinned genome of box189 and box191-box194, all pinned in box195/end.pins)",
              "plus the 14 R117 corpus genomes in spec mode (sweep195.out); and check195.out (re-run by check.sh): 8 families × 300, seed 1953, per mode, plus every pinned genome of box189 and box191-box194; all pinned in box195/end.pins)"),
 ("R11 LN-6", "nofb 0, late 0, capped 0 (unit: runs)", "nofb 0 and capped 0 (unit: runs), late 0 (unit: iterations after F + 2)"),
 ("R12 LN-6", "on 4,297 genomes (4,283 random IDEAL-ACYC ones in the spec sweep, 3,000 of them from acyc, and the 14 corpus genomes; L(G) up to 59, RECT_d11_T59_norm; L(G) by L-RED's ideal.traj at claude/l-red 86a7a7a8, record only)",
              "on 4,297 genomes, spec runs only (4,283 random IDEAL-ACYC ones in the spec rows of sweep195.out, 3,000 of them from acyc, and the 14 corpus genomes; L(G) up to 59, RECT_d11_T59_norm, 62 iterations; L(G) by L-RED's ideal.traj at claude/l-red 86a7a7a8, record only (not re-run by check.sh, which leaves LRED unset))"),
 ("R13 LN-6", "controls fire (ctrl1 100 of 100 runs, ctrl2 200 states; check195.out)",
              "controls fire (check195.out: ctrl1 e2fail, e3fail, e4fail, stopfail, finsbar, fintie 100 each in 100 runs; ctrl2 e0fail 200 and e1fail 200 (unit: states), nofb 100 (unit: runs))"),
 ("R14 LN-6", "independent replay L-RED 57 R222 item 3 (claude/l-red 6f56004c, own code): 8,100 runs, every counter 0, and L-RED 58 R223 item 1 (claude/l-red 143f0b4c): 8,100 family runs, 48,816 exhaustive N ≤ 2 genomes × 3 modes, 30,000 N = 3 genomes, 515 second-implementation checks, 0 fails; both cited, not re-run; ",
              "independent replays, every fail counter 0, their counters in their own pinned outputs, cited, not re-run: L-RED 57 R222 item 3 (claude/l-red 6f56004c), L-RED 58 R223 item 1 (claude/l-red 143f0b4c), REFEREE 29 R-P-N5-END §4 (claude/referee e4cb208a); "),
 ("R15 LN-7", "it bounds none of F, T3, L(G), and nothing outside Γ3(G)", "it bounds none of F, T3, L(G) (OPEN), and nothing outside Γ3(G)"),
 ("R16 LN-8", "with fixes entry 1, docs/new/P-N5-END-fixes.md;", "with fixes entries 1-2, docs/new/P-N5-END-fixes.md;"),
]
for name, old, new in R:
    assert L.count(old) == 1, (name, L.count(old)); L = L.replace(old, new)
b = L.encode("utf-8"); h = hashlib.sha1(b).hexdigest()
assert L.count("\n") == 1 and "|" not in L and L.count("(") == L.count(")"), (L.count("("), L.count(")"))
open("docs/new/P-N5-END-line-L2.txt", "w", encoding="utf-8").write(L)
print(f"R1-R{len(R)} old once each, applied; sha1 {h} {len(b)} bytes; parens {L.count('(')} {L.count(')')}")
