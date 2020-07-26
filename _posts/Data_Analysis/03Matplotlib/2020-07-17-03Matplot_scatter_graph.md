---
layout: post
title: "산점도 그리기"
date: 2020-07-17
desc: "scatter_graph"
keywords: python, pandas, matplotlib, pyplot, scatter
categories: [Data_analysis]
tags: [python, pandas,  matplotlib, pyplot, scatter]
---

## 산점도

___

산점도 그래프는 scatter() 함수를 이용해서 그립니다. 산점도는 x,y축에 해당하는 데이터들의 상관관계를 표시할 때 데이터들이 얼마나 어떻게 흩어져 있는가를 알기위해서 사용됩니다. 2개의 축을 기준으로 데이터가 얼마나 퍼져있는지(분포도)를 알 수 있기 때문에 산포도 혹은 산점도로 불립니다. 

~~~python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

arr1 = [[1,2,3,4],[10,20,30,40]]
plt.scatter(arr1[0], arr1[1],s=[100,200,300,500])
plt.show()
~~~

![scatter](/static/assets/img/blog/data_analysis/03Matplotlib/scatter.png){:width="50%" height="50%"}

<br>

~~~python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

np.random.seed(100)
data = dict(a=np.arange(0,50,1), c=np.random.randint(0,50,50), d=np.random.randn(50))
data['b'] = data['a']+10 *np.random.randn(50)
data['d'] = np.abs(data['d'])*100

plt.scatter('a', 'b', data = data, c='c')
plt.show()
~~~

![scatter2](/static/assets/img/blog/data_analysis/03Matplotlib/scatter2.png){:width="50%" height="50%"}