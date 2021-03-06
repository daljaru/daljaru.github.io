---
layout: post
title: "ML Category"
date: 2020-07-22
desc: "ML Category"
keywords: Machine Learning, Supervised, Unsupervised, Reinforcement
categories: [Ai]
tags: [Machine Learning, Supervised, Unsupervised, Reinforcement]
---

## 머신러닝 학습 분류

___

1. **지도학습(Supervised Learning)**

    데이터를 학습시킬 때 미리 정해진 답도 같이 학습합니다. 정해진 답이 있기 때문에 분류와 회귀에 적합합니다. 답이 있는 데이터이기 때문에 정량화가 가능합니다. 

2. **비지도학습(Unsupervised Learning)**

    데이터를 학습시킬 때 답을 알려주지 않고, 모델이 스스로 데이터의 특성에 따라 유의미한 결과를 뽑아내도록 하는 것. 단순히 데이터만 주어지기 때문에 특정한 값을 유도해 낼수는 없습니다. 다만 데이터자체가 어떤 의미를 내포하고 있는지는 알 수 있습니다. 예를 들어 군집(Clustering)의 정도를 알 수 있습니다. 

    비지도 학습의 경우 지도학습에 비해 데이터셋이 크지 않아도 크게 문제가 되지 않기 때문에 만약 데이터셋이 대량으로 준비되어 있지 않은 그룹에 상대적으로 적당하다. 

    라벨이 없는 데이터를 학습하기 때문에 정량화가 불가능합니다. 

3. **강화학습(Reinforcement Learning)**

    Agent가 현재 상태에서 선택 가능한 행동들 중 보상을 최대화하는 방식으로 학습합니다. 모델이 여러 번 시행착오를 겪으며 보상이 최대화되는 행동을 합니다. 

<br>

## Model

___

모델은 머신의 블랙박스입니다. 세부적인 코드가 어떻게 돌아가는지는 알 수 없겠지만 데이터를 학습하고 데이터의 질과 양에 따라 모델의 성능이 변화합니다. 

모델은 머신이 학습하는 방법 자체를 말하는데 크게 2가지로 나뉩니다. 
 ㅍ
1. Training(학습)

    라벨이 붙어있는 데이터를 이용해서 모델을 학습시킵니다. 

2. Inference(추론, 예측)

    신규데이터를 넣고 학습시킨 모델을 이용해 결과값을 예측합니다. 예측의 정확도에 따라 모델의 성능을 평가할 수 있습니다. 

<br>

## 간단한 머신러닝 학습분류

___

### Unsupervised

* Clustering & Dimensionality Reduction

    * SVD, PCA, K-means
  
* Association Analysis

    * Apriori, FP-Growth

* Hidden Markov Model

### Supervised

* Regression

    * Linear, Polynomial

* Decision Tree

* Random Forests

* Classification

    * KNN, Trees, Logistic Regression, Naive-Bayes, SVM