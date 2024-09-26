#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#

# @lc code=start
from sortedcontainers import SortedList


class MyCalendar:
    def __init__(self):
        self.books = SortedList()

    def book(self, start: int, end: int) -> bool:
        index = self.books.bisect_left((start, end))

        if (index and self.books[index - 1][1] > start) or (
            index < len(self.books) and self.books[index][0] < end
        ):
            return False
        self.books.add((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end
