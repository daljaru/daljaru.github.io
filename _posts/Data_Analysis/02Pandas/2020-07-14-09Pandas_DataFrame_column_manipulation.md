---
layout: post
title: "DataFrame 컬럼명 변경 및 추가"
date: 2020-07-14
desc: "DataFrame 컬럼명 변경 및 추가"
keywords: python, pandas, DataFrame, columns
categories: [Data_analysis]
tags: [python, pandas, DataFrame, columns]
---

## Column명 변경

___

~~~python
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

df3 = pd.read_csv('../data/tips.csv')
df3

'''
     total_bill   tip     sex smoker   day    time  size
0         16.99  1.01  Female     No   Sun  Dinner   2.0
1         10.34  1.66    Male     No   Sun  Dinner   3.0
2         21.01  3.50    Male     No   Sun  Dinner   3.0
3         23.68  3.31    Male     No   Sun  Dinner   2.0
4         24.59  3.61  Female     No   Sun  Dinner   4.0
..          ...   ...     ...    ...   ...     ...   ...
240       27.18  2.00  Female    Yes   Sat  Dinner   2.0
241       22.67  2.00    Male    Yes   Sat  Dinner   2.0
242       17.82  1.75    Male     No   Sat  Dinner   2.0
243       18.78  3.00  Female     No  Thur  Dinner   2.0
244       25.34   NaN     NaN    NaN   NaN     NaN   NaN

[245 rows x 7 columns]
'''
~~~

위 데이터을 토대로 작업하겠습니다. 

<br>

### rename()

rename()함수를 이용해 컬럼 명을 변경할 수 있습니다. 이 때 columns속성에 딕셔너리를 넣어야 합니다. 

total_bill컬럼명을 total로, smoker컬럼명을 smoking으로 바꿔보겠습니다.

~~~python
df3.rename(columns={'total_bill':'total', 'smoker':'smoking'})
print(df3)
'''
     total   tip     sex smoking   day    time  size
0    16.99  1.01  Female      No   Sun  Dinner   2.0
1    10.34  1.66    Male      No   Sun  Dinner   3.0
2    21.01  3.50    Male      No   Sun  Dinner   3.0
3    23.68  3.31    Male      No   Sun  Dinner   2.0
4    24.59  3.61  Female      No   Sun  Dinner   4.0
..     ...   ...     ...     ...   ...     ...   ...
240  27.18  2.00  Female     Yes   Sat  Dinner   2.0
241  22.67  2.00    Male     Yes   Sat  Dinner   2.0
242  17.82  1.75    Male      No   Sat  Dinner   2.0
243  18.78  3.00  Female      No  Thur  Dinner   2.0
244  25.34   NaN     NaN     NaN   NaN     NaN   NaN

[245 rows x 7 columns]
'''
~~~

<br>

### columns attribute이용하기 

데이터프레임 인스턴스의 columns attribute에 리스트를 줌으로써 컬럼명을 변경할 수 있습니다. 

각 컬럼명을 A, B, C, D, E, F, G로 바꿔보겠습니다. 

~~~python
df3.columns = ['A', 'B', 'C', 'D', 'E', 'F','G']
print(df3)

'''
         A     B       C    D     E       F    G
0    16.99  1.01  Female   No   Sun  Dinner  2.0
1    10.34  1.66    Male   No   Sun  Dinner  3.0
2    21.01  3.50    Male   No   Sun  Dinner  3.0
3    23.68  3.31    Male   No   Sun  Dinner  2.0
4    24.59  3.61  Female   No   Sun  Dinner  4.0
..     ...   ...     ...  ...   ...     ...  ...
240  27.18  2.00  Female  Yes   Sat  Dinner  2.0
241  22.67  2.00    Male  Yes   Sat  Dinner  2.0
242  17.82  1.75    Male   No   Sat  Dinner  2.0
243  18.78  3.00  Female   No  Thur  Dinner  2.0
244  25.34   NaN     NaN  NaN   NaN     NaN  NaN

[245 rows x 7 columns]
'''
~~~

<br>

## Column 추가

___

컬럼을 추가할 때는 데이터프레임 객체에 `['새로운 컬럼명']`을 붙여주고 값을 대입해줍니다. 

~~~python
df3['new'] = np.nan
print(df3)
'''
         A     B       C    D     E       F    G  new
0    16.99  1.01  Female   No   Sun  Dinner  2.0  NaN
1    10.34  1.66    Male   No   Sun  Dinner  3.0  NaN
2    21.01  3.50    Male   No   Sun  Dinner  3.0  NaN
3    23.68  3.31    Male   No   Sun  Dinner  2.0  NaN
4    24.59  3.61  Female   No   Sun  Dinner  4.0  NaN
..     ...   ...     ...  ...   ...     ...  ...  ...
240  27.18  2.00  Female  Yes   Sat  Dinner  2.0  NaN
241  22.67  2.00    Male  Yes   Sat  Dinner  2.0  NaN
242  17.82  1.75    Male   No   Sat  Dinner  2.0  NaN
243  18.78  3.00  Female   No  Thur  Dinner  2.0  NaN
244  25.34   NaN     NaN  NaN   NaN     NaN  NaN  NaN

[245 rows x 8 columns]
'''
~~~