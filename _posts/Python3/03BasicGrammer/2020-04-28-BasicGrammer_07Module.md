---
layout: post
title: "Module programming"
date: 2020-04-28
desc: "module programming is essential."
keywords: module, function, import, package, from
categories: [Python3]
tags: [python3,module, package]
---

## 모듈(Module)에 대해서

잠시 쉬어갈겸 **모듈**로 프로그래밍을 하는 방법에 대해 알아보겠습니다. **모듈이란 파이썬 함수나 클래스들을 모아놓은 파일**을 말합니다. 우리는 이제까지 짧은 프로그램 예시를 만들었기 때문에 파일을 체계적으로 만들지는 않았습니다. 하지만 앞으로 클래스나 함수를 배우면서 우린 파일관리를 체계적으로 하며 코딩하는 방법을 알게 될 것입니다. 

좀 긴 프로그램을 쓰고자 한다면, 대신 인터프리터 입력을 편집기를 사용해서 준비한 후에 그 파일을 입력으로 사용해서 실행하는 것이 좋습니다. 이렇게 하는 것을 **스크립트**를 만든다고 합니다.

만약 우리가 정수값이 들어있는 리스트의 총합과 평균을 구하는 **함수**나 혹은 쓸만한 **클래스**들을 재사용하고 싶다면 스크립트를 만들고 **메인 모듈로 불러와서 쉽게 사용할 수 있습니다.** (Import)라고 말합니다. 

~~~python
import testModule #import를 하자. 
~~~

import를 할 때 위와같이 **import 키워드**를 사용합니다.

~~~python
if __name__ == '__main__': #__name__은 Python의 특별한 변수명입니다.
    
#import하는 모듈이 없을때 __name__에는 __main__이 들어갑니다. 그리고 if조건문 안에 있는 코드가 실행됩니다
#모듈 자기자신이 import가 될때 모듈의 이름이 __name__으로 들어가게 됩니다. 그렇기 때문에 if조건문 안에 있는 코드가 실행이 되지 않습니다. 
~~~



무슨 말인지 코드를 작성하며 알아볼까요. <br>Pycharm에서 다른 Python파일을 하나 만들겠습니다.(다른 모듈을 만드는 것입니다.)<br>이름은 testModule.py라고 하고 아래와 같이 쓰겠습니다.

~~~python
# 두 인자를 받아 더해서 출력하는 함수
def add(num1, num2):
    return print(num1 +num2)

print(100)
~~~

이제 메인 모듈을 아래와 같이 수정합니다. 

~~~python
import testModule

if __name__ == '__main__':
    testModule.add(10, 20)
    print(1000)
~~~

실행해보면 아래와 같이 100과 1000이 뜨는 것을 확인할 수 있습니다. 

.![module](/static/assets/img/blog/python3/03BasicGrammer/module.png)



 조금 곤란합니다. 우리는 단지 **testModule모듈의 add함수**와 **메인모듈의 print(1000)**만 사용하고 싶었습니다. 그런데 import만 해도 testModule모듈의 print(100)까지 출력됩니다.  이유를 아시겠나요? 인터프리터가 testModule모듈을 import하는 것과 상관없이 `__name__`에(코드가 명시적으로 적혀있지는 않습니다만) `__main__`을 넣어버렸기 때문입니다.

이런 경우를 방지하기 위해 testModule모듈을 아래와 같이 수정합니다. 

~~~python
# 두 인자를 받아 더해서 출력하는 함수
def add(num1, num2):
    return print(num1 +num2)

if __name__ == '__main__':
	print(100)
~~~

이제 메인모듈을 실행하면 아래와 같은 결과가 뜹니다. 

.![moduleResult](/static/assets/img/blog/python3/03BasicGrammer/moduleResult.png)

 드디어 100이 출력되지 않게 할 수 있었네요. 저렇게 testModule모듈안에 `if __name__ == '__main__'`을 넣으면 외부에서 해당 모듈을 import할 때 `__name__`에 `__main__`대신 모듈의 이름(여기서는 testModule)를 넣어버립니다. 그래서 if 조건문 아래의 내용이 실행되지 않는 것이죠.



 import가 너무 쓸데 없어 보이나요? 고작 add함수를 쓰려고 저랬다니..... 하지만 실제로 데이터 분석 분야의 코딩을 하면 매우 많은 라이브러리들을 import하는 것을 확인 할 수 있습니다. 

예시) keras에서 샴 비전모델(공유 합성곱 기반 층)을 구현하는 예

~~~python
from keras import layers
from keras import applications
from keras import Input

xception_base = applications.Xception(weights=None, include_top = False)

left_input = Input(shape=(250, 250, 3))
right_input = Input(shape=(250, 250, 3))

left_features = xception_base(left_input)
right_features = xception_base(right_input)

merged_features = layers.concatenate([left_features, right_features], axis=-1)
~~~

 이렇게 외부파일을 끌어다 쓰는 건 프로그래밍에서는 비일비재한 일입니다. python만의 전유물도 아닙니다. C++, Java, Ruby, kotlin등등 많은 프로그래밍 언어들이 이러한 임포트 방식으로 코딩을 하고 우리가 쓰는 앱과 프로그램을 만듭니다.



## 패키지(Package)

 위의 예시에서 import앞에 있는 **from키워드**가 보이시나요. from뒤에는 패키지명이 들어갑니다. 

 실제 컴퓨터환경에서는 그저 폴더하나입니다. 자료들을 묶어서 정리하고 싶다면 패키지를 활용하는 것도 좋은 방법입니다. Pycharm에서는 new -> Python package를 클릭하여 생성할 수 있습니다. 자신이 원하는 공간을 만들고 원하는 **모듈들**을 넣어서 프로그램들을 관리할 수 있습니다.







## 대표적인 모듈 Math, Random, Statistics

파이썬 입문자들이 자주 쓰고, 그리고 알고리즘 문제를 풀 때 자주 쓰는 모듈은 대표적으로 [Math](https://docs.python.org/ko/3/library/math.html?highlight=math#module-math), Random, Statistics가 있습니다.

**Math Module**는 팩토리얼, 제곱근, 지수계산, 최소공배수등을 지원합니다. 

```python
import math

if __name__ == '__main__':
    num1 = math.pow(2, 3)
    print(num1) #8.0
    
    num2 = math.gcd(450,434220)
    print(num2) #30
    
    num3 = math.sqrt(36)
    print(num3) #6.0
    
    num4 = math.factorial(5)
    print(num4) #120
```



**Random Module**은 여러가지 방법으로 유사 랜덤 숫자를 발생시킵니다. 

~~~python
import random

if __name__ == '__main__':
    times = 5;

    while(times > 0):
        num1 = random.randrange(0, 10);
        print(num1)
        times -= 1
#0부터 9사이의 숫자를 5번 랜덤하게 발생하는 코드
~~~

~~~python
import random

if __name__ == '__main__':
    testList = [1,2,3,4,5,6,7,8];

    print("origin List : ", end = '')
    print(testList)  #Original
    
    num = random.choice(testList)
    print(num) #무작위로 하나 고르기

    templist = random.choices(testList, k=5)
    print(templist) #무작위로 k개만큼 고르기

    random.shuffle(testList)
    print(testList) #섞기
~~~



**Statistics Module**에는 평균, 중간값, 1,3사분위수, 표준편차 등 각종 통계관련 함수들이 모여있습니다. 

```python
import statistics as st

if __name__ == '__main__':
    testList = [1,4,12,16,38]
    result = st.mean(testList)
    print(result)  #평균

    result = st.median(testList)
    print(result) #중간값

    result = st.pstdev(testList)
    print(result) #모집단의 표준편차..
```