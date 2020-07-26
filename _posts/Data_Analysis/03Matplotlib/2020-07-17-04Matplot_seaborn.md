---
layout: post
title: "seaborn 기초"
date: 2020-07-17
desc: "seaborn basic"
keywords: python, pandas, matplotlib, pyplot, seaborn
categories: [Data_analysis]
tags: [python, pandas,  matplotlib, pyplot, scatter]
---

## seaborn

___

![seaborn](/static/assets/img/blog/data_analysis/03Matplotlib/seaborn.png){:width="70%" height="70%"}

[Seaborn](https://seaborn.pydata.org/index.html)은 matplotlib를 기반으로한 파이썬 데이터 시각화 라이브러리입니다. 상당히 높은 수준의 시각화 인터페이스를 제공합니다.

간단한 regplot예제입니다. 

~~~python
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

np.random.seed(100)
data = dict(a=np.arange(0,50,1), c=np.random.randint(0,50,50), d=np.random.randn(50))
data['b'] = data['a']+10 *np.random.randn(50)
data['d'] = np.abs(data['d'])*100

import seaborn as sns

cuthalf = (data['a']>25) & (data['b']>30)
data['color'] = np.where(cuthalf==True, 'red', 'blue')

sns.regplot(x = data['a'],y=data['b'],scatter_kws={'facecolors':data['color']})
plt.title('Scatter Plot with Colors', fontsize=20)
plt.show()
~~~

![regplot](/static/assets/img/blog/data_analysis/03Matplotlib/regplot.png){:width="40%" height="40%"}