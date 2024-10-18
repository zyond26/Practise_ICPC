def matrix_coloring(n, m, grid):
    visited = [[False] * m for _ in range(n)]  # Matrix to track visited cells
    actions = 0  

    def dfs(x, y, direction):
        visited[x][y] = True
        if direction == 'row':
            for j in range(y + 1, m):  # Color all consecutive '#' in the row
                if grid[x][j] == '#' and not visited[x][j]:
                    visited[x][j] = True
                else:
                    break
        elif direction == 'col':
            for i in range(x + 1, n):  # Color all consecutive '#' in the column
                if grid[i][y] == '#' and not visited[i][y]:
                    visited[i][y] = True
                else:
                    break

    # Traverse the matrix
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#' and not visited[i][j]:
                actions += 1  # Start a new coloring action
                dfs(i, j, 'row')  # First color the row
                dfs(i, j, 'col')  # Then color the column

    return actions

n, m = map(int, input().split())  # Matrix dimensions
grid = [input().strip() for _ in range(n)]  # The matrix grid

print(matrix_coloring(n, m, grid))
