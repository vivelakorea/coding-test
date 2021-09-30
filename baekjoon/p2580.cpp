#include <iostream>
#include <vector>
#include <string>
using namespace std;

// void dfs(int idx, int emptySpaces[]) {

// }
int bigSquareIdx(int i, int j) {
    if (1 <= i && i < 4) {
        if (1 <= j && j < 4) {
            return 1;
        } else if (4 <= j && j < 7) {
            return 2;
        } else {
            return 3;
        }
    } else if (4 <= i && i < 7) {
        if (1 <= j && j < 4) {
            return 4;
        } else if (4 <= j && j < 7) {
            return 5;
        } else {
            return 6;
        }
    } else {
        if (1 <= j && j < 4) {
            return 7;
        } else if (4 <= j && j < 7) {
            return 8;
        } else {
            return 9;
        }
    }
}

int main() {
    int tmp, row[10][10], column[10][10], bigSquare[10][10], emptyCnt = 0;
    vector < vector<int> > emptySpaces;
    // ex) row[3][4] == 1: 3번째 줄은 4가 남아있음
    //     column[4][9] == 0: 4번째 열은 9가 이미 쓰였음
    //     bigSquare[3][1] == 1: 3번째 큰 정사각형은 1이 남아있음
    for (int i = 1; i < 10; i++) {
        for (int j = 1; j < 10; j++) {
            row[i][j] = 1;
            column[i][j] = 1;
            bigSquare[i][j] = 1;
        }
    }

    // 입력
    int totalSquare[10][10];

    for (int j = 1; j < 10; j++) {
        string a;
        vector<int> v;
        getline(cin, a);
        // cout << a << '\n';
        int idx = 0;
        for (int i = 0; i < a.size(); i++) {
            if (a[i] == ' ') {
                // cout << stoi(a.substr(idx, i - idx)) << ' ';
                v.push_back(stoi(a.substr(idx, i - idx)));
                idx = i + 1;
            }
        }
        v.push_back(stoi(a.substr(idx)));
        for (int i = 1; i < 10; i++) {
            totalSquare[j][i] = v[i - 1];
        }
    }

    for (int i = 1; i < 10; i++) {
        for (int j = 1; j < 10; j++) {
            tmp = totalSquare[i][j];
            if (tmp != 0) {
                row[i][tmp] = 0;
                column[j][tmp] = 0;
                bigSquare[bigSquareIdx(i, j)][tmp] = 0;
            } else {
                emptyCnt++;
                emptySpaces.push_back(vector({i, j, bigSquareIdx(i, j)}));
            }
        }
    }

    // 백트래킹
    
}