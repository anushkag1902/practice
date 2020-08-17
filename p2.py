import time
start_time=time.time()

t=int(input())
for a in range(t):
    n=int(input())
    z=[int(c) for c in input().split()]
    for d in z:
        if (z.count(d)%2!=0):
            k=d
    print(k)

print(time.time()-start_time)