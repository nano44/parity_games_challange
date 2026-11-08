# REFEREE-2 32: every OLD string of my W / D items occurs exactly once in its file at claude/l-si e3ac4b06 (byte test, own code)
import subprocess, hashlib
S = "e3ac4b06f13cd0c7c7ac4589b0c5824bf41ca5a7"
def show(f): return subprocess.run(["git", "show", f"{S}:{f}"], capture_output=True).stdout
P, L = show("docs/si/P-ACYC.md"), show("docs/si/P-ACYC-line-L1.txt")
print("packet sha1", hashlib.sha1(P).hexdigest(), len(P), "B; L-1 sha1", hashlib.sha1(L).hexdigest(), len(L), "B")
olds = [
 ("P", "w*: the two plays from K2 lie inside the closed core, which does not depend on σ. So Odd's optimal choice at K2 does not depend on σ."),
 ("P", "w* does not depend on σ."),
 ("P", "Hence a super-polynomial\ntower family would bear on N5 only, and N5′-xi lower bounds need Ξ-cyclic genomes."),
 ("P", "A family of towers with L super-polynomial in N + M would therefore bear on N5 (R117's Corollary REAL-IDEAL-S3), not on N5′-xi."),
 ("P", "For N5′-xi to be slow, R must grow (R118 (l)'s equivalence), and R = 0 on every Ξ-acyclic genome. So a candidate counter for\n  N5′-xi must have a Ξ-cycle."),
 ("P", "its FL run has length exactly L(G)"),
 ("P", "the number of iterations after the first fallback (DATA: 2 more on every genome of §6, but no bound);"),
 ("P", "Unit: genomes whose first fallback k1 has k1 − 1 > N; genomes with no fallback; states 0, …, k1 − 1 that are non-standard."),
 ("L", "σ̄ off the β-face 0, non-standard states 0, genomes with first fallback after iteration N + 1 0;"),
 ("L", "control, five Ξ-cyclic genomes: σ̄ off the β-face 121, C 15, R 25"),
 ("L", "the order ⊴ and σ̄ of R118 [VJ]"),
 ("P", "- Notation. Ω_τ(v) is the value of the (σ, τ)-play from v. σ̄ is an optimal counterstrategy: Ω_σ̄(v) ⊴ Ω_τ(v) for every Odd strategy τ and\n  every v (R118 [VJ]: the order of VJ00 §4.2, Friedmann §3)."),
]
for w, s in olds:
    t = (P if w == "P" else L).decode()
    print(w, t.count(s), "|", s.replace("\n", "⏎")[:110])
