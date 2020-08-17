import time
start_time=time.time()

n=int(input())
a=pow(7,n)
rq=a//10
qu=a%10
print(rq+qu)

print(time.time()-start_time)