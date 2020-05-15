## Namespace에 대한 이해

클래스를 '정확히' 이해하려면 **Namespace에 대한 이해**가 필수입니다. 약간 어려울 수도 있습니다. 하지만 정확히 알면 남들보다 확연히 다른 이해도를 가지게 될 것입니다. 파이썬은 쉬운 언어가 아닙니다. 잘 몰라서 쉽다고 하는 사람들이 많을 뿐입니다. 

Namespace란 Attribute을 저장하고 있는 공간입니다. 

#### 클래스의 Namespace를 알아봅시다.

아래 코드를 실행해봅시다. 

~~~python
class Bread:
    
    ingredients = 'meal'

    def breadInfo(self):
        print(self.ingredients)
        
if __name__ == '__main__':
    print(dir())
	
#['Bread', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
~~~

dir() 내장 함수는 현재 local scope에서 쓸 수 있는 **모든 attribute들**을 리스트 형으로 반환합니다.**(슈퍼클래스, 해당클래스, 인스턴스 포함)**

 dir에 인자를 아무것도 주지 않았으므로 if조건문 아래공간에서 쓸 수 있는 Attribute들의 리스트가 표현됩니다. 우리가 선언했던 Bread클래스도 있네요.

(`__???__` 언더바 두 개의 사이에 있는 것들은 파이썬에서 이미 사용중인 특변한 변수입니다. 우리가 흔히 봤던 `__name__`도 있네요!) `print(__name__)`도 해보시기 바랍니다. `__main__`이 뜨는 것을 확인 할 수 있을 겁니다.

 

한번 Bread를 print해볼까요.

~~~python
class Bread:
    
    ingredients = 'meal'

    def breadInfo(self):
        print(self.ingredients)
        
if __name__ == '__main__':
    print(Bread)
#<class '__main__.Bread'>
~~~

`<class '__main__.Bread'>`라는 결과가 뜨는 것을 확인 할 수 있습니다.  `__main__`안에 있는 Bread라는 클래스 라는 뜻입니다.



이번엔 dir(Bread)를 해봅시다. dir(Object)처럼 객체인자가 있으면 Bread객체 안에서 유효한 모든 Attribute들을 리스트 형으로 반환합니다.

~~~python
class Bread:
    
    ingredients = 'meal'

    def breadInfo(self):
        print(self.ingredients)
        
if __name__ == '__main__':
    print(dir(Bread))
    
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'breadInfo', 'ingredients']
~~~

우리가 선언했던 ingredients도 있고 breadInfo도 있습니다.  Bread는 breadInfo(self)라는 메소드도 가지고 있지만 breadInfo라는 메소드자체의 정보를 attribute로 가지고 있기도 합니다. 

~~~python
class Bread:
    
    ingredients = 'meal'

    def breadInfo(self):
        print(self.ingredients)

if __name__ == '__main__':
    print(Bread.breadInfo)
#<function Bread.breadInfo at 0x0000020EABF56CA0>
~~~



그렇다면 이제 Bread Class가 가지고 있는 Attribute들 중에서 Bread클래스만의 Namespace를 확인해봅시다. `__dict__`는 해당 클래스의 Namespace를 반환합니다. 

~~~python
class Bread:
    
    ingredients = 'meal'
    
    def breadInfo(self):
        print(self.ingredients)


if __name__ == '__main__':
    print(Bread.__dict__)
    print(Bread.ingredients)
#{'__module__': '__main__', 'ingredients': 'meal', 'breadInfo': <function Bread.breadInfo at 0x000001E9F6A46CA0>, '__dict__': <attribute '__dict__' of 'Bread' objects>, '__weakref__': <attribute '__weakref__' of 'Bread' objects>, '__doc__': None}
#meal
~~~

우리가 선언한 ingredients와 breadInfo가 보입니다!



#### 이제 인스턴스의 attribute를 살펴봅시다. 

~~~python
class Bread:
    
    ingredients = 'meal'
    
    def breadInfo(self):
        print(self.ingredients)


if __name__ == '__main__':
    
    bread1 = Bread()
    bread2 = Bread()
    
    print(dir(bread1))
    print(dir(bread2))
~~~

위 코드를 실행하면 print(dir(Bread))와 똑같은 결과가 나옵니다. bread1인스턴스와 관련있는 모든 attribute들(슈퍼클래스, 해당 클래스, 인스턴스)을 출력하기 때문입니다. 



bread1인스턴스만의 Namespace를 확인해봅시다.

~~~python
class Bread:
    ingredients = 'meal'

    def breadInfo(self):
        print(self.ingredients)


if __name__ == '__main__':
    bread1 = Bread()
    bread2 = Bread()

    print(bread1.__dict__)
    print(bread2.__dict__)
'''
결과
{}
{}
'''
~~~

아무것도 뜨지 않습니다. 

bread1과 bread2의 이름공간에는 아무것도 없습니다. 그렇다면 bread1인스턴스로 ingredients변수에 접근하지 못하는 것일까요? bread1.ingredients로 코딩하면 아무것도 뜨지 않을까요?

~~~python
class Bread:
    ingredients = 'meal'

    def breadInfo(self):
        print(self.ingredients)


if __name__ == '__main__':
    bread1 = Bread()
    bread2 = Bread()

    print(bread1.ingredients)
    print(bread2.ingredients)
    
'''
결과
meal
meal
'''
~~~

bread1과 bread2의 인스턴스를 이용해 ingredients에 접근했더니 둘 다 meal이 출력됩니다. 이름공간에는 없는데 어떻게 출력이 되는 것일까요? 

 바로 **Python 인터프리터**가 **자동으로 클래스의 이름공간에서 값을 찾았기 때문**입니다. Python 인터프리터는 **인스턴스의 이름공간에서 변수를 찾지 못하면** 클래스의 이름공간에서 변수를 찾게 됩니다. 

메소드는 내용을 변경할 일이 없기 때문에 크게 헷갈리지는 않지만 Attribute의 경우는 값이 변경될 일이 많기 때문에 이름공간의 사용에 대해서 항상 중요하게 생각하고 있어야 합니다. 



##### 그렇다면 인스턴스의 이름공간이 빈 값이 아니라면 어떻게 될까요?

~~~python
class Bread:
    ingredients = 'meal'

    def breadInfo(self):
        print(self.ingredients)


if __name__ == '__main__':
    bread1 = Bread()
    bread2 = Bread()

    bread1.ingredients = 'chocolate meal'
    print(bread1.__dict__)
    print(bread2.__dict__)
    print(bread1.ingredients)
    print(bread2.ingredients)
'''
결과:
{'ingredients': 'chocolate meal'}
{}
chocolate meal
meal
'''
~~~

bread1인스턴스에서 ingredients에 접근해서 직접 chocolate meal이라는 문자열 객체를 바인딩했습니다. 

그리고 bread1 인스턴스의 이름공간에 'ingredients' : 'chocolate meal'이라는 매핑이 생겨난 것을 확인할 수 있습니다. 

bread2 인스턴스의 이름공간에는 여전히 아무것도 들어있지 않습니다. 그래서 클래스 이름공간에 있는 attribute에 접근했습니다. 





###  정리

1. dir(Bread)와 dir(bread1), dir(bread2)가 같은점으로 보아 클래스 Attribute는 **클래스이름.attribute이름**으로 공동으로 사용할 수 있습니다. 

~~~python
class Bread:
    ingredients = 'meal'

    def breadInfo(self):
        print(self.ingredients)


if __name__ == '__main__':
    bread1 = Bread()
    bread2 = Bread()

    Bread.ingredients = 'chocolate meal'

    bread1.breadInfo()
    bread2.breadInfo()
~~~

위 코드와 같이 Bread.ingredients로 클래스 Attribute를 변경했더니 인스턴스에서 접근하는 ingredient도 변경되었습니다. **(인스턴스 Namespace가 비었으므로)**



2. 인스턴스의 attribute를 초기화하지 않으면 Namespace에는 아무것도 들어가있지 않는다. 그렇기 때문에 자동으로 클래스의 이름공간을 참조하게 된다.
3. 인스턴스의 attribute를 초기화하면 인스턴스의 Namespace가 갱신되면서 인스턴스만의 이름공간에서 attribute를 사용하게 된다.  (Immutable Sequence에 한해서만)
