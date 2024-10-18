def count_beautiful_substrings(s):
    n = len(s)
    count = 0
    for i in range(n - 2):
        if s[i] != s[i + 1] and s[i] != s[i + 2] and s[i + 1] != s[i + 2]:
            count += 1
    return count

n = int(input())
s = input()

result = count_beautiful_substrings(s)
print(result)

