# N6 (IPM on the P-matrix LCP of the induced discounted game): code and results. Write-up: docs/new/N6-ipm.md.
- n6.py: binarisation, Jurdzinski weights, gamma = beta_G, HIJ (1304.1888) Def. 16 LCP, path following in arb arithmetic.
  Default track() (N6PATH=central | weighted). Env switches used in the write-up: N6GINV (other discount, experiments only), N6PRECF
  (precision factor), N6PROX (neighbourhood), N6FGAP (closest mu-factor to 1), N6TFAC (centring target step), N6DBG / N6LIM
  (diagnostics), N6ALG=ipm (the older Mehrotra-type variant with infeasible / big-M starts; jams, kept for the record).
- gen_hij.py: parity game on HIJ's kappa-extremal arena G_n.
- bench.sh: family sweeps -> results/<family>.<mode>.csv; each produced solution checked by ../check_sol2.py (Oink zlk regions,
  harness/verify.py strategies). results/random.central.csv: 40 random games (gen.py n n 1 4 seed, seeds 20261023..20261062).
- Killing instance: ../instances/n6/counter_ortl-3.pg (sha1 c8bc349942b32305edee56ba8fb7d6504ed86622); also tc-4.pg (sha1 d92e89fa…).
