from typing import List


class State:
    def __init__(self, obstacles: list) -> None:
        self.i = 0
        self.dist = 0
        self.pos = [0, 0]
        self.dir = ((0, 1), (1, 0), (0, -1), (-1, 0))
        self.obstacles = set(map(tuple, obstacles))

    @staticmethod
    def euclidean(pos: list):
        return pos[0] ** 2 + pos[1] ** 2

    def move(self, x):
        if x == -2:
            self.i -= 1
        elif x == -1:
            self.i += 1
        else:
            self.i %= len(self.dir)
            cur = self.dir[self.i]
            for _ in range(x):
                if (self.pos[0] + cur[0], self.pos[1] + cur[1]) not in self.obstacles:
                    self.pos[0] += cur[0]
                    self.pos[1] += cur[1]
                else:
                    break
            self.dist = max(self.dist, self.euclidean(self.pos))


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        s = State(obstacles)
        for cmd in commands:
            s.move(cmd)
        return s.dist


assert Solution().robotSim(commands=[4, -1, 4, -2, 4], obstacles=[[2, 4]]) == 65
