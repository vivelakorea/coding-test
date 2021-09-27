#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(int &a, int &b) {
    return a > b;
}
int main() {
    int num;
    vector<int> nums;
    cin >> num;
    // cout << num << '\n';
    while (num) {
        nums.push_back(num % 10);
        num /= 10;
        // cout << num << '\n';
    }
    // for (auto &element : nums) {
    //     cout << element << '\n';
    // }
    sort(nums.begin(), nums.end(), cmp);
    for (auto &element : nums) {
        cout << element;
    }
    cout << '\n';
}