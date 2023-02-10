#Kermack McKendrick Model

import numpy as np
import matplotlib.pyplot as plt

h = 0.01 #Step Size
S = [2e3] #Susceptible
I = [3e2] #Infected
R = [0] #Recovered
time = [0] #Initial Time
maxtime = float(50) #Maximum Time till observation

#Constants
a = 0.2 
r = 0.0005 

for t in range(1, int(maxtime/h) + 1):
    y = S[t-1] + h*( -1*r*I[t-1]*S[t-1]  )
    S.append(y)
    x = I[t-1] + h*( r*I[t-1]*S[t-1] - a*I[t-1] )
    I.append(x)
    z = R[t-1] + h*( a*I[t-1] )
    R.append(z)
    time.append(t*h)

plt.figure("Figure 1")
plt.xlabel("Time")
plt.ylabel("Suceptible Population")
plt.plot(time, S)

plt.figure("Figure 2")
plt.xlabel("Time")
plt.ylabel("Infected Population")
plt.plot(time, I)

plt.figure("Figure 3")
plt.xlabel("Time")
plt.ylabel("Recovered Population")
plt.plot(time, R)

plt.figure("Figure 4")
plt.xlabel("Susceptible Population")
plt.ylabel("Infected Population")
plt.plot(S, I)

plt.show()
