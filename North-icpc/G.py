def is_nice_string(s):
    n = len(s)
    if '1' not in s:
        return False
        
    for i in range(n):
        if s[i] == '1':
            left_zeros = 0
            j = i - 1
            while j >= 0 and s[j] == '0':
                left_zeros += 1
                j -= 1
                
            right_zeros = 0
            j = i + 1
            while j < n and s[j] == '0':
                right_zeros += 1
                j += 1
                
            if left_zeros != right_zeros:
                return False
                
    return True

def solve(n, s):
    max_len = 0
    
    for mask in range(1 << n):
        curr = ""
        for i in range(n):
            if mask & (1 << i):
                curr += s[i]
                
        if len(curr) > 0 and '1' in curr and is_nice_string(curr):
            max_len = max(max_len, len(curr))
            
    return max_len

n = int(input())
s = input().strip()

print(solve(n, s))




