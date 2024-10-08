# cho 1 mảng , tìm 4 số trong mảng sao cho bằng 1 tổng cho trước và các bộ số không lặp lại
#  vd: [1,0,-1,0,-2,2] sum =0;
# a) [-2,-1,1,2]; [-2,0,0,2],[-1,0,0,-1]
# b) [2,2,2,2,2] sum =8;--> [2,2,2,2]

#  ------------------- Giải ----------------------------

def four_sum(nums, target):
    nums.sort()
    results = set()
    n = len(nums)
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left, right = j + 1, n - 1
            while left < right:
                s = nums[i] + nums[j] + nums[left] + nums[right]
                if s == target:
                    results.add((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1

    return [list(result) for result in results]
n = int(input())
arr = list(map(int, input().split()))
target = int(input())
print(four_sum(arr, target))
