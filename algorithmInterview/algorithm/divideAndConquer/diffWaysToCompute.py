# https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operators = collections.Counter(list(expression[1::2]))
        nums = list(map(int,list(expression[::2])))
        def diffWaysToCompute__helper(node):
            # node: [(2, {}), (3, {}), (4, {}), (5, {})]
            #         made      made     made     made
            
            # merge: [(2, {})], [(3, {})]
            # can use: {'-': 2, '*': 1}
            # merged: [(2-3, {'-': 1}), (3-2, {'-': 1}), (2*3, {'*': 1})]
            
            # merge: [(2-3, {'-': 1}), (3-2, {'-': 1}), (2*3, {'*': 1})], [(4-5, {'-': 1}), (5-4, {'-': 1}), (4*5, {'*': 1})]
            # can use: in for
            # ...
            n = len(node)
            if n == 1:
                return node # [(2, {})]
            leftNode = diffWaysToCompute__helper(node[:n//2])
            rightNode = diffWaysToCompute__helper(node[n//2:])
            print(leftNode, rightNode)
            merged = []
            for i_made in leftNode:
                for j_made in rightNode:
                    used = i_made[1] + j_made[1]
                    canUse = operators - used
                    print(canUse)
                    for operator in canUse:
                        if operator == '-':
                            if i_made[0] == j_made[0]:
                                merged.append((0, used + collections.Counter(['-'])))
                            else:
                                merged.append((i_made[0] - j_made[0], used + collections.Counter(['-'])))
                                merged.append((j_made[0] - i_made[0], used + collections.Counter(['-'])))
                        elif operator == '+':
                            merged.append((i_made[0] + j_made[0], used + collections.Counter(['+'])))
                        else: # *
                            merged.append((i_made[0] * j_made[0], used + collections.Counter(['*'])))
            print(merged)
            print('-----------')
            return merged
        firstNode = list(map(lambda x: (x, collections.Counter()), nums))
        final = diffWaysToCompute__helper(firstNode)
        return list(map(lambda x: x[0], final))
