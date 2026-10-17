"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 7): write the union game number IDX of dtl_step5stats.games (same
env: UNIONS, SEED, UM_CROSS, NMAX; same file list) to OUT.pg, so a union hit can be re-run as a plain instance.
Usage: UNIONS=k SEED=s UM_CROSS=c NMAX=m dtl_union_dump.py IDX OUT.pg G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_step5stats as ST

if __name__ == "__main__":
    idx, out = int(sys.argv[1]), sys.argv[2]
    for name, g in ST.games(sys.argv[3:]):
        if name == f"union{idx}":
            pg.write(g, out); print("wrote", out, "n", g.n); break
    else:
        print("union", idx, "not generated"); sys.exit(1)
