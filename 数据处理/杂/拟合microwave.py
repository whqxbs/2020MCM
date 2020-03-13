import numpy as np
from sklearn import datasets,linear_model
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
#数据
x = np.array([[0.1038,0.2863,10],[0.099,0.2863,7],[0.0562,0.1535,1],[0.0974,0.5823,14],[0.0874,0.4763,25],[0.082,0.3035,12],[0.0815,0.4504,29],[0.0683,0.4287,67],[0.1782,0.5656,150],[0.1157,0.6034,279],[0.2683,0.7011,472],[0.9509,0.7593,549]])

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