/* L-LOWER 6 (BOX L6): gad2 = gad.c plus edits of existing options (env EDIT = comma list of OLD option indices m = 2x + k; each
   may get a new target (any old mover, Z, W, X), a new rank tier, a new parity), a gate order for level J (g6), and P = 0 = no inserted
   level. Score = 1000 min(caps, GUARD) + 2 good + max(0, F(J) - FB) (+ 10^5 at F(J) = FT); env FT (default 2^(J+2) - 2), FB (default 222).
   With P = J the inserted level sits directly below pair J: pass J + 1 (pair J renumbered) and FT = 254 for the old level 6.
   GADGET search. Base genome B (text). Insert ONE new level at position P (old levels P..d-1 shift up by one;
   movers >= 2P get +2), holding two new movers Z = 2P, W = 2P+1. Gadget parameters: for each of the 4 new options a Xi-target
   (from a candidate list, in OLD numbering, or Z/W, or X), a rank TIER (a real number among the old ranks: new rank sits just above
   old rank floor(tier)), a parity; start bits of Z, W; a gate order (g(0), g(1) of the new level); and up to NW re-points of existing
   options (from a candidate option list) to Z or W. Score = 1000 * min(caps,GUARD) + good J-windows (exactly two pair-J moves)
   + 100000 if F(J) = 2^(J+2)-2. Simulated annealing over gadget parameters. Simulator = l5/fev.c rules (__int128; d <= 31).
   Usage: gad BASE P J GUARD NW STEPS SEED [ANNEAL]  -> best score lines; best genome written to gad_best_<SEED>.txt */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 70
typedef __int128 VT;
int d0,N0; int xt0[MAXN*2],br0[MAXN*2],bp0[MAXN*2],gate0[MAXN*2],st0[MAXN];
int d,N; int xt[MAXN*2],br[MAXN*2],bp[MAXN*2],gate[MAXN*2],st[MAXN];
static unsigned long long rs=88172645463325252ULL; static unsigned long long rnd(){rs^=rs<<13;rs^=rs>>7;rs^=rs<<17;return rs;}
static double urand(){return (rnd()>>11)*(1.0/9007199254740992.0);}
static int ord_[MAXN], vis[MAXN], no;
static int dfs(int x){ if(vis[x]==2) return 1; if(vis[x]==1) return 0; vis[x]=1; for(int k=0;k<2;k++){int y=xt[2*x+k]; if(y>=0 && !dfs(y)) return 0;} vis[x]=2; ord_[no++]=x; return 1; }
static int acyclic(){ memset(vis,0,sizeof vis); no=0; for(int x=0;x<N;x++) if(!dfs(x)) return 0; return 1; }
static int F[MAXN]; int J=6;
static VT bv(int m){ VT b=((VT)1)<<br[m]; return bp[m]? -b : b; }
static int good;
static int run(void){ int s[MAXN], ns[MAXN]; VT v[MAXN]; memcpy(s,st,sizeof(int)*N); memset(F,0,sizeof F);
  int T=0; int oprev[MAXN]; int have=0; int wmv=0; good=0; int started=0;
  for(;T<6000;){ for(int i=0;i<N;i++){int x=ord_[i]; int m=2*x+s[x]; v[x]=bv(m)+(xt[m]>=0? v[xt[m]]:0);}
    int av[MAXN]; int any=0; for(int x=0;x<N;x++){ int m=2*x+1-s[x]; VT ov=bv(m)+(xt[m]>=0? v[xt[m]]:0); av[x]= ov>v[x]; any|=av[x]; }
    if(!any) break;
    int c=0, o[MAXN];
    for(int l=0;l<d;l++){ for(int q=0;q<2;q++){ int x=2*l+q; ns[x]=s[x];
        if(l==0){ if(av[x] && gate[2*x+1-s[x]] < gate[2*x+s[x]]) ns[x]=1-s[x]; }
        else if(av[x] && s[x]!=c) ns[x]=c; }
      if(l==0) o[0] = gate[0+ns[0]] > gate[2+ns[1]];
      else { int a=ns[2*l], b=ns[2*l+1]; o[l] = (a!=b)? (a!=c) : (gate[2*(2*l)+a] > gate[2*(2*l+1)+a]); }
      c=o[l]; }
    int ch=0; for(int x=0;x<N;x++) if(ns[x]!=s[x]) ch=1; if(!ch) break;
    if(!have){ int c0=0, o0[MAXN]; for(int l=0;l<d;l++){ if(l==0) o0[0]=gate[0+s[0]]>gate[2+s[1]]; else {int a=s[2*l],b=s[2*l+1]; o0[l]=(a!=b)?(a!=c0):(gate[4*l+a]>gate[4*l+2+a]);} c0=o0[l]; } memcpy(oprev,o0,sizeof(int)*d); have=1; }
    if(o[J-1]!=oprev[J-1]){ if(started && wmv==2) good++; started=1; wmv=0; }
    wmv += (ns[2*J]!=s[2*J]) + (ns[2*J+1]!=s[2*J+1]);
    for(int l=0;l<d;l++){ if(o[l]!=oprev[l]) F[l]++; oprev[l]=o[l]; }
    memcpy(s,ns,sizeof(int)*N); T++; }
  if(started && wmv==2) good++;
  return T; }
static void rd(const char*fn){ FILE*f=fopen(fn,"r"); if(!f){perror(fn);exit(1);} char w[64]; while(fscanf(f,"%63s",w)==1){ int n=0;
    if(!strcmp(w,"d")){ if(fscanf(f,"%d",&d0)!=1) exit(1); N0=2*d0; continue; }
    int *a = !strcmp(w,"xt")?xt0: !strcmp(w,"br")?br0: !strcmp(w,"bp")?bp0: !strcmp(w,"gate")?gate0: !strcmp(w,"start")?st0:NULL; if(!a) continue;
    n = !strcmp(w,"start")? N0 : 2*N0; for(int i=0;i<n;i++) if(fscanf(f,"%d",&a[i])!=1) exit(1); } fclose(f); }
/* gadget */
int P, NW; int ncand; int cand[64]; int nopt; int optc[64];
typedef struct { int tgt[4]; double tier[4]; int par[4]; int stz[2]; int gord; int wopt[4], wto[4]; int eT[16]; double eR[16]; int eP[16]; int g6; } Gad;
int NE; int eopt[16];
static int newidx(int x){ return (x<0||P<=0)? x : (x>=2*P? x+2 : x); }
static void build(const Gad*g){ d=d0+(P>0); N=2*d; int Z=2*P;
  for(int x=0;x<N0;x++){ int y=newidx(x); for(int k=0;k<2;k++){ xt[2*y+k]=newidx(xt0[2*x+k]); bp[2*y+k]=bp0[2*x+k]; gate[2*y+k]=gate0[2*x+k]; } st[y]=st0[x]; }
  if(P>0) for(int i=0;i<4;i++){ int t=g->tgt[i]; xt[2*Z+i]= t==-1? -1 : t==-2? Z : t==-3? Z+1 : newidx(t); bp[2*Z+i]=g->par[i]; }
  if(P>0){ st[Z]=g->stz[0]; st[Z+1]=g->stz[1]; }
  if(P>0){ int gg[4][4]={{0,2,1,3},{2,0,3,1},{0,3,1,2},{3,0,2,1}}; /* gate[4P+a] vs gate[4P+2+a]: g(a) = gate[4P+a] > gate[4P+2+a] */
    for(int i=0;i<4;i++) gate[4*P+i]=5000+gg[g->gord][i]; }
  /* ranks: sort keys */
  double key[MAXN*2]; int M=2*N;
  for(int x=0;x<N0;x++){ int y=newidx(x); for(int k=0;k<2;k++) key[2*y+k]=br0[2*x+k]; }
  if(P>0) for(int i=0;i<4;i++) key[2*Z+i]=g->tier[i]+0.001*(i+1);
  for(int e=0;e<NE;e++) if(g->eR[e]>-5){ int m=eopt[e]; key[2*newidx(m/2)+m%2]=g->eR[e]+0.0001*(e+1); }
  for(int m=0;m<M;m++){ int r=0; for(int m2=0;m2<M;m2++) if(key[m2]<key[m]) r++; br[m]=r; }
  for(int e=0;e<NE;e++){ int m=eopt[e]; int y=2*newidx(m/2)+m%2; if(g->eT[e]>-5) xt[y]= g->eT[e]==-1? -1 : g->eT[e]==-2? Z : g->eT[e]==-3? Z+1 : newidx(g->eT[e]); if(g->eP[e]>=0) bp[y]=g->eP[e]; }
  { int gg[4][4]={{0,2,1,3},{2,0,3,1},{0,3,1,2},{3,0,2,1}}; if(g->g6>=0) for(int i=0;i<4;i++) gate[4*J+i]=3000+gg[g->g6][i]; }
  for(int i=0;i<NW;i++) if(P>0 && g->wopt[i]>=0){ int m=g->wopt[i]; int x=m/2,k=m%2; xt[2*newidx(x)+k]= Z + g->wto[i]; }
}
static double tiers[]={-0.5,10.5,25.5,26.5,40.5,45.5,68.5,70.5,71.5,78.5,79.5,80.5,81.5,86.5,87.5,88.5,89.5,90.5,91.5,94.5,95.5,99.5,100.5,101.5,104.5,105.5,106.5,107.5,108.5,109.5,110.5,111.5};
#define NT (int)(sizeof tiers/sizeof tiers[0])
static void randgad(Gad*g){ for(int i=0;i<4;i++){ int r=rnd()%(ncand+3); g->tgt[i]= r<ncand? cand[r] : -(r-ncand+1); g->tier[i]=tiers[rnd()%NT]; g->par[i]=rnd()&1; }
  g->stz[0]=rnd()&1; g->stz[1]=rnd()&1; g->gord=rnd()%4; for(int i=0;i<4;i++){ g->wopt[i]= i<NW? optc[rnd()%nopt] : -1; g->wto[i]=rnd()&1; }
  for(int e=0;e<NE;e++){ g->eT[e]=-9; g->eR[e]=-9; g->eP[e]=-1; } g->g6=-1; }
static int anytgt(void){ int r=rnd()%(N0+3); return r<N0? r : -(r-N0+1); }
static void mutate(Gad*g){ int f=rnd()%(P>0?12:4); if(P<=0) f+=8; int i=rnd()%4;
  if(f>=8){ int e=rnd()%NE; int h=rnd()%5; if(h==0) g->eT[e]= (rnd()%3==0)? -9 : anytgt(); else if(h==1) g->eR[e]= (rnd()%3==0)? -9 : tiers[rnd()%NT]; else if(h==2) g->eP[e]= (int)(rnd()%3)-1; else if(h==3) g->g6=(int)(rnd()%5)-1; else { g->eT[e]=-9; g->eR[e]=-9; g->eP[e]=-1; } if(P>0 && g->eT[e]==-2 && 0) ; return; }
  if(f==0){ int r=rnd()%(ncand+3); g->tgt[i]= r<ncand? cand[r] : -(r-ncand+1);} else if(f==1||f==2) g->tier[i]=tiers[rnd()%NT]; else if(f==3) g->par[i]^=1;
  else if(f==4) g->stz[rnd()&1]^=1; else if(f==5) g->gord=rnd()%4; else if(f==6 && NW>0){ int j=rnd()%NW; g->wopt[j]=optc[rnd()%nopt]; } else if(NW>0){ g->wto[rnd()%NW]^=1; } }
int GUARD; int FT, FB;
static long score(const Gad*g){ build(g); if(!acyclic()) return -1; run(); int h=0; for(int l=0;l<d;l++){ if(F[l]==(1<<(l+2))-2) h++; else break; }
  long sc = 1000L*(h<GUARD?h:GUARD) + (h>=GUARD? 2*good + (F[J]>FB? F[J]-FB:0) :0); if(F[J]==FT && h>=GUARD) sc+=100000; return sc; }
static void wr(const char*fn){ FILE*f=fopen(fn,"w"); fprintf(f,"d %d\nxt",d); for(int i=0;i<2*N;i++) fprintf(f," %d",xt[i]); fprintf(f,"\nbr"); for(int i=0;i<2*N;i++) fprintf(f," %d",br[i]);
  fprintf(f,"\nbp"); for(int i=0;i<2*N;i++) fprintf(f," %d",bp[i]); fprintf(f,"\ngate"); for(int i=0;i<2*N;i++) fprintf(f," %d",gate[i]); fprintf(f,"\nstart"); for(int i=0;i<N;i++) fprintf(f," %d",st[i]); fprintf(f,"\n"); fclose(f); }
int main(int argc,char**argv){ if(argc<8){fprintf(stderr,"usage\n");return 1;} rd(argv[1]); P=atoi(argv[2]); J=atoi(argv[3]); GUARD=atoi(argv[4]); NW=atoi(argv[5]);
  long STEPS=atol(argv[6]); FT= getenv("FT")? atoi(getenv("FT")) : (1<<(J+2))-2; FB= getenv("FB")? atoi(getenv("FB")) : 222; rs^=(unsigned long long)atol(argv[7])*0x9E3779B97F4A7C15ULL; double AN= argc>8? atof(argv[8]) : 30;
  /* candidates: movers on pair J's chains at the failing windows and pair J-1, J-2 members, plus pair 7..9 members (old numbering) */
  int cl[]={8,9,10,11,14,15,16,17,18,19,20,22,50,52,54,7,34,35,45}; ncand=sizeof cl/sizeof cl[0]; memcpy(cand,cl,sizeof cl);
  int ol[]={24,25,26,27,22,23,18,19,108,109,44,45}; nopt=sizeof ol/sizeof ol[0]; memcpy(optc,ol,sizeof ol);
  { const char*E=getenv("EDIT"); NE=0; if(E){ char buf[256]; strncpy(buf,E,255); buf[255]=0; for(char*t=strtok(buf,",");t&&NE<16;t=strtok(NULL,",")) eopt[NE++]=atoi(t); } if(NE==0){ int dfl[]={24,25,26,27}; NE=4; memcpy(eopt,dfl,sizeof dfl);} }
  Gad cur,best; randgad(&cur); long cs=score(&cur), bs=cs; best=cur; double temp=AN;
  for(long it=0;it<STEPS;it++){ Gad nx=cur; int nm=1+rnd()%3; for(int k=0;k<nm;k++) mutate(&nx); long s=score(&nx);
    if(s>=cs || (s>=0 && urand()<__builtin_exp((s-cs)/temp))){ cur=nx; cs=s; if(s>bs){ bs=s; best=nx; build(&best); acyclic(); run();
        printf("it %ld best %ld F",it,bs); for(int l=0;l<9;l++) printf(" %d",F[l]); printf(" good %d\n",good); fflush(stdout);
        char fn[64]; sprintf(fn,"gad2_best_%s.txt",argv[7]); wr(fn); } }
    temp = AN*(1.0-(double)it/STEPS)+0.5;
    if(it%200000==0 && it){ cur=best; cs=bs; } }
  printf("END best %ld\n",bs); return 0; }
