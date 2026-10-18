"""L-ALG succ. 10 (box 13, produced on Opus 5.5), GAP-A-M §33: the no-counter CORE behind (VR-NEW_all) on 𝒞^1P. For a search s of a
phase and a depth-0 position p, state_s(p) = (R_p, rank_p, V_p, piece_p) and sig_s(p) = (rank_p, |R_p|, |V_p|) (b12_pot.chain).
  (CORE)      if sig_{s′}(p) = sig_{s″}(p) for s′ < s″ and piece_{s′}(p) ∩ piece_{s″}(p) ≠ ∅, then state_s(p) is the same for every s in
              [s′, s″].
  (CORE-ALL)  the weaker form FD-WITNESS needs: at a transition s → s+1, let p0 be the first position whose state changes; then NOT
              every vertex of piece_{s+1}(p0) held sig_{s+1}(p0) at position p0 in some earlier search.
CORE ⇒ CORE-ALL ⇒ (VR-NEW_all) at that transition (GAP-A-M §33a). Printed: transitions, CORE violations (pairs (s′, s″) of one
position), CORE-ALL violations, first instance of each.
Corpus: CLASS=1 [DIST=1] (b12_topchain.classgames, 3 trials, seed 2, n ≤ 200), else the files with n ≤ NMAX (default 100).
Modes (MODE=): core (default), xcover (§33c: cover of the new piece at p0 by earlier same-signature pieces, same / different
context set), sigdisj (§33c: (SIG-DISJ)), samectx (§33b: mechanical check of Lemma SAME-CTX).
Usage: DTL_ORDER=stable|oink [MODE=...] [CLASS=1 DIST=1] b12_core.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, b12_pot as B
from b12_topchain import classgames
from b12_fdkey import plain


def states(ch):
    return [(R, r, V, piece) for j, R, r, V, piece, _ in ch]


def check(d, n):
    """(transitions, CORE violations, CORE-ALL violations, first CORE example, first CORE-ALL example) over the phases of run d."""
    phases = {}
    for ph, calls in getattr(d, "log", []): phases.setdefault(ph, []).append(states(B.chain(calls, n)))
    tr = core = coreall = 0; exc = exa = None
    for ph, L in phases.items():
        for p in range(max(len(x) for x in L)):
            col = [x[p] if p < len(x) else None for x in L]
            for a in range(len(col)):
                for b in range(a + 1, len(col)):
                    A, Bb = col[a], col[b]
                    if A is None or Bb is None: continue
                    if (A[1], len(A[0]), len(A[2])) != (Bb[1], len(Bb[0]), len(Bb[2])) or not (A[3] & Bb[3]): continue
                    if any(col[c] != A for c in range(a, b + 1)):
                        core += 1
                        if exc is None: exc = (ph, p, a, b)
        for s in range(len(L) - 1):
            x, y = L[s], L[s + 1]; tr += 1
            p0 = next((p for p in range(max(len(x), len(y))) if p >= len(x) or p >= len(y) or x[p] != y[p]), None)
            if p0 is None or p0 >= len(y): continue
            R, r, V, piece = y[p0]; sg = (r, len(R), len(V)); held = set()
            for z in L[:s + 1]:
                if p0 < len(z) and (z[p0][1], len(z[p0][0]), len(z[p0][2])) == sg: held |= z[p0][3]
            if piece and piece <= held:
                coreall += 1
                if exa is None: exa = (ph, s, p0, sorted(piece))
    return tr, core, coreall, exc, exa




def xcover(d, n):
    """per transition: |piece_{s+1}(p0)|, vertices of it held (same p0, same signature) at earlier searches with the SAME context
    set (must be ⊆ piece_s(p0) by §33b), and with a DIFFERENT context set (the residual of §33b)."""
    phases = {}
    for ph, calls in getattr(d, "log", []): phases.setdefault(ph, []).append(states(B.chain(calls, n)))
    out = []
    for ph, L in phases.items():
        for s in range(len(L) - 1):
            x, y = L[s], L[s + 1]
            p0 = next((p for p in range(max(len(x), len(y))) if p >= len(x) or p >= len(y) or x[p] != y[p]), None)
            if p0 is None or p0 >= len(y): continue
            R, r, V, piece = y[p0]; sg = (r, len(R), len(V)); same = set(); other = set()
            for z in L[:s + 1]:
                if p0 < len(z) and (z[p0][1], len(z[p0][0]), len(z[p0][2])) == sg:
                    (same if z[p0][0] == R else other).update(z[p0][3] & piece)
            prevpiece = x[p0][3] if p0 < len(x) and x[p0][0] == R else frozenset()
            out.append((len(piece), same, other, same <= prevpiece | other, (ph, s, p0)))
    return out


def sigdisj(d, n):
    """(SIG-DISJ) violations: pairs of searches of one phase whose contexts at one position p differ as sets but share the signature
    (rank, |R|, |V|), with overlapping pieces. Returns (pairs checked, violations, first example)."""
    phases = {}
    for ph, calls in getattr(d, "log", []): phases.setdefault(ph, []).append(states(B.chain(calls, n)))
    chk = bad = 0; ex = None
    for ph, L in phases.items():
        for p in range(max(len(x) for x in L)):
            col = [x[p] for x in L if p < len(x)]
            for a in range(len(col)):
                for b in range(a + 1, len(col)):
                    A, Bb = col[a], col[b]
                    if A[0] == Bb[0] or (A[1], len(A[0]), len(A[2])) != (Bb[1], len(Bb[0]), len(Bb[2])): continue
                    chk += 1
                    if A[3] & Bb[3]:
                        bad += 1
                        if ex is None: ex = (ph, p, a, b, len(A[0]), A[1], len(A[2]), sorted(A[3] & Bb[3])[:5])
    return chk, bad, ex


def samectx(d, n):
    """Mechanical check of Lemma SAME-CTX (§33b): for searches s′ < s of one phase with the same context SET R at one depth-0 position
    and the same signature, V must be equal and piece_{s′} ⊆ piece_s. Returns (pairs checked, V differs, piece not ⊆, first)."""
    phases = {}
    for ph, calls in getattr(d, "log", []): phases.setdefault(ph, []).append(states(B.chain(calls, n)))
    chk = bv = bp = 0; ex = None
    for ph, L in phases.items():
        for p in range(max(len(x) for x in L)):
            col = [x[p] for x in L if p < len(x)]
            for a in range(len(col)):
                for b in range(a + 1, len(col)):
                    A, Bb = col[a], col[b]
                    if A[0] != Bb[0] or (A[1], len(A[2])) != (Bb[1], len(Bb[2])): continue
                    chk += 1
                    if A[2] != Bb[2]: bv += 1; ex = ex or (ph, p, a, b, "V")
                    if not A[3] <= Bb[3]: bp += 1; ex = ex or (ph, p, a, b, "piece")
    return chk, bv, bp, ex


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable"); mode = os.environ.get("MODE", "core")
    src = classgames(sys.argv[1:], 3, 2, 200) if os.environ.get("CLASS") == "1" else plain(sys.argv[1:], int(os.environ.get("NMAX", "100")))
    T = [0, 0, 0, 0]; ex = [None, None]; worst = (0, None)
    for name, g in src:
        try:
            d = B.run(g, order)
        except RecursionError:
            continue
        if mode == "core":
            tr, c, ca, e1, e2 = check(d, g.n); T = [T[0] + tr, T[1] + c, T[2] + ca, 0]
            if e1 and ex[0] is None: ex[0] = (name, g.n, e1)
            if e2 and ex[1] is None: ex[1] = (name, g.n, e2)
        elif mode == "xcover":
            for sz, same, other, ok, where in xcover(d, g.n):
                T[0] += 1; T[1] += bool(other); T[2] += (not ok)
                f = len(same | other) / sz
                if f > worst[0]: worst = (round(f, 3), (name, g.n, where, sz, len(same), len(other)))
        elif mode == "sigdisj":
            c, b, e = sigdisj(d, g.n); T[0] += c; T[1] += b
            if e and ex[0] is None: ex[0] = (name, g.n, e)
        elif mode == "samectx":
            c, bv, bp, e = samectx(d, g.n); T[0] += c; T[1] += bv; T[2] += bp
            if e and ex[0] is None: ex[0] = (name, g.n, e)
    if mode == "core":
        print("order", order, "transitions", T[0], "| CORE violations", T[1], "first", ex[0], "| CORE-ALL violations", T[2], "first", ex[1])
    elif mode == "xcover":
        print("order", order, "transitions", T[0], "| some vertex of the new piece covered cross-context", T[1],
              "| same-context cover outside piece_s (contradicts SAME-CTX)", T[2], "| max covered fraction", worst)
    elif mode == "sigdisj":
        print("order", order, "same-signature different-context pairs", T[0], "| overlapping pieces (SIG-DISJ violations)", T[1], "| first", ex[0])
    else:
        print("order", order, "same-set same-signature pairs", T[0], "| V differs", T[1], "| piece not ⊆", T[2], "| first", ex[0])
