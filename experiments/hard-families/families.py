"""Metadata for the M1 hard families: source (repo, file, commit), the solvers each family targets, contrast solvers.
Paper references are as given in the source repositories; all are 'awaiting source' until L-LIT opens them."""
OINK = "github.com/trolando/oink @ 8fbf0a7c3e5b0baa254cb4516258c5c42fa99db1"
PGS = "github.com/tcsprojects/pgsolver @ d3cd624b61cd66739c45aff9554f6bbdcdd05401"
F = {
    "tc": dict(src=f"{OINK}, src/tools/tc.cpp", gen="tools/oink/build/tc N",
               claim="Oink README.md:199-219: 'Two binary counters ... exponential lower bound for many algorithms' "
                     "(TL, FPI/FPJ/FPJG, NPP/PP/PPP/DP/RRDP, ZLK/UZLK/ZLKPP-STD, TSPM/SPM/MSPM); quasi-polynomial for "
                     "ZLKQ/ZLKPP-WAW/ZLKPP-LIV/SSPM/QPT; polynomial for RTL/ORTL/PTL/SPPTL/DTL/IDTL/PSI",
               paper="T. van Dijk, A Parity Game Tale of Two Counters, GandALF 2019, doi:10.4204/EPTCS.305.8 (awaiting source)",
               targets=["oink-tl", "oink-zlk", "oink-uzlk", "oink-rr", "oink-dp", "oink-fpi", "oink-tspm", "oink-zlkq"],
               contrast=["oink-rtl", "oink-psi"]),
    "tc+": dict(src=f"{OINK}, src/tools/tc+.cpp", gen="tools/oink/build/tc+ N",
                claim="Oink README.md:200: 'TC modified to defeat the RTL solver'",
                paper="none given in the repository (awaiting source)",
                targets=["oink-rtl", "oink-tl", "oink-zlk"], contrast=["oink-ortl", "oink-psi"]),
    "counter_symsi": dict(src=f"{OINK}, src/tools/counter_symsi.cpp", gen="tools/oink/build/counter_symsi N",
                          claim="Oink README.md:198 and counter_symsi.cpp:23: 'Matthew Maat's counterexample to Schewe et al's "
                                "symmetric strategy improvement'",
                          paper="M. Maat (no reference in the repository); Schewe et al. symmetric strategy improvement (awaiting source)",
                          targets=["oink-ssi"], contrast=["oink-psi", "oink-tl", "oink-uzlk"]),
    "counter_rr": dict(src=f"{OINK}, src/tools/counter_rr.cpp", gen="tools/oink/build/counter_rr N",
                       claim="Oink README.md:190: 'Counterexample to the RR solver'", paper="none given (awaiting source)",
                       targets=["oink-rr", "oink-rrdp"], contrast=["oink-tl", "oink-psi", "oink-zlk"]),
    "counter_dp": dict(src=f"{OINK}, src/tools/counter_dp.cpp", gen="tools/oink/build/counter_dp N",
                       claim="Oink README.md:191: 'Counterexample to the DP solver'", paper="none given (awaiting source)",
                       targets=["oink-dp", "oink-pp"], contrast=["oink-tl", "oink-psi", "oink-zlk"]),
    "counter_m": dict(src=f"{OINK}, src/tools/counter_m.cpp", gen="tools/oink/build/counter_m N",
                      claim="Oink README.md:192: 'Counterexample of Maciej Gazda, PhD Thesis, Sec. 3.5' (the solver it "
                            "targets is not named in the repository; measured: priority promotion family)",
                      paper="M. Gazda, PhD thesis, Sec. 3.5 (awaiting source)",
                      targets=["oink-pp", "oink-dp", "oink-rr"], contrast=["oink-tl", "oink-psi", "oink-zlk"]),
    "counter_core": dict(src=f"{OINK}, src/tools/counter_core.cpp", gen="tools/oink/build/counter_core N",
                         claim="Oink README.md:194: 'Counterexample of Benerecetti, Dell'Erba, Mogavero, Robust Exponential "
                               "Worst Cases for Divide-et-Impera Algorithms for Parity Games'",
                         paper="Benerecetti, Dell'Erba, Mogavero, GandALF 2017, doi:10.4204/EPTCS.256.9 (awaiting source)",
                         targets=["oink-uzlk", "oink-zlk", "oink-zlkpp-std"], contrast=["oink-tl", "oink-psi"]),
    "counter_rob": dict(src=f"{OINK}, src/tools/counter_rob.cpp", gen="tools/oink/build/counter_rob N",
                        claim="Oink README.md:195: 'SCC version of counter_core'", paper="as counter_core (awaiting source)",
                        targets=["oink-uzlk", "oink-zlk", "oink-zlkpp-std"], contrast=["oink-tl", "oink-psi"]),
    "counter_ortl": dict(src=f"{OINK}, src/tools/counter_ortl.cpp", gen="tools/oink/build/counter_ortl N",
                         claim="Oink README.md:197: 'Counterexample to the ORTL solver'", paper="none given (awaiting source)",
                         targets=["oink-ortl"], contrast=["oink-rtl", "oink-tl", "oink-psi"]),
    "counter_qpt": dict(src=f"{OINK}, src/tools/counter_qpt.cpp", gen="tools/oink/build/counter_qpt N",
                        claim="Oink README.md:193: 'Counterexample of Fearnley et al, An ordered approach to solving parity "
                              "games in quasi polynomial time and quasi linear space'",
                        paper="Fearnley, Jain, Schewe, Stephan, Wojtczak, SPIN 2017, doi:10.1145/3092282.3092286 (awaiting source)",
                        targets=["oink-qpt-raw", "oink-sspm-raw"], contrast=["oink-zlk-raw", "oink-tl-raw"]),
    "recursiveladder": dict(src=f"{PGS}, src/lib/generators/recursiveladder.ml (Python port: pgsolver_port.py)",
                            gen="python3 experiments/hard-families/pgsolver_port.py recursiveladder N",
                            claim="PGSolver registers it as 'Recursive Ladder Game' (recursiveladder.ml:48); the repository "
                                  "does not state the target; it is cited in the literature as Friedmann's lower bound for "
                                  "the recursive (Zielonka) algorithm (Lead brief; awaiting source)",
                            paper="O. Friedmann, recursive algorithm lower bound (awaiting source)",
                            targets=["oink-uzlk-raw", "oink-zlk-raw", "oink-zlkpp-std-raw"], contrast=["oink-tl-raw", "oink-psi-raw"]),
    "switchallexp": dict(src=f"{PGS}, src/lib/generators/policyiter/generators/switchallexp.ml (Python port)",
                         gen="python3 experiments/hard-families/pgsolver_port.py switchallexp N",
                         claim="switchallexp.ml:72: 'Exponential Lower Bound for (Voege's) switch-all rule' (PGSolver's "
                               "strategy improvement, src/lib/solvers/stratimpralgs.ml; not Oink's psi/ssi)",
                         paper="O. Friedmann, strategy-improvement lower bounds (awaiting source)",
                         targets=["PGSolver switchall SI (not run, see README)"], contrast=["oink-psi-raw", "oink-ssi-raw", "oink-zlk-raw", "oink-tl-raw"]),
    "switchbestexp": dict(src=f"{PGS}, src/lib/generators/policyiter/generators/switchbestexp.ml (Python port)",
                          gen="python3 experiments/hard-families/pgsolver_port.py switchbestexp N",
                          claim="ident 'switchbestexp'; its description string (line 79) repeats the switch-all text; target "
                                "presumably PGSolver's 'switchbest' SI (stratimpralgs/switch_globally_best.ml:119)",
                          paper="O. Friedmann, strategy-improvement lower bounds (awaiting source)",
                          targets=["PGSolver switchbest SI (not run, see README)"], contrast=["oink-psi-raw", "oink-ssi-raw", "oink-zlk-raw", "oink-tl-raw"]),
}
