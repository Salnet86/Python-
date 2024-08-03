import psutil
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
while True:
    cpu=psutil.cpu_percent(interval=1)
    memoria=psutil.virtual_memory()
    storage=psutil.disk_usage('/')
    print(f'CPU {cpu}% : STORAGE  {storage}% : MEMORIA {memoria}')
   # print('CPU ',cpu,'%','STORAGE ',storage,'%','MEORIA ',memoria,'%')
    time.sleep(1)
'''


while True:
    df=pd.DataFrame([[f"{psutil.cpu_percent(interval=1)}",f"{psutil.disk_usage('/').percent}%",f"{psutil.virtual_memory().percent}%"]],columns=['CPU','DISK','MEMORIA'])
    print(df)
    time.sleep(1)
 
