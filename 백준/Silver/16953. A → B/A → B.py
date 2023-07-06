A, B = map(int, input().split())
cnt = 1
while B != A:
    if B < A:
        cnt = -1
        break;
    if B % 10 == 1:
        B = B // 10
        cnt += 1
    else:
        # B가 홀수이면 만들수가 없다.
        if B % 2 == 1:
            cnt = -1
            break
        B //= 2
        cnt += 1

print(cnt)