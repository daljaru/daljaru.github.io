---
layout: post
title: "java.io 패키지 클래스 구조와 스트림에 대한 이해"
date: 2020-05-20
desc: "java.io Package Class diagram"   
keywords: java.io, class diagram
categories: [Java]
tags: [java.io, class diagram]
---

## java.io 패키지 클래스 구조

___

![javaIOClassStructure](/static/assets/img/blog/java/03JavaIO/javaIOClassStructure.png){:width="100%" height="100%"}
<br>

## Streams에 대한 간략한 설명

___

Java는 입출력을 Streams을 통해 수행합니다. Streams은 '연속적인 데이터의 흐름'입니다. 실제로 물리적으로는 java io 시스템상에서 연결되어 있고 java.io패키지로 캡슐화를 해놓았습니다. 그래서 개발자는 실제 물리적인 연결을 알지는 못해도 코드로 쉽게 입출력을 구현할 수 있습니다.
<br>
<br>

## Byte Stream / Character Stream

___

Streams은 크게 Byte Stream과 Character Stream으로 나뉩니다. Byte Stream은 byte데이터의 입출력을 다룰 수 있고 Character Stream은 오직 문자의 입출력을 다룰 수 있습니다. Character Stream은 유니코드를 사용하기 때문에 언어의 제약 없이 사용할 수 있습니다.
<br>

### Byte Stream

Byte Stream은 java.io패키지에 있는 클래스 다이어그램에서 InputStream와 OutputStream으로 묶여진 클래스들이 담당합니다.

이 클래스들이 가지는 메소드중에서 가장 중요한 메소드는 read()와 write()입니다. 최상단 추상클래스인 InputStream은 read()메소드를 선언하고 OutputStream이 write()메소드를 선언합니다. 

* read() - 데이터의 바이트를 입력받습니다.

* write() - 데이터의 바이트를 출력합니다. 
<br>

### Character Stream

Character Stream은 java.io패키지에 있는 클래스 다이어그램에서 Reader와 Writer로 묶여진 클래스들이 담당합니다. 

이 클래스들이 가지는 메소드중에서 가장 중요한 메소드는 read()와 write(), close()입니다. 최상단 추상클래스인 InputStream은 read(), close()메소드를 선언하고 OutputStream이 write(), close()메소드를 선언합니다.

