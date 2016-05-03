#第七次作业
##摘要
 这个程序模拟了棒球的运动，考虑了阻力系数随棒球速度的变化，并且由于击出的棒球带有旋转，所以加入了马格努斯力对棒球运动轨迹的影响，最后通过Vpython作出了三维轨迹图。
##正文
 棒球的运动与加农炮类似，都是抛体运动，但由于初始条件有较大不同，导致在运动过程中我们要考虑的因素也有所不同。以球场竖向为x轴，横向为y轴，垂直于地面方向为z轴，认定棒球初速度方向在x-y平面内，将棒球的运动沿x轴和y轴分解，设棒球初始速度与x轴夹角为$\theta$，设棒球质量为m，在两个方向上列牛顿运动方程可以得到

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?m%5Cfrac%7Bdv_x%7D%7Bdt%7D%3DF_%7Bdrag%2Cx%7D%3DF_%7Bdrag%7Dcos%7B%5Ctheta%7D">

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?m%5Cfrac%7Bdv_y%7D%7Bdt%7D%3DF_%7Bdrag%2Cy%7D-mg%3D-F_%7Bdrag%7Dsin%7B%5Ctheta%7D-mg">

分解风阻可以知道

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?F_%7Bdrag%2Cx%7D%3DF_%7Bdrag%7Dcos%7B%5Ctheta%7D%3DF_%7Bdrag%7D%28v_x/v%29">

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?F_%7Bdrag%2Cy%7D%3DF_%7Bdrag%7Dsin%7B%5Ctheta%7D%3DF_%7Bdrag%7D%28v_y/v%29">

而对于风阻有公式

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%3D-B_2v%5E2">

式中<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?B_2">为一个系数，先考虑这个系数恒定不变的情况。联立上面三式可得到

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?F_%7Bdrag%2Cx%7D%3D-B_2vv_x">

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?F_%7Bdrag%2Cy%7D%3D-B_2vv_y">

把这两个式子代入开始列出的牛顿运动方程有

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?m%5Cfrac%7Bdv_x%7D%7Bdt%7D%3D-B_2vv_x">

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?m%5Cfrac%7Bdv_y%7D%7Bdt%7D%3D-B_2vv_y-mg">

将<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?v_x%28t%29">和<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?v_y%28t%29">进行泰勒展开，然后舍弃高阶无穷小项可得到关系式

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?v_x%28t&amp;plus;%5CDelta%20t%29%3Dv_x%28t%29&amp;plus;%5Cfrac%7Bdv_x%7D%7Bdt%7D%5CDelta%20t">

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?v_y%28t&amp;plus;%5CDelta%20t%29%3Dv_y%28t%29&amp;plus;%5Cfrac%7Bdv_y%7D%7Bdt%7D%5CDelta%20t">

所以联立以上四式可得得出

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?v_x%28t&amp;plus;%5CDelta%20t%29%3Dv_x%28t%29-%5Cfrac%7BB_2vv_x%7D%7Bm%7D%5CDelta%20t">

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?v_y%28t&amp;plus;%5CDelta%20t%29%3Dv_y%28t%29-%5Cfrac%7BB_2vv_y%7D%7Bdt%7D%5CDelta%20t-g%5CDelta%20t">

然后我们考虑到棒球带有旋转，所以在z轴方向会受到马格努斯力的作用，而关于马格努斯力有

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?F_M%3DS_0%5Comega%20v_x">

因此在z轴可列出动力学方程

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?m%5Cfrac%7Bdv_z%7D%7Bdt%7D%3DS_0%5Comega%20v_x-B_2vv_z">

所以同样可以得到

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?v_z%28t&amp;plus;%5CDelta%20t%29%3Dv_z%28t%29&amp;plus;%5Cfrac%7BS_0%5Comega%20v_x%7D%7Bm%7D%5CDelta%20t-%5Cfrac%7BB_2vv_z%7D%7Bm%7D%5CDelta%20t">

故可得到三个递推式为

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?v_%7Bx%2Ci&amp;plus;1%7D%3Dv_%7Bx%2Ci%7D-%5Cfrac%7BB_2vv_%7Bx%2Ci%7D%7D%7Bm%7D%5CDelta%20t">

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?v_%7By%2Ci&amp;plus;1%7D%3Dv_%7By%2Ci%7D-%5Cfrac%7BB_2vv_%7By%2Ci%7D%7D%7Bdt%7D%5CDelta%20t-g%5CDelta%20t">

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?v_%7Bz%2Ci&amp;plus;1%7D%3Dv_%7Bz%2Ci%7D&amp;plus;%5Cfrac%7BS_0%5Comega%20v_x%7D%7Bm%7D%5CDelta%20t-%5Cfrac%7BB_2vv_%7Bz%2Ci%7D%7D%7Bm%7D%5CDelta%20t">

在棒球的运动过程中，阻力系数的变化对棒球运动的轨迹有较大的影响，所以必须考虑在程序内，这里使用了公式

<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?%5Cfrac%7BB_2%7D%7Bm%7D%3D0.0039&amp;plus;%5Cfrac%7B0.0058%7D%7B1&amp;plus;exp%5B%28v-v_d%29%5D/%5CDelta%5D%7D">

其中<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?v_d%3D35m/s">，<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?%5CDelta%3D5m/s">。把这个式子与递推式联立就可以得到新的递推式，然后对棒球运动进行模拟，取<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?g%3D9.8%20m/s%5E2">。

最终的程序代码为[程序代码]()

设定初始速度为30m/s，抛射角为35度，角速度为2000rpm，<img id="equationview" name="equationview" title="This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program." src="http://latex.codecogs.com/gif.latex?%5Cfrac%7BS_0%7D%7Bm%7D%3D0.00041">，计算的时间间隔为0.1s，运行程序后得到了三维图像。

[3D图像]()

##结论
带入设定的初始d参数运行程序后发现棒球在z轴的偏转距离较大，这并不符合我们的生活经验，可能的原因是没有考虑棒球旋转的衰减。棒球在实际运动过程中的旋转角速度不可能是恒定不变的，我觉得这对棒球的偏转有较大影响。
