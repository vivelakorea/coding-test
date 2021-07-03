from typing import List

class Solution:
    def josephus(self, N: int, K: int) -> List[int]:
        tmp_stack, main_stack = [], list(range(N,0,-1))
        res = []
        while main_stack or tmp_stack:
            for i in range(K - 1):
                tmp_stack.append(main_stack.pop())
                if not main_stack:
                    main_stack = list(reversed(tmp_stack))
                    tmp_stack = []
            res.append(main_stack.pop())
            if not main_stack:
                    main_stack = list(reversed(tmp_stack))
                    tmp_stack = []
        return res

s = Solution()
N, K = map(int, input().split())
answer = s.josephus(N, K)
print('<' + str(answer)[1:-1] + '>')
