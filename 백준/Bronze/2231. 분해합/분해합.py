import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

prod = 0

for i in range(N,-1,-1):
    res = 0
    arr =[]
    arr.append(i)
    # i가 0이 되면 반복 종료함.
    while(i > 0):
        arr.append(i%10)
        i = i // 10
    for elem in arr:
        res += elem;
    
    if res == N:
        prod = arr[0]

print(prod)