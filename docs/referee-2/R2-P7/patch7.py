import sys
p = sys.argv[1]; s = open(p).read()
def rep(old, new, cnt=1):
    global s
    assert s.count(old) == cnt, (old, s.count(old)); s = s.replace(old, new)
rep('#include "dtl.hpp"\n', '#include "dtl.hpp"\n#include <cstdio>\n#include <cstdlib>\nstatic FILE* r7f = nullptr;\n'
    '#define R7BS(b) do { if (r7f) { for (auto _v=(b).find_first(); _v!=pg::bitset::npos; _v=(b).find_next(_v)) fprintf(r7f," %d",(int)_v); } } while(0)\n')
rep('    G = disabled;\n    G.flip();\n',
    '    G = disabled;\n    G.flip();\n    if (getenv("R2P7_LOG")) { r7f = fopen(getenv("R2P7_LOG"), "w");\n'
    '      for (int v=0; v<nodecount(); v++) { fprintf(r7f, "N %d %d %d :", v, priority(v), owner(v)); for (auto e=outs(v); *e!=-1; e++) fprintf(r7f," %d",*e); fprintf(r7f,"\\n"); } }\n')
rep('    bitset CurG(G);\n', '    bitset CurG(G);\n    if (r7f) { fprintf(r7f, "S %d :", player); R7BS(G); fprintf(r7f, "\\n"); }\n')
rep('        tpr.push_back(pr);\n',
    '        tpr.push_back(pr);\n        if (r7f) { fprintf(r7f, "T %d %d :", (int)tpr.size()-1, pr); for (int*q=tv.back(); *q!=-1; q+=2) fprintf(r7f," %d",*q); fprintf(r7f," :"); for (int*q=tout.back(); *q!=-1; q++) fprintf(r7f," %d",*q); fprintf(r7f,"\\n"); }\n')
rep('    int curdist = 0;\n', '    int curdist = 0;\n    if (r7f) { fprintf(r7f, "B %d :", player); R7BS(R); fprintf(r7f, "\\n"); }\n')
rep('    if (!hasV) return 0;\n', '    if (!hasV) { if (r7f) fprintf(r7f,"E 0\\n"); return 0; }\n')
rep('        curdist++;\n        prevV = V;\n', '        curdist++;\n        prevV = V;\n        if (r7f) { fprintf(r7f, "V :"); R7BS(V); fprintf(r7f, "\\n"); }\n')
rep('                Z |= CurZ;\n                CurZ.reset();\n', '                if (r7f) { fprintf(r7f, "P %d :", top); R7BS(CurZ); fprintf(r7f, "\\n"); }\n                Z |= CurZ;\n                CurZ.reset();\n')
rep('        if (n_candidates == 0) return 1; // no more vertices are removed\n', '        if (n_candidates == 0) { if (r7f) fprintf(r7f,"E 1\\n"); return 1; } // no more vertices are removed\n')
rep('''            // run tangle attractor to Z with the given threshold
            while (Q.nonempty()) {
                const int u = Q.pop();
                attractVertices(player, u, R, Z, R, t);
                attractTangles(player, u, R, Z, R, t);
            }
''', '''            // run tangle attractor to Z with the given threshold
            while (Q.nonempty()) {
                const int u = Q.pop();
                attractVertices(player, u, R, Z, R, t);
                attractTangles(player, u, R, Z, R, t);
            }
            if (r7f) { fprintf(r7f, "W %d :", t); R7BS(Z); fprintf(r7f, "\\n"); }
''')
rep('''            // No vertices were removed from V
            return 1;''', '''            // No vertices were removed from V
            if (r7f) fprintf(r7f,"E 1\\n");
            return 1;''')
rep('''            V.swap(prevV);
            return -1;''', '''            V.swap(prevV);
            if (r7f) fprintf(r7f,"E -1\\n");
            return -1;''')
open(p, 'w').write(s)
