# coding test

1 problem / day

## folders

```
.
└── algorithmInterview
    ├── algorithm
    │   ├── binarySearch
    │   ├── bitManipulation
    │   ├── divideAndConquer
    │   │   ├── dynamic
    │   │   └── greedy
    │   ├── slidingWindow
    │   └── sort
    └── dataStructure
        ├── linearDataStructure
        │   ├── array
        │   ├── deqeueAndPriorityQueue
        │   ├── hash
        │   ├── linkedList
        │   └── stackAndQueue
        ├── nonLinearDataStructure
        │   ├── heap
        │   ├── shortestPath
        │   ├── tree
        │   └── trie
        └── string
```

## 오답

- algroithmInterview/dataStructure/string/longestPalindrome.py

- algroithmInterview/dataStructure/nonLinearDataStructure/tree/maxDepth.py (root가 None인 경우 오류 날 수 있었음)

- algorithmInterview/dataStructure/linearDataStructure/array/trap.py

- algorithmInterview/dataStructure/linearDataStructure/linkedList/mergeTwoLists.py (재귀 풀이)

- algorithmInterview/dataStructure/linearDataStructure/stackAndQueue/removeDuplicateLetters.py (https://www.youtube.com/watch?v=nsnpeb_0Hfw)

- algorithmInterview/algorithm/sort/insertionSortList.py (간소화, 최적화)

## tip

- 문자열을 i 이상 j 미만으로 슬라이싱 한 후 반대로 뒤집기:

  s[i:j][::-1]
