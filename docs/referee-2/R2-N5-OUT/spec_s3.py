#!/usr/bin/env python3
"""Attribution: out_check on the SPEC trace (experiments/new/n5.py via re_check.n5_spec) from the S3 start only, over a list of files,
to compare with the lane's fbsplit.py numbers (same trace). Usage: spec_s3.py list.txt [extra.pg ...]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import out_check as OC
FC, RC = OC.FC, OC.RC
st = OC.Stats(); R = os.path.join(HERE, "..", "..", "..")
files = [l.strip() for l in open(sys.argv[1]) if l.strip()] + sys.argv[2:]
for f in files:
    try: g = RC.parse(open(os.path.join(R, f)).read())
    except Exception: st.c["skipped_unparsable"] += 1; continue
    if len([v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]) != 1: st.c["skipped_not_C1O"] += 1; continue
    o = FC.odd_vertex(g); s, t = FC.s3_start(g)
    A, fbs = OC.run_trace(g, o, s, t, None, "spec"); OC.check_run(g, o, A, fbs, st, f"spec-s3:{os.path.basename(f)}")
print("TRACE spec, S3 start only"); FC.report(st)
