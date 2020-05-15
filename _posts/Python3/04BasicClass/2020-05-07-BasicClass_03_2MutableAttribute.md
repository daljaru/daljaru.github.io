## Mutable Attribute

NameSpace를 소개하면서 인스턴스의 attribute를 초기화하면 해당 인스턴스의 Namespace가 갱신되면서 인스턴스만의 이름공간에서 attribute를 사용하게 된다고 말했습니다.  

하지만 **위의 문장은 Immutable Sequence에 한해서만 가능한 경우**입니다. Mutable Sequence의 경우는 다르게 작동합니다. List Datatype을 설명할때 Immutable과 Mutable의 차이를 말했었습니다. 

* 불변시퀀스의 경우 선언이 될 때마다 메모리의 공간이 달라집니다. 
* 반면 가변시퀀스의 경우에 메모리공간이 하나가 주어지고 그 메모리공간 늘어나는 형식으로 관리가 됩니다.

| 분류       | 이름                                                         |
| ---------- | ------------------------------------------------------------ |
| 불변시퀀스 | Sclasstring(문자열), Tuple(튜플), 바이트열(Bytes)            |
| 가변시퀀스 | Lists(리스트), 바이트 배열(Byte Arrays), arrays(확장 모듈 array) |



클래스의 Attribute를 선언과 무슨 관계가 있는지 알아보겠습니다. 아래 코드를 적어봅시다.

~~~python
class Bread:
    ingredients = []

    def addIngredients(self, ingredient):
        self.ingredients.append(ingredient)

    def breadInfo(self):
        print(self.ingredients)


if __name__ == '__main__':
    chocolateBread = Bread()
    muffin = Bread()
~~~

위 코드를 보고 이제 보이는 것이 있죠. 

* Bread 클래스가 만들어졌다. 
* 클래스 Attribute에 리스트형 객체의 인스턴스가 있고 ingredients로 바인딩했다. 
* addIngredients(), breadInfo()메소드가 있다. 
* Bread 객체를 이용해서 인스턴스 2개를 만들고 각각 chocolateBread와 muffin변수로 바인딩했다.



아래에 코드를 더 추가해봅시다. 

~~~python
	print(chocolateBread.__dict__) #{}
    print(muffin.__dict__) #{}
~~~

각 인스턴스의 Namespace를 출력해보았더니 둘 다 당연히 빈값으로 나옵니다. 

이제 chocolateBread의 attribute를 초기화해보겠습니다. 

~~~python
class Bread:
    ingredients = []

    def addIngredients(self, ingredient):
        self.ingredients.append(ingredient)

    def breadInfo(self):
        print(self.ingredients)


if __name__ == '__main__':
    chocolateBread = Bread()
    muffin = Bread()

    chocolateBread.ingredients.append('meal')
    print(chocolateBread.__dict__)  # {}
    print(muffin.__dict__)			# {}
~~~



두 인스턴스의 Namespace가 그대로 빈 것이 확인됩니다. 

분명히 이전 챕터에서 ingredients가 문자열일때는 인스턴스의 attribute를 초기화해주면 인스턴스의 Namespace가 갱신되었습니다. 하지만 Lists는 그렇지 않네요.

이유가 짐작이 가시나요? 

Lists는 muttable sequence이기 때문에 초기화를 아무리 해줘도 메모리 공간이 달라지지 않기 때문입니다. 그렇기 때문에 `chocolateBread.ingredients.append('meal')`을 해줘도 Class Attribute인 ingredients 리스트만 변하고 인스턴스 Attribute는 변하지 않습니다. 

~~~ python
	print(id(Bread.ingredients)) #1361107873984
    print(id(chocolateBread.ingredients)) ##1361107873984
    print(id(muffin.ingredients)) ##1361107873984    주소값이 모두 똑같이 나옵니다. 인스턴스에 이름공간이 없기 때문에 클래스 Attribute를 참조하기 때문입니다. 
~~~

이 차이를 아는 것이 파이썬을 '그냥 안다'와 '제대로 안다'의 차이라고 할 수 있겠습니다. 이 점을 모른다면 파이썬이 쉽다고 말하는 것이고 안다며 파이썬이 그래도 어렵게 설계된 언어구나 라고 알 수 있을 것입니다. 



##### 그렇다면 가변시퀀스들은 영원히 인스턴스 attribute를 못만드는 것일까요?  

##### Python은 이 문제를 `__init__`메소드를 사용해서 해결합니다.