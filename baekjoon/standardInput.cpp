#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main() {
    // // 입력값의 길이를 알고있을때, 숫자들이 일렬로 들어올 때
    // // ex)
    // // 1234567

    // int a[7];
    // for (int i = 0; i < 7; i++) {
    //     scanf("%1d", &a[i]);
    // }
    // // 그대로 출력해서 확인
    // for (int i = 0; i < 7; i++) {
    //     cout << a[i] << '\n';
    // }
    
    ////////////////////////////////////////////////////////////////////////////////////////////////////

    // // 입력값의 길이를 모르고 있을 때, 숫자들이 일렬로 들어올 때
    // // ex)
    // // 12345678912345678

    // vector<int> nums;
    // string a;
    // cin >> a;
    // for (int i = 0; i < a.size(); i++) {
    //     nums.push_back(a[i] - '0');
    // }
    // for (int i = 0; i < nums.size(); i++) {
    //     cout << nums[i] << '\n';
    // }
    
    ////////////////////////////////////////////////////////////////////////////////////////////////////

    // // 공백을 포함해서 받는 방법
    // // ex)
    // // abc de fg
    // // 를 하나의 string으로 받기

    // string name;
    // // cin >> name; -> abc만 받음
    // getline(cin, name);
    // cout << name << '\n';

    ////////////////////////////////////////////////////////////////////////////////////////////////////

    // // 길이를 알 때, 띄어쓴 입력을 분류해서 얻는 방법
    // // ex)
    // // 1234 323 44 252 21221

    // vector<int> nums;
    // int tmp1, tmp2, tmp3, tmp4, tmp5;
    // scanf("%d %d %d %d %d", &tmp1, &tmp2, &tmp3, &tmp4, &tmp5);
    // nums.push_back(tmp1);
    // nums.push_back(tmp2);
    // nums.push_back(tmp3);
    // nums.push_back(tmp4);
    // nums.push_back(tmp5);

    // for (int i = 0; i < nums.size(); i++) {
    //     cout << nums[i] << '\n';
    // }

    ////////////////////////////////////////////////////////////////////////////////////////////////////

    // // 길이를 모를 때, 띄어쓴 단어들을 구분해서 읽는 방법
    // // ex)
    // // sdd fdsf gdsg sdf asg gasdg asdg sdfd saf wqeqw jgd sdfg fdsf
    
    // string str_arr[100];
    // int str_cnt = 0;

    // string a;
    // getline(cin, a);

    // char* str_buffer = new char[1000];
    // strcpy(str_buffer, a.c_str());

    // char* tok = strtok(str_buffer, " ");
    // while (tok != nullptr) {
    //     str_arr[str_cnt++] = string(tok);
    //     tok = strtok(nullptr, " ");
    // }
    // for (int i = 0; i < str_cnt; i++) {
    //     cout << str_arr[i] << '\n';
    // }

    ////////////////////////////////////////////////////////////////////////////////////////////////////

    // // 길이를 모를 때, 띄어쓴 수들을 구분해서 읽는 방법
    // // ex)
    // // 123 123 323 324 141 5242 64645 132323
    // string a;
    // vector<int> v;
    // getline(cin, a);
    // int idx = 0;
    // for (int i = 0; i < a.size(); i++) {
    //     if (a[i] == ' ') {
    //         v.push_back(stoi(a.substr(idx, i - idx)));
    //         idx = i + 1;
    //     }
    // }
    // v.push_back(stoi(a.substr(idx)));

    // for (int i = 0; i < v.size(); i++) {
    //     cout << v[i] << '\n';
    // }
}