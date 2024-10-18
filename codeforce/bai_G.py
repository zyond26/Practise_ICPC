from collections import defaultdict

def largest_match(L, C, image1, image2):
    translation_count = defaultdict(int)

    points_image1 = [(i, j) for i in range(L) for j in range(C) if image1[i][j] == 1]
    points_image2 = [(i, j) for i in range(L) for j in range(C) if image2[i][j] == 1]
    
    if not points_image1 or not points_image2:
        return 0
    
    for (x1, y1) in points_image1:
        for (x2, y2) in points_image2:
            dx = x1 - x2
            dy = y1 - y2
            translation_count[(dx, dy)] += 1

    return max(translation_count.values(), default=0)

def solve():
    t = int(input())  
    for _ in range(t):
        L, C = map(int, input().split())

        image1 = [list(map(int, input().split())) for _ in range(L)]
        image2 = [list(map(int, input().split())) for _ in range(L)]
        
        result = largest_match(L, C, image1, image2)
        print(result)

if __name__ == "__main__":
    solve()
