#ktra số chính phương 

import math
n = int(input())
def is_perfect_square(n):
    if n < 0:
        return False
    sqrt_n = math.isqrt(n)
    return sqrt_n * sqrt_n == n
if is_perfect_square(n):
    print("YES")
else:
    print("NO")
