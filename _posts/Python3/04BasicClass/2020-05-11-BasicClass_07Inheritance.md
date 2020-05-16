---
layout: post
title: "Inheritance"
date: 2020-05-11
desc: "Inheritance is oop's charateristic"
keywords: oop, inheritance, parent, child
categories: [Python3]
tags: [python3,oop, inheritance, parent, child]
---

## Inheritance(상속)

상속은 객체를 부모와 자식클래스로 나누는 것을 말합니다. 

예를 들어 우리가 '모여봐요 동물의 숲' 게임을 만든다고 해봅시다. 

모여봐요 동물의 숲 게임에는 다양한 동물 캐릭터들이 나오기 때문에 우리는 '동물'이라는 객체를 만들었습니다. 

그런데 동물에도 종류가 엄청 많습니다. 
포유류도 있고 양서류도 있고, 어류도 있습니다. 생각해보니 동물이라는 객체가 모두의 특징을 표현할 수는 없을 것 같습니다. 악어는 동물의 특징 말고도 악어만의 특징이 있으니까요. 

그래서 우리는 포유류, 양서류, 어류라는 객체를 따로 만들어서 동물의 특징을 모두 가져오는 한편 이 3개의 객체만의 특징은 각 객체마다 구현하기로 했습니다.

이 '동물' 객체가 부모 클래스가 되고
'포유류', '양서류', '어류'가 자식 클래스가 됩니다.


~~~python
class animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("eat")

    def move(self):
        print("move")

    def sleep(self):
        print("sleep")

    def print_name(self):
        print(self.name)


class tiger(animal):

    #Method Overriding
    def move(self):
        print("run")

    def attack(self):
        print("attack")


if __name__ == '__main__':
    my_pet = tiger("titi")
    my_pet.eat()
    my_pet.move()
    my_pet.attack()
    '''
    결과
    eat
    run
    attack
    '''
~~~

상속 관계를 작성하는 방법은 아주 간단합니다.

자식클래스의 이름을 적고 오른쪽에 괄호를 열어 부모 클래스의 이름을 적습니다. tiger(animal)처럼요.

~~~python
class 자식클래스이름(부모클래스이름):
    
    자식클래스의 내용
    .
    .
    .
~~~

자식클래스는 부모클래스의 Attribute와 Method를 전부 가지고 있습니다. 

main을 실행하고 my_pet Instance에서 eat() Method를 실행했습니다.<br>
my_pet은 tiger 객체로 만든 Instance이지만 animal 클래스의 eat()메소드를 그대로 쓰고 있습니다. 

## Method Overriding

Method Overriding은 부모 클래스에서 정의된 method를 자식 클래스에서 재정의하는 방법입니다.

~~~python
class animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("eat")

    def move(self):
        print("move")

    def sleep(self):
        print("sleep")

    def print_name(self):
        print(self.name)


class tiger(animal):

    #Method Overriding
    def move(self):
        print("run")

    def attack(self):
        print("attack")
~~~
animal 클래스에 move() Method에는 move를 출력하고 있지만

tiger 클래스에서 move()는 run을 출력하고 있습니다. 그리고 main에서 tiger Instance에서 move()를 호출하면 run이 출력되는 것을 확인 할 수 있습니다. 


## Polymorphism(다형성)

Method Overriding에서 OOP의 특징 중 하나인 다형성을 확인할 수 있습니다.

Python3에서 다형성이란 부모-자식간의 상속관계에서 똑같은 메소드 이름을 쓸 수 있다는 의미입니다.    

다만, 파이썬에서 말하는 다형성은 완전히 OOP적이라고 말할 수는 없습니다. Python3에서는 같은 이름을 가지지만 다른 인자값을 가지는 Method Overriding을 허용하지 않기 때문입니다. 

~~~python
class tiger(animal):

    #Method Overriding
    def move(self):
        print("run")

    def move(self, a):
        print("dfd")

    def attack(self):
        print("attack")
~~~

위 코드와 같이 move라는 이름은 같지만 인자의 개수가 다른 Method Overriding은 허용하지 않습니다. 

이러한 Method Overriding을 Java입니다. 완벽한 다형성은 Java라는 언어에서 구현된다는 걸 참고지식으로 알고 넘어갑시다.


## 자식 클래스에서 `__init__`(생성자) 만들기

animal tiger관계에서 우린 Method에 집중해서 상속관계를 봤습니다. 이제 Attribute에 집중해서 살펴봅시다. 

자식클래스는 자식클래스만의 Attribute도 가질 수 있습니다. 

아래의 상속관계를 볼까요. 참고로 아래 코드는 잘못된 코드입니다.

~~~python
class Lecture:

    def __init__(self, lec_name, prof_name):
        self.lec_name = lec_name
        self.prof_name = prof_name
        

class BioLab(Lecture):

    def __init__(self, laboratory):
        self.laboratory = laboratory
~~~

BioLab 자식 클래스는 자신만의 laboratory Attribute를 가지고 있습니다. 

~~~python
if __name__ == "__main__":
    bio_lecture1 = BioLab("Bio laboratory015")
    print(bio_lecture1.laboratory)
    print(bio_lecture1.lec_name) #?????
    print(bio_lecture1.prof_name) #?????
~~~
![child__init__error](/static/assets/img/blog/python3/04BasicClass/child__init__error.png)


자식 클래스는 부모 클래스에 포함되므로 당연히 부모클래스의 Instance Attribute를 쓸 수 있어야 합니다.

그런데 부모클래스의 `__init__()` Method를 가져와야 lec_name과 prof_name을 쓸 수 있는데  이미 BioLab클래스에서 `__init__()` Method를 만든 상태네요.

이럴 때는 자식클래스의 `__init__()` Method에서 부모클래스의 `__init__()` Method를 호출함으로써 해결합니다. 

아래 코드를 볼까요. 
~~~python
class Lecture:

    def __init__(self, lec_name, prof_name):
        self.lec_name = lec_name
        self.prof_name = prof_name


class BioLab(Lecture):

    def __init__(self, lec_name, prof_name, laboratory):
        super().__init__(lec_name, prof_name)
        self.laboratory = laboratory
~~~

자식클래스의 `__init__()` Method안에 `__init__()`메소드가 또 나옵니다. 앞에 `super()`가 붙어있네요. `super()` 는 부모 객체를 반환하기 때문에 `super().__init__()`f로 부모클래스의 `__init__()` Method를 호출할 수 있었습니다. 

아래에서 결과를 확인해보세요. 

~~~python
if __name__ == "__main__":
    bio_lecture1 = BioLab("Cell Division", "Lee", "Bio laboratory015")
    print(bio_lecture1.lec_name) #Cell Division
    print(bio_lecture1.prof_name) #Lee
    print(bio_lecture1.laboratory) #Bio laboratory015
~~~