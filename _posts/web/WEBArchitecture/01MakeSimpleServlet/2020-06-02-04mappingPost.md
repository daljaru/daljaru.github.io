---
layout: post
title: "Data request through URL"
date: 2020-06-02
desc: "how to request data through URL"
keywords: web, html, servlet, server, WAS, tomcat, container, request
categories: [Web]
tags: [web, server, servlet, tomcat, container, WAS, httpservletrequest, httpservletresponse, doget, dopost, service]
---
해당 게시글은 웹을 공부하기 위해 개인적으로 기록했던 자료입니다.
___
<br>
<br>
## Get방식의 쓰임새

___

Get방식이 또 어떻게 쓰일 수 있는지 확인해 보겠습니다. 먼저 아래와 같은 login.html파일을 만들어보겠습니다.
<br>

~~~html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>

<style type="text/css">
	#loginbox{
		width: 600px;
		height: 200px;
		border: 1px solid black;
		align-content: center;
	}
	#bookimg{
		width: 300px;
		height: 200px;
		float: left;
	}
	td{
		text-align: right;
	}
	#loginbutton{
		color: white;
		background-color: #58B850;
		width: 100px;
		height: 30px;
	}
</style>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script type="text/javascript">
$(function(){
	$("#loginbutton").click(function(event){
		var id = $('#idText').val();
		var pw = $('#pwText').val();
		if(id==""){
			alert("아이디를 입력하세요.");
			event.preventDefault();
			return;
		}
		if(pw==""){
			alert("패스워드를 입력하세요.");
			event.preventDefault();
		}
	});
});
</script>


</head>
<body>
<div id = "loginbox">
	<div id="bookimg">
		<img src="img/book.jpg" height="100%">
	</div>
	<div>
		<form action="login" method="post">
			<h3>Login...</h3>
			<table>
				<tr>
					<td>ID</td>
					<td><input id="idText" type="text" name = "userId"></td>
				</tr>
				<tr>
					<td>PW</td>
					<td><input id="pwText" type="password" name = "userPassword"></td>
				</tr>
				<tr>
					<td></td>
					<td>...............................................</td>
				</tr>
			</table>
			<input id = "loginbutton" type="submit" name="button" value="login">
		</form>
	</div>
</div>
</body>
</html>
~~~
<br>
아래와 같은 UI를 만듭니다.
<br>

![30login](/static/assets/img/blog/web/01MakeSimpleServlet/30login.png)

<br>
아이디와 패스워드를 입력하면 로그인 성공페이지 혹은 로그인 실패 페이지로 넘어가게 됩니다. 우선 login버튼을 눌렀을 때 로직을 처리할 Servlet을 만들어야 합니다. 

그리고 로직을 처리하면서 로그인이 실패하면 로그인 실패 화면으로 넘어가야하고 로그인이 성공하면 성공화면으로 넘어가야 하기 때문에 각 로직을 처리할 로그인성공, 실패 Servlet을 추가로 만들어줍니다. 

<br>

![31ServletExplorer](/static/assets/img/blog/web/01MakeSimpleServlet/31ServletExplorer.png)

<br>
LoginForm.java
<br>

~~~java
package servlet.loginForm;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Enumeration;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class LoginForm extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    public LoginForm() {
        super();
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doProcess(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doProcess(request, response);
	}
	
	protected void doProcess(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("UTF-8");
		response.setCharacterEncoding("UTF-8");
		response.setContentType("text/html;charset=UTF-8");
		
		
		String id = request.getParameter("userId");
		String password = request.getParameter("userPassword");
		
		if(id.equals("encore") && password.equals("1234")) {
			response.sendRedirect("LS?id="+id);    
		}
		else {
			response.sendRedirect("LE");
		}		
	}
}

~~~
<br>
LoginForm.java에서 우리가 봐야할 점은 request와 response인스턴스로 미리 한글인코딩을 진행했다는 점입니다. 그리고 getParameter("name")으로 속성의 값을 받아오고 있다는 점, 마지막으로 sendRedirect("url")을 통해 페이지 Redirection을 진행하고 있습니다. 

Redirection이란 서버가 URL을 읽고 해당 URL로 다시 응답처리를 진행하는 것을 말합니다. sendRedirect()메소드에서 URL을 적는 부분을 중요하게 봐야하는데  바로 여기에 web.xml파일에서 적었던 `<url-pattern>`태그의 값을 적어야한다는 점입니다. 그리고  get방식에서 봤던 것과 같이 **`?`**뒤에 속성=값의 방법으로 데이터를 요청하고 있다는 것을 알 수 있습니다.
<br>
<br>

LoginSuccess.java
<br>

~~~java
package servlet.loginForm;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class LoginSuccess extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    public LoginSuccess() {
        super();
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doProcess(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doProcess(request, response);
	}
	
	protected void doProcess(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("UTF-8");
		response.setCharacterEncoding("UTF-8");
		response.setContentType("text/html;charset=UTF-8");
		
		
		String id = request.getParameter("id");

		PrintWriter out = response.getWriter();
		out.println("<html><body>");
		out.println("<div id='loginSuccessBox'>");
		out.println("<h2>"+id+"님이 로그인 되었습니다.</h2>");
		out.println("<a href='register?id="+id+"'>도서등록</a>");
		out.println("<a href='logout?id="+id+"'>로그아웃</a>");
		out.println("</body></html>");
		out.close();
	}
}

~~~
LoginSuccess.java에서는 로그인이 성공했을 경우에 대한 페이지가 들어갑니다. LoginForm.java에서 로그인이 성공했을 때 LS?id=id의 방식으로 데이터를 전송했기 때문에 request.getParameter("id")로 id를 다시 가져오는 것을 알 수 있습니다.
<br>
<br>
LoginError.java
<br>

~~~java
package servlet.loginForm;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class LoginError extends HttpServlet {
	private static final long serialVersionUID = 1L;

    public LoginError() {
        super();
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doProcess(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doProcess(request, response);
	}
	
	protected void doProcess(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("UTF-8");
		response.setCharacterEncoding("UTF-8");
		response.setContentType("text/html;charset=UTF-8");
		
		PrintWriter out = response.getWriter();
		out.println("<html><body>");
		out.println("<h2>로그인 실패</h2>");
		out.println("</body></html>");
		out.close();
	}

}

~~~
<br>

Servlet은 로직중심의 파일이여야하기 때문에 애초에 PrintWriter out을 이용해서 태그를 작성하는 것이 적절하지 않습니다. 이런 태그방식의 표현은 jsp로 작성하는 것이 좋습니다. 그러나 잠깐동안의 학습을 위해 적었습니다. 

요약하자면 Get방식의 ?속성=속성값 기술방법이 데이터를 어떻게 전송할 수 있는지 확인했습니다. 