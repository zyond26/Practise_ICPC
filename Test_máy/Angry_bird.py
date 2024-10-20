def classify_trajectory(t, cases):
    results = []
    for a, b, c in cases:
        if c > 0:
            results.append("CURVE UP")
        elif c < 0:
            results.append("CURVE DOWN")
        else:
            results.append("NO CURVE")
    return results

t = int(input())  
cases = [tuple(map(int, input().split())) for _ in range(t)]

results = classify_trajectory(t, cases)
for result in results:
    print(result)
