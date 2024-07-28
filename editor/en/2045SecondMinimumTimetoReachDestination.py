from collections import defaultdict, deque
from typing import List


class Solution:
    def secondMinimum(
        self, n: int, edges: List[List[int]], time: int, change: int
    ) -> int:

        graph = defaultdict(list)
        times = [[float("inf"), float("inf")] for _ in range(n)]
        times[0][0] = 0

        for u, v in edges:
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)

        q = deque([(0, 0)])

        while q:
            cn, ct = q.popleft()
            for node in graph[cn]:
                nt = ct + time
                d, m = divmod(ct, change)
                if d % 2:
                    nt += change - m

                if nt < times[node][0]:
                    times[node][1] = times[node][0]
                    times[node][0] = nt
                    q.append((node, nt))
                elif times[node][0] < nt < times[node][1]:
                    times[node][1] = nt
                    q.append((node, nt))

        return times[n - 1][1]


assert Solution().secondMinimum(n=2, edges=[[1, 2]], time=3, change=2) == 12  # 1
assert (
    Solution().secondMinimum(
        n=5, edges=[[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], time=3, change=5
    )
    == 13
)
