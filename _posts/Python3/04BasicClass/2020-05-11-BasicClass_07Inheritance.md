---
layout: post
title: "Inheritance"
date: 2020-05-11
desc: "Inheritance is oop's charateristic"
keywords: oop, inheritance, parent, child
categories: [Python3]
tags: [python3,oop, inheritance, parent, child]
---

## Inheritance(상속)

상속은 객체를 부모와 자식클래스로 나누는 것을 말합니다. 

예를 들어 우리가 '모여봐요 동물의 숲' 게임을 만든다고 해봅시다. 

모여봐요 동물의 숲 게임에는 다양한 동물 캐릭터들이 나오기 때문에 우리는 '동물'이라는 객체를 만들었습니다. 

그런데 동물에도 종류가 엄청 많습니다. 
포유류도 있고 양서류도 있고, 어류도 있습니다. 생각해보니 동물이라는 객체가 모두의 특징을 표현할 수는 없을 것 같습니다.

그래서 우리는 포유류, 양서류, 어류라는 객체를 따로 만들어서 동물의 특징을 모두 가져오는 한편 이 3개의 객체만의 특징은 각 객체마다 구현하기로 했습니다.

이 '동물' 객체가 부모 클래스가 되고
'포유류', '양서류', '어류'가 자식 클래스가 됩니다.










## Method Overriding