#print the triangle of odd no of series :- if n=3     output=
#[1]
#[1, 3]
#[1, 3, 5]

n=int(input())
list_data=[]
for a in range(0,n):
    list_data.append(2*a+1)
    print(list_data)