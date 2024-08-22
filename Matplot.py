#Scatter python matplotlib


import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()



#Linea 
import matplotlib.pyplot as plt
import numpy as np

points = np.array([3, 8, 1, 10])

plt.plot(points, marker = 'o')
plt.show()



point = np.array([3, 8, 1, 10])

plt.plot(point, marker = 'o', ms = 20)
plt.show()


#Grafico con griglia esempio sports calorie averange pulse

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'x')

plt.show()

#Histograms

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 

#Torta

y = np.array([35, 25, 25, 15])
mylabels = ["mele", "pere", "fragole", "meloni"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 

#Bar
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()






