---
layout: post
title: "A Servlet Instance Initialization"
date: 2020-06-03
desc: "how to get extra resources"
keywords: Servlet, getInitParameter, WAS, init, container, field, initialization
categories: [Web]
tags: [web, server, servlet, tomcat, container, WAS, Servlet, getInitParameter, init, field, initialization]
---

## A Servlet Instance Initialization

Servlet의 필드 값을 외부자원(extra resources)를 통해서 초기화하는 것을 간단하게 줄여서 A Servlet instance Initialization이라고 말할 수 있습니다. 

Servlet instance 하나를 초기화할 수 있다는 뜻입니다. 그렇다면 어떤 값으로 초기화를 해야하나요? 보통 자바 클래스파일을 만들때는 생성자를 통해서 초기화가 이루어지지만 Servlet 클래스는 기본 생성자밖에 없으므로 init()메소드를 통해서 필드 초기화가 이루어져야 합니다. 

코드를 통해 확인해보겠습니다.

아래와 같이 config1.html파일을 만듭니다.


Container차원의 값으로 초기화

getinitparamet는 web.xml로부터 받음. . . extra resources....

`<init-param>`
    `<param-name>`   속성
    `<param-value>` 속성값.
`</init-param>`
