
# hình vuông xoáy giảm dần từ N*N -> 1
# OUTPUT: 9 8 7
#         2 1 6
#         3 4 5


def main():
    N = 5
    for i in range(N):
        line = ""
        for j in range(N):
            x0 = min(i, N - i - 1)
            y0 = min(j, N - j - 1)
            t = min(x0, y0)

            value = (N - 2 * t) 
            value = value * value
            
            d = N - 2 * t  # d -> distance
            
            # duyệt các vị trí -> hoàn thiện tam giác trên và tam giác ngược
            if x0 == t:
                if i < N - i - 1:
                    value = value - j + t
                else:
                    value = value - 2 * d + 3 - N + j + t
            else:
                if j < N - j - 1:
                    value = value - 3 * d + 3 - N + i + 1 + t
                else:
                    value = value - d + 1 - i + t

            #  định dạng các số căn chỉnh đều đặn
            line += f"{value:3d}"
        
        print(line)
main()