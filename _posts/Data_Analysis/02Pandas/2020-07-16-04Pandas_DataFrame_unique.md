---
layout: post
title: "unique function"
date: 2020-07-16
desc: "unique function"
keywords: python, pandas, DataFrame, unique
categories: [Data_analysis]
tags: [python, pandas, DataFrame, unique]
---

## unique

unique함수는 중복된 것은 걸러버리고 중복되지 않은 값만 출력합니다. 

~~~python
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

df = pd.read_csv('../data/tips.csv',encoding='utf-8')
print(df.head())
'''
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner   2.0
1       10.34  1.66    Male     No  Sun  Dinner   3.0
2       21.01  3.50    Male     No  Sun  Dinner   3.0
3       23.68  3.31    Male     No  Sun  Dinner   2.0
4       24.59  3.61  Female     No  Sun  Dinner   4.0
'''
~~~

<br>

#### sex column에서 유니크한 값을 조회.

~~~python
print(df['sex'].unique())
'''
['Female' 'Male' nan]
'''
~~~
