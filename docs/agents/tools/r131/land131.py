#!/usr/bin/env python3
"""land131.py: lands RESULTS R131 from docs/agents/R131-draft.md.

    python3 docs/agents/tools/r131/land131.py <checker-sha> [DRYRUN <outdir>]

It edits FOUR working-tree files and nothing else; it never runs git add / commit / push:
  (b) docs/RESULTS.md   the entry block (title with the checker token filled) and one empty line, inserted directly
                        before the line that starts «**Erratum E-1** (not a result» (after R130's block);
  (c) docs/GAPS.md      the UPDATE (date and time from `date -u` at run time, checker filled) appended to the
                        G-N5-TIME row with one separating space before the closing pipe; the row's status cell set
                        to «closed»; the whole row moved to the end of the «## Closed» table;
  (d) docs/NOW.md       the counter replacements of cfg.json "now.replacements" (default «R17-R130» -> «R17-R131»);
  (e) the draft         its first line gets « — LANDED in RESULTS <date> <time>Z (CHECKER C148 <sha> PASS), after
                        R130, before Erratum E-1».
(a) It REFUSES (exit 2, nothing written) if the draft holds the open-slot word anywhere but in the title's checker
    token, if the draft's block / UPDATE sha1 differ from out/hashes.json (written by build.sh), or if RESULTS / GAPS /
    NOW do not have the expected anchors.
(f) With DRYRUN <outdir> nothing in the repository is written: the four results go to <outdir> (a small copy of the
    tree that scripts/check_docs.py needs), check_docs.py is run there, and line counts, the RESULTS line range of
    R131, pipe counts and the check's result are printed.
Harness only (build.sh's tests): R131_DRAFT, R131_HASHES (other files), R131_NOW="YYYY-MM-DD HH:MM" (fixed stamp).
"""
import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib131 import OPEN_WORD, ROOT, block_sha1, line_sha1, load_cfg, split_draft  # noqa: E402


class Refuse(Exception):
    pass


def rd(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def plan(cfg, checker, draft_path, hashes_path, stamp):
    E, PREV, CN = cfg["entry"], cfg["prev_entry"], cfg["checker_number"]
    if not re.fullmatch(r"[0-9a-f]{7,40}", checker):
        raise Refuse("the checker sha %r is not 7 to 40 hex digits" % checker)
    draft = rd(draft_path)
    hashes = json.load(open(hashes_path, encoding="utf-8"))
    # ---- (a) the draft
    d = split_draft(draft, cfg)
    token = ", CHECKER PASS (docs/checker/%s.md, checker %s)" % (CN, OPEN_WORD)
    title = d["block"][0]
    if not title.endswith(token):
        raise Refuse("the title does not end with the checker token %r" % token)
    n_open = draft.count(OPEN_WORD)
    if n_open != 1:
        where = [i + 1 for i, l in enumerate(d["lines"]) if OPEN_WORD in l and i != d["b0"]]
        raise Refuse("the draft holds the open-slot word %d times; only the title's checker token may carry it (other lines: %s%s)"
                     % (n_open, where[:12], " …" if len(where) > 12 else ""))
    if block_sha1(d["block"]) != hashes["block_sha1"] or len(d["block"]) != hashes["block_lines"]:
        raise Refuse("the draft's entry block (sha1 %s, %d lines) is not the block build.sh recorded (sha1 %s, %d lines)"
                     % (block_sha1(d["block"]), len(d["block"]), hashes["block_sha1"], hashes["block_lines"]))
    if line_sha1(d["update"]) != hashes["update_sha1"]:
        raise Refuse("the draft's UPDATE line (sha1 %s) is not the UPDATE build.sh recorded (sha1 %s)" % (line_sha1(d["update"]), hashes["update_sha1"]))
    if hashes.get("line_stand_in"):
        raise Refuse("build.sh recorded that the line (%s) is a STAND-IN for the line of record" % hashes.get("line_name"))
    if "|" in title or "|" in d["update"]:
        raise Refuse("pipe characters in the title or in the UPDATE")
    upd = d["update"]
    for t in ("<DATE>", "<HH:MM>", "<checker>"):
        if upd.count(t) != 1:
            raise Refuse("the UPDATE has %d fill tokens %s (need 1)" % (upd.count(t), t))
    date, hhmm = stamp
    upd_f = upd.replace("<DATE>", date).replace("<HH:MM>", hhmm).replace("<checker>", checker)
    block_f = [title[:-len(token)] + ", CHECKER PASS (docs/checker/%s.md, checker %s)" % (CN, checker)] + d["block"][1:]
    # ---- (b) RESULTS
    R = rd(os.path.join(ROOT, "docs", "RESULTS.md"))
    RL = R.split("\n")
    anchor = cfg["results"]["insert_before_prefix"]
    ai = [i for i, l in enumerate(RL) if l.startswith(anchor)]
    if len(ai) != 1:
        raise Refuse("RESULTS: %d lines start with %r (need 1)" % (len(ai), anchor))
    ai = ai[0]
    hd = [(i, m.group(1)) for i, l in enumerate(RL) for m in [re.match(r"### (R\d+) \[", l)] if m]
    if any(n == E for _, n in hd):
        raise Refuse("RESULTS already has a heading %s" % E)
    before = [(i, n) for i, n in hd if i < ai]
    if not before or before[-1][1] != PREV or max(i for i, _ in hd) != before[-1][0]:
        raise Refuse("RESULTS: the last entry heading before the Erratum line is %s, not %s" % (before[-1][1] if before else None, PREV))
    if RL[ai - 1] != "":
        raise Refuse("RESULTS: the line before the Erratum line is not empty")
    RL2 = RL[:ai] + block_f + [""] + RL[ai:]
    # ---- (c) GAPS
    G = rd(os.path.join(ROOT, "docs", "GAPS.md"))
    GL = G.split("\n")
    gid, sf, st = cfg["gaps"]["row_id"], cfg["gaps"]["status_from"], cfg["gaps"]["status_to"]
    gi = [i for i, l in enumerate(GL) if l.startswith("| %s | " % gid)]
    if len(gi) != 1:
        raise Refuse("GAPS: %d rows start with '| %s | ' (need 1)" % (len(gi), gid))
    gi = gi[0]
    row = GL[gi]
    m = re.match(r"(\| %s \| [^|]+ \| [^|]+ \| )%s( \| )" % (re.escape(gid), re.escape(sf)), row)
    if not m:
        raise Refuse("GAPS: the status cell of the row %s is not %r" % (gid, sf))
    if not row.endswith(" |"):
        raise Refuse("GAPS: the row %s does not end with ' |'" % gid)
    ci = [i for i, l in enumerate(GL) if l == cfg["gaps"]["closed_heading"]]
    if len(ci) != 1 or ci[0] < gi:
        raise Refuse("GAPS: the heading %r occurs %d times, or lies before the row" % (cfg["gaps"]["closed_heading"], len(ci)))
    ci = ci[0]
    if "RESULTS %s (" % E in row:
        raise Refuse("GAPS: the row already carries an UPDATE of %s" % E)
    row2 = m.group(1) + st + m.group(2) + row[m.end():-1] + upd_f + " |"
    end = next((i for i in range(ci + 1, len(GL)) if GL[i].startswith("## ")), len(GL))
    rows_closed = [i for i in range(ci + 1, end) if GL[i].startswith("|")]
    if len(rows_closed) < 3:
        raise Refuse("GAPS: no table under the closed heading")
    if cfg["gaps"].get("closed_position", "end_of_section") == "end_of_first_block":
        j = rows_closed[0]
        while j + 1 < end and GL[j + 1].startswith("|"):
            j += 1
        last = j
    else:
        last = rows_closed[-1]
    GL2 = GL[:gi] + GL[gi + 1:last + 1] + [row2] + GL[last + 1:]
    # ---- (d) NOW
    N = rd(os.path.join(ROOT, "docs", "NOW.md"))
    N2 = N
    nrep = []
    for old, new, cnt in cfg["now"]["replacements"]:
        if N2.count(old) != cnt:
            raise Refuse("NOW: %r occurs %d times (cfg expects %d)" % (old, N2.count(old), cnt))
        if new in N2:
            raise Refuse("NOW: %r is already there" % new)
        N2 = N2.replace(old, new)
        nrep.append((old, new, cnt))
    # ---- (e) the draft
    DL = draft.split("\n")
    if " — LANDED in RESULTS " in DL[0] or not DL[0].startswith("# Draft RESULTS %s " % E):
        raise Refuse("the draft's first line is not an unlanded '# Draft RESULTS %s' line" % E)
    DL2 = [DL[0] + " — LANDED in RESULTS %s %sZ (CHECKER %s %s PASS), after %s, before Erratum E-1" % (date, hhmm, CN, checker, PREV)] + DL[1:]
    info = {"anchor_old": ai + 1, "first": ai + 1, "last": ai + len(block_f), "erratum_new": ai + len(block_f) + 2,
            "res_lines": (len(RL) - 1, len(RL2) - 1), "res_pipes": (R.count("|"), "\n".join(RL2).count("|")),
            "gaps_lines": (len(GL) - 1, len(GL2) - 1), "row_old": gi + 1, "row_new": last + 1, "row_pipes": (row.count("|"), row2.count("|")),
            "gaps_pipes": (G.count("|"), "\n".join(GL2).count("|")), "now": nrep, "block_lines": len(block_f),
            "update_bytes": len(upd_f.encode("utf-8")), "title_pipes": block_f[0].count("|"),
            "upd_head": upd_f[:95], "row_tail": row2[-110:], "row_head": row2[:70]}
    return {"docs/RESULTS.md": "\n".join(RL2), "docs/GAPS.md": "\n".join(GL2), "docs/NOW.md": N2, "docs/agents/R131-draft.md": "\n".join(DL2)}, info


def check_docs(root):
    p = subprocess.run([sys.executable, "-B", os.path.join(root, "scripts", "check_docs.py")], capture_output=True)
    return p.returncode, p.stdout.decode("utf-8", "replace")


def main(argv):
    if len(argv) not in (2, 4) or (len(argv) == 4 and argv[2] != "DRYRUN"):
        print(__doc__)
        return 2
    cfg = load_cfg()
    checker = argv[1]
    dry = argv[3] if len(argv) == 4 else None
    draft_path = os.environ.get("R131_DRAFT", os.path.join(ROOT, "docs", "agents", "R131-draft.md"))
    hashes_path = os.environ.get("R131_HASHES", os.path.join(HERE, "out", "hashes.json"))
    if (draft_path != os.path.join(ROOT, "docs", "agents", "R131-draft.md") or "R131_HASHES" in os.environ or "R131_NOW" in os.environ) and not dry:
        print("land131: REFUSED: R131_DRAFT / R131_HASHES / R131_NOW are for DRYRUN only")
        return 2
    if "R131_NOW" in os.environ:
        stamp = tuple(os.environ["R131_NOW"].split())
    else:
        out = subprocess.run(["date", "-u", "+%Y-%m-%d %H:%M"], capture_output=True).stdout.decode().split()
        stamp = (out[0], out[1])
    try:
        files, info = plan(cfg, checker, draft_path, hashes_path, stamp)
    except Refuse as e:
        print("land131: REFUSED: %s" % e)
        return 2
    except SystemExit as e:
        print("land131: REFUSED: %s" % e)
        return 2
    E = cfg["entry"]
    print("land131: %s%s, stamp %s %sZ, checker %s" % ("DRYRUN into " + os.path.basename(os.path.normpath(dry)) if dry else "LANDING in the working tree", "", stamp[0], stamp[1], checker))
    print("  RESULTS: %d -> %d lines (+%d = block %d + 1 empty); %s at l. %d-%d, the Erratum line moves l. %d -> l. %d; pipes %d -> %d (title %d)"
          % (info["res_lines"][0], info["res_lines"][1], info["res_lines"][1] - info["res_lines"][0], info["block_lines"], E, info["first"], info["last"],
             info["anchor_old"], info["erratum_new"], info["res_pipes"][0], info["res_pipes"][1], info["title_pipes"]))
    print("  GAPS: %d -> %d lines; row %s l. %d -> l. %d (status %s -> %s, under the closed table); row pipes %d -> %d; file pipes %d -> %d; UPDATE %d bytes"
          % (info["gaps_lines"][0], info["gaps_lines"][1], cfg["gaps"]["row_id"], info["row_old"], info["row_new"], cfg["gaps"]["status_from"],
             cfg["gaps"]["status_to"], info["row_pipes"][0], info["row_pipes"][1], info["gaps_pipes"][0], info["gaps_pipes"][1], info["update_bytes"]))
    print("  GAPS row starts %r" % info["row_head"])
    print("  GAPS UPDATE starts %r" % info["upd_head"])
    print("  GAPS row ends %r" % info["row_tail"])
    print("  NOW: %s" % "; ".join("%s -> %s (%d place%s)" % (o, n, c, "" if c == 1 else "s") for o, n, c in info["now"]))
    if dry:
        if os.path.exists(dry):
            shutil.rmtree(dry)
        for rel in ("scripts/check_docs.py", "CLAUDE.md", "TARGET.md", "docs/DECISIONS.md", "docs/DECISIONS-INDEX.md"):
            os.makedirs(os.path.dirname(os.path.join(dry, rel)), exist_ok=True)
            shutil.copy(os.path.join(ROOT, rel), os.path.join(dry, rel))
        os.makedirs(os.path.join(dry, "notes"), exist_ok=True)
        for f in sorted(os.listdir(os.path.join(ROOT, "notes"))):
            if f.endswith(".md"):
                shutil.copy(os.path.join(ROOT, "notes", f), os.path.join(dry, "notes", f))
        root = dry
    else:
        root = ROOT
    for rel, text in files.items():
        os.makedirs(os.path.dirname(os.path.join(root, rel)), exist_ok=True)
        with open(os.path.join(root, rel), "w", encoding="utf-8") as f:
            f.write(text)
    rc, out = check_docs(root)
    print("  scripts/check_docs.py on %s: rc %d%s" % ("the copies" if dry else "the working tree", rc, "" if rc == 0 else " :: " + out[:300].replace("\n", " / ")))
    print("land131: %s" % ("DRYRUN done (nothing in the repository was written)" if dry else
                           "written: docs/RESULTS.md, docs/GAPS.md, docs/NOW.md, docs/agents/R131-draft.md (not added, not committed)"))
    return 0 if rc == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
