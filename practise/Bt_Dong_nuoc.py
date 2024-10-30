def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def water_jug_solution(a, b, c):
    # Kiểm tra điều kiện có thể đong được C lít nước
    if c > max(a, b) or c % gcd(a, b) != 0:
        return "Không thể đong chính xác lượng nước yêu cầu"

    # Khởi tạo trạng thái ban đầu
    x, y = 0, 0
    steps = []
    
    # Thuật toán mô phỏng các thao tác
    while x != c and y != c:
        if x == 0:  # Đổ đầy bình a
            x = a
            steps.append(f"Đổ đầy bình {a}-lít: ({x}, {y})")
        elif y == b:  # Đổ hết bình b
            y = 0
            steps.append(f"Đổ hết bình {b}-lít: ({x}, {y})")
        else:  # Đổ nước từ bình a sang bình b
            pour = min(x, b - y)
            x -= pour
            y += pour
            steps.append(f"Đổ từ bình {a}-lít sang bình {b}-lít: ({x}, {y})")

    return steps

# Ví dụ
a, b, c = 5, 3, 4
result = water_jug_solution(a, b, c)
if isinstance(result, list):
    for step in result:
        print(step)
else:
    print(result)
