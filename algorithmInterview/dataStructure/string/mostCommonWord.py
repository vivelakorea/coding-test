from collections import Counter 
class Solution:
    def mostCommonWord(self, paragraph, banned):
        words = Counter()
        word = ""
        for c in paragraph:
            if c.isalpha():
                word += c.lower()
            elif word:
                if word not in banned:
                    words[word] += 1
                word = ""
        words[word] += 1
        return words.most_common()[0][0]

s = Solution()
s.mostCommonWord("bob a .. bab.  bab  bab, bab ba, asf", ['bob'])