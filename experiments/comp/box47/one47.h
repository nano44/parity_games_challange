/* L-COMP box 47: C port of L-NEW's one-player model 1P(G) (claude/l-new a32a588d experiments/new/box217/one217.py, class OneP, rules
   key / howard / seq), written line by line from that file. Genome: gen47.h (Ξ-acyclic); eps(x, k) = er[option] (the e-slot rank; one217's
   eidx / G["gate"] enter only through their ORDER, and er orders options as box 189's e-indices do when er = gt).
   Ξ_s(x, k) = (w, hops): w = Σ over the β-ids on the Ξ-chain x -k-> β(x, k) -> xt(x, k) -s-> ... of +2^rank (even β priority) or −2^rank
   (odd), rank = position of the β priority 6 + 2 br + bp in ascending (priority, β-id) order; hops = chain length; larger (w, hops) better.
   EXACT arithmetic: on a Ξ-acyclic genome a chain holds each β-id at most once, so w is stored as the SET of its ranks (a bitset; the sign
   of a rank is fixed by its parity) and two w are compared by the highest rank in their symmetric difference (no unit-cost big integers).
   A_s(x) = {s(x)} ∪ {k : Ξ_s(x, k) > Ξ_s(x, s(x))}. key rule: levels from 0 up (movers in (lev, index) order, as one217's bylev);
   s'(x) = argmin over A_s(x) of key(x, k) = key(wt, s'(wt)) + (eps(x, k)) — compared as (key rank of wt among its level, eps), since all keys
   of one level have one length and distinct movers' keys differ. howard: argmax Ξ_s over A_s(x). seq: s' of the key rule at the least-index
   mover where it differs. Run: stop when every |A_s(x)| = 1 or s' = s. T = number of steps; sw[x] = steps at which mover x switches.
   Control ONE47_CTRL=1: eps replaced by a fixed pseudo-random permutation of the e-ranks (the permuted-key control; must fire mism). */
#ifndef ONE47_H
#define ONE47_H
#define OW ((GMAXM + 63) / 64)
typedef unsigned long long u64;
static int o_topo[GMAXN], o_bylev[GMAXN], o_rank[GMAXM], o_eps[GMAXM], o_ctrl = -1;
static int o_W;                                     /* words used */
static u64 o_mv[GMAXN][OW]; static int o_mh[GMAXN];  /* Ξ value of each mover's chosen option: rank set + hops */
static int o_odd[GMAXM];                             /* rank -> 1 if that β priority is odd */
static int o_cmpset(const u64 *a, const u64 *b) {    /* compare w(a) vs w(b): +1, 0, -1 */
  for (int j = o_W - 1; j >= 0; j--) { u64 d = a[j] ^ b[j]; if (d) { int r = 64 * j + 63 - __builtin_clzll(d); int ina = (a[j] >> (r & 63)) & 1;
      int pos = !o_odd[r]; return (ina == pos) ? 1 : -1; } } return 0; }
/* value of option i given mover values: set = mv[xt] + {rank(i)}, hops = mh[xt] + 1; compare option i vs option j (same mover) */
static int o_cmpopt(const Gen *g, int i, int j) {
  static u64 a[OW], b[OW]; int yi = g->xt[i], yj = g->xt[j];
  for (int w = 0; w < o_W; w++) { a[w] = yi >= 0 ? o_mv[yi][w] : 0; b[w] = yj >= 0 ? o_mv[yj][w] : 0; }
  a[o_rank[i] >> 6] |= 1ULL << (o_rank[i] & 63); b[o_rank[j] >> 6] |= 1ULL << (o_rank[j] & 63);
  int c = o_cmpset(a, b); if (c) return c; int hi = (yi >= 0 ? o_mh[yi] : 0) + 1, hj = (yj >= 0 ? o_mh[yj] : 0) + 1; return (hi > hj) - (hi < hj); }
static int o_nt;
static void o_setup(const Gen *g) {
  int M = g->M, N = g->N; o_W = (M + 63) / 64;
  /* β rank: ascending (priority 6 + 2 br + bp, β-id); β-id = option index in canonical order (one217: b = opts[x][k][2], our gen47 j2t keeps it) */
  static int ord[GMAXM]; for (int i = 0; i < M; i++) ord[i] = i;
  for (int i = 1; i < M; i++) { int v = ord[i], pv = 6 + 2 * g->br[v] + g->bp[v], j = i - 1;
    while (j >= 0) { int u = ord[j], pu = 6 + 2 * g->br[u] + g->bp[u]; if (pu > pv || (pu == pv && u > v)) { ord[j + 1] = u; j--; } else break; } ord[j + 1] = v; }
  for (int r = 0; r < M; r++) { o_rank[ord[r]] = r; o_odd[r] = (6 + 2 * g->br[ord[r]] + g->bp[ord[r]]) & 1; }
  for (int i = 0; i < M; i++) o_eps[i] = g->er[i];
  if (o_ctrl < 0) { const char *c = getenv("ONE47_CTRL"); o_ctrl = c && !strcmp(c, "1"); }
  if (o_ctrl) { static int pm[GMAXM]; for (int i = 0; i < M; i++) pm[i] = i; u64 s = 5; for (int i = M - 1; i > 0; i--) { s = s * 6364136223846793005ULL + 1442695040888963407ULL; int j = (int)((s >> 33) % (u64)(i + 1)); int t = pm[i]; pm[i] = pm[j]; pm[j] = t; }
    for (int i = 0; i < M; i++) o_eps[i] = pm[g->er[i]]; }
  /* topological order of the Ξ-DAG, targets first (one217: visit(x) recursively over options in order, append after) */
  static int seen[GMAXN], stk[GMAXN], it[GMAXN]; memset(seen, 0, sizeof(int) * N); o_nt = 0;
  for (int x0 = 0; x0 < N; x0++) { if (seen[x0]) continue; int sp = 0; stk[sp] = x0; it[sp] = g->first[x0]; seen[x0] = 1;
    while (sp >= 0) { int x = stk[sp]; if (it[sp] < g->first[x + 1]) { int y = g->xt[it[sp]++]; if (y >= 0 && !seen[y]) { seen[y] = 1; sp++; stk[sp] = y; it[sp] = g->first[y]; } }
      else { o_topo[o_nt++] = x; sp--; } } }
  /* bylev: sorted by level, stable in index (python sorted is stable) */
  int n = 0, maxl = 0; for (int x = 0; x < N; x++) if (g->lev[x] > maxl) maxl = g->lev[x];
  for (int l = 0; l <= maxl; l++) for (int x = 0; x < N; x++) if (g->lev[x] == l) o_bylev[n++] = x; }
static void o_values(const Gen *g, const int *s) {   /* mv[x] = Ξ_s(x, s(x)) in topological order */
  for (int t = 0; t < o_nt; t++) { int x = o_topo[t], i = g->first[x] + s[x], y = g->xt[i];
    for (int w = 0; w < o_W; w++) o_mv[x][w] = y >= 0 ? o_mv[y][w] : 0; o_mv[x][o_rank[i] >> 6] |= 1ULL << (o_rank[i] & 63); o_mh[x] = (y >= 0 ? o_mh[y] : 0) + 1; } }
/* one step from s (option index k per mover) under rule 0 key, 1 howard, 2 seq; writes t; returns 0 = stop (no improving option), 1 = moved */
static int o_krank[GMAXN];
static int o_step(const Gen *g, const int *s, int *t, int rule) {
  int N = g->N, any = 0; static unsigned char A[GMAXM];
  o_values(g, s);
  for (int x = 0; x < N; x++) { int c = g->first[x] + s[x]; for (int i = g->first[x]; i < g->first[x + 1]; i++) { A[i] = (i == c) || o_cmpopt(g, i, c) > 0; if (i != c && A[i]) any = 1; } }
  if (!any) return 0;
  if (rule == 1) { for (int x = 0; x < N; x++) { int b = -1; for (int i = g->first[x]; i < g->first[x + 1]; i++) if (A[i] && (b < 0 || o_cmpopt(g, i, b) > 0)) b = i; t[x] = b - g->first[x]; } return 1; }
  /* key rule, level by level; krank of a mover = rank of its key among its level (computed after the level is done) */
  static int tmp[GMAXN]; int p = 0;
  while (p < N) { int l = g->lev[o_bylev[p]], q = p; while (q < N && g->lev[o_bylev[q]] == l) q++;
    for (int a = p; a < q; a++) { int x = o_bylev[a], b = -1; long bk = 0;
      for (int i = g->first[x]; i < g->first[x + 1]; i++) if (A[i]) { long kk = ((long)(l > 0 && g->wt[i] >= 0 ? o_krank[g->wt[i]] : 0) << 32) | (long)o_eps[i];
          if (b < 0 || kk < bk) { b = i; bk = kk; } }
      tmp[x] = b - g->first[x]; t[x] = tmp[x]; }
    /* rank this level's keys: key(x) = (krank(wt(x, t(x))), eps(x, t(x))) — sort the level's movers by it (insertion sort; levels are small) */
    static int lv[GMAXN]; static long kv[GMAXN]; int m = 0;
    for (int a = p; a < q; a++) { int x = o_bylev[a], i = g->first[x] + t[x]; long kk = ((long)(l > 0 && g->wt[i] >= 0 ? o_krank[g->wt[i]] : 0) << 32) | (long)o_eps[i];
      int j = m - 1; while (j >= 0 && kv[j] > kk) { kv[j + 1] = kv[j]; lv[j + 1] = lv[j]; j--; } kv[j + 1] = kk; lv[j + 1] = x; m++; }
    for (int j = 0; j < m; j++) o_krank[lv[j]] = j;
    p = q; }
  if (rule == 2) { int d = -1; for (int x = 0; x < N; x++) if (t[x] != s[x]) { d = x; break; } for (int x = 0; x < N; x++) t[x] = s[x]; if (d >= 0) t[d] = tmp[d]; }
  return 1; }
/* full run; returns T; sw[x] switches per mover; if STATES != NULL, appends the states (N ints each) up to cap */
static int *o_states; static long o_nstates;
static long run_rule(const Gen *g, long cap, long *sw, int rule) {
  static int s[GMAXN], t[GMAXN]; o_setup(g); for (int x = 0; x < g->N; x++) { s[x] = g->st[x]; if (sw) sw[x] = 0; }
  if (o_states) { memcpy(o_states, s, sizeof(int) * g->N); o_nstates = 1; }
  long T = 0;
  while (T < cap) { if (!o_step(g, s, t, rule)) break; int same = 1; for (int x = 0; x < g->N; x++) if (t[x] != s[x]) { same = 0; if (sw) sw[x]++; }
    if (same) break; memcpy(s, t, sizeof(int) * g->N); T++;
    if (o_states) { memcpy(o_states + (size_t)o_nstates * g->N, s, sizeof(int) * g->N); o_nstates++; } }
  return T; }
static long run1p(const Gen *g, long cap, long *sw) { return run_rule(g, cap, sw, 0); }
#endif
