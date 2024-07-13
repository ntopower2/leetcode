from typing import List


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        robots = sorted(
            [
                [rob[0], rob[1], rob[2], i]
                for i, rob in enumerate(zip(positions, healths, directions))
            ]
        )
        stackRight = []

        for robot in robots:
            if robot[2] == "R":
                stackRight.append(robot)
                continue
            while stackRight and stackRight[-1][2] == "R" and robot[1]:
                if robot[1] == stackRight[-1][1]:
                    robot[1] = 0
                    stackRight[-1][1] = 0
                    stackRight.pop()
                elif robot[1] > stackRight[-1][1]:
                    robot[1] -= 1
                    stackRight.pop()
                else:
                    robot[1] = 0
                    stackRight[-1][1] -= 1
            if robot[1]:
                stackRight.append(robot)

        return list(
            map(lambda x: x[1], sorted([v for v in stackRight], key=lambda x: x[3]))
        )


assert Solution().survivedRobotsHealths([3, 5, 2, 6], [10, 10, 15, 12], "RLRL") == [14]
