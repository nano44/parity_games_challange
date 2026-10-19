// Box 8, (P_strict) probe. One-player SINK parity games on a DAG: vertices 1..n, sink 0 (self-loop, least relevant),
// every edge goes from v to some w < v, every vertex belongs to the improver (+). Under VJ00 Ω the cycle node of every
// vertex is the sink, every path vertex is more relevant than it, and two different paths from v have different vertex
// sets, so Ω(v) is the path set compared by its most relevant differing vertex; encoded exactly as
// val(v) = sum over path vertices w of sgn(w) * 2^rank(w) (rank distinct, sgn = +1 for even priority). No flat steps exist.
// Computes the LONGEST chain of single improving switches over all starts (a lower bound on the any-subset longest chain),
// and anneals the game to maximise it. Usage: dagchain n deg iters seed [dump]
#include <bits/stdc++.h>
using namespace std; typedef long long ll;
int n, D; vector<vector<int>> succ; vector<int> rk, sg;
vector<int> radix; ll nstates; vector<int> memo;
ll wt(int v){ return v==0?0:(ll)sg[v]*(1LL<<rk[v]); }
void decode(ll s, vector<int>& c){ for(int v=1;v<=n;v++){ c[v]=s%succ[v].size(); s/=succ[v].size(); } }
ll encode(const vector<int>& c){ ll s=0; for(int v=n;v>=1;v--) s=s*succ[v].size()+c[v]; return s; }
void vals(const vector<int>& c, vector<ll>& val){ val[0]=0; for(int v=1;v<=n;v++) val[v]=wt(v)+val[succ[v][c[v]]]; }
int longest(ll s){
  if(memo[s]>=0) return memo[s];
  vector<int> c(n+1); decode(s,c); vector<ll> val(n+1); vals(c,val); int best=0;
  for(int v=1;v<=n;v++) for(int k=0;k<(int)succ[v].size();k++) if(k!=c[v] && val[succ[v][k]]>val[succ[v][c[v]]]){
    int old=c[v]; c[v]=k; int L=1+longest(encode(c)); c[v]=old; best=max(best,L); }
  return memo[s]=best;
}
int score(){ nstates=1; for(int v=1;v<=n;v++) nstates*=succ[v].size(); memo.assign(nstates,-1); int b=0;
  for(ll s=0;s<nstates;s++) b=max(b,longest(s)); return b; }
int main(int argc,char**argv){
  n=atoi(argv[1]); D=atoi(argv[2]); long iters=atol(argv[3]); mt19937 rng(atoi(argv[4])); bool dump=argc>5;
  succ.assign(n+1,{}); rk.assign(n+1,0); sg.assign(n+1,1);
  vector<int> perm(n); iota(perm.begin(),perm.end(),0); shuffle(perm.begin(),perm.end(),rng);
  for(int v=1;v<=n;v++){ rk[v]=perm[v-1]; sg[v]=(rng()%2)?1:-1; set<int> s; int d=1+rng()%min(D,v); while((int)s.size()<d) s.insert(rng()%v); succ[v]=vector<int>(s.begin(),s.end()); }
  int cur=score(), best=cur; auto bs=succ; auto br=rk; auto bg=sg; double T=2.0;
  for(long it=0;it<iters;it++){
    auto os=succ; auto orr=rk; auto og=sg; int m=rng()%3; int v=1+rng()%n;
    if(m==0){ set<int> s; int d=1+rng()%min(D,v); while((int)s.size()<d) s.insert(rng()%v); succ[v]=vector<int>(s.begin(),s.end()); }
    else if(m==1){ int u=1+rng()%n; swap(rk[u],rk[v]); } else sg[v]=-sg[v];
    int sc=score();
    if(sc>=cur || exp((sc-cur)/T) > (rng()%100000)/100000.0){ cur=sc; if(sc>best){best=sc;bs=succ;br=rk;bg=sg;} }
    else { succ=os; rk=orr; sg=og; }
    T=max(0.05,T*0.9995);
  }
  printf("n=%d D=%d best=%d\n",n,D,best);
  if(dump){ for(int v=1;v<=n;v++){ printf("%d rank=%d sgn=%+d ->",v,br[v],bg[v]); for(int w:bs[v]) printf(" %d",w); printf("\n"); } }
}
