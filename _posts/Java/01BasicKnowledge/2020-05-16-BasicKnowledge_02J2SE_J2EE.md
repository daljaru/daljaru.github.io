---
layout: post
title: "Java SDKs, and configurations"
date: 2020-05-16
desc: "Difference J2SE, J2EE"
keywords: java, jdk, jre, J2SE, J2EE
categories: [java]
tags: [Java,JRE,JDK,J2SE, J2EE]
---

### Java SE(Standard Edition) 와 Java EE(Enterprise Edition)의 차이

이름에서 약간 감이 오실지는 모르겠습니다만 **Java SE**는 **로컬머신에서 작동하는 애플리케이션**을 위해서 쓰입니다. 반면에 **Java EE**는 **클라이언트/서버사이드로 나누어진 환경**에 적합합니다. 그래서 주로 기업의 서버컴퓨터에서 설치가 되기 때문에 Enterprise Edition이라고 합니다. 

만약에 여러분이 계산기 프로그램을 쓴다고 해봅시다. 이 계산기 프로그램은 인터넷이 연결되지 않아도 됩니다. 그저 유저 한명이 혼자서 씁니다. 그렇기 계산기 프로그램을 쓰기 위해서는 컴퓨터에 SE만 설치하면 됩니다.  

반면 여러분이 쇼핑회사에서 일을 하는데 실시간 고객 반응형 쇼핑 프로그램을 만들었다고 합시다. 서비스를 시작하려면 고객과 데이터를 주고 받아야하기 때문에 네트워크환경을 통해 클라이언트와 데이터를 주고받기 위해 회사의 서버컴퓨터에 Java Enterprise Edition을 설치합니다. 

---

### JDK, JRE
Java SE를 누르면 [Java SE Download페이지](https://www.oracle.com/java/technologies/javase-downloads.html)로 넘어갑니다.
![04_javaSEDownloadPage](/static/assets/img/blog/java/01BasicKnowledge/04_javaSEDownloadPage.png)

여러가지 버전이 있습니다. 어떤 버전을 선택해서 다운로드 받을지는 개발자들에게는 아주아주 중요한 문제입니다. 우리는 자바를 배우는 단계이기 때문에 아주 안전한 java SE 8u251을 다운로드 받습니다. 

![05_j2SE_8u](/static/assets/img/blog/java/01BasicKnowledge/05_j2SE_8u.png)


Oracle JDK라고 적힌 곳 아래에 다운로드 아이콘이 5개나 있습니다. 여기에서 JDK Download를 선택하고 다운로드를 진행합니다. 

JDK와 JRE의 차이를 알아두는게 좋습니다. 
**Which Java package do I need?**라고 아래쪽에 설명도 되어 있네요. 여기서 Java 'package'라고 말한 것에 주의를 기울여야 합니다. 

**JRE**는 Java Runtime Environment의 약자로서 컴파일된 Java 프로그램을 실행하기 위한 모든 패키지들이 들어 있습니다. 다운로드 받으면 아래와 같이 폴더형식으로 이름이 지어지고 그 안에 패키지들이 들어있는 것을 확인 할 수 있을 겁니다. 

![06_jrefolder](/static/assets/img/blog/java/01BasicKnowledge/06_jrefolder.png)

이 안에 **JVM**, Java Class Library, java command 같은 것들이 들어있습니다. JRE만 가지고는 프로그램을 만들 수 없습니다. 단지 Java로 만든 프로그램을 실행할 수만 있습니다. 

**JDK**는 Java Development Kit의 약자로서 기본적으로 JRE를 포함하고 있고 여기에 컴파일러(javac)와 여러 툴들을(javadoc, jdb)를 포함합니다. 이것들을 이용해서 컴파일된 프로그램을 만들 수 있습니다. 

앞으로 우리는 file.java 소스파일을 만들고 컴파일러(javac)을 통해 file.class 바이트코드를 만들고 이 코드를 JRE를 이용해 실행하게 됩니다. 

![07_jdkfolder](/static/assets/img/blog/java/01BasicKnowledge/07_jdkfolder.png)

![08_jdkPackages](/static/assets/img/blog/java/01BasicKnowledge/08_jdkPackages.png)

---

### JVM

JRE에 대해 얘기하면서 JVM이라는 용어가 나왔습니다. **JVM**(Java Virtual Machine)은 컴파일러가 만들어낸 file.class 바이트 코드들을 실행할 수 있는 주체입니다.

컴파일러가 file.java 소스파일을 굳이 바이트 코드로 만들어서 JRE에 있는 JVM으로 넘겨주는 이유가 있습니다. Java라는 언어를 운영체제의 종류에 의존하지 않게 설계하려 했기 때문입니다. 

덕분에 Window OS에서 java파일을 만들고 그 파일을 Linux OS, Mac OS에서 컴파일하고 실행해도 똑같은 결과가 나옵니다. 대신에 JVM은 Window용 JVM, Mac용 JVM들을 별도로 만들어야합니다.

하지만 JVM들은 개인이 만들지 않아도 됩니다. 이미 Oracle에서 개발자들이 열심히 만들어서 사이트에서 배포하고 있습니다. (OS 별로 다운 받을 수 있는 JDK가 다릅니다.) 우린 그걸 편리하게 다운받을 수 있던 것이구요.

![09_jvm](/static/assets/img/blog/java/01BasicKnowledge/09_jvm.png)

jdk > jre > bin > server > jvm.dll을 확인 할 수 있습니다.