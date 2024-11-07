def can_place_cows(positions, N, C, distance):
    count = 1  
    last_position = positions[0]
    
    for i in range(1, N):
        if positions[i] - last_position >= distance:
            count += 1
            last_position = positions[i]
            if count == C:
                return True
    return False

def largest_min_distance(positions, N, C):
    positions.sort()
    
    low, high = 1, positions[-1] - positions[0]
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        if can_place_cows(positions, N, C, mid):
            result = mid 
            low = mid + 1  
        else:
            high = mid - 1 
    
    return result

t = int(input())
for _ in range(t):
    N, C = map(int, input().split())
    positions = [int(input()) for _ in range(N)]
    print(largest_min_distance(positions, N, C))
