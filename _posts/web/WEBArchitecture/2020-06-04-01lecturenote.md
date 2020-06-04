attribute

business logic

전체적인 흐름

servletContext는 WAS가 가동하자마자 만들어진다. 



redirect vs fowarding을 가장 많이 쓴다. 


폼값 받고
vo만들고 
dao만들고
business로직 만들고

SErvletRequet or Servelt Context or HTTPSession에 데이터 보관

forwarding : 서버상에서 다이렉트로 이동. 

forwarding에 대한 설명 . . . . 구축구축구축

ServletRequest안에 getRequestDispatcher("url")이 있고


RequestDispatcher라는 객체의 메소드에 forward(req, res)가 있다. 


다시 정리

화면에서 (동적인)요청이 들어오면
서버상에서 제일 먼저 dd를 읽고
SErvletContext가 만들어지고
dd에 매핑되어져있는 Servlet을 만들고

Servlet을 만든직후에 만들어지는 객체가 ServletConfig이고
filtering..상태....

여기까지가 ready on상태. ==요청이 들어오기전 모든 상태. 

그리고
init()을 실행하면서 외부자원으로 필드 초기화.
SErvlet Request, ServletREsponse가 알아서 만들어지고
콘트롤러가 폼값을 받아서
vo생성하고
dao를 리턴하고
business로직을 호출하고 serVletRequest의 rdp를 부르고 rdp의 foward를 불러서 req res를 보내고 view에서 requestgetattribute를 해서 화면에 출력.

