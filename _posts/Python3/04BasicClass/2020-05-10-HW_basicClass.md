---
layout: post
title: "HW02"
date: 2020-05-10
desc: "HW02"
keywords: HW02
categories: [Python3]
tags: [python3]
---

# HW02

아래의 다이어그램을 보고 클래스를 만들어보세요.

![quiz2_diagram](/static/assets/img/blog/python3/QuizImages/quiz2_diagram1.png)

파일 구조는 아래와 같습니다. 

Package : `CafeTest, CafeVO`

Modules : `CafeTest.py Cafe.py, Employee.py, Manager.py, Arbeit.py, Beverage.py, Coffee.py, Tea.py`

![quiz2_filetree](/static/assets/img/blog/python3/QuizImages/quiz2_filetree.png)


CafeTest.py에서 main을 실행하고 
결과는 아래와 같이 나오게 합니다. 

![quiz2_test](/static/assets/img/blog/python3/QuizImages/quiz2_test.png)

결과

![quiz2_result](/static/assets/img/blog/python3/QuizImages/quiz2_result.png)

![quiz2_result2](/static/assets/img/blog/python3/QuizImages/quiz2_result2.png)




과제에 적용되는 객체지향프로그래밍의 특징
* 상속(Inheritance)
* 다형성(Polymorphism)
* 추상화(Abstraction)
* 캡슐화(Encapsulation)
* 1:N 연결관계 (Cafe - Beverage,  Cafe - Employee)
  
과제에 적용되는 파이썬의 특징
* 패키지, 모듈 프로그래밍
* 이외 기본 문법들..


~~~python
#과제에 필요한 추가 문법!
#isinstace(A, B)
#A객체와 B객체의 타입이 같은지 검사합니다. 결과는 True or False를 반환합니다. 
~~~