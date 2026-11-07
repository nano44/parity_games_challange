"""L-RED 54 R217: apply an E-DOM priority state (order/par) to switchallexp G_n (shared by edomclimb.py / edomcomp.py)."""
def apply(V, order, par):
    # order: list of names (non-m, non-p) low -> high; then m's in order 'morder'; p on top
    nmv = {v[4]: v for v in V}; newp = {}; cur = -1
    for nm in order["low"] + order["m"]:
        if nm not in nmv: continue
        p = par.get(nm, nmv[nm][1] % 2); cur += 1
        if cur % 2 != p: cur += 1
        newp[nm] = cur
    top = cur + 2 + (cur % 2); newp["p"] = top if nmv["p"][1] % 2 == 0 else top + 1
    return [(v[0], newp[v[4]], v[2], v[3], v[4]) for v in V]
