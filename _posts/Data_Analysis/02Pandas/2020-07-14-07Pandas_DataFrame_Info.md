---
layout: post
title: "DataFrame Info"
date: 2020-07-14
desc: "DataFrame Info"
keywords: python, pandas, DataFrame, index, columns, values, dtype
categories: [Data_analysis]
tags: [python, pandas, DataFrame, index, columns, values, dtype]
---

## DataFrame 구조 확인

___

생성된 DataFrame의 기본적인 구조를 파악하는 메소드는 index, values, columns, dtype이 있습니다. 

### index

~~~python
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

np.random.seed(100)
df3 = DataFrame(np.random.randint(1, 100, 16).reshape(4,4))
df3.columns=['A','B','C','D']
df3
'''
A	B	C	D
0	9	25	68	88
1	80	49	11	95
2	53	99	54	67
3	99	15	35	25
'''
~~~

위와 같이 DataFrame을 만들고 확인해보겠습니다. 인덱스 정보를 확인할 수 있습니다. 

~~~python
df3.index
'''
RangeIndex(start=0, stop=4, step=1)
'''
~~~

<br>

### columns

컬럼의 정보를 확인할 수 있습니다. dtype도 확인가능합니다. 

~~~python
df3.columns
'''
Index(['A', 'B', 'C', 'D'], dtype='object')
'''
~~~

<br>

### values

데이터의 값들을 확인할 수 있습니다. 

~~~python
df3.values

'''
array([[ 9, 25, 68, 88],
       [80, 49, 11, 95],
       [53, 99, 54, 67],
       [99, 15, 35, 25]])
'''
~~~

<br>

### dtypes

각 컬럼의 데이터 타입을 확인할 수 있습니다. 

~~~python
df3.dtypes
'''
A    int32
B    int32
C    int32
D    int32
dtype: object
'''
~~~