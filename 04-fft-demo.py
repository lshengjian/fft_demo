import numpy as np
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
 
mpl.rcParams['font.sans-serif'] = ['SimHei']   #显示中文
mpl.rcParams['axes.unicode_minus']=False       #显示负号
 
#采样点选择1400个，因为设置的信号频率分量最高为600赫兹，根据采样定理知采样频率要大于信号频率2倍，所以这里设置采样频率为1400赫兹（即一秒内有1400个采样点，一样意思的）
N=1400
ts=np.linspace(0,1,N)      
 
tau=2*np.pi
#设置需要采样的信号，频率分量有200，400和600
y=7*np.sin(200*ts*tau) + 5*np.sin(400*ts*tau)+3*np.sin(600*ts*tau)
 
fft_y=fft(y)               #快速傅里叶变换
print(fft_y[0:5])

ws = np.arange(N)          # 频率取值
half_N=range(int(N/2))
half_w = ws[half_N]  #取一半区间
 
abs_y=np.abs(fft_y)                # 取复数的绝对值，即复数的模(双边频谱)
angle_y=np.angle(fft_y)            #取复数的角度
normalization_y=abs_y/N            #归一化处理（双边频谱）                              
normalization_half_y = normalization_y[half_N]      #由于对称性，只取一半区间（单边频谱）
plt.figure(figsize=(8, 6))  # 设置窗口大小为宽度10和高度8 
plt.subplot(231)
plt.plot(ts[0:50],y[0:50]) 
plt.title('原始部分波形(前50组样本)')  

 
plt.subplot(232)
plt.plot(ws,abs_y,'black')
plt.title('双边振幅谱',fontsize=9,color='black') 
 
plt.subplot(233)
plt.plot(ws,angle_y,'r')
plt.title('双边相位谱',fontsize=9,color='red') 

plt.subplot(235)
plt.plot(ws,normalization_y,'g')
plt.title('双边振幅谱(归一化)',fontsize=9,color='green')
 
plt.subplot(236)
plt.plot(ws,angle_y,'violet')
plt.title('双边相位谱(未归一化)',fontsize=9,color='violet')
 

 
plt.subplot(234)
plt.plot(half_N,normalization_half_y,'blue')
plt.title('单边振幅谱(归一化)',fontsize=9,color='blue')
 
plt.show()
 