
def find_max_in_array(n, arr):
    if n == 0:
        return None
    return max(arr)

n = int(input())
arr = list(map(int, input().split()))

print(find_max_in_array(n, arr))
