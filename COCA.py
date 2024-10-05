# Nam là một kẻ nghiện cô ca, rất khó để cậu ấy uống đủ số cô ca cậu cần, điều đáng buồn là Nam lại 
# không có nhiều tiền, nhiều khi cậu ta phải nhặt thêm vỏ lon bán đi để có tiền mua cô ca.Một ngày nọ,
#  Nam quyết định dùng số vỏ lon đang có để mua nhiều lon cô ca nhất có thể. Thậm chí những lon cô ca
#  mới mua sau khi uống hết cũng được bán đi để mua lon mới.
# Hãy viết chương trình tính xem nam có thể uống được tối đa bao nhiêu lon cô ca
# INPUT: Nhập 3 số nguyên dương a,b,c lần lượt là số vỏ lon của Nam đang có, 
# số vỏ lon của Nam kiếm thêm và số vỏ lon cần bán để có một lon cô ca mới.
# OUTPUT: số lượng tối đa các lon co-ca mà Nam có thể uống.
# vd1:9 0 3   => kết quả: 4; 
# vd2: 5 5 2  ->kq: 9;  
# vd3: 6 1 2 ->kq: 6;



def max_coca_drinks(a, b, c):
    total_drinks = a + b  # Tổng số vỏ lon mà Nam có ban đầu
    drinks = 0  # Số lon Nam có thể uống
    
    while total_drinks >= c:  # Khi đủ vỏ lon để đổi lấy 1 lon mới
        new_drinks = total_drinks // c  # Số lon mới có thể đổi được
        drinks += new_drinks  # Tăng số lon đã uống
        total_drinks = total_drinks % c + new_drinks  # Cập nhật số vỏ lon còn lại
    
    return drinks

# Nhập các giá trị a, b, c
a, b, c = map(int, input("Nhập a, b, c: ").split())

# Gọi hàm và in kết quả
print("Số lượng tối đa các lon cô-ca mà Nam có thể uống là:", max_coca_drinks(a, b, c))
