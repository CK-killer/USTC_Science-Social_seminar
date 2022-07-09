import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import lstsq

#avoid font problem
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']= False

#原始实验数据
t = np.array([29.0,29.5,30.0,30.5,31.0,31.5,32,32.5,33,33.5,34,34.6,35,35.5,36.0,36.5,37.0,37.3,37.8,38.4,38.8,39.6,40.0,40.5,41.0,41.5,42,42.6,
              43.1,43.6,44,44.5,45.3,46,46.6,47.2,48,48.8,49.5,50,51,52,53,54,55,55.9,56.5,58.5,60,62,64,65,66.6,70])
v = np.array([7,8,8,7.5,4,8,8,7,7,6.5,5,6,6,8,7,7,7.5,5,4,8,4,5,6,6,7,8,8.5,9,8,8,8,9,9,6,9,8,9,10,15,13.5,12,15,10,9,10,8,9,8,10,19,9,8.5,8,9])

x1 = np.array([29,70])
y1 = np.array([11,11])

x2 = np.array([29,70])
y2 = np.array([9,9])

x3 = np.array([29,70])
y3 = np.array([6,6])

#plt.scatter(t,v,marker="x",color='r',label='原始数据')
plt.plot(t,v,marker="o",label='原始数据')
plt.plot(x1,y1,color='r')
plt.plot(x2,y2,color='pink')
plt.plot(x3,y3,color='purple')
plt.xlabel('温度$T$/℃')
plt.ylabel('击穿临界距离$d/mm$')
#显示图例
plt.legend(loc=4)
#标题
plt.title('该实验装置下空气击穿临界距离随温度的变化图')
plt.savefig(r'D:\\Documents\\USTC\\Freshman\\second\\社会与科学\\static\\fig1.png')
plt.show()
