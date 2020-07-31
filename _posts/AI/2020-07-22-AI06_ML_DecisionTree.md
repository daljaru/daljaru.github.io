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

Decision Tree(결정 트리, 의사결정나무, 의사결정트리)는 특정기준(질문)에 따라서 데이터를 구분하는 모델이고, 분류와 회귀 문제에서 가장 널리 사용되는 모델입니다. 

![decision_tree](/static/assets/img/blog/ai/decision_tree.png){:width="40%", height="40"}

<br>

### Decision Tree 구조

질문이나 네모상자 : 노드

가장 맨 위의 노드 : Root Node 

decision tree에서 오버피팅을 줄이는 방법 중 하나는 가지치기다. .

<br>

### Pruning(가지치기)

가지치기란 최대트리로 형성된 결정트리의 특정 노드 밑의 하부 트리를 제거하여 일반화 성능을 높히는 것을 의미합니다. 

일반화 성능을 높여서 Overfitting을 막는데 기여할 수 있습니다. 여러 방법을 쓸 수 있는데 실제 코드에서 min_sample_split 파라미터를 조정하거나 max_dapth 파라미터를 설정할 수 있습니다. 

min_sample_split는 한 노드가 갖는 데이터의 개수를 제한하며 max_depth는 tree의 깊이를 제한합니다. 



score함수는 원래, 학습이 끝난 모델에 적용, 새로운 Data -> 예측값

예측값, 실제값을 각각 비교, 이때 일치하는 확률을 리턴. 