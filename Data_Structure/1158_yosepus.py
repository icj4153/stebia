import queue, sys

n, k = tuple(map(int,sys.stdin.readline().split()))

in_queue = queue.Queue()
result = queue.Queue()

for i in range(n):
    in_queue.put(i+1)

while(in_queue.qsize() >= 3):
    for i in range(k-1):
        in_queue.put(in_queue.get())
    result.put(in_queue.get())

result.put(in_queue.get())
result.put(in_queue.get())


print("<",end="")
for i in range(n):
    if i == n-1:
        print(result.get(),end="")
    else:
        print(result.get(),end=", ")

print(">",end="")