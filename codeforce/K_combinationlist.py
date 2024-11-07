def generate_combinations(n, m, start, combination):
    if len(combination) == m:
        print(" ".join(map(str, combination)))
        return

    for i in range(start, n + 1):
        combination.append(i)
        generate_combinations(n, m, i + 1, combination)
        combination.pop()

n, m = map(int, input().split())

generate_combinations(n, m, 1, [])
