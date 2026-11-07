/* L-LOWER box L3: search over UNIFORM (period-P) level templates of 2-wide degree-2 ladders L^R_d (R110 convention:
   option k of a mover of level l >= 1 W-points to mover 2(l-1)+k), evaluating mu(G_d) = max moves of a Xi-target mover of
   level >= 1, for d = DMIN..DMAX, from the template's own start. Own simulator (literal lexicographic keys, Xi-values as
   integers sum +-2^rank). Output: best templates as text genomes per d, to be re-checked by sim.py / movescheck.py.
   Usage: tsearch SEED ITERS PERIOD DMIN DMAX [mode]   mode 0: score = sum_d mu(d) ; 1: score = mu(DMAX)*100 + sum */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#define MAXD 24
#define MAXN (2*MAXD)
typedef __int128 i128;
typedef struct { int d, N; int wt[MAXN][2], xt[MAXN][2], rk[MAXN][2], par[MAXN][2], gate[MAXN][2]; int start[MAXN]; } Gen;
typedef struct { int xc[2][2], band[2][2], r[2][2], par[2][2], dlt[2], st[2]; } LevP;
typedef struct { int NB, P, TOP; LevP base[4], per[3], top, tops[4]; int dir[2]; int g0[4]; } Tpl;
static int TOPK=0;
static uint64_t rs=88172645463325252ULL; static inline uint64_t rnd(){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
#define NXC 20
/* xt codes: 0 X, 1/2 down1 q, 3/4 down2 q, 5 partner(2l -> 2l+1 if p=0 else X), 6/7 up1 q, 8/9 up2 q, 10/11 top pair q,
   12/13 level-0 pair q, 14/15 level-1 pair q.  Out-of-range -> X. */
static int target(int code, int l, int p, int d){
  int L, q;
  switch(code){ case 0: return -1; case 5: return p==0 ? 2*l+1 : -1;
    case 1: case 2: L=l-1; break; case 3: case 4: L=l-2; break; case 6: case 7: L=l+1; break; case 8: case 9: L=l+2; break;
    case 10: case 11: L=d-1; break; case 12: case 13: L=0; break; case 14: case 15: L=1; break;
    case 16: case 17: L=d-2; break; default: L=d-3; }
  q = (code==2||code==4||code==7||code==9||code==11||code==13||code==15||code==17||code==19);
  if (L<0 || L>=d) return -1; return 2*L+q; }
static const LevP *lp(const Tpl *T, int l, int d){ if (TOPK && l>=d-TOPK && l>=T->NB) return &T->tops[l-(d-TOPK)]; if (T->TOP && l==d-1 && l>=T->NB) return &T->top; if (l<T->NB) return &T->base[l]; return &T->per[(l-T->NB)%T->P]; }
static int build(const Tpl *T, int d, Gen *G){
  G->d=d; G->N=2*d; int N=G->N;
  long key[MAXN][2];
  for (int l=0;l<d;l++) for (int p=0;p<2;p++){ int x=2*l+p; const LevP *L=lp(T,l,d);
    for (int k=0;k<2;k++){
      G->wt[x][k] = l==0 ? -1 : 2*(l-1)+k;
      G->xt[x][k] = target(L->xc[p][k],l,p,d);
      G->par[x][k] = L->par[p][k];
      int band=L->band[p][k];
      key[x][k] = (long)band*100000 + (long)(T->dir[band]? l : (d-1-l))*16 + L->r[p][k]*2;
      if (l==0) G->gate[x][k] = T->g0[2*p+k];
      else { int dl = L->dlt[k]; G->gate[x][k] = 1000 + 4*l + 2*k + (p==0 ? (dl?0:1) : (dl?1:0)); }
    }
    G->start[x] = L->st[p];
  }
  /* ranks: sort options by key (ties broken by mover index) */
  int idx[2*MAXN]; int M=0; for (int x=0;x<N;x++) for(int k=0;k<2;k++) idx[M++]=x*2+k;
  for (int i=1;i<M;i++){ int v=idx[i], j=i; long kv=key[v/2][v%2]*1000+v; while(j>0 && key[idx[j-1]/2][idx[j-1]%2]*1000+idx[j-1] > kv){ idx[j]=idx[j-1]; j--; } idx[j]=v; }
  for (int i=0;i<M;i++) G->rk[idx[i]/2][idx[i]%2]=i;
  /* acyclicity: DFS on xt graph */
  int color[MAXN]={0}; int stack[MAXN*4]; 
  for (int s0=0;s0<N;s0++){ if (color[s0]) continue; /* iterative */
    int sp=0; stack[sp++]=s0; int it[MAXN]={0};
    while(sp){ int v=stack[sp-1]; if(color[v]==0) color[v]=1;
      if (it[v]<2){ int k=it[v]++; int w=G->xt[v][k]; if(w<0) continue; if(color[w]==1) return 0; if(color[w]==0) stack[sp++]=w; }
      else { color[v]=2; sp--; } } }
  return 1; }
static int topo[MAXN];
static void mktopo(const Gen *G){ /* order such that xt targets come first */
  int N=G->N, done[MAXN]={0}, n=0;
  while(n<N) for (int v=0;v<N;v++) if(!done[v]){ int ok=1; for(int k=0;k<2;k++){int w=G->xt[v][k]; if(w>=0&&!done[w]) ok=0;} if(ok){done[v]=1; topo[n++]=v;} } }
static inline i128 eps(const Gen *G,int x,int k){ i128 one=1; i128 e = one<<G->rk[x][k]; return G->par[x][k]==0? e : -e; }
/* key compare under state s: literal lexicographic keys, lowest level first */
static int keycmp(const Gen *G, const int *s, int x, int kx, int y, int ky){
  /* keys are (key(wt(x,kx), s) , gate(x,kx)); same length for same level */
  int a[MAXD], b[MAXD], n=0;
  int u=x, ku=kx, w=y, kw=ky;
  while(1){ a[n]=G->gate[u][ku]; b[n]=G->gate[w][kw]; n++; int wu=G->wt[u][ku], ww=G->wt[w][kw]; if(wu<0||ww<0) break; u=wu; ku=s[wu]; w=ww; kw=s[ww]; }
  for (int i=n-1;i>=0;i--){ if(a[i]<b[i]) return -1; if(a[i]>b[i]) return 1; } return 0; }
static int run(const Gen *G, const int *s0, int *mv, int cap){
  int N=G->N; int s[MAXN], ns[MAXN]; memcpy(s,s0,sizeof(int)*N); memset(mv,0,sizeof(int)*N);
  i128 cv[MAXN]; int T=0;
  while (T<cap){
    for (int i=0;i<N;i++){ int v=topo[i]; int w=G->xt[v][s[v]]; cv[v]=eps(G,v,s[v]) + (w>=0?cv[w]:0); }
    int any=0, A1[MAXN];
    for (int v=0;v<N;v++){ int o=1-s[v]; int w=G->xt[v][o]; i128 vo=eps(G,v,o)+(w>=0?cv[w]:0); A1[v] = vo>cv[v]; any|=A1[v]; }
    if(!any) break;
    memcpy(ns,s,sizeof(int)*N);
    for (int l=0;l<G->d;l++) for(int p=0;p<2;p++){ int x=2*l+p; if(!A1[x]) continue; int o=1-s[x];
      /* key of (x,o) vs (x,s[x]) under new state ns (lower levels already updated) */
      if (keycmp(G,ns,x,o,x,s[x])<0) ns[x]=o; }
    int ch=0; for(int v=0;v<N;v++) if(ns[v]!=s[v]){ch=1; mv[v]++;}
    if(!ch) break; memcpy(s,ns,sizeof(int)*N); T++; }
  return T; }
static int isZ[MAXN];
static int mu(const Gen *G, int *Tout){
  int mv[MAXN]; mktopo(G); memset(isZ,0,sizeof isZ);
  for(int v=0;v<G->N;v++) for(int k=0;k<2;k++) if(G->xt[v][k]>=0) isZ[G->xt[v][k]]=1;
  int T=run(G,G->start,mv,100000); if(Tout)*Tout=T; int m=0;
  for(int v=2;v<G->N;v++) if(isZ[v] && mv[v]>m) m=mv[v]; return m; }
static void randlev(LevP *L){ for(int p=0;p<2;p++){ for(int k=0;k<2;k++){ L->xc[p][k]=rnd()%NXC; L->band[p][k]=rnd()%2; L->r[p][k]=rnd()%8; L->par[p][k]=rnd()%2; } L->dlt[p]=rnd()%2; L->st[p]=rnd()%2; } }
static int NBG=1, PG=1, TOPG=0;
static void randtpl(Tpl *T, int P){
  T->P=P; T->NB=NBG; T->TOP=TOPG; for(int i=0;i<4;i++) randlev(&T->base[i]); for(int i=0;i<3;i++) randlev(&T->per[i]); randlev(&T->top); for(int i=0;i<4;i++) randlev(&T->tops[i]);
  T->dir[0]=rnd()%2; T->dir[1]=rnd()%2; for(int i=0;i<4;i++) T->g0[i]=i; for(int i=3;i>0;i--){int j=rnd()%(i+1); int t=T->g0[i]; T->g0[i]=T->g0[j]; T->g0[j]=t;} }
static void mutlev(LevP *L){ int w=rnd()%6, p=rnd()%2, k=rnd()%2;
  switch(w){ case 0: L->xc[p][k]=rnd()%NXC; break; case 1: L->band[p][k]^=1; break; case 2: L->r[p][k]=rnd()%8; break;
   case 3: L->par[p][k]^=1; break; case 4: L->dlt[p]^=1; break; default: L->st[p]^=1; } }
static void mutate(Tpl *T){
  int nsl = T->NB + T->P + (T->TOP?1:0) + 1 + TOPK; int w=rnd()%nsl;
  if (w>=T->NB + T->P + (T->TOP?1:0) + 1) { mutlev(&T->tops[w-(T->NB + T->P + (T->TOP?1:0) + 1)]); return; }
  if (w<T->NB) mutlev(&T->base[w]); else if (w<T->NB+T->P) mutlev(&T->per[w-T->NB]); else if (T->TOP && w==T->NB+T->P) mutlev(&T->top);
  else { if(rnd()%2) T->dir[rnd()%2]^=1; else { int i=rnd()%4,j=rnd()%4; int t=T->g0[i]; T->g0[i]=T->g0[j]; T->g0[j]=t; } } }
static int DMIN, DMAX, MODE;
static long score(const Tpl *T, int *mus){
  long sc=0; Gen G;
  for(int d=DMIN; d<=DMAX; d++){ if(!build(T,d,&G)) return -1000000000L; int m=mu(&G,NULL); mus[d]=m; sc+=m; }
  if (MODE==1) sc += 100L*mus[DMAX];
  if (MODE==2) { long mn=1000; for(int d=DMIN;d<=DMAX;d++){ long e=mus[d]-2L*d; if(e<mn) mn=e; } sc += 1000L*mn; }
  if (MODE==3) sc += 1000L*(mus[DMAX]-mus[DMIN]);
  if (MODE==4) { sc = 0; for(int d=DMIN; d<=DMAX; d++) sc += (long)mus[d] * (1L<<(d-DMIN)); }
  return sc; }
static void printgen(const Gen *G, FILE *f){
  fprintf(f,"d %d\nxt",G->d); for(int x=0;x<G->N;x++) for(int k=0;k<2;k++) fprintf(f," %d",G->xt[x][k]);
  fprintf(f,"\nbr"); for(int x=0;x<G->N;x++) for(int k=0;k<2;k++) fprintf(f," %d",G->rk[x][k]);
  fprintf(f,"\nbp"); for(int x=0;x<G->N;x++) for(int k=0;k<2;k++) fprintf(f," %d",G->par[x][k]);
  fprintf(f,"\ngate"); for(int x=0;x<G->N;x++) for(int k=0;k<2;k++) fprintf(f," %d",G->gate[x][k]);
  fprintf(f,"\nstart"); for(int x=0;x<G->N;x++) fprintf(f," %d",G->start[x]); fprintf(f,"\n"); }
static void prlev(const LevP *L, FILE *f){ for(int p=0;p<2;p++){ for(int k=0;k<2;k++) fprintf(f," [xc%d b%d r%d e%d]",L->xc[p][k],L->band[p][k],L->r[p][k],L->par[p][k]); fprintf(f," dl%d st%d",L->dlt[p],L->st[p]); } }
static void printtpl(const Tpl *T, FILE *f){
  fprintf(f,"TPL2 NB %d P %d TOP %d dir %d %d g0 %d %d %d %d",T->NB,T->P,T->TOP,T->dir[0],T->dir[1],T->g0[0],T->g0[1],T->g0[2],T->g0[3]);
  for(int i=0;i<T->NB;i++){ fprintf(f," | B"); prlev(&T->base[i],f); }
  for(int i=0;i<T->P;i++){ fprintf(f," | S"); prlev(&T->per[i],f); }
  if(T->TOP){ fprintf(f," | T"); prlev(&T->top,f); }
  fprintf(f,"\n"); }
static int pslev(const char **pp, LevP *L){ const char *p=*pp; int n;
  for(int q=0;q<2;q++){ for(int k=0;k<2;k++){ if(sscanf(p," [xc%d b%d r%d e%d]%n",&L->xc[q][k],&L->band[q][k],&L->r[q][k],&L->par[q][k],&n)<4) return 0; p+=n; }
    if(sscanf(p," dl%d st%d%n",&L->dlt[q],&L->st[q],&n)<2) return 0; p+=n; } *pp=p; return 1; }
static int parsetpl(const char *line, Tpl *T){
  memset(T,0,sizeof *T); const char *p=strstr(line,"TPL2"); if(!p) return 0; int n;
  if(sscanf(p,"TPL2 NB %d P %d TOP %d dir %d %d g0 %d %d %d %d%n",&T->NB,&T->P,&T->TOP,&T->dir[0],&T->dir[1],&T->g0[0],&T->g0[1],&T->g0[2],&T->g0[3],&n)<9) return 0; p+=n;
  for(int i=0;i<T->NB;i++){ while(*p==' '||*p=='|'||*p=='B') p++; if(!pslev(&p,&T->base[i])) return 0; }
  for(int i=0;i<T->P;i++){ while(*p==' '||*p=='|'||*p=='S') p++; if(!pslev(&p,&T->per[i])) return 0; }
  if(T->TOP){ while(*p==' '||*p=='|'||*p=='T') p++; if(!pslev(&p,&T->top)) return 0; }
  return 1; }
int main(int argc, char **argv){
  if(argc>1 && !strcmp(argv[1],"-g")){ /* -g "TPL line" dmin dmax : print genomes */
    Tpl T; if(!parsetpl(argv[2],&T)){ fprintf(stderr,"bad TPL\n"); return 1; } Gen G;
    for(int d=atoi(argv[3]); d<=atoi(argv[4]); d++){ if(!build(&T,d,&G)){ printf("# d %d CYCLIC\n",d); continue; } int T2, mv[MAXN]; int m=mu(&G,&T2); run(&G,G.start,mv,100000);
      printf("# d %d mu %d T %d moves",d,m,T2); for(int v=0;v<G.N;v++) printf(" %d",mv[v]); printf("\n"); printgen(&G,stdout);} return 0; }
  if(argc<6){ fprintf(stderr,"usage\n"); return 1; }
  rs ^= (uint64_t)atol(argv[1])*0x9E3779B97F4A7C15ULL; for(int i=0;i<10;i++) rnd();
  long iters=atol(argv[2]); int P=atoi(argv[3]); PG=P; if(getenv("NB")) NBG=atoi(getenv("NB")); if(getenv("TOPK")) TOPK=atoi(getenv("TOPK")); if(getenv("TOP")) TOPG=atoi(getenv("TOP")); DMIN=atoi(argv[4]); DMAX=atoi(argv[5]); MODE= argc>6? atoi(argv[6]) : 0;
  Tpl best, cur, nw; int mus[MAXD+1], bm[MAXD+1]; long bs=-2000000000L, cs=-2000000000L;
  for (long i=0;i<iters;i++){
    if (i%200000==0){ randtpl(&cur,P); cs=score(&cur,mus); }
    nw=cur; int nm=1+rnd()%3; for(int j=0;j<nm;j++) mutate(&nw);
    long s=score(&nw,mus);
    if (s>=cs){ cur=nw; cs=s; if (s>bs){ bs=s; best=nw; memcpy(bm,mus,sizeof mus);
        printf("it %ld score %ld mu:",i,bs); for(int d=DMIN;d<=DMAX;d++) printf(" %d",bm[d]); printf("\n"); fflush(stdout);} } }
  printf("BEST score %ld mu:",bs); for(int d=DMIN;d<=DMAX;d++) printf(" %d",bm[d]); printf("\n"); printtpl(&best,stdout);
  Gen G; for(int d=DMIN; d<=DMAX; d++){ build(&best,d,&G); int T; int m=mu(&G,&T); printf("# d %d mu %d T %d\n",d,m,T); printgen(&G,stdout);} 
  /* extend to larger d */
  for(int d=DMAX+1; d<=MAXD && d<=DMAX+6; d++){ if(!build(&best,d,&G)) break; int T; int m=mu(&G,&T); printf("# ext d %d mu %d T %d\n",d,m,T); }
  return 0; }
