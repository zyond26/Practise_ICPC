def generate_binary_strings(n):
    result = []
    
    for i in range(2 ** n):
        result.append(f'{i:0{n}b}')
    
    return result

n = int(input())

binary_strings = generate_binary_strings(n)
for binary_string in binary_strings:
    print(binary_string)
