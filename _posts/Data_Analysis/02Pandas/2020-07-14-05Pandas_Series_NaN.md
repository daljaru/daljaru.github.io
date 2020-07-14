---
layout: post
title: "Series NaN handling"
date: 2020-07-14
desc: "Series NaN handling"
keywords: python, pandas, NaN, Series
categories: [Data_analysis]
tags: [python, pandas, NaN, Series]
---

## Pandas의 결측치

___

Pandas에서는 null값을 missing data 혹은 missing이라고 부릅니다. missing과 null은 번갈아가며 쓸 수 있지만 pandas의 표준대로 말하자면 missing이 더 잘 쓰입니다. 우리나라 말로는 결측치라고 합니다.

~~~python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

test= Series([None, None, 1, 2, 3, 4, 5, 6, None])
print(test)
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
'''
~~~

<br>

### isnull()

~~~python
.
.
print(test.isnull())
'''
0     True
1     True
2    False
3    False
4    False
5    False
6    False
7    False
8     True
dtype: bool      --> NaN은 True, 그 외는 False
'''
.
.
~~~

<br>

### notnull()

~~~python
.
.
print(test.notnull())
'''
0    False
1    False
2     True
3     True
4     True
5     True
6     True
7     True
8    False         -->Nan은 False, 그 외는 True
'''
.
.
~~~