#!/usr/bin/env python3
"""L-SI P-N5-GATE fixes entry 2 (Lead ruling 2026-11-09 09:24Z (a): the IDEAL-CYC PROVISO only). Prints entry 2 (to be appended after
entry 1). L-RED's statement is quoted from the byte copy ref_R229-box93_2730ab90.md (sha1 in fix2.sha1), asserted verbatim once (wrapped
lines joined by one space); the frozen packet's sha1 is asserted, and each packet string named here is asserted once in it.
Usage: mkfix2.py ROOT L2SHA1 L2BYTES"""
import hashlib, os, re, sys
ROOT, S2, B2 = sys.argv[1], sys.argv[2], sys.argv[3]
HERE = os.path.dirname(os.path.abspath(__file__))
raw = open(os.path.join(ROOT, "docs/si/P-N5-GATE.md"), "rb").read()
assert hashlib.sha1(raw).hexdigest() == "f3a584e68b5c998276ea717f42920bdeeca581ab"
pk = re.sub(r"\s*\n\s*", " ", raw.decode("utf-8"))
ref = re.sub(r"\s*\n\s*", " ", open(os.path.join(HERE, "ref_R229-box93_2730ab90.md"), encoding="utf-8").read())
def q(s, src):
    assert src.count(s) == 1, s[:70]
    return "«" + s + "»"
ST = q("**Lemma PROVISO (PROVED, L-RED lane; premises: landed R123 B-ONLY; [DEF]: e_o's only successor is its W-target D, or c_W).** On "
       "IDEAL-CYC(G), for every genome, every gate o and every state t, D's play does not pass e_o.", ref)
B = q("(b) At every t with e_o ∉ P_(t−1)(D) ∪ P_t(D): Ω_t(p_e) ≠ Ω_(t−1)(p_e) ⟺ Ω_t(D) ≠ Ω_(t−1)(D).", pk)
C = q("(c) If D's play avoids e_o over the run:", pk)
W = q("Lemma WAIT-QUIET (= (a) + (b)). A gate whose e-face continuation D changes value at most K times while its play avoids e_o", pk)
P = q("- The proviso «D's play avoids e_o» was never violated on any measured instance (L-RED 63: dpass 0 on 29 instances).", pk)
O = []
w = O.append
w("")
w("## Entry 2 (fix round 2; L-SI successor 50; Lead ruling 2026-11-09 09:24Z (a): the IDEAL-CYC PROVISO only)")
w("Item: the proviso «D's play avoids e_o» of §3.4 (b), (c) and WAIT-QUIET, on IDEAL-CYC. Γ3 is NOT changed here: B-ONLY on Γ3 (box 96's")
w("Lemma B-ONLY3) goes to a separate packet P-N5-BONLY3 after L-RED 64's attack (ruling (b)). Strings: this text by")
w("experiments/si/box95/fix2/mkfix2.py (quotes asserted verbatim once, in L-RED's text and in the frozen packet); L-2 by fix2/mkL2.py.")
w("")
w("### F2-1 (PROVISO on IDEAL-CYC): cited, and derived independently")
w("- Cited: L-RED 63, claude/l-red 2730ab90, docs/red/R229-box93.md Addendum B (byte copy experiments/si/box95/fix2/ref_R229-box93_2730ab90.md,")
w("  sha1 in fix2/fix2.sha1): " + ST)
w("- Independent derivation (L-SI box 96 §1, docs/si/box96-bonly3.md at claude/l-si 6ee19b24, written before L-RED's text was on origin;")
w("  the same argument). D := e_o's successor (RESULTS R104: e has one edge, to the W-target or to c_W). If D = c_W, P_t(D) is c_W's")
w("  loop. Otherwise D is a mover; if e_o ∈ P_t(D), the vertex after e_o is D, the play's first vertex, so the play closes there and its")
w("  cycle is the whole play, which carries e_o; then Λ_t(D) is e_o or more relevant. RESULTS R123 Lemma B-ONLY («at every state t and")
w("  every vertex v other than c_W and the e-vertices whose successor is c_W, Λ_t(v) is less relevant than every e-vertex») at the")
w("  mover D says the opposite. ∎")
w("- Shared premise: RESULTS R123 B-ONLY is the one premise of both G1's IDEAL-CYC clause (entry 1: K10 empty) and PROVISO.")
w("- Effect on the frozen text (IDEAL-CYC only; no statement is weakened; Γ3 unchanged):")
w("  - §3.4 " + B + ": on IDEAL-CYC the hypothesis holds at every t, so S(p_e) = S(D) for every gate over the whole run (both values")
w("    constant when D = c_W).")
w("  - §3.4 " + C + " and " + W + ": on IDEAL-CYC the proviso is always met; read them there with it deleted.")
w("  - §3.4 " + P + " New, after it: «On IDEAL-CYC it holds at every state (Lemma PROVISO, L-RED 63, claude/l-red 2730ab90 R229-box93")
w("    Addendum B; premise RESULTS R123 B-ONLY). On Γ3 it remains a hypothesis of (b), (c) and WAIT-QUIET in this packet.»")
w("  - §1 premises: RESULTS R123 B-ONLY is now used on IDEAL-CYC (it is already in §1's landed list, «R123 (LOC-GATE, NO-TIE, B-ONLY, …)»).")
w("- DATA: L-RED 63's dpass 0 on 29 instances (own engine; R229-box93 §2, fa4e50fe; and its 2000-iteration DP climb, Addendum A); L-SI")
w("  box 96's dpass 0 (unit (gate, state); 19 instances: box 91's 11, box 93's 8; 307,737 pairs per engine; own and g3, rows identical;")
w("  experiments/si/box96/out/own96.out, g396.out); control CTRL=anti (Odd non-optimal: e-face at o, β-face elsewhere; own engine) fires")
w("  on 14 of 19 (out/ctrl96.out).")
w("")
w("### Line L-2")
w("- docs/si/P-N5-GATE-line-L2.txt = L-1 with three replacements (fix2/mkL2.py, each Old asserted once in L-1): the proviso clause (IDEAL-CYC")
w("  PROVISO stated, with its proof in one sentence; Γ3 a hypothesis), PROVISO's DATA clause, «fixes entries 1-2». sha1 " + S2 + ", " + B2)
w("  bytes (wc -c). L-1 stays as written (a44647db…, 9,541 bytes).")
sys.stdout.write("\n".join(O) + "\n")
