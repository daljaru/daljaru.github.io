---
layout: post
title: "StringBuffer 생성자"
date: 2020-05-19
desc: "StringBuffer Constructor"
keywords: String, datatype
categories: [Java]
tags: [String, type]
---

## StringBuffer 생성자 사용하기

___

![StringBufferConstructor](/static/assets/img/blog/java/02DataType/StringBufferConstructor.png){:width="100%" height="100%"}
<br>

~~~java
package test;

public class Test {
	public static void main(String[] args) {	
		StringBuffer stBuffer = new StringBuffer();  //빈 String buffer 기본 16개의 문자공간
		stBuffer.append("anything");
		System.out.println(stBuffer);
	}
}
/*결과
anything
*/
~~~
<br>

~~~java
package test;

public class Test {
	public static void main(String[] args) {	
		StringBuffer stBuffer2 = new StringBuffer(100);
		stBuffer2.append("Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.");
		System.out.println(stBuffer2);
		System.out.println(stBuffer2.length());
	}
}
/*결과
Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
128
*/
~~~
<br>

![CharSequence](/static/assets/img/blog/java/02DataType/CharSequence.png){:width="50%" height="50%"}
<br>

CharSequence 인터페이스는 CharBuffer, StringBuffer클래스를 자식으로 가지고 있기 대문에 이를 이용해서 만들어보았다. 

~~~java
package test;

import java.nio.CharBuffer;

public class Test {
	public static void main(String[] args) {	
		
		char[] charArr = {'a', 'b', 'c', 'd'};
		CharSequence charSeq = CharBuffer.wrap(charArr);
		StringBuffer stBuffer3 = new StringBuffer(charSeq);
		System.out.println(stBuffer3);
		
		CharSequence charSeq2 = new StringBuffer();	
		StringBuffer stBuffer4 = new StringBuffer(charSeq2);
		stBuffer4.append("what??");
		
		System.out.println(stBuffer4);
	}
}
/*결과
abcd
what??
*/
~~~
<br>

~~~java
package test;

public class Test {
	public static void main(String[] args) {		
		StringBuffer stBuffer = new StringBuffer("Lorem Ipsum is simply dummy text of the printing and typesetting industry.");
		System.out.println(stBuffer);
	}
}
/*
결과
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
*/
~~~
