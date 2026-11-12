import sys, glob, re
for d in sys.argv[1:]:
    tot = {}; n = 0; mx = ("rec_Tmax", "rec_platmax", "rec_plat_len_max", "rec_win_maxlen", "rec_phivals_max", "rec_rh_changes_max")
    for f in glob.glob(d + "/*.out"):
        for l in open(f):
            if not l.startswith("TOTAL"): continue
            n += 1; t = l.replace("|", " ").split()
            for i in range(len(t) - 1):
                if re.fullmatch(r"\d+", t[i + 1]) and not re.fullmatch(r"\d+", t[i]):
                    k, v = t[i], int(t[i + 1])
                    tot[k] = max(tot.get(k, 0), v) if k in mx else tot.get(k, 0) + v
    fails = sum(v for k, v in tot.items() if k.endswith("fail"))
    print(d, "files", n, "runs", tot.get("runs"), "FAILSUM", fails, " ".join(f"{k} {v}" for k, v in sorted(tot.items()) if k.startswith("rec_") or k == "capped"))
