class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = j = 1
        sSkips = tSkips = 0
        hasChange = True
        while hasChange:
            # for each of the strings we either consume literal or #
            sInRange = i <= len(s)
            tInRange = j <= len(t)
            hasChange = False
            if sInRange:
                if s[-i] == "#":
                    sSkips += 1
                    i += 1
                    hasChange = True
                elif sSkips:
                    sSkips -= 1
                    i += 1
                    hasChange = True
            if tInRange:
                if t[-j] == "#":
                    tSkips += 1
                    j += 1
                    hasChange = True
                elif tSkips:
                    tSkips -= 1
                    j += 1
                    hasChange = True
            sInRange = i <= len(s)
            tInRange = j <= len(t)
            if not sSkips + tSkips and sInRange and tInRange:
                if s[-i] == t[-j] and not s[-i] == "#":
                    i += 1
                    j += 1
                    hasChange = True
                elif t[-j] != "#" and s[-i] != "#":
                    return False

        sInRange = i <= len(s)
        tInRange = j <= len(t)
        if not sInRange and not tInRange:
            return True
        elif sInRange or tInRange:
            return False


assert (
    Solution().backspaceCompare(
        "x#end##outp###twoyc#nj###h#ozx##qy#m##cwjdrmn##wtje###v#r##nhew#k#xh#wsjc##",
        "j#x#g#end##outp#o###twoyc#l#l#nj###p#h#oa#zx##qyz##m##cwjdci##rmn##wtje###v#rq###nhew#kw##xh#wsjc##",
    )
    == True
)
