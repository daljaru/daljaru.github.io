---
layout: post
title: "Decision Tree"
date: 2020-07-22
desc: "Decision Tree"
keywords: Machine Learning, decision tree
categories: [Ai]
tags: [Machine Learning, decision tree]
---

특성중요도 : 0과 1사이의 값. 

정규화 > normalization  모든 특성을 더했을 때 1이 나온다. 



feature의 가중치를 바꾼다................................................


문제 풀어야 하는거. 

random decisin tree를 여러개 만드는 게 ansemble tree.. . . . . ..

----------------------------------

20200724


분류 두가지 

* Binary Classification
* Multi Label Classification

예측을 할때 둘 중에 어떤 것을 사용하는지에 따라 함수가 달라진다. 



Eensemble 알고리즘. . . . . . . . . . . . . .

무작위로 추첨..? data와 decisiontree를 병행해서 생성... estimator를 각각만들고 각각의 estimator의 평균...  Bagging

그 중에 하나가 RandomForest 알고리즘.



Bagging > RandomForest
Boostrap Aggregation

Boosting > GBM  -> learning_rate... . .  0.1, ~ 0.004

에이다. 

normalization. . . . . . . . . . 

feature_importances_

특성 중요도.  .  .  . dicision tree 에서 불순도를 조정할 때 중요. 

원하는 중요한 특징만으로 decision tree를 주거나... (ansenble안주고도. . . . 그럴때도 있다. )

variance,, , , , ,, ,,, , ,, ,,  



=========


linear regression 아주 중요하다. 

회귀와 분류

여기서 회귀는 linear regression. . . . . . . .선형 회귀 

여기서 분류는 classification. . . . .logistic regression



x -> 2, 4, 6, 8, 10
y -> 40, 45, 70, 75, 80

회귀 모델. . . . . . . . . 좌표개념. . . . .  x와 y의 매칭 . 

1차 함수. . . . . . . . . . . . . . . . . . . . . . . . . . .

회귀 모델. . . -> 선상에서 예측 . . . . . . . .                    

---

back propogation -> 최적의 w와 d를 구하는 과정. 

수학 of 수학

weight와 bias를 업데이트 하면서 기울기를 완만하게 . optimization하는 전반적인 방법. 


loss function의 값이 0근처.   . . . . ..->

