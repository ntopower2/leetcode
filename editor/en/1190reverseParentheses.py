class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = ""
        found = []
        jumps = [None for _ in s]
        for i, c in enumerate(s):
            if c == "(":
                found.append(i)
            elif c == ")":
                j = found.pop()
                jumps[j] = i
                jumps[i] = j

        i, d = 0, 1
        while i < len(s):
            if s[i] in "()":
                d *= -1
                i = jumps[i]
            else:
                res += s[i]
            i += d
        return res


assert Solution().reverseParentheses("(ed(et(oc))el)") == "leetcode"
