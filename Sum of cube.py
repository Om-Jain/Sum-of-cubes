def sum_of_cubes(M, N):
    if M > N:
        return 0
    
    sum_of_cubes = 0
    for num in range(M, N + 1):
        sum_of_cubes += num ** 3
    
    return sum_of_cubes

M = int(input("Enter the value of M: "))
N = int(input("Enter the value of N: "))

result = sum_of_cubes(M, N)

if result == 0:
    print("0")
else:
    print(result)