from collections import deque

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(grid, start, R, C):
    queue = deque([start])
    dist = [[-1] * C for _ in range(R)]
    dist[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != '#' and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

    return dist

def island_challenge(R, C, N, grid):
    shrines = []
    start = (0, 0)  

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'S':
                shrines.append((i, j))

    all_positions = [start] + shrines
    dist = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        d = bfs(grid, all_positions[i], R, C)
        for j in range(N + 1):
            if d[all_positions[j][0]][all_positions[j][1]] == -1:
                dist[i][j] = float('inf')
            else:
                dist[i][j] = d[all_positions[j][0]][all_positions[j][1]]

    dp = [[float('inf')] * (N + 1) for _ in range(1 << (N + 1))]
    dp[1][0] = 0  

    for mask in range(1 << (N + 1)):
        for u in range(N + 1):
            if dp[mask][u] == float('inf'):
                continue
            for v in range(1, N + 1):
                if not (mask & (1 << v)):
                    dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + dist[u][v])

    final_mask = (1 << (N + 1)) - 1
    result = min(dp[final_mask][i] for i in range(1, N + 1))

    return result if result != float('inf') else -1

if __name__ == "__main__":
    R, C, N = map(int, input().split())

    grid = []
    for _ in range(R):
        grid.append(input().strip())

    print(island_challenge(R, C, N, grid))
