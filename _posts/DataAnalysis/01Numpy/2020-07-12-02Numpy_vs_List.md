---
layout: post
title: "Numpy 배열과 List 비교"
date: 2020-07-12
desc: "Comparison Numpy with list"
keywords: numpy, array, list
categories: [Data_Analysis]
tags: [numpy, array, list]
---

## Numpy Array vs List

___

numpy array는 array()를 사용합니다. 리스트는 list()를 사용합니다. 
<br>

~~~python
import numpy as np

myList=[4,5,6,7]
print(myList)

myArr=np.array(myList)
print(myArr)

'''
출력
[4, 5, 6, 7]
[4 5 6 7]
'''
~~~
<br>
<br>

리스트는 출력결과가 `[]`안에 요소들이 `,`로 구분이 되어 나타나고 Numpy배열은 출력결과가`[]`안에 요소들이 `,`로 구분되지 않습니다. 

<br>

~~~python
print(type(myList))
print(type(myArr))

'''
출력
<class 'list'>
<class 'numpy.ndarray'>
'''
~~~
<br>
<br>

Numpy배열은 ndarray객체 타입으로 나옵니다. ndarray객체는 다차원 행렬구조를 지원하는 numpy의 핵심클래스입니다. 

<br>

### Slicing

~~~python
myL_sub=myList[1:3]
print(myL_sub)

myA_sub=myArr[1:3]
print(myA_sub)
'''
출력
[5, 6]
[-5  6]
'''
~~~

<br>

### indexing

~~~python

myL_sub[0] = -5
print(myL_sub)

myA_sub[0] = -5
print(myA_sub)

print(myList)
print(myArr)
'''
출력
[-5, 6]
[-5  6]
[4, 5, 6, 7]
[ 4 -5  6  7]
'''
~~~

