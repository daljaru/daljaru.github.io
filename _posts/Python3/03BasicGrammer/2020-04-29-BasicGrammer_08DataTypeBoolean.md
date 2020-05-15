## Boolean(논리값)

 논리값은 두 개의 상수 객체인 **True**와 **False**입니다. 실제로 파이썬에서 True와 False를 사용할 수 있습니다.

~~~python
if __name__ == '__main__':
    if True:
        print("참이라서 출력됩니다.")
    if False:
        print("거짓이라서 출력이 안됩니다.")
        
        #결과 : 참이라서 출력됩니다. 
~~~

 논리값은 위의 예와 같이 if 조건문에서 조건식자리에 피연산자로 쓰일 수 있습니다. 

 **참고** : [**if문**](./10Condition.md)은 if 뒤의 조건식이 참인지 거짓인지 검사하고 참이라면 하위 블록을 실행합니다. 거짓이라면 하위 블록을 실행하지 않고 다음 코드로 넘어갑니다.  



~~~python
if __name__ == '__main__':
    while True:
        print("while문에서 조건식자리에 피연산자로 쓰일 수 있습니다.")
        break
    #결과 : while문에서 조건식자리에 피연산자로 쓰일 수 있습니다.
~~~

 while문에서 조건식자링 피연산자로 쓰일 수 있습니다. 

 **참고** : [**while문**](./13While.md)은 while 뒤의 조건식이 참인지 거짓인지 검사하고 참이라면 하위 블록을 실행합니다. 그리고 하위블록이 끝나면 다시 while뒤의 조건식을 검사하고 하위블록을 실행합니다.(이후 동일..) 거짓이라면 하위블록을 실행하지 않고 다음 코드로 넘어갑니다. 

 [**break**](./14BreakContinue.md)키워드는 반복문 내에서 쓰일 수 있으며 break키워드를 만나면 반복을 즉시 중단하고 상위 블록으로 빠져나갑니다. 우리는 print문을 실행하고 바로 break문을 만났기 때문에 결과 문장이 한번만 출력이 된 것입니다. 



## True와 False의 다른 표현들.

거짓으로 정의된 상수는 False로 간주됩니다. - None, False<br>대표적으로 모든 숫자 형들의 0이 False로 간주됩니다. -  `0`, `0.0`. `0j`<br>그리고 빈 시퀀스나 컬렉션이 False로 간주됩니다.  - `''`, `()`, `[]`, `{}`, `set(0)`, `range(0)`<br>이 이외의 값은 거의 대부분 99% True값을 반환합니다. 

예시

~~~python
if __name__ == '__main__':
    numberInt = 0
    numberFloat = 0.0
    numberComplex =0j
    emptyStr = ''
    emptyTuple = ()
    emptyLists = []
    emptyDic = {}
    emptyRange = range(0)
    if True:
        print("참이라서 출력됩니다.")
    if None:
        print("거짓이라서 출력이 안됩니다.")
    if numberInt:
        print("거짓이라서 출력이 안됩니다.")
    if numberFloat:
        print("거짓이라서 출력이 안됩니다.")
    if numberComplex:
        print("거짓이라서 출력이 안됩니다.")
    if emptyStr:
        print("거짓이라서 출력이 안됩니다.")
    if emptyTuple:
        print("거짓이라서 출력이 안됩니다.")
    if emptyLists:
        print("거짓이라서 출력이 안됩니다.")
    if emptyDic:
        print("거짓이라서 출력이 안됩니다.")
    if emptyRange:
        print("거짓이라서 출력이 안됩니다.")
#결과 : 참이라서 출력됩니다
~~~

~~~python
if __name__ == '__main__':
    if(1):
        print("참입니다.")
    if('테스트 문자열'):
        print("테스트 문자열 참입니다.")
~~~



### True와 False를 판별하는 논리연산과 비교연산

**논리연산**과 **비교연산**는 True나 False를 되돌려주는 아주아주 중요한 내장연산입니다. 



#### 논리연산

| 기호 | 연산    | 내용                                                         | 예시          | 결과  |
| ---- | ------- | ------------------------------------------------------------ | ------------- | ----- |
| and  | A and B | A와 B가 모두 True이면 결과는 True.<br>모두 True가 아니라면 결과는 False | True and True | True  |
| or   | A or B  | A와 B가 모두 False면 결과는 False<br>모두 False가 아니라면 결과는 True | True or False | True  |
| not  | not A   | A가 True이면 결과는 False<br>A가 False이면 결과는 True       | not True      | False |

~~~python
if __name__ == '__main__':
    if(True and True):
        print("참이라서 실행됩니다.")
    if(True and False):
        print("실행이 될까요?")   
#결과 : 참이라서 실행됩니다.
~~~

~~~python
if __name__ == '__main__':
    if(True or True):
        print("참이라서 실행됩니다.")
    if(True or False):
        print("실행이 될까요?")
"""
결과 : 
참이라서 실행됩니다.
실행이 될까요?
"""
~~~



#### 비교연산

| 기호     | 연산                   | 내용                      | 예시   | 결과  |
| :------- | :--------------------- | ------------------------- | ------ | ----- |
| `<`      | A < B                  | A가 B보다 작다            | 1 < 10 | True  |
| `<=`     | A <= B                 | A가 B보다 작거나 같다     | 2 <=2  | True  |
| `>`      | A > B                  | A가 B보다 크다            | 3 > 1  | True  |
| `>=`     | A >= B                 | A가 B보다 크거나 같다     | 3 >= 1 | True  |
| `==`     | A == B                 | A와 B가 같다              | 1 == 2 | False |
| `!=`     | A != B                 | A와 B가 같지 않다         | 1 != 2 | True  |
| `is`     | Class A is Class B     | A객체가 B객체와 같다      | -      | -     |
| `is not` | Class A is not Class B | A객체가 B객체와 같지 않다 | -      | -     |

~~~python
if __name__ == '__main__':

    string1 = 'abcd'
    string2 = 'abcd'
    string3 = 'cdef'

    if(1 < 10):
        print('조건이 True입니다.')
    if(string1 == string2):
        print('조건이 True입니다.')
    if(string2 != string3):
        print('조건이 True입니다.')
"""
결과:
조건이 True입니다.
조건이 True입니다.
조건이 True입니다.
"""
~~~