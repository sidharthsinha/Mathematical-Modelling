#Pest Control Model
#Spruce Budworm Model

import numpy as np
import matplotlib.pyplot as plt

h = 0.001 #Step Size
N = [3e5] #Initial Population
time = [0] #Initial Time
A = 850
B = 1000
maxtime = float(100) #Maximum Time till observation
r = 0.1 #Constant
k = 200*N[0] #Constant

for t in range(1, int(maxtime/h) + 1):
    y = N[t-1] + h*(  r*N[t-1]*(1-(N[t-1]/k)) - (B*(N[t-1]**2))/(A**2+N[t-1]**2)  )
    N.append(y)
    time.append(t*h)

plt.figure("Figure 3")
plt.xlabel("Time")
plt.ylabel("Population")
plt.plot(time, N)

plt.show()
