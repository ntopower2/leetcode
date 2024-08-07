class Solution:
    def numberToWords(self, num: int) -> str:
        numNames = [
            "Zero",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]

        tensNames = [
            "Ten",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]

        units = [
            "Thousand",
            "Million",
            "Billion",
            "Trillion",
            "Quadrillion",
            "Quintillion",
            "Sextillion",
            "Septillion",
            "Octillion",
            "Nonillion",
            "Decillion",
            "Undecillion",
            "Duodecillion",
            "Tredecillion",
            "Quattuordecillion",
            "Quindecillion",
            "Sexdecillion",
            "Septendecillion",
            "Octodecillion",
            "Novemdecillion",
        ]

        def handleUnderThousand(small: int):
            res = ""
            if not small:
                return "Zero"
            if small >= 1000:
                return res
            if small // 100:
                res += " " + numNames[small // 100] + " Hundred"
            remainderTens = small % 100
            if remainderTens and remainderTens < len(numNames):
                res += " " + numNames[remainderTens]
            else:
                div, rem = divmod(remainderTens, 10)
                if div:
                    res += " " + tensNames[div - 1]
                if rem:
                    res += " " + numNames[rem]
            return res[1:]

        res = ""
        i = 0
        if not num:
            return "Zero"
        while num:
            num, rem = divmod(num, 1000)
            tmp = handleUnderThousand(rem)
            if tmp != "Zero":
                if i >= 1:
                    tmp2 = res
                    res = tmp + " " + units[i - 1]
                    if tmp2:
                        res += " " + tmp2
                else:
                    res = tmp
            i += 1

        return res


assert Solution().numberToWords(1000) == "One Thousand"
assert Solution().numberToWords(123) == "One Hundred Twenty Three"
assert (
    Solution().numberToWords(1234567)
    == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
)
