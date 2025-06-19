import numpy as n
import pandas as p
import matplotlib.pyplot as pt
import seaborn as s

# sin wave
h = n.linspace(10,21,100)
hy = n.sin(h)
pt.plot(h,hy)
pt.title("Haris Haha")
pt.xlabel("HX-Label")
pt.ylabel("Hy-Label")
pt.show()

# Bar 
hxbar = ["A","B","C"]
Hybar = [10,30,50]
pt.bar(hxbar,Hybar)
pt.title("Bar Plot")
pt.show()

# Scatter
hxScat = n.random.randint(100)
hyScat = n.random.randint(100)
pt.scatter(hxScat,hyScat)
pt.title("Scatter Plot")
pt.show()



