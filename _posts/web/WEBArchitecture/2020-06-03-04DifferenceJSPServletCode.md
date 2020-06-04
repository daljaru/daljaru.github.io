---
layout: post
title: "Difference between JSP and Servlet"
date: 2020-06-03
desc: "Difference between JSP and Servlet"
keywords: jsp, tomcat, servlet, tag, logic
categories: [Web]
tags: [jsp, tomcat, servlet, tag, logic, web]
---

## Servlet과 jsp의 차이

___

Servlet과 JSP는 브라우저의 요청중에서 동적인 데이터 처리가 필요한 부분을 담당한다는 점에서 같습니다. 예를 들어 폼 데이터를 버튼을 통해 전송하고 해당 데이터를 다른 곳에서 핸들링한다는 얘기입니다. 

그러나 Servlet은 Logic중심이고 JSP는 Tag기반으로 코드를 작성한다는 점에서 차이가 있습니다. 

Servlet에서는 `<>`를 통해 화면을 구성하지 않습니다. 순수하게 데이터 핸들링을 통해 결과값을 얻습니다. 반면에 JSP는 데이터 핸들링도 할 수 있고 Tag기반이라서 화면을 좀 더 쉽게 구성할 수 있습니다. Servlet은 out.println()을 해야하는 반면 JSP는 일반 HTML파일과 구성이 같습니다. 
<br>
<br>

## 그렇다면 굳이 Servlet을 쓸 필요가 있을까? 

___

결론부터 말하자면 Servlet은 인스턴스이기 때문에 동적인 페이지를 만든다면 무조건 생성됩니다. 그렇기 때문에 안쓰는 선택지를 고려할 수 없습니다. ?? JSP가 있는데 무슨말이지 하겠지만 종국에는 JSP파일이 Servlet파일로 변환된다는 말입니다.

앞에서 썼던 life cycle 코드에 jsp파일을 추가해보겠습니다. 
<br>

~~~html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2 align="center">LifeCycle...CallBack Method Test...</h2>
<a href="Life2">LifeCycle Test...Click</a>
</body>
</html>
~~~
<br>

a href의 링크를 Life2로 줍니다. xml에서는 url-pattern Life2가 Servlet과 연결되어 있습니다. 그리고 Servlet안에서 jsp와 연결할 것입니다. 
<br>

~~~java
package servlet.life;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class ServletLifeCycleTest2 extends HttpServlet {
	private static final long serialVersionUID = 1L;
	private int count = 0;
       
    public ServletLifeCycleTest2() {
    	super();
    	System.out.println(this.count+" ServletLifeCycleTest2 constructor....by container");
        
    }
	public void init() throws ServletException {
		System.out.println(this.count+" ServletLifeCycleTest2 init....by container");
	}
	
	public void destroy() {
		System.out.println(this.count+" ServletLifeCycleTest2 destroy....by container");
	}
	
	public ServletConfig getServletConfig() {
		return null;
	}
	
	public String getServletInfo() {
		return null; 
	}

	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		this.count++;
		System.out.println(this.count+" ServletLifeCycleTest2 service....by container");
		response.setContentType("text/html; charset=UTF-8");
		
		PrintWriter out = response.getWriter();
		out.println("<a href='life2.jsp?cnt="+count+"'>life2.jsp로 이동합니다</a>");
		out.close();
	}
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("doGet....");
		service(request, response);
	}
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("doPost....");
		service(request, response);
	}
	
}
~~~
<br>
Local 환경에서 Tomcat home으로 들어가서 배포된 파일들을 보겠습니다.
<br>

![38jspdeploy](/static/assets/img/blog/web/02MakeServlet/38jspdeploy.png)
<br>

tomcat-home> webapps안에 배포되게 했었습니다. root context안에 WEB-INF는 동적인 프로그램들이 들어가야 하는데 jsp파일은 그 바깥에 있습니다. jsp파일은 태그기반이기 때문에 html파일들이 배포되는 곳과 동일한 곳에 배포가 됩니다. 

![39jspdeploy2](/static/assets/img/blog/web/02MakeServlet/39jspdeploy2.png)

Tomcat home에서 work폴더로 들어가면 Catalina라는 폴더가 나옵니다. 톰캣은 여러개의 기능으로 구성되어 있는데 Tomcat의 core component은 Catalina라고 말합니다. Servlet스펙의 실질적인 구동을 담당하고 있습니다. 

Catalina에 들어가면 localhost > root context이름을 가진 폴더들이 나옵니다. 그 안에 org>apache>jsp파일로 들어가면 우리가 작성했던 jsp파일들이 확장자가 .java로 가진것과 .class를 가진것을 볼 수 있습니다. 

.java확장자로 가진것이 바로 .jsp파일이 Servlet파일로 변환된 모습입니다. life2_jsp.java파일을 Editplus로 열어보면 아래와 같은 java코드를 볼 수 있습니다. 
<br>
Servlet으로 변환된 jsp파일. 

![40jsptoServlet](/static/assets/img/blog/web/02MakeServlet/40jsptoServlet.png)

