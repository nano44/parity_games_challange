// Reproduces Oink game.cpp:492-495 (Game::sort mapping): prints "oink_id file_id" for a PGSolver file (ids 0..n-1).
#include <algorithm>
#include <cstdio>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
int main(int argc, char** argv) {
    std::ifstream in(argv[1]); std::string line; std::vector<int> pr;
    while (std::getline(in, line)) {
        if (line.rfind("parity", 0) == 0 || line.empty()) continue;
        std::istringstream ss(line); int id, p; ss >> id >> p; if ((int)pr.size() <= id) pr.resize(id + 1); pr[id] = p;
    }
    int n = pr.size(); std::vector<int> mapping(n);
    for (int i = 0; i < n; i++) mapping[i] = i;
    std::sort(mapping.data(), mapping.data() + n, [&](const int &a, const int &b) { return (unsigned int)pr[a] < (unsigned int)pr[b]; });
    for (int i = 0; i < n; i++) printf("%d %d\n", i, mapping[i]);
}
