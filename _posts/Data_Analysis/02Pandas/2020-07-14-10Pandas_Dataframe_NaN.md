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

Pandas에서는 null값을 missing data 혹은 missing이라고 부릅니다. missing과 null은 번갈아가며 쓸 수 있지만 pandas의 표준대로 말하자면 missing이 더 잘 쓰입니다. 우리나라 말로는 결측치라고 합니다.

~~~python
from numpy import nan as NA
import pandas as pd
from pandas import DataFrame, Series

df = DataFrame([[1,6.5,3],[NA,NA,NA],[NA,NA,4.6],[NA,6.5,3]])
df
~~~


'''
dropna(): NaN 값이 하나라도 있으면 해당 rwo를 삭제
dropna(how='all') : NaN 값이 하나라도 있으면 해당 row를 삭제.
dropna(how='any') : NaN 값이 하나라도 있으면 해당 row를 삭제.
dropna(thresh=3) : NaN 값이 2개라도 있으면 해당 row를 삭제.

fillna() : 누락된 데이터를 다른 값으로 채움.

isnull()
notnull()
'''
