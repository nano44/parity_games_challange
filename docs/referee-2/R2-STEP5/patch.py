import sys,re
p=sys.argv[1]; s=open(p).read()
def rep(old,new,cnt=1):
    global s
    assert s.count(old)==cnt,(old,s.count(old)); s=s.replace(old,new)
# globals
rep('namespace pg {\n','''namespace pg {
// R2 probe counters (instrumentation only)
static long r2_acc=0; static int r2_mode=0; // 1=region loop, 2=Dom
static long c_m1=0,c_ntf_viol=0,c_fm_viol=0,c_P=0,c_P0=0,c_yz_viol=0,c_dom_acc=0,c_dom_nonstr=0,c_dom_str=0,c_acyc_viol=0,c_tang=0,c_tpr_bad=0,c_notop=0,c_r1fail=0;
static std::vector<int> r2_lastacc; // tangle ids accepted
''')
# record acceptance in attractTangle
rep('''    return true;
}

/**
 * Attract vertices that are in tangles.''','''    r2_acc++; r2_lastacc.push_back(t);
    return true;
}

/**
 * Attract vertices that are in tangles.''')
# tangle creation check
rep('''        // and set p to pr
        tpr.push_back(pr);''','''        // and set p to pr
        { c_tang++; int mx=-1; bool hastop=false; for (int v: tangle){ if (priority(v)>mx) mx=priority(v); if (v==startvertex) hastop=true;} if (mx!=pr) c_tpr_bad++; if(!hastop) c_notop++; }
        tpr.push_back(pr);''')
# best_vertices: record per-round Z
rep('''    while (true) {
        curdist++;
        prevV = V;
''','''    std::vector<bitset> r2Z; std::vector<long> r2A;
    while (true) {
        curdist++;
        prevV = V;
''')
rep('''        CurR = R;
        for (int top=nodecount()-1; top>=0; top--) {''','''        CurR = R; long acc0=r2_acc;
        for (int top=nodecount()-1; top>=0; top--) {''')
rep('''        /**
         * Now find all Candidates: v \\in V that do not yet have a good path to Z
         */
''','''        r2Z.push_back(Z); r2A.push_back(r2_acc-acc0);
        /**
         * Now find all Candidates: v \\in V that do not yet have a good path to Z
         */
''')
rep('''            V.swap(prevV);
            return -1;''','''            V.swap(prevV);
            c_m1++; size_t f=r2Z.size()-1; if (r2A[f]!=0) c_ntf_viol++;
            for (size_t r=0;r<f;r++){ bitset d=r2Z[f]; d-=r2Z[r]; if (d.any()) { c_fm_viol++; break; } }
            r2_Zf = r2Z[f];
            return -1;''')
# Dom instrumentation
rep('''            // Add Dom(V,R) to X
            for (int top=nodecount()-1; top>=0; top--) {
                if (V[top] and !X[top]) {
                    X[top] = true; // add to <X>
                    str[top] = -1;
                    Q.push(top);
                    while (Q.nonempty()) {
                        const int v = Q.pop();
                        R[v] = false;
#ifndef NDEBUG''','''            // Add Dom(V,R) to X
            bitset r2R0(R); bitset r2X0(X); bitset r2cur(nodecount()); c_P++; if (depth==0) c_P0++;
            for (int top=nodecount()-1; top>=0; top--) {
                if (V[top] and !X[top]) {
                    X[top] = true; // add to <X>
                    str[top] = -1;
                    Q.push(top);
                    r2cur.reset(); r2cur[top]=true;
                    while (Q.nonempty()) {
                        const int v = Q.pop();
                        R[v] = false;
                        bitset r2Xb(X); r2_lastacc.clear();
                        attractVertices(player, v, R, X, R, priority(top));
                        bitset r2Xm(X);
                        attractTangles(player, v, R, X, R, priority(top));
                        // new from vertex rules
                        { bitset nv(r2Xm); nv-=r2Xb; r2cur|=nv; }
                        for (int tt : r2_lastacc) {
                            c_dom_acc++;
                            bool straddle=false; std::vector<int> nw; bitset nb(nodecount());
                            int *ptr=tv[tt]; for(;;){int u=*ptr++; if(u==-1)break; ptr++; if (r2Xm[u] && !r2cur[u]) straddle=true; if(!r2Xm[u]){nw.push_back(u); nb[u]=true;} }
                            if (straddle) c_dom_str++; else c_dom_nonstr++;
                            // ACYC check on new part: H_t restricted to nb
                            std::map<int,int> st; ptr=tv[tt]; for(;;){int u=*ptr++; if(u==-1)break; st[u]=*ptr++;}
                            // Kahn: remove vertices with no succ in nb
                            bitset rem(nb); bool changed=true;
                            while(changed){changed=false; for(int u: nw){ if(!rem[u]) continue; bool hs=false;
                                if (owner(u)==player){ int s2=st[u]; if (s2>=0 && rem[s2]) hs=true; }
                                else { for (auto ce=outs(u); *ce!=-1; ce++) if (rem[*ce]) { hs=true; break; } }
                                if(!hs){rem[u]=false; changed=true;} } }
                            if (rem.any()) c_acyc_viol++;
                            r2cur|=nb;
                        }
                        r2_lastacc.clear();
                        continue;
#ifndef NDEBUG''')
rep('''                    }
#ifndef NDEBUG
                    if (trace >= 2) {
                        // report region
                        logger << "\\033[1;33mregion\\033[m ";''','''                    }
#ifndef NDEBUG
                    if (trace >= 2) {
                        // report region
                        logger << "\\033[1;33mregion\\033[m ";''')
# after Dom loop: YZ check. find end of Dom for-loop: the closing of else branch
rep('''                        Zvec.clear();
                    }
#endif
                }
            }
        }
    }
}''','''                        Zvec.clear();
                    }
#endif
                }
            }
            { bitset Y0(r2R0); Y0-=R; if (Y0 != r2_Zf) c_yz_viol++; }
        }
    }
}''')
# print at end of run
rep('''    logger << "found " << dominions''','''    fprintf(stderr,"R2PROBE m1=%ld ntf_viol=%ld fm_viol=%ld P=%ld P0=%ld yz_viol=%ld dom_acc=%ld dom_nonstr=%ld dom_str=%ld acyc_viol=%ld tangles=%ld tpr_bad=%ld notop=%ld\\n",c_m1,c_ntf_viol,c_fm_viol,c_P,c_P0,c_yz_viol,c_dom_acc,c_dom_nonstr,c_dom_str,c_acyc_viol,c_tang,c_tpr_bad,c_notop);
    logger << "found " << dominions''')
rep('#include "dtl.hpp"\n','#include "dtl.hpp"\n#include <map>\n#include <vector>\n#include <cstdio>\nstatic pg::bitset r2_Zf;\n')
open(p,'w').write(s)
