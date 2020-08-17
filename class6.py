#bonus question to print * in the format shown, where width of a tree's trunk is 3* n in the middle.also,height is 4* constant . 
# the base is 2* in height n width is maximum width of tree.
 
n=int(input("enter :"))
a=[]
for _ in range(1,n+1):
  print(" "*(n-_)+"*"*(2*_-1))
print(" "*(n-2)+"***")
print(" "*(n-2)+"***")
print(" "*(n-2)+"***")
print(" "*(n-2)+"***")
print("*"*(2*n-1))
print("*"*(2*n-1))


