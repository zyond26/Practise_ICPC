# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)

# def combination(n, k):
#     return factorial(n) // (factorial(k) * factorial(n - k))

# def candy(n, k):
#     return combination(n + k - 1, k - 1)

# n,k = map(int,input().split())
# ways = candy(n, k)
# print(ways)

def permutations(nums, start):
    if start == len(nums):
        print(" ".join(map(str, nums)))  
        return
    
    for i in range(start, len(nums)):
        nums[start], nums[i] = nums[i], nums[start] 
        permutations(nums, start + 1)  
        nums[start], nums[i] = nums[i], nums[start]  

def main():
    n = int(input())
    nums = list(range(1, n + 1))
    permutations(nums, 0)

main()