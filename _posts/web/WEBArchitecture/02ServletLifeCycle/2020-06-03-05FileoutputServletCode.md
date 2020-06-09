---
layout: post
title: "File IO in Servlet code"
date: 2020-06-03
desc: "File IO in Servlet code"
keywords: file, servlet, init, destroy, BufferedReader, io
categories: [Web]
tags: [file, servlet, init, destroy, BufferedReader, io]
---
해당 게시글은 웹을 공부하기 위해 개인적으로 기록했던 자료입니다.
<br>
<br>
## Simple File I/O in Servlet Life cycle
___

init(), destroy()와 같은 메소드들을 call back method라고 합니다. 

서버가 켜져있는 동안 Servelt 인스턴스에 있던 필드의 값들은 서버가 꺼짐과 동시에 사라지게 되니까 영구히 저장하려면 별도의 저장공간에 저장하는 방법밖에 없습니다. 

Servlet Life cycle에서 데이터를 Database로부터 불러오고 반대로 저장하는 시기는 init()과 destroy() method가 호출될 때 입니다. 

init()을 시작하면서 Servlet의 구성요소(field)를 초기화하는 과정에서 Database에서 정보를 불러와야하고 서버가 꺼지기 전에 (destroy()method가 작동되기 전에) Database에 정보를 저장해야 합니다.
<br>
<br>


___

Servlet을 통해서 간단하게 파일 입출력 과정을 작성해보겠습니다.

ServletConfig2Text Servlet의 init()메소드를 아래와 같이 작성합니다. 

~~~java
public void init() throws ServletException {
        System.out.println("ServletConfig2Test init()...");
		path = getInitParameter("path");
		try {
			BufferedReader br = new BufferedReader(new FileReader(path));
			String line = br.readLine();
			count = Integer.parseInt(line);
			br.close();
			System.out.println("이제까지"+count+"명이 왔다갔습니다.");
		}
		catch(IOException e) {
			System.out.println(e.getMessage());
		}
	}
~~~

Servlet의 Lifecycle상 init()메소드는 Servlet의 구체적인 인스턴스의 초기화를 위해 실행이됩니다. 그렇게 때문에 여기에서 external resource로 정의된(web.xml에 정의된) path를 가져옵니다. 그리고 파일에서 데이터를 읽어옵니다. 

이후 브라우저에서 요청이 들어오면 해당 Servelt이 가지는 기능을 실행하고 서버가 종료되면 destroy를 통해 파일에 데이터를 저장합니다. 

doProcess(request, response)
<br>

~~~java
protected void doProcess(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("ServletConfig2Test doProcess()...");
		count++;
		request.setCharacterEncoding("UTF-8");
		response.setCharacterEncoding("UTF-8");
		response.setContentType("text/html; charset=UTF-8");
		
		String name = request.getParameter("name");
		
		PrintWriter out = response.getWriter();
		out.println("<html><body>");
		out.println("<h2>"+name+"님은 "+count+"번째로 입장하셨습니다.</h2>");
		out.println("</body></html>");
		out.close();
	}
~~~
<br>

destroy()
<br>

~~~java

	@Override
	public void destroy() {
        System.out.println("ServletConfig2Test destroy()...");
		File file = new File(path);
		file.getParentFile().mkdirs();
		try {
			PrintWriter pw = new PrintWriter(new FileWriter(file));
			pw.println(count);
			pw.close();
			System.out.println(path+" count 값: "+count+"을 파일에 저장함.");
		}
		catch(IOException e){
			System.out.println(e.getMessage());
		}
	}
~~~
<br>

![41fileio](/static/assets/img/blog/web/02ServletLifeCycle/41fileio.png)


