class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def convertIntoNumeric(version):
            if version is None or version == "":
                return [0]
            return [int(val) for val in version.split(".")]

        lst1 = convertIntoNumeric(version1)
        lst2 = convertIntoNumeric(version2)
        for v1, v2 in zip(lst1, lst2):
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        n, m = len(lst1), len(lst2)
        if n > m:
            return 1 if any([v > 0 for v in lst1[m:]]) else 0
        elif n < m:
            return -1 if any([v > 0 for v in lst2[n:]]) else 0
        return 0


assert Solution().compareVersion("1.0.1", "1") == 1
assert Solution().compareVersion("1.01", "1.001") == 0
assert Solution().compareVersion("1.0.0", "1.0") == 0
assert Solution().compareVersion("1.0.1", "1.0") == 1
assert Solution().compareVersion("0.1", "1.0") == -1
assert Solution().compareVersion("0.1", "1.1") == -1
