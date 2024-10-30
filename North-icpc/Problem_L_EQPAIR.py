MOD = 10**9 + 7

def pairs(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    pairs_count = 0
    for count in freq.values():
        if count > 1:
            pairs_count += (count * (count - 1)) // 2
            pairs_count %= MOD  
    
    return pairs_count

n = int(input())
arr = list(map(int, input().split()))

print(pairs(arr))
