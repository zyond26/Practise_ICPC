import math
from itertools import combinations
from functools import reduce

MOD = 10**9 + 7

#tính LCM của hai số
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_multiple(nums):
    return reduce(lcm, nums)

def solve_case(arr):
    N = len(arr)
    total_sum = 0
    # Duyệt qua tất cả các tập con không rỗng của dãy
    for r in range(1, N + 1):
        for subset in combinations(arr, r):
            total_sum = (total_sum + lcm_multiple(subset)) % MOD
    return total_sum

def solve():
    T = int(input())  
    for _ in range(T):
        N = int(input())  
        arr = list(map(int, input().split()))  
        print(solve_case(arr))

if __name__ == "__main__":
    solve()
