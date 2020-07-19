---
layout: post
title: "DataFrame 조회"
date: 2020-07-14
desc: "DataFrame 조회"
keywords: python, pandas, DataFrame, head, tail, info, shape
categories: [Data_analysis]
tags: [python, pandas, DataFrame, head, tail, info, shape]
---

### tail

tail()함수는 인자값을 주지 않으면 제일 끝에서 5개의 행을 보여줍니다. 인자값을 원하는 숫자로 주면 해당 숫자만큼 의 행을 데이터의 뒤에서부터 잘라서 보여줍니다. 

~~~python
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

df3 = pd.read_csv('../data/tips.csv')
df3.tail()

'''
    total_bill	tip	sex	smoker	day	time	size
240	27.18	2.00	Female	Yes	Sat	Dinner	2.0
241	22.67	2.00	Male	Yes	Sat	Dinner	2.0
242	17.82	1.75	Male	No	Sat	Dinner	2.0
243	18.78	3.00	Female	No	Thur	Dinner	2.0
244	25.34	NaN	NaN	NaN	NaN	NaN	NaN
'''
~~~

<br>

### head()

head()함수는 인자값을 주지 않으면 제일 앞에서 5개의 행을 보여줍니다. 인자값을 원하는 숫자로 주면 해당 숫자만큼 의 행을 데이터의 앞에서부터 잘라서 보여줍니다. 

~~~python
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

df3 = pd.read_csv('../data/tips.csv')
df3.head()

'''
    total_bill	tip	sex	smoker	day	time	size
0	16.99	1.01	Female	No	Sun	Dinner	2.0
1	10.34	1.66	Male	No	Sun	Dinner	3.0
2	21.01	3.50	Male	No	Sun	Dinner	3.0
3	23.68	3.31	Male	No	Sun	Dinner	2.0
4	24.59	3.61	Female	No	Sun	Dinner	4.0
'''
~~~

<br>

### info()

info()함수는 데이터프레임의 기본적인 정보를 보여줍니다. 각 컬럼, 커럼의 타입, NaN이 아닌 행의 개수를 보여줍니다. 

~~~python
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

df3 = pd.read_csv('../data/tips.csv')
df3.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 245 entries, 0 to 244
Data columns (total 7 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   total_bill  245 non-null    float64
 1   tip         244 non-null    float64
 2   sex         244 non-null    object 
 3   smoker      244 non-null    object 
 4   day         244 non-null    object 
 5   time        244 non-null    object 
 6   size        244 non-null    float64
dtypes: float64(3), object(4)
memory usage: 13.5+ KB
'''
~~~