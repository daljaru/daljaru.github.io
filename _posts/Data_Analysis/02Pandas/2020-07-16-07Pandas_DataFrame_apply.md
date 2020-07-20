---
layout: post
title: "DataFrame apply function"
date: 2020-07-16
desc: "DataFrame apply functionn"
keywords: python, pandas, DataFrame, apply
categories: [Data_analysis]
tags: [python, pandas, DataFrame, apply]
---

## apply

___

apply함수는 각 컬럼의 값에 임의로 만든 함수를 적용하고 싶을 때 사용합니다. 

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

예를 들어 tip데이터에 1씩 더해주고 싶다면 아래와 같이 plus함수를 만들고 apply의 인자값으로 넣습니다. 

~~~python
def plus(x):
    return x+1

print(df[['tip']].apply(plus))

'''
      tip
0    2.01
1    2.66
2    4.50
3    4.31
4    4.61
..    ...
240  3.00
241  3.00
242  2.75
243  4.00
244   NaN

[245 rows x 1 columns]
'''
~~~