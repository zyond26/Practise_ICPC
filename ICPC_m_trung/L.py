def largest_number_digit(N, K):
    numbers = [str(i) for i in range(1, N + 1)]
    
    numbers.sort(reverse=True, key=lambda x: x * 20)  
    
    total_length = 0
    for number in numbers:
        total_length += len(number)
    
    if K > total_length:
        return -1
    
    current_length = 0
    for number in numbers:
        current_length += len(number)
        if current_length >= K:
            return number[K - (current_length - len(number)) - 1]

T = int(input())
results = []
for _ in range(T):
    N, K = map(int, input().split())
    results.append(largest_number_digit(N, K))

for result in results:
    print(result)