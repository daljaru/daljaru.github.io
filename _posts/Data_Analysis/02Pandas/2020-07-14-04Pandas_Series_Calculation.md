---
layout: post
title: "Series 연산"
date: 2020-07-14
desc: "Series 연산"
keywords: python, pandas, series
categories: [Data_analysis]
tags: [python, pandas, series]
---

## Series 연산

___

~~~python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

test= Series([None, None, 1, 2, 3, 4, 5, 6, None])
test2 = Series(np.random.randint(1, 10, 9))

print(test)
print(test2)
'''
0    NaN
1    NaN
2    1.0
3    2.0
4    3.0
5    4.0
6    5.0
7    6.0
8    NaN
dtype: float64

0    9
1    9
2    4
3    8
4    8
5    1
6    5
7    3
8    6
dtype: int32
'''

result = test + test2
print(result)
'''
0     NaN
1     NaN
2     5.0
3    10.0
4    11.0
5     5.0
6    10.0
7     9.0
8     NaN
dtype: float64
'''

result = test - test2
print(result)
'''
0    NaN
1    NaN
2   -3.0
3   -6.0
4   -5.0
5    3.0
6    0.0
7    3.0
8    NaN
dtype: float64
'''
~~~