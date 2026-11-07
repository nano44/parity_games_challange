/* L-LOWER 4, box L4: structured perturbation climb on L^R_d (R110 wiring), IDEAL model (R104 definition), own simulator
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
typedef __int128 VT; static VT bv(int m){ VT b=((VT)1)<<br[m]; return bp[m]? -b : b; }
static int run(int *Tout){ int s[MAXN], ns[MAXN]; VT v[MAXN]; memcpy(s,st,sizeof(int)*N); memset(F,0,sizeof F); memset(MV,0,sizeof MV);
  int T=0; int oprev[MAXN]; int have=0;
  for(;T<5000;){ for(int i=0;i<N;i++){int x=ord_[i]; int m=2*x+s[x]; v[x]=bv(m)+(xt[m]>=0? v[xt[m]]:0);}
    int av[MAXN]; int any=0; for(int x=0;x<N;x++){ int m=2*x+1-s[x]; VT ov=bv(m)+(xt[m]>=0? v[xt[m]]:0); av[x]= ov>v[x]; any|=av[x]; }
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
    memcpy(s,ns,sizeof(int)*N); T++; }
  *Tout=T; return T; }
static int LV=-1, SCT=0, SCH=0;
static long score(int *T){ run(T); if(SCT) return *T;
  if(getenv("ANYRUN")){ long best=-1000000; for(int a=1;a<d;a++){ int h=0; while(a+h<d && F[a+h]==2*F[a+h-1]+2 && F[a+h]>0) h++; long sc=3000L*h + 4L*F[a+h-1>=0?a+h-1:0]; if(a+h<d){int def=2*F[a+h-1]+2-F[a+h]; sc -= 100L*(def<0?-def:def);} if(sc>best)best=sc; } return best; }
  if(SCH){ long sc=0; for(int l=1;l<=SCH;l++){ int def=2*F[l-1]+2-F[l]; sc += def==0? 3000 : -200*(def<0?-def:def); } return sc + 16L*F[SCH] + (*T<15?*T:15); } if(LV>=0) return (long)F[LV]*256 + (*T<255?*T:255); return *T; }
static void rd(const char*fn){ FILE*f=fopen(fn,"r"); char w[64]; while(fscanf(f,"%63s",w)==1){ int n=0;
    if(!strcmp(w,"d")){ if(fscanf(f,"%d",&d)!=1) exit(1); N=2*d; continue; }
    int *a = !strcmp(w,"xt")?xt: !strcmp(w,"br")?br: !strcmp(w,"bp")?bp: !strcmp(w,"gate")?gate: !strcmp(w,"start")?st:NULL; if(!a) continue;
    n = !strcmp(w,"start")? N : 2*N; for(int i=0;i<n;i++) if(fscanf(f,"%d",&a[i])!=1) exit(1); } fclose(f); }
static void wr(const char*fn, long sc, int T){ FILE*f=fopen(fn,"w"); fprintf(f,"d %d\nxt",d); for(int i=0;i<2*N;i++)fprintf(f," %d",xt[i]);
  fprintf(f,"\nbr"); for(int i=0;i<2*N;i++)fprintf(f," %d",br[i]); fprintf(f,"\nbp"); for(int i=0;i<2*N;i++)fprintf(f," %d",bp[i]);
  fprintf(f,"\ngate"); for(int i=0;i<2*N;i++)fprintf(f," %d",gate[i]); fprintf(f,"\nstart"); for(int i=0;i<N;i++)fprintf(f," %d",st[i]);
  fprintf(f,"\n# score %ld T %d F",sc,T); for(int l=0;l<d;l++)fprintf(f," %d",F[l]); fprintf(f," moves"); for(int x=0;x<N;x++)fprintf(f," %d",MV[x]); fprintf(f,"\n"); fclose(f); }
int main(int argc,char**argv){ rd(argv[1]); rs+=atol(argv[2])*7919; long iters=atol(argv[3]);
  if(getenv("LV")) LV=atoi(getenv("LV")); if(getenv("SCORE")&&!strcmp(getenv("SCORE"),"T")) SCT=1; if(getenv("CHAIN")) SCH=atoi(getenv("CHAIN"));
  int nomut[MAXN]={0};
  if(getenv("FIX")){ char*p=strdup(getenv("FIX")); for(char*t=strtok(p,",");t;t=strtok(NULL,",")) fixo[atoi(t)]=1; }
  if(getenv("NOMUT")){ char*p=strdup(getenv("NOMUT")); for(char*t=strtok(p,",");t;t=strtok(NULL,",")) {int x=atoi(t); nomut[x]=1; fixo[2*x]=fixo[2*x+1]=1;} }
  double temp=getenv("ANNEAL")?atof(getenv("ANNEAL")):0; const char*out=getenv("OUT")?getenv("OUT"):"/dev/null";
  if(!acyclic()){ fprintf(stderr,"input cyclic\n"); return 1; }
  int T; long cur=score(&T), best=cur; wr(out,best,T); printf("start score %ld T %d F(LV) %d\n",cur,T,LV>=0?F[LV]:-1); fflush(stdout);
  int sxt[MAXN*2],sbr[MAXN*2],sbp[MAXN*2],sg[MAXN*2],sst[MAXN];
  for(long it=0;it<iters;it++){ memcpy(sxt,xt,sizeof xt);memcpy(sbr,br,sizeof br);memcpy(sbp,bp,sizeof bp);memcpy(sg,gate,sizeof gate);memcpy(sst,st,sizeof st);
    int nm=1+rnd()%3; for(int q=0;q<nm;q++){ int r=rnd()%6; int m=rnd()%(2*N);
      if(r==0||r==5){ if(fixo[m]) continue; int y=(int)(rnd()%(N+1))-1; if(y==m/2) y=-1; xt[m]=y; }
      else if(r==1){ int m2=rnd()%(2*N); int t=br[m];br[m]=br[m2];br[m2]=t; }
      else if(r==2){ bp[m]^=1; }
      else if(r==3){ int x=m/2,l=x/2,k=m%2; if(l==0){ int m2=rnd()%4; int t=gate[m];gate[m]=gate[m2];gate[m2]=t; if(m>=4){} } else { int a=4*l+k, b=4*l+2+k; int t=gate[a];gate[a]=gate[b];gate[b]=t; } }
      else { st[rnd()%N]^=1; } }
    /* level-0 gate swaps must stay within level 0: m<4 guaranteed only if x<2; enforce */
    if(!acyclic()){ memcpy(xt,sxt,sizeof xt);memcpy(br,sbr,sizeof br);memcpy(bp,sbp,sizeof bp);memcpy(gate,sg,sizeof gate);memcpy(st,sst,sizeof st); acyclic(); continue; }
    long sc=score(&T); double tt=temp*(1.0-(double)it/iters);
    if(sc>=cur || (tt>0 && (rnd()%1000000)/1e6 < exp((double)(sc-cur)/(tt*(LV>=0?256:((SCH||getenv("ANYRUN"))?200:1)))))){ cur=sc; if(sc>best){ best=sc; wr(out,best,T); printf("it %ld score %ld T %d F",it,sc,T); for(int l=0;l<d;l++)printf(" %d",F[l]); printf("\n"); fflush(stdout);} }
    else { memcpy(xt,sxt,sizeof xt);memcpy(br,sbr,sizeof br);memcpy(bp,sbp,sizeof bp);memcpy(gate,sg,sizeof gate);memcpy(st,sst,sizeof st); acyclic(); } }
  return 0; }
