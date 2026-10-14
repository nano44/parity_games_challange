# Harness validation run (2026-10-14)
Corpus: 2000 own games (`gen.py corpus out/own 2000 11 --nmax 150`) + 1000 Oink rngame games
(`rngame_corpus.sh out/rn 1000 120`; not reproducible from parameters). Reference: oink-uzlk. Timeout 30 s per run.

| solvers | status |
| --- | --- |
| oink-tl, tlq, zlk, zlkpp-liv, zlkpp-std, zlkpp-waw, zlkq | agree with uzlk on all 3000 |
| oink-tspm | agrees on 2999, 1 timeout |
| py-zlk and the remaining 26 Oink solvers | IN PROGRESS (this file is updated when the run ends) |
| oink-mspm | UNSOUND at 8fbf0a7: so far 3 crashes (logic error, mspm.cpp:486) and 1 wrong answer that Oink's own verifier rejects ("loser can escape"); instances in `regressions/` |
