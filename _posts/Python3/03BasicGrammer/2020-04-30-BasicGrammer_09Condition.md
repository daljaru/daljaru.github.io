## Condition 조건문

#### 제어흐름도구

코드를 작성하다보면 자신이 원하는 조건대로 결과를 출력하고 싶을 때가 있습니다. 또는 데이터들을 조건에 따라서 분류하고 싶은 경우도 있습니다. 이럴때 코드의 진행을 여러 갈래로 분기시킬 수 있는 도구들이 있는데 이것을 **제어흐름도구**라고 합니다. 



## if, elif, else

**if**를 먼저 살펴보겠습니다. **if문 뒤에 조건식**을 넣고 조건식의 결과로 나오는 **boolean의 값에 따라** 코드의 흐름을 제어할 수 있습니다. 앞서 boolean형식을 소개할 때 많이 사용해봤습니다. 

if를 써볼까요

~~~python
if __name__ == '__main__':
    testNum = 1
    testStr = 'I likes banana, apple, orange'
    testList = ['bonobono', 'porory', 'nuburi']

    if True:
        print('It prints well')
    if testNum == 1:
        print('Number 1')
    if 'orange' in testStr:
        print("I like orange")
    if len(testList) == 3:
        print('My friends...')
    '''
    결과:
    It prints well
    Number 1
    I like orange
    My friends
    '''
~~~

if문 뒤에서 조건식에 논리값(True와 False)를 반환하는 표현식을 넣었고  마지막 에 `:`를 붙였습니다. <br>그리고 아랫줄을 들여쓰기를 한 후 **조건식의 결과가 True일 때 실행하고 싶은 코드**를 넣었습니다.<br>`__name__` 이라는 것이 `__main__`문자열과 같다는 조건식이 True를 반환하기 때문에 전체 코드가 실행된다는 것도 알게 되었습니다. 



#### 조건식과 함수의 조합

조건식 자리에 논리값이 들어가야 하므로 논리값을 리턴하는 함수를 넣는 것도 가능합니다.

~~~python
def isNumOverTen(number):
    if number > 10:
        return True
    if number < 10:
        return False
~~~

~~~python
if __name__ == '__main__':
    testNum = 100
    if isNumOverTen(testNum) :
        print('This number is over 100') 
'''
결과:
This number is over 100
'''
~~~

10이 넘는지 판별하는 함수를 정의하고 조건식자리에 넣어보았습니다. <br>정수값 100을 testNum변수에 지정하고 testNum을 다시 isNumOverTen()함수에 인자값으로 넣습니다. <br>결과는 당연히 True를 반환할 것이고 if문 검사를 통과해서 결과를 출력하게 됩니다. 



## elif와 else

elif 와 else를 만들면 조건문을 훨씬 보기 쉽게 만들 수 있습니다. (가독성이 좋아집니다.)

~~~python
if __name__ == '__main__':
    testNum = 100

    if testNum > 100:
        print('100보다 큽니다.')
        if testNum > 200:
            print('200도 넘습니다!')
        else:
            print('100과 200사이의 숫자입니다.')
    elif testNum < 100:
        print('100보다 작습니다.')
        if testNum < 50:
            print('50보다도 작습니다.!')
        else:
            print('50과 100사이의 숫자입니다. ')
    else:
        print('100입니다.')
~~~

**elif**는 **동일한 들여쓰기 라인**에 있는 **바로 위**의 조건문에서 조건식이 False가 되면 실행이 됩니다. 'range(0, 5)
[0, 1, 2, 3, 4]'이라고 생각해도 됩니다.  elif를 쓰려면 **자신보다 앞에 조건문**이 **반드시**  있어야합니다.   

**else**는 동일한 들여쓰기 라인에 있는 **모든 조건문**이 False가 되면 실행이 됩니다. 'range(0, 5)
[0, 1, 2, 3, 4]'이라고 생각해도 됩니다. else는 동일한 들여쓰기 라인에서 마지막 조건으로 위치할 수 밖에 없습니다. 하지만 반드시 있어야 하는 것은 아닙니다. 



위의 **코드를 눈으로 보고 여러 값들을 넣어서 무슨 값이 나오게 될지 상상해봅시다.** 그리고 Pycharm에 코드를 넣고 실행해봅시다. 상상한 것과 맞나요? 

testNum을 100, 60, 10, 120, 160, 250으로 초기화해보고 각각의 결과를 확인해보세요.
