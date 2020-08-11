---
layout: post
title: "DI Framework"
date: 2020-08-03
desc: "DI Framework"
keywords: Spring, framework, di, dependency injection
categories: [Spring]
tags: [Spring, framework, di, dependency injection]
---

## Dependency Injection(DI)

___

![spring_framework](/static/assets/img/blog/spring/spring_framework.png)

위 그림은 Spring Framework 의 간략한 요약 그림입니다. 

맨 아래에 Core Container라고 적혀진 박스가 있습니다. 이번 글에서는 이 Core Container를 다뤄보려고 합니다.
 
Core Containersms DI(Dependency Injection) Framework라고도 합니다.  

이 Dependency Injection이라는 말의 의미를 알아보기 위해 아주 기초적인 코드부터 쌓아보겠습니다. 

![sts4_dynamic_web_project5](/static/assets/img/blog/spring/sts4_dynamic_web_project5.png)

초기 project의 구조는 위와 같습니다. 

<br>

### Book 클래스 생성

Java Resources > src/main/java > com.spring.object패키지를 만들고 Book클래스를 생성합니다. 

![bookclass](/static/assets/img/blog/spring/bookclass.png)

![bookclasscode](/static/assets/img/blog/spring/bookclasscode.png)

field를 생성한 후 기본생성자, 필드생성자, getter, setter, toString메소드를 만듭니다. 

<br>

### BookTest 클래스 생성

그리고 Java Resources > src/test/java > com.spring.test패키지를 만들고 BookTest클래스를 생성합니다. 

![booktestclass](/static/assets/img/blog/spring/booktestclass.png)

<br>

~~~java
package com.spring.test;

import com.spring.Object.Book;

public class BookTest {
	public static void main(String[] args) {
		Book book = new Book("book1", "Book is Great");
		System.out.println(book);
	}
}
~~~

위 코드는 Book클래스를 이용해 인스턴스를 생성한 후 book의 내용을 출력합니다. 

위 코드는 개발자가 `new`라는 생성자 코드를 직접 만들어줘야 하는 코드 입니다. 

<br>

### BookService Class생성
___

Book에 대한 정보를 출력하는 BookService Class를 만들어보겠습니다. 

![booksvc](/static/assets/img/blog/spring/booksvc.png)

~~~java
package com.spring.service;

import com.spring.Object.Book;

public class BookService {
	
	private Book book;
	
    public BookService(){}

    public BookService(Book book){
        this.book = book;
    }

	public void setBook(Book book) {
		this.book = book;
	}
	
	public void pringBookInfo() {
		System.out.println("Book's title: "+book.getBookName()+" Book's description: "+book.getDescription());
	}
}
~~~

<br>

~~~java
package com.spring.test;

import com.spring.Object.Book;
import com.spring.service.BookService;

public class BookTest {
	public static void main(String[] args) {
		Book book = new Book("book1", "Great");
		BookService bookSvc = new BookService(book);
		bookSvc.pringBookInfo();
	}
}
~~~

<br>

## Interface를 통해 재사용성 높이기.

보통 Java Coding에서는 Interface를 통해 재사용성을 높이고 Coupling을 줄입니다. 그리고 실체클래스의 명이 언급되지 않는 것도 결합도와 재사용성을 줄입니다. 

BookService Interface, BookServiceImpl Class로 나누겠습니다. 

~~~java
package com.spring.service;

public interface BookService {
	public void pringBookInfo();
}
~~~

~~~java
package com.spring.service;

import com.spring.Object.Book;

public class BookServiceImpl implements BookService{
	
	private Book book;
	
	public BookServiceImpl() {
		
	}
	
	public BookServiceImpl(Book book) {
		this.book = book;
	}
	
	public void setBook(Book book) {
		this.book = book;
	}
	
	public void pringBookInfo() {
		System.out.println("Book's title: "+book.getBookName()+" Book's description: "+book.getDescription());
	}
}
~~~

~~~java
package com.spring.test;

import com.spring.Object.Book;
import com.spring.service.BookService;
import com.spring.service.BookServiceImpl;

public class BookTest {
	public static void main(String[] args) {
		Book book = new Book("book1", "Great");
		BookService bookSvc = new BookServiceImpl(book);
		bookSvc.pringBookInfo();
	}
}
~~~

Interface를 선언함으로써 앞으로 bookService를 이용할 때는 실체 클래스를 사용하지 않게 될 것입니다. 인터페이스를 사용하는 것만으로도 재사용성을 높일 수 있습니다. 

<br>

## 객체 생성을 메소드에 위임하기

직접 new를 작성해서 인스턴스를 생성하는 것보다 method를 이용해서 객체를 생성하는 방법도 있습니다. 대표적으로 싱글톤 패턴입니다. 싱글톤패턴으로 생성되는 코드는 인스턴스를 단 하나만 다루기 때문에 Service객체만 싱글톤으로 만들겠습니다. 

lazy initialization Singleton pattern으로 만들겠습니다. 

~~~java
package com.spring.service;

import com.spring.Object.Book;

public class BookServiceImpl implements BookService{
	
	private Book book;
	
	private static BookService instance;
	private BookServiceImpl() {}
	private BookServiceImpl(Book book) {
		this.book = book;
	}
	public static BookService getInstance(Book book) {
		if(instance== null) {
			instance = new BookServiceImpl(book);
		}
		return instance;
	}
	
	public void setBook(Book book) {
		this.book = book;
	}
	
	public void pringBookInfo() {
		System.out.println("Book's title: "+book.getBookName()+" Book's description: "+book.getDescription());
	}
}
~~~

~~~java
package com.spring.test;

import com.spring.Object.Book;
import com.spring.service.BookService;
import com.spring.service.BookServiceImpl;

public class BookTest {
	public static void main(String[] args) {
		Book book = new Book("book1", "Great");
		BookService bookSvc = BookServiceImpl.getInstance(book);
		bookSvc.pringBookInfo();
	}
}
~~~

객체의 생성을 클래스에게 맡겼지만 여전히 new 키워드를 통해 개발자에게 객체 생성의 책임이 있습니다. 

<br>

## Resource파일을 이용해 객체 생성하기

___

이번엔 좀 다른 방법으로 객체를 생성해보겠습니다. properties파일을 이용해 객체를 생성하는 방법입니다. 



![spring_mvc_architecture](/static/assets/img/blog/spring/spring_mvc_architecture.png)



Core Container.... Beans. Core.. Contxt   library    -> di framework. 


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
                    1. 저장


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



di framework가 구축이 된 상태에서 AOP를 끼워 넣을 수 있읍. Aspect Oriented Programming. . . . . . . . . . . 



spring jdbc. . .

mibatis를 쓰자. 


Web > 라이브러리.. . prtlet , struts는 spring mvc를 쓰기전에 쓰던거.. . 지금 안씀.