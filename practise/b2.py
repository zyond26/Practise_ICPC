
# input N=5
# OUTPUT :    5 5 5 5 5
#             5 3 3 3 5
#             5 3 1 3 5
#             5 3 3 3 5
#             5 5 5 5 5

# viết thuật toán vẽ tam giác 
def main():
    N = 4
    for i in range(N):
        for j in range(N):
          
            x0 = min(i, N - i - 1)
            y0 = min(j, N - j - 1)
            t = min(x0, y0)
            value = N - t * 2

            s0 = f"{value }  "
            print(s0, end="")
        print("")
    print("Ended")

if __name__ == "__main__":
    main()
 

