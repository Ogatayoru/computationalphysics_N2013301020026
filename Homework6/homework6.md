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

再考虑重力的修正，由于随着高度的变化，重力加速度g并不是一个恒定不变的量，随高度的增加g会变小，具体关系如下







[程序代码](https://github.com/rwh457/computationalphysics_N2013301020026/blob/master/Homework6/cannon.py)


