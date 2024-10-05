def longest_palindromic(s):
    res = ""
    
    def expand(left, right):
        nonlocal res
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if len(res) < right - left - 1:
            res = s[left + 1:right]

    for i in range(len(s)):
        expand(i, i)       # Odd length palindrome
        expand(i, i + 1)   # Even length palindrome

    return res

s = input().strip()
print(longest_palindromic(s))