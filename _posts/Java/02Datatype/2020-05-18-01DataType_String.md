---
layout: post
title: "String class의 특징"
date: 2020-05-18
desc: "String class"
keywords: String, datatype
categories: [Java]
tags: [String, type]
---

## String 클래스

___

Java에서 문자열을 다룰 때 String Class를 사용합니다. 
<br>

![StringClass](/static/assets/img/blog/java/02DataType/StringClass.png)

<br>
java.base모듈, java.lang 패키지, java.lang.Object클래스를 SuperClass로 하고 있습니다. 그리고 인터페이스가 5개나 연결되어 있습니다.

문자열은 연결된 문자들을 나타냅니다.
 > ex) "abc"는 'a', 'b', 'c'의 연결된 상태.

그리고 모든 스트링 리터럴들이 이 클래스의 인스턴스입니다. 
 > ex) String abc = "abc"   "abc"그 자체로 인스턴스가 된다. 

> 리터럴(literal)이란 소스코드의 고정된 값을 대표하는 용어입니다. 주로 초기화에 많이 쓰입니다. ex) int number = 1; String str = "Hello"; 가 있다면 1과 "Hello"가 literal입니다.
<br>

## 특징

___

* [Strings are constant](https://stackoverflow.com/questions/8798403/string-is-immutable-what-exactly-is-the-meaning) = 값이 생성되면 변경할 수 없습니다. 

이 말은 문자열 리터럴 하나가 생성될 때마다 이걸 참조하는 String 객체가 생성된다는 뜻입니다. 예를 들어 아래와 같은 코드가 있다고 봅시다.
<br>

~~~java
package test;

public class Test {
	public static void main(String[] args) {
		String test ="Hello";
		System.out.println(System.identityHashCode(test));
		
		test = test+"World";
		System.out.println(System.identityHashCode(test));
	}
}

/*
결과:
2018699554
1311053135
*/
~~~
<br>

System.identityHashCode()을 이용하면 인스턴스의 주소값을 출력할 수 있습니다. 

얼핏 보면 test변수만 있으므로 주소가 하나만 나와야 할 것처럼 보이지만 서로 다른 주소값이 보입니다. 

처음에 "Hello"라는 String 클래스의 인스턴스를 생성하고 test와 바인딩을 했습니다. 그리고 test+"World"를 통해 새로운 String 클래스의 인스턴스를 생성하고 다시 test와 바인딩(다른 메모리 주소)를 합니다. 

* StringBuffer는 mutable string을 지원합니다. 이와 다르게 String buffer는 mutable한 String을 지원합니다. 새로 인스턴스를 생성하는 과정이 없기 때문에 StringBuffer가 String보다 문자열을 이어주는데 더 빠릅니다.

* String 클래스는 시퀀스의 각 문자(Unicode code)들을 다룰 수 있는 메소드를 제공합니다. 
  
* String 객체에 null값을 패싱하면 NullPointerException 에러가 일어납니다. 

* String 은 UTF-16포맷을 사용하며 supplementary characters의 경우)UTF-16 포맷 크기보다 큰 경우)에는 surrogate pairs로 표현이 됩니다.

* String concatenation 연산자의 경우 자바 컴파일러의 재량에 따라 작동하는 방식이 달라질 수 있습니다. StringBuffer, StringBuilder로 할 수도 있고 java.lang.invoke.StringConcatFactory로 할 수도 있습니다. 
