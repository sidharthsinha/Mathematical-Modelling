#Alternate Prey Predator Model

import numpy as np
import matplotlib.pyplot as plt

h = 0.01 #Step Size
N = [5] #Initial Population of Prey
P = [2] #Initial Population of Predator
time = [0] #Initial Time
maxtime = float(200) #Maximum Time till observation

#Constants
a = 0.1 # Natural Birth rate of Predator
b = 0.2 # Natural Birth rate of Prey

for t in range(1, int(maxtime/h) + 1):
    y = N[t-1] + h*( a*N[t-1] - b*P[t-1] -N[t-1]*(N[t-1]**2 + P[t-1]**2)  )
    N.append(y)
    x = P[t-1] + h*( b*N[t-1] + a*P[t-1] - P[t-1]*( N[t-1]**2 + P[t-1]**2 ) )
    P.append(x)
    time.append(t*h)

plt.figure("Figure 5")
plt.xlabel("Time")
plt.ylabel("Population of Prey")
plt.plot(time, N)

plt.plot(time, P)

plt.show()