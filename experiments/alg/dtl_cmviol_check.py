"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4), GAP-A-M §18i: candidate (CM) FAILS in an actual A_DTL run.
instances/cm_viol_oink_n28.pg (dtl_cmclimb.py seed 301 from instances/h4_def9_oink_n28.pg; pinned Oink 9 iterations,
verified). Search 5 -> 6 of one phase: depth-0 piece 0 makes a DEF change (same context, ideal result unchanged, actual -1
return set grows), so piece 1's context SHRINKS (27 -> 24 vertices); piece 1's ideal (C6) result is stable in both
searches, and the child's actual round count M DROPS 7 -> 6 (7 common vertices die earlier). Checked in both order data.
Exit 0 iff reproduced. Usage: dtl_cmviol_check.py"""
import sys, os, importlib, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
ok = True
for order in ("oink", "stable"):
    os.environ["DTL_ORDER"] = order
    import dtl_pyref, dtl_deficit, dtl_regvec, dtl_childM
    for m in (dtl_pyref, dtl_deficit, dtl_regvec, dtl_childM): importlib.reload(m)
    sys.argv = ["dtl_childM.py", os.path.join(HERE, "instances", "cm_viol_oink_n28.pg")]
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(compile(open(os.path.join(HERE, "dtl_childM.py")).read(), "dtl_childM.py", "exec"), {"__name__": "__main__", "__file__": os.path.join(HERE, "dtl_childM.py")})
    out = buf.getvalue()
    good = "'M_drop': 1" in out and "('cm_viol_oink_n28.pg', 5, 1, 27, 24, 7, 6, 7)" in out
    print(f"order {order}: {out.splitlines()[0]} -> {'CM-VIOLATION REPRODUCED' if good else 'NOT reproduced'}")
    ok &= good
sys.exit(0 if ok else 1)
