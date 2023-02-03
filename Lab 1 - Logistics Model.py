#LOGISTICS MODEL

import numpy as np
import matplotlib.pyplot as plt

h = 0.01 #Step Size
N = [3e5] #Initial Population
time = [0] #Initial Time
maxtime = float(100) #Maximum Time till observation
r = 0.1 #Constant
k = 1e4 #Constant

for t in range(1, int(maxtime/h) + 1):
    y = N[t-1] + h*r*N[t-1]*(1-(N[t-1]/k))
    N.append(y)
    time.append(t*h)

plt.figure("Figure 2")
plt.xlabel("Time")
plt.ylabel("Population")
plt.plot(time, N)

plt.show()