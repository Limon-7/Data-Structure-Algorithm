from collections import deque
from typing import List


def bfs(matrix: List[List[int]]) -> int:
    rows, cols = len(matrix), len(matrix[0])
    visit = set()
    queue = deque()
    queue.append((0, 0))
    visit.add((0, 0))

    length = 0
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            if r == rows - 1 and c == cols - 1:
                return length

            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr, dc in neighbors:
                if (
                    min(dr + r, c + dc) < 0
                    or r + dr == rows
                    or c + dc == cols
                    or (r + dr, c + dc) in visit
                    or matrix[r + dr][c + dc] == 1
                ):
                    continue
                
                queue.append((r + dr, c + dc))
                visit.add((r + dr, c + dc))
        length += 1

matrix = [[0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]
print(bfs(matrix)) # 6 #TC=O(r*c) SC: O(r*n)