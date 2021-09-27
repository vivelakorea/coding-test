#include <iostream>
#include <string>
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;
bool sortBy(tuple<int, string, int> &a, tuple<int, string, int> &b) {
    if (get<0>(a) == get<0>(b)) return get<2>(a) < get<2>(b);
    return get<0>(a) < get<0>(b);
}

int main() {
    int N, tmp1;
    string tmp2;
    vector< tuple<int, string, int> > nums;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> tmp1 >> tmp2;
        nums.push_back(make_tuple(tmp1, tmp2, i));
    }
    sort(nums.begin(), nums.end(), sortBy);
    for (auto &element : nums) {
        cout << get<0>(element) << ' ' << get<1>(element) << '\n';
    }
}