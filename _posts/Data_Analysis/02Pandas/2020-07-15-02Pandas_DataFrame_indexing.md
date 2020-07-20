---
layout: post
title: "DataFrame indexing"
date: 2020-07-15
desc: "DataFrame indexing"
keywords: python, pandas, DataFrame, loc, iloc, at, iat
categories: [Data_analysis]
tags: [python, pandas, DataFrame, loc, iloc, at, iat]
---

## DataFrame indexing

___


~~~python
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

df = DataFrame(np.random.randint(0, 100, 25).reshape(5,5))
df.columns=['A','B','C','D','E']
df
'''
	A	B	C	D	E
0	8	24	67	87	79
1	48	10	94	52	98
2	53	66	98	14	34
3	24	15	60	58	16
4	9	93	86	2	27
'''
~~~

<br>

## iloc()

iloc()함수는 순수 정수형 자릿수를 기반으로한 인덱싱 기법입니다. 

### only scalar

~~~python
print(df.iloc[0])
'''
A     8
B    24
C    67
D    87
E    79
Name: 0, dtype: int32
'''

print(df.iloc[0,3])
'''
87
'''
~~~

<br>

### with slicing object

~~~python
print(df.iloc[0:3])
'''
    A   B   C   D   E
0   8  24  67  87  79
1  48  10  94  52  98
2  53  66  98  14  34
'''

print(df.iloc[0:3,3:5])
'''
    D   E
0  87  79
1  52  98
2  14  34
'''
~~~

<br>

### with list object

~~~python
df.iloc[[0]]
'''
   A   B   C   D   E
0  8  24  67  87  79
'''

print(df.iloc[[0,2]])
'''
    A   B   C   D   E
0   8  24  67  87  79
2  53  66  98  14  34
'''

print(df.iloc[[0,2],[1,2]])
'''
    B   C
0  24  67
2  66  98
'''
~~~

<br>

## loc()

loc()함수는 라벨명을 기반으로한 인덱싱 기법입니다. 

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
        A	B	C	D	E
first	8	24	67	87	79
second	48	10	94	52	98
third	53	66	98	14	34
fourth	24	15	60	58	16
fifth	9	93	86	2	27
'''
~~~

<br>

### Single label

~~~python
df.loc['first']
'''
A     8
B    24
C    67
D    87
E    79
Name: first, dtype: int32
'''

df.loc[,'B']


df.loc['second','B']
'''
10
'''
~~~

<br>

### List label

~~~python
print(df.loc[['first']])
'''
       A   B   C   D   E
first  8  24  67  87  79
'''

print(df.loc[['first','third']])
'''
        A   B   C   D   E
first   8  24  67  87  79
third  53  66  98  14  34
'''

print(df.loc[['first','third'],['A','B']])
'''
        A   B
first   8  24
third  53  66
'''

df.loc['sixth']=np.nan
print(df)
'''
           A     B     C     D     E
first    8.0  24.0  67.0  87.0  79.0
second  48.0  10.0  94.0  52.0  98.0
third   53.0  66.0  98.0  14.0  34.0
fourth  24.0  15.0  60.0  58.0  16.0
fifth    9.0  93.0  86.0   2.0  27.0
sixth    NaN   NaN   NaN   NaN   NaN
'''
~~~

<br>

### slice object

~~~python
print(df.loc['first':'third','C':'E'])
'''
         C   D   E
first   67  87  79
second  94  52  98
third   98  14  34
'''
~~~

<br>

## iat[], at[]

iat()와 at()는 인자값을 두개를 줘서 데이터 하나에 접근하는 방법입니다. 

___

### iat[]

~~~python
df.iat[3,2]
'''
60
'''

df.at['first','C']
'''
67
'''
~~~