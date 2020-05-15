---
title: Variable
layout: post
date: '2020-04-23'
desc: "How to write variable with python3"
keywords: variable, python3, namespace, datatype, logical scope, object, memory
categories: [Python3]
tags:
- python3
- variable
- memory
- object
- logical_scope
---

## 숫자를 계산하는 프로그램

~~~python
#두 숫자를 더하는 프로그램
var1 = 10
var2 = 20
var3 = var1 + var2
print(var3)
~~~

~~~python
#두 숫자를 더하는 프로그램
var1, var2 = 10, 20 #이렇게도 적을 수 있습니다. 
var3 = var1 + var2
~~~

 ![plus](/static/assets/img/blog/python3/03BasicGrammer/plus.png)



 Python을 배운지 얼마 되지 않았으므로 아직 배워야할게 많습니다. 위의 코드만 해도 **객체**, **자료형**, **이름공간**에 대해서 기본적으로 알아야 합니다. 더 **깊게** 들어가면 파이썬이 객체를 **메모리에서 생성하는 방식**, **메모리 주소에 있는 데이터 호출 순서**를 알아야합니다.  위 프로그램은 쉬운 프로그램이고 Python이 쉬운 언어라 지금 당장은 무슨 프로그램인지 바로 알 수 있습니다. 

10이라는 정수형 객체에 var1이라는 이름을 붙이고 20이라는 객체에 var2라는 이름을 붙였습니다. 그리고 var1에 있는 객체와 var2에 있는 객체를 더해서 var3라는 변수와 연결했습니다. 마지막으로 print()메소드를 통해 출력을 했습니다. 

## Variable

변수는 **객체을 저장하기 위한 메모리공간**의 별칭입니다. 갑자기 무슨 소리인가 싶을 수도 있는데 이 말을 정확히 이해하려면 컴퓨터의 구조를 아는 것이 좋지만! 너무 깊게 들어가므로.. 간단하게만 적어놓겠습니다. 

우리는 코드에서 단순히 숫자만 적고 끝났지만 사실 python.exe 인터프리터가 코드를 읽고 해석하면서 컴퓨터 내부에서는 다양한 일이 벌어집니다. 

컴퓨터라는 기계는 계산을 하려면 **메모리에 있는 값을 참조**해야합니다. 메모리에서 값을 가져와 CPU가 계산을 진행하고 결과를 다시 메모리에 저장하는 것이죠. 그리고 저장된 결과를 출력장치가 가져가서 바로 Console창에 띄우는 것입니다.  

즉 우리는 10, 20, 30이라는 객체을 저장할 수 있는 공간을 메모리에 확보하고 이 공간을 python언어로 var1, var2, var3라는 변수명으로 지정했습니다. 

~~~python
print(id(var1)) #id()로 객체가 생성된 메모리의 주소를 확인할 수 있다.
print(id(var2))
print(id(var3))
~~~



''**=**'' 문자는 Python에서 **구분자**(delimiter) 중에 하나입니다. = 기호 오른쪽에 있는 **객체**을 왼쪽에 있는 **변수**로 지정합니다. **객체를 변수로 지정하는 것** 혹은 **객체에 '변수명'이라는 이름을 붙이는 것**을 "**Binding**(바인딩)한다"라고 부릅니다. 



변수를 초기화하지 않고 그냥 출력한다면 에러가 뜹니다.

~~~python
print(variable) #초기화를 하지 않은 변수
~~~

**초기화** : 변수에 지정되어 있는 객체를 갱신하는 것.

![variableError](/static/assets/img/blog/python3/03BasicGrammer/variableError.png)



변수를 만드는 방법은 딱히 정해져 있지 않습니다만 개발자들이 선호하는 규칙은 있습니다. [Camel naming convention](http://guswnsxodlf.github.io/camelcase-pascalcase-snakecase)이라고 개발자들 사이에서 권고하는 규칙입니다. 많은 개발자들은 이 규칙들 중에서 변수에는 **lowerCamelCase**를 많이 쓰고 있습니다. **첫 문자는 반드시 소문자**이고 **각 단어의 첫 글자를 대문자**로 적습니다. 

~~~python
# 변수를 만드는 방법???? lowerCalmelCase!!
number = 10
myHeight = 175
speed = 80
~~~

