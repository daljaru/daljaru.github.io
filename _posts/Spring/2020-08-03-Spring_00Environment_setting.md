---
layout: post
title: "Environment Setting for learning Spring"
date: 2020-08-03
desc: "Environment Setting for learning Spring"
keywords: Spring, sts, eclipse
categories: [Spring]
tags: [Spring, sts, eclipse]
---

## Spring 공부를 위한 환경설정. 

___

### Spring Tool Suite 다운로드하기

![spring_tool_4](/static/assets/img/blog/spring/spring_tool_4.png){:width="40%" height="40%"}

Spring을 학습하기 위해 코딩 환경설정을 먼저 진행합니다. ㄸ

Spring Tools 4라는 걸 설치할 것입니다. Spring Tools 4는 Spring기반의 enterprise application을 위한 개발 환경을 제공합니다. 외양은 Eclipse와 동일합니다.

<br>

https://spring.io/tools0

위 사이트로 들어가면 Spring tool 4를 다운로드 받을 수 있습니다. 저는 이클립스 환경에서 Spring을 사용할 것이기 때문에 Spring Tools 4 for Eclipse로 들어가서 jar파일을 다운로드 받았습니다. 

![st4_download1](/static/assets/img/blog/spring/st4_download1.png)

![st4_download2](/static/assets/img/blog/spring/st4_download2.png)

<br>

### jar파일 압축해제하기

아마 jar파일이 다운로드 될 것입니다. 이제 jdk를 이용해 jar파일을 압축해제 합니다. 명령어 창에서 압축파일이 다운로드된 곳으로 들어가 java 명령어로 압축을 해제합니다. 

~~~
java -jar spring-tool-suite-4-4.7.1.RELEASE-e4.16.0-win32.win32.x86_64.self-extracting.jar
~~~

cmd창에서 위와 같이 치면 압축해제가 진행되면서 sts-4.7.1.RELEASE 폴더가 나옵니다. 

![st4_download4](/static/assets/img/blog/spring/st4_download4.png)

![st4_download3](/static/assets/img/blog/spring/st4_download3.png)

<br>

sts-4.7.1.RELEASE 폴더를 열면 SpringToolSuite4.exe라는 실행파일이 있습니다. 이 아이콘을 눌러서 Spring Tool Suite 4를 실행합니다. 

![st4_download3](/static/assets/img/blog/spring/st4_download3.png)

![st4_start](/static/assets/img/blog/spring/st4_start.png)

<br>

### workspace 설정하기

저는 default workspace가 아닌 제가 원하는 곳에 workspace를 만들었습니다. 

![st4_workspace](/static/assets/img/blog/spring/st4_workspace.png)

<br>

### Server window view 표시하기

처음에 시작하면 Eclipse와 동일한 UI가 나옵니다. Eclipse를 기반으로 하는 Spring ide를 다운로드 했기 때문입니다. 

![st4_openide](/static/assets/img/blog/spring/st4_openide.png)

<br>

여기서 Window -> Show Views -> Others..로 들어갑니다. 

![st4_showviews](/static/assets/img/blog/spring/st4_showviews.png)

<br>

Server -> Servers를 클릭합니다. 

![st4_server_view](/static/assets/img/blog/spring/st4_server_view.png)

<br>

![st4_tomcat](/static/assets/img/blog/spring/st4_tomcat.png)

그러면 sts4 하단 레이어에 Servers탭이 뜨고 No servers are available...이라는 파란색 문장이 뜹니다. 

어떤 Server를 쓸지 설정을 안해서 뜨는 문구입니다. 이 링크를 클릭하면 New Server라는 새 창이 뜨면서 Server를 설정할 수 있습니다. 

저는 Tomcat v8.5 Server를 사용할 것이기 때문에 Apache-> Tomcat v8.5 Server를 선택했습니다. 만약 다른 Tomcat version을 가지고 있다면 해당 version을 선택하면 됩니다. 

<br>

![st4_tomcat2](/static/assets/img/blog/spring/st4_tomcat2.png)

next를 클릭하면 Tomcat이 설치된 디렉토리의 경로를 설정하는 화면이 나옵니다. Browse를 누르고 Tomcat home을 누르 후, 폴더 선택 -> Finish를 클릭합니다. 

<br>

Server설정이 완료되면 Servers탭에 Tomcat서버가 설정된 것을 확인할 수 있고 Package Explorer에 Servers가 추가된 것을 확인할 수 있습니다. 

![sts4_package_explorer](/static/assets/img/blog/spring/sts4_package_explorer.png)

<br>

저는 Dynamic web project를 생성해서 Spring web framework를 공부할 예정이기 때문에 dynamic web project를 생성하겠습니다. 

File -> New -> Other..을 클릭합니다. 

![sts4_dynamic_web_project](/static/assets/img/blog/spring/sts4_dynamic_web_project.png)

<br>

Web -> Dynamic Web Project -> Next를 클릭합니다. 

![sts4_dynamic_web_project2](/static/assets/img/blog/spring/sts4_dynamic_web_project2.png)

<br>

project의 이름을 sp01_Core_DI로 설정하고 Next를 클릭합니다. 

![sts4_dynamic_web_project3](/static/assets/img/blog/spring/sts4_dynamic_web_project3.png)

<br>

소스폴더를 구조화할 수 있는 창이 나옵니다. default로 src폴더가 하나 있습니다. 먼저 이를 지운 후 아래 사진과 같이 폴더들을 만듭니다. 그리고 Finish를 클릭합니다. 

![sts4_dynamic_web_project4](/static/assets/img/blog/spring/sts4_dynamic_web_project4.png)

<br>

dynamic web project _ spring의 기본적인 세팅이 완료되었습니다. Package Explorer가 아래와 같이 나타나야합니다. 

![sts4_dynamic_web_project5](/static/assets/img/blog/spring/sts4_dynamic_web_project5.png)
