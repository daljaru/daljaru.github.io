---
layout: post
title: "Series값 조회하기"
date: 2020-07-13
desc: "Series값 조회하기"
keywords: python, pandas, series, isnull, notnull
categories: [Data_analysis]
tags: [python, pandas, series, isnull, notnull]
---

## Series값 조회하기

___

Series의 값을 조회할 때는 인덱스로 조회하는 방법, 라벨로 조회하는 방법 두 가지가 있습니다. 

~~~python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

np.random.seed(100)
testSeries = Series(np.random.randint(1, 10, 10), index=list('abcdefghij'))
print(testSeries)
'''
a    9
b    9
c    4
d    8
e    8
f    1
g    5
h    3
i    6
j    3
dtype: int32
'''

print(testSeries[0])
print(testSeries['a'])
'''
9
9
'''
print(testSeries[1:5])
print(testSeries['b':'f'])

'''
b    9
c    4
d    8
e    8      --> 인덱스로 조회할 때는 : 기준 오른쪽 인덱스의 값을 포함하지 않는다. 
dtype: int32
b    9
c    4
d    8
e    8
f    1      --> 라벨로 조회할때는 : 기준 오른쪽 라벨인덱스의 값도 포함한다. 
dtype: int32
'''
~~~

numpy에서 

<br>

## step을 활용해서 조회하기

___

~~~python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

np.random.seed(100)
testSeries = Series(np.random.randint(1, 10, 10), index=list('abcdefghij'))

print(testSeries)
'''
a    9
b    9
c    4
d    8
e    8
f    1
g    5
h    3
i    6
j    3
dtype: int32
'''

print(testSeries[::-1])
'''
j    3
i    6
h    3
g    5
f    1
e    8
d    8
c    4
b    9
a    9      --> label도 거꾸로 조회. 
dtype: int32   
'''

print(testSeries[::2])
'''
a    9
c    4
e    8
g    5
i    6      --> 2step으로 건너뛰어서 조회
dtype: int32
'''
~~~