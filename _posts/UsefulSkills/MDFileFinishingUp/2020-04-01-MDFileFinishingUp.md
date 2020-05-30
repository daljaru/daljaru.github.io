---
layout: post
title: "How to make MD Files.."
date: 2020-04-01
desc: "How to make MD Files..."
keywords: header, table, bold, italic, code, quotes
categories: [Useful skills]
tags: [mdfile]
---

## 헤더

# 제목1

```
# 제목1
```

## 제목2

```
## 제목2
```

### 제목3

```
### 제목3
```

#### 제목4

```
#### 제목4
```

##### 제목5

```
##### 제목5
```

###### 제목6

```
###### 제목6
```



## 글씨 변형

굵은 글씨는 **굵게**

```
**굵게**
```

기울인 글씨는 *기울이게*

```
*기울이게*
```

기울인 글씨는 _다르게 표현_도 가능

```
_다르게 표현_
```

기울이면서 굵은 글씨는 ***별을 세개 붙인다.***

```
간단하게 ***별을 세개 붙이는 방법***도 있다.
```

취소선은 ~~물결표시~~로 가능.

```
~~물결표시~~
```

밑줄은 <u>u태그로 가능.</u>

```
<u>태그로 가능.</u>
```



## 목록

1. 순서가 있는 목록1 ---> 순서는 앞에 번호를 붙인다.
    1. 순서가 있는 서브 목록1
    1. 순서가 있는 서브 목록2
2. 순서가 있는 목록2
3. 순서가 있는 목록3

```
1. 순서가 있는 목록1 ---> 순서는 앞에 번호를 붙인다.
	1. 순서가 있는 서브 목록1
	1. 순서가 있는 서브 목록2
1. 순서가 있는 목록2
1. 순서가 있는 목록3
```

- 순서가 있는 목록1 ---> 순서는 앞에 번호를 붙인다.
	- 순서가 있는 서브 목록1
	- 순서가 있는 서브 목록2
- 순서가 있는 목록2
- 순서가 있는 목록3

```
- 순서가 있는 목록1 ---> 순서는 앞에 번호를 붙인다.
	- 순서가 있는 서브 목록1
	- 순서가 있는 서브 목록2
- 순서가 있는 목록2
- 순서가 있는 목록3
```

-는 * + 기호로 대체가능하다. 



## 링크

+ 일단 사이트 주소를 그냥 써도 링크는 만들어진다. https://www.google.com

+ 글자에 링크기능을 주소 싶으면 [글자]링크주소를 적는다.
  + [Google](https://www.google.com)

  >```
  >[Google](https://www.google.com)
  >```

+ 링크설명을 쓸 수도 있다. 링크에 커서를 갖다대면 뜨는 문구다. 
  + [Google](https://www.google.com " 이 링크는 구글링크입니다.")

  > ```
  > [Google](https://www.google.com " 이 링크는 구글링크입니다.")
  > ```

  예시)![testlink](/static/assets/img/blog/usefulSkills/MDFileFinishingImages/testlink.png)
  
  

- 자신의 디렉토리 안의 사이트를 상대적 참조할 수도 있습니다. 

  - [myFile](./Python3/)

    > [myFile](./Python3/)



## 이미지

```
![텍스트](이미지 링크 "링크 설명")
```

위의 형식으로 쓸 수 있습니다. !가 붙는다는 점이 일반 링크와의 차이입니다. 

![창문](/static/assets/img/blog/usefulSkills/MDFileFinishingImages/window.png "창문")

```
![창문](/static/assets/img/blog/usefulSkills/MDFileFinishingImages/window.png "창문")
```



```
![텍스트][간단한 변수]
[간단한 변수] : 링크 "링크 설명"
```

위의 형식으로도 쓸 수 있습니다. 

![창문][window]

[window]: /static/assets/img/blog/usefulSkills/MDFileFinishingImages/window.png "창문"

```
![창문][window]
[window]: /static/assets/img/blog/usefulSkills/MDFileFinishingImages/window.png 창문
```



## 이미지 + 링크

이미지를 눌러서 링크를 타고 다른 사이트로 가고 싶을 때도 있습니다. 원래의 기본링크가

```
[링크](https://google.com "구글링크입니다.")
```

이였으니까 [텍스트]부분에 이미지를 넣어주면 완성이 됩니다. 

```
[![텍스트](이미지 링크 "링크 설명")](사이트 주소)
```

[![GoogleImageLink](/static/assets/img/blog/usefulSkills/MDFileFinishingImages/window.png "windowGoogle")](https://www.google.com)

```
[![GoogleImageLink](/static/assets/img/blog/usefulSkills/MDFileFinishingImages/window.png "windowGoogle")](https://www.google.com)
```



## 네임드 앵커

문서 내에서 A라는 영역에서 B라는 영역으로 이동할 수 있게 만드는 방법이 있습니다. 

```
[텍스트](#이동할 변수)
```

```
<a id="이동할 변수"></a>
```

위와 같은 형태로 쓰시면 됩니다. 

예시)

* [A](#A place)
* [B](#B place)
* [C](#C place)

```
* [A](#A_place)
* [B](#B_place)
* [C](#C_place)
```

A 내용<a id = "A_place"></a>

B 내용<a id = "B_place"></a>

C 내용<a id = "C_place"></a>

```
A 내용<a id = "A_place"></a>

B 내용<a id = "B_place"></a>

C 내용<a id = "C_place"></a>
```

A를 클릭하면 A내용으로 페이지 위치가 옮겨집니다. 



## 코드

이제까지 제가

```
여기에 코드를 적은 것을 보셨을텐데요. 여기는 코드를 적는 란입니다. 
```

```
​```언어이름
코드내용
​```
```

위의 형식으로 씁니다. 코드의 내용이 언어에 알맞게 타이핑되시는 걸 확인할 수 있습니다. 

* 예시1. 코드선택

![code](/static/assets/img/blog/usefulSkills/MDFileFinishingImages/code.png)



* 예시2 코드 작성

  ```java
  int num = 0;
  int plusNum(int num){
      return ++num;
  }
  ```

  ```
  ​```java
  int num = 0;
  int plusNum(int num){
  	return ++num;
  }
  ```



## 표

표에서 제일 상단에 위치한 row를 헤더라고 합니다. 헤더와 row를 구분하는 선을 긋는 것이 가장 중요합니다.  

```
|헤더1|헤더2|헤더3|
```

를 기본으로 아래와 같이 만듭니다. 

| 헤더1   | 헤더2   | 헤더3   |
| ------- | ------- | ------- |
| 내용1   | 내용2   | 내용3   |
| 내용1-2 | 내용2-2 | 내용3-2 |
| 내용1-3 | 내용2-3 | 내용3-3 |

```
| 헤더1   | 헤더2   | 헤더3   |
| ------- | ------- | ------- |
| 내용1   | 내용2   | 내용3   |
| 내용1-2 | 내용2-2 | 내용3-2 |
| 내용1-3 | 내용2-3 | 내용3-3 |
```



![header](/static/assets/img/blog/usefulSkills/MDFileFinishingImages/header.png)

Typora에서는 상단의 헤더만 만들면 자동으로 표가 만들어지며 그 이후 크기 조정, 글자정렬 등은 마우스로 조절할 수 있는 기능을 제공합니다. 

Typora에서는 크기 조절, 정렬등을 자유로히 쓰시면 됩니다. 



## 인용문

인용문은 출처가 있는 텍스트를 적을 때 씁니다. '>'기호를 이용해 적을 수 있습니다. 

> 인용문을 적습니다. 
>
> > 중첩된 인용문입니다. 

```
> 인용문을 적습니다. 
>> 중첩된 인용문입니다. 
```



## Raw HTMl

마크다운 문서에는 html코드를 넣어도 괜찮습니다. 



## 수평선

---

```
---
```

___

```
___
```



## 줄바꿈

해당 라인 끝에<br>태그를 붙이시면 됩니다. 

```
해당 라인 끝에<br>태그를 붙이시면 됩니다. 
```