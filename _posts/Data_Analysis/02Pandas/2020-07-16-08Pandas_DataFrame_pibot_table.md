---
layout: post
title: "DataFrame pivot_table"
date: 2020-07-16
desc: "DataFrame pivot_table"
keywords: python, pandas, DataFrame, pivot_table, index, columns, values
categories: [Data_analysis]
tags: [python, pandas, DataFrame, pivot_table, index, columns, values]
---

## Pivot Table

___

pivot은 영어로 '축을 중심으로 회전하다' 라는 뜻을 가지고 있습니다. DataFrame에서 pivot_table의 의미는 컬럼과 인덱스를 자유자재로 회전시키며 DataFrame의 형태를 바꾸는 것을 의미합니다. 

DataFrame객체의 pivot_table()함수를 사용합니다. pivot_table()함수에서 가장 중요한 속성은 바로 values, index, columns, aggfuncs입니다. 

values는 컬럼 중에서 새로운 DataFrame의 내용으로 만들 컬럼을 바인딩합니다.

index는 컬럼 중에서 index로 만들고 싶은 컬럼을 리스트 형태로 속성값으로 바인딩합니다.

columns는 선택 한 데이터를 다시 특정한 컬럼의 주제로 나누고 싶을 때 컬럼명을 속성 값으로 바인딩합니다.  

aggfunc은 통계데이터를 넣습니다. pivot_table함수는 DataFrame을 재정렬하고 특정한 컬럼 데이터로 DataFrame을 만드는 것이기 때문에 groupby함수처럼 꼭 통계함수를 적용해줘야 합니다.

<br>

## pivot_table()

> df.pivot_table(
    values=None,
    index=None,
    columns=None,
    aggfunc='mean',
    fill_value=None,
    margins=False,
    dropna=True,
    margins_name='All',
    observed=False,
) -> 'DataFrame'
> 
> Docstring:<br> 
> Create a spreadsheet-style pivot table as a DataFrame.
> 
> The levels in the pivot table will be stored in MultiIndex objects(hierarchical indexes) on the index and columns of the result DataFrame.

<br>

### Parameters
----------
> **values** : column to aggregate, optional<br>
> index : column, Grouper, array, or list of the previous
    If an array is passed, it must be the same length as the data. The list can contain any of the other types (except list).<br>
    Keys to group by on the pivot table index.  If an array is passed,it is being used as the same manner as column values. <br>
> 
> **columns** : column, Grouper, array, or list of the previous
    If an array is passed, it must be the same length as the data. The list can contain any of the other types (except list).<br>
    Keys to group by on the pivot table column.  If an array is passed, it is being used as the same manner as column values.
> 
> **aggfunc** : function, list of functions, dict, default numpy.mean
    If list of functions passed, the resulting pivot table will have hierarchical columns whose top level are the function names (inferred from the function objects themselves)<br>
    If dict is passed, the key is column to aggregate and value
    is function or list of functions.
> 
> **fill_value** : scalar, default None<br>
Value to replace missing values with.
> 
> **margins** : bool, default False<br>
    Add all row / columns (e.g. for subtotal / grand totals).
> 
> **dropna** : bool, default True<br>
    Do not include columns whose entries are all NaN.
> 
> **margins_name** : str, default 'All'<br>
    Name of the row / column that will contain the totals
    when m  argins is True.
> 
> **observed** : bool, default False<br>
    This only applies if any of the groupers are Categoricals.<br>
    If True: only show observed values for categorical groupers.
    If False: show all values for categorical groupers.<br>

>   .. versionchanged:: 0.25.0
 
### Returns

-------

> DataFrame
    An Excel style pivot table.

<br>

## 예시

___

~~~python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt


data = {
    "도시":['서울','서울','서울','부산','부산','부산','인천','인천'],
    "연도":["2015","2010","2005","2015","2010","2005","2015","2010"],
    "인구":[9904312, 963148, 976254, 34487,333231,300231,2890564,257812],
    "지역":['수도권','수도권','수도권','경상권','경상권','경상권','수도권','수도권']
}
df = DataFrame(data)
df
'''
   도시    연도       인구   지역
0  서울  2015  9904312  수도권
1  서울  2010   963148  수도권
2  서울  2005   976254  수도권
3  부산  2015    34487  경상권
4  부산  2010   333231  경상권
5  부산  2005   300231  경상권
6  인천  2015  2890564  수도권
7  인천  2010   257812  수도권
'''
~~~

위 DataFrame을 가지고 pivot_table()함수를 써보겠습니다. 

<br>

#### '도시'를 index로, '인구'를 values로. 

~~~python
print(df.pivot_table(index=['도시'], values='인구')) #aggfunc의 default는 mean함수.
'''
             인구
도시              
부산  2.226497e+05
서울  3.947905e+06
인천  1.574188e+06
'''
~~~

<br>

#### '도시'를 index로, '인구'를 values로, '연도'를 columns로.

~~~python
print(df.pivot_table(index=['도시'], columns='연도', values='인구'))
'''
연도      2005      2010       2015
도시                               
부산  300231.0  333231.0    34487.0
서울  976254.0  963148.0  9904312.0
인천       NaN  257812.0  2890564.0
'''
~~~

<br>

#### '도시','지역'을 index로, '인구'를 values로.

~~~python
print(df.pivot_table(index=['도시','지역'], values='인구'))
'''
                  인구
도시 지역               
부산 경상권  2.226497e+05
서울 수도권  3.947905e+06
인천 수도권  1.574188e+06
'''
~~~

<br>

#### '도시','지역'을 index로, '인구'를 values로, '연도'를 columns로.

~~~python
print(df.pivot_table(index=['도시','지역'], columns='연도', values='인구'))
'''
연도          2005      2010       2015
도시 지역                                
부산 경상권  300231.0  333231.0    34487.0
서울 수도권  976254.0  963148.0  9904312.0
인천 수도권       NaN  257812.0  2890564.0
'''
~~~

위의 예시와 같이 기존의 DataFrame을 자유자재로 변형할 수 있다.

