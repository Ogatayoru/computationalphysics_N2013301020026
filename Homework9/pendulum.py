from pylab import *
import math
theta=[]
omega=[]
t=[]
F_D=float(raw_input('Please enter the initial amplitude of the driving force:'))
q=float(raw_input('Please enter the value of the parameter about damping:'))
theta.append(float(raw_input('Initial angel:')))
l=float(raw_input('Length of the line:'))
omega_D=float(raw_input('Value of the angular freguency of driving force:'))
T=float(raw_input('Total time:'))
dt=float(raw_input('Time step:'))
omega.append(0)
t.append(0)
n=int(T/dt)
for i in range(1,n+1):
    omega.append(omega[-1]-(9.8*math.sin(theta[-1])/l+q*omega[-1]-F_D*math.sin(omega_D*t[-1]))*dt)
    tmp=theta[-1]+omega[-1]*dt
    if abs(tmp)>math.pi:
        tmp=tmp-sign(tmp)*2*math.pi
    theta.append(tmp)
    t.append(t[-1]+dt)
    print t[-1],theta[-1],omega[-1]

plot(theta,omega,'-',color='blue')
show()


