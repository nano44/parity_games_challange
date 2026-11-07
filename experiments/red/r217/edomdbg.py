import sys, json, runpy
import fried, comp
from edomprio import apply
n, sf = int(sys.argv[1]), sys.argv[2]; d = json.load(open(sf)); V = apply(fried.game(n), d["order"], d["par"])
fried.game = lambda m: V; comp.game = lambda m: V
sys.argv = ["fdbg.py", str(n)] + sys.argv[3:]; runpy.run_path("fdbg.py", run_name="__main__")
