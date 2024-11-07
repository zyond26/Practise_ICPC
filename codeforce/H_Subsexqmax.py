#  cách 1 . quy hoạch động 
# def max_sum(arr):
#     l = arr[0]
#     r = arr[0]
    
#     for i in range(1, len(arr)):
#         l = max(arr[i], l + arr[i])
        
#         if l > r:
#             r = l
#     return r
 
# n = int(input())
# arr = list(map(int, input().split()))
 
# if len(arr) != n:
#     print("Error")
# else:
#     result = max_sum(arr)
#     print(result)




#  cách 2. Chia để trị

def max_crossing_sum(arr, left, mid, right):
    left_sum = float('-inf')
    total = 0
    for i in range(mid, left - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total

    right_sum = float('-inf')
    total = 0
    for i in range(mid + 1, right + 1):
        total += arr[i]
        if total > right_sum:
            right_sum = total

    return left_sum + right_sum

def max_subarray_sum(arr, left, right):
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    max_left_sum = max_subarray_sum(arr, left, mid)
    max_right_sum = max_subarray_sum(arr, mid + 1, right)
    max_cross_sum = max_crossing_sum(arr, left, mid, right)

    return max(max_left_sum, max_right_sum, max_cross_sum)

n = int(input())
arr = list(map(int, input().split()))
result = max_subarray_sum(arr, 0, n - 1)
print(result)
