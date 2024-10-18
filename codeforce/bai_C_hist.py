def largest_rectangle(heights):
    n = len(heights)
    Left = [0] * n  
    Right = [0] * n  
    stack = []

    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if not stack:
            Left[i] = -1 
        else:
            Left[i] = stack[-1]
        stack.append(i)

    stack.clear()

    for i in range(n-1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if not stack:
            Right[i] = n  
        else:
            Right[i] = stack[-1]
        stack.append(i)

    res = 0
    for i in range(n):
        width = Right[i] - Left[i] - 1
        res = max(res, width * heights[i])

    return res

def solve():
    with open('hist.inp', 'r') as infile:
        data = infile.read().splitlines()  

    results = []

    for line in data:
        arr = list(map(int, line.split()))  
        n = arr[0]  
        if n == 0: 
            break
        heights = arr[1:]  
        results.append(str(largest_rectangle(heights)))  

    with open('hist.out', 'w') as outfile:
        outfile.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
