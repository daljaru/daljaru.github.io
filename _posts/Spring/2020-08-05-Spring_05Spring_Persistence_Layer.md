spring

servlet oop layer

~~~java
'''
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



단위 테스트가 성공적이다. -> DAO오류난다?   dao만 보면 됨. 

단위 테스트를 안했다. -> 오류난다? -> 망함. 


'''
~~~