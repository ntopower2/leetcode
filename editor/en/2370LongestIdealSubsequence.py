class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        LETTERS = "abcdefghijklmnopqrstuvwxyz"
        LETTER_SIZE = len(LETTERS)
        ltrOpts = [[0] * 2 * k] * LETTER_SIZE
        for i in range(LETTER_SIZE):
            tmp = []
            for j in range(LETTER_SIZE):
                if abs(j - i) <= k:
                    tmp.append(j)
            ltrOpts[i] = tmp

        n = len(s)
        longestUntil = [1] * n
        lastPos = [-1] * LETTER_SIZE

        def findBestForPosition(i: int) -> int:
            possibleLetterIndexes = ltrOpts[i]
            # m = 0
            # for j in possibleLetterIndexes:
            #     if lastPos[j]:
            #         m = max(m, longestUntil[lastPos[j]])
            tmp = [
                longestUntil[lastPos[j]]
                for j in possibleLetterIndexes
                if -1 < lastPos[j] < i
            ]

            return max(tmp) + 1 if tmp else 1

        for i in range(0, n):
            lastPos[LETTERS.index(s[i])] = i
            longestUntil[i] = findBestForPosition(i)
        return max(longestUntil)


print(Solution().longestIdealString("acfgbd", 2))
