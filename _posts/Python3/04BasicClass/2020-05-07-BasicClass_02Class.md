## Class(클래스)

'객체'를 어떻게 만들 수 있을까요? Python에서는 class라는 키워드으로 구현할 수 있습니다. 

클래스는 '객체'라는 개념을 프로그래밍으로 구현하기 위한 실제 코드입니다. '클래스를 작성한다'라고 표현합니다.

기본 형태는 아래와 같습니다. 

~~~python
class Bread: #클래스 이름은 임의로 적습니다. 
    '''
    클래스의 내용이 들어갑니다.
    .
    '''

if __name__ == '__main__':
	#인스턴스를 생성해서 쓸 수 있습니다. 
    #인스턴스란 '객체'라는 개념적인 틀에 구체적인 값이 들어간 데이터를 말합니다. 
    
~~~

`class`키워드 뒤에 클래스 이름을 적습니다. `:`이후에 아래 블록에 Attribute와 Method가 들어갑니다. 



구체적으로 만들어봅시다. 

~~~python
class Bread:
    ingredients = []

    def addIngredients(self, ingredient):
        self.ingredients.append(ingredient)

    def breadInfo(self):
        print(self.ingredients)


if __name__ == '__main__':
    chocolateBread = Bread()
    
    chocolateBread.addIngredients('chocolate')
    chocolateBread.addIngredients('meal')
    
    chocolateBread.breadInfo()
    
'''
결과
['chocolate', 'meal']
'''
~~~

우리는 빵의 재료와 재료를 추가하고 재료정보를 확인할 수 있는 클래스를 만들었습니다. 

* Attribute로 리스트 객체의 Instance를 만들고 이를 변수 ingredients로 지정했습니다. 
* 변수이름 = 클래스이름() 으로 Bread클래스의 Instance를 생성했습니다. 별다른 생성자가 없으며 `()`를 클래스 이름 옆에 붙입니다.  
* 변수이름을 가지고 Attribute나 Method에 접근할 수 있습니다.  
* chocolate와 meal을 재료로 추가하고 재료정보를 출력하고 있습니다. 
* 파이썬에서 인스턴스 메소드의 첫번째 인자는 항상 self를 넣습니다. 



정말 맛보기에 불과한 클래스 다루기였습니다. 다음 챕터부터는 약간 어려워집니다.



