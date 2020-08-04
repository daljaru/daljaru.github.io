---
layout: post
title: "Spring mibtis"
date: 2020-08-03
desc: "Spring mibtis"
keywords: Spring, framework
categories: [Spring]
tags: [spring, framework]
---


dao가 있는 layer == persistence layer. . . . . . .persistence framework



service layer : persistence layer에 있는 데이터를 받아서 가공하는 layer. 라고 이름 붙임. 

db에 있는 데이터에 access ... persistence layer. ... ...> service layer가 받고  > dispatcher를 통해 기능. . . . . . . . . .. . . . . . . . . . . . ... . .  . .. . . . .. .


컨테이너는 일종의 소프트웨어다. . 톰캣 컨테이너와는 성격이 조금 다름.

mibatis는 RDBMS와 DAo사이에서... . 

mibatis . . .로 바꾸면 DAO의 코드를 대체함. . . 

오늘 mibatis를 다할거임. . . ?   ? ? ?  ?? ? ?? 

단위테스트도 할거임. 

xml기반의 쿼리문. .  xml기반의 mapper. . 단위 테스트, jdbc가 어떻게 바뀌는가?

파이썬 의 장고

중간 스칼라. .. .  . . . . . . AI 스칼라 연결???

자바 웹개발



mibatis3

sql mapper : sql을 mapping하는......프레임워크까지는 안부르고
stand alone용..?



mibtis하고 di하고 연결하려면  다른 걸 배워야함. 

주문서 만들기. . . . xml  모든 컨테이너를 인식할 수 있는 게 xml



jdbc코드와 수동으로 셋팅하는 파라미터와 결과 매핑을 제거한다. . .-> jdbc5단계 생략

1. 드라이버 로딩
2. 디비연결 -> connection 리턴
3. preparedStatement 생성 -> 쿼리
4. 쿼리문 실행 <executeQuery(), executeUpdate()>
5. 자원닫고   ....

SqlSessionFactorybuilder -> SqlSessionFactory > SqlSession을 얻고 ..

~~~java
'''                     mySawonClass - mysawon db
                        |
            SqlMapConfig.xml  => mibatis 의 핵심 설정문서. 
            |           |
dbconn.properties       mysawon_mapping.xml

'''
~~~

정리할 때 그림을 그리면 좋은데. . 

멀로 그리지. .

property - db서버의 상수값 정보를 메타데이터화시킨것

깔끔한 sprint boot를 만들때 property가 중요. 상수를 넣을 때 map방식으로 넣는다. 

값은 값대로 모듈화.. .끌어다 쓰는게 중요. 

