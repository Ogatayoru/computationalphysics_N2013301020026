from pylab import plt

from mpl_toolkits.mplot3d import Axes3D

x=[]

y=[]

z=[]

t=[]

dt=0.01

T=50

x.append(float(raw_input('Enter the initial value of x:')))

y.append(float(raw_input('Enter the initial value of y:')))

z.append(float(raw_input('Enter the initial value of z:')))

dt=float(raw_input('Enter the time step:'))

T=float(raw_input('Enter the total time:'))

r=float(raw_input('Enter the value of r:'))

n=int(T/dt)

for i in range(1,n+1):
    
temp1=x[-1]+0.5*36*(y[-1]-x[-1])*dt
    
temp2=y[-1]+0.5*(-x[-1]*z[-1]+r*y[-1])*dt
    
temp3=z[-1]+0.5*(x[-1]*y[-1]-3*z[-1])*dt
    
temp4=t[-1]+0.5*dt
    
x.append(x[-1]+36*(temp2-temp1)*dt)
    
y.append(y[-1]+(-temp1*temp3+r*temp2)*dt)
    
z.append(z[-1]+(temp1*temp2-3*temp3)*dt)
    
t.append(t[-1]+dt)



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x,y,z)

plt.title('Phase space plot of Lu system with a=3,b=36,c=20')

ax.set_xlabel("x")  

ax.set_ylabel("y")  

ax.set_zlabel("z")  

plt.show()
