## Basic Function

 함수를 기초적으로 다루어보겠습니다. 수학공부를 하다보면 함수라는 건 미지수에 값을 넣고 계산을 통해 결과값을 출력하는 것이죠.

 프로그래밍에서의 함수도 이와 비슷하게 인자값을 받고 계산을 통해 원하는 결과를 만드는 일을 합니다. 다만 그 형태가 수학에서의 방정식하고는 약간 다르고 그 의미도 다릅니다. 

Python에서 함수(메소드)의 기본적을 형태는 아래와 같습니다. 

~~~python
def appendString(argument1, argument2):  # appendString은 자신이 임의로 정한 함수명입니다.
    # function works with argument1, argument2 or others
    result = ""
    for i in argument1:
        result += i

    result += argument2
    return result  #결과값 내보내기
~~~

~~~python
str = "This is test String"
list1 = list(str) 

string = appendString(list1, 'Good bye')
print(string) #This is test StringGood bye

# Lists타입의 변수 list1과 문자열 'Good bye'를 함수의 인자로 넣었습니다. 
~~~



**def 키워드**는 함수(혹은 메소드)를 만들기 위해 사용합니다. def 뒤에는 **자신이 원하는** **함수의 이름**을 적습니다. 

 이후 괄호를 열고 함수의 **입력값을 받을 변수**들을 넣습니다. 이 변수들에 넣을 값에 따라 문자열형이 될 수도 있고 숫자, 리스트형 등 다양한 타입이 될 수 있습니다. 자신이 만들기를 원하는 함수에 적절한 변수명을 설정해야하고 입력값을 넣어야합니다. 

위에서는 문자열을 넣어서 이어붙일 목적으로 만든 함수이기 때문에 숫자를 넣으면 의도한것과는 다른 결과가 나오게 되겠죠. 그리고 `:` 를 적고 아랫줄부터 **들여쓰기**를 한 후 함수의 내용을 코딩합니다. 

**return**키워드는 함수의 결과값으로 내보낼 **객체**나 **변수**를 적을 수 있습니다. 

~~~python
string = appendString(list1, 'Good bye')  
#appendString함수는 내부에서 result라는 결과값을 내보내서 최종적으로 string변수에 대입하고 있습니다. 
~~~



## 함수를 쓰는 목적(의미)

함수를 쓰는 목적은 간단한데 

1. **동일한 기능을 그룹화**한다는 점입니다. 
2. **코딩이 좀 더 수월**하고 **코드의 가독성**이 좋아집니다.
3. **모듈 임포팅으로 활용할 수 있습니다.**  

예를 들어 리스트의 평균을 구하는 코드가 있다고 해봅시다. 코딩을 하다보니 3개의 리스트의 평균을 구해야하는 상황입니다. 함수를 쓰지 않는다면 아래의 코드가 되겠지요. 

~~~ python
list1 = [1, 2, 3, 4, 5]
list2 = [5, 3, 7, 8, 9]
list3 = [100, 134, 26, 737]


# list1의 평균
total = 0
for i in list1:
    total += i

avg = total / len(list1)
print(avg)

# list2의 평균
total = 0
for i in list2:
    total += i

avg = total / len(list2)
print(avg)

# list3의 평균
total = 0
for i in list3:
    total += i

avg = total / len(list3)
print(avg)
~~~

하지만 함수를 만들어서 쓴다면 조금 보기가 편해집니다. 그리고 써야할 코드의 양도 줄어듭니다. 자연스레 코드를 작성하면서 저지르는 실수를 줄일 수 있습니다. [**모듈 임포팅**](./07Module.md)은 다음 문서에서 자세히 알아보겠습니다. 

~~~python
list1 = [1, 2, 3, 4, 5]
list2 = [5, 3, 7, 8, 9]
list3 = [100, 134, 26, 737]

def calAvg(list): #리스트의 평균을 구하기
    total = 0
    for i in list:
        total += i
    avg = total / len(list)
    print(avg)

# list1의 평균
calAvg(list1)

# list2의 평균
calAvg(list2)

# list3의 평균
calAvg(list3)
~~~
