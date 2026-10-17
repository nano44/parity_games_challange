"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), GAP-C candidate (NODUP): in an A_DTL run, extractTangles never
meets an SCC equal to a stored tangle (the duplicate check dtl.cpp 385-424 never fires). With DTL-proof.md §2.3 K2/K6, a
duplicate at a closed lowest region is exactly shape (beta'). Counts duplicate-check hits on the given games and on
random games (gen.random_game, n in [nmin, nmax]); DTL_ORDER = oink | stable. Usage: dtl_nodup.py [count seed nmin nmax] [G.pg ...]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, gen, dtl_spp as P

class CL(list):
    hits = 0
    def __contains__(self, x):
        r = list.__contains__(self, x)
        if r: CL.hits += 1
        return r

def run_counting(g):
    d = P.build(g); d.tkeys = CL(); h0 = CL.hits
    while d.G:
        d.iterations += 1
        if not d.search(0): break
    while d.G:
        d.iterations += 1
        if not d.search(1): break
    return CL.hits - h0, d

if __name__ == "__main__":
    sys.setrecursionlimit(100000); a = sys.argv[1:]; files = [x for x in a if x.endswith(".pg")]; nums = [x for x in a if not x.endswith(".pg")]
    nf = sum(run_counting(pg.read(f))[0] > 0 for f in files)
    if files: print(f"{len(files)} files: games with a duplicate-check hit {nf}, total hits {CL.hits}")
    if nums:
        cnt, seed, nmin, nmax = map(int, nums); bad = 0; inc = 0
        for k in range(cnt):
            n = nmin + k % (nmax - nmin + 1); g = gen.random_game(n, n, 1, 3, seed + k); h, d = run_counting(g)
            if h: bad += 1; print("DUPLICATE in random game seed", seed + k, "n", n, flush=True) if bad <= 3 else None
            if d.G: inc += 1; print("INCOMPLETE random game seed", seed + k, "n", n, flush=True)
        print(f"random games {cnt} (n {nmin}..{nmax}, order {os.environ.get('DTL_ORDER', 'stable')}): with a duplicate hit {bad}, incomplete {inc}")
