---
layout: post
title: "Numpy Random
date: 2020-07-12
desc: "Generate Random Number"
keywords: numpy, randint, randn, randrange
categories: [Data_analysis]
tags: [numpy, randint, randn, randrange]
---

## Numpy Randome Module

___

Numpy의 random모듈(서브패키지)에는 난수를 생성하는 다양한 함수들이 존재합니다. 그 중에서 가장 많이 사용되는 3가지를 정리해보았습니다. 

<br>

## rand(row, col)

~~~python
import numpy as np

a = np.random.rand(2,5)
print(a)
print(type(a))

'''
0~1사이의 실수값을 반환 - rand(행, 열)

[[0.80306318 0.57553494 0.09794534 0.36055787 0.70541897]
 [0.13541828 0.40088818 0.06587423 0.25068831 0.23445649]]
<class 'numpy.ndarray'>
'''
~~~

<br>

## randn(d0, d1, ..., dn)

~~~python
import numpy as np

test = np.random.randn(3,6)
print(test)

'''
가우시안 정규분포값을 랜덤하게 반환.

[[ 0.3351595  -2.4747068  -1.02648842 -0.40648476 -2.8249841  -0.80974402]
 [-1.87516334 -2.23693565  0.138042    1.21586366 -0.38712595 -0.42160231]
 [-0.41451907  0.78348981 -1.03663163  0.25960017 -0.8042373   0.58684031]]
'''
~~~

<br>

## randint(low, high=None, size=None, dtype='l')

~~~python
import numpy as np

b=np.random.randint(2, 9,size=9)
b
print(b)
'''
[8 6 6 3 3 5 4 2 7]
'''
~~~

<br>

## seed(self, seed=None)

특정한 시작 숫자(Seed Number)를 제공해서 난수를 발생시킵니다. 고정적인 난수가 발생합니다. 즉 실행할 때마나 난수값이 바뀌지 않기 때문에 분석결과를 확인하는데 용이합니다. Seed값은 한 번만 정해주면 계속 유지된다.

~~~python
import numpy as np

np.random.seed(404)  #seed 값을 설정했으므로 이후 일정한 랜덤숫자가 나오게 된다. 
arr3 = np.random.randn(4,4)
print(arr3)
'''
[[-1.18269089  1.33746165 -0.31430504  0.5566431 ]
 [-0.20929933 -0.01180037  1.23493345 -0.04341894]
 [-0.68178724  1.20069197  1.34394438 -0.834109  ]
 [ 1.0359977   1.6657991   0.94947856  1.06700952]]
'''
~~~