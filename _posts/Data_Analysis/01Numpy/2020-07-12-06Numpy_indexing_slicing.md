---
layout: post
title: "Numpy Indexing and Slicing"
date: 2020-07-12
desc: "Numpy Indexing and Slicing"
keywords: numpy, ndarray, indexing, slicing, where, axis
categories: [Data_analysis]
tags: [numpy, ndarray, indexing, slicing, where, axis]
---

## 1 Dimension에서 Indexing과 Slicing

___

인덱스가 0부터 length-1까지 있고, 뒤에서부터 접근할 때는 -를 붙여준다. `:`를 기준으로 Slicing을 진행할 때 오른쪽 인덱스는 포함하지 않는다.

~~~python
import numpy as np

narray = np.arange(5)  #[0 1 2 3 4]

print(narray[-1], narray[-1])
print(narray[1:])
print(narray[:])
print(narray[2:4])

'''
4 4
[1 2 3 4]
[0 1 2 3 4]
[2 3]
'''
~~~

<br>

## 2 Dimension에서 Indexing과 Slicing

___

2차원 ndarray타입에서 인덱스는 [, ] 콤마를 기준으로 2개의 인자를 받는다. 앞 인자값은 행의 index, 뒤 인자값은 열의 index를 나타낸다. 

~~~python
import numpy as np

np.random.seed(100)
narray1 = np.random.randint(0,20,16).reshape(4,4)
print(narray1)
'''
[[ 8  3  7 15]
 [16 10  2  2]
 [ 2 14  2 17]
 [16 15  4 11]]
'''

#1. narray1에서 첫번째 줄 7을 가져오려면
print(narray1[0,2])   # ,로 접근
print(narray1[0][2])  # 일반적인 접근

#2. 두번째 라인 [16,10,2,2]을 가져오려면
print(narray1[1])
print(narray1[1,])
print(narray1[1,:])
print(narray1[1,0:4])
print(narray1[1,0:])

#3. 전체행에 대해서 4번재 열만 다 가져오려면
print(narray1[:,3].reshape(4,1))

'''
7
7

[16 10  2  2]
[16 10  2  2]
[16 10  2  2]
[16 10  2  2]
[16 10  2  2]

[[15]
 [ 2]
 [17]
 [11]]
'''
~~~

<br>

## Indexing and Condition Slicing

___

조건을 줘서 특정한 데이터들을 바꾸거나 데이터들을 가져오고 싶을 때 사용합니다. 

~~~python
import numpy as np

np.random.seed(0)
arr3 = np.random.randn(4,4)
print(arr3)

'''
[[ 1.76405235  0.40015721  0.97873798  2.2408932 ]
 [ 1.86755799 -0.97727788  0.95008842 -0.15135721]
 [-0.10321885  0.4105985   0.14404357  1.45427351]
 [ 0.76103773  0.12167502  0.44386323  0.33367433]]
'''

print(arr3[arr3>0])         #0보다 큰 값들을 가져온다. 
print(type(arr3[arr3>0]))   #타입
print(arr3[arr3>0].ndim)    #차원
'''
[1.76405235 0.40015721 0.97873798 2.2408932  1.86755799 0.95008842
 0.4105985  0.14404357 1.45427351 0.76103773 0.12167502 0.44386323
 0.33367433]
<class 'numpy.ndarray'>
1                                   1차원의 ndarray를 반환하게 됐다. 
'''

print(arr3[arr3<0])
'''
[-0.97727788 -0.15135721 -0.10321885]
'''

arr3[arr3<0] = 0      #0보다 작은 데이터를 0으로 초기화 
print(arr3)
'''
[[1.76405235 0.40015721 0.97873798 2.2408932 ]
 [1.86755799 0.         0.95008842 0.        ]
 [0.         0.4105985  0.14404357 1.45427351]
 [0.76103773 0.12167502 0.44386323 0.33367433]]   #초기화만 했기 때문에 2차원으로 출력됨.
'''

#3. where 함수
arr3_1 = np.where(arr3>0, arr3, -1)   #0보다 큰것은 arr3(그대로..) 아니면 -1로 초기화. 
print(arr3_1)
'''
[[ 1.76405235  0.40015721  0.97873798  2.2408932 ]
 [ 1.86755799 -1.          0.95008842 -1.        ]
 [-1.          0.4105985   0.14404357  1.45427351]
 [ 0.76103773  0.12167502  0.44386323  0.33367433]]
'''

a = np.array([[1,2],[3,4],[5,6]])
print(a)
print(a[a>2])
'''
[[1 2]
 [3 4]
 [5 6]]
[3 4 5 6]
'''
~~~


