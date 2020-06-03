---
layout: post
title: "doGet(), doPost()"
date: 2020-06-02
desc: "more specific about request response mechanism..."
keywords: web, html, servlet, server, WAS, tomcat, container, request
categories: [Web]
tags: [web, server, servlet, tomcat, container, WAS, httpservletrequest, httpservletresponse, doget, dopost, service]
---

## service()

__

[HttpServlet API 문서](http://tomcat.apache.org/tomcat-8.5-doc/servletapi/index.html)를 보면 GenericServlet을 상속 받은 service(ServletRequest req, ServletResponse res)메소드와 오버로딩한 	service(HttpServletRequest req, HttpServletResponse resp) 메소드를 확인할 수 있습니다. 

이 메소드는 브라우저가 요청을 시작한 순간 생성된 request 인스턴스와 response인스턴스를 인자로 받아 요청받은 작업을 수행해서 돌려주는 메소드입니다. 
<br>
<br>

## doGet(), doPost()

___

HttpServlet Class API를 보면 doGet()가 doPost()라는 메소드가 있습니다. service(req, res)와 동일한 역할을 하지만 doGet은 get방식의 데이터포맷, doPost는 post방식의 데이터포맷방식에 사용됩니다. 

그래서 보통 서블릿을 만들 때 아래와 같이 만듭니다. 

![29doGetdoPost](/static/assets/img/blog/web/02MakeServlet/29doGetdoPost.png)

doProcess라는 메소드를 하나 만들고 doGet과 doPost가 doProcess를 사용하는 형태로 만듭니다. 이렇게 만들면 웹브라우저가 get이든, post든 어떤 방식으로 페이지나 데이터를 요청해도 doProcess를 통해 가져올 수 있습니다.

doGet(), doPost() 이 외에도 doPut() doDelete()..등의 다양한 메소드들이 있습니다. 이것들은 나중에 Restful API를 다룰 때 더 자세히 알아보겠습니다. 