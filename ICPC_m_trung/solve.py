def find_kth_digit(N, K):
    num_arr = [i for i in range(N - 1, 0, -1)]
    num_arr.append(N)

    print(num_arr)
    
    if K > len(num_arr):
        return -1
    else:
        return num_arr[K - 1]

N,K = map(int,input().split())
print(find_kth_digit(N, K))
