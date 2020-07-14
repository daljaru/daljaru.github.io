---
layout: post
title: "Numpy 배열 초기화"
date: 2020-07-12
desc: "Numpy Array Initialization"
keywords: numpy, array, initialization
categories: [Data_analysis]
tags: [numpy, array, initialization]
---

## Numpy Array Initialization

___

Numpy Array를 초기화하는 방법은 array()함수를 쓰는 것 외에도 여러가지가 있습니다. 

### zeros(value)

~~~python
import numpy as np

az = np.zeros(10)
print(az)

'''
출력
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
'''
~~~

<br>

### ones(value)

~~~python
import numpy as np

ao = np.ones(10)
print(ao)

'''
출력
[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
'''
~~~

<br>

### zeros(value)+value

~~~python
import numpy as np

am = np.zeros(10)+3
print(am)

'''
출력
[3. 3. 3. 3. 3. 3. 3. 3. 3. 3.]
'''
~~~

<br>

### eye(value)

~~~python
import numpy as np

ae = np.eye(3)
print(ae)

'''
출력
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''
~~~

<br>

### arange(start, end, step)

~~~python
import numpy as np

print(np.arange(10,3,-2))

'''
출력
[10  8  6  4]
'''
~~~

<br>

### full(shape, value, dtype)

~~~python
import numpy as np

print(np.full((4,4),5))
print(np.full((4,4),-11.0,dtype='int32'))

'''
출력
[[5 5 5 5]
 [5 5 5 5]
 [5 5 5 5]
 [5 5 5 5]]
[[-11 -11 -11 -11]
 [-11 -11 -11 -11]
 [-11 -11 -11 -11]
 [-11 -11 -11 -11]]
'''
~~~