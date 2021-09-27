#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
bool sortBy(string &a, string &b) {
    if (a.length() == b.length()) return a.compare(b) < 0;
    return a.length() < b.length();
}

int main() {
    int N;
    string tmp;
    vector< string > words;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> tmp;
        words.push_back(tmp);
    }
    sort(words.begin(), words.end(), sortBy);
    tmp = words[0];
    cout << words[0] << '\n';
    for (int i = 0; i < N; i++) {
        if (tmp.compare(words[i])) {
            cout << words[i] << '\n';
        }
        tmp = words[i];
    }
}