#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int tmp, N;
    vector<int> nums;
    
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> tmp;
        nums.push_back(tmp);
    }
    sort(nums.begin(), nums.end());
    for (int i = 0; i < N; i++) {
        cout << nums[i] << '\n';
    }
}