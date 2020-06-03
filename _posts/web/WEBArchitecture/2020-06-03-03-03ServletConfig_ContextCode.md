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

___

Servlet의 필드 값을 외부자원(extra resources)를 통해서 초기화하는 것을 간단하게 줄여서 A Servlet instance Initialization이라고 말합니다.

보통 자바 클래스파일을 만들때는 생성자를 통해서 필드의 초기화가 이루어지지만 Servlet 클래스는 기본 생성자밖에 없으므로 init()메소드를 통해서 필드 초기화가 이루어져야 합니다. 

코드를 통해 확인해보겠습니다.

아래와 같이 config1.html파일을 만듭니다.
<br>

~~~html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<marquee bgcolor="orange"><h1>ServletConfig를 이용한 Servlet Initialization...</h1></marquee><p>
	<a href="SC1">Here Click</a>
</body>
</html>
~~~
<br>

그리고 Servlet을 아래와 같이 만듭니다. 
<br>

~~~java
package servlet.config;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class ServletConfigTest1 extends HttpServlet {
	private static final long serialVersionUID = 1L;
    private String name, addr="";
    
    public ServletConfigTest1() {
        super();
        System.out.println("constructor...");
    }
    @Override
    public void init() throws ServletException {
    	super.init();
    	System.out.println("init().....");
    	this.name = getInitParameter("name");
    	this.addr = getInitParameter("addr");
    	System.out.println(name+", "+addr);
    }
    
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doProcess(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doProcess(request, response);
	}
	protected void doProcess(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
	}
}
~~~
<br>

Servlet의 필드영역에 문자열변수 name과 addr를 만들었습니다. 생성자로는 초기화를 할 수 없으므로 init()을 통해 초기화를 진행해줍니다. 

눈여겨 봐야할 게<br>
~~~java
this.name = getInitParameter("name");
this.addr = getInitParameter("addr");
~~~

위의 코드입니다.<br>
ServletContext에 정의되어 있는 getInitParameter()라는 Method를 사용하고 있습니다.

ServletConfig가 ServletContext를 hasing하고 있고, 또한 GenericServlet이 ServletConfig를 상속하며 HttpServlet이 GEnericServlet을 상속하고 있는 구조를 기억해야합니다. 

그렇기 때문에 방금 제가 만든 ServletConfigTest1.java Servlet에서 getInitParameter() Method를 바로 쓸 수 있습니다. 

파라미터로 name과 addr이 전달되고 있는데 이 값이 바로 외부자원(extra resources)이고 web.xml에 정의되어 있습니다. 

web.xml코드를 보면 아래와 같습니다. 
<br>

~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://java.sun.com/xml/ns/javaee" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" id="WebApp_ID" version="2.5">
  <display-name>web05_ServletConfig</display-name>
  <welcome-file-list>
    <welcome-file>index.html</welcome-file>
    <welcome-file>index.htm</welcome-file>
    <welcome-file>index.jsp</welcome-file>
    <welcome-file>default.html</welcome-file>
    <welcome-file>default.htm</welcome-file>
    <welcome-file>default.jsp</welcome-file>
  </welcome-file-list>
  
  
  <servlet>
    <description></description>
    <display-name>ServletConfigTEst1</display-name>
    <servlet-name>ServletConfigTEst1</servlet-name>
    <servlet-class>servlet.config.ServletConfigTEst1</servlet-class>
    <init-param>
      <param-name>name</param-name>
      <param-value>habari</param-value>
    </init-param>
    <init-param>
      <param-name>addr</param-name>
      <param-value>seoul</param-value>
    </init-param>
    <load-on-startup>1</load-on-startup>
  </servlet>
  <servlet-mapping>
    <servlet-name>ServletConfigTEst1</servlet-name>
    <url-pattern>/SC1</url-pattern>
  </servlet-mapping>
</web-app>
~~~
<br>

`<servlet>`태그가 닫히기 전에 `<init-param>`태그와 `<param-name>`, `<param-value>`태그를 볼 수 있습니다. 

~~~xml
<!--파라미터 하나당 init-param태그를 달아줍니다. -->
<init-param>
    <param-name>   <!-- 속성 -->
    <param-value> <!-- 속성값 -->
</init-param>
~~~

이 파라미터들이 getInitParameter()로 넘겨집니다. 넘겨진 값들로 필드 초기화를 진행할 수 있습니다. 