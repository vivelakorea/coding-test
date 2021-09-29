#include <iostream>
#include <vector>
using namespace std;

int N, res = 0;

void dfs(int N, int row, int eachRowPosition[]) {
    if (row == N) {
        res++;
        return;
    }
    for (int i = 0; i < N; i++) {
        // i : 현재 row에서 둘 position
        // 이전 row들의 position 중에 하나라도 걸리면 넘어가고 다 안걸리면 재귀적 호출
        bool canPlace = true;
        for (int j = 0; j < row; j++) {
            // j : 이전 줄들 중 j번째 줄
            int obstacle = eachRowPosition[j];
            if (obstacle == i || (obstacle - i) == (row - j) || (i - obstacle) == (row - j)) {
                canPlace = false;
                break;
            }
        }
        if (canPlace) {
            eachRowPosition[row] = i;
            dfs(N, row + 1, eachRowPosition);
        }
    }
}

int main() {
    cin >> N;
    int eachRowPosition[N];
    dfs(N, 0, eachRowPosition);
    cout << res << '\n';
}