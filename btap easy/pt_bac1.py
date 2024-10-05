# giải phương trình bậc nhất 

# a,b = map(int,input().split())

# def solve(a, b):
#     if a == 0:
#         if b == 0:
#             return "WOW" 
#         else:
#             return "NO"
#     else:
#         solution = -b / a
#         return f"{solution:.2f}" 
# print(solve(a, b))






# pt bậc 2 :
import math

a,b,c = map(float,input().split())

def solve(a, b, c):
    denta = b ** 2 - 4 * a * c

    if a == 0:
        # If a is 0, it's actually a linear equation
        if b == 0:
            return "WOW" if c == 0 else "NO"  # Infinite solutions or no solution
        else:
            return f"{-c / b:.2f}"  # Linear equation solution

    if denta < 0:
        return "NO"  # No real solution

    elif denta == 0:
        root = -b / (2 * a)
        return f"{root:.2f}"

    else:
        root1 = (-b + math.sqrt(denta)) / (2 * a)
        root2 = (-b - math.sqrt(denta)) / (2 * a)
        root1,root2 = sorted([root1,root2])
        return f"{root1:.2f} {root2:.2f}"
print(solve(a, b, c))
