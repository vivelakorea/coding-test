from typing import List

class Solution:
    def josephus(self, N: int, K: int) -> List[int]:
        tmp_stack, main_stack = [], list(range(N,0,-1))
        res = []
        while main_stack or tmp_stack:
            for i in range(K - 1):
                # print(str(i + 1) + 'th move')
                # print('tmp_stack', tmp_stack, 'main_stack', list(reversed(main_stack)))
                tmp_stack.append(main_stack.pop())
                # print('moved!')
                # print('tmp_stack', tmp_stack, 'main_stack', list(reversed(main_stack)))
                if not main_stack:
                    main_stack = list(reversed(tmp_stack))
                    tmp_stack = []
                    # print('refreshed!')
                    # print('tmp_stack', tmp_stack, 'main_stack', list(reversed(main_stack)))
            res.append(main_stack.pop())
            if not main_stack:
                    main_stack = list(reversed(tmp_stack))
                    tmp_stack = []
                    # # print('refreshed!')
                    # print('tmp_stack', tmp_stack, 'main_stack', list(reversed(main_stack)))
            # print('popped!')
            # print('tmp_stack', tmp_stack, 'main_stack', list(reversed(main_stack)))
            # print('res', res)
        return res

s = Solution()
# answer = s.josephus(7, 3)
# print('<' + str(answer)[1:-1] + '>')

N, K = map(int, input().split())
answer = s.josephus(N, K)
print('<' + str(answer)[1:-1] + '>')
