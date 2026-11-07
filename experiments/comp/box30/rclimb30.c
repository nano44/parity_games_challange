/* L-COMP box 30: copy of L-LOWER 4's rclimb.c (claude/l-lower, see l-lower/COMMIT) with ONE change: the value type VT is a 192-bit
   signed integer (struct, hi*2^64 + lo) instead of __int128, so ranks up to 127 (d = 32: 128 options) do not overflow. Everything else
   (moves, scores, annealing, output) is unchanged. Original header:
   L-LOWER 4, box L4: structured perturbation climb on L^R_d (R110 wiring), IDEAL model (R104 definition), own simulator
   (same rules as l3/sim.py: A-sets on the old state, keys level by level on the new state, lexicographic W-chain keys).
   Input: text genome (d/xt/br/bp/gate/start; option m = 2x+k, beta index m). Env: FIX="m1,m2,..." options whose Xi-target is
   frozen; NOMUT="x1,.." movers whose options are not re-targeted; LV=l -> score F(l)*256 + min(T,255); SCORE=T -> T;
   ANNEAL=temp. Output: best genome text to OUT. Usage: rclimb in.txt seed iters */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAXN 64
int d,N; int xt[MAXN*2], br[MAXN*2], bp[MAXN*2], gate[MAXN*2], st[MAXN]; int fixo[MAXN*2];
static unsigned long long rs=88172645463325252ULL; static unsigned long long rnd(){rs^=rs<<13;rs^=rs>>7;rs^=rs<<17;return rs;}
static int ord_[MAXN], vis[MAXN];
static int dfs(int x){ if(vis[x]==2) return 1; if(vis[x]==1) return 0; vis[x]=1; for(int k=0;k<2;k++){int y=xt[2*x+k]; if(y>=0 && !dfs(y)) return 0;} vis[x]=2; return 1; }
static int no; static void topo(int x){ if(vis[x]) return; vis[x]=1; for(int k=0;k<2;k++){int y=xt[2*x+k]; if(y>=0) topo(y);} ord_[no++]=x; }
static int acyclic(){ memset(vis,0,sizeof vis); for(int x=0;x<N;x++) if(!dfs(x)) return 0; memset(vis,0,sizeof vis); no=0; for(int x=0;x<N;x++) topo(x); return 1; }
static int F[MAXN], MV[MAXN];
#define MAXT 5000
static int SS[MAXT+1][MAXN];   /* box 30: the run's states s_0..s_T (for the slack counter) */
/* box 30 (Lead 10:23Z): port of L-LOWER 5's experiments/lower/l5/slack.py counter (claude/l-lower 13b2b4d8) for ONE level j and
   need = H - j: windows of level j are cut at the steps where level j-1's key order flips (cuts = 1, those steps, T+1); in window
   [a, b) the moves of movers 2j, 2j+1 in step order (t, then 2j before 2j+1); PULSE = u2 - u1 (first two moves), GAP = first move of
   the next window - u2; a violation for each PULSE < need and each GAP < need (a window with < 2 moves, where slack.py would stop
   with an error, counts 1 violation). Key order per level as in run(). Also counts the (q-2, 1)-type windows (only mover 2j-1 moved
   at the window's first step, to option 1) with PULSE >= need and GAP >= need into *good. */
static void oflags(const int *s, int *o){ int c=0; for(int l=0;l<d;l++){ if(l==0) o[0]=gate[0+s[0]]>gate[2+s[1]];
    else { int a=s[2*l],b=s[2*l+1]; o[l]=(a!=b)?(a!=c):(gate[4*l+a]>gate[4*l+2+a]); } c=o[l]; } }
static int slack_viol(int T, int j, int need, int *good){
  static int O[MAXT+1][MAXN]; if(T>MAXT) return 1000000;
  for(int t=0;t<=T;t++) oflags(SS[t],O[t]);
  int p=2*j, q=2*j+1; int cuts[MAXT+3], nc=0; cuts[nc++]=1; for(int t=1;t<=T;t++) if(O[t][j-1]!=O[t-1][j-1]) cuts[nc++]=t; cuts[nc++]=T+1;
  int v=0; *good=0; int prev_u2=-1, prev_ok=0, prev_typ91=0, prev_pu=0;
  for(int w=0;w+1<nc;w++){ int a=cuts[w], b=cuts[w+1]; int u[2], nm=0;
    for(int t=a;t<b && nm<2;t++) for(int x=p;x<=q && nm<2;x++) if(SS[t][x]!=SS[t-1][x]) u[nm++]=t;
    int m8 = a>1 && SS[a][p-2]!=SS[a-1][p-2], m9 = a>1 && SS[a][q-2]!=SS[a-1][q-2]; int typ91 = !m8 && m9 && SS[a][q-2]==1;
    if(prev_ok){ int ga = (nm>=1)? u[0]-prev_u2 : -1; if(ga<need) v++; else if(prev_typ91 && prev_pu>=need) (*good)++; }
    if(nm<2){ v++; prev_ok=0; continue; }
    int pu=u[1]-u[0]; if(pu<need) v++;
    if(w+2==nc && typ91 && pu>=need) (*good)++;     /* last window: no GAP */
    prev_u2=u[1]; prev_ok=1; prev_typ91=typ91; prev_pu=pu; }
  return v; }
typedef struct { __int128 hi; unsigned long long lo; } VT;   /* value = hi*2^64 + lo, two's complement over 192 bits */
static VT vz(void){ VT z={0,0}; return z; }
static VT vadd(VT a, VT b){ VT r; r.lo=a.lo+b.lo; r.hi=a.hi+b.hi+(r.lo<a.lo); return r; }
static VT vneg(VT a){ VT r; r.lo=~a.lo+1ULL; r.hi=~a.hi+(a.lo==0ULL); return r; }
static int vgt(VT a, VT b){ return a.hi>b.hi || (a.hi==b.hi && a.lo>b.lo); }
static VT bv(int m){ VT b; int r=br[m]; if(r<64){ b.hi=0; b.lo=1ULL<<r; } else { b.hi=((__int128)1)<<(r-64); b.lo=0; } return bp[m]? vneg(b) : b; }
static int run(int *Tout){ int s[MAXN], ns[MAXN]; VT v[MAXN]; memcpy(s,st,sizeof(int)*N); memset(F,0,sizeof F); memset(MV,0,sizeof MV);
  int T=0; int oprev[MAXN]; int have=0; memcpy(SS[0],s,sizeof(int)*N);
  for(;T<5000;){ for(int i=0;i<N;i++){int x=ord_[i]; int m=2*x+s[x]; v[x]=vadd(bv(m), xt[m]>=0? v[xt[m]]:vz());}
    int av[MAXN]; int any=0; for(int x=0;x<N;x++){ int m=2*x+1-s[x]; VT ov=vadd(bv(m), xt[m]>=0? v[xt[m]]:vz()); av[x]= vgt(ov,v[x]); any|=av[x]; }
    if(!any) break;
    int c=0, o[MAXN];
    for(int l=0;l<d;l++){ for(int q=0;q<2;q++){ int x=2*l+q; ns[x]=s[x];
        if(l==0){ if(av[x] && gate[2*x+1-s[x]] < gate[2*x+s[x]]) ns[x]=1-s[x]; }
        else if(av[x] && s[x]!=c) ns[x]=c; }
      if(l==0) o[0] = gate[2*0+ns[0]] > gate[2*1+ns[1]];
      else { int a=ns[2*l], b=ns[2*l+1]; o[l] = (a!=b)? (a!=c) : (gate[2*(2*l)+a] > gate[2*(2*l+1)+a]); }
      c=o[l]; }
    int ch=0; for(int x=0;x<N;x++) if(ns[x]!=s[x]){ch=1; MV[x]++;} if(!ch) break;
    if(!have){ /* o at s_0 */ int c0=0, o0[MAXN]; for(int l=0;l<d;l++){ if(l==0) o0[0]=gate[0+s[0]]>gate[2+s[1]]; else {int a=s[2*l],b=s[2*l+1]; o0[l]=(a!=b)?(a!=c0):(gate[4*l+a]>gate[4*l+2+a]);} c0=o0[l]; } memcpy(oprev,o0,sizeof(int)*d); have=1; }
    for(int l=0;l<d;l++){ if(o[l]!=oprev[l]) F[l]++; oprev[l]=o[l]; }
    memcpy(s,ns,sizeof(int)*N); T++; if(T<=MAXT) memcpy(SS[T],s,sizeof(int)*N); }
  *Tout=T; return T; }
static int LV=-1, SCT=0, SCH=0; static int SLV=-1, SLG=-1;
/* box 30 (Lead 17:27Z): port of L-LOWER 6 guard_l6.score (claude/l-lower bca48384, guard_l6.py sha1 18e85589): lexicographic
   (min(caps, 6), -npaths(q5, {12, 13}), F(6)), encoded as caps*10^9 - min(npaths, 99999)*10^4 + F(6). caps = number of leading levels l
   with F(l) = 2^(l+2) - 2. q5 = second mover of pair 5 from roles(): level-5 windows cut at the flips of key o(4) (cuts 1, flips, T+1);
   the first window with EXACTLY two moves of movers 10, 11 (in step order, 10 before 11 within a step) at different steps -> q5 = the
   second; none -> q5 = 10 (as score()). npaths: Xi-paths over the DISTINCT targets of each option pair, 1 at a mover in {12, 13}.
   L6Q5/L6NP/L6CAPS hold the last values (written to OUT). */
static int L6Q5=-1, L6CAPS=-1; static long long L6NP=-1; static int L6NS=-1, L6C24=-1;
static long long np_memo[MAXN]; static int np_done[MAXN];
static long long np_f(int x){ if(x==12||x==13) return 1; if(np_done[x]) return np_memo[x]; long long r=0; int a=xt[2*x], b=xt[2*x+1];
  if(a>=0) r+=np_f(a); if(b>=0 && b!=a) r+=np_f(b); if(r>1000000000LL) r=1000000000LL; np_done[x]=1; np_memo[x]=r; return r; }
static long l6score(int T){ int caps=0; for(int l=0;l<d;l++){ if(F[l]==(1<<(l+2))-2) caps++; else break; } if(caps>6) caps=6;
  int q5=-1; if(T<=MAXT){ static int O[MAXT+1][MAXN]; for(int t=0;t<=T;t++) oflags(SS[t],O[t]);
    int cuts[MAXT+3], nc=0; cuts[nc++]=1; for(int t=1;t<=T;t++) if(O[t][4]!=O[t-1][4]) cuts[nc++]=t; cuts[nc++]=T+1;
    for(int w=0;w+1<nc && q5<0;w++){ int a=cuts[w], e=cuts[w+1]-1, n=0, mt[3], mx[3];
      for(int t=a;t<=e && n<3;t++) for(int x=10;x<=11 && n<3;x++) if(SS[t][x]!=SS[t-1][x]){ mt[n]=t; mx[n]=x; n++; }
      if(n==2 && mt[0]!=mt[1]) q5=mx[1]; } }
  L6Q5=q5; int src = q5>=0? q5 : 10; memset(np_done,0,sizeof np_done); long long np=0; int a=xt[2*src], b=xt[2*src+1];
  if(a>=0) np+=np_f(a); if(b>=0 && b!=a) np+=np_f(b); L6NP=np; L6CAPS=caps;
  long long npc = np>99999? 99999 : np;
  if(getenv("L6W")){ /* Lead 21:36Z (L-LOWER 8, L8-design §1c): (caps, [F6 >= L6GATE], -npaths, -#length-1 6-windows, F6); 6-windows as
       guard_l6.windows(S, O, 6): cuts 1, the flips of o(5), T+1; window [a, next cut - 1]; length 1 <=> next cut - a == 1. Guard: options
       20 (10:0) -> 17 and 34 (17:0) -> 22 must hold (else score -10^15). */
    if(xt[20]!=17 || xt[34]!=22) return -1000000000000000L;
    int ns=-1; if(T<=MAXT){ static int O6[MAXT+1][MAXN]; for(int t=0;t<=T;t++) oflags(SS[t],O6[t]); int prev=1; ns=0;
      for(int t=1;t<=T;t++) if(O6[t][5]!=O6[t-1][5]){ if(t-prev==1) ns++; prev=t; } if(T+1-prev==1) ns++; }
    if(ns<0) ns=9999; L6NS=ns; int g = F[6] >= (getenv("L6GATE")? atoi(getenv("L6GATE")) : 0); long long npc2 = np>999? 999 : np;
    if(getenv("L6W24")){ /* Lead 23:48Z (L-LOWER 8 c6a8980f §1e): + c24 = number of steps t in 1..min(T, L6W24-1) with o(24) changed; order
         (caps, gate, -npaths, -n1, c24, F6) = caps*1e13 + g*1e12 - npaths*1e9 - n1*1e6 + c24*1e3 + F6 */
      int lim=atoi(getenv("L6W24"))-1, c24=0; if(T<=MAXT){ static int O7[MAXT+1][MAXN]; for(int t=0;t<=T;t++) oflags(SS[t],O7[t]);
        for(int t=1;t<=T && t<=lim;t++) if(O7[t][24]!=O7[t-1][24]) c24++; } L6C24=c24;
      return (long)caps*10000000000000L + (long)g*1000000000000L - npc2*1000000000L - (long)(ns>999?999:ns)*1000000L + (long)c24*1000L + F[6]; }
    return (long)caps*1000000000000L + (long)g*100000000000L - npc2*100000000L - (long)ns*10000L + F[6]; }
  if(getenv("L6GATE")){ int g = F[6] >= atoi(getenv("L6GATE")); return (long)caps*10000000000L + (long)g*1000000000L - npc*10000L + F[6]; }  /* Lead 17:42Z: (caps, [F6>=gate], -npaths, F6) */
  return (long)caps*1000000000L - npc*10000L + F[6]; }
static long score(int *T){ run(T); if(SCT) return *T;
  if(getenv("L6SCORE")) return l6score(*T);
  if(getenv("GUARD") && LV>=1){ int g=atoi(getenv("GUARD")); long pen=0; for(int l=1;l<=g;l++){ int df=2*F[l-1]+2-F[l]; if(F[0]!=2) df+=4; pen += df<0?-df:df; } if(pen) return -100000L*pen + F[LV]; }
  if(getenv("SLACKH") && LV>=0){ int H=atoi(getenv("SLACKH")), j=H-2, g; int v=slack_viol(*T,j,H-j,&g); SLV=v; SLG=g; return -1000L*v + F[LV]; }
  if(getenv("ANYRUN")){ long best=-1000000; for(int a=1;a<d;a++){ int h=0; while(a+h<d && F[a+h]==2*F[a+h-1]+2 && F[a+h]>0) h++; long sc=3000L*h + 4L*F[a+h-1>=0?a+h-1:0]; if(a+h<d){int def=2*F[a+h-1]+2-F[a+h]; sc -= 100L*(def<0?-def:def);} if(sc>best)best=sc; } return best; }
  if(SCH){ long sc=0; for(int l=1;l<=SCH;l++){ int def=2*F[l-1]+2-F[l]; sc += def==0? 3000 : -200*(def<0?-def:def); } return sc + 16L*F[SCH] + (*T<15?*T:15); } if(LV>=0) return (long)F[LV]*256 + (*T<255?*T:255); return *T; }
static void rd(const char*fn){ FILE*f=fopen(fn,"r"); char w[64]; while(fscanf(f,"%63s",w)==1){ int n=0;
    if(!strcmp(w,"d")){ if(fscanf(f,"%d",&d)!=1) exit(1); N=2*d; continue; }
    int *a = !strcmp(w,"xt")?xt: !strcmp(w,"br")?br: !strcmp(w,"bp")?bp: !strcmp(w,"gate")?gate: !strcmp(w,"start")?st:NULL; if(!a) continue;
    n = !strcmp(w,"start")? N : 2*N; for(int i=0;i<n;i++) if(fscanf(f,"%d",&a[i])!=1) exit(1); } fclose(f); }
static void wr(const char*fn, long sc, int T){ FILE*f=fopen(fn,"w"); fprintf(f,"d %d\nxt",d); for(int i=0;i<2*N;i++)fprintf(f," %d",xt[i]);
  fprintf(f,"\nbr"); for(int i=0;i<2*N;i++)fprintf(f," %d",br[i]); fprintf(f,"\nbp"); for(int i=0;i<2*N;i++)fprintf(f," %d",bp[i]);
  fprintf(f,"\ngate"); for(int i=0;i<2*N;i++)fprintf(f," %d",gate[i]); fprintf(f,"\nstart"); for(int i=0;i<N;i++)fprintf(f," %d",st[i]);
  fprintf(f,"\n# score %ld T %d F",sc,T); for(int l=0;l<d;l++)fprintf(f," %d",F[l]); fprintf(f," moves"); for(int x=0;x<N;x++)fprintf(f," %d",MV[x]); if(SLV>=0) fprintf(f," slack_viol %d good91 %d",SLV,SLG); if(L6CAPS>=0) fprintf(f," l6_caps %d l6_q5 %d l6_npaths %lld",L6CAPS,L6Q5,L6NP); if(L6NS>=0) fprintf(f," l6_len1w6 %d",L6NS); if(L6C24>=0) fprintf(f," l6_c24 %d",L6C24); fprintf(f,"\n"); fclose(f); }
int main(int argc,char**argv){ rd(argv[1]); rs+=atol(argv[2])*7919; long iters=atol(argv[3]);
  if(getenv("LV")) LV=atoi(getenv("LV")); if(getenv("SCORE")&&!strcmp(getenv("SCORE"),"T")) SCT=1; if(getenv("CHAIN")) SCH=atoi(getenv("CHAIN"));
  int nomut[MAXN]={0}; int FB = getenv("FROZENBELOW")? atoi(getenv("FROZENBELOW")) : 0; /* movers < FB: no field mutated */
  if(getenv("FIX")){ char*p=strdup(getenv("FIX")); for(char*t=strtok(p,",");t;t=strtok(NULL,",")) fixo[atoi(t)]=1; }
  if(getenv("NOMUT")){ char*p=strdup(getenv("NOMUT")); for(char*t=strtok(p,",");t;t=strtok(NULL,",")) {int x=atoi(t); nomut[x]=1; fixo[2*x]=fixo[2*x+1]=1;} }
  int NMIN=getenv("NMIN")?atoi(getenv("NMIN")):1, NMAX=getenv("NMAX")?atoi(getenv("NMAX")):3; if(NMAX<NMIN) NMAX=NMIN;
  int biasm[MAXN], nbias=0, bias19=getenv("BIAS19")?atoi(getenv("BIAS19")):-1, biasr=getenv("BIASR")?atoi(getenv("BIASR")):87; double biasp=getenv("BIASP")?atof(getenv("BIASP")):0.5; double bias19p=getenv("BIAS19P")?atof(getenv("BIAS19P")):0.25;
  if(getenv("BIAS")){ char*p=strdup(getenv("BIAS")); for(char*t=strtok(p,",");t;t=strtok(NULL,",")){ int x=atoi(t); if(x<FB||x>=N){ fprintf(stderr,"BIAS mover %d outside [FB,N)\n",x); return 1; } biasm[nbias++]=x; } }
  if(bias19>=0 && (bias19<FB||bias19>=N)){ fprintf(stderr,"BIAS19 outside [FB,N)\n"); return 1; }
  static int frz[MAXN]; if(getenv("FROZENSET")){ char*p=strdup(getenv("FROZENSET")); for(char*t=strtok(p,",");t;t=strtok(NULL,",")) frz[atoi(t)]=1; }   /* movers whose fields never change */
  int rept[MAXN*2], nrept=0; if(getenv("REPT")){ char*p=strdup(getenv("REPT")); for(char*t=strtok(p,",");t;t=strtok(NULL,",")) rept[nrept++]=atoi(t); }
  const char*testout=getenv("TESTOUT"); int tested=0; if(testout){ FILE*e=fopen(testout,"r"); if(e){ tested=1; fclose(e); } }   /* first test genome only, across units */
  double temp=getenv("ANNEAL")?atof(getenv("ANNEAL")):0; const char*out=getenv("OUT")?getenv("OUT"):"/dev/null";
  if(!acyclic()){ fprintf(stderr,"input cyclic\n"); return 1; }
  int T; long cur=score(&T), best=cur; wr(out,best,T);
  if(getenv("SLACKDBG")){ int H=atoi(getenv("SLACKDBG")); for(int j=1;j<=H-2;j++){ int g; printf("slack j %d need %d: %s violations %d\n", j, H-j, F[j]==2*F[j-1]+2?"doubling":"NOT doubling", slack_viol(T,j,H-j,&g)); } } printf("start score %ld T %d F(LV) %d\n",cur,T,LV>=0?F[LV]:-1); fflush(stdout);
  int sxt[MAXN*2],sbr[MAXN*2],sbp[MAXN*2],sg[MAXN*2],sst[MAXN];
  for(long it=0;it<iters;it++){ memcpy(sxt,xt,sizeof xt);memcpy(sbr,br,sizeof br);memcpy(sbp,bp,sizeof bp);memcpy(sg,gate,sizeof gate);memcpy(sst,st,sizeof st);
    int nm=NMIN+rnd()%(NMAX-NMIN+1);
    /* box 30 (Lead 11:42Z) FUEL BIAS: with probability BIASP one of the nm edits is a fuel edit on a mover w of BIAS (default: drawn
       uniformly; with prob 1/4 w = BIAS19 if set): option m = 2w + k (k random); (a) prob 1/2: swap br[m] with a random option m2 >= 2FB
       whose rank > BIASR (m gets a rank above BIASR); (b) prob 1/2: flip bp[m]; (c) prob 1/2: re-target xt[m] to a random mover that owns
       an option m2 >= 2FB of rank > BIASR; at least one of (a)-(c) is applied. Movers of BIAS must be >= FB (checked at start). */
    if(nbias && (rnd()%1000000) < (unsigned long long)(biasp*1e6)){ int w = (bias19>=0 && (rnd()%1000000) < (unsigned long long)(bias19p*1e6))? bias19 : biasm[rnd()%nbias];   /* BIAS19P default 0.25 = the original 1/4 */ int m=2*w+rnd()%2;
      int hi[MAXN*2], nh=0; for(int m2=2*FB;m2<2*N;m2++) if(br[m2]>biasr && m2!=m) hi[nh++]=m2; int done=0;
      while(!done){ if(nh && rnd()%2){ int m2=hi[rnd()%nh]; int t=br[m];br[m]=br[m2];br[m2]=t; done=1; }
        if(rnd()%2){ bp[m]^=1; done=1; }
        if(nh && !fixo[m] && rnd()%2){ int y=hi[rnd()%nh]/2; if(y!=w){ xt[m]=y; done=1; } } }
      nm--; }
    if(nrept && nm>0 && rnd()%4==0){ int m=rept[rnd()%nrept]; int y=(int)(rnd()%(N+1))-1; if(y==m/2) y=-1; xt[m]=y; nm--; }   /* REPT re-point */
    for(int q=0;q<nm;q++){   /* box 30 (Lead 11:38Z): NMIN..NMAX edits per proposal (default 1..3 = original) */ int r=rnd()%6; int m=2*FB+rnd()%(2*N-2*FB);
      if(frz[m/2]) continue;   /* FROZENSET (Lead 21:46Z): no field of a frozen mover changes */
      if(r==0||r==5){ if(fixo[m]) continue; int y=(int)(rnd()%(N+1))-1; if(y==m/2) y=-1; xt[m]=y; }
      else if(r==1){ int m2=2*FB+rnd()%(2*N-2*FB); if(frz[m2/2]) continue; int t=br[m];br[m]=br[m2];br[m2]=t; }
      else if(r==2){ bp[m]^=1; }
      else if(r==3){ int x=m/2,l=x/2,k=m%2; if(frz[2*l]||frz[2*l+1]) continue; if(l==0){ int m2=rnd()%4; int t=gate[m];gate[m]=gate[m2];gate[m2]=t; if(m>=4){} } else { int a=4*l+k, b=4*l+2+k; int t=gate[a];gate[a]=gate[b];gate[b]=t; } }
      else { int xs=FB+rnd()%(N-FB); if(frz[xs]) continue; st[xs]^=1; } }
    /* level-0 gate swaps must stay within level 0: m<4 guaranteed only if x<2; enforce */
    if(!acyclic()){ memcpy(xt,sxt,sizeof xt);memcpy(br,sbr,sizeof br);memcpy(bp,sbp,sizeof bp);memcpy(gate,sg,sizeof gate);memcpy(st,sst,sizeof st); acyclic(); continue; }
    long sc=score(&T); double tt=temp*(1.0-(double)it/iters);
    if(testout && !tested && L6CAPS>=6 && L6Q5>=0 && L6NP==0 && (!getenv("TESTGATE") || F[6]>=atoi(getenv("TESTGATE")))){ tested=1; wr(testout,sc,T); printf("TEST it %ld caps 6 q5 %d npaths 0 F(6) %d\n",it,L6Q5,F[6]); fflush(stdout); }
    if(sc>=cur || (tt>0 && (rnd()%1000000)/1e6 < exp((double)(sc-cur)/(tt*(LV>=0?256:((SCH||getenv("ANYRUN"))?200:1)))))){ cur=sc; if(sc>best){ best=sc; wr(out,best,T); printf("it %ld score %ld T %d F",it,sc,T); for(int l=0;l<d;l++)printf(" %d",F[l]); printf("\n"); fflush(stdout);} }
    else { memcpy(xt,sxt,sizeof xt);memcpy(br,sbr,sizeof br);memcpy(bp,sbp,sizeof bp);memcpy(gate,sg,sizeof gate);memcpy(st,sst,sizeof st); acyclic(); } }
  return 0; }
