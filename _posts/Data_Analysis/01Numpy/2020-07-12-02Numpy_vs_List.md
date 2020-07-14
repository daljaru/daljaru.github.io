---
layout: post
title: "Numpy 배열과 List 비교"
date: 2020-07-12
desc: "Comparison Numpy with list"
keywords: numpy, array, list
categories: [Data_analysis]
tags: [numpy, array, list]
---

## Numpy Array vs List

___

numpy array는 array()를 사용합니다. 리스트는 list()를 사용합니다. 

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

리스트는 출력결과가 `[]`안에 요소들이 `,`로 구분이 되어 나타나고 Numpy배열은 출력결과가`[]`안에 요소들이 `,`로 구분되지 않습니다. Numpy배열은 ndarray객체 타입으로 나옵니다. ndarray객체는 다차원 행렬구조를 지원하는 numpy의 핵심클래스입니다. 

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

<br>

### Data Type

~~~python
L = [1,2,3,4,'5',6,7,8,9]
A = np.array([1,2,3,'4',6,7,8,'9'])
B = np.array([1,2,3,4,5,6.4,8.7])
print(L)
print(A)
print(B)
'''
출력
[1, 2, 3, 4, '5', 6, 7, 8, 9] -> 리스트는 숫자와 문자가 섞여져서 들어갈 수 있다. 
['1' '2' '3' '4' '6' '7' '8' '9'] -> 숫자가 문자열로 변함
[1.  2.  3.  4.  5.  6.4 8.7]  -> 숫자가 실수형으로 변함
'''
~~~

<br>

### dtype

값의 타입을 명시할 수도 있다. dtype 속성을 사용한다.(int32, int64, float32, float64)

~~~python
C = np.array([1.0,2.0,3.0,4.0], dtype='int32')
print(C)
'''
출력
[1 2 3 4]
'''
~~~