---
layout: post
title: "Servlet 01"
date: 2020-06-01
desc: "Let's make Servlet"
keywords: web, html, servlet, server, WAS, tomcat, container
categories: [Web]
tags: [web, server, servlet, tomcat, container, WAS]
---

해당 게시글은 웹을 공부하기 위해 개인적으로 기록했던 자료입니다. 정보를 얻는 목적으로는 적합하지 않다는 점을 참고바랍니다. 

## Servlet을 간단하게 구현해보자. 
<br>
## Tomcat Server 설정

Eclipse에서 Apache tomcat을 서버로 만듭니다. 

서버 타입을 설치한 Tomcat의 버전에 맞게 선택하고 next를 누릅니다. 

![01_makeServer](/static/assets/img/blog/web/02MakeServlet/01_makeServer.png){:width="40%" height="40%"}

Tomcat installation directory는 Tomcat의 home으로 지정합니다. 

![02_makeServer2](/static/assets/img/blog/web/02MakeServlet/02_makeServer2.png){:width="40%" height="40%"}

tomcat을 설치한 폴더로 들어가면 아래와 같은 폴더와 파일들이 있습니다.

![03_tomcatServer](/static/assets/img/blog/web/02MakeServlet/03_tomcatServer.png){:width="40%" height="40%"}

bin은 tomcat이 실행되기 위한 여러가지 파일들이 들어있고 conf에는 환경설정과 관련된 파일들이 있습니다. webapps에는 우리가 만든 front파일들이 들어가게 될 것입니다.

![14_webappsconfig](/static/assets/img/blog/web/02MakeServlet/14_webappsconfig.png){:width="40%" height="40%"}

Eclipse에서 서버를 새로 생성할 때 ServerLocation을 tomcat Installation으로 설정합니다. 그리고 Browse를 눌러 webapps에 배포가 되도록 합니다. 

Tomcat과 Web Application Server, Container는 모두 같은 말입니다. 
<br>
<br>

## Tomcat Servlet 3.0 API

[Tomcat Servlet 3.0 API](http://tomcat.apache.org/tomcat-7.0-doc/servletapi/index.html)화면으로 가봅시다.

![04_tomcatServletAPI](/static/assets/img/blog/web/02MakeServlet/04_tomcatServletAPI.png){:width="40%" height="40%"}

위 페이지는 톰캣환경에서 servlet을 구현하기 위한 API가 기술되어 있습니다. Servlet 3.0버전의 API가 있습니다. 

Package들 중에서 javax.servlet과 javax.servlet.http이 두개만 알면 servlet을 만들어낼 수 있습니다. 

javax.servlet같은 경우 프로토콜과 독립적인 servlet을 만들어낼 수 있습니다. 반면 javax.servlet.http는 웹프라우저에서 http통신에 최적화된 servlet을 만들 수 있습니다. 

먼저 javax.servlet을 보기로 합시다. 

javax.servlet에서 interface Summary를 봅시다.

![servletInterface](/static/assets/img/blog/web/02MakeServlet/06servletInterface.png){:width="40%" height="40%"}

여기에 Servlet과 ServletConfig라는 인터페이스가 있습니다. 

Servlet interface는 servlet이 반드시 실행해햐하는 모든 method가 정의되어 있습니다. 

![08servlet](/static/assets/img/blog/web/02MakeServlet/08servlet.png){:width="40%" height="40%"}


ServletConfig는 초기화과정에서 servlet container에 의해서 servlet으로 정보가 보내지는 servlet구성객체를 반환하는 Method를 담고 있습니다.

![07servletConfig](/static/assets/img/blog/web/02MakeServlet/07servletConfig.png){:width="40%" height="40%"}

내용을 보면 전부 get메소드밖에 없는 것을 알 수 있습니다. 그리고 servletContext인터페이스와 연관되어 있는 것을 확인할 수 있습니다.

이 두 인터페이스를 상속받고 있는 것이 GenericServlet이라는 클래스입니다. 

![09genericServlet](/static/assets/img/blog/web/02MakeServlet/09genericServlet.png){:width="40%" height="40%"}

![10genericServlet02](/static/assets/img/blog/web/02MakeServlet/10genericServlet02.png){:width="40%" height="40%"}

GenericServlet에 대한 설명을 보면 일반적이고 프로토콜 독립적인 Servlet을 정의한다고 적혀있습니다. 즉 GenericServlet클래스(Generic)를 재정의하면 사용자가 원하는 Servlet을 만들 수 있다는 의미입니다. 

GenericServlet은 Service Interface에 있는 init(ServletConfig config)를 오버라이딩하고 있는데 GenericServelt클래스에서는 더 쉽게 사용할 수 있게 인자값이 없는 init()로 만들어졌습니다. 

그리고 	service(ServletRequest req, ServletResponse res) Method를 오버라이딩 하고 있는 것을 알 수 있습니다.

![11genericServlet03](/static/assets/img/blog/web/02MakeServlet/11genericServlet03.png){:width="40%" height="40%"}

sevice 메소드에서 인자의 이름에서 유추할 수 있듯이 **요청**을 받고 **응답**을 처리하는 메소드인 것을 알 수 있습니다. 

바로 클라이언트(Front UI)에서 오는 요청들을 받아서 처리하고 Back-end단에서 오는 응답을 처리하는 메소드입니다. 

우리는 이 service Method를 재정의 해주면 servlet을 완성할 수 있습니다.

![05servletAPI](/static/assets/img/blog/web/02MakeServlet/05servletAPI.png){:width="40%" height="40%"}
<br>
<br>

## Eclipse Dynamic Project

Eclipse로 돌아와서 Dynamic Web Project를 하나 만듭니다. 이름은 web01_GenericServlet이라고 하겠습니다. 여기서 Dynamic web module version을 2.5로 설정했는데 servlet구축을 좀더 상세히 하고 싶어서 설정했습니다. 

![12newProjectGenericServlet](/static/assets/img/blog/web/02MakeServlet/12newProjectGenericServlet.png){:width="40%" height="40%"}

Java application이 저장되기 위한 폴더를 설정합니다. build\classes가 기본적으로 설정됩니다. 

![13classes](/static/assets/img/blog/web/02MakeServlet/13classes.png){:width="40%" height="40%"}

Finish를 눌러 프로젝트를 생성합니다. 

![15_dynamicFinish](/static/assets/img/blog/web/02MakeServlet/15_dynamicFinish.png){:width="40%" height="40%"}

우선 servlet을 만들건데 기본적으로 프로젝트에서 우클릭 후에 new를 누르면 servlet을 만들 수 있지만 학습을 위해 클래스 파일부터 만들어봅니다. 이름은 GenericServletTest1으로 하겠습니다.

![16_createClass](/static/assets/img/blog/web/02MakeServlet/16_createClass.png){:width="40%" height="40%"}

~~~java
package servlet.generic;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.GenericServlet;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;

public class GenericServletTest1 extends GenericServlet{
		@Override
	public void service(ServletRequest req, ServletResponse res) throws ServletException, IOException{
		PrintWriter out = res.getWriter();
		out.println("<html><body bgcolor='yellow'>");
		out.println("<h2>Hello!!!GenericServlet!!!</h2>");
		out.println("</body></html>");
		
		out.close();
	}
	//http://127.0.0.1:8888/web01_GenericServlet/GenericServletTest1
}
~~~

GenericServlet abstract class를 재정의 해야하므로 `extends GenericServlet`을 붙였습니다. 

그리고 재정의할 메소드는 바로 service입니다. 우선 일련의 요청을 수행했다고 치고 인자 ServletResponse res를 다뤄보도록 하겠습니다. 

res instance에서 getWriter()를 사용해서 java의 입출력 객체인 PrintWriter Object를 반환할 수 있습니다. 그리고 PrintWriter Object에서 println(args)메소드를 이용해 브라우저로 내용을 보낼 수 있습니다. 이번 경우 html태그들을 보내면 되겠죠. 

전부 보내고 close()메소드를 통해 객체를 닫아줍니다.

여기서 그냥 실행하면 Page 404 페이지가 뜨는데 이 그 이유는 WebContent\WEB-INF\web.xml파일을 잘못만들었기 때문입니다. 
<br>
<br>

## web.xml
web xml은 web application의 설정을 위한 deployment descriptor입니다. 

Deploy할 때 Servlet의 정보를 설정해줍니다. 브라우저가 Java Servlet에 접근하기 위해서는 WAS(Web Application Server)에 필요한 정보를 알려줘야 해당하는 Servlet을 호출할 수 있습니다. 

* 배포할 Servlet이 무엇인지
* 해당 Servlet이 어떤 URL에 매핑되는지
를 알려줘야 합니다. 

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
</web-app>
~~~
위와 같이 web.xml을 바꿔줍니다. xml파일은 메타데이터로 쓰이는데 정보에 대한 의미를 담고 있기 때문입니다. 

`<servlet>`태그는 servlet 인스턴스를 생성한다는 의미입니다. servlet-class는 servelt.generic.GenericServletTest1클래스를 사용하는 것이고 여기에 GenericServletTest1이라는 이름을 붙여주었습니다. 

`<servlet-mapping>`은 브라우저의 URL에 어떤 servlet이 매핑되는지를 설정하는 것입니다. 우리는 요청을 생략했으므로 url-pattern을 비워놔도 괜찮습니다. 

이제 web.xml도 고쳤으니 다시 실행을 해봅니다. 페이지가 정상적으로 로드되는 것을 확인할 수 있습니다. 

![18resultGeneric](/static/assets/img/blog/web/02MakeServlet/18resultGeneric.png){:width="40%" height="40%"}

