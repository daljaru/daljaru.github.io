---
layout: post
title: "histogram basic"
date: 2020-07-17
desc: "histogram basic"
keywords: python, pandas, matplotlib, pyplot, hist
categories: [Data_analysis]
tags: [python, pandas,  matplotlib, pyplot, hist]
---

## histogram

___

> 히스토그램(histogram)은 표로 되어 있는 도수 분포를 정보 그림으로 나타낸 것입니다. 더 간단하게 말하면, 도수분포표를 그래프로 나타낸 것입니다. - wikipedia

~~~python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(100)
plt.hist(np.random.randint(0,10,100), bins=20)
plt.show()
~~~

![histogram](/static/assets/img/blog/data_analysis/03Matplotlib/histogram.png){:width="40%" height="40%"}

bins 속성은 막대기의 굵기를 나타냅니다. 크면 클수록 막대기의 굵기가 얇아집니다. 

<br>

~~~python
dice=[]
for i in range(10000):
    dice.append(np.random.randint(1,7))
plt.hist(dice, bins= 20)
plt.show(
~~~

![histogram2](/static/assets/img/blog/data_analysis/03Matplotlib/histogram2.png){:width="40%" height="40%"}

<br>

~~~python
n,bins,patches=plt.hist(x,bins=80,density=1, alpha=0.35)
plt.xlabel('Smarts')
plt.ylabel('Probablity')
plt.title('Histogram of Info')
plt.grid()
plt.text(60,0.025,'$ \mu  \gamma \sigma $')
plt.show()
~~~

![histogram3](/static/assets/img/blog/data_analysis/03Matplotlib/histogram3.png){:width="40%" height="40%"}