#第五次作业
##摘要
这个程序利用Euler方法近似计算了两种不同（可能相同）的粒子的衰变问题，这两种粒子的衰变并不是独立无关的，而是一种粒子的衰变受另一种粒子的影响，
这种影响可以通过一个方程表现出来。这个程序通过对方程的解的近似可以绘出两种粒子的粒子数-时间关系。
##正文
首先，设A，B两种粒子的粒子数为<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?N_A">、
<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?N_B">，
两种粒子的时间常数为\tau_A、\tau_B。那么这四个量满足方程

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?%5Cfrac%7BdN_A%7D%7Bdt%7D%3D-%5Cfrac%7BN_A%7D%7B%5Ctau_A%7D">

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?%5Cfrac%7BdN_A%7D%7Bdt%7D%3D%5Cfrac%7BN_A%7D%7B%5Ctau_A%7D-%5Cfrac%7BN_B%7D%7B%5Ctau_B%7D">

从第二个方程就可以看出B粒子的衰变受到了A粒子的影响，不过第一个方程也说明了A粒子的衰变并不受到B粒子的影响。对于A粒子，与处理一种粒子衰变的情况相同，由泰勒展开有

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?N_A%28%5CDelta%20t%29%3DN_A%280%29&amp;plus;%5Cfrac%7BdN_A%7D%7Bdt%7D%5CDelta%20t&amp;plus;%5Cfrac%7B1%7D%7B2%7D%5Cfrac%7Bd%5E2%20N_A%7D%7Bdt%5E2%7D%28%5CDelta%20t%29%5E2&amp;plus;%5Ccdots">

舍弃二阶及以上的无穷小项可得到

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?N_A%28%5CDelta%20t%29%3DN_A%280%29&amp;plus;%5Cfrac%7BdN_A%7D%7Bdt%7D%5CDelta%20t">

所以同样可以得到

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?N_A%28t&amp;plus;%5CDelta%20t%29%3DN_A%28t%29&amp;plus;%5Cfrac%7BdN_A%7D%7Bdt%7D%5CDelta%20t">

与最开始的第一个方程联立可以得到

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?N_A%28t&amp;plus;%5CDelta%20t%29%3DN_A%28t%29-%5Cfrac%7BN_A%28t%29%7D%7B%5Ctau_A%7D%5CDelta%20t">

对于粒子B，仿照粒子A的做法用泰勒展开，然后略去高阶无穷小项，同样可以得到

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?N_A%28t&amp;plus;%5CDelta%20t%29%3DN_B%28t%29&amp;plus;%5Cfrac%7BdN_B%7D%7Bdt%7D%5CDelta%20t">

再与最开始的第二个方程联立有关系式

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?N_B%28t&amp;plus;%5CDelta%20t%29%3DN_B%28t%29&amp;plus;%5Cfrac%7BN_A%28t%29%7D%7B%5Ctau_A%7D%5CDelta%20t-%5Cfrac%7BN_B%28t%29%7D%7B%5Ctau_B%7D%5CDelta%20t">

利用两个递推式，设定初始d条件后通过程序可以计算出一系列时刻A、B两种粒子的粒子数，将这些数据绘在粒子数-时间图上，则可以得到散点图，将散点拟
合就可以得到A、B两种粒子衰变的曲线图。在绘图时，给图像添加了网格和标题，由与粒子数不带单位，所以只给x轴加上了坐标轴标签。

程序代码的链接为：[程序代码](https://github.com/rwh457/computationalphysics_N2013301020026/blob/master/Homework5/decay.py)
##结论
这个程序解决了一个两粒子间衰变存在影响的一类简单问题，大致模拟出了两种粒子衰变的趋势，并且能从图像上定性推测一下两种粒子的相关关系，可以观
察A粒子对B粒子的影响随A粒子衰变的变化。





