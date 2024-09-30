#
# @lc app=leetcode id=1381 lang=python3
#
# [1381] Design a Stack With Increment Operation
#


# @lc code=start
class CustomStack:
    def __init__(self, maxSize: int):
        self.values = [-1] * maxSize
        self.size = 0

    def push(self, x: int) -> None:
        if self.size == len(self.values):
            return
        self.values[self.size] = x
        self.size += 1

    def pop(self) -> int:
        if not self.size:
            return -1

        self.size -= 1
        tmp = self.values[self.size]
        return tmp

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.size)):
            self.values[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# @lc code=end


def driver(operations, values):
    struct = None
    results = []

    for i, operation in enumerate(operations):
        if operation == "CustomStack":
            struct = CustomStack(values[i][0])
            results.append(None)
        elif operation == "push":
            struct.push(values[i][0])
            results.append(None)
        elif operation == "pop":
            results.append(struct.pop())
        elif operation == "increment":
            struct.increment(values[i][0], values[i][1])
            results.append(None)

    return results


assert driver(
    [
        "CustomStack",
        "push",
        "push",
        "pop",
        "push",
        "push",
        "push",
        "increment",
        "increment",
        "pop",
        "pop",
        "pop",
        "pop",
    ],
    [[3], [1], [2], [], [2], [3], [4], [5, 100], [2, 100], [], [], [], []],
) == [None, None, None, 2, None, None, None, None, None, 103, 202, 201, -1]
