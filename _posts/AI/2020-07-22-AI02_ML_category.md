---
layout: post
title: "ML Category"
date: 2020-07-22
desc: "ML Category"
keywords: Machine Learning, Supervised, Unsupervised, Reinforcement
categories: [AI]
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

## Error

___

1. Training error(학습 오차)

    라벨이 붙어있지만 모든 데이터를 다 perfect하게 맞추는 모델은 아닙니다.

2. Test error(예측 오차)

    신규 데이터를 넣어서 결과를 예측했을 때의 오차입니다. 
    예측 오차는 작을수록 좋은 모델이 완성된 것입니다.

<br>

## Overfitting, Underfitting

___

Training Error가 높으면 높을 수록 좋지 않습니다. 이 경우는 Underfitting되었다고 표현합니다. 

반대로 Training Error가 작으면 작을 수록 좋습니다. 하지만 예외적으로 만약 training error가 극단적으로 작다면 모델의 성능을 의심해봐야 합니다. training data에만 정확한 모델이 만들어졌을 가능성이 높기 때문입니다. 

만약에 training Error가 극단적으로 낮은데 신규 데이터의 에러(test Error)가 높게 나온다면 과도하게 train data에 의존한 모델이 만들어진 것입니다. 이 경우를 Overfitting 되었다고 표현합니다. 

<br>

Underfitting의 경우에는 해결책으로 학습데이터의 양을 늘리거나 학습의 기간을 늘립니다. 

Overfitting의 경우에는 해결책으로 학습데이터가 너무 천편일률적이지는 않은지 확인하는 것이 좋습니다. 학습데이터의 다양성을 늘리는 것이 중요하고 또는 데이터의 학습 깊이를 낮추는 것이 좋습니다. 굉장히 
세밀하게, 오차를 허용하지 않게 학습이 되었을 가능성이 높기 때문입니다. 

<br>

## 라벨의 개수

___

라벨(데이터셋의 정답에 해당하는 데이터 클래스)은 최대 50개가 마지노선입니다. 만약 50개가 넘는다면 굉장한 수준의 컴퓨팅 파워가 필요하기 때문에 데이터 셋을 변형하는 과정에서 조절해야 합니다.  

--------------

용어 

지도학습에서 Machine Learning이 Propagation :  

forward propagation하는 방법. flow

feature,속성,특징   | label, target            test Dataset -> predict 

accuracy 정확도를 측정. 



회귀는 scope안에 있는지 파악하는 것. 

decision tree에서 오버피팅을 줄이는 방법 중 하나는 가지치기다. .


pruning은 가지치기인데   오버피팅을 막는데 

여러가지 기법을 쓸 수 있음.  

min_sample_split 파라미터 조정. 

속성값을 hyperparameter라고 한다. ... 이걸 예술이라고 한다. . . . . . 

예술 . . . . . . . . . . . . . . . . . . . . . .

가지치기... . . .. . .art.. . . . .. 



머신러닝을 안좋게 시작하는것....-> 


score함수는 원래, 학습이 끝난 모델에 적용, 새로운 Data -> 예측값

예츠값, 실제값을 각각 비교, 이때 일치하는 확률을 리턴. 

