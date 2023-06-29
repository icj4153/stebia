import sys

N = int(sys.stdin.readline())

for _ in range(N):
    cmd = sys.stdin.readline()
    left_cnt = 0
    right_cnt = 0
    for i in range(len(cmd)):