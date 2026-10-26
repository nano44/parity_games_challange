# R85: Friedmann's binary-counter gadgets under N5's S4a: what the W/Ξ split breaks (sources opened; DATA on switchallexp and switchbestexp) (L-RED successor 20, box 52; Lead 11:13Z, D18, date -u)
Labels per L40: SOURCE (quoted, opened), DATA, READING. Every game. Not a TARGET.md claim. G-N5-TIME stays open.

## 0. Sources opened (text extracted with pdftotext from the arXiv PDFs; sha1 of the PDF files as downloaded)
- [F] O. Friedmann, "An exponential lower bound for the latest deterministic strategy iteration algorithms", LMCS 7(3:19) 2011,
  arXiv 1106.0778 (PDF sha1 a63a9293). Read: §4 (the policies), §6.1 (simple cycles, Table 1, Lemmas 6.1 and 6.2), Theorem 6.14,
  §8 opening (the modified gadgets), Theorem 8.4.
  - §4 defines Schewe's globally optimizing policy I^glo: "given … the improved strategy σ* = I^glo_G(σ), we have for an arbitrary
    strategy σ′ in the arena A_{G,σ} that Ξσ′ ⊴ Ξσ*". The arena A_{G,σ} is σ plus its improving edges.
  - Theorem 6.14: I^loc needs ≥ 2^n improvement steps on G_n. Theorem 8.4: I^glo needs ≥ 2^n on H_n. Both start from ι.
- [STV] S. Schewe, A. Trivedi, T. Varghese, "Symmetric Strategy Improvement", arXiv 1501.06484 (PDF sha1 4fbbea66). Read: §4,
  §4.1 ("Escaping the traps with symmetric strategy improvement").
  - §4.1 argues that once Player Min (Odd) improves too, "Player Min will move to the right in the j most significant positions after
    2j improvement steps", and that "the deceleration lane ceases to work".
  - It also says traps for the symmetric algorithm "need to trap them simultaneously".

## 1. S4a against I^glo (READING from [F] §4 and SPEC S4a)
- N5's S4a uses the SAME arena as I^glo: Even v restricted to {σ(v)} ∪ Iσ(v), where Iσ is the Ξ-improving edges.
- It optimises a DIFFERENT objective: W, the valuation against Odd's current FIXED strategy τ, instead of Ξ, the valuation against Odd's
  best response σ̄. So S4a = "I^glo with Odd frozen to τ".
- [F]'s hiding device is the simple cycle (§6.1). While the cycle is open, Odd's best response stays in it (Lemma 6.1(3): τσ(e_i) = d_i),
  so closing looks worth only {d_i, e_i} in Ξ. Closing is still Ξ-IMPROVING ([F] §6.1: "e_i is an improving node for d_i"), so the
  edge is in S4a's arena.
- Under W, its worth depends on τ(e_i), not on the best response:
  - once τ(e_i) = h_i (Odd's own strategy leaves), W(e_i) carries h_i's full value, and S4a closes at once;
  - if τ(e_i) = d_i, closing creates a cycle won by Even in G_τ, which S4a also takes.
- Either way the hiding needs Odd's play at e_i to be the BEST RESPONSE at every state. N5's Even never reads that, except through the
  gate test.

## 2. DATA (experiments/red/usplit/frcyc.py, frcyc2.py; PGSolver ports from experiments/hard-families/pgsolver_port.py; SPEC S3 start)
- switchallexp (the I^loc family; simple cycles Even d → {e} ∪ D, Odd e → {d, h}):

| N | n | iterations | closings | openings | open states with (d, e) Ξ-improving but not closed | W-tempted and Ξ-blocked |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 35 | 8 | 3 | 1 | 0 | 0 |
| 4 | 63 | 8 | 5 | 1 | 0 | 0 |
| 6 | 91 | 12 | 7 | 1 | 1 | 0 |
| 8 | 119 | 16 | 9 | 1 | 3 | 0 |

- switchbestexp (the I^glo family, modified gates: Odd centre CC(i) → {CN0(i), CLv(i)}, Even chain CN0 → CN1 → CN2 → CC). N 2 / 4 /
  6, n 60 / 110 / 160, iterations 32 / 47 / 62, 0 fallbacks.
  - Every bit closes at most twice and opens at most once. A binary counter needs bit i to toggle 2^{N−i} times.
  - Odd's own τ(CC(i)) changes exactly ONCE per bit, from stay (CN0) to leave (CLv), at transitions 12…17 (top bit first, N 6). It
    never changes again.
  - σ̄(CC(i)), the best response, changes 3 times per bit. So [F]'s best-response alternation is present in Ξ, but N5's Even never
    optimises against it.
- This agrees with the fleet's earlier counts (RESULTS, N11 entry): N5 takes 32-77 iterations on switchbestexp N 2-8 and 8-16 on
  switchallexp N 2-8.

## 3. What a trap for N5 would need (READING; links R83 §2 and R84)
- [F]'s traps hide a profitable switch inside the VALUATION. N5 sees W, against τ, and the trap's alternation lives in σ̄.
  - [STV] §4.1's mechanism appears here verbatim: Odd's τ at the centres becomes optimal after a few steps.
  - From then on, Even's W-objective is a fixed one-player game G_τ.
- So in N5 a trap must hide profitable W-switches through the GATE: W-tempted, Ξ-blocked edges (N5-RUND §16 "forbidden").
  - The only Ξ-blocks I can build come from D. They re-arm (R84), but each release costs fresh content (R82, R83).
  - A counter would need forbidden edges released in binary-counter order with re-blocking ("closed cycle opens"). That is route (i)
    of R83 §2: super-polynomially many unforbid-switches per run.
- [F]'s cycle-opening step (Lemma 6.2(4): a closed cycle opens when the lane beats h_i) is a W-improving switch in G_τ. Under N5 it
  happens only if the lane's W-value rises. That is a G_τ improvement, and G_τ re-equilibrates within n + m steps when nothing is
  blocked (Lemma P).
- Open: a "simultaneous" trap in [STV]'s sense, with the gadget's alternation placed in τ-independent W-structure and released only by Ξ
  events. I have no construction.
