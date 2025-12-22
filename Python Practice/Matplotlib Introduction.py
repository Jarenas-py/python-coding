import numpy as np
import matplotlib.pyplot as plt

font1= {'family':'Lucida Console', 'color': 'green', 'fontsize': 30}
font2= {'family':'Lucida Console', 'color': 'green', 'size': 20}
font3= {'family':'Lucida Console', 'color': 'green', 'size': 10}

x1= np.array([0, 1, 5, 10])
y1= np.array([0, 10, 5, 7])

plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'o--b', ms= 10, mfc= 'k')

plt.title("Test 1", fontdict= font2)
plt.xlabel("Test 1 X", fontdict= font3)
plt.ylabel("Test 1 Y", fontdict= font3)
plt.grid()

x2= np.array([3, 4, 6, 9])
y2= np.array([3, 1, 8, 6])

plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'o--r', ms= 10, mfc= 'k')

plt.title("Test 2", fontdict= font2)
plt.xlabel("Test 2 X", fontdict= font3)
plt.ylabel("Test 2 Y", fontdict= font3)
plt.grid()

plt.suptitle("TESTING", fontdict= font1)
plt.show()