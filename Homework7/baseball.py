from visual import *
import math
x=[]
y=[]
z=[]
v_x=[]
v_y=[]
v_z=[]
k_1=[]
y.append(float(raw_input('Please enter the ininial hight:')))
v=float(raw_input('Please enter the initial speed:'))
theta=float(raw_input('Please enter the angle:'))
omega=float(raw_input('Please enter the angular velocity:'))
k_1.append(float(0.0039+0.0058/(1+2.7183**((v-35)/5))))
k_2=float(raw_input('Please enter the value of S/m:'))
dt=float(raw_input('Please enter the time step:'))
x.append(0)
z.append(0)
v_x.append(v*math.cos(theta*math.pi/180))
v_y.append(v*math.sin(theta*math.pi/180))
v_z.append(0)
n=0
while True:
     x.append(x[-1]+v_x[-1]*dt)
     y.append(y[-1]+v_y[-1]*dt)
     z.append(z[-1]+v_z[-1]*dt)
     v_x.append(v_x[-1]-k_1[-1]*((v_x[-1]**2+v_y[-1]**2+v_z[-1]**2)**0.5)*v_x[-1]*dt)
     v_y.append(v_y[-1]-9.8*dt-k_1[-1]*((v_x[-1]**2+v_y[-1]**2+v_z[-1]**2)**0.5)*v_y[-1]*dt)
     v_z.append(v_z[-1]+k_2*v_x[-1]*omega-k_1[-1]*((v_x[-1]**2+v_y[-1]**2+v_z[-1]**2)**0.5)*v_z[-1]*dt)
     k_1.append(0.0039+0.0058/(1+2.7183**((((v_x[-1]**2+v_y[-1]**2)**0.5)-35)/5)))
     if y[-1]<0:
        break
     print x[-1],y[-1],z[-1]
     n=n+1
for i in range(1,n+1):
    ball=sphere(pos=vector(x[i],y[i],z[i]),radius=x[-1]/30,color=color.red)
greenbox=box(pos=vector(0.5*x[-1],0,0.5*z[-1]),size=(x[-1],0,abs(z[-1])),color=color.green)
ball=sphere(pos=vector(x[0],y[0],z[0]),radius=x[-1]/30,color=color.blue)
