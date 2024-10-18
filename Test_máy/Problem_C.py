def is_Trinh_number(n):
    temp = n
    while temp > 0:
        digit = temp % 10  
        if digit == 0 or n % digit != 0:
            return False
        temp //= 10 
    return True

def count_Trinh_numbers(l, r):
    return sum(1 for num in range(l, r + 1) if is_Trinh_number(num))

l, r = map(int, input().split())
print(count_Trinh_numbers(l, r))

