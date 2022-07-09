import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import lstsq

#avoid font problem
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']= False

#原始实验数据1
t1 = np.array([26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62.5,63,64,65,66,67,68,69,70,71,72,73,74,75,77.8,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94])
v1 = np.array([11.7,11.7,11.7,12.0,11.2,11.2,11.2,11.2,10.2,10.7,11.2,12.2,12.2,12.2,13.2,12.2,13.2,12.2,12.2,11.7,11.2,11.2,11.7,11.0,10.2,11.2,11.2,11.2,10.2,10.7,10.7,9.7,9.2,9.7,8.7,8.2,8.2,7.2,8.7,8.2,7.2,8.2,7.2,7.2,9.4,11.2,7.2,8.2,8.7,7.2,9.2,10.2,7.2,8.2,7.2,6.2,7.2,6.2,3.2,5.2,4.0,4.2,4.0,5.2,5.2,5.7,6.2,6.2])

#原始实验数据2
t = np.array([29,35,40,45,50,55,60,65,70,75,80,85,90])
v = np.array([13.0,13.5,13.5,13.5,13.5,11.5,11.5,10.5,10,9.5,7.5,5.5,4.5])

x1 = np.array([26,94])
y1 = np.array([12,12])

#plt.scatter(t,v,marker="x",color='r',label='原始数据')
plt.plot(t1,v1,marker="o",color='pink',label='第一组改进实验')
plt.plot(t,v,marker="o",color='purple',label='第二组改进实验')

plt.xlabel('温度$T$/℃')
plt.ylabel('击穿临界距离$d/mm$')
#显示图例
plt.legend(loc=3)
#标题
plt.title('第一第二组改进实验装置下空气击穿临界距离随温度的变化图')

plt.savefig(r'D:\\Documents\\USTC\\Freshman\\second\\社会与科学\\static\\fig4.png')
plt.show()
