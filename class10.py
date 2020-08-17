#give an array of integers ,find the sum of its elements. for ex if an array ar=[1,2,3] , 1+2+3=6
#print the sum of the array's elements as a single integer :- 
# input   :- 6
#           1 2 3 4 10 11                                       outout :-31

n=int(input())
data=input().split(" ")
sum=0
for i in data:
    sum=sum+int(i)
print(sum)