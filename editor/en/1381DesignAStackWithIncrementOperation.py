#
# @lc app=leetcode id=1381 lang=python3
#
# [1381] Design a Stack With Increment Operation
#


# @lc code=start
class CustomStack:
    def __init__(self, maxSize: int):
        self.values = [-1] * maxSize
        self.increments = [0] * maxSize
        self.size = 0

    def push(self, x: int) -> None:
        if self.size < len(self.values):
            self.values[self.size] = x
            self.size += 1

    def pop(self) -> int:
        if not self.size:
            return -1

        self.size -= 1
        tmp = self.values[self.size] + self.increments[self.size]
        if self.size:
            self.increments[self.size - 1] += self.increments[self.size]
        self.increments[self.size] = 0
        return tmp

    def increment(self, k: int, val: int) -> None:
        if not self.size:
            return
        self.increments[min(k, self.size) - 1] += val


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
        "pop",
        "increment",
        "push",
        "increment",
        "increment",
        "increment",
        "pop",
        "increment",
    ],
    [[30], [], [3, 40], [30], [4, 63], [2, 79], [5, 57], [], [5, 32]],
) == [None, -1, None, None, None, None, None, 229, None]
