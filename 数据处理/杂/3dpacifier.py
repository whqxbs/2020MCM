from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

# 数据录入
X = np.array([2,1,0])
Y = np.array([5,4,3,2,1])
X, Y = np.meshgrid(X, Y)
print("网格化后的X=",X)
print("X维度信息",X.shape)
print("网格化后的Y=",Y)
print("Y维度信息", Y.shape)

Z = np.array(
    [
    [10220,153,1310],
    [1895,49,495],
    [597,68,632],
    [183,34,605],
    [913,21,140] 
]
)
print("维度调整前的Z轴数据维度",Z.shape)
#Z = Z.T
print("维度调整后的Z轴数据维度",Z.shape)

ax.plot_surface(X, Y, Z,
    rstride=1,  # rstride（row）指定行的跨度
    cstride=1,  # cstride(column)指定列的跨度
    cmap=plt.get_cmap('rainbow'))  # 设置颜色映射
# 设置Z轴范围
ax.set_zlim(0, 2000)
# 设置标题
plt.title("pacifier")
plt.show()
