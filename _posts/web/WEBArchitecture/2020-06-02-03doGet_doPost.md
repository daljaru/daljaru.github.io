---
layout: post
title: "doGet, doPost"
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



