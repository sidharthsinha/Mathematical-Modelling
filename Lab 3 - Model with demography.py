#Model with demography

import numpy as np
import matplotlib.pyplot as plt

h = 0.01 #Step Size
S = [2e3] #Susceptible
I = [3e2] #Infected
R = [0] #Recovered
time = [0] #Initial Time
maxtime = float(50) #Maximum Time till observation

#Constants
a = 0.1
b = 0.05
r = 0.0003

for t in range(1, int(maxtime/h) + 1):
    y = S[t-1] + h*( b + (-1*r*I[t-1]*S[t-1])  - b*S[t-1] )
    S.append(y)
    x = I[t-1] + h*( r*I[t-1]*S[t-1] - a*I[t-1] )
    I.append(x)
    z = R[t-1] + h*( a*I[t-1] - b*R[t-1] )
    R.append(z)
    time.append(t*h)

plt.figure("Figure 1")
plt.xlabel("Time")
plt.ylabel("Suceptible Population")
plt.plot(time, S)

plt.xlabel("Time")
plt.ylabel("Infected Population")
plt.plot(time, I)

plt.xlabel("Time")
plt.ylabel("Recovered Population")
plt.plot(time, R)

plt.xlabel("Time")
plt.ylabel("Population")
plt.plot(time, np.array(S) +np.array(I) +np.array(R))

plt.figure("Figure 2")
plt.xlabel("Susceptible Population")
plt.ylabel("Infected Population")
plt.plot(S, I)

plt.show()
