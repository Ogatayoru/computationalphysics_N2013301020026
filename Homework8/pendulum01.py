from pylab import *
import math
theta=[]
omega=[]
t=[]
theta.append(float(raw_input('Initial angel:')))
l=float(raw_input('Length of the line:'))
T=float(raw_input('Total time:'))
dt=float(raw_input('Time step:'))
omega.append(0)
t.append(0)
n=int(T/dt)
for i in range(1,n+1):
    omega.append(omega[-1]-9.8*math.sin(theta[-1])*dt/l)
    tmp=theta[-1]+omega[-1]*dt
    theta.append(tmp)
    t.append(t[-1]+dt)
    print t[-1],theta[-1],omega[-1]

plot(t,theta,'-',color='blue')
title('Simple Pendulum-Euler-Cromer method')
xlabel('time(s)')
ylabel('theta(radians)')
show()

