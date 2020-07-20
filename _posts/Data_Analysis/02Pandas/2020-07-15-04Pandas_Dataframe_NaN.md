---
layout: post
title: "NaN handling in pandas"
date: 2020-07-14
desc: "Nan handling in pandas"
keywords: python, pandas, NaN
categories: [Data_analysis]
tags: [python, pandas, NaN]
---

## Pandas의 결측치

___

Pandas에서는 null값을 missing data 혹은 missing이라고 부릅니다. missing과 null은 번갈아가며 쓸 수 있지만 pandas의 표준대로 말하자면 missing이 더 잘 쓰입니다. 우리나라 말로는 결측치라고 합니다. Pandas에서는 결측치를 모두 NaN으로 처리합니다. 

None과 numpy.na로 표시할 수 있습니다. 리스트의 마지막 값을 비움으로써 NaN을 표시할 수도 있습니다. 

~~~python
from numpy import nan as NA
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

df = DataFrame([[1,6.5,3],[NA,None,],[NA,NA,4.6],[NA,6.5,3]])
print(df)
'''
     0    1    2
0  1.0  6.5  3.0
1  NaN  NaN  NaN
2  NaN  NaN  4.6
3  NaN  6.5  3.0
'''
~~~

<br>

## 결측치를 처리하는 여러 함수들 

___

### dropna()

dropna()함수는 NaN값이 하나라도 있으면 해당 row를 삭제합니다. 

~~~python
print(df.dropna())
'''
     0    1    2
0  1.0  6.5  3.0
'''
~~~

<br>

### dropna(how='all')

dropna()함수에 how속성을 활용하면 NaN값을 지우는 방식을 정할 수 있습니다. 

how에 all값을 주면 모든 열이 NaN값인 행만 지워집니다. 

~~~python
print(df.dropna(how='all'))
'''
     0    1    2
0  1.0  6.5  3.0
2  NaN  NaN  4.6
3  NaN  6.5  3.0
'''
~~~

<br>

### dropna(how='any')

how에 any값을 주면 열에 NaN값이 하나라도 있는 행이 지워집니다. 

~~~python
print(df.dropna(how='any'))
'''
     0    1    2
0  1.0  6.5  3.0
'''
~~~

<br>

### dropna(thresh=2)

thresh속성은 행마다 NaN값이 아닌 데이터들의 개수를 넣을 수 있습니다. 

~~~python
print(df.dropna(thresh=1))
'''
     0    1    2
0  1.0  6.5  3.0
2  NaN  NaN  4.6
3  NaN  6.5  3.0
행마다 non-NaN 값이 적어도 1개는 있습니다. 
'''

print(df.dropna(thresh=3))
'''
     0    1    2
0  1.0  6.5  3.0
non=NaN값이 적어도 3개는 필요하므로 나머지 행이 지워졌습니다. 
'''

print(df.dropna(thresh=4))
'''
Empty DataFrame
Columns: [0, 1, 2]
Index: []   

thresh의 값이 열의 개수를 초과해버리면 빈 DataFrame이 나오게 됩니다. 
'''
~~~

<br>

### fillna()

fillna()함수는 결측치를 다른 값으로 채웁니다. 

~~~python
print(df.fillna(0))
'''
     0    1    2
0  1.0  6.5  3.0
1  0.0  0.0  0.0
2  0.0  0.0  4.6
3  0.0  6.5  3.0
'''

print(df.fillna('filled!'))
'''
         0        1        2
0        1      6.5        3
1  filled!  filled!  filled!
2  filled!  filled!      4.6
3  filled!      6.5        3

-->이 경우에는 컬럼이 object타입으로 변환됩니다. 
'''
~~~

<br>

## null값인지 판단하기

___

해당 값이 NaN인지 아닌지 판단하는 방법에는 대표적으로 isnull()과 notnull()이 있습니다. 

### isnull()

isnull()함수는 NaN인 값을 True로, non NaN값은 False로 변환해줍니다. 

~~~python
print(df.isnull())
'''
       0      1      2
0  False  False  False
1   True   True   True
2   True   True  False
3   True  False  False
'''
~~~

<br>

### notnull()

반대로 notnull()함수는 non-Nan값은 True로, NaN값은 False로 변환해줍니다. 

~~~python
print(df.notnull())
'''
       0      1      2
0   True   True   True
1  False  False  False
2  False  False   True
3  False   True   True
'''
~~~
