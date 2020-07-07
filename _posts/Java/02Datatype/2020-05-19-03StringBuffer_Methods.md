---
layout: post
title: "StringBuffer 주요 메소드"
date: 2020-05-19
desc: "StringBuffer useful methods"
keywords: StringBuffer
categories: [Java]
tags: [StringBuffer, type]
---

## StringBuffer 주요 메소드

___

### append

append 메소드는 buffer에 있는 String sequence뒤에 주어진 인자를 문자열로 변환하여 붙여넣는 기능을 한다. 

![StringBufferAppend](/static/assets/img/blog/java/02DataType/StringBufferAppend.png){:width="100%" height="100%"}
<br>

위 사진처럼 매우 매우 다양한 데이터타입이 인자로 들어갈 수 있다.

~~~java
package test;

public class Test {
	public static void main(String[] args) {
		StringBuffer strBuffer = new StringBuffer();
		strBuffer.append("String");
		System.out.println(strBuffer);
		strBuffer.append(" can append");
		System.out.println(strBuffer);
		strBuffer.append(" after buffer");
		System.out.println(strBuffer);
	}
}
/*결과
String
String can append
String can append after buffer
*/
~~~
<br>

### insert

insert 메소드는 String sequence의 임의의 위치에 String sequence를 삽입할 수 있다. 

![StringBufferInsert](/static/assets/img/blog/java/02DataType/StringBufferInsert.png){:width="100%" height="100%"}
<br>

이것도 무지 많은 메소드들이 오버로딩돼있는 걸 볼 수 있다. 

~~~java
package test;

public class Test {
	public static void main(String[] args) {
		StringBuffer strBuffer = new StringBuffer("abcdefghijklmnop");
		strBuffer.insert(5, " insert!!! ");
		System.out.println(strBuffer);
	}
}
/*결과
abcde insert!!! fghijklmnop
*/
~~~
<br>

5번째 인덱스 자리에 지정한 문자열이 삽입된다. 

이외에도 문자열을 다루는 다양한 메소드들이 있다. 

~~~java
package test;

public class Test {
	public static void main(String[] args) {
		StringBuffer strBuffer = new StringBuffer("abcdefghijklmnop");
		System.out.println(strBuffer.charAt(0));    //a
		System.out.println(strBuffer.length());     //16
		System.out.println(strBuffer.capacity());   //32
		System.out.println(strBuffer.delete(4, 9)); //abcdjklmnop
		System.out.println(strBuffer.replace(0, 4, "zyxwv"));//zyxwvjklmnop
		System.out.println(strBuffer.reverse());//pomlkjvwxyz
	}
}
~~~

capacity()는 default capacity인 16에서 새 문자열의 길이만큼 늘어난다.