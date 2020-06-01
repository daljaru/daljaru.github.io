---
layout: post
title: "Servlet 02"
date: 2020-06-01
desc: "Let's make Servlet"
keywords: web, html, servlet, server, WAS, tomcat, container
categories: [Web]
tags: [web, server, servlet, tomcat, container, WAS]
---
해당 게시글은 웹을 공부하기 위해 개인적으로 기록했던 자료입니다. 정보를 얻는 목적으로는 적합하지 않다는 점을 참고바랍니다. 

## javax.servlet.http

이제 javax.servlet.http패키지를 이용한 servlet을 생성해보겠습니다.

![20httpServlet](/static/assets/img/blog/web/02MakeServlet/20httpServlet.png){:width="70%" height="70%"}

[Tomcat Servlet 3.0 API](http://tomcat.apache.org/tomcat-7.0-doc/servletapi/index.html)에서 확인해보면 HttpServlet은 GenericServlet과 상속관계에 있고 HttpServletRequest는 ServletRequest와 HttpServletResponse는 ServletResponse와 상속관계에 있습니다. 왜 GenericServlet이라고 불렀었는지 이제 조금 감이 옵니다. 


이번에는 WebContent>index.html을 만들었습니다. 
~~~html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
    <form action="urlname">
        search word : <input type="text" name="word">
        <input type="submit" value="send">
    </form>
</body>
</html>
~~~

`<form>`태그를 만들어서 action을 urlname으로 지정했습니다. 그리고 입력창을 만들고 name을 word로 지정했습니다. 

이번에는 java resources>src>servlet.first>WordEncoreServlet.java파일(Servlet)을 만들었습니다. 
~~~java
package servlet.first;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class WordEncoreServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String wName=request.getParameter("word");
		wName = wName+"...update server side";
		PrintWriter out = response.getWriter();
		out.println("<html><body>");
		out.println("<h2>");
		out.println(wName);
		out.println("</h2></body></html>");
		out.close();
	}
}
~~~

우선 요청을 받아야 하므로 request 인스턴스의 getPrameter()Method를 사용합니다. 인자는 index.html의 텍스트입력창 이름이 word였으므로 "word"를 입력합니다. 불러온 문자열을 wName이란 변수와 바인딩합니다. 

이제 응답절차를 작성합니다. 앞에서 했던 예제와 같이 만듭니다. PrintWriter Instance를 생성해서 response.getWriter()로부터 반환되는 값을 받고 out.println()을 통해 브라우저에 내용을 띄워줍니다. 마지막으로 close()를 통해 객체를 닫습니다. 


web.xml파일을 수정해야합니다. 
~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://java.sun.com/xml/ns/javaee" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" id="WebApp_ID" version="2.5">
  <servlet>
    <servlet-name>GenericServletTest1</servlet-name>
    <servlet-class>servlet.generic.GenericServletTest1</servlet-class>
  </servlet>
  <servlet-mapping>
    <servlet-name>GenericServletTest1</servlet-name>
    <url-pattern></url-pattern>
  </servlet-mapping>
  
  <servlet>
    <description></description>
    <display-name>WordEncoreServlet</display-name>
    <servlet-name>WordEncoreServlet</servlet-name>
    <servlet-class>servlet.first.WordEncoreServlet</servlet-class>
  </servlet>
  <servlet-mapping>
    <servlet-name>WordEncoreServlet</servlet-name>
    <url-pattern>/urlname</url-pattern>
  </servlet-mapping>
  
</web-app>
~~~

WordEncoreServlet이 하나 추가된 것을 확인할 수 있습니다. 이 코드에서 중요한 것은 `<url-pattern>`인데 `/`를 적고 index.html에서 `<form>`태그에 action을 urlname이라고 지정했으므로 urlname을 적어줍니다. 

이제 index.html을 돌려보면 아래 화면처럼 나오고

![21httpServlet02](/static/assets/img/blog/web/02MakeServlet/21httpServlet02.png){:width="70%" height="70%"}

위 페이지에서 myworld를 입력하고 send버튼을 누르면 아래와 같은 페이지가 응답되어 나오는 것을 확인 할 수 있습니다. 

![22httpServlet02response](/static/assets/img/blog/web/02MakeServlet/22httpServlet02response.png){:width="70%" height="70%"}