


1, db

2. vo

3. sqlmapconfig, jdbc.properties, mapping

4. sqlsessionFactory -> sqlsessionFactorybean
    sqlsession  -> sqlsessiontemplate

    crud

5. 단위테스트

자동생성기능 값이 pk일때 


기본적으로 패키지가 세개가 들어가는데  groupid artifactid, project명.

maven구조는 패키지를 세개 이상 넣는ㄷ.  groupi 

어떤 프로젝트인지.. 세번재. 






presentation layer -> disatcher servlet, handler maping, viewresolver, @ controller

service layer -> @service

persistence layer -> @repository

mybatis framework -> sqlsessiontemplate(library), sqlsessionfactorybean(library), basicdatasource(library)

mvcbean.xml, ?.xml -> DI container

web.xml  -> was



presentation layer + business logic layer => 2 architecture layer

presentation layer | business logic layer( service layer + persistence layer)

layer를 기준으로 이렇게 모듈화. . . 현업에서는 도메인별로 나누기도 한다. 

layer별로 모듈화. 





was가 구동되자마자  제일 먼저 web.xml을 만들고 

servletcontext가 제일 먼저 만들어지고. 

dispatcher > init  



이클립스에 있잖아. webapp밑에 있는 애들은 전부 다 파일 pathsystem이고 이클립승 javaResources안에 있는 애들은 classpathsystem이라고 이해하면 됩니다. 

param-value /WEB-INF/businessBean.xml을    classathsystem으로 설정해도 된다. 

