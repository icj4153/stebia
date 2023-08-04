
import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = input().split()

n = int(n)
k = str(k)
padding = '0'
len = 2

cnt = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            h = str(h).rjust(len,padding)
            m = str(m).rjust(len,padding)
            s = str(s).rjust(len,padding)
            st = h + m + s
            if st.find(k) != -1:
                cnt += 1

print(cnt)