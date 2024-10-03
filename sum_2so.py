# a, b,c = [int(x) for x in input().split()]
# print(a+b+c)

# tổng , hiệu, tích, thương

# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)

# if b != 0:
#     thuong = a / b
#     print("{:.2f}".format(thuong))
# else:
#     print("ERROR ")

#  lấy phần dư
# a, b = map(int, input().split())
# if b!=0 :
#     print(a%b)


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
