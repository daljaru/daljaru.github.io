---
layout: post
title: "Numpy Statistics function"
date: 2020-07-12
desc: "Numpy Statistics function"
keywords: sum, mean, min, max, argmin, argmax, cumsum
categories: [Data_analysis]
tags: [sum, mean, min, max, argmin, argmax, cumsum]
---

## Numpy Array statistics function

___

Numpy에서 자주 쓰이는 통계함수 몇개를 알아보겠습니다. 

~~~python
import numpy as np

arr4 = np.random.randint(0,20,16).reshape(4,4)
print(arr4)

'''
[[18  3 17 19]
 [19 19 14  7]
 [ 0  1  9  0]
 [10  3 11 18]]
'''
~~~

<br>

### np.sum

> np.sum(
    a,
    axis=None,
    dtype=None,
    out=None,
    keepdims=<>,
    initial=<>,
    where=<>
)

~~~python
.
.

print(np.sum(arr4))
print(np.sum(arr4, axis=0)) #0이 행들의 합. (각 행마다 있는 데이터를 연산)
print(np.sum(arr4, axis=1)) #1이 열들의 합. (각 열마다 있는 데이터를 연산) 
'''
168
[57 59 10 42]

[47 26 51 44]
'''
.
.
~~~

<br>

### np.cumsum

> np.cumsum(a, axis=None, dtype=None, out=None)

~~~python
.
.
print(np.cumsum(arr4, axis=0))  #0이 행들의 합. (각 행마다 있는 데이터를 차례대로 연산)
print(np.cumsum(arr4, axis=1))  #1이 열들의 합. (각 열마다 있는 데이터를 차례대로 연산)
'''
[[18  3 17 19]   ↓
 [37 22 31 26]   ↓
 [37 23 40 26]   ↓
 [47 26 51 44]]  ↓     

  →  →  →  →
[[18 21 38 57]      
 [19 38 52 59]
 [ 0  1 10 10]
 [10 13 24 42]]
'''
.
.
~~~

<br>

### np.argmax

> np.argmax(a, axis=None, out=None)

~~~python
.
.
print(np.argmax(arr4, axis=0)) #0이 행들을 검사. 각 행들을 검사하여 최대인덱스를 반환
print(np.argmax(arr4, axis=1)) #1이 열들을 검사. 각 열들을 검사하여 최대인덱스를 반환
'''
[1 1 0 0]
[3 0 2 3]
'''
.
.
~~~
