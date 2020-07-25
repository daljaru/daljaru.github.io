---
layout: post
title: "Matplot Library 기본 개념"
date: 2020-07-17
desc: "Matplot Library Basic Concept"
keywords: python, pandas, matplotlib, pyplot
categories: [Data_analysis]
tags: [python, pandas,  matplotlib, pyplot]
---

## matplotlib

___

![matplotIndex](/static/assets/img/blog/data_analysis/03Matplotlib/matplotIndex.png){:width="80%" height="80%"}

<br>

파이썬으로 분석한 데이터를 시각화 하는데는 [matplotlib](https://matplotlib.org/)이라는 라이브러리를 가장 많이 사용합니다. matplotlib은 파이썬에서 2D 형태의 그래프, 이미지등을 그릴 때와 실제 과학 컴퓨팅 분야나 인공지능 연구분석결과 도출에 가장 많이 사용됩니다. matplotlib 모듈 중에는 다양한 서브 모듈이 있는데 그 중에서 가장 많이 사용하는 서브 모듈을 pyplot입니다. 

기존에 설치된 파이썬에 추가로 설치하려면

~~~
python -m pip install -U pip
python -m pip install -U matplotlib
~~~

아래의 python command를 통해 설치 할 수 있습니다. 아나콘다환경에서 사용한다면 아마 이미 다 설치되어 있을 것이므로 별다른 설치 프로세스가 필요하지 않습니다.

<br>

## plot() (간단한 예시)

___

> plt.plot(*args, scalex=True, scaley=True, data=None, **kwargs)

plot함수는 x,y 좌표에 해당하는 점을 라인이나 마커로 그릴 수 있습니다. plot이라는 말은 그래프의 도면을 짜놓는다..라고 생각하시면 편합니다. 

~~~python
import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,4,9,16]) 
plt.show()
~~~

첫번째 리스트가 x좌표들의 모임이 되고 두번째 리스트로 y좌표들의 모임이됩니다. (1,1), (2,4), (3,9), (4,16)점을 포인트로 라인이 그려집니다. 

![plot](/static/assets/img/blog/data_analysis/03Matplotlib/plot.png){:width="40%" height="40%"}

<br>

~~~python
import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,4,9,16], 'bo') 
plt.show()
~~~

파란색 동그라미 모양으로 그래프를 그립니다. 

![bluedot](/static/assets/img/blog/data_analysis/03Matplotlib/bluedot.png){:width="40%" height="40%"}

<br>

모양을 지정할 수 있는 표시에는 다양한 것들이 있습니다. Line2D 속성값을 사용해서 지정해줄 수 도 있습니다. 

~~~python
plt.plot([1,2,3,4], [1,4,9,16], color='green', marker='o', linestyle='dashed',linewidth=2, markersize=12)
plt.show()
~~~

![line2d](/static/assets/img/blog/data_analysis/03Matplotlib/line2d.png){:width="40%" height="40%"}

<br>

### line

* '-' -> 실선
* '--' -> 끊어진 실선
* '-.' -> 점선과 점
* ':' -> 점선

<br>

#### dot

* '.' -> 점
* ',' -> 픽셀
* 'o' -> 동그라미
* '*' -> 별표
* '^' -> 삼각형
* 'v' -> 역삼각형
* '<' -> 왼쪽 방향 삼각형
* '>' -> 오른쪽 방향 삼각형
* '1' -> tri_down marker
* '2' -> tri_up marker
* '3' -> tri_left marker
* '4' -> tri_right marker
* 'd' or 'D'-> 다이아몬드
* 'p' -> 오각형
* 's' -> 사각형
* 'h' or 'H' -> 육각형
* 'x' -> x표시
* '+' -> +표시
* '|' -> 수직막대기
* '_' -> 수평막대기

<br>

#### color

색깔도 다양하게 지정할 수 있습니다. 

* 'b' -> blue
* 'g' -> green
* 'r' -> red
* 'c' -> cyan
* 'm' -> magenta
* 'y' -> yellow
* 'k' -> black
* 'w' -> white