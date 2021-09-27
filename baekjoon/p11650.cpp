#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
bool sortBy(pair<int, int> &a, pair<int, int> &b) {
    if (a.first == b.first) return a.second < b.second;
    return a.first < b.first;
}

int main() {
    int N, tmp1, tmp2;
    vector< pair<int,int> > nums;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> tmp1 >> tmp2;
        nums.push_back(make_pair(tmp1, tmp2));
    }
    sort(nums.begin(), nums.end(), sortBy);
    for (auto &element : nums) {
        cout << element.first << ' ' << element.second << '\n';
    }
}