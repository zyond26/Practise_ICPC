MOD = 998244353

# Hàm đệ quy với memoization để đếm số lượng dãy đối xứng thỏa mãn
def count_palindromic_sequences(n, k, memo):
    if n == 0:
        return 1  # Nếu tổng là 0, chỉ có một cách là không thêm phần tử nào
    if n < 0:
        return 0  # Không có cách nào để tạo tổng âm
    if (n, k) in memo:
        return memo[(n, k)]
    
    count = 0
    for i in range(1, n // 2 + 1):  # Chỉ xét một nửa dãy để tạo đối xứng
        if i != k:  # Không cho phép số K
            count += count_palindromic_sequences(n - 2 * i, k, memo) % MOD
            count %= MOD

    memo[(n, k)] = count
    return count

# Hàm chính để xử lý từng trường hợp
def solve(test_cases):
    results = []
    memo = {}
    for n, k in test_cases:
        result = count_palindromic_sequences(n, k, memo)
        results.append(result)
    return results

# Đọc đầu vào
T = int(input().strip())
test_cases = []
for _ in range(T):
    N, K = map(int, input().strip().split())
    test_cases.append((N, K))

# Tính toán và in kết quả
results = solve(test_cases)
for result in results:
    print(result)
