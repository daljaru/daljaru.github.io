상속 2개. 


interface -> 컴포넌트 기반.

oop핵심. 

클래스끼리 상속은 재사용성이 떨어진다.    재사용성이 떨어지려면 coupling이 낮아져야 하는데 

부모가 만들어지고 jvm에 memory에 올라가고 자식이 거기에 붙어서.....  가장 coupling이 높다..... 헐 ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ

그래서 interface를 쓰는게 낫다.


오늘은 

1. presentation설정

2. 설정문서들의 wiring.

3. 이거 머지 ㅋㅋ?ㅋ?ㅋ?ㅋ?ㅋ?ㅋ?ㅋ?ㅋ?ㅋ?ㅋ?ㅋ?ㅋ?ㅋ?  spring vui restful까지. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4. 형태는 workshop이지만 실제로는 테스트. . . . . . . . . . . .시간은 하루. 그만큼 꼼꼼히. . . . .  workshop은 오늘 바로 낼 거임.

file new other spring legacy project  -> templates -> Spring MVC Project -> top level package 이름 설정하고 finish

폴더 다각화를 왜 했니. 

src를 다각화.

pom.xml-> org frame work version 4.1.1로 변경 -> 다시 라이브러리 긁어옴. 

dependencies -> dependency 하나가 라이브러리 하나.  

.m2 > repository > org > springframework

web하려면 web , webmvc

jdbc는 없다. 이건 나중에 dependency추가해야함. 

mybatis도 dependency추가해야함.

몇명은 잘 못 내려질 때가 있다. 그 때는 이 .m2폴더를 삭제하고 다시 maven project를 만든다.  > 이 방법이 제일 깔끔한 방법임.

webapp > new > index.jsp

com.encore.spring-> controller.java  
import org.springframework.web.servlet.mvc.Controller;

WEB-INF -> spring, views

views : 결과페이지를 저기에 넣어라. 

WEB-INF 디렉토리가 가지고 있는 의미. -> 정적인 문서와 동적인 문서를 나누는 기준이 되는 ....... ㅠㅠ  주소창에서 치고 접근을 못함.

우리는 주문서만 만들면 된다. -> DI가 해주고. 

이거를 tomcat이 해준다. 




web.xml  servletname->  dispatcher

url-patten *.do   확장자가 있을 때 / 안함. 

