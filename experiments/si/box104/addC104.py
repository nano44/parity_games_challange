#!/usr/bin/env python3
"""L-SI box 104 Addendum C (and packet P-N5-WRAP): the strings of REFEREE successor 33's pre-read of Lemma WRAP (docs/referee/R-WRAP-preread.md, claude/referee
e44ce56b, and its Addendum 1 at 90703a81) that Addendum C carries are COPIED BY THIS SCRIPT from the byte copies (git show SHA:PATH),
never retyped; so are four trunk premises (RESULTS R15 (a), (c), (d), R104's [RULE] clause; trunk 7fa6aff4): each item is the source text between a start anchor and an end anchor (both included), with line breaks and the
indentation after them joined to one space; each item must occur exactly once in its source.
Usage: addC104.py src                 (needs the two commits locally) one line per item: «ADDC104 <id> OK <sha1 of the item>» or FAIL
       addC104.py build TEMPLATE      (needs the commits) prints TEMPLATE with every «{{ID}}» replaced by «item ID»; a line with a
                                      placeholder is wrapped at 134 columns with its own indentation; asserts that the wrap is lossless
       addC104.py doc DOC.md          (no git) every item stands in DOC.md, verbatim up to line wrapping; one summary line"""
import sys, re, subprocess, hashlib, textwrap
SRC = "docs/referee/R-WRAP-preread.md"
R33 = "e44ce56bf"        # claude/referee, REFEREE s33: R-WRAP-preread
R33A = "90703a810"       # claude/referee, REFEREE s33: R-WRAP-preread Addendum 1 (n = 8 row)
TRUNK = "7fa6aff4a"      # claude/vibrant-johnson-nxvvxo (docs/RESULTS.md)
RES = "docs/RESULTS.md"
ITEMS = [  # (id, commit, start anchor, end anchor[, path])
 ("VERDICT-NT", R33, "**YES, and the item can be CLOSED in its second form", "the other referee checks it independently."),
 ("REPLAY", R33, "No FALSE statement found; no instance against any step.", "on the lane's frozen instances."),
 ("NOT-EST", R33, "What this read does NOT establish:", "on these wrappers."),
 ("W-1", R33, "Note W-1 (wording, required for a packet).", "«from a vertex of H, a gate, a valve, or a pad m, pβ, x_i, y»."),
 ("W-2", R33, "W-2 (required): the Definition says only", "«SPEC's choice, then the larger index»."),
 ("W-3", R33, "W-3 (required): premises to name.", "(Ω^H_s is the pointwise minimum)."),
 ("W-4", R33, "W-4 (for a packet):", "defined for W."),
 ("T-1", R33, "(T-1) WRAP's H-policy is a policy with the I^loc property", "among best successors."),
 ("NT", R33, "(T-2) **Claim NT (no tie on a 1-sink game; mine).**", "against Sink Seeking. ∎"),
 ("T-3", R33, "(T-3) G_n with ι_(G_n) is a 1-sink game", "between Table 4 and Figure 4."),
 ("T-4", R33, "(T-4) Every strategy σ of an improvement run from ι", "never invoked on G_n."),
 ("X-TIE", R33, "So (X-TIE) holds in its second form", "(ranks by (Ω, index) are injective in SPEC)."),
 ("NT-DATA", R33, "DATA for it (scratch/wrap_f11.py", "n = 1, …, 8 with Table 4's as printed (§5.3)."),
 ("STATUS", R33, "Status. Claim NT and (T-4) are referee-originated", "I would sign them."),
 ("F-1", R33, "F-1 (the game; READING, stated by the box, confirmed here).", "(it does, §5.1 and §6)."),
 ("F-2", R33, "F-2 (the count).", "above 2^n."),
 ("F-3", R33, "F-3 (wording).", "should read «in n» or «super-polynomial» here."),
 ("PW", R33, "PW-1 (required):", "they are not needed for XI-EXP."),
 ("A1", R33A, "So on my wrapper of my transcription of G_8", "all 18 counters 0."),
 ("R15-a", TRUNK, "(a) Lemma A: for any non-empty unambiguous set I of improvements of σ", "Ωσ ⊴ Ω_{Switch_I(σ)}.", RES),
 ("R15-c", TRUNK, "(c) Theorem: with φ(σ) = Σ_{v ∈ M⊕", "|φ| ≤ n(n−1).", RES),
 ("R15-d", TRUNK, "(d) N5: every iteration applies Switch_I", "(two potentials φ, φ^d).", RES),
 ("RULE", TRUNK, "with RESULTS R24 (a) Lemma R and R24 (b)'s choice rule (TB proof steps 1, 3-5; fixes §2.3) with RESULTS R103's bridge B, whose proof uses no", "(RESULTS R103's (R1) ruling)", RES),
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
            print("ADDC104 %s OK %s %s %d chars" % (k, c, hashlib.sha1(s.encode()).hexdigest()[:12], len(s)))
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
            it = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "out", "addC104.json"), encoding="utf-8"))
            it = {k: (v[0], v[1]) for k, v in it.items()}
        miss = [k for k, (c, s) in it.items() if s not in d]
        print("ADDC104 doc items %d missing %d %s" % (len(it), len(miss), " ".join(miss)))
        sys.exit(1 if miss else 0)
    elif sys.argv[1] == "json":
        import json
        print(json.dumps({k: [c, s] for k, (c, s) in items().items()}, ensure_ascii=False, indent=0))

if __name__ == "__main__":
    main()
