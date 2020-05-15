---
title: Install Python
layout: post
date: '2020-04-14'
desc: Learn about python, and how to install python3
keywords: python3, pip, env, pipenv, interpreter, guido
categories: [Python3]
tags:
- python3
- install
- pipenv
- pip
- env
---

## Python

![Python](/static/assets/img/blog/python3/01EnvSetting/Python.png)

Guido van Rossum이라는 네덜란드 프로그래머가 1991년에 개발.

Guido가 좋아하는 Monty Python's Flying Circus라는 영국의 코메디 프로그램에서 이름을 따왔다. 

2020년 기준  [전 세계 프로그래밍 언어 사용 비중](https://www.tiobe.com/tiobe-index/)중에서 3위로 부상하고 있다. 

Time Peters라는 미국의 소프트웨어 개발자가 파이썬의 핵심철학을 정리해 놓았으며 [Philosophy of Python](https://www.python.org/dev/peps/pep-0020/)라는 리스트를 만들어 놓았다. import this  print(this)를 통해 확인할 수 있다.



### Point

* 대화 기능의 인터프리터 언어
* 동적인 데이터 타입 결정 지원(Dynamic Typing) - 실행시간에 자료형을 검사.
* 플랫폼 독립적 언어
* 개발 기간 단축에 초점을 둔 언어
* 간단하고 쉬운 문법
* 고수준의 내장 객체 자료형 제공
* 메모리 자동 관리
* 팀워크에 유용
* 쉬운 유지보수
* 많은 수의 라이브러리 제공
* 짧아지는 코드
* 높은 확장성
* 확장 및 내장기능
* 무료



## Install Python

1. [Python 공식 홈페이지](https://www.python.org/)에 들어가서 Downloads -> Windows클릭.

   ![PythonDownload](/static/assets/img/blog/python3/01EnvSetting/PythonDownload.png)

   

2. Python3.8.2 - Feb.24, 2020을 찾아 Windows x86-64 executable installer를 다운로드 받고 실행한다. 

   ![PythonVersion](/static/assets/img/blog/python3/01EnvSetting/PythonVersion.png)

   

3. Add Python 3.8 to PATH를 클릭하고 Install Now를 클릭한다. 이후 설치과정 진행.

   ![Install](/static/assets/img/blog/python3/01EnvSetting/Install.png)

   

4. 파이썬이 설치가 완료되면 다음과 같이 설치가 제대로 되었는지 확인을 해봅니다.   

   * 윈도우키 + R 을 치고 검색창에 cmd 입력 > 콘솔 창이 나오면 python을 입력.

   ![PythonConsole](/static/assets/img/blog/python3/01EnvSetting/PythonConsole.png){: width="100%" height="100%"}

   위와 같은 창이 나온다면 설치가 정상적으로 진행이 된 것입니다. 



## Pipenv 설치

pipenv는 pip와 virtualenv가 합쳐진 것이다. 

* pip :  [pypi](https://pypi.org/)(Python Package Index) 저장소로부터 Python package를 받아 설치하는 패키지 도구. 
* Pypi : Third-party(The CheeseShop) Python open-source package들을 위한 저장소.
* virtualenv : 각 프로그램별로 완전히 독립적인 가상의 환경을 만들어 항상 최신의 라이브러리를 동일하게 유지하게끔 관리해준다. 



1. 윈도우키 + x -> Window Powershell로 입장 -> 파이썬이 설치된 폴더로 경로 변경 -> pipenv를 위한 새로운 폴더를 만들고 -> pip install pipenv 입력.

   ![Pipenv](/static/assets/img/blog/python3/01EnvSetting/Pipenv.png)

   

2. 다음과 같이 진행이 완료된 후 python -m pip install --upgrade pip라는 명령을 치라고 문구가 뜨게 될것이다. 그대로 진행한다. 

   ![pipenvInstallFinish](/static/assets/img/blog/python3/01EnvSetting/pipenvInstallFinish.png)

   

3. 업그레이드까지 완료되면 다음과 같이 마지막에 Successfully installed pip-20.0.2라고 뜨게 된다. 

   ![pipenvUpgrade](/static/assets/img/blog/python3/01EnvSetting/pipenvUpgrade.png)





