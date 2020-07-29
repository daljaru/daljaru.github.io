---
layout: post
title: "Decision Tree"
date: 2020-07-22
desc: "Decision Tree"
keywords: Machine Learning, decision tree
categories: [AI]
tags: [Machine Learning, decision tree]
---

## Decision Tree

___

Decision Tree(결정 트리, 의사결정나무, 의사결정트리)는 특정기준(질문)에 따라서 데이터를 구분하는 모델, 분류와 회귀 문제에서 가장 널리 사용되는 모델입니다. 

![decision_tree](/static/assets/img/blog/ai/decision_tree.png){:width="40%", height="40"}

<br>

### 결정트리 구조

결정 트리에서 질문이나 네모상자를 노드라고 합니다. 

결정 트리에서 가장 맨 위의 노드를 Root Node라고 합니다. 

decision tree에서 오버피팅을 줄이는 방법 중 하나는 가지치기다. .


pruning은 가지치기인데   오버피팅을 막는데 

여러가지 기법을 쓸 수 있음.  

min_sample_split 파라미터 조정. 

속성값을 hyperparameter라고 한다. ... 이걸 예술이라고 한다. . . . . . 

예술 . . . . . . . . . . . . . . . . . . . . . .

가지치기... . . .. . .art.. . . . .. 



머신러닝을 안좋게 시작하는것....-> 


score함수는 원래, 학습이 끝난 모델에 적용, 새로운 Data -> 예측값

예측값, 실제값을 각각 비교, 이때 일치하는 확률을 리턴. 