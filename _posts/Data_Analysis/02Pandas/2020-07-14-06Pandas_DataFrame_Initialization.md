---
layout: post
title: "DataFrame Initialization"
date: 2020-07-14
desc: "DataFrame Initialization"
keywords: python, pandas, DataFrame, read_csv, read_excel
categories: [Data_analysis]
tags: [python, pandas, DataFrame, read_csv, read_excel]
---

## DataFrame

___

DataFrame은 Pandas라이브러리에서 제공하는 2차원 배열형식의 자료구조입니다. 표같은 스프레드시트 구조와 비슷합니다. 여러개의 컬럼을 가지고 서로 다른 구조의 값이 담깁니다.

DataFrame은 다양한 방법으로 생성할 수 있습니다. 

1. 리스트 값을 딕셔너리로 사용하는 방법. 


2. Numpy 배열을 이용하는 방법.


3. read_csv(), read_excel()등을 이용해서 외부 파일을 읽어오는 방법.

<br>

### 딕셔너리를 이용해서 DataFrame 생성

~~~python
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

list_dic=dict(state=['Ohio','Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'], year=[2000,2001,2002,2001,2002,2003], pop=[1.5,1.4,2.3,1.2,1.4,2.4])
listDf = DataFrame(list_dic)
listDf
'''
	state	year	pop
0	Ohio	2000	1.5
1	Ohio	2001	1.4
2	Ohio	2002	2.3
3	Nevada	2001	1.2
4	Nevada	2002	1.4
5	Nevada	2003	2.4
'''

print(listDf.state)
'''
0      Ohio
1      Ohio
2      Ohio
3    Nevada
4    Nevada
5    Nevada
Name: state, dtype: object
'''

print(type(listDf.state))
'''
<class 'pandas.core.series.Series'>
'''
~~~
pandas의 각 열을 조회해서 타입을 출력하면 Series가 뜨는 것을 확인 할 수 있습니다. 

<br>

### numpy를 이용해서 DataFrame 생성

~~~python
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

df2 = DataFrame(np.random.randint(10,100,16).reshape(4,4),index=list('abcd'), columns=list('ABCD'))
df2
'''
A	B	C	D
a	18	34	77	97
b	89	58	20	62
c	63	76	24	44
d	34	25	70	68
'''
~~~

<br>

### read_csv()를 이용해서 DataFrame 생성

csv(comma seperated value)는 데이터 값이 쉼표로 구분되는 텍스트 파일입니다. 

~~~python
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

df3 = pd.read_csv('../data/tips.csv')
df3
'''
	total_bill	tip	sex	smoker	day	time	size
0	16.99	1.01	Female	No	Sun	Dinner	2.0
1	10.34	1.66	Male	No	Sun	Dinner	3.0
2	21.01	3.50	Male	No	Sun	Dinner	3.0
3	23.68	3.31	Male	No	Sun	Dinner	2.0
4	24.59	3.61	Female	No	Sun	Dinner	4.0
...	...	...	...	...	...	...	...
240	27.18	2.00	Female	Yes	Sat	Dinner	2.0
241	22.67	2.00	Male	Yes	Sat	Dinner	2.0
242	17.82	1.75	Male	No	Sat	Dinner	2.0
243	18.78	3.00	Female	No	Thur	Dinner	2.0
244	25.34	NaN	NaN	NaN	NaN	NaN	NaN
'''
~~~