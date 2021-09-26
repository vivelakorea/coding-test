#include <iostream>
#include <vector>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    int i, j, N, tmp, max = 0;
    vector<int> counts(10001, 0);
    cin >> N;
    for (i = 0; i < N; i++) {
        cin >> tmp;
        counts[tmp]++;
        if (max < tmp) max = tmp;
    }
    for (i = 1; i <= max; i++) {
        for (j = 0; j < counts[i]; j++) {
            cout << i << '\n';
        }
    }
}