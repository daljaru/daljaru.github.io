---
layout: post
title: "Object"
date: 2020-05-07
desc: "Python is composed of objects"
keywords: OOP, object, method, attribute, instance
categories: [Python3]
tags: [python3,object, oop, method, attribute, instance]
---

## Object Oriented Language(객체지향 언어)

파이썬은 **객체지향언어**입니다. 영어로는 Object Oriengted Language라고 합니다. 

객체지향 언어가 무슨 말일까요? 이 개념을 정확하게 알려면 우선 Object(객체)라는 개념부터 정확히 짚고 넘어가야 합니다. 

### 객체의 정의

> 상태 (**Attribute**나 **Value**) 를 갖고 동작 (**Method**) 이 함께 정의된 모든 데이터.

그 동안 자주 봤던 개념들이 보이네요. 앞서 파이썬의 기본적인 문법을 공부하면서 우린 **값**과 **메소드(함수)**라는 개념을 자주 사용했습니다.

~~~python
def add(num1, num2):
    return num1 + num2

if __name__ == '__main__':
    num1 = 1
    num2 = 2
    print(add(num1, num2))  #3
~~~

 우린 num1 변수에 값 1과 num2변수에 값 2를 지정하고 add()함수를 이용해  두 숫자를 더했습니다. 이렇게 우리는 값과 함수를 각각 만들어서 썼습니다. 

 객체는 이런 값과 함수들을 동시에 묶어 놓은 데이터묶음이라고 쉽게 개념적으로 생각할 수 있습니다.



##### 조금 쉬운 비유 

**계산기**에 비유를 하자면 계산기에는 **값을 입력** 받을 수 있는 버튼들이 있고 **사칙연산을 계산**할 수 있는 버튼도 모여있습니다.  숫자 1,2,3... 등의 버튼을 눌러서 값을 지정할 수 있고 +, - 버튼을 눌러서 연산을 수행할 수 있습니다. 

 이 비유에서  바로 '**계산기**'가 객체가 되고 Attribute(혹은 Value)는 숫자 Method(동작)은 사칙연산입니다.  



##### 약간 어려운 비유

염색체에 비유해봅시다. 염색체는 DNA와 히스톤 단백질로 이루어져 있습니다. 사람의 염색체는 총 46개이며 23쌍으로 이루어져 있습니다. 염색체는 염색사로 풀어질 수 있고 세포 분열시 DNA가 복제되고 염색사가 염색체로 응축됩니다. 

 이 비유에서 '**염색체**'가 객체가 되고 Attribute(혹은 Value)는 **DNA**와 **히스톤 단백질**, **염색체의 개수**, **쌍의 개수**입니다. Method(동작)은 **DNA복제**, **염색체로 응축**이 됩니다. 



### Instance(인스턴스)의 정의

인스턴스는 '객체'라는 개념적인 틀에 구체적인 데이터(빈 데이터 포함)가 들어간 것입니다. 

##### 조금 쉬운 비유

**계산기**비유에서 만약 계산기의 브랜드 명을 명시할 수 있는 객체라면 '계산기'라는 객체를 가지고 **Casio 계산기**라는 인스턴스를 만들 수 있습니다. 또 **Sharp 계산기**라는 인스턴스를 만들 수 있습니다. (Casio와 Sharp는 현재 공학용 계산기 브랜드 1, 2위입니다.)



**카페**라는 객체가 있다고 해봅시다. 위와 비슷하게 카페라는 객체를 가지고 구체적인 값을 넣어준다면 우린 **스타벅스 카페**, **커피빈 카페**등을 만들 수 있습니다. 



클래스는 개념적, 인스턴스는 실제적인 것이라고 생각하면 좋습니다. 



### **파이썬은 모든 것이 객체입니다.** 

 우리가 그동안 너무 당연하게 썼지만 사실 객체였던 것이 있습니다. 

~~~python
if __name__ == '__main__':
    num1 = 1
    num2 = 2.5
    testString = 'hello'
    
    print(type(num1)) #<class 'int'>
    print(type(num2)) #<class 'float'>
    print(type(testString)) #<class 'str'>
~~~

여기서 `class`는 '객체'라는 개념적인 용어를 파이썬에서 코드로 구현할 때 쓰는 키워드입니다. '보통 클래스를 구현한다.' 그리고 '클래스를 이용해서 객체를 생성한다.' 라고 말합니다. 

1, 2.5, 'hello'모두 각각 int, float, str**객체**로 만든 **인스턴스**인 것을 확인할 수 있고 이 객체를 각각 num1, num2, testString이라는 변수로 지정했습니다. 

 

**Pycharm**에서 메소드 확인하기

.![strMethod](/static/assets/img/blog/python3/04BasicClass/strMethod.png)

testString 뒤에 .을 붙이면 위 사진과 같이 여러개의 메소드들이 뜨는 것을 볼 수 있습니다. m이라고 나오나요? str클래스에 rstrip, format등의 메소드들이 정의되어 있다는 뜻입니다.



~~~python
if __name__ == '__main__':
    list1 = [1,2,3,4,5]
    print(type(list1))  #<class 'list'>
    
    print(list1.pop(3))  #4
~~~

리스트도 객체인 것을 확인 할 수 있습니다.





### 객체지향언어의 쓰임

객체지향 언어는 이렇게 **값와 메소드**를 **객체라는 묶음**으로 만들어서 프로그래밍을 할 수 있게 만들어진 언어입니다. 대표적으로 Java와 C++이 있습니다. Python과 Java, C++로 프로그래밍을 할 때에는 코딩을 할 때 항상 객체를 활용할 수 있게 만들어야 합니다. 

객체지향 언어와 자주 비교되는 언어로 '절차지향 언어'가 있습니다. 대표적인 언어가 C입니다. 절차지향 언어는 클래스로 묶어서 프로그래밍을 하지 않습니다. 이제까지 우리가 해왔던 것처럼 필요한 함수를 만들어서 선언하고 순차적으로 코드가 실행됩니다.  

 이제까지 우리는 Python에 있는 내장클래스와 내장 메소드를 사용하는 것으로 객체지향프로그래밍을 간접적으로 알아봤습니다. 이제는 우리가 직접 클래스를 만들어서 사용해보도록 합시다. 
