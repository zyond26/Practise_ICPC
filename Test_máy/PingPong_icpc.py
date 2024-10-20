def count_scenarios(n, sA, sB):
    memo = {}

    def solve(a, b):
        if (a, b) in memo:
            return memo[(a, b)]

        if a == sA and b == sB:
            if (a >= n and a - b >= 2) or (b >= n and b - a >= 2):
                return 1
            return 0
        
        if a > sA or b > sB:
            return 0
        
        memo[(a, b)] = solve(a + 1, b) + solve(a, b + 1)
        return memo[(a, b)]

    return solve(0, 0)

T = int(input())  
results = []
for _ in range(T):
    n, sA, sB = map(int, input().split())  
    results.append(count_scenarios(n, sA, sB))

print("\n".join(map(str, results)))
