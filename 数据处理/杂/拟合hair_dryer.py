import numpy as np
from sklearn import datasets,linear_model
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
#数据
x = np.array([[0.1019,0.502,8],[0.0868,0.5989,10],[0.0927,0.3222,8],[0.1086,0.4158,20],[0.1146,0.3362,71],[0.156,0.5945,182],[0.1651,0.4974,233],[0.1897,0.524,301],[0.2523,0.5081,580],[0.2849,0.5655,634],[0.349,0.5428,918],[0.6871,0.563,2149],[0.9091,0.5873,3206],[0.9153,0.5506,3143]])

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