/*
 * Copyright 2017-2018 Tom van Dijk, Johannes Kepler University Linz
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <iostream>
#include <random>

using namespace std;

// L-COMP battery: the ONLY change against Oink's rngame.cpp (commit 8fbf0a7) is the seed. Oink's rngame seeds its
// mt19937 from std::random_device, so its games cannot be reproduced; here the seed is the LAST command-line argument
// and the bounded draw is written out (rejection sampling on mt19937's 32-bit output), because
// std::uniform_int_distribution is implementation-defined and would tie the corpus to one libstdc++ version.
static unsigned long SEED = 0;

int
rng(int low, int high)
{
    static mt19937 generator(SEED);
    unsigned long range = (unsigned long)(high - low) + 1UL;      // 1 .. 2^31
    unsigned long limit = (4294967296UL / range) * range;         // largest multiple of range below 2^32
    unsigned long x;
    do { x = generator(); } while (x >= limit);                   // mt19937 yields 32-bit values (fixed by the C++ standard)
    return low + (int)(x % range);
}

int
main(int argc, char** argv)
{
    if (argc != 6 && argc != 7) {
        cout << "Syntax: " << argv[0] << " nNodes maxPrio minDeg maxDeg [noSelfLoops] seed" << endl;
        cout.flush();
        return -1;
    }

    // parse arguments
    int n = stoi(argv[1]);
    int maxP = stoi(argv[2]);
    int minD = stoi(argv[3]);
    int maxD = stoi(argv[4]);
    int SL = argc == 6 ? 1 : 0;
    SEED = stoul(argv[argc-1]);

    // check bad arguments
    if (maxD > n) {
        cout << "max degree >= num nodes?!" << endl;
        cout.flush();
        return -1;
    }
    if (minD > maxD) {
        cout << "min degree >= max degree?!" << endl;
        cout.flush();
        return -1;
    }
    if (maxD == n && SL == 0) {
        maxD--; // just fix the number
    }

    // allocate edge target array
    int *tgt = new int[n];

    // generate game
    cout << "parity " << n << ";" << endl;
    for (int i=0; i<n; i++) {
        // generate priority and owner
        cout << i << " " << rng(0, maxP) << " " << rng(0, 1) << " ";
        // determine number of edges
        int e_count = rng(minD, maxD);
        // initialize edge target array
        for (int j=0; j<n; j++) tgt[j] = j;
        // initialize size of array
        int m = n;
        // maybe remove the self-loop
        if (SL == 0) {
            tgt[i] = n-1;
            m--;
        }
        // generate random edges
        for (int j=0; j<e_count; j++) {
            int x = rng(0, m-1);
            if (j != 0) cout << ",";
            cout << tgt[x];
            tgt[x] = tgt[m-1];
            m--;
        }
        // generate no label
        cout << ";" << endl;
    }

    // free edge target array
    delete[] tgt;

    return 0;
}
