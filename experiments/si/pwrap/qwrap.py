#!/usr/bin/env python3
"""L-SI packet P-N5-WRAP: every «…» of docs/si/P-N5-WRAP.md that the template marks {{ID}} is COPIED BY THIS SCRIPT from its source at
a pinned commit (git show SHA:PATH): the text between a start and an end anchor (both included), line breaks and the indentation after
them joined to one space; never retyped. Sources: trunk 7fa6aff4 (SPEC docs/new/N5-ssi-global.md, docs/new/P-N5-XICYC.md,
docs/RESULTS.md) and REFEREE 33's pre-read (claude/referee e44ce56b / 90703a81, docs/referee/R-WRAP-preread.md).
Usage: qwrap.py src | build TEMPLATE | json | doc DOC.md   (as experiments/si/box104/addC104.py; doc mode reads out/qwrap.json, no git)"""
import sys, re, subprocess, hashlib, textwrap
SRC = "docs/referee/R-WRAP-preread.md"
SPEC = "docs/new/N5-ssi-global.md"
XICYC = "docs/new/P-N5-XICYC.md"
R33 = "e44ce56bf"        # claude/referee, REFEREE s33: R-WRAP-preread
R33A = "90703a810"       # claude/referee, REFEREE s33: R-WRAP-preread Addendum 1 (n = 8 row)
TRUNK = "7fa6aff4a"      # claude/vibrant-johnson-nxvvxo (docs/RESULTS.md)
RES = "docs/RESULTS.md"
ITEMS = [  # (id, commit, start anchor, end anchor[, path]); trunk items are quoted again inside RESULTS: first occurrence
 ("S1-rank", TRUNK, "injective priorities: rank(v) = position of v", "p'(v) = 2·rank(v) + (Ω(v) mod 2).", SPEC),
 ("S1-val", TRUNK, "valuation of v under (σ, σ̄): (c, P, ℓ)", "ℓ = number of steps to reach c.", SPEC),
 ("S1-ord", TRUNK, "order (better for Even): compare reward of c", "if c even, shorter is better.", SPEC),
 ("S1-xi", TRUNK, "Ξσ = valuation of every vertex under σ", "(minimising this order at every vertex at once).", SPEC),
 ("S1-dual", TRUNK, "Odd's side: everything on the DUAL game G^d", "Iτ computed there.", SPEC),
 ("S2", TRUNK, "S2 Improving edges:", "Iτ the same on G^d for τ.", SPEC),
 ("S4", TRUNK, "S4 Iteration (one iteration", "applied together):", SPEC),
 ("S4a", TRUNK, "a. If Iσ ≠ ∅: A(v) = {σ(v)}", "Else σ_new = σ.", SPEC),
 ("S4b", TRUNK, "b. If Iτ ≠ ∅: A(v) = {τ(v)}", "Else τ_new = τ.", SPEC),
 ("S4c", TRUNK, "c. FALLBACK, if σ_new = σ", "Count it.", SPEC),
 ("S5", TRUNK, "S5 Stop when Iσ = Iτ = ∅.", "S5 Stop when Iσ = Iτ = ∅.", SPEC),
 ("FIX1", TRUNK, "FIX 1 (S3, A2).", "largest index if Ω(w) odd, smallest if even.", SPEC),
 ("FIX3", TRUNK, "FIX 3 (S4c, A7).", "Odd falls back only if Iσ = ∅.", SPEC),
 ("N5XI", TRUNK, "SPEC S1-S5 with ONE change in", "Here A(v) = {σ(v)} ∪ Iσ(v).", XICYC),
 ("1E-N3", TRUNK, "used in two forms: S1's σ̄, and τ̄ on the dual game, are pointwise optima;", "is a pointwise optimum of that arena, before S4c)", RES),
 ("DUAL-a", TRUNK, "«The order of G^d is the REVERSE of the order of Γ»", "«and τ̄ maximises Γ's order at every vertex.»", RES),
 ("R15-a", TRUNK, "(a) Lemma A: for any non-empty unambiguous set I of improvements of σ", "Ωσ ⊴ Ω_{Switch_I(σ)}.", RES),
 ("R15-c", TRUNK, "(c) Theorem: with φ(σ) = Σ_{v ∈ M⊕", "|φ| ≤ n(n−1).", RES),
 ("R15-d", TRUNK, "(d) N5: every iteration applies Switch_I", "(two potentials φ, φ^d).", RES),
 ("RULE", TRUNK, "with RESULTS R24 (a) Lemma R and R24 (b)'s choice rule (TB proof steps 1, 3-5; fixes §2.3) with RESULTS R103's bridge B, whose proof uses no", "(RESULTS R103's (R1) ruling)", RES),
 ("NT", R33, "(T-2) **Claim NT (no tie on a 1-sink game; mine).**", "against Sink Seeking. ∎"),
 ("T-3", R33, "(T-3) G_n with ι_(G_n) is a 1-sink game", "between Table 4 and Figure 4."),
 ("T-4", R33, "(T-4) Every strategy σ of an improvement run from ι", "never invoked on G_n."),
 ("STATUS", R33, "Status. Claim NT and (T-4) are referee-originated", "I would sign them."),
 ("F-1", R33, "F-1 (the game; READING, stated by the box, confirmed here).", "(it does, §5.1 and §6)."),
 ("F-2", R33, "F-2 (the count).", "above 2^n."),
 ("F-3", R33, "F-3 (wording).", "should read «in n» or «super-polynomial» here."),
 ("W-2", R33, "W-2 (required): the Definition says only", "«SPEC's choice, then the larger index»."),
 ("REPLAY", R33, "No FALSE statement found; no instance against any step.", "on the lane's frozen instances."),
 ("A1", R33A, "So on my wrapper of my transcription of G_8", "all 18 counters 0."),
]

def norm(s):
    return re.sub(r"\n[ \t]*", " ", s)

def extract(text, a, b, uniq=True):
    i = text.find(a)
    if i < 0 or (uniq and text.find(a, i + 1) >= 0):
        raise SystemExit("start anchor not found exactly once: " + a[:60])
    j = text.find(b, i)
    if j < 0:
        raise SystemExit("end anchor not found after start: " + b[:60])
    return norm(text[i:j + len(b)])

def items():
    cache, out = {}, {}
    for it in ITEMS:
        k, c, a, b = it[:4]; path = it[4] if len(it) > 4 else SRC
        if (c, path) not in cache:
            cache[(c, path)] = subprocess.run(["git", "show", c + ":" + path], capture_output=True, check=True).stdout.decode()
        s = extract(cache[(c, path)], a, b, path == SRC)   # trunk premises are quoted again inside RESULTS: first occurrence
        if path == SRC and norm(cache[(c, path)]).count(s) != 1:
            raise SystemExit("item not unique in its source: " + k)
        out[k] = (c, s)
    return out

def wrap(s, ind):
    lines = textwrap.wrap(s, width=134, initial_indent=ind, subsequent_indent=" " * len(ind), break_long_words=False,
                          break_on_hyphens=False)
    assert norm("\n".join(lines)).strip() == (ind + s).strip(), "lossy wrap"
    return lines

def main():
    if sys.argv[1] == "src":
        for k, (c, s) in items().items():
            print("QWRAP %s OK %s %s %d chars" % (k, c, hashlib.sha1(s.encode()).hexdigest()[:12], len(s)))
    elif sys.argv[1] == "build":
        it = items()
        for line in open(sys.argv[2], encoding="utf-8").read().split("\n"):
            if "{{" in line:
                ind = re.match(r"\s*(?:- )?", line).group(0)
                body = re.sub(r"\{\{([A-Za-z0-9-]+)\}\}", lambda m: "«" + it[m.group(1)][1] + "»", line[len(ind):])
                print("\n".join(wrap(body, ind)))
            else:
                print(line)
    elif sys.argv[1] == "doc":
        d = norm(open(sys.argv[2], encoding="utf-8").read())
        it = items() if len(sys.argv) > 3 and sys.argv[3] == "git" else None
        if it is None:
            import json, os
            it = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "out", "qwrap.json"), encoding="utf-8"))
            it = {k: (v[0], v[1]) for k, v in it.items()}
        miss = [k for k, (c, s) in it.items() if s not in d]
        print("QWRAP doc items %d missing %d %s" % (len(it), len(miss), " ".join(miss)))
        sys.exit(1 if miss else 0)
    elif sys.argv[1] == "json":
        import json
        print(json.dumps({k: [c, s] for k, (c, s) in items().items()}, ensure_ascii=False, indent=0))

if __name__ == "__main__":
    main()
