#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <unordered_map>
#include <cmath>
using namespace std;
bool sortByFirstDescAndSecondAsc(const pair<int, int> &a, const pair<int, int> &b){
    if (a.first == b.first) return a.second < b.second;
    return a.first > b.first;
}

int main() {
    int N, first, tmp, sum, average, median, mode, range;
    bool allSame = true;
    vector<int> nums;
    vector< pair<int, int> > countArr;
    unordered_map<int, int> counter;
    cin >> N;
    cin >> first;
    nums.push_back(first);
    for (int i = 1; i < N; i++) {
        cin >> tmp;
        if (tmp != first) allSame = false;
        nums.push_back(tmp);
    }

    // all numbers are same
    if (allSame) {
        cout << first << '\n' 
        << first << '\n'
        << first << '\n'
        << 0 << '\n';
        return 0;
    }


    // average
    sort(nums.begin(), nums.end());
    sum = accumulate(nums.begin(), nums.end(), 0);
    average = round((float)sum / N);
    
    // median
    median = nums[N / 2];

    // mode
    for (int i = 0; i < N; i++) {
        if (!counter.count(nums[i])) counter.insert(make_pair(nums[i], 0));
        counter[nums[i]]++;
    }
    for (auto &element : counter) {
        countArr.push_back(make_pair(element.second, element.first));
    }

    sort(countArr.begin(), countArr.end(), sortByFirstDescAndSecondAsc);
    
    if (countArr[0].first == countArr[1].first) { // no same number -> len(countArr) >= 2
        mode = countArr[1].second;
    } else {
        mode = countArr[0].second;
    }

    // range
    range = nums[N-1] - nums[0];



    cout << average << '\n'
    << median << '\n'
    << mode << '\n'
    << range << '\n';

    return 0;
}