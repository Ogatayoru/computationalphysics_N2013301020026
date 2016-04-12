#第六次作业
##摘要
这个程序用来计算加农炮在空中飞行的轨迹，程序中把发射点设在了原点，考虑了风阻和重力的影响。对于重力，加入了飞行高度对重力大小的影响；而对于风阻，加入了空气密度对风阻大小的影响。
##正文
首先，沿海平面朝加农炮飞行方向为x轴方向，垂直海平面向上为y轴方向，将加农炮的运动沿x轴和y轴分解，设加农炮初始速度与x轴夹角为$\theta$，设加农炮质量为m，在两个方向上列牛顿运动方程可以得到
$m\frac{dv_x}{dt}=F_{drag,x}=F_{drag}cos{\theta}$
$m\frac{dv_y}{dt}=F_{drag,y}-mg=-F_{drag}sin{\theta}-mg$
分解风阻可以知道
$F_{drag,x}=F_{drag}cos{\theta}=F_{drag}(v_x/v)$
$F_{drag,y}=F_{drag}sin{\theta}=F_{drag}(v_y/v)$
而对于风阻有公式
$F_{drag}=-B_2v^2$
式中$B_2$为一个系数，这个系数的大小考虑为在海平面处的情况。联立上面三式可得到
$F_{drag,x}=-B_2vv_x$
$F_{drag,y}=-B_2vv_y$
把这两个式子代入开始列出的牛顿运动方程有
$m\frac{dv_x}{dt}=-B_2vv_x$
$m\frac{dv_y}{dt}=-B_2vv_y-mg$
将$v_x(t)$和$v_y(t)$进行泰勒展开，然后舍弃高阶无穷小项可得到关系式
$v_x(t+\Delta t)=v_x(t)+\frac{dv_x}{dt}\Delta t$
$v_y(t+\Delta t)=v_y(t)+\frac{dv_y}{dt}\Delta t$
所以联立以上四式可得得出
$v_x(t+\Delta t)=v_x(t)-\frac{B_2vv_x}{m}\Delta t$
$v_y(t+\Delta t)=v_y(t)-\frac{B_2vv_y}{dt}\Delta t-g\Delta t$
可以把上面两个递推式子写为
$v_{x,i+1}=v_{x,i}-\frac{B_2vv_{x,i}}{m}\Delta t$
$v_{y,i+1}=v_{y,i}-\frac{B_2vv_{y,i}}{dt}\Delta t-g\Delta t$
再考虑重力的修正，由于随着高度的变化，重力加速度g并不是一个恒定不变的量，随高度的增加g会变小，具体关系如下















