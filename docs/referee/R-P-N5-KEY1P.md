# R-P-N5-KEY1P: FIRST REVIEW of packet P-N5-KEY1P (L-NEW successor 77; claude/l-new 44775605, docs/new/P-N5-KEY1P.md sha1 f7191623e9ee212fa127c7e4a224f7ab9d689156, 321 lines)
REFEREE successor 36, first referee (D1). Written 2026-11-13T14:56Z (date -u, by command substitution). A SIGNATURE review of the frozen packet: a REDUCTION /
STRUCTURE packet (it bounds nothing polynomially; the packet says so). Not read before this report: docs/referee-2/ on this packet
(REFEREE-2 40 / 41's pre-read is quoted by the packet; I checked the two quoted strings by script only), box 217's source note,
the lane's key1p.py / one217.py beyond key1p.py's header (read to see the counters' definitions; not run, not imported).

## 0. Verdicts
| § | statement | verdict | kind | items |
| --- | --- | --- | --- | --- |
| §1 | the model 1P(G) | well defined | definition | none |
| §2 | Lemma IDEAL-1P (a)-(d); T_key(G) = L(G) | **SIGN**, no gap | unconditional (R104's definition; R105 ENC, landed, «at any degree», acyclic Ξ-graphs) | none |
| §3 | Theorem RED-1P (a)-(c); KILL-TRANSFER; BOUND-TRANSFER | **SIGN AS A COROLLARY of landed R117 (f)**, i.e. CONDITIONAL on R117's premises as landed (the statement says «under R117's premises as landed») | conditional | K-1 |
| §4 | Lemma 0 (a)-(c) | **SIGN**, no gap | unconditional | none |
| §5 | A1 MONO-1P (V), (μ) | **SIGN**, no gap | unconditional | none |
| §6 | A2 SWITCH-BOUND; A2-POLY | **SIGN**, no gap (A2-POLY's N5 sentence: as §3) | unconditional / conditional | none |
| §7 | A3 PAIR-1P (i), (ii) | **SIGN**, no gap | unconditional | none |
| §8 | A4 HEREDITY (i)-(iii) | **SIGN**, no gap | unconditional | none |
| §9 | SW-POLY ⟺ QUIET-KEY-1P; ENUM-NEC | **SIGN**, no gap | unconditional | K-2 |
| §9 | QUIET-KEY-1P, SW-POLY «OPEN» | not signed (the packet claims nothing) | — | K-2: decided NO by Theorem EXP-IDEAL once P-N5-EXP lands |
| §10 | DATA | reproduced with own code on the model side (§3) and with this lane's builder and engine on the N5 side (§4) | measured | none |
| quotes | 35 of 35 verbatim by own script | — | — | none |
No statement is REFUSED; no gap found.

## 1. Method
- Read: the packet in full; premises as landed on trunk 6eaf4604 (R104 title l. 9864, R105 title l. 10155 «on acyclic Ξ-graphs … any
  number of movers per level … at any degree», R117 l. 13362 and scope tail (f), (g)).
- Own tool docs/referee/scratch/k1p.py: the model 1P written from the packet's §1 (integer weights ±2^rank, values by recursion
  along the Ξ-graph, availability, root-first keys, the KEY step by increasing level), compared with gkx.py's step(), which is
  written from P-N5-REALIZE §2 (β-sets, largest rank in the symmetric difference, the level-by-level step). The lane's key1p.py and
  one217.py are not imported. Sets: this lane's G_3..G_10 (rule R of P-N5-EXP: wires, exits at every level), the packet's five towers
  and 63 climbed records (frozen files), own random genomes (degrees 1-3, random parities, 1-5 levels), own mutants of the towers
  (1-4 mutations: W-target, Ξ-target, rank swap, parity flip, gate swap, start flip; acyclic kept), LIFT(H5, D).

## 2. The proofs, statement by statement
- IDEAL-1P. (a): the chain of (x, k) under s is a Ξ-path of distinct movers, so the β-set has the integer value ω(x, k) + V_s(xt(x,
  k)); for two different sets the β of largest rank r in the symmetric difference contributes ±2^r to the difference and the rest at
  most 2^r − 1 in absolute value, so the integer order is R104's order (this is R105 ENC, and Lemma 0 (b)'s proof gives it again). (b),
  (c): the same tuples and the same level-by-level choice. (d): «opt» is the case A_s(x) = {s(x)} for all x, where s′ = s. Correct.
  Counter ordv (every state of every run, every ordered pair of options of every mover: [v_s larger] against the β-set order) and
  ideq (the two runs, state by state): 0 on every set below.
- RED-1P. With IDEAL-1P the key run is the IDEAL run, and (a)-(c) are R117 (f) word for word (states 0..L standard, transitions 1..L
  FL, transition L + 1 a fallback; an FL transition is not a fallback by R104's definition of an FL run). KILL-TRANSFER is R117 (g)
  (b); BOUND-TRANSFER is (c). The statement carries «under R117's premises as landed (§0)», and §0 quotes them. **K-1 (wording;
  title l. 1, l. 6, §11 l. 305 «Why the packet is unconditional»).** «unconditional» here means «no premise beyond landed R117's»
  (no KEY-TAU, no [IMP3]); R117 itself stands under 1E-N3, R24, R103's bridge B, R36 (c). A RESULTS line must not print
  «unconditional» for RED-1P or KILL-TRANSFER without these words.
- Lemma 0. (a): the map (k, κ) ↦ κ ++ (gate(x, k)) is a bijection onto K(x) because gate indices are distinct; hence the recursion
  and both bounds. (b): two distinct Ξ-paths share a prefix and a mover x_i and split there; the β of (x_i, k_i) is not on the other
  path (acyclic), so the β-sets differ and the values differ by the 2^r argument. (c) from (b). Correct. Counters l0a, l0b (the
  recursions against a full enumeration of the W-paths / Ξ-paths wherever the count is at most 3,000; the bounds), l0c: 0.
- A1. (V): V_(t+1)(x) = ω(x, k′) + V_(t+1)(y′) ≥ ω(x, k′) + V_t(y′) = v_t(x, k′) ≥ V_t(x), strict when k′ ≠ s_t(x), by induction
  targets first. (μ): μ_(t+1)(x) ≤ key_(s_(t+1))(x, s_t(x)) = μ_(t+1)(w) ++ (gate) ≤ μ_t(w) ++ (gate) = μ_t(x) by induction on the level,
  strict at a switch because the least key is attained once. Correct. Counters a1v, a1mu: 0.
- A2, A2-POLY. Two monotone sequences in sets of |PΞ(x)| and |K(x)| elements, strict at every switch; every step switches a mover.
  D^(c·log2 N) = N^(c·log2 D). Correct. Counters a2 (both bounds, both inequalities on T, and Σ sw ≤ Σ (min − 1)), a2p: 0.
- A3. (i) one W-target or level 0: the two keys differ in the last entry only, at every state; the option of smaller gate, once
  taken, is never left. (ii) one Ξ-target: v_s(x, a) − v_s(x, b) is a nonzero constant. Correct; (ii) «whatever the rule» tested on runs
  of a random rule (a3r). On G_k the wires are (i)-movers and never switch.
- A4. (i), (ii) as in the packet (a non-increasing sequence with |K| − 1 strict decreases in a set of |K| elements takes every
  element; the last entry of a key names the option). (iii): consecutive switches of a degree-2 mover go to the option that is
  strictly better under the state they are computed from, so the sign of v(x, a) − v(x, b) changes between them. Correct. a4h, a4x: 0.
- §9. max sw ≤ T ≤ N·max sw gives SW-POLY ⟺ QUIET-KEY-1P. ENUM-NEC: a witness at level k − 1 has |K| ≥ 2^k when every degree is ≥ 2.
  Correct. Counter enum (c ∈ {1, 3/4, 1/2}): 0. **K-2 (status; §3 l. 138-139, §9 l. 227).** The packet labels QUIET-KEY-1P and
  SW-POLY «OPEN (not claimed)», which was right at its freeze (12:31Z). Theorem EXP-IDEAL of P-N5-EXP (l-red-b 350d84eb; this
  lane's report R-P-N5-EXP.md signs (b), (c)) gives a family with max_x sw(x) = 2^(k−2) and T_key = 2^k − 2 at N + M = 27k − 48: SW-POLY
  and QUIET-KEY-1P are then FALSE, by exactly the packet's «Kill form». Nothing in this packet depends on the answer; a fixes entry
  (or the RESULTS line) should carry the status as it is on the day of landing. On G_k my counters of A1-A4 and ENUM-NEC are 0, and
  k(G_k) = 1 (the packet's diagnostic), as P-N5-EXP §11 says.

## 3. DATA on own code (model side; k1p.py; logs docs/referee/scratch/k1p_logs/, regenerated by k1p_logs/s36_k1p_run.sh)
Must-0 counters (failures; unit: one (state, mover) or mover or genome as in k1p.py's header): ideq, ordv (IDEAL-1P), l0a, l0b, l0c
(Lemma 0), a1v, a1mu (A1), a2, a2p (A2, A2-POLY), a3, a3r (A3), a4h, a4x (A4), enum (ENUM-NEC); recdiff = [T ≠ the record's own T_key].
```
model, G_3..G_10 (rule R of P-N5-EXP): genomes 8; key-run steps 2,024; T 6..1022; ideq 0 ordv 0 l0a 0 l0b 0 l0c 0 a1v 0 a1mu 0 a2 0 a2p 0 a3 0 a3r 0 a4h 0 a4x 0 enum 0
model, five towers: genomes 5; key-run steps 741; T 30..299; ideq 0 ordv 0 l0a 0 l0b 0 l0c 0 a1v 0 a1mu 0 a2 0 a2p 0 a3 0 a3r 0 a4h 0 a4x 0 enum 0
  tower DBL4_d20_F30.json: T 30 maxsw 15 k 0 k_(3/4) 5
  tower H5_d20_F62.json: T 136 maxsw 31 k 5 k_(3/4) 6
  tower H6_d24_F126.json: T 209 maxsw 63 k 6 k_(3/4) 6
  tower HIT7_d28_F254.json: T 299 maxsw 127 k 7 k_(3/4) 7
  tower RECF4_d20_F60.json: T 67 maxsw 30 k 4 k_(3/4) 5
model, 63 climbed records: genomes 63; key-run steps 1,945; T 3..340; ideq 0 ordv 0 l0a 0 l0b 0 l0c 0 a1v 0 a1mu 0 a2 0 a2p 0 a3 0 a3r 0 a4h 0 a4x 0 enum 0 recdiff 0
model, rand seed 1: genomes 3,000; notmember 0; key-run steps 2,238; largest T 3; ideq 0 ordv 0 l0a 0 l0b 0 l0c 0 a1v 0 a1mu 0 a2 0 a2p 0 a3 0 a3r 0 a4h 0 a4x 0 enum 0
model, rand seed 2: genomes 3,000; notmember 0; key-run steps 2,217; largest T 3; ideq 0 ordv 0 l0a 0 l0b 0 l0c 0 a1v 0 a1mu 0 a2 0 a2p 0 a3 0 a3r 0 a4h 0 a4x 0 enum 0
model, mut seed 7: genomes 500; notmember 0; key-run steps 23,069; largest T 299; ideq 0 ordv 0 l0a 0 l0b 0 l0c 0 a1v 0 a1mu 0 a2 0 a2p 0 a3 0 a3r 0 a4h 0 a4x 0 enum 0
model, LIFT(H5, D), D = 0, 10, 40: genomes 3; key-run steps 408; T 136..136; ideq 0 ordv 0 l0a 0 l0b 0 l0c 0 a1v 0 a1mu 0 a2 0 a2p 0 a3 0 a3r 0 a4h 0 a4x 0 enum 0 liftdiff 0 notmember 0
```
Controls on HIT7 (howard: Howard's rule in place of KEY; down: movers leave A; a2half: |K|/2 for |K|; a3all: A3 on every degree-2
mover; a4any: A4 without its hypothesis; w0: all weights 0; perm: keys by a permuted gate order). Each fires:
```
model control howard on HIT7_d28_F254.json: fires a1mu 103, a2 1, a3 1
model control down on HIT7_d28_F254.json: fires a1v 149, a1mu 103
model control a2half on HIT7_d28_F254.json: fires a2 14
model control a3all on HIT7_d28_F254.json: fires a3 43
model control a4any on HIT7_d28_F254.json: fires a4h 7553, a4x 36
model control w0 on HIT7_d28_F254.json: fires ideq 1, ordv 56, l0b 40, l0c 56
model control perm on HIT7_d28_F254.json: fires ideq 1
```
The packet's rows «five towers: T_key 30, 136, 209, 299, 67», «climbed records: 63 genomes, 1,945 steps, largest 340», its k and
k_(3/4) values (0, 4, 5, 6, 7 and 5, 5, 6, 6, 7 for DBL4, RECF4, H5, H6, HIT7) and «LIFT(H5, D): T_key 136, largest sw 31» are
reproduced by my code from the frozen files. (The packet's mutated-tower and random sets use the lane's generators; mine are own
generators with other seeds: an independent sample, not a replay.)

## 4. DATA on this lane's engine (N5 itself; RED-1P (a)-(c))
gkx_n5.py: genome from the frozen file, IDEAL run by gkx.step(), game by this lane's builder gk_gamma3.py (successor 35, from R104
§3.1 and P-N5-REACH §3), N5 by this lane's engine rl_engine.py (from SPEC), winners by this lane's Zielonka. RED-1P (a) is STD and
S3START, (b) is FLFB, (c) is LASTFB; EXACT = [iterations ≠ L + 3] + [fallbacks ≠ 1] is landed R124's count; WIN compares the winners.
```
N5 itself, five towers: games 5; n 610..850; iterations in all 756; L 30..299; S3START 0 STD 0 FLFB 0 FLTAU 0 FLSIG 0 LASTFB 0 WIN 0 EXACT 0
N5 itself, LIFT(H5, 10): games 1; n 690..690; iterations in all 139; L 136..136; S3START 0 STD 0 FLFB 0 FLTAU 0 FLSIG 0 LASTFB 0 WIN 0 EXACT 0
N5 itself, 63 climbed records: games 63; n 100..970; iterations in all 2,134; L 3..340; S3START 0 STD 0 FLFB 0 FLTAU 0 FLSIG 0 LASTFB 0 WIN 0 EXACT 0
```
Controls on H5 (lastfb: the fallback flag read one transition early, the packet's «fbearly»; revE: e-indices reversed; rank:
β-ranks reversed in the game only; start: one mover's Ω-2 pad on the other option):
```
N5 control lastfb on H5_d20_F62.json: fires LASTFB 1
N5 control revE on H5_d20_F62.json: fires STD 8, FLFB 1, EXACT 1
N5 control rank on H5_d20_F62.json: fires STD 6, FLFB 1, EXACT 1
N5 control start on H5_d20_F62.json: fires S3START 1, STD 74, FLFB 1, EXACT 1
```

## 5. Quotes (k1p_quotes.py, own script; R-ids against the RESULTS entry of trunk 5d7aab0f, path@commit labels by `git show`)
```
quotes: tags 19 tagged_quotes 35 found 35 notfound 0 nosource 0
```
The two strings quoted from docs/referee-2/R2-key-preread.md@abd629d7 were matched by the script; I did not open that file.

## 6. Items
| id | where | what | kind |
| --- | --- | --- | --- |
| K-1 | title, l. 6, §11 l. 305 | «unconditional» = no premise beyond landed R117's; the line must carry R117's premises | required for the RESULTS line (wording) |
| K-2 | §3 l. 138-139, §9 l. 227 | QUIET-KEY-1P / SW-POLY «OPEN»: superseded by P-N5-EXP when it lands (FALSE on G_k) | status note for the line |

## DONE / FINDINGS / NEEDS
- DONE: every statement re-derived; own model code against the definition-based step on the sets of §3; N5 itself on the towers,
  LIFT and the 63 records with this lane's builder and engine (§4); 35 of 35 quotes.
- FINDINGS: every statement SIGNED, no gap; RED-1P and its corollaries are corollaries of R117 (f), conditional on R117's premises
  (K-1); the «OPEN» label of QUIET-KEY-1P / SW-POLY is overtaken by P-N5-EXP (K-2).
- NEEDS (L-NEW, through the Lead): K-1 and K-2 in the RESULTS line or a fixes entry. (Lead): nothing else.
