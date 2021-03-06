---
layout: post
title: "Servlet Lifecycle 01"
date: 2020-06-03
desc: "Explaining servlet lifecycle"
keywords: web.xml, html, servlet, server, WAS, tomcat, container, request, lifecycle, servletconfig, servletcontext
categories: [Web]
tags: [web.xml, html, servlet, server, WAS, tomcat, container, request, lifecycle, servletconfig, servletcontext]
---
해당 게시글은 웹을 공부하기 위해 개인적으로 기록했던 자료입니다.
___
<br>
<br>
## Web architecture Servlet Life Cycle

___

Middle Server에서 WAS가 가동되기시작하고 일어나는 일들을 다시 한 번 적어보겠습니다. 

1. WAS(Web Application Server) = Container가 가동되자마자 web.xml을 읽어들입니다. web.xml파일은 deploy descriptor라고 일반적으로 부르며 줄여서 DD파일이라고도 말합니다. 
<br>

2. Servlet들의 인스턴스를 생성합니다. 인스턴스는 Servlet name tag에 매핑된 이름과 일치하게 만들어집니다. 그리고 인스턴스를 생성하기 위해 WAS는 내부적으로 Servlet.java의 기본 생성자를 이용해서 인스턴스를 만듭니다. 인스턴스가 없으면 윗단에서는 아무것도 돌아가지 않습니다. 
<br>

3. Servlet 인스턴스 하나당 ServletConfig 인스턴스를 하나 생성합니다. ServletConfig는 WAS가 init()과정에서 Servlet에게 Servlet 구성요소 객체를 전달하는 역할을 합니다. 
<br>

4. ServletConfig는 내부적으로 ServletContext인터페이스를 가지고 있는데 ServletContext는 Servlet이 WAS와 소통할 수 있는 여러 Method들을 가지고 있습니다. ServletContext는 JVM윗단에 있는 Web Application하나당 하나가 만들어집니다.(배포 설정에 distributed설정이 되어있지 않는 한.) 이 ServletContext로 web.xml에 있는 여러 파라미터들을 읽어올 수 있습니다. 
<br>

5. ServletConfig인스턴스는 init()메소드의 인자로 들어가고 init()이 실행됩니다. 여기까지가 Middle Server의 **Ready on 상태**라고 합니다. Ready on상태는 서버가 꺼지기 전까지 한 번만 이뤄집니다.
<br>

6. 이 상태에서 브라우저가 요청을 하면 요청을 Web Server(httpd)가 받습니다. 만약 Dynamic한 요청인 경우 요청의 처리를 WAS(=Container)단으로 내립니다. 그리고 (Http)ServletRequest, (Http)ServletResponse인스턴스를 만들고 해당하는 Servlet의 Thread를 만듭니다. 
<br>

7. service()가 호출되고 doGet/doPost가 재호출 됩니다. 
<br>

8. service()실행이 다 끝나면 응답이 WebServer(httpd)를 거쳐서 브라우저로 갑니다. 그리고 (Http)ServletRequest, (Http)ServletResponse, thread가 death상태로 들어가게 됩니다. 다른 말로 메모리에서 unbind한 상태가 됩니다. 그리고 Servlet인스턴스만 메모리에 남아있게 됩니다. 
<br>

9. 만약 서버가 멈춘다면 Servlet인스턴스는 메모리를 반환하고 destroy()메소드를 실행한 후 사라집니다. 