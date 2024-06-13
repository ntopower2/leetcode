from typing import List
from heapq import heapify, heappop
from time import time
from random import randint


class Solution:
    def minMovesToSeat2(self, seats: List[int], students: List[int]) -> int:
        s = time()
        heapify(seats)
        heapify(students)
        res = 0
        while seats:
            seat = heappop(seats)
            student = heappop(students)
            res += abs(seat - student)
        t = time()
        print("elapsed2 ", t - s)
        return res

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        s = time()
        seats.sort()
        students.sort()
        res = 0
        for seat, student in zip(seats, students):
            res += abs(seat - student)
        t = time()
        print("elapsed ", t - s)
        return res


def produceArray(size=10**6):
    seats = [randint(1, size / 2) for _ in range(size)]
    students = [randint(1, size / 2) for _ in range(size)]
    return (seats, students)


seats, students = produceArray()
s = Solution()
se2 = seats.copy()
st2 = students.copy()
s.minMovesToSeat(seats, students)
s.minMovesToSeat2(se2, st2)
