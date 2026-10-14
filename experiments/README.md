# Experiments
One folder per experiment: experiments/<name>/ with README.md (what, how to re-run, results), the scripts, and
an optional check.sh: a fast (< 2 min) deterministic self-check that scripts/verify.sh runs on every push.
Large outputs go to experiments/<name>/out/ (gitignored); summary tables and plots are committed.
