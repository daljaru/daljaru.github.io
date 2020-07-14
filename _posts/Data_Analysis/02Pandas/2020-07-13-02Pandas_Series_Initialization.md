---
layout: post
title: "Series 초기화"
date: 2020-07-13
desc: "Series Initialization"
keywords: python, pandas, series
categories: [Data_analysis]
tags: [python, pandas, series]
---

## Series

___

Series는 인덱스를 명시적으로 지정하지 않으면 자동으로 0~N-1까지의 정수를 지정합니다. 시리즈는 결론적으로 말하자면 Numpy Array이기 때문에 시리즈는 동일한 자료형만 담을 수 있다.

### Series()

> Series(ndarray, index)

~~~python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

np.random.seed(0)

ser = Series(np.random.randint(1,10,5))
print(ser)
'''
0    6
1    1
2    4
3    4
4    8
dtype: int32
'''

ser1 = Series(np.random.randint(10,20,5), index=list('abcde'))
print(ser1)
'''
a    15
b    10
c    13
d    13
e    17
dtype: int32
'''

print(ser1.index)
'''
Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
'''

print(ser1.values)
'''
[19 13 15 12 14]
'''
~~~