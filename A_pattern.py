'''n=int(input('Enter the number '))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j+1,end="")
    print()'''
#odd
'''num=int(input('Enter the number'))
k=1
for i in range(1,num+1):
    for j in range(1,k+1):
        print(j,end="")
    k=k+2
    print()'''
#3
n=int(input('Enter the number'))
for i in range(0,n):
    for j in range(0,n-i-1):
        print("",end='')
    for j in range(0,i+1):
        print("*",end='')
    print()        
