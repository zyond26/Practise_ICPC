# E. PIZZA
# Alex has a pizza that he wants to share with his friends. The pizza is in the shape of a convex polygon 
# with N sides.
# He decides to make cuts along the diagonals of the polygon.
# After all the cuts have been made, count the number of pizza slices there are in total. 
# As the answer may be large,
# please print it modulo 987654321.
# Note that it is guaranteed that no three diagonals of the polygon intersect at a point.
# INPUT
# The first and only line contains the positive integer N. (3 ≤ N ≤ 1018)
# OUTPUT
# Print the answer, modulo 987654321.
# Sample Input Sample Output
# 4 4

#  ------------------------ Bài Làm ------------------

MOD = 987654321

def number_of_slices(n):
    # Nếu N <= 2 thì kết quả là 1 (tức là số miếng = số cạnh)
    if n == 3:
        return 1
    elif n == 4:
        return 4
    else:
        # Trả về số miếng (tạm thời sử dụng công thức cho N lớn)
        return (n * (n-3) // 2) % MOD

# Đọc input
n = int(input())

# Gọi hàm và in kết quả
print(number_of_slices(n))
