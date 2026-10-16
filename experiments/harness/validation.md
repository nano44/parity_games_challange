# Harness validation run (2026-10-14)
Corpus: 2000 own games (`gen.py corpus out/own 2000 11 --nmax 150`, n in 1..150) + 1000 Oink rngame games
(`rngame_corpus.sh out/rn 1000 120`; rngame is not reproducible from parameters). Reference: oink-uzlk. Timeout 30 s per run.
Oink 8fbf0a7, single worker. 36 solvers x 3000 games.

| solver(s) | agree with uzlk | timeout | wrong |
| --- | --- | --- | --- |
| py-zlk (independent) | 3000 | 0 | 0 |
| oink bqpt bsspm dp dtl fpi fpj fpjg idtl npp ortl pmtl pp ppp ppq psi ptl rr rrdp rtl spm spptl ssi tl tlq zlk zlkpp-liv zlkpp-std zlkpp-waw zlkq | 3000 each | 0 | 0 |
| oink gpm | 2978 | 22 | 0 |
| oink qpt | 2995 | 5 | 0 |
| oink sspm | 2971 | 29 | 0 |
| oink tspm | 2999 | 1 | 0 |
| **oink mspm** | 2983 | 12 | **5**: 4 crashes (`logic error` at mspm.cpp:486), 1 wrong region rejected by Oink's own verifier ("loser can escape") |

Verdict: the harness and the reference agree with 34 of 35 other solvers on every game that finished; Oink's mspm is
unsound at 8fbf0a7 (instances: `regressions/mspm_*.pg`; reproduce with `oink --mspm -v -w 1 FILE`).
