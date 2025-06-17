import numpy as n
import matplotlib.pyplot as hlt
HR = n.random.randint(0,100,(5,5))
HR[1:4,1:4] = 999
# Boolean Indexing
HR[HR>50]=-1
print(HR)

x = n.arange(99,1,8)
print(x)


h = n.array([1,2,3])
print(h[:,n.newaxis,n.newaxis])
x = n.arange(24).reshape(2,3,4)
print(x)
print(x[:, :, 0])
print(x[..., 0])
## 2D Indexing
y = n.arange(35).reshape(5, 7)
y1 = y[n.array([0, 2, 4])]
print(y1)
x = n.arange(35).reshape(5, 7)
b = x > 20
h = b[:, 5]
print(x[h])

#Fancy Indexing 
x = n.arange(9).reshape(3,3)
print(x[[2,1,0]])
y = [0,1,2]
print(n.mean(x[:,y],axis=1)) # colom
print(n.mean(x[y,:],axis=0)) # rows
print(x.flatten())

#Project
Temp = n.linspace(15. , 35.,30)
print("Mean: ",Temp.mean(),"\nMedian: ",n.median
(Temp),"\nMax: ",n.max(Temp),"\nMin: ",n.min(Temp))
xx = Temp[Temp > 30]
yy = Temp[Temp < 20]
print(xx)
print(yy)
hlt.plot(xx,yy)
hlt.xlabel("X Haxis")
hlt.ylabel("Y Haxis")
hlt.title("Hyeah")
hlt.show()