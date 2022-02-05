# coding test

## folders

```
.
├── algorithmInterview
│   ├── algorithm
│   │   ├── binarySearch
│   │   ├── bitManipulation
│   │   ├── divideAndConquer
│   │   ├── dynamic
│   │   ├── greedy
│   │   ├── slidingWindow
│   │   └── sort
│   └── dataStructure
│       ├── linearDataStructure
│       │   ├── array
│       │   ├── deqeueAndPriorityQueue
│       │   ├── hash
│       │   ├── linkedList
│       │   └── stackAndQueue
│       ├── nonLinearDataStructure
│       │   ├── heap
│       │   ├── shortestPath
│       │   ├── tree
│       │   └── trie
│       └── string
├── baekjoon
└── dataScienceIntro
```

## 오답

- algroithmInterview/dataStructure/string/longestPalindrome.py

- algroithmInterview/dataStructure/nonLinearDataStructure/tree/maxDepth.py (root가 None인 경우 오류 날 수 있었음)

- algorithmInterview/dataStructure/linearDataStructure/array/trap.py

- algorithmInterview/dataStructure/linearDataStructure/linkedList/mergeTwoLists.py (재귀 풀이)

- algorithmInterview/dataStructure/linearDataStructure/stackAndQueue/removeDuplicateLetters.py (https://www.youtube.com/watch?v=nsnpeb_0Hfw)

- algorithmInterview/algorithm/sort/insertionSortList.py (간소화, 최적화)

- algorithmInterview/algorithm/slidingWindow/maxSlidingWindow.py (time limit exceeded)

- algorithmInterview/algorithm/slidingWindow/minWindow.py (스파게티코드)

- p9461 왠지는 모르겠는데 vector<long long> 했을때 범위 안넘어가는데도 오버플로우됨

## tip

- 문자열을 i 이상 j 미만으로 슬라이싱 한 후 반대로 뒤집기:

  s[i:j][::-1]

- 분할정복할때 반으로 쪼개는거면 merge(conquer)할때 O(N)만 해도 이득임 (O(N^2) -> O(NlogN)일때)
