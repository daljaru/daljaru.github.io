---
layout: post
title: "heatmap basic"
date: 2020-07-17
desc: "heatmap basic"
keywords: python, pandas, matplotlib, pyplot, heatmap
categories: [Data_analysis]
tags: [python, pandas,  matplotlib, pyplot, heatmap]
---

## heatmap

___

> 히트 맵(heat map)은 열을 뜻하는 히트(heat)와 지도를 뜻하는 맵(map)을 결합시킨 단어로, 색상으로 표현할 수 있는 다양한 정보를 일정한 이미지위에 열분포 형태의 비쥬얼한 그래픽으로 출력하는 것이 특징입니다. 주로 웹사이트의 방문자를 분석하는 웹로그분석에 많이 사용하는 분석 기법입니다. - wikipedia

~~~python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
~~~

<br>

~~~python
flights = sns.load_dataset('flights')
flights=flights.pivot_table(values=['passengers'], index=['month'], columns=['year'])
plt.figure(figsize=(10,8))
sns.heatmap(flights, annot=True, )
plt.show()
~~~

![hitmap](/static/assets/img/blog/data_analysis/03Matplotlib/hitmap.png){:width="60%" height="60%"}

