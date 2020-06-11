---
layout: post
title: "Page Moving in Code"
date: 2020-06-04
desc: "Page moving mechanism in server data transferring."
keywords: forward, server, request, response, include, redirect, RequestDispather, attribute 
categories: [Web]
tags: [forward, server, request, response, include, redirect, RequestDispather, attribute]
---
해당 게시글은 웹을 공부하기 위해 개인적으로 기록했던 자료입니다.
<br>
<br>

## include

___

![04include](/static/assets/img/blog/web/03Attribute/04include.png)
<br>
위와 같이 텍스트를 하나 입력하고 Servlet으로 이동한 뒤에 include방식으로 페이지 이동을 하겠습니다. 

~~~java
	protected void doProcess(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String id = request.getParameter("id");
		request.setAttribute("id", id);
		RequestDispatcher rdp = request.getRequestDispatcher("includeTest.jsp");
		//rdp.forward(request, response);
		rdp.include(request, response);
		PrintWriter out = response.getWriter();
		out.println("이거 안뜸");
		
	}
~~~
<br>

includeTest.jsp

~~~html
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2><b>INCLUDE TEST...</b></h2>
<img alt="" src="img/book.jpg" width="20%" height="20%">
</body>
</html>
~~~
<br>

![05includeResult](/static/assets/img/blog/web/03Attribute/05includeResult.png)
<br>
위와 같이 includeTest.jsp의 내용이 뜬 다음 Servlet에서 PrintWriter로 만들어준 내용도 같이 출력되는 것을 확인할 수 있습니다. 그리고 URL을 보면 마지막에 Servlet의 url-pattern으로 끝나는 것을 확인할 수 있습니다. 
<br>
<br>

## Redirect

___

redirect2.html

![06redirect](/static/assets/img/blog/web/03Attribute/06redirect.png)
<br>

위와 같이 Form을 만들어준 뒤 Servlet으로 보내겠습니다.
<br>

RedirectServlet2.doProcess()

~~~java
protected void doProcess(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String value= request.getParameter("choose");
		if (value == null)
			response.sendRedirect("error/error.html");
		else {
			request.setAttribute("choose", value);
			RequestDispatcher rdp = request.getRequestDispatcher("checkResult.jsp");
			rdp.forward(request, response);
		}
		
	}
~~~
<br>

체크박스가 체그가 안돼있으면 error.html로 Redirect를 하고 체크가 되어 있으면 forward방식으로 checkResult.jsp페이지로 넘어갑니다.

forward방식을 사용하기 위해 RequestDispatcher 객체를 사용한 것에 주의를 기울여야 합니다. 그리고 url을 통해 제어권이 Servlet에 남아있다는 것을 확인할 수 있습니다. 

![07redirecError](/static/assets/img/blog/web/03Attribute/07redirecError.png)
<br>

Redirect방식은 Servlet의 제어권에서 나와서 다시 브라우저가 해당 페이지로 요청하는 방식이기 때문에 URL이 error.html로 끝나는 것을 확인할 수 있습니다. 

![08redirecErrordd.png](/static/assets/img/blog/web/03Attribute/08redirecErrordd.png)