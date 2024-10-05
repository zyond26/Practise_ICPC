# import math
# t = int(input())
# def snt(t):
#     if t <= 1:
#         return False
#     if t >= 4:
#         if t % 2 == 0 or t % 3 == 0:
#             return False
#         for i in range(5, int(math.sqrt(t)) + 1, 6):
#             if t % i == 0 or t % (i + 2) == 0:
#                 return False
#     return True
# print(snt(t))



def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())

if is_prime(n):
    print("YES")
else:
    print("NO")
