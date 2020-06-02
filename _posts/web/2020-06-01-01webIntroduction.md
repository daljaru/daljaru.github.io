---
layout: post
title: "Web Introduction"
date: 2020-06-01
desc: "Web Introduction"
keywords: web, html, css3, javascript, jquery, bootstrap
categories: [Web]
tags: [web, bootstrap,web server]
---

해당 게시글은 웹을 공부하기 위해 개인적으로 기록했던 자료입니다.
<br>
<br>

## Web에서 다룰 중요한 기술들
___
Web에서 Servet과 JSP라는 중요한 두 기술을 다루게 될겁니다.  

Servlet은 웹프로그래밍에서 클라이언트의 요청을 처리하고 그 결과를 다시 클라이언트에게 전송하는 Servlet 클래스의 구현 규칙을 지킨 자바 프로그래밍 기술입니다. 

JSP는 이 Servlet을 Tag중심으로 바꾼 것일 뿐입니다. 즉 코드를 기술하는 방식이 다른 것일 뿐입니다.
<br>
<br>

## 둘 중에 어떤 것을 배워야 하는가? 
___
저는 개인적을 Servlet을 배우는 것이 중요하다고 생각합니다. 많은 대학교에서 대부분 JSP에 밑도끝도없이 진입해서 배웁니다만 Servlet을 배워야 MVC Pattern을 제대로 이해할 수 있고 Web Application Server구축할 때 많은 도움이 됩니다. 

* Servlet - Web에서 돌아가는 프로그래밍 기술, Logic 중심. 
* JSP - Web에서 돌아가는 프로그래밍 기술, Tag 중심.
* 참고 - Python은 라이브러리가 매우 강력하기 때문에 실제로 서버사이드 프로그래밍을 하기에는 무리가 있습니다.
* Servlet을 배우면서 비동기통신인 Ajax를 다룰 것입니다.
<br>
<br>

## Model
___
만약 Java를 배웠다면 Class를 만드는 방법을 알 것입니다. Java로 클래스를 만들때 가장 기초적인 정보를 저장하는 방법으로 VO(Value Object)를 만듭니다. Private field에 생성자 오버로딩으로 구현한 생성자를 통해 정보를 주입합니다. 그리고 Database에 Access하는 클래스인 DAO(Data Access Object)를 만듭니다. 

DAO와 VO두개를 Model이라고 합니다. 두 개를 합쳐서 Model이라고 부르기도 하고 각각을 Model이라고 말해도 좋습니다.

DB Server에서 DBMS로 DB Schema를 만들고 그 안에 Table들을 만들고 Relations, restriction을 설정하게 됩니다. 

DB Server와 Model을 JDBC로 연결하게 됩니다. 그 과정에서 DML쿼리문과 SELECT쿼리문을 통해 CRUD를 진행합니다. 

여기까지가 기초적인 Back-end 단계입니다.

![01_serverside](/static/assets/img/blog/web/01BasicServlet/01_serverside.png){:width="50%" height="50%" text-align="center";}
<br>
<br>

## Front UI
___
Appearance를 만드는 기술에 HTML5, CSS3, Javascript를 사용했고 Javascript를 더 쉽게 사용하기 위해 Front UI Framework인 JQuery를 사용했습니다. 그리고 이 모든게 합쳐진 Bootstrap3, 4를 사용했습니다. 

HTML5에서 제공하는 가장 중요한 Storage를 Web Storage가 2개가 있는데 Local Storage와 Session Storage가 있습니다. 두 개중에 Local Storage만 알면 됩니다. Session Storage는 거의 쓸 일이 없습니다. 
<br>
<br>

## Static Document(Script language) versus Dynamic Language
___
Front UI를 만들때 .html파일을 만들었는데 이와 같은 문서는 프로그램이 아니라 스크립트 문서라고 합니다. 프로그램은 동적인( 사용자의 입력에 따라서 결과값이 달라지는) 특징이 있어야 하기 때문에 작성한 그대로 보여지는 Front 화면은 프로그램이 아닙니다. 

이런 html같은 파일을 Static Document라고 합니다. 그리고 이런 Tag기반 언어를 Script Language라고 합니다. 반대로 Java와 같은 언어를 Dynamic Language라고 합니다. 입력결과에 따라 그때그때 다르게 반응한다는 말입니다. 

여기까지가 기초적인 Front-end의 구성입니다.

![02_front](/static/assets/img/blog/web/01BasicServlet/02_front.png){:width="30%" height="30%"}
<br>
<br>

## Servlet
___
Front와 Back이 생긴다고 전체적인 메카니즘이 확립되지 않습니다. Front에서 값을 입력하고 이 값을 Database에 어떻게 저장할 것인지.. 혹은 Database에 있는 값을 읽어와서 어떻게 인터넷 브라우저에 띄우게 할 것인지에 대한 해답이 제시되지 않았습니다. 중간에 Middle이 있어야 하는데  보통 이 Servlet과 Back-end를 합쳐서 Server side라고 합니다. 

전체적인 시각에서 보면 이 두개를 Server side라고 하지만 시야를 좁게 해서 Back-end의 입장에서 보면 Servlet은 Server side에서 front에 해당됩니다. 

이 말은 Server side에서 Servlet은 Front에서 입력값을 받고 DAO에 입력받은 값을 연결하기 때문입니다. 이 정보는 Database까지 갔다가 다시 DAO로, Servlet을 거쳐서 Front로 돌아오게 될 것입니다. 

Client의 요청을 Server Side의 가장 앞 단에서 받는 게 Servlet입니다. Servlet은 보통 5각형으로 표현하는게 일반적입니다. 

![03_framework](/static/assets/img/blog/web/01BasicServlet/03_framework.png){:width="80%" height="80%"}


위 그림도 꽤나 두루뭉술 합니다. Front와 Back사이에서 Servlet이라는 것이 어떻게 동작하는지 알아봅시다. 