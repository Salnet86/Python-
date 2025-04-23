'''
n =5

for i in range(n,-1,-1):

    for j in range(n - i):
        print(j,end='')



    print()


'''

'''
n =5

for i in range(n):

    for j in range(n):
        if j>=i:
            print("*",end='')
        else:
            print(" ",end='')



    print()

'''


n =5

for i in range(n):

    for j in range(n):
        if i<=j:
            print(j,end='')
        else:
            print(" ",end='')



    print()




