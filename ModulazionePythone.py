import numpy as np
import matplotlib.pyplot as plt
Ampiezza=20
t1=123
t2=223
x1 = np.linspace(0.0,2.0*np.pi,t1)
x2 = np.linspace(0.0,2.0*np.pi,t1)
Vp1=Ampiezza*np.sin(x1)
Vp2=Ampiezza*np.cos(x2)
fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(x1, Vp1,marker = ".", color = 'green')
ax.plot(x2, Vp2,marker = ".", color = 'blue')
ax.set_xlabel('Time second')
ax.set_ylabel('Vp')
ax.set_title('Elettronica modulazione di ampiezza')
