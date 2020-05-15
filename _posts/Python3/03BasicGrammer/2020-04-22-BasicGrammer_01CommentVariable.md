---
layout: post
title: "Comment"
date: 2020-04-22
desc: "How to write comment"
keywords: comment, python3
categories: [Python3]
tags: [python3,comment]
---

## 주석(Comment)

Comment는 컴퓨터가 인터프리터를 통해 해독하지 않는다고 인식하는 기호입니다. 

Comment뒤에 주로 코드, 프로젝트에 대한 설명을 적습니다.  주석은 원시파일에 적을 수 있습니다. Python에서는 hash character(#) 를 문장 앞에 붙이는 규칙을 가집니다. #뒤에 라인 하나를 대상으로 주석처리를 합니다.

~~~python
#이 부분은 주석입니다. 
print('Hello World!!') #print 메소드는 문자열을 출력할 수 있습니다. 
~~~

 ![Comment](/static/assets/img/blog/python3/03BasicGrammer/Comment.png)

한글로 친 주석부분은 인터프리터가 넘기고 print()만 실행합니다.

**여러 줄을 주석처리할 수 있는 방법**입니다. 아래와 같은 기호를 씁니다. 

~~~python
"""
여러 줄 주석을 
쓸 수 있습니다. HaHa
"""

'''
여러 줄 주석을 
쓸 수 있습니다. HaHa
'''

~~~

Github에서 아무 Python 파일이나 찾아서 확인해보면 각 프로그래머들이 자신이 달고 싶은 주석을 단 것을 확인할 수 있습니다.

![CoomentExample](/static/assets/img/blog/python3/03BasicGrammer/CoomentExample.png)



#### 주석을 쓸 때 주의할 점

프로그래밍은 컴퓨터와 대화를 하기 위해 사람이 쓰는 언어입니다. 그런데 프로그래밍을 하다보면 자연스레 다른 사람이 쓴 코드를 참고할 수도 있고 내 코드를 보고 싶어하는 사람도 있기 마련입니다. 

그렇기 때문에 주석은 너무 길거나 복잡해서 원래의 코드를 읽는데 방해가 되지 않아야합니다. **꼭 필요한 곳에 간결하게 적도록 노력합시다.** 물론 복잡한 주석을 쓰는 것을 방지하기 위해 **원시코드를 쓰는 방법을 정해놓은 규칙**(Example : Camel Naming Convention)도 있습니다. 