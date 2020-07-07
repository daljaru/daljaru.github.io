---
layout: post
title: "StringBuffer Class의 특징"
date: 2020-05-19
desc: "String class"
keywords: String, datatype
categories: [Java]
tags: [String, type]
---

## StringBuffer Class

___

![StringBuffer](/static/assets/img/blog/java/02DataType/StringBuffer.png)
<br>

### 특징

*  String과 비슷한 역할을 하지만 가변적이라는 점에다 다릅니다. String과 비슷하게 문자들의 나열로 이루어진 인스턴스를 가질 수 있지만 언제든지 길이나 내용이 바뀔 수 있습니다. 

* 멀티스레드 환경에서 매우 안정적으로 작동합니다. 

* append와 insert method가 핵심적인 기능입니다. 다양한 타입의 데이터를 받아서 String으로 변환 후에 String Buffer에 append하거나 insert하게 됩니다. 

* testBuffer가 StringBuffer의 인스턴스라면 testBuffer.append(str1)은 testBuffer.insert(testBuffer.length(), str1)과 의미가 같습니다. 

* String buffer는 일정한 크기가 있지만 만약 내부 버퍼가 오버플로우가 된다면 자동으로 버퍼의 크기를 늘립니다. 

* 단일스레드 환경에 특화된 클래스는 StringBuilder클래스입니다. StringBuffer클래스보다 단일스레드환경에서 속도가 빠릅니다. 그리도 동기화를 제공하지 않습니다.