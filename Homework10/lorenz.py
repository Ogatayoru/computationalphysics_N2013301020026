from pylab import *
x=[]
y=[]
z=[]
t=[]
t.append(0)
x.append(float(raw_input('Enter the initial value of x:')))
y.append(float(raw_input('Enter the initial value of y:')))
z.append(float(raw_input('Enter the initial value of z:')))
dt=float(raw_input('Enter the time step:'))
T=float(raw_input('Enter the total time:'))
r=float(raw_input('Enter the value of r:'))
n=int(T/dt)
for i in range(1,n+1):
    temp1=x[-1]+0.5*10*(y[-1]-x[-1])*dt
    temp2=y[-1]+0.5*(-x[-1]*z[-1]+r*x[-1]-y[-1])*dt
    temp3=z[-1]+0.5*(x[-1]*y[-1]-8*z[-1]/3)*dt
    temp4=t[-1]+0.5*dt
    x.append(x[-1]+10*(temp2-temp1)*dt)
    y.append(y[-1]+(-temp1*temp3+r*temp1-temp2)*dt)
    z.append(z[-1]+(temp1*temp2-8*temp3/3)*dt)
    t.append(t[-1]+dt)

plot(t,z,'-',color='blue')
show()


