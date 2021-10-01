#include <iostream>
#include <string>
#include <vector>
using namespace std;
int N, S[20][20], minimum = 100 * 20 * 20;

void dfs(vector<int> start) {
    // cout << "start ";
    // for (int i = 0; i < (int)start.size(); i++) {
    //     cout << start[i] << ' ';
    // }
    // cout << '\n';
    if ((int)start.size() < N / 2 && ((int)start.size() != 0 && start.back() == N - 1)) return;

    if ((int)start.size() == N / 2) {
        int startScore = 0, linkScore = 0;
        for (int i = 0; i < N / 2; i++) {
            for (int j = 0; j < N / 2; j++) {
                if (j == i) continue;
                // cout << "add " << i << ' ' << j << '\n';
                startScore += S[start[i]][start[j]];
            }
        }
        vector<int> link;
        int idx = 0;
        for (int i = 0; i < N; i++) {
            if (idx == N || start[idx] == i) idx++;
            else link.push_back(i);
        }
        // cout << "link ";
        // for (int i = 0; i < (int)link.size(); i++) {
        //     cout << link[i] << ' ';
        // }
        // cout << '\n';
        for (int i = 0; i < N / 2; i++) {
            for (int j = 0; j < N / 2; j++) {
                if (j == i) continue;
                linkScore += S[link[i]][link[j]];
            }
        }
        if (startScore > linkScore) {
            minimum = min(minimum, startScore - linkScore);
        } else {
            minimum = min(minimum, - startScore + linkScore);            
        }
        // cout << "startScore ";
        // cout << startScore << ' ';
        // cout << "linkScore ";
        // cout << linkScore << '\n';
        return;
    }


    int idx;
    if ((int)start.size() == 0) idx = 0;
    else idx = start.back() + 1;

    for (int i = idx; i < N; i++) {
        start.push_back(i);
        dfs(start);
        start.pop_back();
    }
}

int main() {
    // 입력
    scanf("%d\n", &N);
    for (int i = 0; i < N; i++) {
        string a;
        getline(cin, a);
        int idx = 0;
        vector<int> v;
        for(int j = 0; j < (int)a.size(); j++) {
            if (a[j] == ' ') {
                v.push_back(stoi(a.substr(idx, j - idx)));
                idx = j + 1;
            }
        }
        v.push_back(stoi(a.substr(idx)));
        for (int j = 0; j < N; j++) {
            S[i][j] = v[j];
        }
    }
    vector<int> start;
    dfs(start);

    cout << minimum << '\n';
}