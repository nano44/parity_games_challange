import sys, os, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "so"))
import kw18, sox
for f in sys.argv[1:]:
    try: g = sox.load(f)
    except Exception: continue
    if len(sox.oddchoice(g)) != 1: continue
    acc = {}
    with contextlib.redirect_stdout(io.StringIO()): kw18.analyse(g, acc, f)
    if acc.get("U3x_kindchange_transitions", 0) or acc.get("CW_switches", 0): print(f, g.n, acc.get("U3x_kindchange_transitions"), acc.get("CW_switches"), acc.get("DIR_kindchanges_at_wflat"), acc.get("KM_postfreeze_kindchanges"), flush=True)
