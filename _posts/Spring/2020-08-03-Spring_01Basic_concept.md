---
layout: post
title: "Spring Basic Conception"
date: 2020-08-03
desc: "Spring Basic Conception"
keywords: Spring, framework
categories: [Spring]
tags: [spring, framework]
---

해당 게시물은 Spring Framework를 공부하기 위해 개인적으로 공부했던 자료입니다. 현업에서 쓰이는 코드와는 무관합니다. 기본적인 베이스를 탄탄히 다지는 코드들로 점근적으로 빌드업하는 방향으로 쓰여졌습니다. 

<br>

## Spring framework

___

![spring_logo](/static/assets/img/blog/spring/spring_logo.png)

<br> 

## Framework?? 프레임워크가 뭐지... 

___

Spring Framework를 공부할 때 Framework의 의미를 어느정도 알고 있다면 Spring을 공부할 때 많은 도움이 됩니다. 앞으로 공부할 수록 점점 알게 되겠지만 **Framework**는 다른 것에 비유하자면 '일정한 공정 프로세스를 가진 공장'이라고 볼 수 있습니다. 

![myway](/static/assets/img/blog/spring/myway.png)

Java Programming을 생각해봅시다. 우리는 패키지를 만들고 싶은대로 구조화하고 각 패키지마다 자바클래스파일을 만들어서 빌드 후 배포를 합니다. 비유하자면 '자유로운 작업방식이 허용된 공장' 이라고 볼 수 있겠네요. 

<br>

![rule](/static/assets/img/blog/spring/rule.png)

이와 다르게 Framework는 조금 다릅니다. 반드시 작성해야하는 일종의 '규칙'이 굉장히 많이 있습니다. 어떤 클래스를 쓰기위해 반드시 지정된 라이브러리를 import해야하고, 태그기반의 xml파일 경우 반드시 써야하는 태그들이 정해져 있습니다. 심지어 파라미터명까지 작성하는 규칙이 정해져 있을 정도입니다. 

<br>

## For what??

___

이렇게 규칙이 정해진 데는 이유가 있습니다. Spring이 제공하는 규칙을 따라서 자바프로그래밍을 한다면 굉장히 재사용성이 높은 프로젝트를 완성할 수 있습니다. 

![pre](/static/assets/img/blog/spring/pre.png)

Java Programming에서는 모든 것은 클래스로 이루어져 있고 클래스간의 연관관계를 통해서 전체 프로젝트를 완성할 수 있습니다. Java Programming에서 가장 중요한 부분은 바로 이 연관관계의 정도를 낮추는 것입니다. 흔히 연관도를 낮춘다, 결합도를 낮춘다, 재사용성을 높인다 라고 표현합니다.  

클래스간의 연관도를 줄여야 유지보수를 잘 할 수 있기 때문에 이와 관련된 기법도 아주 다양하게 존재합니다. 

<br>

![rule2](/static/assets/img/blog/spring/rule2.png)

Spring Framework는 이 연관도를 아주아주 느슨하게(거의 없다시피 느껴지게)만들어 개발자입장에서 유지보수가 정말 편리해지고 프로젝트의 확장성을 획기적으로 높여줍니다. 

<br>

## Spring....

___

Spring은 java에서 가장 핵심적인 프레임워크로 서버사이드 영역에서 현업에서 많이 쓰입니다. 

흔히 Spring Framework라고 하면 Spring MVC Framework를 떠올리는데 Spring에는 다양한 Framework들이 존재합니다. 예를 들어 Spring di, Spring jdbc, Spring aop, Spring security 프레임워크가 있습니다. 위 말을 하나로 그룹화해서 나온 단어가 spring framework입니다.

Spring jdbc framework는 한국에서는 잘 쓰지 않고 있습니다. 일본에서 많이 쓰는 걸로 알고 있습니다. 대신에 jpa나 mybatis프레임워크를 한국에서 가장 많이 쓰고 있습니다. 

Mybatis 프레임워크는 한국어로 된 튜토리얼도 있습니다. Mybatis를 소개하는 책도 있지만 내용은 튜토리얼과 매우 비슷하기 때문에 책을 사기보단 Tutotial을 보면서 공부하는 게 좋습니다. 

<br>

## Spring basic structure

___

![spring_framework](/static/assets/img/blog/spring/spring_framework.png)

Spring framework의 간단한 구조를 예시르 그렸습니다.

Spring framework는 여러개의 모듈들이 합쳐진 거대한 묶음입니다. 예를 들어 위 그림에서 Core Container는 beans, Core, Context, Expression Language라는 라이브러리들이 묶여진 모듈이고 이와 비슷한 모듈이 묶여 framework가 이루어집니다. 

여러개의 모듈들을 모두 spring것으로 굳이 쓰지 않아도 됩니다. 하나하나가 완벽한 컴포넌트이기 때문에   spring jdbc자리에 mybatis로 대체해도 되고, jpa로 대체해도 됩니다.