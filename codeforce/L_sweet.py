MOD = 10**9 + 7

def sweet(limit, mod):
    factorial = [1] * (limit + 1)
    inv_factorial = [1] * (limit + 1)
    
    for i in range(2, limit + 1):
        factorial[i] = factorial[i - 1] * i % mod
    
    inv_factorial[limit] = pow(factorial[limit], mod - 2, mod)
    
    for i in range(limit - 1, 0, -1):
        inv_factorial[i] = inv_factorial[i + 1] * (i + 1) % mod
    
    return factorial, inv_factorial

def combination(n, k, factorial, inv_factorial, mod):
    if k > n or k < 0:
        return 0
    return factorial[n] * inv_factorial[k] % mod * inv_factorial[n - k] % mod

def count_ways(n, k):
    limit = n + k - 1
    factorial, inv_factorial = sweet(limit, MOD)
    return combination(n + k - 1, k - 1, factorial, inv_factorial, MOD)

n, k = map(int, input().split())

print(count_ways(n, k))
