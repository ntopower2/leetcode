from collections import defaultdict
import re


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        res = ""

        nextNums = re.compile("(\d*)")
        stack = [defaultdict(int)]
        i = 0

        while i < len(formula):
            c = formula[i]

            if c == "(":
                stack.append(defaultdict(int))
                i += 1
            elif c == ")":
                m = nextNums.match(formula, i + 1).group()
                val = 1 if m == "" else int(m)
                tmp = stack.pop()
                for key in tmp:
                    stack[-1][key] += tmp[key] * val

                i += len(m) + 1
            else:
                formulaParts = re.compile("([A-Z]{1}[a-z]*)(\d*)")
                part = formulaParts.match(formula[i:])
                theValue = int(part.group(2)) if part.group(2) != "" else 1
                stack[-1][part.group(1)] += 1 * theValue
                i += part.end() - part.start()

        res = "".join(
            sorted(
                [key + (str(val) if val != 1 else "") for key, val in stack[-1].items()]
            )
        )
        return res


assert Solution().countOfAtoms("Mg(H2O)N") == "H2MgNO"
assert Solution().countOfAtoms("H50") == "H50"
assert Solution().countOfAtoms("K4(ON(SO3)2)2") == "K4N2O14S4"
