#
# @lc app=leetcode id=641 lang=python3
#
# [641] Design Circular Deque
#


# @lc code=start
class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.begin = 0
        self.end = 0
        self.values = [-1] * k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.begin -= 1
        self.begin += self.k
        self.begin %= self.k
        self.values[self.begin] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.values[self.end] = value
        self.end += 1
        self.end %= self.k
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.begin += 1
        self.begin %= self.k
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.end -= 1
        self.end += self.k
        self.end %= self.k
        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.values[self.begin] if not self.isEmpty() else -1

    def getRear(self) -> int:
        return (
            self.values[(self.end - 1 + self.k) % self.k] if not self.isEmpty() else -1
        )

    def isEmpty(self) -> bool:
        return not self.size

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end
def driver(operations, values):
    deque = None  # This will hold the deque instance
    results = []  # List to store the results of each operation

    for i, operation in enumerate(operations):
        if operation == "MyCircularDeque":
            k = values[i][0]
            deque = MyCircularDeque(k)
            results.append(None)  # The constructor does not return anything

        elif operation == "insertLast":
            result = deque.insertLast(values[i][0])
            results.append(result)

        elif operation == "insertFront":
            result = deque.insertFront(values[i][0])
            results.append(result)

        elif operation == "deleteLast":
            result = deque.deleteLast()
            results.append(result)

        elif operation == "deleteFront":
            result = deque.deleteFront()
            results.append(result)

        elif operation == "getFront":
            result = deque.getFront()
            results.append(result)

        elif operation == "getRear":
            result = deque.getRear()
            results.append(result)

        elif operation == "isEmpty":
            result = deque.isEmpty()
            results.append(result)

        elif operation == "isFull":
            result = deque.isFull()
            results.append(result)

    return results


assert driver(
    [
        "MyCircularDeque",
        "insertLast",
        "insertLast",
        "insertFront",
        "insertFront",
        "getRear",
        "isFull",
        "deleteLast",
        "insertFront",
        "getFront",
    ],
    [[3], [1], [2], [3], [4], [], [], [], [4], []],
) == [None, True, True, True, False, 2, True, True, True, 4]
