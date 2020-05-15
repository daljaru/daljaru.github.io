---
layout: post
title: "While"
date: 2020-05-02
desc: "Control your code flow with while."
keywords: while, condition
categories: [Python3]
tags: [python3,while]
---


## while	

반복문의 또 다른 형태인 while문을 알아보겠습니다. while은 for와 마찬가지로 일련의 코드들을 반복하고 싶을 때 사용합니다. 

for문과 다른 점이 있다면 while 오른쪽에 조건식이 들어온다는 점입니다. 이 조건식이 참이면 `:`아래 블록을 실행하고 다시 while line으로 돌아오게 됩니다. 

~~~python
if __name__ == '__main__':

    number = 0
    while number < 5:
        print(number)
        number += 1
~~~

위 코드에서 while 오른쪽에 number < 5라는 조건식이 들어갔습니다. <br>while 블록에서는 number를 출력하고 number를 1씩 늘리고 있습니다. number를 5번 늘린 후에  조건식은 False값을 가지게 되고 while문을 종료하게 됩니다. 



### for 와 while의 차이점

for와 while은 '반복'이라는 똑같은 기능을 담당하는데 굳이 이렇게 나눈 이유는 무엇일까요?

잘 생각해보면 for는 작성함과 동시에 반드시 반복횟수를 지정합니다. **[range()](./12Range.md)를 통해 범위를 지정**할 수 있고 혹은 **유한한 시퀀스를 넣어서 제한된 길이만큼 반복**할 수 있습니다.

반면에 while은 조건을 넣어서 반복을 빠져나올 수 있도록 사용자가 지정해줘야합니다. 만약 조건식을 잘못 적어서 계속 True가 나오게 되면 어떻게 될까요? 

~~~python
if __name__ == '__main__':

    number = 0
    while True:
        print(number)
        number += 1
'''
결과:
1
2
3
.
.
.
376205
376206
376207
376208
376209
376210
.
.
.
'''
~~~

이런 식으로 무한 Loop에 빠지게 될 것입니다. 

for문을 쓸때는 원하는 범위를 정확하게 지정해야하고 while문은 조건식을 잘 줘야한다는 점을 기억해주세요.
