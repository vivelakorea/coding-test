import collections
class Solution:
    def groupAnagrams(self, strs):
        hashmap = collections.defaultdict(list)
        for word in strs:
            hash_sum = 0
            for c in word:
                hash_sum += hash(c)
            hashmap[hash_sum].append(word)
        return [words for words in hashmap.values()]

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))