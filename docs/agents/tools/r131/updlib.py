#!/usr/bin/env python3
"""The GAPS UPDATE builder (the landed procedure of R118-R130, made generic).

An UPDATE on the G-N5-TIME row is  PREFIX + BODY + '. ' + ENDING  with
  PREFIX = 'UPDATE <DATE> <HH:MM>Z: RESULTS R<n> (<packet>; CHECKER C<c> <checker>) [refereed-only] LANDED: '
  BODY   = the line of record with (1) every label '(Label) ' moved behind its clause, (2) a list of exact
           replacements, each applied where its old string occurs exactly once (the boundary that becomes ': ',
           the dropped scope words, the pipe-bearing strings put into words), (3) the line's final '.' stripped
           when it has one.
build() is the one function; R131 calls it with the labels and strings of cfg.json, the controls call it with the
labels found in the landed titles of R128, R129, R130 and must reproduce their landed UPDATEs byte for byte.
"""
import re

KEYWORDS = ("Lemma ", "Corollary ", "Theorem ", "Claim ", "Statement ", "class facts)")
CONNECTORS = (", and ", "; ", ": ")


class Refuse(Exception):
    pass


def paren_end(s, i):
    """index just after the parenthesis that opens at s[i]."""
    d = 0
    for j in range(i, len(s)):
        if s[j] == "(":
            d += 1
        elif s[j] == ")":
            d -= 1
            if d == 0:
                return j + 1
    raise Refuse("unbalanced parenthesis from %d" % i)


def once(s, x, what):
    n = s.count(x)
    if n != 1:
        raise Refuse("%s: %r occurs %d times (need exactly 1)" % (what, x[:70], n))
    return s.index(x)


def move_at(s, items):
    """items: [(label_start, label_end, clause_end)], label followed by one space; the label goes behind its clause."""
    out, pos = [], 0
    for a, b, e in sorted(items):
        if not (pos <= a < b < e <= len(s)) or s[b] != " ":
            raise Refuse("label at %d-%d with clause end %d: bad order or no space after the label" % (a, b, e))
        out.append(s[pos:a])
        out.append(s[b + 1:e])
        out.append(" " + s[a:b])
        pos = e
    out.append(s[pos:])
    return "".join(out)


def labels_by_string(s, labels):
    """labels: [{'label': ..., 'clause_end': ...}] -> positions; each string exactly once, the end after the label."""
    items = []
    for L in labels:
        a = once(s, L["label"] + " ", "label")
        e = once(s, L["clause_end"], "clause end of %r" % L["label"][:40])
        if e <= a:
            raise Refuse("clause end %r lies before its label %r" % (L["clause_end"][:40], L["label"][:40]))
        items.append((a, a + len(L["label"]), e))
    return items


def labels_auto(head):
    """the labels of a landed title's claim part: a parenthesis that opens with a label keyword, right after ': ',
    '; ' or ', and ', followed by a space; its clause ends where the next label's connector begins (or at the end)."""
    found = []
    for m in re.finditer(r"\(", head):
        i = m.start()
        if not head.startswith(KEYWORDS, i + 1):
            continue
        conn = next((c for c in CONNECTORS if head.endswith(c, 0, i)), None)
        if conn is None:
            continue
        j = paren_end(head, i)
        if j >= len(head) or head[j] != " ":
            continue
        found.append((i, j, i - len(conn) if conn != ": " else None))
    items = []
    for t, (i, j, _) in enumerate(found):
        if t + 1 < len(found):
            e = found[t + 1][2]
            if e is None:
                raise Refuse("a later label follows ': ' (no clause boundary)")
        else:
            e = len(head)
        items.append((i, j, e))
    return items


def build(prefix, line, label_items, replaces, ending):
    """label_items: positions in `line` (labels_by_string / labels_auto); replaces: [(old, new)], each old exactly once."""
    body = move_at(line, label_items)
    for old, new in replaces:
        i = once(body, old, "replacement")
        body = body[:i] + new + body[i + len(old):]
    if body.endswith("."):
        body = body[:-1]
    return prefix + body + ". " + ending


def r131_update(cfg, line):
    """the unfilled UPDATE of R131 from the line of record (one line, no newline)."""
    u = cfg["update"]
    prefix = "UPDATE <DATE> <HH:MM>Z: RESULTS %s (%s; CHECKER %s <checker>) [refereed-only] LANDED: " % (
        cfg["entry"], cfg["packet_name"], cfg["checker_number"])
    once(line, u["source_prefix"], "source parenthesis")
    if not line.endswith(")."):
        raise Refuse("the line does not end with ').'")
    reps = [(d, "") for d in u["drops"]] + [tuple(p) for p in u["pipe_pairs"]]
    out = build(prefix, line, labels_by_string(line, u["labels"]), reps, u["ending"])
    if "|" in out:
        raise Refuse("the UPDATE carries %d pipe characters (add pipe_pairs to cfg.json)" % out.count("|"))
    if out.count("(") != out.count(")"):
        raise Refuse("the UPDATE's parentheses do not balance")
    return out
