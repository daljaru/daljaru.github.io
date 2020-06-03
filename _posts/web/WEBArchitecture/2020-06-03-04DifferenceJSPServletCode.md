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

결론 : JSP파일도 Servlet파일로 변환된다.


