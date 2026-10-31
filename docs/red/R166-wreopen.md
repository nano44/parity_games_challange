# R166 CONJECTURE W-REOPEN (L-SI box 58 §10) DEAD: an Even vertex on the escaped Odd 2-cycle keeps the W-tie (L-RED successor 38)
Written ~21:xxZ (date -u), 2026-10-31, after the Lead's 20:30Z message (last box before park). Labels: DEAD, DATA, READING.

## Target
- W-REOPEN (l-si 8a69c681, docs/si/N5-ANC-box58.md §10; 0 violations on the corpus): inside a W-run, every equal-key re-opening of an
  Odd escape (s, x) whose escaped cycle contains an EVEN vertex needs a strict W-rise at x or x₂ between the two escapes.
- Kill: one (s, x) escaping twice in a W-run at the same swap key, through a cycle with an Even vertex, with no W-rise in between.

## Instance (the Lead's hint (ii))
- Base: red/n3/instances/n3cov_lean.pg with its valid start n3cov_lean_fixed.start (R99).
  - L-SI's wrise.py (l-si 8a69c681, read-only): ODDONLY_NOWRISE 1.
  - Odd s = 35 (succ 29, 44) escapes x = 29 at transitions 12 and 21 with swap key (1, 44), inside one W-run.
  - The escaped cycle is the Odd 2-cycle 35 → 29 → 35.
- Gadget: wre/subdiv.py subdivides one edge of that cycle by a new Even vertex e.
  - All priorities are shifted by +2 (order and parity kept), and e gets priority 0, the unique lowest. So e is never a cycle node or
    in a path set; it only lengthens plays through it by 1.
  - Env CHOICE=1 gives e a second successor: an Odd sink with a self-loop at the top odd priority, which Even never takes. So e is an
    Even vertex WITH a choice.
- Results (wrise.py; the run is unchanged: n5b 35 iterations, 1 fallback, the same as the base):
  | instance | edge subdivided | e's successors | EVEN_NOWRISE | ODDONLY_NOWRISE | NOWRISE witness (s, x, u1, u2, og) |
  | --- | --- | --- | --- | --- | --- |
  | lean_29_35 (pin) | 29 → 35 | {35} | 1 | 0 | 35, 29, 12, 21, (1, 45) |
  | lean_35_29 | 35 → 29 | {29} | 1 | 0 | 35, 48, 12, 21, (1, 45) |
  | leanc_29_35 (pin) | 29 → 35 | {35, sink} | 1 | 0 | 35, 29, 12, 21, (1, 45) |
  | leanc_35_29 | 35 → 29 | {29, sink} | 1 | 0 | 35, 48, 12, 21, (1, 45) |
- Faithfulness: xeng identical and Oink zlk + verify OK on both pins; startck OK; WMONV 0 (R164's W-monotonicity holds).

## Reading
- The «Even vertex on the cycle» condition is not the right separator. An Even vertex that never switches (forced, or with a choice it
  never takes) changes nothing in the dynamics.
- A repair would need the escaped cycle to contain an Even vertex that SWITCHES between the two escapes. That is the condition under
  which candidate (b) (S4a's W-monotone optimum) can act. Untested here.
- Either way, this is the ODD-only mechanism of n3cov (Odd 2-cycles re-opened with W tied). It costs one fallback in this run and does
  not produce long runs. It is a counterexample to the lemma as stated, not to G-N5-TIME.

## DONE / FINDINGS / NEEDS
- DONE: this note; wre/subdiv.py; pins wre/instances/{lean_29_35, leanc_29_35} (wre/pins.sha1); check.sh block R166.
- FINDINGS: DEAD W-REOPEN as stated (EVEN_NOWRISE 1 on lean_29_35 and leanc_29_35). Suggested repair: require an Even vertex that switches
  between the escapes.
- NEEDS: none from the owner.
