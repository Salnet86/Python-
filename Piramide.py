BACKGROUND_GREEN = '\033[42m'
BLACK = '\033[30m'


piramide='''
         ---------------------------
         |     Piramide Egiziana   |
         ---------------------------
'''

print(BACKGROUND_GREEN,BLACK, piramide,end="")

n =20
for i in range(n):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*",end="")
         
         
       
    print()
