
STR='''
       CALCOLO  DI  FIBONACCI

'''



'''
print(STR)

out=''

b=0
a=1
i=0
c=0
while i<=10:
    c=a+b
    out=out + str(c).spilt(',')  
    a=b
    b=c
    i+=1
print(out)
'''



'''
INPUT=int(input('Inserisci un valore'))
print(STR)

out = ''

b = 0
a = 1
i = 0
c = 0
while i < INPUT:  
    out += str(c) + ','  
    c = a + b
    a = b
    b = c
    i += 1

out = out.rstrip(',') 
print(out)
'''

print(STR)


a=0
b=1
n=4
for i in range(n,-1,-1):
    c=a
    for j in range(n - i):
        print(c, end=" ")
        c=a+b
        a=b
        b=c
    print()

