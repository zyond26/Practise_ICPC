def permutation(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i == -1:
        return False
    j = len(arr) - 1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])
    return True
n = int(input())
arr = list(range(1, n + 1))
print(" ".join(map(str, arr)))
while permutation(arr):
    print(" ".join(map(str, arr)))
