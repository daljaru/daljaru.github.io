---
layout: post
title: "DataFrame numeric function"
date: 2020-07-16
desc: "DataFrame numeric function"
keywords: python, pandas, DataFrame, sum, mean, count, value_counts
categories: [Data_analysis]
tags: [python, pandas, DataFrame, sum, mean, count, value_counts]
---

## sum

___

sum함수는 숫자데이터에만 적용되는 함수입니다. 해당하는 컬럼의 합을 구해줍니다. 

~~~python
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

df = pd.read_csv('../data/tips.csv',encoding='utf-8')
print(df.head())
'''
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner   2.0
1       10.34  1.66    Male     No  Sun  Dinner   3.0
2       21.01  3.50    Male     No  Sun  Dinner   3.0
3       23.68  3.31    Male     No  Sun  Dinner   2.0
4       24.59  3.61  Female     No  Sun  Dinner   4.0
'''

print(df['tip'].sum())
'''
731.5799999999999
'''

print(df.groupby(by=['smoker']).sum())
'''
        total_bill     tip   size
smoker                           
No         2897.43  451.77  403.0
Yes        1930.34  279.81  224.0
'''
~~~

<br>

## mean

___

mean 함수는 숫자데이터에만 적용되는 함수입니다. 해당하는 컬럼의 평균을 구해줍니다. 

~~~python
print(df['tip'].mean())
'''
2.9982786885245902
'''

print(df.groupby(by=['smoker']).mean())
'''
        total_bill       tip      size
smoker                                
No       19.188278  2.991854  2.668874
Yes      20.756344  3.008710  2.408602
'''
~~~

<br>

## count

___

count()함수는 해당하는 컬럼의 데이터의 개수를 구합니다. 

~~~python
print(df['tip'].count())
'''
244
'''

print(df.groupby(by=['smoker']).count())
'''
        total_bill  tip  sex  day  time  size
smoker                                       
No             151  151  151  151   151   151
Yes             93   93   93   93    93    93
'''
~~~

<br>

## value_counts

___

value_counts함수는 각각의 컬럼에서 그 값이 몇번 나왔는지 세줍니다. 

~~~python
print(df['tip'].value_counts())
'''
2.00    33
3.00    23
4.00    12
5.00    10
2.50    10
        ..
2.83     1
1.58     1
3.71     1
3.35     1
2.18     1
Name: tip, Length: 123, dtype: int64
'''

print(df['sex'].value_counts())
'''
Male      157
Female     87
Name: sex, dtype: int64
'''
~~~