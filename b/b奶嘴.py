import numpy as np
import matplotlib.pyplot as plt
import xlrd
import xlwt
 
#读数据
path=u'婴儿.xlsx'
hn,nc=1,1
#hn为表头行数,nc为表头列数
sheetname=u'Sheet2'
def readexcel(hn,nc):
    data = xlrd.open_workbook(path)
    table = data.sheet_by_name(sheetname)
    nrows = table.nrows
    data=[]
    for i in range(hn,nrows):
        data.append(table.row_values(i)[nc:])
    #print(np.array(data))
    return np.array(data)

data=readexcel(hn,nc)
#print(data)
X = data[:,0]
Y1 = data[:,1]
Y2 = data[:,2]
#print(X)
#print(Y1)
#print(Y2)
plt.xlabel("Time")#x轴上的名字
plt.ylabel("Reputation")#y轴上的名字
plt.title("pacifier Blue→Reputation1 Green→Reputation2")
plt.plot(X,Y1,color='blue')
plt.plot(X,Y2,color='green')
plt.show()