from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        records = []
        for op in operations:
            if op == "C":
                res -= records.pop()
            elif op == "D":
                num = records[-1] + records[-1]
                res += num
                records.append(num)
            elif op == "+":
                num = records[-1] + records[-2]
                res += num
                records.append(num)
            else:
                num = int(op)
                res += num
                records.append(num)
        return res


assert Solution().calPoints(["5", "2", "C", "D", "+"]) == 30
