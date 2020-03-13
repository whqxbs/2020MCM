import numpy as np
from sklearn import datasets,linear_model
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
#数据
x = np.array([[0.0994,0.15,2],[0.0997,0.2529,4],[0.1104,0.3369,91],[0.1097,0.3366,24],[0.1412,0.4035,100],[0.1615,0.4348,199],[0.1831,0.5098,174],[0.2158,0.6102,302],[0.3065,0.712,1005],[0.3564,0.6865,1424],[0.6513,0.8242,3706],[0.8952,0.7821,6063],[0.8359,0.7858,5769]])

#print(x)
X = x[:,:-1]
Y = x[:,-1]
#print(X,Y)

#拟合
regr = linear_model.LinearRegression()
regr.fit(X,Y)
print('coefficients(b1,b2...):',regr.coef_)
print('intercept(b0):',regr.intercept_)
#print(regr.coef_[1])
A = np.arange(0, 1, 0.0003)
B = np.arange(0, 1, 0.0003)
A, B = np.meshgrid(A, B)
Z = regr.coef_[0]*A+regr.coef_[1]*B+regr.intercept_
ax.plot_wireframe(A, B, Z)
ax.plot_surface(A, B, Z, alpha=0.3)

plt.title("y="+str(regr.coef_[0])+"x1"+str(regr.coef_[1])+"x2"+str(regr.intercept_))
plt.show()
#预测
#x_test = np.array([[102,6],[100,4]])
#y_test = regr.predict(x_test)
#print(y_test)