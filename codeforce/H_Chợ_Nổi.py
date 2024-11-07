import bisect

def get_all_sums(weights):
    all_sums = [0]
    for weight in weights:
        current_length = len(all_sums)
        for i in range(current_length):
            new_sum = all_sums[i] + weight
            bisect.insort(all_sums, new_sum)
    return all_sums

n, m = map(int, input().split())
bags = list(map(int, input().split()))
boats = [int(input()) for _ in range(m)]

half = n // 2
A = bags[:half]
B = bags[half:]

sum_A = get_all_sums(A)
sum_B = get_all_sums(B)

results = []
for boat_capacity in boats:
    max_rice = 0
    right = len(sum_B) - 1
    for a in sum_A:
        if a > boat_capacity:
            break
        while right >= 0 and a + sum_B[right] > boat_capacity:
            right -= 1
        if right >= 0:
            max_rice = max(max_rice, a + sum_B[right])
    results.append(max_rice)

for result in results:
    print(result)
