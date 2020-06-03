---
layout: post
title: "Servlet response"
date: 2020-06-02
desc: "more specific about servlet response..."
keywords: web, html, servlet, server, WAS, tomcat, container, request
categories: [Web]
tags: [web, server, servlet, tomcat, container, WAS, httpservletresponse]
---

## post방식

___

아래의 두 코드를 가지고 post방식을 이야기 해보겠습니다. 이번엔 form.html의 `<form>`태그에 post method방식으로 넘겨보겠습니다.
<br>

~~~html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>Form Data..</h2>
<form action="FS" method="post">
ID <input type="text" name="userId"><br/><br/>
PASS <input type="password" name="userPass"><br/><br/>
<strong>좋아하는 메뉴....</strong><p>
<input type="checkbox" name="menu" value="짜장면">짜장면
<input type="checkbox" name="menu" value="김치볶음밥">김치볶음밥
<input type="checkbox" name="menu" value="닭도리탕">닭도리탕
<input type="checkbox" name="menu" value="파스타">파스타
<br/><br/>
<input type="submit" value="DataSend">
</form>
</body>
</html>
~~~
<br>

<br>

~~~java
package servlet.form;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class HttpFormServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		
		String id = request.getParameter("userId");
		String pass = request.getParameter("userPass");
		
		String[ ] menus = request.getParameterValues("menu");
		
		PrintWriter out = response.getWriter();
		
		out.println("<html><body><h2>정보를 출력합니다....</h2>");
		out.println("<li>당신의 아이디 "+id+"</li>");
		out.println("<li>당신의 패스워드 "+pass+"</li>");
		
		out.println("<b>당신이 좋아하는 음식들 입니다.</b><br/>");
		String menu = "";
		for(int i=0; i<menus.length; i++) {
			menu += menus[i]+" ";
		}
		out.println(menu);
		out.println("</body></html>");
		out.close();
	}
}
~~~
<br>

form.index를 실행시키면 아래와 같이 나옵니다.
<br> 

![26post](/static/assets/img/blog/web/02MakeServlet/26post.png){:width="100% height="100%"}
<br>
주소창을 확인해보면 servlet-mapping까지만 url정보가 가는 것을 확인할 수 있습니다. 그렇다면 서버는 post방식에서 어떻게 브라우저가 전송한 데이터를 볼까요.

http규약에 보면 브라우저가 전송하는 요청데이터 포맷은 아래와 같이 구성되어 있습니다. 

![27requestFormat](/static/assets/img/blog/web/02MakeServlet/27requestFormat.png){:width="70% height="70%"}

get 방식은 request Line과 header까지만 사용한다면 post방식은 body까지 사용합니다. 그리고 이 body부분은 일반적으로 확인할 수 없습니다. 

F12를 누르고 개발자 모드에서도 확인해보면 header까지만 확인할 수 있는 것을 알 수 있습니다. 

![28requestFormat02](/static/assets/img/blog/web/02MakeServlet/28requestFormat02.png){:width="80% height="80%"}

method방식은 Query String이 아니라 Form data형식으로 확인이 됩니다. 하지만 URL에서는 확인할 수 없습니다. 

그렇기 때문에 method방식은 request.setCharacterEncoding()메소드를 통해 한글인코딩을 해줘야합니다. 만약 인코딩을 해주지 않는다면 한글깨짐 현상이 발생합니다.

