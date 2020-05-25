---
layout: post
title: "Input, Output"
date: 2020-05-04
desc: "How to input your number or string to program??"
keywords: input, sys, sequence, print, format, escape sequence
categories: [Python3]
tags: [python3,input,sys,format, escape sequence]
---

## Input(입력)

 우리는 지금까지 변수에 **객체**을 숫자나 문자열로 명시적으로 정한 뒤에 프로그램을 실행했습니다. 하지만 실제 프로그램들은 **사용자의 입력을 받는 경우가 더 많습니다.** 예를 들어 카카오톡의 버튼을 누르는 것, 메시지 창에 글자를 쓰는 것, 전송 버튼을 누르는 것 모두가  사용자의 입력을 받는 경우입니다. 

파이썬에서 사용자의 입력을 받을 수 있게 프로그램을 만들어봅시다. 

### input()

 input()는 사용자의 입력을 받아서 입력값을 **문자열로** 돌려주는 내장 메소드입니다. 아래 코드를 Pycharm에서 실행하면 콘솔 창에 사용자가 글자를 입력할 수 있습니다. 

```python
if __name__ == '__main__':
    testString = input()
    print(testString)
```

.![input](/static/assets/img/blog/python3/03BasicGrammer/input.png)



```python
if __name__ == '__main__':
    testString = input('문자열을 입력하세요.')
    print(testString)
```

.![stringInput](/static/assets/img/blog/python3/03BasicGrammer/stringInput.png)



입력값을 숫자로 다루고 싶다면 [캐스팅](./15Casting.md)을 이용합니다. 캐스팅은 Dictionary와 Tuple을 배우면 고급 문법에서 좀 더 다루도록 하겠습니다. 

#### ex) 정수형을 받고 싶을 때

~~~python
if __name__ == '__main__':
    testInt = int(input("정수를 입력합니다."))
    print(testInt)
~~~



#### ex) 실수형을 받고 싶을 때 

~~~python
if __name__ == '__main__':
    testInt = float(input("정수를 입력합니다."))
    print(testInt)
~~~



### import sys

input()내장메소드는 내부에서 raw_input()을 evaluate 한 결과를 반환합니다. 그렇기 때문에 속도면에서 느리다는 평가를 받습니다. Python에서는 속도를 향상시키려면 sys모듈에서 stdin클래스를 사용할 것을 추천하고 있습니다. 

~~~ python
import sys

if __name__ == '__main__':
    testString = sys.stdin.readline()
    print(testString)
~~~



## Output

우리는 지금까지 출력을 사용할 때 print()메소드만 썼습니다. 이 print()에 대해서 좀 더 알아보기로 합시다.

#### Escape Sequence

print()를 이용해서 `'`나 `"`를 출력할 때 `\'`, `\"` 처럼 문자 앞에 `\`(역슬래시)를 붙입니다. 

~~~python
if __name__ == '__main__':
    print('\'He\' said \"Just do it.\"')

#결과
#'He' said "Just do it."
~~~

`'`는 문자열을 선언할 때 쓰이기 때문에 그냥 쓰면 '문자 `'`'로 인식하지 않습니다. 기존 기능의 사용을 피하고 싶을 때  `\`를 사용하게 됩니다. 

자주 쓰이는 것은 아래와 같습니다. 

| 이스케이프 시퀀스 | 의미                   | 유의 사항 |
| :---------------- | :--------------------- | :-------- |
| `\\`              | 역 슬래시 (`\`)        |           |
| `\'`              | 작은따옴표 (`'`)       |           |
| `\"`              | 큰따옴표 (`"`)         |           |
| `\n`              | ASCII 라인 피드 (LF)   |           |
| `\r`              | ASCII 캐리지 리턴 (CR) |           |
| `\t`              | ASCII 가로 탭 (TAB)    |           |

 더 자세한 내용은 [파이썬의 어휘분석](https://docs.python.org/ko/3/reference/lexical_analysis.html#literals)을 참고하면 좋습니다. 

~~~python
if __name__ == '__main__':
    print('\'He\' said \"Just do it.\"')
    print('\\^_^/')
    print('line feed \n')
    print('carriage return\r what?')
    print('\t tab tab')

#결과
#'He' said "Just do it."
#\^_^/
#line feed 
#
#what?
#	 tab tab
~~~



#### format() method

str클래스의 format()메소드를 이용해서 쓸 때가 더 많습니다. 

~~~python
if __name__ == '__main__':
    name1 = "lee"
    name2 = "kim"
    event = 'python'

    print("{} and {} studies {}".format(name1, name2, event)); #lee studies python
    print("{0} studies {2}".format(name1, name2, event));
   
#결과
#lee and kim studies python
#lee studies python
~~~

위 코드에서 `{}`를 포맷 필드라고 부릅니다. `{}`안에 format()메소드에 인자로 들어가 있는 순서대로 필드가 초기화됩니다.  

`{}`안에 인덱싱을 해주면 format()메소드의 인자값이 인덱스 순서대로 들어가게 됩니다. 두번째 print()메소드에서 0번째 인자인 name1, 2번째 인자인 event의 값이 들어가는 것을 확인 할 수 있습니다. 







