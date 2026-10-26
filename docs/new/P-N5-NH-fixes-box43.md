# P-N5-NH-box42 fixes (box 42 packet, filed in box 44): the referees' notes, written out
L-NEW successor 23 (Opus 5.5, D14/D18, L40), session_011WFfFqRNrU1a8LQwbwazZN. Written 2026-10-26 02:26Z by date -u, at the Lead's GO of
02:21Z (Lead's stamp): "Repairs only. Freeze both." FROZEN at push; its sha1 is reported to the Lead.
- Object: packet docs/new/P-N5-NH-box42.md, sha1 93d19be8018e07a2727bbe1db5920198a0beb1eb (pinned trunk 54ac72e6). The packet is NOT
  edited; this file is its correction layer, a record of the reports, not refereed text. No signed statement changes.
- Sources:
  - REFEREE: docs/referee/R-N5-NH42.md (referee a47f8540, successor 10): every statement SIGNED, no gaps; notes NH42-N1..N3. §C
    (referee 5fc234ba, successor 11): identical verdicts; N-NH42-1..3 accepted.
  - REFEREE-2: docs/referee-2/R2-N5-NH42.md (referee-2 d2142087, successor 13): all SIGN, no gap; notes N-NH42-1..3. §C (referee-2
    253fe5c5): identical; "nothing open".
  - Both §C commits are on origin/claude/referee and origin/claude/referee-2; at trunk 249ad7e3 (02:18Z) neither §C is merged yet.
- Scope unchanged: Theorem NH is a REDUCTION (both referees: an implication). Not a TARGET.md claim; G-N5-TIME stays open.

## 1. Lines (no gap; notes only)
| note(s) | where in the packet | line to read with the packet |
| --- | --- | --- |
| NH42-N1 + N-NH42-1 (complementary, REFEREE §C C.2) | §3 Lemma NR | K_S and E_S enter only as the counts RESULTS R26 defines (non-fallback W-changes on R; transitions containing an event). R26 (d)'s "R-changing" means "a transition with a switch on R"; by Lemma SW (b) a Ξ-change on R comes with a switch on R, so N_R(S) ≤ U3C's count in either reading. |
| N-NH42-2 | §4 Theorem NH, the event count E | "Event" (R26 (c)) may be read narrowly (the switching R-vertex's own kind changes, or c_w switches) or broadly (some R-vertex's kind changes at a transition with a switch); R26 (c)'s kinds-constant makes the transition counts equal. Theorem NH holds in both readings (data: max E 15 in both). |
| NH42-N2 + N-NH42-3 (same point) | §4 last sentence; §5 status table | Theorem NH is signed as an implication ((NH′) from (X), NFB-O, (E), (K_W) read as polynomial per phase), not as a claim that any input is polynomial. §5's statuses (as of trunk 6d78b8f4) are superseded: P-N5-FBPOLY LANDED as RESULTS R48 (with its fixes; FX's F* uses the FBP-1 / N-FBP-2 repair, or F* = 1 + 2n(n − 2)); P-N5-FX is SIGNED by both referees (REFEREE §C FX 9f736349; REFEREE-2 R2-N5-FX), not yet landed; P-N5-PHI LANDED as R47; (E) and (K_W) are bounded per stretch given its fallbacks by RESULTS R50 (P-N5-KW) — a READING for the assembly, outside this packet; the 𝒞^1O chain is assembled in RESULTS R51 (P-N5-1O). |
| NH42-N3 | §0.1 (R with o ∈ R, the R22 convention) and §5 (citing FX) | P-N5-FX and RESULTS R30 use R without o. NH's counts (crossings, intervals) are the same under either convention, since o ∈ R̄ always. |
