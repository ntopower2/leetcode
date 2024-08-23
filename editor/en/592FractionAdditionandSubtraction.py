from math import gcd
import re


class Fraction:
    def __init__(self, expression: list) -> None:
        if len(expression) != 3:
            raise Exception()
        self.nom = int(expression[1])
        if expression[0] == "-":
            self.nom *= -1
        self.denom = int(expression[2])

    def __add__(self, other):
        if other.denom == self.denom:
            self.nom += other.nom
        else:
            self.nom *= other.denom
            self.nom += other.nom * self.denom
            self.denom *= other.denom
        self.simplify()
        return self

    def simplify(self):
        gcd_ = gcd(self.nom, self.denom)
        self.nom //= gcd_
        self.denom //= gcd_

    def __str__(self) -> str:
        return f"{self.nom}/{self.denom}"


class Solution:
    def fractionAddition(self, expression: str) -> str:
        nextFraction = re.compile("(-)?(\d+)/(\d+)")
        fractions = nextFraction.findall(expression)
        base = Fraction(fractions[0])
        for fraction in fractions[1:]:
            base += Fraction(fraction)
        return str(base)


assert Solution().fractionAddition("-1/2+1/2+1/3") == "1/3"
