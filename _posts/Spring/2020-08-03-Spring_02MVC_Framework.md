---
layout: post
title: "Non-Spring MVC Pattern"
date: 2020-08-03
desc: "Non-Spring MVC Pattern"
keywords: Spring, framework, model, view, controller
categories: [Spring]
tags: [Spring, framework, model, view, controller]
---

해당 게시물은 Spring Framework를 공부하기 위해 개인적으로 공부했던 자료입니다. 현업에서 쓰이는 코드와는 무관합니다. 기본적인 베이스를 탄탄히 다지는 코드들로 점근적으로 빌드업하는 방향으로 쓰여졌습니다. 

<br>

## Non-Spring-MVC Pattern

___

Spring의 DI_Framework를 알아보기 전에 Spring Framework를 적용하기 전의 mvc pattern이 어떤지 복습하는 시간을 필요할 것 같습니다. 

![nonspringmvc](/static/assets/img/blog/spring/nonspringmvc.png)

위 그림은 제가 아주 간단하게 그린 web mvc pattern의 기본적인 구조입니다. 

Client가 Web server에 있는 Webpages을 통해 서버에 요청을 하면 Web Application server에 있는 dispather가 작동하면서 맞물려 있는 handlermapping, controller, dao클래스등이 작동하게 됩니다. 

노란색 박스로 제가 표시한 부분은 생성자가 만들어지는 부분을 아주 대략적으로 표시한 곳입니다. 

DispatcherServlet은 서버가 가동되고 생성이 될때 생성자가 만들어지고, 사용자의 요청이 들어오면 Handlermapping과 Controller의 생성자가 만들어집니다. 그리고 각 Controller안에서 비즈니스로직을 실행하기 위해 DAO의 생성자가 만들어지게 됩니다. 

<br>

## 생성자가 만들어지는 부분을 강조한 이유? -> 의존

___

여기서 **의존(dependency)**에 대해서 살펴봐야 합니다. 

Java Programming에서 한 클래스가 다른 클래스를 Hasing하는 방법은 크게 보면 2가지입니다. 

A 클래스에서 B클래스 타입의 변수를 **필드영역**에 일단 생성하고 B클래스의 인스턴스를

1. 생성자를 통해 주입하는 방법.

2. setter method를 통해 주입하는 방법.

이렇게 2가지가 있습니다. 

이 상황에서 어떤 클래스가 어떤 클래스에게 의존하고 있나요? 

다른 클래스를 필드영역에 선언한 클래스가 의존하고 있다고 말합니다. 즉 이 예에서는 A클래스가 B클래스에 의존하고 있습니다. B클래스가 필요했기 때문에, B클래스의 인스턴스를 통해서 B클래스의 필드나, 메소드를 사용할 필요가 있었기 때문에 A클래스는 B클래스에 의존하고 있는 것입니다. 

예시)

~~~java
class A{
    private B b;

    public A(B b){
        this.b = b;
    }
}
~~~
~~~java
class A{
    private B b;

    public setB(B b){
        this.b = b;
    }
}
~~~

<br>

![nonspringmvc](/static/assets/img/blog/spring/nonspringmvc.png)

다시 위 그림을 보면 이제 의존관계가 어떻게 이어지는 지 볼 수 있습니다. DispatcherServlet은 비록 웹서버가 실행하기는 하지만 그 과정에서 생성자가 만들어집니다. 웹서버가 Dispatcher에 의존하고 있습니다. 

DispatcherServlet가 HandlerMapping에 의존하고 있고 HandelrMapping이 Controller에 의존하고 있습니다. 

Controller는 DAO에 의존하고 있습니다. 

그리고 Controller에서 ModelAndView를 생성하므로 Controller가 ModelAndView에 의존하고 있습니다. 이렇게 연쇄적으로 클래스끼리 의존하고 있는데 여기서 만약 DAO에 있는 메소드를 대폭 수정하게 된다면 Controller, HandlerMapping, Dispatcher서블릿이 연속적으로 수정작업을 거쳐야합니다.

물론 현실에서는 그런일이 잘 일어나지는 않을 것입니다. 의존관계가 이렇다라는 것을 알려드리기 위해 극단적인 경우를 상정해서 적었습니다. 하지만 분명한 것은 재사용성이 극히 떨어진다는 점입니다. 

위 그림에서 중요한 것은 코딩에서의 dependency흐름이 서비스 요청흐름과는 별개라는 사실입니다. 두개의 flow가 역방향임을 인지하고 있어야 합니다. 

Spring Framework의 DI(Dependency Injection) Framework는 이러한 의존관계를 해소시켜주는 역할을 합니다. 