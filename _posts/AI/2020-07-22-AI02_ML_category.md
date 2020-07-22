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

    데이터를 학습시킬 때 미리 정해진 답도 같이 학습합니다. 정해진 답이 있기 때문에 분류와 회귀에 적합합니다. 

2. **비지도학습(Unsupervised Learning)**

    데이터를 학습시킬 때 답을 알려주지 않고, 모델이 스스로 데이터의 특성에 따라 유의미한 결과를 뽑아내도록 하는 것. 단순히 데이터만 주어지기 때문에 특정한 값을 유도해 낼수는 없습니다. 다만 데이터자체가 어떤 의미를 내포하고 있는지는 알 수 있습니다. 예를 들어 군집(Clustering)의 정도를 알 수 있습니다. 

3. **강화학습(Reinforcement Learning)**

    Agent가 현재 상태에서 선택 가능한 행동들 중 보상을 최대화하는 방식으로 학습합니다. 모델이 여러 번 시행착오를 겪으며 보상이 최대화되는 행동을 합니다. 

<br>

## Machine Learning Devleopment Life Cycle

___





데이터가 뭔지에 대한 라벨링이 있어야 한다.

머신러닝정도를 쓰려면 학습데이터가 굉장히 많아야 한다. training data set, test data set.

지금에야 각광받는 이유는 데이터가 그동안 부족했기 때문. . . .. 지금은 데이터가 많음.

performance 조정.   t에 새로 접근. 


training data를 맞추는 건 굉장히 잘함. 

test data 를 맞추는 것 못 할 때가 있음.


trainig 데이터를 넣고  > 데이터를 학습하고 > test data를 넣고(new) >근데 오차가 발생하면 > 뭘 바꿔야 할까? > 오차 줄이기 >( 예측하고 다시 돌아갈때 학습이 이뤄진다고 한다. )

관심있는 것끼리 뭉쳐지는 거.. 비지도학습... 하는 거. . . . . . . . . . . . 

유사도. . . . ..  . .. . . .  . . . . . . .  .비지도학습은 클러스터링이다. 

머신러닝을 환경적인 입장에서 본다면 ..스타트업이라면 비지도가 좋다. . . . . . . . . . . . ... . . .데이터셋이 많지 않아도 가능하다. 



지도학습,,분류....

비지도 학습.. 그냥 데이터만 있다. > 평가를 못함. 퍼포먼스의 수치화를 못한다. 정량화를 못한다. 


정량화........... 맞추고 안맞추고를 알수 있으니까 정량화를 할 수 있다. 


비지도학습은 맞추고 안맞추고가 아니므로 정량화를 하지 못한다. 

모델은 머신이 학습하는 블랙박스.....어떤 방법론으로 학습할 지는 정해줄 수 있다. 


모델은 머신이 학습하는 방법 자체를 말하는데 크게 2가지로 나뉘다. 

training model이냐 inference model이냐로 나뉩니다. 

inference model의 성능을 좋게 하는 것이 우리의 목적이다.



70퍼면 데이터를 늘리거나 학습의 기간을 늘린다. 


inference는 무조건 높게...  . . . . . .



오버피팅은 training할때는 잘 맞췄는데 test할 때 완전 망하는 것. -> 데이터를 추상적으로. . . . 학습 데이터를 너무 정량화하지 않는 것. 학습데이터의 다양성을 늘려야함.  

라벨 50개가 마지노선.. 

정확도 93%까지는 석사수준에서 낼 수 있다. 비용: 500만원

성능 80-90프로  하루 일주일 3일. 

500만원 93%

95 97% - 5000만



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

