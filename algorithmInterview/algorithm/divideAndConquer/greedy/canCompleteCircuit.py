# https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def traverse(gas, cost, idx):
            remain = 0
            for g, c in zip(gas[idx:], cost[idx:]):
                remain += g - c
                if remain < 0: 
                    return False
            for g, c in zip(gas[:idx], cost[:idx]):
                remain += g - c
                if remain < 0:
                    return False
            return True
        for i in range(len(gas)):
            if traverse(gas, cost, i):
                return i
        return -1