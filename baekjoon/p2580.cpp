#include <iostream>
#include <vector>
#include <string>
using namespace std;
int fillin[81];
vector < vector<int> > emptySpaces;
int row[10][10], column[10][10], bigSquare[10][10];

bool dfs(int fillinIdx) {
    // // print
    // cout << fillinIdx << '\n';
    // for (auto &e: fillin) {
    //     cout << e << ' ';
    // }
    // cout << '\n';
    if (fillinIdx == emptySpaces.size()) return true;
    int r = emptySpaces[fillinIdx][0], c = emptySpaces[fillinIdx][1], b = emptySpaces[fillinIdx][2];
    bool isFillable = false;
    // 가능한 수 찾기
    for (int i = 1; i < 10; i++) {
        if (row[r][i] && column[c][i] && bigSquare[b][i]) {
            isFillable = true;
            // fillin의 fillinIdx 자리에 숫자 넣고 row, column, bigSquare 업데이트
            fillin[fillinIdx] = i;
            row[r][i] = 0;
            column[c][i] = 0;
            bigSquare[b][i] = 0;
            // go deeper
            if(!dfs(fillinIdx + 1)) {
                isFillable = false;
                row[r][i] = 1;
                column[c][i] = 1;
                bigSquare[b][i] = 1;
            }
        }
    }
    return isFillable;
}

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
    int tmp, emptyCnt = 0;
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
        int idx = 0;
        for (int i = 0; i < a.size(); i++) {
            if (a[i] == ' ') {
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

    // 표시
    fillin[emptySpaces.size()] = -1;

    // 백트래킹
    dfs(0);

    
    // 출력
    int emptySpaceIdx = 0;
    for (int i = 1; i < 10; i++) {
        for (int j = 1; j < 10; j++) {
            if (totalSquare[i][j]) cout << totalSquare[i][j] << ' ';
            else cout << fillin[emptySpaceIdx++] << ' ';
        }
        cout << '\n';
    }
}