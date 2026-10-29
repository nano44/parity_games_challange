#!/usr/bin/env python3
"""Box 22: on fcN (S3 start): N5-SF on L-COMP's engine (sfb.py): iterations, fallbacks, SBC_σ, SBC_τ, regions vs Oink zlk; N5 on n5b
(SPEC): iterations, fallbacks; optional --xcheck: n5sf.py's state sequence must equal sfb's. Usage: run22.py [--xcheck] GAME.pg ..."""
import hashlib, json, os, subprocess, sys, tempfile, time
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(EXP, "n5-second"))
import sfb, sfxcheck, pg, n5b
OINK = os.path.join(EXP, "..", "tools", "oink", "build", "oink")
a = sys.argv[1:]; xc = a[0] == "--xcheck"; a = a[1:] if xc else a
for path in a:
    t0 = time.time(); g = pg.read(path); sha = hashlib.sha1(open(path, "rb").read()).hexdigest()
    r = sfb.run(g); t1 = time.time()
    with tempfile.TemporaryDirectory() as td:
        subprocess.run([OINK, "--zlk", "-w", "1", path, td + "/s"], capture_output=True, check=True); ref = pg.read_sol(open(td + "/s").read(), g.n)
    win, strat, it5, fb5 = n5b.N5(g, mode="spec").run(); t2 = time.time()
    row = dict(game=os.path.basename(path), sha1=sha[:12], n=g.n, start="S3", sf_it=r["it"], sf_fb=r["fb"], sbc_sigma=r["sbc_sigma"], sbc_tau=r["sbc_tau"],
               sf_regions_eq_oink=(r["win"] == list(ref)), n5_it=it5, n5_fb=fb5, n5_regions_eq_oink=(win == list(ref)), sf_s=round(t1 - t0), n5_s=round(t2 - t1))
    if xc:
        ok, _ = sfxcheck.cmp(g, None); row["n5sf_equal"] = ok
    print("ROW", json.dumps(row), flush=True)
