#
# @lc app=leetcode id=731 lang=python3
#
# [731] My Calendar II
#


# @lc code=start
from sortedcontainers import SortedDict


class MyCalendarTwo:
    def __init__(self):
        self.books = SortedDict()

    def book(self, start: int, end: int) -> bool:
        self.books[start] = self.books.get(start, 0) + 1
        self.books[end] = self.books.get(end, 0) - 1

        occur = 0

        for count in self.books.values():
            occur += count
            if occur > 2:
                self.books[start] -= 1
                self.books[end] += 1
                return False

        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
# @lc code=end
obj = MyCalendarTwo()
for start, end in [[10, 20], [50, 60], [15, 40], [5, 15], [5, 10], [25, 55]]:
    obj.book(start, end)
