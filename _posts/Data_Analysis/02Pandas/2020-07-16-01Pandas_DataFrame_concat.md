---
layout: post
title: "DataFrame Concat"
date: 2020-07-16
desc: "DataFrame Concat"
keywords: python, pandas, NaN, concat, outer, inner, join
categories: [Data_analysis]
tags: [python, pandas, NaN, concat, outer, inner, join]
---

## Concat

___

서로 다른 DataFrame을 하나로 합치는 작업입니다. Concat은 단순히 하나의 DataFrame에 다른 DataFrame을 연속적으로 붙이는 방법입니다. 이 경우에는 두 개의 DataFrame의 인덱스와 컬럼이 서로 동일한 경우가 대부분입니다. 기본이 위,아애를 연결하는 방식이지만 axis를 수정하면 좌우연결도 가능합니다. 

Outer join이 기본방식이고 key를 이용한 concat이 가능합니다. 

~~~python
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

df1 = DataFrame({'A':['A0','A1','A2','A3'],
                'B':['B0','B1','B2','B3'],
                'C':['C0','C1','C2','C3'],
                'D':['D0','D1','D2','D3']})
print(df1)
'''
    A   B   C   D
0  A0  B0  C0  D0
1  A1  B1  C1  D1
2  A2  B2  C2  D2
3  A3  B3  C3  D3
'''
df2 = DataFrame({'A':['A4','A5','A6','A7'],
                'B':['B4','B5','B6','B7'],
                'C':['C4','C5','C6','C7'],
                'D':['D4','D5','D6','D7']})
print(df2)
'''
    A   B   C   D
0  A4  B4  C4  D4
1  A5  B5  C5  D5
2  A6  B6  C6  D6
3  A7  B7  C7  D7
'''
~~~

<br>

DataFrame df1과 df2를 상하로 병합해보겠습니다. 

### 상하연결

~~~python
result = pd.concat([df1,df2], ignore_index=True))
print(result)
'''
    A   B   C   D
0  A0  B0  C0  D0
1  A1  B1  C1  D1
2  A2  B2  C2  D2
3  A3  B3  C3  D3
4  A4  B4  C4  D4
5  A5  B5  C5  D5
6  A6  B6  C6  D6
7  A7  B7  C7  D7
'''
~~~

<br>

### 좌우 연결

~~~python
result2 = pd.concat([df1, df2], axis=1)
print(result2)
'''
    A   B   C   D   A   B   C   D
0  A0  B0  C0  D0  A4  B4  C4  D4
1  A1  B1  C1  D1  A5  B5  C5  D5
2  A2  B2  C2  D2  A6  B6  C6  D6
3  A3  B3  C3  D3  A7  B7  C7  D7
'''
~~~

<br>

### keys 

데이터를 합칠 때 어느 그룹에서 가져왔는지 구분을 하기 위해 keys속성을 넣습니다. keys속성을 통해 데이터의 그룹핑이 됩니다. 

~~~python
result3 = pd.concat([df1, df2], keys=['ClassA','ClassB','ClassC','ClassD'])
print(result3)
'''
           A   B   C   D
ClassA 0  A0  B0  C0  D0
       1  A1  B1  C1  D1
       2  A2  B2  C2  D2
       3  A3  B3  C3  D3
ClassB 0  A4  B4  C4  D4
       1  A5  B5  C5  D5
       2  A6  B6  C6  D6
       3  A7  B7  C7  D7
'''
~~~

## join

___

만약 열의 수가 다른 DataFrame두 개가 있다고 해봅시다. 

~~~python
df3 = DataFrame({'A':['A0','A1','A2','A4'],
                'B':['B0','B1','B2','B3'],
                'C':['C0','C1','C2','C3']})
df4 = DataFrame({'A':['A4','A5','A6','A7'],
                'B':['B4','B5','B6','B7'],
                'C':['C4','C5','C6','C7'],
                'D':['D4','D5','D6','D7']})
~~~

df3는 A,B,C열이 있고 df4는 A,B,C,D열이 있습니다. 이 두 DataFrame을 상하로 연결하면 concat함수에 join속성에 기본값인 outer가 지정되면서 outer join이 됩니다. 

~~~python
result2 = pd.concat([df3, df4], ignore_index=True)
print(result2)
'''
    A   B   C    D
0  A0  B0  C0  NaN
1  A1  B1  C1  NaN
2  A2  B2  C2  NaN
3  A4  B3  C3  NaN
4  A4  B4  C4   D4
5  A5  B5  C5   D5
6  A6  B6  C6   D6
7  A7  B7  C7   D7
'''
~~~

<br>

join값을 inner로 주면 inner join이 됩니다. inner join은 NaN값이 발생하는 열을 잘라냅니다. 

~~~python
result3 = pd.concat([df3, df4], join='inner', ignore_index=True)
print(result3)
'''
    A   B   C
0  A0  B0  C0
1  A1  B1  C1
2  A2  B2  C2
3  A4  B3  C3
4  A4  B4  C4
5  A5  B5  C5
6  A6  B6  C6
7  A7  B7  C7
'''
~~~