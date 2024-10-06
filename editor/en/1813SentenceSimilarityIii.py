#
# @lc app=leetcode id=1813 lang=python3
#
# [1813] Sentence Similarity III
#


# @lc code=start
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1, words2 = sentence1.split(), sentence2.split()
        n1, n2 = len(words1), len(words2)

        if n1 < n2:
            words1, words2 = words2, words1
            n1, n2 = n2, n1

        start, end = 0, len(words2)
        while start < n2 and words1[start] == words2[start]:
            start += 1

        while end < n2 and words1[n1 - 1 - end] == words2[n2 - 1 - end]:
            end += 1

        return start + end >= n2


# @lc code=end

assert (
    Solution().areSentencesSimilar(sentence1="Eating right now", sentence2="Eating")
    == True
)
