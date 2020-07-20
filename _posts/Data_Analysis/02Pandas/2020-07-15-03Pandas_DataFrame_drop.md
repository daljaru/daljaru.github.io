---
layout: post
title: "DataFrame drop columns"
date: 2020-07-15
desc: "DataFrame drop columns"
keywords: python, pandas, DataFrame, drop
categories: [Data_analysis]
tags: [python, pandas, DataFrame, drop]
---

## DataFrame column 삭제하기

___

~~~python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

np.random.seed(100)
df = DataFrame(np.random.randint(0, 100, 25).reshape(5,5))
df.columns=['A','B','C','D','E']
df.index = ['first','second','third','fourth','fifth']
df
'''
         A   B   C   D   E
first    8  24  67  87  79
second  48  10  94  52  98
third   53  66  98  14  34
fourth  24  15  60  58  16
fifth    9  93  86   2  27
'''
~~~

<br>

### drop()

원하는 column을 삭제하려면 drop()함수를 씁니다. 

~~~python
print(df.drop(['A','B'], axis = 1))
'''
         C   D   E
first   67  87  79
second  94  52  98
third   98  14  34
fourth  60  58  16
fifth   86   2  27
'''

print(df.drop(columns=['A','B']))
'''
         C   D   E
first   67  87  79
second  94  52  98
third   98  14  34
fourth  60  58  16
fifth   86   2  27
'''

print(df.drop(['first','second']))
'''
         A   B   C   D   E
third   53  66  98  14  34
fourth  24  15  60  58  16
fifth    9  93  86   2  27
'''

print(df.drop(index='first', columns='C'))
'''
         A   B   D   E
second  48  10  52  98
third   53  66  14  34
fourth  24  15  58  16
fifth    9  93   2  27
'''
~~~