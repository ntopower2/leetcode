from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return list(words[0])

        wordMin = min(words, key=lambda x: len(x))

        res = Counter(wordMin)

        for word in words:
            tmp = Counter(word)
            for key in res:
                res[key] = min(res[key], tmp[key])

        return list(res.elements())


assert Solution().commonChars(["bella", "label", "roller"]) == ["e", "l", "l"]
