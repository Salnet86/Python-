import time


i=1
Dong=0
start=""

while i==1:
    Dong=Dong+1
    start='{:02d}'.format(Dong)
    print(start, end='\r')
    #print(f'{Dong:02}', end=' \r')
    time.sleep(1)
   
    if Dong==10:
        print('Stop Dong')
        i=0

