#!/usr/bin/env python3
"""Set c: the 13 M1 hard families at the sizes L-COMP reproduced (experiments/hard-families/run_all.sh; M1 DONE 2026-10-14),
plus counter_m N = 41, 42 (the CLAUDE.md trap: Oink --zlk aborts there; reference --tl). Writes MANIFEST.tsv.
The instances are NOT stored: M1 never froze them as files (sweep.py regenerates them on every run). Each manifest line gives
the generator (Oink's generator binary at the pinned commit 8fbf0a7, or experiments/hard-families/pgsolver_port.py) and the
sha1 of its output; the battery regenerates into its cache and checks the pin.
ref: zlk when `oink --zlk -v` verifies the instance within ZLKBUDGET seconds, else tl (must verify)."""
import os, sys, subprocess, hashlib, tempfile, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
O = os.path.join(ROOT, "tools", "oink", "build"); PORT = os.path.join(ROOT, "experiments", "hard-families", "pgsolver_port.py")
ZLKBUDGET = 20
C40 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 28, 32, 40]; C32 = C40[:-1]
FAMS = [("tc", "oink", C32), ("tc+", "oink", C32), ("counter_symsi", "oink", C40), ("counter_rr", "oink", C40), ("counter_dp", "oink", C40),
        ("counter_m", "oink", C40 + [41, 42]), ("counter_core", "oink", C40), ("counter_rob", "oink", C32), ("counter_ortl", "oink", C40),
        ("counter_qpt", "oink", [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 32, 64, 128]),
        ("recursiveladder", "pgsolver", [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 34, 38]),
        ("switchallexp", "pgsolver", [1, 2, 4, 8, 16, 32, 64]), ("switchbestexp", "pgsolver", [1, 2, 4, 8, 16, 32, 64])]
out = ["# set c: the 13 M1 hard families (experiments/hard-families; sizes of run_all.sh) + counter_m 41, 42 (zlk trap, reference tl).",
       "# gen: 'oink <generator> <N>' = tools/oink/build/<generator> <N> (Oink 8fbf0a7); 'pgsolver <family> <N>' = experiments/hard-families/pgsolver_port.py <family> <N>.",
       "# family\tparam\tfile\tsha1\tkind\tref\tgen"]
for fam, tool, sizes in FAMS:
    for N in sizes:
        cmd = [os.path.join(O, fam), str(N)] if tool == "oink" else [sys.executable, "-B", PORT, fam, str(N)]
        data = subprocess.run(cmd, capture_output=True, check=True).stdout
        assert data.startswith(b"parity"), (fam, N, data[:60])
        fd, p = tempfile.mkstemp(suffix=".pg"); os.write(fd, data); os.close(fd); ref = None; note = ""
        for s, budget in (("zlk", ZLKBUDGET), ("tl", 300)):
            t0 = time.time()
            try: r = subprocess.run([os.path.join(O, "oink"), "--" + s, "-v", p], capture_output=True, text=True, timeout=budget); ok = r.returncode == 0 and "solution verified" in r.stdout + r.stderr; rc = r.returncode
            except subprocess.TimeoutExpired: ok = False; rc = "timeout"
            note += " %s rc %s %.1fs" % (s, rc, time.time() - t0)
            if ok: ref = s; break
        os.remove(p); assert ref, (fam, N, note)
        print(fam, N, "n", data.split(b";")[0].decode(), "ref", ref, note, flush=True)
        out.append("%s\t%d\t%s_%d.pg\t%s\tfit\t%s\t%s %s %d" % (fam, N, fam, N, hashlib.sha1(data).hexdigest(), ref, tool, fam, N))
open(os.path.join(HERE, "MANIFEST.tsv.new"), "w").write("\n".join(out) + "\n"); os.replace(os.path.join(HERE, "MANIFEST.tsv.new"), os.path.join(HERE, "MANIFEST.tsv"))
print("wrote", len(out) - 3, "instances")
