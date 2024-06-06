from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def produceNodes(curr):
            neighbors = []
            for c in range(len(curr)):
                tmp = curr[0:c] + str((int(curr[c]) + 1) % 10) + curr[c + 1 :]
                if tmp not in deadends:
                    neighbors.append(tmp)
                tmp = curr[0:c] + str((int(curr[c]) - 1) % 10) + curr[c + 1 :]
                if tmp not in deadends:
                    neighbors.append(tmp)

            return neighbors

        if "0000" in deadends:
            return -1
        graph = {}
        distances = {}
        visited = set()
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    for l in range(10):
                        key = f"{i}{j}{k}{l}"
                        graph[key] = produceNodes(key)
                        distances[key] = float("inf")
            visited = set()

        distances["0000"] = 0

        queue = deque(["0000"])
        while queue:
            curr = queue.popleft()
            visited.add(curr)

            for neighbor in graph[curr]:
                if neighbor not in visited:
                    new_distance = distances[curr] + 1
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        queue.append(neighbor)

        if target in distances and distances[target] != float("inf"):
            return distances[target]
        else:
            return -1


print(
    Solution().openLock(
        ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"
    )
)
