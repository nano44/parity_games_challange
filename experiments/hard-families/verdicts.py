"""Hand-written verdicts per family, from results/*.csv (sweep of 2026-10-14, 20 s timeout per run, one worker).
b = fitted growth base of the solver's work counter per +1 in N over the last finished sizes (see README tables)."""
NOTE = (" Positional strategies were not checked in this sweep (the check was added to sweep.py during it); "
        "a re-run with strategy checks is pending.")
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
    "counter_qpt": "BLOW-UP OBSERVED, TYPE OPEN. With preprocessing off, qpt's lifts grow fast (work ~ n^5.2 between "
                   "N = 2 and 16, 975553 lifts at N = 16; timeout at N = 32), sizes were doubled so the growth type "
                   "(polynomial of high degree vs super-polynomial) is not determined; needs N = 16..32 step 1. "
                   "Contrast zlk, tl constant; sspm ~ n^2. Oink with default preprocessing solves the family outright.",
    "recursiveladder": "CONFIRMED (on the Python port). Zielonka grows by b = 1.618 per +1 in N in Oink uzlk/zlk/zlkpp-std "
                       "and in the independent py-zlk (44.8M iterations at N = 34); contrast tl (~linear) and psi (constant) up to N = 38.",
    "switchallexp": "NOT CONFIRMED: the targeted algorithm (PGSolver's switch-all strategy improvement) was not run "
                    "(PGSolver binaries blocked; port of stratimpralgs.ml queued). Oink's psi grows ~linearly (132 major "
                    "iterations at N = 64) and ssi, zlk, tl are constant: the family does not hurt them.",
    "switchbestexp": "NOT CONFIRMED: targeted algorithm (PGSolver's switch-best SI) not run, as for switchallexp. "
                     "Oink psi ~ linear (390 at N = 64); ssi, zlk, tl constant; py-zlk grows mildly (b = 1.47 over N = 2..16, "
                     "it then timed out on these sizes because of Python recursion cost).",
}
VERDICTS = {k: v + NOTE for k, v in VERDICTS.items()}
