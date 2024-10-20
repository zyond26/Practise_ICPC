def find_best_k(s):
    n = len(s)
    
    # Tính toán tiền tố (prefix sums)
    prefix_R = [0] * (n + 1)
    prefix_P = [0] * (n + 1)
    prefix_S = [0] * (n + 1)
    
    for i, char in enumerate(s):
        prefix_R[i+1] = prefix_R[i] + (char == 'R')
        prefix_P[i+1] = prefix_P[i] + (char == 'P')
        prefix_S[i+1] = prefix_S[i] + (char == 'S')
    
    max_wins = 0
    best_k = 1
    
    # Kiểm tra từng k từ 2 đến n
    for k in range(2, n + 1):
        wins = 0
        for i in range(0, n, k):
            end = min(i + k, n)
            rock_count = prefix_R[end] - prefix_R[i]
            paper_count = prefix_P[end] - prefix_P[i]
            scissor_count = prefix_S[end] - prefix_S[i]
            wins += max(rock_count, paper_count, scissor_count)
        
        if wins > max_wins:
            max_wins = wins
            best_k = k
        elif wins == max_wins:
            best_k = max(best_k, k)
    
    return best_k

# Đọc input
t = int(input())
results = []

for _ in range(t):
    s = input().strip()
    results.append(find_best_k(s))

# In kết quả
for result in results:
    print(result)