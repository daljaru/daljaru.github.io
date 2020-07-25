---
layout: post
title: "겹쳐진 그래프 그리기"
date: 2020-07-17
desc: "duplicated_graph"
keywords: python, pandas, matplotlib, pyplot
categories: [Data_analysis]
tags: [python, pandas,  matplotlib, pyplot]
---

## plot()

___

plot()메소드를 통해 여러개의 그래프를 미리 만들어두고 plt.show()메소드를 사용하면 여러개의 그래프가 한 도면에 그려지는 것을 확인 할 수 있습니다. 또는 plot()메소드 안에 여러개의 그래프 형식을 넣을 수 있습니다. 

<br>

## plot()을 여러번 쓰기

___

~~~python
import numpy as np
t = np.arange(0,5,0.2)
plt.plot(t,t,'r--',t,t**2,'gs', t,t**3,'*')
plt.show()
~~~

![dupli_plot](/static/assets/img/blog/data_analysis/03Matplotlib/dupli_plot.png)

<br>

## plot()메소드 안에 여러 그래프를 설정하기

___

~~~python
import numpy as np
t = np.arange(0,5,0.2)
plt.plot(t,t,'r--',label='Tips')
plt.plot(t,t**2,'gs',label='Population')
plt.plot(t,t**3,'b^', label='Product Layer')

plt.legend()
plt.xlabel('Contents')
plt.ylabel('Count', rotation=0)
plt.show()
~~~

![dup](../../../static/assets/img/blog/data_analysis/03Matplotlib/dup.png)

<br>

## 인자값 실험

___

리스트 뿐만 아니라 numpy Array, Series도 들어갈 수 있습니다. 

~~~python
plt.plot(np.random.randint(0,10,10), np.random.randint(0,10,10), 'ro')
plt.plot(np.random.randint(0,50,20), np.random.randint(0,50,20), 'g*')
plt.plot(Series(np.random.randint(20,60,20)), Series(np.random.randint(20,60,20)), 'm^')
plt.show()
~~~

![argtype](../../../static/assets/img/blog/data_analysis/03Matplotlib/argtype.png)

<br>

## sin, cos그리기

___

여러 타입이 x, y인자값으로 들어갈 수 있기 때문에 아래와 같이 만들 수도 있습니다. 

~~~python
t = np.arange(0,12,0.01)
plt.plot(t, np.cos(t), 'r')
plt.plot(t, np.sin(t), 'c')
plt.plot(t, np.cos(t)*np.sin(t), 'g')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('SinCos graph')
plt.show()
~~~

~[consin](../../../static/assets/img/blog/data_analysis/03Matplotlib/consin.png)

<br>

## figure