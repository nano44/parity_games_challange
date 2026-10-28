#!/usr/bin/env python3
"""Box 16 tables from results/*.json (box16.py): run table, per-phase table, least-squares fits of iterations and longest phase in n
(linear a*n+b, and the log-linear base b of b^n), per start family.  Usage: table.py"""
import glob, json, math, os
HERE = os.path.dirname(os.path.abspath(__file__))
R = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(HERE, "results", "H*.json")))]
R.sort(key=lambda d: (d["mode"], d["name"].split("_")[1], d["n"]))
print("| run | n | V | sha1 | start sha1 | it | fb | phases | longest | τ ch | λ_Ξ ch | λ_W ch | max N_ep | max NCONF | max ALT | Σ ALT | viol | checks |")
print("| --- " * 18 + "|")
for d in R:
    P = d["phases_detail"]
    print(f"| {d['name']} | {d['n']} | {d['V']} | {d['sha1'][:8]} | {d['start_sha1'][:8]} | {d['it']} | {d['fb']} | {d['phases']} | {d['longest']} | "
          f"{d['tau_changes']} | {d['lamXi_changes']} | {d['lamW_changes']} | {max(p['N_ep'] for p in P)} | {max(p['NCONF'] for p in P)} | "
          f"{max(p['ALT'] for p in P)} | {sum(p['ALTsum'] for p in P)} | {len(d['viol'])} | {'OK' if d['ok'] else 'FAIL'} |")


def fit(xs, ys):
    n = len(xs); mx = sum(xs) / n; my = sum(ys) / n
    a = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    res = max(abs(y - (a * x + my - a * mx)) for x, y in zip(xs, ys))
    return a, my - a * mx, res


print("\n| start | mode | n range | it ≈ a·n + b (max residual) | longest ≈ a·n + b (max residual) | base of it ~ c^n (last two n) | base of longest |")
print("| --- " * 7 + "|")
fam = {}
for d in R:
    fam.setdefault((d["name"].split("_")[1], d["mode"]), []).append(d)
for (s, mode), ds in sorted(fam.items()):
    if len(ds) < 3:
        continue
    ds.sort(key=lambda d: d["n"]); xs = [d["n"] for d in ds]
    a1, b1, r1 = fit(xs, [d["it"] for d in ds]); a2, b2, r2 = fit(xs, [d["longest"] for d in ds])
    x0, x1 = ds[-2], ds[-1]
    c1 = (x1["it"] / x0["it"]) ** (1 / (x1["n"] - x0["n"])); c2 = (x1["longest"] / x0["longest"]) ** (1 / (x1["n"] - x0["n"]))
    print(f"| {s} | {mode} | {xs[0]}..{xs[-1]} | {a1:.3f} n + {b1:.2f} ({r1:.2f}) | {a2:.3f} n + {b2:.2f} ({r2:.2f}) | {c1:.4f} | {c2:.4f} |")

print("\nPer phase (F and S3 starts, mode fig): len/end/ntau/dW/f/N_ep/NCONF/NCONF2/S/ALT/SBG/max|D|")
for d in R:
    if d["mode"] != "fig" or d["name"].split("_")[1] not in ("F", "S3"):
        continue
    print(f"- {d['name']}: " + "; ".join(f"#{p['p']} {p['len']}/{p['end']}/{p['ntau']}/{p['dW']}/{p['f']}/{p['N_ep']}/{p['NCONF']}/{p['NCONF2']}/{p['S']}/"
                                       f"{p['ALT']}/{p['SBG']}/{p['D']}" for p in d["phases_detail"]))
