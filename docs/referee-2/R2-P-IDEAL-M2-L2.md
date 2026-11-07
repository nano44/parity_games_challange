# R2-P-IDEAL-M2-L2: line L-2 and fixes entry 1 of P-IDEAL-M2
REFEREE-2 successor 27 (Opus 5.5, D12/D19). Written 2026-11-04 08:52Z (date -u). Object: claude/l-new 4d244698.

## Hashes (re-measured with git show 4d244698:FILE | sha1sum)
- docs/new/P-IDEAL-M2-fixes.md 66fd61731df0667e380e8ac231ee27062ee6b8a8, 50 lines. docs/new/P-IDEAL-M2-line-L2.txt
  c890f2685edf3725a5fccb12cf93e9d3dd7d44ff, 1 line, 0 «|». Packet bc47b06c and L-1 0160d1e3 unchanged.

## Fixes entry 1 (M2-G1): CORRECT
- Quotes checked against the landed R105 body on trunk (item «(b) Lemma LOCAL (§1, l. 75-85)», whitespace-normalised): «(a) If two
  states s, s′ agree on every mover of the chain of (x, k) under s other than x, then the chains of (x, k) under s and s′» «are equal and
  Ξ_s(x, k) = Ξ_(s′)(x, k).» FOUND; «(b) the same for every k when s, s′ agree on every strict Ξ-descendant of x» FOUND (unquoted
  RESULTS text, verbatim); «(c) key_s(x, k) = key_(s′)(x, k) whenever s and s′ agree on every mover of level < lev(x).» FOUND.
- TRIGGER (b) replacement: LOCAL (a) with s = s_(t−2), s′ = s_(t−1), x = z, k ∈ {o, o′}; hypothesis «no mover y ≠ z on the chains under
  s_(t−2) in Mv_(t−1)» is exactly «agree on every mover of the chain under s other than x». Correct, whether or not z moved.
- MIN-FLIP XF replacement: LOCAL (b) with s = s_(j−1), s′ = s_j. Correct. No statement or DATA change. M2-G1 CLOSED on my side.

## Line L-1 → L-2: MATCHES
Token diff (git diff --no-index --word-diff=plain, my own run) equals the 15 changes listed in fixes entry 2:
- +«N movers, M options,» (M2-L3): binds N, M. ✓
- +«(step t ≥ 2 is chained iff h_(t−1) lies on the chain under s_(t−2) of the option h_t takes, as a mover other than h_t)» (my P-1):
  the packet definition, = P-IDEAL-RED l. 118-119; removes the LINE reading of R2-R105-chained.md. ✓
- TRIGGER: «caused by a» → «and then some», «moving» → «under s_(t−2) moves»; «caused by a lower-level» → «and then some», «moving» →
  «of lower level moves» (my P-2, P-3; REFEREE M2-L2): existence wording, chains bound to s_(t−2). = packet §2 (b), (c). ✓
- MIN-FLIP: +«moves(x) the number of steps moving x, KF_x R105's number of steps at which KP(x) changes (KEYFLIP),»: my REQUIRED M2-L1
  text byte-exact. ✓
- DEAD: +«from its stored start», +«> ⌊3·8/2⌋ = 12,» (REFEREE M2-L4): start = the JSON's start [1, 1, 0, 0, 0, 1, 0, 1] (my run used
  it); 12 = ⌊24/2⌋. ✓
- DATA: «on 54 corpus runs, on 34,934 random runs (every start for N ≤ 8, the genome start otherwise; experiments/new/box155/mcharge.py)
  and on 3,981 all-start degree-≤-2 random runs (experiments/new/box156/trig.py))»: my REQUIRED M2-L2 in the joint wording. Counts
  reproduced by my own simulator (R2-P-IDEAL-M2.md): 34,934 runs = every start of the 192 genomes with N ≤ 8 + the genome start of the
  8 with N 9-10; 3,981 = every start of the 93 degree-≤-2 genomes. ✓
- Provenance: + fixes entry 1, docs/new/P-IDEAL-M2-fixes.md. ✓
- Binder pass: T, Mv_t, U (with h_t, s_t of R105 / R104), M₂, N, M, o, o′, z, XF_x, KF_x, moves(x), KP(x) (R105) all bound. Scope tail
  unchanged and still matches packet §1-§5.
### Optional (not required)
- P-4: h_t appears in the new parenthesis without its definition («h_t a least-level mover of step t», R105's line); bound by «of
  R105», so optional.
- P-5: the 54 corpus runs no longer name their tools (mcharge.py and trig.py both ran on them); the count is right.

Verdict: L-2 MATCHES. All seven statements stay SIGN (Opus 5.5, D12); with entry 1, TRIGGER and MIN-FLIP cite LOCAL (a), (b).
