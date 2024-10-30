n = int(input())
board = []

for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

white_sum = [[0] * (n + 1) for _ in range(n + 1)]
black_sum = [[0] * (n + 1) for _ in range(n + 1)]

#  sum white and black
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i + j) % 2 == 0:  # white
            white_sum[i][j] = board[i - 1][j - 1]
            black_sum[i][j] = 0
        else:  #black
            white_sum[i][j] = 0
            black_sum[i][j] = board[i - 1][j - 1]
        
        white_sum[i][j] += white_sum[i - 1][j] + white_sum[i][j - 1] - white_sum[i - 1][j - 1]
        black_sum[i][j] += black_sum[i - 1][j] + black_sum[i][j - 1] - black_sum[i - 1][j - 1]

q = int(input())
question = []
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    question.append((x1 - 1, y1 - 1, x2 - 1, y2 - 1))  

def get_sum(prefix_sum, x1, y1, x2, y2):
    return (
        prefix_sum[x2 + 1][y2 + 1]
        - (prefix_sum[x1][y2 + 1] if x1 > 0 else 0)
        - (prefix_sum[x2 + 1][y1] if y1 > 0 else 0)
        + (prefix_sum[x1][y1] if x1 > 0 and y1 > 0 else 0)
    )

for x1, y1, x2, y2 in question:
    sum_white = get_sum(white_sum, x1, y1, x2, y2)
    sum_black = get_sum(black_sum, x1, y1, x2, y2)
    result = abs(sum_white - sum_black)
    print(result)
 