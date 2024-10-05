#  đảo số n

n = int(input())

def daoso(n):
    s = 0
    while n != 0:
        s = s * 10 + n % 10
        n = n // 10
    return s
sodao = daoso(n)
print(sodao)
