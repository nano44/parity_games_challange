import sys, os, io, contextlib, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "so"))
import kw18, sox
for f in sys.argv[1:]:
    try: g = sox.load(f)
    except Exception: continue
    if len(sox.oddchoice(g)) != 1: continue
    acc = {}
    with contextlib.redirect_stdout(io.StringIO()): kw18.analyse(g, acc, f)
    print(f, g.n, acc.get("FRZU_margin_changed"), acc.get("KWF_margin_changed"), acc.get("KWF_margin_r_changed"), acc.get("RUN_len"), flush=True)
