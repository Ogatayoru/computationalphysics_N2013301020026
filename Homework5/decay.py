from pylab import *
import pickle
N_A=[]
N_B=[]
t=[0]
N_A.append(float(raw_input('Enter the initial number of the type A nuclei:')))
N_B.append(float(raw_input('Enter the initial number of the type B nuclei:')))
tau_A=float(raw_input('Enter the time constant of the type A nuclei:'))
tau_B=float(raw_input('Enter the time constant of the type B nuclei:'))
dt=float(raw_input('Enter the time step:'))
T=float(raw_input('Enter the total time:'))
n=int(T/dt)
for i in range(0,n+1):
    tmp1=N_A[i]-(N_A[i]*dt)/tau_A
    tmp2=N_B[i]+(N_A[i]*dt)/tau_A-(N_B[i]*dt)/tau_B
    N_A.append(tmp1)
    N_B.append(tmp2)
    t.append(i*dt)
    print t[-1],N_A[-1],N_B[-1]

ax = axes([0.025,0.025,0.95,0.95])

ax.yaxis.set_major_locator(MultipleLocator(max(N_A[0],N_B[0])*0.1))
ax.yaxis.set_minor_locator(MultipleLocator(max(N_A[0],N_B[0])*0.01))
ax.xaxis.set_major_locator(MultipleLocator(t[-1]*0.1))
ax.xaxis.set_minor_locator(MultipleLocator(t[-1]*0.01))
ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')

ax=gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',min(N_A[-1],N_B[-1])))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))


plot(t,N_A,'-',color='red',linewidth=2.5,label='N_A')
plot(t,N_B,'-',color='blue',linewidth=2.5,label='N_B')
legend(loc='upper right')
title('Decay involving two types of nuclei')

xmajorLocator=MultipleLocator(t[-1]*0.1)
xmajorFormatter=FormatStrFormatter('%5.1f')
xminorLocator=MultipleLocator(t[-1]*0.01)

ymajorLocator=MultipleLocator(max(N_A[0],N_B[0])*0.1)
ymajorFormatter=FormatStrFormatter('%1.1f')
yminorLocator=MultipleLocator(max(N_A[0],N_B[0])*0.01)

ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)

ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)

ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.grid(True, which='major')
ax.yaxis.grid(True, which='minor')

xlabel('Time(s)')

show()
