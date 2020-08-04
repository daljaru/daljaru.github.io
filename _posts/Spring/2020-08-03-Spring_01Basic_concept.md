---
layout: post
title: "Spring basic"
date: 2020-08-03
desc: "Spring basic"
keywords: Spring, framework
categories: [Spring]
tags: [spring, framework]
---

## Spring framework

___



java에서 가장 핵심적인 프레임워크 서버사이드 현업에서 쓰인다. 

우리가 말하는 spring framework에는 spring mvc, spring di, spring jdbc, spring aop, spring security 프레임워크도 포함되어 있다. 

위 말을 하나로 말하는게 spring framework.

spring jdbc framework는 잘 안쓰고 jpa, mybatis, mibatis프레임워크를 현업에서 가장 많이 쓴다. 

jdbc framework는 일본기업에서 많이 쓴다. 



mybatis.org......튜토리얼은..한국어로 된것도 있다.... . 

Mybatis. . . . . 튜토리얼이 거의 전부다. 

spring framework....는 실상 mvc를 말하는 거일텐데.. spring framework는 여러개의 모듈들이 합쳐진거를 한번에 말하는 거다. . .

여러개의 모듈들이 모두 spring꺼를 굳이 쓰지 않아도 된다. 하나하나가 완벽한 컴포넌트이기 때문에   spring jdbc자리에 mybatis로 대체해도 되고, jpa로 대체해도 된다. 



spring mvc framework가 나오기 전에 strut1, strut2가 있었다. 

framework란 무엇인가??? ->->->->

기본을 알면... . 어떤 framework를 접하든지,, 공부하면 익숙하게 사용할 수 있다. 

![spring_structure](/static/assets/img/blog/spring/spring_structure.png)



Core container... hasing. . .


dependency injection 

의존 : 필요한 사람이 의존하는 것.  고객이 통장을 필요로 하니까 고객이 의존의 대상. 


Core Container.... Beans. Core.. Contxt   library    -> di framework. 

di framework가 구축이 된 상태에서 AOP를 끼워 넣을 수 있읍. Aspect Oriented Programming. . . . . . . . . . . 



spring jdbc. . .

mibatis를 쓰자. 


Web > 라이브러리.. . prtlet , struts는 spring mvc를 쓰기전에 쓰던거.. . 지금 안씀.



순서는 DI(dependency injection)

data access / integration



Maven 구조?   수동으로 만들어서 확실히 이해할 수 있도록. 


spring frame work의 핵심 모듈. 

core라고 부르는 di

그 다음은 aop, db framework

최종적으로 web. 

전부다 같이 돌아간다. 

그 전까지 하나하나 살펴보고 merge... . .

내가 지금 뭘 하고 있는지 항상 생각해야 한다. 

.

.

.

dependency는 뒤어서부터..? 

dao.. . service . . con->>>>   

dao에서 만든걸 Service로 넘기고. . . Controller -> handleradapter> dispatcherservlet.. 

코딩에서의 dependency 흐름.


서비스 요청흐름과는 별개. 

모든 것에는 방향성이 있다. 

전체 flow이해하기..

![spring_mvc_architecture](/static/assets/img/blog/spring/spring_mvc_architecture.png)

dependency > 

dao수정하면 > > > > >> > > >>>     연쇄적으로 수정. 

도메인별로 dao가 나오게 된다. 

집에 못가.... . . . . . . . . ㅠㅅㅠ  --> 재사용성이 떨어짐. 

enterprise급으로 가게 되면....  기존의 dependency구조는 재사용성이 떨어진다. . . 


해결책은 관계를 끊으면 되는데... 

Coupling 
 * tight한 coupling 생성자로 만드는 것. 
 * loose한 coupling setter...로 주입. 
 coupling의 발상.

 DAO와 service의 의존성 해제를 위해 di framework가 먼저 나왔다.    (dependency injection)

 DAO를 완전한 독립적인 클래스로 만들기 위한.......  -> DAO를 아무리 바꿔도 Service에 아무런 영향을 안끼치는.. . . 

 sts...


 maven 구조. 

 modeuler...


프로젝트 만들때 src를 없앴다/?
src폴더를 다각화 시킨다. . ... .. javacode,,  xml, testcode. . . 

![src_structure](/static/assets/img/blog/spring/src_structure.png)


지금 maven 구조..를 만들고 있는 것. 


현업에서는 5개이상의 패키지를 쓴다. (최소)


spring framework > service > hello 도메인


![first_web_project](/static/assets/img/blog/spring/first_web_project.png)



plain  어느 것으로부터 제약 받지 않는. 


interface도 없는 ...  생성자 getter, setter만 있는. . . .



~~~java
Hello hello = new HelloImpl()

/*

HelloImpl() 구상객체, 실체클래스. 실제로 메모리에 올라가는 클래스.  component bean 

재사용성을 높이는 방법은 인터페이스 코드의 실체클래스명이 언급되면 안되는 것. 

-- > 객체생성은 내가 안하고 컨테이너에게 맡기는 것. . . . . . 이것도 재사용성을 높인다.



hello           DI container (core container)   helloAppTest02
heloImpl            1. 생성
                    2. 저장


개발자는 주문서를 만든다. 
*/
~~~

라이브러리 사이에 dependence가 일어남????/


인터페이스를 써도 재사용성이 늘어나긴 하는데  new 키워드를 쓰긴 쓴ㄷ다. 


그래서 객체생성 역할을 다른 곳으로 위임해주는에 di container로 위임한다. 

hellofactory를 생각하면 쉬운데       ==> new를 생성하는 권한을 컨테이너한테 준ㄷ. ioc (제어의 역전) 


~~~java
'''
DAO                 BeanContainer (-> 추상 컨테이너)....
                        XMLBeanContainer -> 
|                   1. Bean을 생성하고 
                    2. 생성한 Bean을 보관. 
DAOImpl             3. 다른 기능은 다른 컨테이너가 있다.. . XMLBeanContainer는 deprecated...
                    개발자는 설정문서. bean.xml  -> Bean설정문서. .(Bean Configuration file) . 

                    컨테이너가 주문서를 읽어들인다. 



'''
~~~

Bean이 생성되는 시점은 클라이언트가 요청을 할 때. 

pre loading은 언제 하냐??? 


