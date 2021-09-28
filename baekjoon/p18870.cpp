#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <vector>
using namespace std;
int main() {
    int N, tmp, idx = 0;
    string s;
    vector<int> nums;
    unordered_map<int, int> orders;

    scanf("%d\n", &N);
    getline(cin, s);
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == ' ') {
            nums.push_back(stoi(s.substr(idx, i - idx)));
            idx = i + 1;
        }
    }
    nums.push_back(stoi(s.substr(idx)));

    vector<int> nums_tmp(nums);

    sort(nums.begin(), nums.end());
    tmp = nums[0];
    idx = 0;
    orders.insert(make_pair(tmp, idx++));
    for (int i = 1; i < N; i++) {
        // cout << "i : " << i << ' ' << "tmp : " << tmp << " nums[i] : " << nums[i] << '\n';
        if (tmp != nums[i]) {
            tmp = nums[i];
            orders.insert(make_pair(tmp, idx++));
        }
    }
    for (int i = 0; i < N; i++) {
        cout << orders[nums_tmp[i]] << ' ';
    }
    cout << '\n';
}