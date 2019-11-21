import numpy as np

a = np.arange(9)  #创建数组a
b = np.random.randn(3,3)  #创建二维数组b
a1 = np.array(a).reshape(3,3)   #将一维数组a变换为二维数组，且形状和b相同
c = np.concatenate((b,a1),axis = 1)    #将a1和b在轴1方向上进行拼接
d = np.transpose(c)    #对数组进行翻转操作
print("数组a：\n",a)
print("数组a1：\n",a1)
print("数组b：\n",b)
print("数组c：\n",c)
print("数组d：\n",d)