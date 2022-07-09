import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import lstsq

#avoid font problem
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']= False

#原始实验数据
t = np.array([29,35,40,45,50,55,60,65,70,75,80,85,90])
v = np.array([13.0,13.5,13.5,13.5,13.5,11.5,11.5,10.5,10,9.5,7.5,5.5,4.5])

x1 = np.array([26,94])
y1 = np.array([12,12])

plt.plot(t,v,marker="o",label='原始数据')

plt.plot(x1,y1,color='r')

plt.xlabel('温度$T$/℃')
plt.ylabel('击穿临界距离$d/mm$')
#显示图例
plt.legend(loc=4)
#标题
plt.title('第二组改进实验装置下空气击穿临界距离随温度的变化图')

plt.savefig(r'D:\\Documents\\USTC\\Freshman\\second\\社会与科学\\static\\fig2.png')
plt.show()
