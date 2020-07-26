---
layout: post
title: "subplot basic"
date: 2020-07-17
desc: "subplot basic"
keywords: python, pandas, matplotlib, pyplot, subplot
categories: [Data_analysis]
tags: [python, pandas,  matplotlib, pyplot, subplot]
---

## subplot

___

subplot은 하나의 figure안에 여러개의 그래프를 그릴 수 있게 만들어주는 메소드입니다. 

~~~python
names=['group_A', 'group_B', 'group_C']
values=[1,10,100]
plt.figure(1, figsize=(9,3))

plt.subplot(131)
plt.bar(names, values)

plt.subplot(132)
plt.scatter(names, values)

plt.subplot(133)
plt.plot(names, values)

plt.show()
~~~

![subplot](/static/assets/img/blog/data_analysis/03Matplotlib/subplot.png){:width="50%" width="50%"}