#!/usr/bin/env python3
"""REFEREE successor 37, stage 5b: own-model tests for line L-3 / L-4 of P-N5-EXP and for fixes entry 7 (l-red-b 10dfedb6).
Built on gkx.py (own transcription of the packet's TABLE, own IDEAL step from R104's definitions); no lane code imported.
Subcommands (one line per k; `ctrl` rows are firing controls):
  gloss k..   the line's gloss of rule R's rank clause read AS WRITTEN: «β-ranks by Ξ-depth with ties broken by β-id», i.e.
              br = the rank of (Ξ-depth key, β-id) WITHOUT the rule's local δ, in its four readings (a smaller or a larger depth
              outranks; ties by increasing or decreasing β-id; a wire counts as depth 2k + 5 as in the rule), against rule R
              (rank of the triple (−depth, local δ, β-id), fixes entry 5.1): membership in IDEAL-ACYC and the IDEAL run.
  gloss2 k..  the corrected gloss of line L-5 (depth-major, inside a depth the rule's local δ, the remaining ties by β-id) in
              every reading its words leave open (the direction of the β-id tie-break; the place of the wires): all give G_k's run.
  r3 k.. [--ctrl 1]   fixes entry 7.1 (F-1): clause (R3) of LEMMA′ with the range t − 1 ≤ τ < last at every response window of
              the recursion with j ≥ 2 (r3in, r3move, r3rest must 0); literal = windows where the clause WITHOUT a lower end is
              false (s_τ(E(j)) ≠ a for some τ < t − 1): expected 2^(k−1) − k. Control 1: the range one step too long.
  xt k..      fixes entry 7.3 (F-3): the kinds of movers that are Ξ-targets; wiretgt, etgt must 0; yptgt = 2(k − 3).
No absolute paths. Run with python3 -I."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gkx


def cmd_gloss(args):
    for k in map(int, args):
        G, meta = gkx.rule(k)
        rows, N = meta["rows"], G["N"]
        S0, w0 = gkx.run(G)
        keyR = {}
        variants = {"small_depth_first,bid_up": {}, "small_depth_first,bid_down": {}, "large_depth_first,bid_up": {}, "large_depth_first,bid_down": {}}
        for i, (n, lev, W, X, st, eps, dep, dl) in enumerate(rows):
            d = dep if dep is not None else 2 * k + 5
            for o in range(2):
                b = 2 * i + o
                keyR[b] = (-d, dl[o], b)
                variants["small_depth_first,bid_up"][b] = (-d, b)
                variants["small_depth_first,bid_down"][b] = (-d, -b)
                variants["large_depth_first,bid_up"][b] = (d, b)
                variants["large_depth_first,bid_down"][b] = (d, -b)
        def with_br(key):
            H = dict(G)
            br = [0] * (2 * N)
            for r, b in enumerate(sorted(key, key=lambda b: key[b])):
                br[b] = r
            H["br"] = br
            return H
        ruleok = int(with_br(keyR)["br"] == G["br"])
        out, viol, eq = [], 0, 0
        for name, key in variants.items():
            H = with_br(key)
            S, w = gkx.run(H)
            viol += sum(gkx.member(H))
            eq += int(S == S0)
            out.append(f"{name} L {len(S) - 1}")
        print(f"gloss k {k} rule_R_is_the_rank_of_the_triple {ruleok} L {len(S0) - 1} Lform {int(len(S0) - 1 != 2 ** k - 2)} | the gloss as written, br = rank of "
              f"(depth, β-id) without the local δ: " + "; ".join(out) + f" | member_viol (all four) {viol} runs equal to rule R's {eq} of 4", flush=True)


def cmd_gloss2(args):
    """The corrected gloss (line L-5): «β-ranks depth-major (a smaller Ξ-depth outranks a larger one), inside a Ξ-depth by the rule's
    local δ, the remaining ties (wire options only) by β-id». What the words leave open is the direction of the β-id tie-break and
    the place of the wires (the rule: «a wire counting as depth 2k + 5»; read from the Ξ-graph alone a wire, whose Ξ-target is X,
    would stand at depth 0, the lane's variant wire0). Every reading must give G_k's run."""
    for k in map(int, args):
        G, meta = gkx.rule(k)
        rows, N = meta["rows"], G["N"]
        S0, w0 = gkx.run(G)
        variants = {}
        for wname, wd in (("wires_last_as_in_the_rule", 2 * k + 5), ("wires_first", -1), ("wires_in_the_middle", k + 0.5),
                          ("wires_at_depth_0_their_target_being_X", 0)):
            for bname, sg in (("bid_up", 1), ("bid_down", -1)):
                key = {}
                for i, (n, lev, W, X, st, eps, dep, dl) in enumerate(rows):
                    d = dep if dep is not None else wd
                    for o in range(2):
                        b = 2 * i + o
                        key[b] = (-d, dl[o], sg * b)
                variants[f"{wname},{bname}"] = key
        same = eq = viol = 0
        for name, key in variants.items():
            H = dict(G)
            br = [0] * (2 * N)
            for r, b in enumerate(sorted(key, key=lambda b: key[b])):
                br[b] = r
            H["br"] = br
            same += int(br == G["br"])
            viol += sum(gkx.member(H))
            S, w = gkx.run(H)
            eq += int(S == S0 and w == w0)
        print(f"gloss2 k {k} readings {len(variants)} genome_equal_to_G_k {same} member_viol {viol} run_equal_to_G_k {eq} L {len(S0) - 1} "
              f"Lform {int(len(S0) - 1 != 2 ** k - 2)}", flush=True)


def cmd_r3(args):
    ctrl = 0
    if "--ctrl" in args:
        i = args.index("--ctrl")
        ctrl = int(args[i + 1])
        del args[i:i + 2]
    for k in map(int, args):
        G, meta = gkx.rule(k)
        ix = meta["idx"]
        S, word = gkx.run(G)
        L = len(S) - 1
        sched, calls = {}, []
        gkx.response(k, meta, 1, 0, 1, sched, calls)
        w2 = r3in = r3move = r3rest = literal = 0
        for (j, a, t, last) in calls:
            c = 1 - a
            r3rest += int(not gkx.rest(k, meta, S[last], j, c) or not all(gkx.rest(k, meta, S[last], i, 0) for i in range(j + 1, k)))
            if j < 2:
                continue
            w2 += 1
            e = ix[meta["E"](j)]
            hi = last + 1 if ctrl == 1 else last                 # control 1: t - 1 <= tau <= last
            r3in += sum(1 for tau in range(t - 1, hi) if S[tau][e] != a)
            r3move += int(not (S[last - 1][e] == a and S[last][e] == c))
            literal += int(any(S[tau][e] != a for tau in range(0, t - 1)))
        print(f"r3 k {k} ctrl {ctrl} L {L} windows {len(calls)} windows2 {w2} r3in {r3in} r3move {r3move} r3rest {r3rest} literal {literal} "
              f"expected {2 ** (k - 1) - k} litdiff {int(literal != 2 ** (k - 1) - k)}", flush=True)


def cmd_xt(args):
    for k in map(int, args):
        G, meta = gkx.rule(k)
        names = meta["names"]
        kind = lambda n: "".join(ch for ch in n if not ch.isdigit())
        kinds, wiretgt, etgt, yptgt = set(), 0, 0, 0
        for x in range(G["N"]):
            for (wt, xt, b) in G["opts"][x]:
                if xt < 0:
                    continue
                kd = kind(names[xt])
                kinds.add(kd)
                wiretgt += int(kd in ("wv", "wu"))
                etgt += int(kd == "e")
                yptgt += int(kd in ("yp", "ypb"))
        order = [x for x in ("u", "v", "y", "yb", "yp", "ypb", "e", "wv", "wu") if x in kinds]
        print(f"xt k {k} N {G['N']} kinds {' '.join(order)} wiretgt {wiretgt} etgt {etgt} yptgt {yptgt} expected {2 * (k - 3)} "
              f"ypdiff {int(yptgt != 2 * (k - 3))} outside_the_list_of_5.1_as_written {yptgt + etgt + wiretgt}", flush=True)


if __name__ == "__main__":
    {"gloss": cmd_gloss, "gloss2": cmd_gloss2, "r3": cmd_r3, "xt": cmd_xt}[sys.argv[1]](sys.argv[2:])
