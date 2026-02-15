
n=10
for i in range(n) :
    for j in range(n-i):
        
        print(' ', end="" )
    for k in range(2 * i + 1):
        print(j , end='')
            
    print()
        # Questo "if" garantisce che lavori solo sul triangolo inferiore
        # ... esegui eliminazione ...
