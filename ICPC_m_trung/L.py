from functools import cmp_to_key

# so sánh hai chuỗi để tạo số lớn nhất
def compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

def find_digit(N, K):
    digits = [str(i) for i in range(1, N + 1)]  
    
    # Sắp xếp các số theo thứ tự để tạo ra số lớn nhất
    digits.sort(key=cmp_to_key(compare))  
    
    largest_number = ''.join(digits)  
    
    if len(largest_number) >= K:
        return largest_number[K - 1]  
    else:
        return -1  

def solve():
    T = int(input())  
    results = []
    
    for _ in range(T):
        N, K = map(int, input().split())  
        results.append(find_digit(N, K))  
    
    for result in results:
        print(result)

if __name__ == "__main__":
    solve()
