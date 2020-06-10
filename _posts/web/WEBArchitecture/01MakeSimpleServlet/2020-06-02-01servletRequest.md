---
layout: post
title: "Servlet request"
date: 2020-06-02
desc: "more specific about servlet request..."
keywords: web, html, servlet, server, WAS, tomcat, container, request
categories: [Web]
tags: [web, server, servlet, tomcat, container, WAS, httpservletrequest]
---
해당 게시글은 웹을 공부하기 위해 개인적으로 기록했던 자료입니다.
___
<br>
<br>
## Get과 Post

___

html을 공부하다가가 `<form>`태그를 공부하면 필수속성이 action과 method라고 배우게 됩니다. method에 get이 default로 들어가고 또다른 속성값으로 post가 들어간다는 것을 배우고 get는 입력값을 url상으로 넘겨주고, post는 url상으로 넘겨주지 않는다는 것을 배우게 될 것입니다. 그리고 보안상 post를 써야 좋다는 것을 배웁니다.

이 과정이 너무 두루뭉술한 배움이므로 여기서 앞으로 자세하게 다뤄봅시다.

Eclipse에서 새롭게 Dynamic Web Project를 만들어서 아래와 같은 html파일을 만들었습니다. checkbox를 표현한 화면입니다. 

form 태그의 action은 FS라고 지정했습니다. web.xml의 URL-mapping태그와 일치하는 값입니다. 그리고 method를 따로 지정을 안해주었으므로 get방식이 될 것입니다.

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
    <form action="FS">
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

그리고 Servlet파일을 아래와 같이 만들어줍니다.
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
		//request.setCharacterEncoding("utf-8");
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
이 Servlet은 HttpServlet을 상속받고 있습니다. 그리고 메소드는 service()메소드를 사용하고 있습니다.
<br>
form.html을 구동하고 주소값을 한번 확인해봅니다. localhost:8888이라는 ip주소와 포트번호<br>
web02_HttpServletForm이라는 Context content<br>
마지막으로 그 안에 있는 form.html인 것을 확인할 수 있습니다.

입력값과 체크박스를 선택한뒤 DataSend버튼을 누르겠습니다. 

![22get](/static/assets/img/blog/web/01MakeSimpleServlet/22get.png){:width="60% height="60%"}

<br>

![23get02](/static/assets/img/blog/web/01MakeSimpleServlet/23get02.png){:width="100% height="100%"}
<br>
위의 주소창을 한번 보겠습니다. 톰캣안에서 배포된 파일의 위치가 나오는데<br>
localhost:8888이라는 ip주소와 포트번호, web02_HttpServletForm이라는 content context, 그 다음에 FS라는 servlet-mapping정보가 들어갑니다. `<form action="FS">`이렇게 지정했기 때문에 FS라는 값이 나오는 것입니다.

그 뒤에 ?가 나오고 name속성과 그 값이 `=`를 사이에 두고 적혀진것을 확인할 수 있습니다. 그리고 각 상은 `&`를 사이에 두고 출력이 됩니다.
<br>
<br>

## UTF-8 Encoding

___

~~~java
request.setCharacterEncoding("utf-8");
response.setContentType("text/html;charset=utf-8");	
~~~

한국어를 웹브라우저 상에서 서버로 보내고 서버에서 웹 브라우저로 보내려면 UTF-8인코딩이 필요합니다. 위의 Servlet java파일에서도 적혀있듯이 serCharacterEncoding()과 serContentType으로 인코딩이 진행됩니다.

이 인코딩 코드는 request, response instance를 사용하기 이전에 반드시 작성되어야 합니다. 만약 request.getParameter("...")이후에 request.setCharacterEncoding("utf-8")을 적으면 에러가 납니다. 마찬가지로 response.getWriter()메소드를 작성하고 난후 response.setContentType("text/html;charset=utf-8")을 작성하면 에러가 발생합니다. 

![24encoding.png](/static/assets/img/blog/web/01MakeSimpleServlet/24encoding.png){:width="100% height="100%"}

당연히 인코딩을 먼저 하고 데이터를 보내는게 순서에 맞습니다.

## Get방식과 Query string

___

그런데 위 Servlet코드에서는 request.setCharacterEncoding() Method가 주석처리 되어있습니다. 그럼에도 불구하고 결과값이 잘 나오고 있습니다. 

**굳이 인코딩을 할 필요가 없었기 때문입니다.**

get 방식은 페이지를 불러오는게 주된 목적이고 데이터를 전달하는 것은 부수적입니다. 그리고 페이지를 요청할때 URL로 ?뒤에 name속성과 그 속성값을 전달하게 됩니다. URL의 일련의 문자열을 Query String이라고 부릅니다. 

브라우저에서도 확인할 수 있습니다. F12번을 눌러 개발자 모드로 진입한 후 Network탭으로 들어가면 아래와 같은 화면을 확인할 수 있습니다. 

![25queryString](/static/assets/img/blog/web/01MakeSimpleServlet/25queryString.png){:width="100% height="100%"}

Query String의 값으로 userId와 userPass와 menu가 넘어가는 것을 확인할 수 있습니다.

이렇게 Query String으로 속성=속성값을 넘기는 것은 매우 중요합니다. 다른 예제에서 더 살펴보도록 하겠습니다. 이렇게 get방식은 url로 정보요청이 이루어진다는 것을 알 수 있었습니다.
