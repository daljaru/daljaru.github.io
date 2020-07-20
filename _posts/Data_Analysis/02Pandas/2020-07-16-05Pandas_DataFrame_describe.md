---
layout: post
title: "describe function"
date: 2020-07-16
desc: "describe function"
keywords: python, pandas, DataFrame, describe
categories: [Data_analysis]
tags: [python, pandas, DataFrame, describe]
---

## describe

describe함수는 데이터에 대한 간단한 통계자료를 내줍니다. 숫자로서 가능한 데이터만 출력합니다. 

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

print(df.describe())
'''
       total_bill         tip        size
count  245.000000  244.000000  244.000000
mean    19.808612    2.998279    2.569672
std      8.891234    1.383638    0.951100
min      3.070000    1.000000    1.000000
25%     13.370000    2.000000    2.000000
50%     17.810000    2.900000    2.000000
75%     24.270000    3.562500    3.000000
max     50.810000   10.000000    6.000000
'''
~~~

