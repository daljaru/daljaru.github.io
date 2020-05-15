---
layout: post
title: "For"
date: 2020-05-01
desc: "Control your code flow to make better program.."
keywords: loop, for
categories: [Python3]
tags: [python3,for, range]
---

## Loop(반복문)

**일련의 코드들을 반복적으로 사용하고 싶을때** 반복문을 사용합니다. 반복을 위한 대표적인 제어흐름도구로 **for**와 **while**이 있습니다. 

### for

~~~python
if __name__ == '__main__':
    testString = 'Hello'

    for i in testString:
        print(i)
'''
결과:
H
e
l
l
o
'''
~~~

기본적인 형태는 위와 같습니다. 

`for i in testString`에서 `i in testString`를 우린 어디서 많이 본 것 같습니다. 바로 시퀀스 안에 있는 값을 찾을 때 썼던 `in`이 들어가있습니다. for 문에서는 `in`다음에 시퀀스나 **iterable객체**가 옵니다. 

~~~python
if __name__ == '__main__':
    message = "I like apple, orange"
    print('apple' in message)
'''
결과:
True
'''
~~~

이 멤버십 검사 연산(x `in` Sequence)이 **for문 바로 뒤**에 오면 **시퀀스의 맨 앞의 값부터 순차적으로** for 뒤에 있는 변수로 들어가게 됩니다. 그리고 `:` 아래의 들여쓰기 블록을 반복 수행합니다.  

(`for i in testString`에서 `i`도 변수입니다. 다르게 설정할 수 있습니다. )

~~~python
if __name__ == '__main__':
    testString = 'Hello'

    for i in testString:
        print(i)
'''
결과:
H
e
l
l
o
'''
~~~

그래서 첫번째 i에는 'H'가 들어가고 출력으로 결과화면에서 첫번째 글자가 'H'가 뜬 것입니다. 반복은 별다른 조건이 없으면 시퀀스가 끝날 때까지 진행됩니다. 



### for문과 함수의 활용

다른 예를 들어볼까요.

~~~python
def sumOfNumbers(number):
    return (number * (number + 1))/2

if __name__ == '__main__':
    testList = [1,2,3,4,5,6]

    for number in testList:
        print(int(sumOfNumbers(number)))
'''
결과:
1
3
6
10
15
21
'''
~~~

**코드를 눈으로 보고 결과가 어떻게 나올지 상상해보세요.** 코드의 흐름이 어떻게 흘러가는지 보이시나요?

sumOfNumbers는 1부터 number까지의 정수를 모두 더한 결과를 돌려주는 함수입니다. 

이 함수를 for반복문 안에 넣고 인자는 testList안에 있는 값을 주고 있습니다.



### for문과 조건문의 활용

for문에 조건문을 넣어봅시다. 반복적으로 코드를 수행하면서 자신이 원하는 조건에 따라 결과를 다르게 만들 수 있습니다. 

~~~python
if __name__ == '__main__':
    testList = [1,2,3,4,5,6,7,8,9,10,11,12]
    twoTimes = []
    threeTimes = []
    fiveTimes = []


    for number in testList:
        if number % 2 == 0:
            twoTimes.append(number)
        if number % 3 == 0:
            threeTimes.append(number)
        if number % 5 == 0:
            fiveTimes.append(number)

    print(twoTimes)
    print(threeTimes)
    print(fiveTimes)
'''
결과
[2, 4, 6, 8, 10, 12]
[3, 6, 9, 12]
[5, 10]
'''
~~~

**코드를 눈으로 보고 결과가 어떻게 나올지 상상해보세요.**  위 코드는 2의 배수, 3의 배수, 5의 배수를 나누어서 리스트에 넣는 코드입니다.



### for문 중첩하기

for문 안에 또 for문이 들어갈 수 있습니다. 2번들어갈 수도 있고 10번들어갈 수도 있습니다. 문법을 알아두면 어떻게 쓸지는 개발자 마음입니다. 

~~~python
if __name__ == '__main__':
    list1 = [1,2,3,4,5]
    list2 = [1,2,3,4,5]

    for i in list1:
        for j in list2:
            print(i*j, end = " ")
        print()
'''
결과
1 2 3 4 5 
2 4 6 8 10 
3 6 9 12 15 
4 8 12 16 20 
5 10 15 20 25 
'''
~~~

~~~python
if __name__ == '__main__':
    list1 = []
    inList1 = [1,2,3]
    inList2 = [10, 20, 30]
    inList3 = [100, 200, 300]

    list1.append(inList1)
    list1.append(inList2)
    list1.append(inList3)

    print(list1)

    for i in list1:
        for j in i:
            print(j, end = ' ')
        print()
'''
결과
[[1, 2, 3], [10, 20, 30], [100, 200, 300]]
1 2 3 
10 20 30 
100 200 300 
'''
~~~

[**중첩된 Lists**](./05DataTypeList.md)의 경우 **중첩된 for문**으로 결과를 받아올 수 있는 것을 알 수 있습니다. 