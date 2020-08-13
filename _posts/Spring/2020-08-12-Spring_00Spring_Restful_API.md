front UI - presentation layer - business logic layer(service layer + persistence layer) - mybatis framework.(단위테스트 중요)

controller리턴 타입 -> model and view..   string으로 넘겨주고   데이터는 모델이 넣고. 
데이터를 받아서 화면을 넘겨주는 것. 마지막 결론이 화면....마지막 결론이 결과페이지 . . . . 결과페이지가 서버사이드에 존재해서... 이 결과페이지를 넘겨줌.  동적인 문서. . jsp




..
.
.
.
..
.
.
기기가 다양해졌을때....


restful API는 @RestController...데이터만 리턴한다. (Presentation layer에서..)

프론트하고 서버 사이드하고 독립된다.

프론트는 데이터만 받아서 원하는대로 만들면 된다. jsp(x)  ->  vue.js,, html로만 짠다. 


그래서 서버사이드는 restful로 가야하고 front는 vue.js...->  통신은 비동기로. 



마지막으로 spring boot에 얹혀서.. 

1. maven기반 하나. 
2. spring boot기반 하나. 



cross origin

??

restful에서는 doDelete, doGet, doPost, doPut이렇게 네가지를 쓴다.

delete query - > doDelete

insert query -> doPost

update query -> doPut

select query -> doGet


restful  데이터(객체가) 나타나야 하는데  json형태로 나타나야 하기 때문에... . 라이브러리가 반ㄷ시 필요. 



restful  에서  map형식으로 반환하는게 좋다. . . . . . 