---
layout: post
title: "DataFrame Sorting"
date: 2020-07-14
desc: "DataFrame Sorting"
keywords: python, pandas, NaN, sort_value
categories: [Data_analysis]
tags: [python, pandas, NaN]
---

## DataFrame 정렬하기

DataFrame을 정렬할 때는 sort_values()와 sort_index()함수를 이용합니다. 

~~~python
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

df = pd.read_csv('../data/tips.csv')
~~~

### sort_values()

> Signature:
df.sort_values(
    by,
    axis=0,
    ascending=True,
    inplace=False,
    kind='quicksort',
    na_position='last',
    ignore_index=False,
)

sort_values()함수를 이용해서 원하는 컬럼 별로 정렬을 할 수 있습니다. 

예를 들어 tip순으로 정렬을 하고 싶다면 아래와 같이 by에 tip만 들어간 리스트를 값으로 넣습니다. 

~~~python
print(df.sort_values(by=['tip']).head(10))
'''
     total_bill   tip     sex smoker   day    time  size
67         3.07  1.00  Female    Yes   Sat  Dinner   1.0
236       12.60  1.00    Male    Yes   Sat  Dinner   2.0
92         5.75  1.00  Female    Yes   Fri  Dinner   2.0
111        7.25  1.00  Female     No   Sat  Dinner   1.0
0         16.99  1.01  Female     No   Sun  Dinner   2.0
215       12.90  1.10  Female    Yes   Sat  Dinner   2.0
237       32.83  1.17    Male    Yes   Sat  Dinner   2.0
235       10.07  1.25    Male     No   Sat  Dinner   2.0
75        10.51  1.25    Male     No   Sat  Dinner   2.0
135        8.51  1.25  Female     No  Thur   Lunch   2.0
'''
~~~

<br>

tip순으로 정렬한 후 total_bill순으로 세부정렬을 하고 싶다면 리스트에 total_bill을 추가해줍니다. 

tip이 정렬되고 그 안에서 total_bill이 정렬된것을 확인할 수 있습니다. 

~~~python
print(df.sort_values(by=['tip','total_bill']).head(10))
'''
     total_bill   tip     sex smoker   day    time  size
67         3.07  1.00  Female    Yes   Sat  Dinner   1.0
92         5.75  1.00  Female    Yes   Fri  Dinner   2.0
111        7.25  1.00  Female     No   Sat  Dinner   1.0
236       12.60  1.00    Male    Yes   Sat  Dinner   2.0
0         16.99  1.01  Female     No   Sun  Dinner   2.0
215       12.90  1.10  Female    Yes   Sat  Dinner   2.0
237       32.83  1.17    Male    Yes   Sat  Dinner   2.0
135        8.51  1.25  Female     No  Thur   Lunch   2.0
235       10.07  1.25    Male     No   Sat  Dinner   2.0
75        10.51  1.25    Male     No   Sat  Dinner   2.0
'''
~~~

<br>

ascending 속성은 오름차순, 내림차순을 결정합니다. 기본값은 오름차순이기 때문에 설정을 안해주면 자동으로 오름차순으로 정렬됩니다. 내림차순으로 정렬해보겠습니다. 

~~~python
print(df.sort_values(by=['tip'], ascending=False).head(10))
'''
     total_bill    tip     sex smoker   day    time  size
170       50.81  10.00    Male    Yes   Sat  Dinner   3.0
212       48.33   9.00    Male     No   Sat  Dinner   4.0
23        39.42   7.58    Male     No   Sat  Dinner   4.0
59        48.27   6.73    Male     No   Sat  Dinner   4.0
141       34.30   6.70    Male     No  Thur   Lunch   6.0
214       28.17   6.50  Female    Yes   Sat  Dinner   3.0
183       23.17   6.50    Male    Yes   Sun  Dinner   4.0
47        32.40   6.00    Male     No   Sun  Dinner   4.0
239       29.03   5.92    Male     No   Sat  Dinner   3.0
88        24.71   5.85    Male     No  Thur   Lunch   2.0
'''
~~~

<br>

정렬 후에 왼쪽 인덱스를 다시 0부터 주고 싶다면 ignore_index속성을 변경합니다. 

~~~python
print(df.sort_values(by=['tip'], ascending=False, ignore_index=True).head(10))
'''
   total_bill    tip     sex smoker   day    time  size
0       50.81  10.00    Male    Yes   Sat  Dinner   3.0
1       48.33   9.00    Male     No   Sat  Dinner   4.0
2       39.42   7.58    Male     No   Sat  Dinner   4.0
3       48.27   6.73    Male     No   Sat  Dinner   4.0
4       34.30   6.70    Male     No  Thur   Lunch   6.0
5       28.17   6.50  Female    Yes   Sat  Dinner   3.0
6       23.17   6.50    Male    Yes   Sun  Dinner   4.0
7       32.40   6.00    Male     No   Sun  Dinner   4.0
8       29.03   5.92    Male     No   Sat  Dinner   3.0
9       24.71   5.85    Male     No  Thur   Lunch   2.0
'''
~~~