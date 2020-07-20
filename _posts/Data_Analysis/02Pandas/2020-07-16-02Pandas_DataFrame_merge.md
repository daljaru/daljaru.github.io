---
layout: post
title: "DataFrame Merge"
date: 2020-07-16
desc: "DataFrame Merge"
keywords: python, pandas, merge, left, right, how, inner, outer 
categories: [Data_analysis]
tags: [python, pandas, merge, left, right, how, inner, outer]
---

## Merge

___

서로 다른 DataFrame을 하나로 합치는 작업중에서 merge는 두개의 DataFrame의 행이 같은 것은 중복처리하는 특징이 있습니다. 

~~~python
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

df2 = DataFrame({'Year':[2001,2002,2003,2011,2012,2013,2014,2015],
                'Rate':[1.7,4.3,5.4,2.2,2.7,5.8,6.7,4.6],
                'Price':[15000,22000,13000,15000,18500,17600,16500,19340]})

df3 = DataFrame({'Year':[2008,2009,2010,2011,2012,2013,2014,2015],
                'Rate':[1.8,5.3,3.4,3.2,2.7,5.8,6.7,4.6],
                'Class':['A','B','C','D','A','C','B','B']})
print(df2)
print('====================')
print(df3)
'''
   Year  Rate  Price
0  2001   1.7  15000
1  2002   4.3  22000
2  2003   5.4  13000
3  2011   2.2  15000
4  2012   2.7  18500
5  2013   5.8  17600
6  2014   6.7  16500
7  2015   4.6  19340
====================
   Year  Rate Class
0  2008   1.8     A
1  2009   5.3     B
2  2010   3.4     C
3  2011   3.2     D
4  2012   2.7     A
5  2013   5.8     C
6  2014   6.7     B
7  2015   4.6     B
'''
~~~

데이터가 위와 같이 주어졌다고 가정해보겠습니다. 

### merge()

> pd.merge(
    left,
    right,
    how: str = 'inner',
    on=None,
    left_on=None,
    right_on=None,
    left_index: bool = False,
    right_index: bool = False,
    sort: bool = False,
    suffixes=('_x', '_y'),
    copy: bool = True,
    indicator: bool = False,
    validate=None,
) -> 'DataFrame'

#### how속성을 비면 기본적으로 inner로 설정되어 있는 것을 볼 수 있습니다. 

<br>

### inner

~~~python
result = pd.merge(df2, df3)
print(result)
'''
   Year  Rate  Price Class
0  2012   2.7  18500     A
1  2013   5.8  17600     C
2  2014   6.7  16500     B
3  2015   4.6  19340     B
'''
~~~

df2와 df3의 공통 열(Year, Rate)가 2012,2013,2014, 2015년이 있는 행이 같기 때문에 위 4개의 행만 출력이 되었습니다. 

<br>

### outer

~~~python
result = pd.merge(df2, df3, how='outer')
print(result)
'''
    Year  Rate    Price Class
0   2001   1.7  15000.0   NaN
1   2002   4.3  22000.0   NaN
2   2003   5.4  13000.0   NaN
3   2011   2.2  15000.0   NaN
4   2012   2.7  18500.0     A
5   2013   5.8  17600.0     C
6   2014   6.7  16500.0     B
7   2015   4.6  19340.0     B
8   2008   1.8      NaN     A
9   2009   5.3      NaN     B
10  2010   3.4      NaN     C
11  2011   3.2      NaN     D
'''
~~~

how속성을 outer로 설정해서 merge를 하면 df2와 df3의 모든 행이 나타나는 것을 볼 수 있습니다. 다만 df2에는 있지만 df3에 없는 행은 Class가 NaN값이 나왔고, df2에는 없지만 df3에 있는 행은 Price가 NaN값이 나온 것을 확인할 수 있습니다. 

<br>

### left

left값은 두 DataFrame을 merge시 왼쪽 DataFrame에는 있지만 오른쪽 DataFrame에는 없는 행도 같이 병합됩니다. 

~~~python
result3 = pd.merge(df2, df3, how='left')
print(result3)
'''
   Year  Rate  Price Class
0  2001   1.7  15000   NaN
1  2002   4.3  22000   NaN
2  2003   5.4  13000   NaN
3  2011   2.2  15000   NaN
4  2012   2.7  18500     A
5  2013   5.8  17600     C
6  2014   6.7  16500     B
7  2015   4.6  19340     B
'''
~~~

<br>

### right

right값은 두 DataFrame을 merge시 오른쪽 DataFrame에는 있지만 왼쪽 DataFrame에는 없는 행도 같이 병합됩니다. 

~~~python
result3 = pd.merge(df2, df3, how='right')
print(result3)
'''
   Year  Rate    Price Class
0  2012   2.7  18500.0     A
1  2013   5.8  17600.0     C
2  2014   6.7  16500.0     B
3  2015   4.6  19340.0     B
4  2008   1.8      NaN     A
5  2009   5.3      NaN     B
6  2010   3.4      NaN     C
7  2011   3.2      NaN     D
'''
~~~

<br>

### on

on속성은 두 DataFrame이 merge할 때 비교 기준을 정할 때 씁니다. 앞서 아무 조건을 주지 않고 merge를 하면 두 DataFrame의 공통된 열에서 완전히 같은 행들만 추출이 되었습니다. 

on은 속성값으로 공통된 열중에서 하나를 지정하고 그 열에서 서로 같은 데이터를 가진 행들을 추출합니다. 

~~~python
result3 = pd.merge(df2, df3, on='Year')
print(result3)
'''
   Year  Rate_x  Price  Rate_y Class
0  2011     2.2  15000     3.2     D
1  2012     2.7  18500     2.7     A
2  2013     5.8  17600     5.8     C
3  2014     6.7  16500     6.7     B
4  2015     4.6  19340     4.6     B
'''
~~~

how는 기본값인 inner로 설정되었습니다. on을 Year로 설정했기 때문에 df2와 df3의 Year 열에서 2011년부터 2015년이 똑같이 있기 때문에 2011~2015행들을 inner merge시켰습니다. 여기서 다른 공통열 Rate를 _x, _y를 통해 구분되어 출력해줍니다. 

잘 보면 2011년의 Rate_x와 Rate_y가 다른 것을 확인할 수 있습니다. 