import re
from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        parsedExpression = re.compile("\d{10}[MFO](\d{2})\d{2}")
        res = 0
        for detail in details:
            num = int(parsedExpression.match(detail).group(1))
            if num > 60:
                res += 1
        return res


assert (
    Solution().countSeniors(
        ["5612624052M0130", "5378802576M6424", "5447619845F0171", "2941701174O9078"]
    )
    == 2
)
