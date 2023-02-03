#POPULATION GROWTH MODEL

import numpy as np
import matplotlib.pyplot as plt

lamb = 0.05 #Constant
h = 0.05 #Step Size 
N = [3e5] #Initial Population
time = [0] #Initital Time
maxtime = float(100.0) #Maximum Time till observation

for t in range(1, int(maxtime/h) + 1):
    y = N[t-1] + h*lamb*N[t-1]
    N.append(y)
    time.append(t*h)

plt.figure("Figure 1")
plt.xlabel("Time")
plt.ylabel("Population")
plt.plot(time, N)

plt.show()