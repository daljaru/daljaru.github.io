---
layout: post
title: "DataFrame slicing"
date: 2020-07-15
desc: "DataFrame slicing"
keywords: python, pandas, DataFrame
categories: [Data_analysis]
tags: [python, pandas, DataFrame]
---

## DataFrame Slicing

___

함수를 사용하지 않고 0데이터 프레임을 Slicing하는 방법에는 자릿 수를 이용하는 방법과 라벨로 조회하는 방법이 있습니다. 자릿 수로 슬라이싱하면 행이 조회되고 라벨로 슬라이싱하면 열이 조회됩니다. 

~~~python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

np.random.seed(100)
df = DataFrame(np.random.randint(0, 100, 25).reshape(5,5))
df.columns=['A','B','C','D','E']
print(df)
'''
    A   B   C   D   E
0   8  24  67  87  79
1  48  10  94  52  98
2  53  66  98  14  34
3  24  15  60  58  16
4   9  93  86   2  27
'''
~~~

<br>

### 자릿수로 슬라이싱하기

`[start:end]`를 DataFrame 변수 오른쪽에 붙여서 인덱싱 합니다. start번째 행부터 end번째 행 이전까지가 조회됩니다. 

~~~python
print(df[0:3])
'''
    A   B   C   D   E
0   8  24  67  87  79
1  48  10  94  52  98
2  53  66  98  14  34
'''

print(df[0:1])
'''
   A   B   C   D   E
0  8  24  67  87  79
'''

print(df[:])
'''
    A   B   C   D   E
0   8  24  67  87  79
1  48  10  94  52  98
2  53  66  98  14  34
3  24  15  60  58  16
4   9  93  86   2  27
'''
~~~

<br>

### 라벨로 슬라이싱 하기 

인덱스 자리에 column들의 이름이 있는 리스트를 넣습니다. [['column1, column2']]를 적으면 column1의 열부터 column2의 열까지 슬라이싱 됩니다. 

~~~python
print(df[['A','B']])
'''
    A   B
0   8  24
1  48  10
2  53  66
3  24  15
4   9  93
'''

print(df[[]])
'''
Empty DataFrame
Columns: []
Index: [0, 1, 2, 3, 4]
'''
~~~