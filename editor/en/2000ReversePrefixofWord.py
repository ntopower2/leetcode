class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        i = word.index(ch)
        return word[i::-1] + word[i + 1 :]

    def reversePrefix2(self, word: str, ch: str) -> str:
        lst = list(word)
        for r, c in enumerate(word):
            if c == ch:
                l = 0
                while r > l:
                    lst[r], lst[l] = lst[l], lst[r]
                    l += 1
                    r -= 1
                return "".join(lst)

        return word


import random, string


def randomword(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


s = randomword(250)
for _ in range(100000):
    Solution().reversePrefix2(s, s[78])
