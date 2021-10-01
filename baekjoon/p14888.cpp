#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
int N, operatorNums[4], maximum = -(int)pow(10, 9), minimum = (int)pow(10, 9);
vector<int> nums;

void dfs(int n, int tmp) { // 2번째 숫자: n = 1 ~~ N번째 숫자: n = N-1
    if (n == N) {
        if (tmp > maximum) maximum = tmp;
        if (tmp < minimum) minimum = tmp;
        return;
    }
    if (operatorNums[0]) { // +
        tmp += nums[n];
        operatorNums[0]--;
        dfs(n + 1, tmp);
        tmp -= nums[n];
        operatorNums[0]++;
    }
    if (operatorNums[1]) { // -
        tmp -= nums[n];
        operatorNums[1]--;
        dfs(n + 1, tmp);
        tmp += nums[n];
        operatorNums[1]++;
    }
    if (operatorNums[2]) { // *
        tmp *= nums[n];
        operatorNums[2]--;
        dfs(n + 1, tmp);
        tmp /= nums[n];
        operatorNums[2]++;
    }
    if (operatorNums[3]) { // /
        tmp /= nums[n];
        int remain = tmp % nums[n];
        operatorNums[3]--;
        dfs(n + 1, tmp);
        tmp *= nums[n];
        tmp += remain;
        operatorNums[3]++;
    }
}

int main() {
    string a;
    scanf("%d\n", &N);
    getline(cin, a);
    int idx = 0;
    for (int i = 0; i < (int)a.size(); i++) {
        if (a[i] == ' ') {
            nums.push_back(stoi(a.substr(idx, i - idx)));
            idx = i + 1;
        }
    }
    nums.push_back(stoi(a.substr(idx)));
    cin >> operatorNums[0] >> operatorNums[1] >> operatorNums[2] >> operatorNums[3];
    
    dfs(1, nums[0]);

    cout << maximum << '\n' << minimum << '\n';
}