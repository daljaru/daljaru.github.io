---
layout: post
title: "Spring Tool Suite JRE Setting Error, missing tools.jar"
date: 2020-08-03
desc: "Spring Tool Suite JRE Setting Error, missing tools.jar"
keywords: STS, JRE, JKE, tools.jar
categories: [Spring]
tags: [STS, JRE, JKE, tools.jar]
---

## Missing Tools.jar

___

![sts_jre](/static/assets/img/blog/usefulSkills/EnvironmentSettingError/sts_jre.png)

Spring Tools Suite 4 를 사용하다가 사진과 같은 에러가 떠서 고치려고 한다. 

처음에 Spring Tools Suite4를 설치했을 땐 이런 에러가 없었는데 다른 스프링 project를 import를 한 이후로 계속 이런 메시지가 나온다. 

<br>

잘 읽어보면.. active된 JRE에서 tools.jar를 찾을 수가 없다고 한다. 

그리고 내가 Eclipse에서 실행하고 있는 jre는 jre1.8.0_261경로 까지인데   Eclipse가 찾는 건 Java\lib\tools.jar ,   jre1.8.0_261\lib\tools.jar라고 한다. 

<br>

멍청한 STS놈... 

일단 jre경로부터 확인하기로 했다.

![jrelib](/static/assets/img/blog/usefulSkills/EnvironmentSettingError/jrelib.png)

![jdklib](/static/assets/img/blog/usefulSkills/EnvironmentSettingError/jdklib.png)

tools.jar파일은 jre> lib에 있는게 아니라 jdk안에 lib폴더에 있다.

<br>

그럼 찾는 경로를 좀 바꿔주면 되지 않을까.. 해서 project > properties > java build path로 들어갔다. 

![buildpath](/static/assets/img/blog/usefulSkills/EnvironmentSettingError/buildpath.png)

<br>

쌩 jre로 설정이 되어 있어서 tools.jar가 없다...

![addlibraryno](/static/assets/img/blog/usefulSkills/EnvironmentSettingError/addlibraryno.png)

내 컴퓨터에서 tools.jar은  jdk > lib에 있어서  add Library는 아니고... (해보니까 안된다.)

그래서 그냥 Add External JARs..로 tools.jar를 받아와야할 것 같았다.

<br>

![sts_jre](/static/assets/img/blog/usefulSkills/EnvironmentSettingError/sts_jre.png)

똑같이 안된다... .. . tools.jar를 직접 넣어도 다른 경로에서 tools.jar파일을 찾는다고 한다. 

이쯤되면 .init파일을 건드려야 할 것 같다. 

<br>

![init](/static/assets/img/blog/usefulSkills/EnvironmentSettingError/init.png)

STS4 설치폴더로 가면 SpringToolSuite4.init파일이 보인다. 이 파일을 우클릭한우 편집버튼을 누르고 > 메모장이 뜨면   --vmargs를 찾는다.

그리고 --vmargs바로 위에 아래와 같이 2줄을 추가했다. 

-vm<br>
C:\Program Files\Java\jdk1.8.0_251\bin\javaw.exe

이클립스를 시작할때 구동환경설정을 javaw로 맞춰주었다. 

<br>

다시 STS4를 키면 메세지가 뜨지 않는다! 해결!



