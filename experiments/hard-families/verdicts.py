"""Hand-written verdicts per family, from results/*.csv (sweep of 2026-10-14, 20 s timeout per run, one worker).
b = fitted growth base of the solver's work counter per +1 in N over the last finished sizes (see README tables)."""
NOTE = (" Re-run 2026-10-14 with positional-strategy checks (harness/verify.py): every finishing solver's "
        "strategies verified, no disagreement.")
VERDICTS = {
    "tc": "CONFIRMED. Exponential for the targets: tl, zlk, uzlk, rr, dp grow by b = 2.00 per +1 in N (fpi 1.92, "
          "tspm 2.74, zlkq 2.23 over shorter ranges; zlkq is claimed quasi-polynomial by Oink, which our range cannot "
          "separate from exponential). Contrast rtl and psi stay polynomial (b = 1.04, work ~ n^0.5) up to N = 32 (3232 vertices).",
    "tc+": "CONFIRMED. rtl (the target) and tl grow by b = 1.98, zlk by 2.00; contrast ortl (b = 1.10) and psi (1.08) "
           "stay polynomial (psi times out only at N = 32, 33984 vertices).",
    "counter_symsi": "CONFIRMED. ssi (the target) grows by b = 2.00 per +1 in N (152924 major iterations at N = 18, "
                     "timeout after); uzlk also blows up (3.04). Contrast psi is constant (11 major iterations) and tl ~ linear up to N = 40.",
    "counter_rr": "CONFIRMED. rr (the target) grows by b = 1.618 (Fibonacci-like), as does zlk; rrdp grows slowly "
                  "(b = 1.06); contrast tl and psi are constant (2 and 6) up to N = 40.",
    "counter_dp": "CONFIRMED. dp (the target) and pp grow by b = 2.07; zlk by 1.62; contrast tl (~linear) and psi (constant) up to N = 40.",
    "counter_m": "CONFIRMED for the priority-promotion family as measured (pp, dp, rr: b = 1.61; zlk 1.62); the source "
                 "names no target. Contrast tl and psi constant up to N = 40.",
    "counter_core": "CONFIRMED. The Zielonka variants blow up: uzlk b = 3.64, zlkpp-std 2.85, zlk 2.62, py-zlk 3.66. "
                    "Contrast tl (~linear) and psi (constant) up to N = 40.",
    "counter_rob": "CONFIRMED. As counter_core: uzlk b = 3.67, zlkpp-std 2.90, zlk 2.62, py-zlk 3.74; contrast tl and psi polynomial.",
    "counter_ortl": "CONFIRMED. ortl (the target) grows by b = 2.00 (2048 iterations at N = 12, then timeout); contrast rtl, tl (2 iterations) and psi (6) constant up to N = 40.",
    "counter_qpt": "SUPER-POLYNOMIAL JUMPS OBSERVED, CLASS OPEN. With preprocessing off, qpt's lifts jump at N = 8 "
                   "(x15 over N = 6) and N = 16 (x31 over N = 14), growing only ~N^3..N^4 in between (13.8M lifts at N = 28; "
                   "timeout at N = 32, the next power of two). The jumps at powers of two fit a counter over log N bits, i.e. "
                   "quasi-polynomial-type growth, but the data cannot fix the class. Contrast zlk, tl constant; sspm ~ n^2. "
                   "Oink with default preprocessing solves the family outright.",
    "recursiveladder": "CONFIRMED (on the Python port). Zielonka grows by b = 1.618 per +1 in N in Oink uzlk/zlk/zlkpp-std "
                       "and in the independent py-zlk (44.8M iterations at N = 34); contrast tl (~linear) and psi (constant) up to N = 38.",
    "switchallexp": "CONFIRMED against the targeted algorithm, run through Python ports: PGSolver's switch-all "
                    "strategy improvement (pgsolver_si.py, port of stratimpralgs.ml; bare SI loop, without PGSolver's "
                    "universal_solve preprocessing) takes 11, 31, 71, 151, 311, 631, 1244, 2487, 4973, 9928 iterations for "
                    "N = 1..10 (doubling per N; table switchallexp-pgs below). Oink's psi grows ~linearly (24 major iterations "
                    "at N = 10, 132 at N = 64), ssi, zlk, tl are constant: the family does not hurt them.",
    "switchbestexp": "CONFIRMED against the targeted algorithm, run through Python ports: PGSolver's switch-best "
                     "strategy improvement (pgsolver_si.py --switchbest; port of switch_globally_best.ml with the alternating "
                     "and cheap-escape transformations; bare SI loop) takes 23, 61, 137, 289, 593, 1201 iterations for N = 1..6 "
                     "(doubling; table switchbestexp-pgsbest below). Oink psi ~linear (390 at N = 64); ssi, zlk, tl constant.",
}
VERDICTS = {k: v + NOTE for k, v in VERDICTS.items()}
