spring

servlet oop layer

~~~java
'''
Presentation Layer

DispatcherServlet - HandlerMaping
                  - Controller
                  - ModelAndView

====================================
Service Layer

User Service
    |
userServiceImpl

=============================================     
Persistence Layer

userDAO
    |
MyBatisUserDaoImpl


MyBatisTestApp102 
    |
Persistence Layer단위테스트

=================================

MyBatisFramework
      SQLSession, SqlSessionFactory  -----MySQL
        |
    SqlConfig       ------------User
    |                   |
dbconn.properties       useservice01.xml

MyBatisTestApp101

MyBatis Framework 단위테스트 -> UnitTest..

========================================


단위 테스트가 성공적이다. -> DAO오류난다?   dao만 보면 됨. 

단위 테스트를 안했다. -> 오류난다? -> 망함. 


'''
~~~


framework는 소통. 

실제클래스는 설정문서에서 


tomat도 컨테이너고 di도 컨테이너인데 어떻게 다를까

spring di
tomcat
JVM
OS
hw

객체생성은 컨테이너. 

개발자는 설정문서.

