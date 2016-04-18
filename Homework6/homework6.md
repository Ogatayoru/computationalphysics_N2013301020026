#第六次作业
##摘要
这个程序用来计算加农炮在空中飞行的轨迹，程序中把发射点设在了原点，考虑了风阻和重力的影响。对于重力，加入了飞行高度对重力大小的影响；而对于风阻，加入了空气密度对风阻大小的影响。
##正文
首先，沿海平面朝加农炮飞行方向为x轴方向，垂直海平面向上为y轴方向，将加农炮的运动沿x轴和y轴分解，设加农炮初始速度与x轴夹角为$\theta$，设加农炮质量为m，在两个方向上列牛顿运动方程可以得到

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?m%5Cfrac%7Bdv_x%7D%7Bdt%7D%3DF_%7Bdrag%2Cx%7D%3DF_%7Bdrag%7Dcos%7B%5Ctheta%7D">

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?m%5Cfrac%7Bdv_y%7D%7Bdt%7D%3DF_%7Bdrag%2Cy%7D-mg%3D-F_%7Bdrag%7Dsin%7B%5Ctheta%7D-mg">

分解风阻可以知道

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?F_%7Bdrag%2Cx%7D%3DF_%7Bdrag%7Dcos%7B%5Ctheta%7D%3DF_%7Bdrag%7D%28v_x/v%29">

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?F_%7Bdrag%2Cy%7D%3DF_%7Bdrag%7Dsin%7B%5Ctheta%7D%3DF_%7Bdrag%7D%28v_y/v%29">

而对于风阻有公式

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%3D-B_2v%5E2">

式中<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?B_2">为一个系数，这个系数的大小考虑为在海平面处的情况。联立上面三式可得到

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?F_%7Bdrag%2Cx%7D%3D-B_2vv_x">

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?F_%7Bdrag%2Cy%7D%3D-B_2vv_y">

把这两个式子代入开始列出的牛顿运动方程有

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?m%5Cfrac%7Bdv_x%7D%7Bdt%7D%3D-B_2vv_x">

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?m%5Cfrac%7Bdv_y%7D%7Bdt%7D%3D-B_2vv_y-mg">

将$v_x(t)$和$v_y(t)$进行泰勒展开，然后舍弃高阶无穷小项可得到关系式

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?v_x%28t&amp;plus;%5CDelta%20t%29%3Dv_x%28t%29&amp;plus;%5Cfrac%7Bdv_x%7D%7Bdt%7D%5CDelta%20t">

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?v_y%28t&amp;plus;%5CDelta%20t%29%3Dv_y%28t%29&amp;plus;%5Cfrac%7Bdv_y%7D%7Bdt%7D%5CDelta%20t">

所以联立以上四式可得得出

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?v_x%28t&amp;plus;%5CDelta%20t%29%3Dv_x%28t%29-%5Cfrac%7BB_2vv_x%7D%7Bm%7D%5CDelta%20t">

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?v_y%28t&amp;plus;%5CDelta%20t%29%3Dv_y%28t%29-%5Cfrac%7BB_2vv_y%7D%7Bdt%7D%5CDelta%20t-g%5CDelta%20t">

可以把上面两个递推式子写为

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?v_%7Bx%2Ci&amp;plus;1%7D%3Dv_%7Bx%2Ci%7D-%5Cfrac%7BB_2vv_%7Bx%2Ci%7D%7D%7Bm%7D%5CDelta%20t">

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?v_%7By%2Ci&amp;plus;1%7D%3Dv_%7By%2Ci%7D-%5Cfrac%7BB_2vv_%7By%2Ci%7D%7D%7Bdt%7D%5CDelta%20t-g%5CDelta%20t">

再考虑重力的修正，由于随着高度的变化，重力加速度g并不是一个恒定不变的量，随高度的增加g会变小，由万有引力定律可知

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?g%3DG%5Cfrac%7BM_%7Bearth%7D%7D%7B%28R_%7Bearth%7D&amp;plus;h%29%5E2%7D">

设海平面处重力加速度为g_0,取地球半径为6400km，那么任意高度h处的重力加速度为

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?g_h%3D%5Cfrac%7B6400000%5E2%7D%7B%286400000&amp;plus;h%29%5E2%7Dg_0">

考虑完重力的修正后，再考虑空气密度随高度的变化，空气密度的变化实际影响的是风阻的大小，取空气密度变化的公式为

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?%5Crho%3D%5Crho_0%281-%5Cfrac%7Bah%7D%7BT_0%7D%29%5E%5Calpha">

式中，<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?%5Crho_0">为海平面处的空气密度，<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?T_0">为海平面处的温度，单位是K，<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?a%5Capprox6.5%5Ctimes10%5E%7B-3%7D%2C%5Calpha%5Capprox2.5">

所以原先的风阻前要加上因子<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?%281-%5Cfrac%7Bah%7D%7BT_0%7D%29%5E%5Calpha">，所以关于速度的递推式变为

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?v_%7Bx%2Ci&amp;plus;1%7D%3Dv_%7Bx%2Ci%7D-%281-%5Cfrac%7Bay_i%7D%7BT_0%7D%29%5E%7B%5Calpha%7D%5Cfrac%7BB_2vv_%7Bx%2Ci%7D%7D%7Bm%7D%5CDelta%20t">

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?v_%7By%2Ci&amp;plus;1%7D%3Dv_%7By%2Ci%7D-%5Cfrac%7B6400000%5E2%7D%7B%286400000&amp;plus;y_i%29%5E2%7Dg_0%5CDelta%20t-%281-%5Cfrac%7Bay_i%7D%7BT_0%7D%29%5E%7B%5Calpha%7D%5Cfrac%7BbB_2vv_%7By%2Ci%7D%7D%7Bm%7D%5CDelta t">

而关于位移的递推关系可以很容易得到，如下所示

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?x_%7Bi&amp;plus;1%7D%3Dx_i&amp;plus;v_%7Bx%2Ci%7D%5CDelta%20t">

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?y_%7Bi&amp;plus;1%7D%3Dy_i&amp;plus;v_%7By%2Ci%7D%5CDelta%20t">

利用上面四个递推式可以绘出d散点，然后把散点拟合就可以得到加农炮的轨迹曲线。

[程序代码](https://github.com/rwh457/computationalphysics_N2013301020026/blob/master/Homework6/cannon.py)

运行程序，设定初始速度为700m/s，发射角为45°，<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?%5Cfrac%7BB_2%7D%7Bm%7D%3D4%5Ctimes10%5E%7B-5%7Dm%5E%7B-1%7D">,时间间隔为0.1s，得到图像如下

[图像链接](https://github.com/rwh457/computationalphysics_N2013301020026/blob/master/Homework6/cannon.png)

##结论
通过比较修正前与修正后的曲线，发现重力加速度随高度的变化对曲线的影响较小，主要是由于加农炮的初始速度大小的限制，使得加农炮飞行的高度不会太高，从而重力加速度变化的影响不是很明显，而空气密度的变化对轨迹的影响比较明显。

