def gcd(a, b):
    """Hàm tính GCD của hai số a và b sử dụng thuật toán Euclid"""
    while b != 0:
        a, b = b, a % b
    return a

def waterMeasure(a, b, x):
    """Hàm giải bài toán đong nước, hiển thị quá trình"""
    # Kiểm tra nếu không thể đong chính xác x lít
    if x % gcd(a, b) != 0 or x > max(a, b):
        print(f"Không thể đong chính xác {x} lít nước bằng hai bình {a} và {b}.")
        return

    def pour(from_cap, to_cap, target):
        """Giả lập quá trình đong nước từ bình này sang bình kia"""
        from_amt = 0
        to_amt = 0
        steps = []
        while from_amt != target and to_amt != target:
            if from_amt == 0:
                from_amt = from_cap  # Đổ đầy bình from
                steps.append(f"Đổ đầy bình {from_cap}-lít (from). Hiện tại: {from_amt} lít từ, {to_amt} lít đến")

            elif to_amt == to_cap:
                to_amt = 0  # Đổ hết nước bình to
                steps.append(f"Đổ hết bình {to_cap}-lít (to). Hiện tại: {from_amt} lít từ, {to_amt} lít đến")

            else:
                # Chuyển nước từ bình from sang bình to
                transfer_amt = min(from_amt, to_cap - to_amt)
                from_amt -= transfer_amt
                to_amt += transfer_amt
                steps.append(f"Chuyển {transfer_amt} lít từ bình {from_cap}-lít sang bình {to_cap}-lít.")
                steps.append(f"Hiện tại: {from_amt} lít từ, {to_amt} lít đến")

        return steps

    # Thực hiện đong nước
    steps_a_to_b = pour(a, b, x)
    steps_b_to_a = pour(b, a, x)

    # Hiển thị quá trình đong
    print(f"Các bước để đong {x} lít bằng bình {a}-lít và {b}-lít:")
    print("\nGiải pháp 1 (đong từ bình A sang bình B):")
    for step in steps_a_to_b:
        print(step)

    print("\nGiải pháp 2 (đong từ bình B sang bình A):")
    for step in steps_b_to_a:
        print(step)

# Ví dụ: đong 6 lít bằng bình 9 lít và 4 lít
waterMeasure(9, 4, 6)
