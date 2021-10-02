//      0
//      _
//   5/   \1
//   4\   /2
//      -
//      3
//
// 0 1 0 1 0 1 // 1
// 1 1 0 1 1 0 // 2 // 5
// 0 2 0 1 1 1 // 3 // 0
// 2 0 2 1 1 1 // 4 // 1
// 2 2 0 3 1 1 // 5 // 2
// 2 2 3 0 4 1 // 6 // 3
// 2 2 3 4 0 5 // 7 // 4
// 7 2 3 4 5 0 // 8 // 5
// 0 9 3 4 5 7 // 9 // 0
// 9 0 12 4 5 7 // 10 // 1
// 9 12 0 16 5 7 // 11 // 2
// 9 12 16 0 21 7 // 12 // 3
// . . . . . . // N // (N + 3) % 6
#include <iostream>
// #include <unordered_map>
// #include <vector>
// #include <functional>
using namespace std;
// unordered_map<int, vector<long long> > cache;
int main() {
    // int N, T;
    // cache[1] = vector({(long long)0,(long long)1,(long long)0,(long long)1,(long long)0,(long long)1});
    // cin >> T;
    // for (int i = 0; i < T; i++) {
    //     cin >> N;
    //     if (N == 1) {
    //         cout << 1 << '\n';
    //         continue;
    //     }
    //     for (int j = 2; j <= N; j++) {
    //         if (!cache.count(j)) {
    //             int idx = (j + 3) % 6;
    //             cache[j] = vector({(long long)0,(long long)0,(long long)0,(long long)0,(long long)0,(long long)0});

    //             cache[j][(idx + 0) % 6] = 0;
    //             cache[j][(idx + 1) % 6] = cache[j-1][(idx + 1) % 6] + cache[j-1][idx];
    //             cache[j][(idx + 2) % 6] = cache[j-1][(idx + 2) % 6];
    //             cache[j][(idx + 3) % 6] = cache[j-1][(idx + 3) % 6];
    //             cache[j][(idx + 4) % 6] = cache[j-1][(idx + 4) % 6];
    //             cache[j][(idx + 5) % 6] = cache[j-1][(idx + 5) % 6] + cache[j-1][idx];
    //             // print
    //             // for (int k = 1; k <= j; k++) {
    //             //     for (int l = 0; l < 6; l++) {
    //             //         cout << cache[k][l] << ' ';
    //             //     }
    //             //     cout << '\n';
    //             // }
    //             // cout << '\n';
    //         }
    //     }

    //     int maximum = 0;
    //     for (int j = 0; j < 6; j++) {
    //         // print
    //         // cout << cache[N][j] << ' ';
    //         if (cache[N-1][j] > maximum) maximum = cache[N-1][j];
    //     }
    //     // print
    //     // cout << '\n';
    //     cout << maximum << '\n';
    // }
    int T, N;
    unsigned long long P[101] {0,1,1,1,};
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N;
        if (N <= 3) {
            cout << P[N] << '\n';
            continue;
        }
        for (int j = 4; j <= N; j++) {
            P[j] = P[j-2] + P[j-3];
        }
        cout << P[N] << '\n';
    }

}