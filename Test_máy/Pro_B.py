def count_dazzling_sequences(cards):
    n = len(cards)
    seen = {}
    left = 0
    dazzling_count = 0

    for right in range(n):
        if cards[right] in seen:
            seen[cards[right]] += 1
        else:
            seen[cards[right]] = 1

        while seen[cards[right]] > 1:
            seen[cards[left]] -= 1
            if seen[cards[left]] == 0:
                del seen[cards[left]]
            left += 1

        dazzling_count += (right - left + 1)

    return dazzling_count

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))
    results.append(count_dazzling_sequences(cards))

for result in results:
    print(result)