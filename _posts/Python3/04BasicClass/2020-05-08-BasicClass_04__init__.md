---
layout: post
title: """__init__"""
date: 2020-05-07
desc: "Class attribute, class method, instance attribute, instance method"
keywords: class attribute, instance attribute, class method, class attribute
categories: [Python3]
tags: [python3,namespace, attribute, method, class]
---

## `__init__`method. . .

이제 `__init__`method에 대하여 알아봅시다. 앞서 보았듯이 클래스에서 **Mutable Attribute의 경우 Instance attribute를 생성하는데 어려움**이 있었습니다. Mutable Attribute는 메모리 공간이 변하지 않기 때문에 여러 Instance를 만들 수 없었기 때문이죠. 

`__init__`메소드를 쓰면 **Instance attribute들을 생성**할 수 있습니다. 아래 코드를 한 번 볼까요? Bread 클래스를 약간 변경했습니다. 

```python
class Bread:

    ingredients = [] #Class attribute

    def __init__(self):
        self.ingredients = [] #Instance attribute

    def addIngredients(self, ingredient):
        self.ingredients.append(ingredient)

    def breadInfo(self):
        print(self.ingredients)
```

`__init__(self)` method를 추가했습니다. **Instance method의 첫번째인자는 무조건 self**를 넣는다는 것도 기억이 나시죠? s**elf는 Instance 자기자신**을 가리킨다고만 알아두세요.  Instance 자기자신안에 Lists 객체(`[]`)를 만들어 변수 ingredients와 바인딩을 진행했습니다. 이 ingredients는 그 위에 Class attribute인 ingredients와 다르다는 점을 기억해주세요.



~~~python
if __name__ == '__main__':
    chocolateBread = Bread()
    muffin = Bread()

    Bread.ingredients.append('sugar')  #Class attribute
    print(Bread.__dict__)    #Bread Class's Namespace
    #{'__module__': '__main__', 'ingredients': ['sugar'], '__init__': <function Bread.__init__ at 0x00000226FADE6CA0>, ....


    chocolateBread.ingredients.append('meal') 
    #chocolateBread instance attribute
    
    print(chocolateBread.__dict__)  
    # {'ingredients': ['meal']}    #chocolateBread instance's Namespace
    
    print(muffin.__dict__)       
    # {'ingredients': []}          #muffin instance's Namespace
~~~

위의 코드에서 **chocolateBread와 muffin이라는 Instance**들을 만들었습니다.<br>Class attribute인 ingredients에 sugar를 추가했습니다. <br>chocolateBread Instance에서 ingredients에 meal을 추가했습니다. 



이제 Bread, chocolateBread, muffin의 Namespace을 확인해 볼까요? 

**Bread에는 sugar**가 있고, **chocolateBread에는 meal**, **muffin은 빈 List**가 있습니다. 

**Instance마다 Instance attribute 가 생성**된 것을 확인 할 수 있었습니다. 



## Class Attribute와 Instance Attribute 중에 어떤 것을 써야 하나요? 

우린 여러 케이스들을 실습하겠지만 대개 Instance Attribute를 사용하게 될 것입니다. 그래서 앞으로 클래스를 작성할 때는 꼭 `__init__`메소드를 작성하는 것이 좋습니다. 

Class attribute를 써야하는 상황이라면 **Class 이름.class_attribute**로 접근해서 쓴다는 것을 잊지 마세요.



## `__init__`메소드의 또 다른 활용

`__init__`은 메소드입니다. 우리는 `self`인자 하나 밖에 없는 메소드만 봤습니다만, 인자값을 여러개로 만들 수도 있습니다.  아래 예제를 봅시다. 

```python
class Book:

    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author

    def print_book(self):
        print("{} writes \'{}\' book.".format(self.author, self.book_name))


if __name__ == '__main__':
    book1 = Book('Little Women', 'Greta Gerwig')
    book2 = Book('Harry potter', 'J K Rowling')

    book1.print_book()
    book2.print_book()
```

`__init__`메소드에 인자가 3개가 들어갑니다. book_name과 author변수를 통해 메소드밖에서 객체를 받아서

`self.book_name`, `self.author` Instance attribute와 바인딩합니다.



실행 코드에서 볼 수 있듯이 객체를 생성할 때 class 이름 뒤에 method처럼 인자를 넣을 수 있습니다. instance attribute를 바인딩하는 method를 따로 만들 필요 없이 좀 더 간편하게 instance attribute에 바인딩 합니다. 



## Class method, Instance method

제목에서도 알 수 있듯이 method에서도 두 종류가 나뉩니다.  Class method도 Class attribute와 마찬가지로 메소드를 공유할 수 있습니다. 

아래 예제를 봅시다. 





