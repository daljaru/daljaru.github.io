---
layout: post
title: "boxplot basic"
date: 2020-07-17
desc: "boxplot basic"
keywords: python, pandas, matplotlib, pyplot, boxplot
categories: [Data_analysis]
tags: [python, pandas,  matplotlib, pyplot, boxplot]
---

## boxplot

> '상자 그림'(box plot, boxplot)은 수치적 자료를 표현하는 그래프입니다. 이 그래프는 가공하지 않은 자료 그대로를 이용하여 그린 것이 아니라, 자료로부터 얻어낸 통계량인 5가지 요약 수치(다섯 숫자 요약, five-number summary)를 가지고 그립니다. 이 때 5가지 요약 수치란 최솟값, 제 1사분위, 제 2사분위, 제 3사분위, 최댓값을 일컫는 말입니다. 히스토그램과는 다르게 집단이 여러개인 경우에도 한 공간에 수월하게 나타낼수 있습니다. - wikipedia

~~~python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
~~~

<br>

~~~python
xs = np.array(np.linspace(0,100,101))
df = DataFrame(xs, columns=['feature'])
plt.figure(figsize=(7,6))
df.boxplot(column=['feature'])
plt.yticks(np.arange(0,101,step=5))
plt.show()
~~~

![boxplot](/static/assets/img/blog/data_analysis/03Matplotlib/boxplot.png){:width="40%" height="40%"}

<br>

~~~python
tips = sns.load_dataset('tips')
plt.figure(figsize=(10,5))
sns.boxplot(tips['total_bill'])
~~~

![boxplot2](/static/assets/img/blog/data_analysis/03Matplotlib/boxplot2.png){:width="40%" height="40%"}

<br>

~~~python
sns.boxplot(x='day', y='total_bill', data=tips)
plt.show()
~~~

![boxplot3](/static/assets/img/blog/data_analysis/03Matplotlib/boxplot3.png){:width="40%" height="40%"}

<br>

~~~python
sns.boxplot(x='day', y='total_bill', hue='smoker', data=tips)
plt.show()
~~~

![boxplot4](/static/assets/img/blog/data_analysis/03Matplotlib/boxplot4.png){:width="40%" height="40%"}