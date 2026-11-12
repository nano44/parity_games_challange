#!/usr/bin/env python3
"""T66 Addendum D (L-LIT): Friedmann's G_N with the priorities of [F11] Table 4 as printed (g_N and a_1 both 4N + 4) and with the
priorities of [F11] Figure 4 / Fact 6.1 (d, e, g, k, f, h lower by 2; all distinct). Runs docs/lit/T66-depth-check.py's counters on
both and prints one line per game. Run from the repo root: python3 -I docs/lit/T66-fig4-check.py LO HI C
The second variant is made by textual replacement of six priority formulas in T66-depth-check.py's lmcs (asserted to occur once)."""
import sys, io, contextlib
sys.path.insert(0, ".")
src = open("docs/lit/T66-depth-check.py").read()
lo, hi, c = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
def load(shift):
    s = src
    if shift:
        for a, b in [("4 * i + 1, [\"s\"", "4 * i - 1, [\"s\""), ("1, 4 * i + 2, [f\"d{i}\"", "1, 4 * i, [f\"d{i}\""),
                     ("0, 4 * i + 4, [f\"f{i}\"", "0, 4 * i + 2, [f\"f{i}\""), ("8 * n + 4 * i + 7,", "8 * n + 4 * i + 5,"),
                     ("8 * n + 4 * i + 9,", "8 * n + 4 * i + 7,"), ("8 * n + 4 * i + 10,", "8 * n + 4 * i + 8,")]:
            assert s.count(a) == 1, a
            s = s.replace(a, b)
    ns = {"__name__": "t66mod", "__file__": "docs/lit/T66-depth-check.py"}
    exec(compile(s, "t66", "exec"), ns)
    return ns
for shift in (0, 1):
    ns = load(shift)
    for n in range(lo, hi + 1):
        g, start, names = ns["lmcs"](n)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            ns["run"]("lmcs", n, c)
        out = " ".join(buf.getvalue().split())
        print(("FIG4 " if shift else "TAB4 ") + f"N {n} distinct prios {len(set(g.prio))} of {g.n} | " + out[:230])
