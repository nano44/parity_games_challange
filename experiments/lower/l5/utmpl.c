/* L-LOWER 5, BOX L5 step 2/4: search over UNIFORM LEVEL TEMPLATES on L^R_d (R110 wiring), IDEAL model (R104 definition).
   A template fixes, for every level l >= 1, member q, option k: the Xi-target (X, or mover 2(l+dl)+q2 with dl in [-DM, DP];
   out-of-range -> X), the parity, the rank offset (rank key = l*S + off[q][k], S = +-4, ranks = the order of the keys), the gate
   order of member q, the start bit (q, l mod 2). Level 0 has its own four (target, parity, offset) and gate bit. So G_d := the
   template unrolled on d levels: one rule for every d. Score: sum over the D values in DLIST of capped(G_d) (consecutive levels
   from 0 with F(l) = 2^(l+2) - 2) * 1000 + sum F(l) / 2^l (partial credit), cyclic templates rejected.
   Simulator core: same rules as l4/rclimb.c / l3/sim.py (A-sets on the old state, keys level by level on the new state).
   Usage: utmpl SEED ITERS RESTARTS  (env DLIST="6,8,10,12", DM=2, DP=3, OUT=file for the best template + its F profiles) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAXN 96
int d,N; int xt[MAXN*2], br[MAXN*2], bp[MAXN*2], gate[MAXN*2], st[MAXN];
static unsigned long long rs=88172645463325252ULL; static unsigned long long rnd(){rs^=rs<<13;rs^=rs>>7;rs^=rs<<17;return rs;}
static int ord_[MAXN], vis[MAXN];
static int dfs(int x){ if(vis[x]==2) return 1; if(vis[x]==1) return 0; vis[x]=1; for(int k=0;k<2;k++){int y=xt[2*x+k]; if(y>=0 && !dfs(y)) return 0;} vis[x]=2; return 1; }
static int no; static void topo(int x){ if(vis[x]) return; vis[x]=1; for(int k=0;k<2;k++){int y=xt[2*x+k]; if(y>=0) topo(y);} ord_[no++]=x; }
static int acyclic(){ memset(vis,0,sizeof vis); for(int x=0;x<N;x++) if(!dfs(x)) return 0; memset(vis,0,sizeof vis); no=0; for(int x=0;x<N;x++) topo(x); return 1; }
static int F[MAXN];
/* values: exact signed sums of 2^rank over chains; ranks < 4*MAXN: use arrays of limbs via long double is inexact, so compare
   chains exactly by the max-rank element of the symmetric difference (the Xi-order, R105 ENC). */
static int chain(int x,int k,const int*s,int*out){ int n=0; for(;;){ int m=2*x+k; out[n++]=m; int y=xt[m]; if(y<0) return n; x=y; k=s[y]; } }
static int better(int x,const int*s){ /* is the other option strictly better than the current one? */
  int a[MAXN+2], b[MAXN+2]; int na=chain(x,1-s[x],s,a), nb=chain(x,s[x],s,b);
  static int mark[MAXN*2]; static int stamp[MAXN*2]; static int gen=0; gen++;
  for(int i=0;i<na;i++){ stamp[a[i]]=gen; mark[a[i]]=1; }
  int best=-1, side=0; for(int i=0;i<nb;i++){ int m=b[i]; if(stamp[m]==gen && mark[m]==1){ mark[m]=2; continue; } if(br[m]>best){best=br[m]; side=-1;} }
  for(int i=0;i<na;i++){ int m=a[i]; if(mark[m]==2) continue; if(br[m]>best){best=br[m]; side=+1;} }
  if(best<0) return 0; int m=-1; for(int i=0;i<na;i++) if(br[a[i]]==best) m=a[i]; for(int i=0;i<nb;i++) if(br[b[i]]==best) m=b[i];
  int pos = bp[m]==0; /* even parity = +2^rank */ return side>0 ? pos : !pos; }
static int run(int TMAX){ int s[MAXN], ns[MAXN]; memcpy(s,st,sizeof(int)*N); memset(F,0,sizeof F);
  int T=0; int oprev[MAXN]; int have=0;
  for(;T<TMAX;){ int av[MAXN]; int any=0; for(int x=0;x<N;x++){ av[x]=better(x,s); any|=av[x]; } if(!any) break;
    int c=0, o[MAXN];
    for(int l=0;l<d;l++){ for(int q=0;q<2;q++){ int x=2*l+q; ns[x]=s[x];
        if(l==0){ if(av[x] && gate[2*x+1-s[x]] < gate[2*x+s[x]]) ns[x]=1-s[x]; }
        else if(av[x] && s[x]!=c) ns[x]=c; }
      if(l==0) o[0] = gate[2*0+ns[0]] > gate[2*1+ns[1]];
      else { int a=ns[2*l], b=ns[2*l+1]; o[l] = (a!=b)? (a!=c) : (gate[2*(2*l)+a] > gate[2*(2*l+1)+a]); }
      c=o[l]; }
    int ch=0; for(int x=0;x<N;x++) if(ns[x]!=s[x]) ch=1; if(!ch) break;
    if(!have){ int c0=0, o0[MAXN]; for(int l=0;l<d;l++){ if(l==0) o0[0]=gate[0+s[0]]>gate[2+s[1]]; else {int a=s[2*l],b=s[2*l+1]; o0[l]=(a!=b)?(a!=c0):(gate[4*l+a]>gate[4*l+2+a]);} c0=o0[l]; } memcpy(oprev,o0,sizeof(int)*d); have=1; }
    for(int l=0;l<d;l++){ if(o[l]!=oprev[l]) F[l]++; oprev[l]=o[l]; }
    memcpy(s,ns,sizeof(int)*N); T++; }
  return T; }
/* template */
#define PM 4
typedef struct { int dl[PM][2][2], q2[PM][2][2], isx[PM][2][2], par[PM][2][2], off[PM][2][2], g[PM][2], s0[2], salt[2]; int S;
  int z_dl[2][2], z_q2[2][2], z_isx[2][2], z_par[2][2], z_off[2][2], z_g; } Tm;
int DM=2, DP=3, P=1, SCRUN=0;
static void unroll(const Tm*t,int dd){ d=dd; N=2*d; int key[MAXN*2];
  for(int l=0;l<d;l++) for(int q=0;q<2;q++) for(int k=0;k<2;k++){ int m=2*(2*l+q)+k;
      int ph=l%P; int isx = l? t->isx[ph][q][k] : t->z_isx[q][k]; int dl = l? t->dl[ph][q][k] : t->z_dl[q][k]; int q2 = l? t->q2[ph][q][k] : t->z_q2[q][k];
      int L=l+dl; xt[m] = (isx || L<0 || L>=d) ? -1 : 2*L+q2; if(xt[m]==2*l+q) xt[m]=-1;
      bp[m] = l? t->par[ph][q][k] : t->z_par[q][k]; key[m] = l*t->S*8 + (l? t->off[ph][q][k] : t->z_off[q][k]);
      int gq = l? t->g[ph][q] : t->z_g; gate[m] = (l? 1000:0) + 4*(2*l+q) + (k ^ gq); }
  for(int x=0;x<N;x++){ int l=x/2,q=x%2; st[x] = t->s0[q] ^ (t->salt[q] & (l&1)); }
  /* ranks = order of keys (ties broken by index) */
  int idx[MAXN*2]; for(int m=0;m<2*N;m++) idx[m]=m;
  for(int i=1;i<2*N;i++){ int v=idx[i], j=i-1; while(j>=0 && (key[idx[j]]>key[v] || (key[idx[j]]==key[v] && idx[j]>v))){ idx[j+1]=idx[j]; j--; } idx[j+1]=v; }
  for(int r=0;r<2*N;r++) br[idx[r]]=r; }
static int DL[16], nD=0; static int lastF[16][MAXN], lastT[16];
static long score(const Tm*t){ long sc=0; for(int i=0;i<nD;i++){ unroll(t,DL[i]); if(!acyclic()) return -1000000000L; int T=run(20000); lastT[i]=T;
    int cap=0; while(cap<d && F[cap]==(1<<(cap+2))-2) cap++; double part=0; for(int l=0;l<d;l++){ double r=(double)F[l]/((1<<(l+2))-2); part+= r>1?1:r; }
    memcpy(lastF[i],F,sizeof(int)*d);
    if(SCRUN){ /* longest run of doubling levels F(l) = 2F(l-1)+2 with F(l-1) >= 1, then its top value */
      int best=0, top=0; for(int a=1;a<d;a++){ int h=0; while(a+h<d && F[a+h-1]>=1 && F[a+h]==2*F[a+h-1]+2) h++; if(h>best){best=h; top=F[a+h-1];} }
      double lg=0; for(int l=1;l<d;l++) if(F[l-1]>=1){ double r=(double)F[l]/(2*F[l-1]+2); lg += r>1?1:r; }
      sc += best*1000L + (long)(lg*40) + (T<400?T/4:100); }
    else sc += cap*1000L + (long)(part*50); } return sc; }
static void randt(Tm*t){ for(int q=0;q<2;q++) for(int k=0;k<2;k++){ for(int p=0;p<PM;p++){ t->dl[p][q][k]=-DM+(int)(rnd()%(DM+DP+1)); t->q2[p][q][k]=rnd()%2; t->isx[p][q][k]=rnd()%5==0; t->par[p][q][k]=rnd()%2; t->off[p][q][k]=rnd()%8; }
      t->z_dl[q][k]=(int)(rnd()%(DP+1)); t->z_q2[q][k]=rnd()%2; t->z_isx[q][k]=rnd()%4==0; t->z_par[q][k]=rnd()%2; t->z_off[q][k]=rnd()%8; }
  for(int q=0;q<2;q++){ for(int p=0;p<PM;p++) t->g[p][q]=rnd()%2; t->s0[q]=rnd()%2; t->salt[q]=rnd()%2; } t->z_g=rnd()%2; t->S= rnd()%2? 1:-1; }
static void mutate(Tm*t){ int q=rnd()%2,k=rnd()%2,p=rnd()%P; switch(rnd()%13){
  case 0: t->dl[p][q][k]=-DM+(int)(rnd()%(DM+DP+1)); break; case 1: t->q2[p][q][k]^=1; break; case 2: t->isx[p][q][k]^=1; break;
  case 3: t->par[p][q][k]^=1; break; case 4: t->off[p][q][k]=rnd()%8; break; case 5: t->g[p][q]^=1; break; case 6: t->s0[q]^=1; break;
  case 7: t->salt[q]^=1; break; case 8: t->S=-t->S; break; case 9: t->z_dl[q][k]=(int)(rnd()%(DP+1)); t->z_q2[q][k]=rnd()%2; break;
  case 10: t->z_isx[q][k]^=1; break; case 11: t->z_par[q][k]^=1; t->z_off[q][k]=rnd()%8; break; case 12: t->z_g^=1; break; } }
static void wrt(FILE*f,const Tm*t,long sc){ fprintf(f,"score %ld S %d\n",sc,t->S);
  for(int p=0;p<P;p++) for(int q=0;q<2;q++) for(int k=0;k<2;k++) fprintf(f,"lev%%%d=%d q%d k%d: %s dl %d q2 %d par %d off %d\n",P,p,q,k,t->isx[p][q][k]?"X":"T",t->dl[p][q][k],t->q2[p][q][k],t->par[p][q][k],t->off[p][q][k]);
  for(int q=0;q<2;q++) for(int k=0;k<2;k++) fprintf(f,"lev0 q%d k%d: %s dl %d q2 %d par %d off %d\n",q,k,t->z_isx[q][k]?"X":"T",t->z_dl[q][k],t->z_q2[q][k],t->z_par[q][k],t->z_off[q][k]);
  for(int p=0;p<P;p++) fprintf(f,"g[%d] %d %d\n",p,t->g[p][0],t->g[p][1]); fprintf(f,"z_g %d s0 %d %d salt %d %d\n",t->z_g,t->s0[0],t->s0[1],t->salt[0],t->salt[1]);
  score(t); for(int i=0;i<nD;i++){ fprintf(f,"d %d T %d F",DL[i],lastT[i]); for(int l=0;l<DL[i];l++) fprintf(f," %d",lastF[i][l]); fprintf(f,"\n"); } fflush(f); }
static void rdg(const char*fn){ FILE*f=fopen(fn,"r"); char w[64]; while(fscanf(f,"%63s",w)==1){ int n=0;
    if(!strcmp(w,"d")){ if(fscanf(f,"%d",&d)!=1) exit(1); N=2*d; continue; }
    int *a = !strcmp(w,"xt")?xt: !strcmp(w,"br")?br: !strcmp(w,"bp")?bp: !strcmp(w,"gate")?gate: !strcmp(w,"start")?st:NULL; if(!a) continue;
    n = !strcmp(w,"start")? N : 2*N; for(int i=0;i<n;i++) if(fscanf(f,"%d",&a[i])!=1) exit(1); } fclose(f); }
int main(int argc,char**argv){ if(getenv("GENOME")){ /* self-check mode: exact-order simulator on a text genome */
    rdg(getenv("GENOME")); if(!acyclic()) { printf("CYCLIC\n"); return 0; } int T=run(20000); printf("T %d F",T); for(int l=0;l<d;l++) printf(" %d",F[l]); printf("\n"); return 0; }
  rs+=atol(argv[1])*7919; long iters=atol(argv[2]); int rest=atoi(argv[3]);
  if(getenv("DM")) DM=atoi(getenv("DM")); if(getenv("P")) P=atoi(getenv("P")); if(getenv("SCRUN")) SCRUN=1; if(getenv("DP")) DP=atoi(getenv("DP"));
  char*dls=strdup(getenv("DLIST")?getenv("DLIST"):"6,8,10,12"); for(char*p=strtok(dls,",");p;p=strtok(NULL,",")) DL[nD++]=atoi(p);
  const char*out=getenv("OUT"); Tm best; long bsc=-2000000000L;
  for(int r=0;r<rest;r++){ Tm t; long sc; do{ randt(&t); sc=score(&t);}while(sc<0);
    for(long it=0;it<iters;it++){ Tm u=t; int nm=1+rnd()%2; for(int j=0;j<nm;j++) mutate(&u); long su=score(&u); if(su>=sc){ t=u; sc=su; } }
    if(sc>bsc){ bsc=sc; best=t; printf("restart %d best %ld\n",r,bsc); wrt(stdout,&best,bsc); if(out){ FILE*f=fopen(out,"w"); wrt(f,&best,bsc); fclose(f);} } }
  return 0; }
