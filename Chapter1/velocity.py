from pylab import *
import pickle
v=[]
t=[0]
v.append(float(raw_input('Enter the initial velocity:')))
time_step=float(raw_input('Enter the time step:'))
T=float(raw_input('Enter the total time:'))
n=int(T/time_step)
for i in range(1,n+1):
    tmp=v[i-1]+9.8*time_step
    v.append(tmp)
    t.append(i*time_step)
    print t[-1],v[-1]

ax = axes([0.025,0.025,0.95,0.95])

ax.yaxis.set_major_locator(MultipleLocator(v[-1]*0.1))
ax.yaxis.set_minor_locator(MultipleLocator(v[-1]*0.01))
ax.xaxis.set_major_locator(MultipleLocator(t[-1]*0.1))
ax.xaxis.set_minor_locator(MultipleLocator(t[-1]*0.01))
ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
ax.set_xticklabels([])
ax.set_yticklabels([])

ax=gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plot(t,v,'-',color='blue',linewidth=2.5,label='v-t curve')
legend(loc='upper left')
title("freely falling object near Earth's surface")

scatter([0,],[v[0],],50,color='red')
scatter([t[-1],],[v[-1],],50,color='red')

plot([t[0],t[0]],[0,v[0]],linestyle='--',color='red')
plot([t[-1],t[-1]],[0,v[-1]],linestyle='--',color='red')

xlabel('Times(s)')
ylabel('Velocity(m/s)')

annotate('initial velocity',xy=(0,v[0]),xycoords='data',xytext=(-100,+50),textcoords='offset points',fontsize=16,arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"),color='green')
annotate('final velocity',xy=(t[-1],v[-1]),xycoords='data',xytext=(0,+40),textcoords='offset points',fontsize=16,arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"),color='green')

xmajorLocator=MultipleLocator(t[-1]*0.1)
xmajorFormatter=FormatStrFormatter('%5.1f')
xminorLocator=MultipleLocator(t[-1]*0.01)

ymajorLocator=MultipleLocator(v[-1]*0.1)
ymajorFormatter=FormatStrFormatter('%1.1f')
yminorLocator=MultipleLocator(v[-1]*0.01)

ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)

ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)

ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.grid(True, which='major')
ax.yaxis.grid(True, which='minor')

show()

