import collections

class Solution:
    def card2(self, n):
        cards = collections.deque(range(1, n + 1))
        while len(cards) > 1:
            cards.popleft()
            cards.append(cards.popleft())
        return cards[0]


s = Solution()
print(s.card2(int(input())))