#Prey Predator Model

import numpy as np
import matplotlib.pyplot as plt

h = 0.01 #Step Size
N = [2] #Initial Population of Prey
P = [5] #Initial Population of Predator
time = [0] #Initial Time
maxtime = float(200) #Maximum Time till observation

#Constants
a1 = 0.1 # Natural Birth rate of Predator
a2 = 0.2 # Natural Death rate of Prey
gamma = 0.5 # Effect of prey on birth rate of predator
b = 0.1 # Death Rate of prey as a result of predator's presence
k = 100 # Natural Death Constant in Logistics Model

for t in range(1, int(maxtime/h) + 1):
    y = N[t-1] + h*( a1*N[t-1]*( 1-  N[t-1]/k -  b*P[t-1]  ) )
    N.append(y)
    x = P[t-1] + h*( -a2*P[t-1]*( 1-(gamma*N[t-1])) )
    P.append(x)
    time.append(t*h)

plt.figure("Figure 4")
plt.xlabel("Time")
plt.ylabel("Population of Prey")
plt.plot(time, N)

plt.plot(time, P)

plt.show()