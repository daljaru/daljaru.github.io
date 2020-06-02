---
layout: post
title: "Hello World"
date: 2020-04-16
desc: "start python programming.."
keywords: python3, helloworld, print, project, source, code
categories: [Python3]
tags: [python3,helloworld,print]
---

## Connect Pycharm with Python 

이젠 Pycharm과 Python을 연결해보자. Pycharm을 실행하고 Create new Project를 클릭한다. 

![CreateProject](/static/assets/img/blog/python3/01EnvSetting/CreateProject.png)ㅋ

IDE(Integrated Development Environment)로 프로그램을 가장 처음에 만들기 시작할 때 프로젝트를 생성한다고 말한다. 프로젝트는 규모가 매우 다양할 수 있다. 생체데이터 분석 프로그램을 만든다면 데이터분석 프로젝트 라고 할 수도 있고 리듬게임을 만든다면 리듬게임프로젝트, 파이썬 공부를 하기 위해 만든다면 파이썬스터디프로젝트라고 명명해도 좋다.  

프로젝트는 코딩을 지원하고 대량 리팩토링, 코딩 스타일 지원 등등을 제공한다. 

 

아래와 같은 화면이 뜨는 것을 확인할 수 있다. 

![CreateNewProject](/static/assets/img/blog/python3/01EnvSetting/CreateNewProject.png)



* Location을 보면 프로젝트의 이름을 설정할 수 있는 것을 확인할 수 있다. Pycharm에서 자동으로 PycharmProject폴더까지 생성하고 하위 폴더는 사용자가 쓸 수 있게 설정이 된다. 여기서는 MyProject라는 이름으로 프로젝트를 생성한다. 다른 곳을 설정하고 싶다면 오른쪽에 보이는 파일그림을 누르면 된다. 

  

  ##### 인터프리터 선택

* New environment using은 Pipenv를 선택할 수 있다. 

* Base interpreter는 이전에 우리가 설치했던 파이썬3.8이 뜨는 것을 확인할 수 있다.



**인터프리터**는 [고급 언어](https://ko.wikipedia.org/wiki/고급_언어)로 작성된 원시코드 명령어들을 한번에 한 줄씩 읽어들여서 실행하는 프로그램이다. 앞으로 우리는 Python(원시코드)을 사용해 프로그램을 작성할 것이고 이 파이썬들을 읽어서 python.exe라는 인터프리터가 실행을 할 것이다.

 

이제 Create를 누르면 새로운 프로젝트가 생성이 되고 다음과 같은 화면이 나온다. 

![firstScreen](/static/assets/img/blog/python3/01EnvSetting/firstScreen.png){:width="100%" height="100%"}



## 소스코드 작성

이제 프로그래밍을 배운다면 가장 먼저 작성한다는 Hello World파일을 만들 것이다. Pycharm에서 왼쪽에 파일구조가 트리형태로 보이는 곳을 Project tool window라고 부른다. MyProject를 선택하고 마우스 우클릭을 통해 Popup menu를 연다. 

![newFile](/static/assets/img/blog/python3/01EnvSetting/newFile.png)



New로 들어가면 여러 파일들을 선택할 수 있는데 우리는 Python언어로 프로그램을 만들 것이므로 Python File을 선택한다. 파일 이름을 HelloWorld라고 지으면 아래의 화면처럼 HelloWorld.py라는 이름의 파일이 생성되고 Editor가 뜨는 것을 확인할 수 있다. 여기에 print('Hello World')라고 일단 쳐보자. 

![HelloWorld](/static/assets/img/blog/python3/01EnvSetting/HelloWorld.png){: width="100%" height="100%"}



우리는 지금 Pycharm안에서 Python파일을 하나 생성했다. 이 파일은 어디에 생겼을까? 우린 가상의 파일을 만든게 아니라 실제로 파일을 (Pycharm을 통해) 하나 만든 것이다. 한 번 확인을 해보자. HelloWorld를 우클릭을 하고 Popup menu에서 Show in Explorer를 누른다. 

![ShowInExplorer](/static/assets/img/blog/python3/01EnvSetting/ShowInExplorer.png)



아래와 같이 윈도우의 파일창이 하나 켜진것을 확인할 수 있다. 프로젝트 이름으로 지은 MyProject가 하나의 폴더로 되어있고 그 안에 HelloWorld.py가 있는 것을 확인할 수 있다. 이제 Pycharm이 왜 tool이라고 부르는지 이해가 조금 될 수도 있다. 이런 tool이 없었다면 프로그래밍 개발은 아주 시간이 많이 들고  귀찮은 작업이 되었을 것이다. 

![ExplorerScreen](/static/assets/img/blog/python3/01EnvSetting/ExplorerScreen.png){:width="80%" height="80%"}



## 소스코드 실행하기

메뉴에서 Run이라는 항목을 찾아보자. Popup menu에서 Run 'HelloWorld'나 Run을 찾을 수 있을 것이다. 클릭을 하면 PyCharm이 원시코드를 읽어서 컴파일 후 Run tool window에 결과를 출력할 것이다. 

![Run](/static/assets/img/blog/python3/01EnvSetting/Run.png)

정확히 말하면 다음과 같다. PyCharm이라는 IDE가 pipenv라는 환경에서 HelloWorld.py파일을 읽는다. -> PyCharm은 python.exe라는 Interpreter를 이용해서 HelloWorld.py 파일을 원시코드를 한줄씩 읽고 print라는 명령을 해독한 후 "'HelloWorld' 라는 문자열을 읽고 화면에 출력하라"는 명령을 정상적으로 수행한다. 

##### 결과화면

![HelloWorldConsole](/static/assets/img/blog/python3/01EnvSetting/HelloWorldConsole.png)



(재미로)다음 코드를 새로 넣어보자. Time Peters가 말한 파이썬의 철학을 읽어볼 수 있다. 

~~~python
import this
print(this)
~~~

-> 여기에서 생각할 수 있는 질문.

* import가 무엇일까. 
* this는 ' '를 붙이지 않았는데 어떻게 출력되는 것일까. 
* this안에 저렇게 많은 글들이 들어갈 수 있다는 것일까?



여기에 적힌 용어들은 모두 [pycharm-quick-start-guide](https://www.jetbrains.com/help/pycharm/installation-guide.html)에 나오는 용어들을 인용한 것이다. Pycharm이라는 Tool에 대해서 더 자세히 알고 싶고 또 영어에 자신이 있다면 들어가서 쭉 읽어보는 것도 방법이다. 

![Notation](/static/assets/img/blog/python3/01EnvSetting/Notation.png){:width="100%" height="100%"}

