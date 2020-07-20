---
layout: post
title: "DataFrame groupby"
date: 2020-07-16
desc: "DataFrame groupby"
keywords: python, pandas, grouped, groupby,  
categories: [Data_analysis]
tags: [python, pandas, NaN]
---

## groupby

___

데이터를 그룹화(범주화)하는 일은 통계자료에서 굉장히 빈번합니다. 그룹핑을 시켜서 데이터의 합을 구하거나 평균치를 구하는 일을 합니다. 

~~~python
np.random.seed(100)
df1 = DataFrame(dict(Gender=['Female','Male','Female','Male','Female','Male','Female','Female'],
                    Smoking=['Smoker','Smoker','Smoker','Non-Smoker','Non-Smoker','Non-Smoker','Non-Smoker','Smoker'],
                    CountA=np.random.randint(1,10,8),
                    CountB=np.random.randint(1,10,8)))
print(df1)
'''
   Gender     Smoking  CountA  CountB
0  Female      Smoker       9       6
1    Male      Smoker       9       3
2  Female      Smoker       4       3
3    Male  Non-Smoker       8       3
4  Female  Non-Smoker       8       2
5    Male  Non-Smoker       1       1
6  Female  Non-Smoker       5       9
7  Female      Smoker       3       5
'''
~~~

<br>

### 컬럼으로 그룹화하기

groupby의 속성 by에 그룹화 하고 싶은 컬럼명을 리스트형태로 넣습니다. groupby함수를 적용한 후에 반드시 통계함수를 적용해야 합니다. 

~~~python
result = df1.groupby(by=['Smoking']).sum()
print(result)
'''
            CountA  CountB
Smoking                   
Non-Smoker      22      15
Smoker          25      17
'''

result = df1.groupby(by=['Smoking', 'Gender']).sum()
print(result)
'''
                   CountA  CountB
Smoking    Gender                
Non-Smoker Female      13      11
           Male         9       4
Smoker     Female      16      14
           Male         9       3
'''
~~~

<br>

groupby로 묶여진 객체에 agg()함수를 통해 통계함수들을 여러개 적용할 수 있습니다. 

~~~python
result = df1.groupby(by=['Smoking', 'Gender']).agg(['sum', 'mean', 'count'])
print(result)
'''
                  CountA                 CountB                
                     sum      mean count    sum      mean count
Smoking    Gender                                              
Non-Smoker Female     13  6.500000     2     11  5.500000     2
           Male        9  4.500000     2      4  2.000000     2
Smoker     Female     16  5.333333     3     14  4.666667     3
           Male        9  9.000000     1      3  3.000000     1
'''
~~~