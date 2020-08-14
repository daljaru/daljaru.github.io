---
layout: post
title: "AI Introduction"
date: 2020-07-22
desc: "AI Introduction"
keywords: Machine Learning, Deep Learning, Neural Network, Decision Tree, Random Fores, Classification, Linear Regression, Rogistic
categories: [Ai]
tags: [Machine Learning, Deep Learning, Neural Network, Decision Tree, Random Fores, Classification, Linear Regression, Rogistic]
---

## Machine Learning intro..

___

> Machine Learning : Field of study that gives computers the ability to learn without being explicitly programmed. - Arthur Samuel (1959)
>
> 명시적으로 프로그램을 작성하지 않고 컴퓨터에 학습할 수 있는 능력을 부여하기 위한 연구 분야.

컴퓨터 게임 및 인공 지능 분야의 미국 개척자인 Arthur Samuel이 한 말입니다. 그는 1959년에 '머신러닝'이라는 용어를 대중화한 사람입니다. 머신러닝의 필요성을 느끼게 된 건 연산이 너무 많아서 혹은 경우의 수가 너무 많아서 명시적으로 프로그램을 만들 수 없는 경우였습니다. 

예를 들어 바둑 같은 경우 내가 둬야할 수 와 상대방이 둬야할 수 하나 사이에 수 많은 가능성이 있고 돌 하나를 둘 때마다 그 가능성이 그때 그대 바뀌기 때문에 바둑을 최적으로 두는 프로그램을 명시적으로 만들기는 어렵습니다. 

<br>

> Well-posed Learning Problem: A computer program is said to learn from experience E with respect to some task T and some performance measure by P, improves with experience E - Tom Mitchell (1998)
> 
> 어떤 프로그램이 T(Task)라고 하는 작업을 수행하고 P(Performance Measure)라고 하는 성능 측정 결과를 통해 E(Training Experience)라고 하는 경험을 축적, 성능 개선을 한다면 프로그램은 E라는 경험에서 학습한다고 할 수 있다. 

위 글에서 볼 수 있듯이 머신러닝을 위한 핵심적인 세가지 요소는 Task, Performance, Training Experience입니다. 

아이를 키우는 환경에 비유를 하자면 아이가 어떤 행동(Task)를 하고 칭찬,격려나 혹은 꾸중(Performance)를 들었을 때 아이가 자발적으로 얻은 경험을 통해 행동을 교정하는(Training Experience) 모습 이라고 할 수 있습니다. 

<br>

## Machine이 학습한다는 의미.

___

컴퓨터공학에서 일반적인 프로그램을 작성할 때는 코드의 로직에 따라 프로그램의 작동방식을 작성하면 되고 이 방식에 따라 컴퓨터가 작동할 뿐이였습니다. 

기계학습은 단순한 로직을 따르는 것 뿐만 아니라 수 많은 데이터를 기반으로 학습된 모델이 새로운 데이터에 대한 예측값을 뽑아내는 개념을 더합니다. 예측값을 뽑아내는 알고리즘이 있는 것은 사실이지만 예측값이 정확도는 우리가 가공하고 넣어야할 입력값에 많은 영향을 받습니다. 

다량의 데이터를 집어넣는 과정에서 사람의 개입 없이 모델이 스스로 학습하고 성능이 좋아지는 점이 일일이 코드를 개선하며 프로그램의 성능을 향상하던 기존의 방식과 다릅니다. 

<br>

### 알고리즘보다는 데이터가 중요.

같은 구조(같은 머신러닝 알고리즘)을 가진 모델이여도 데이터셋이 다르면 학습된 모델이 달라집니다. 그만큼 데이터가 중요하고, 데이터 중심&모델 중심의 방식이라고 볼 수 있습니다. 

<br>

## AI > Machine Learning > Deep Learning 개념차이

___

AI는 포괄적인 의미의 인공지능으로써 단순히 말하자면 '인공지능은 인간의 지능, 사고, 감각을 재현한 것'이라고 정의할 수 있습니다. 인간과 비슷하거나 더 뛰어난 인지능력 및 지능을 가지고 있으며 일률적인 일이 아닌 새로운 일은 만들어내고 능동적으로 수행합니다. 

좁은 의미의 AI(Narrow A.I) : 한가지 영역에서만 능력을 가집니다. 주로 기업 입장에서 다루는 A.I입니다. 

넓은 의미의 AI(General A.I) : 일반적인, 전 영역에서 능력을 가지는 A.I입니다. 

Machine Learning은 앞서 소개했듯이 데이터를 이용해 인간의 개입 없이 모델을 학습시키고, 새로운 데이터의 결과를 예측합니다. 대용량의 데이터의 특성(features), 패턴(pattern)을 학습해서 그 결과를 바탕으로 신규 데이터에 대한 적절한 결과값을 도출합니다. 

Deep Learning은 Machine Learning에서 인간의 뇌에 있는 뉴런(Neuron)개념을 탑재한 것입니다. 인간의 뉴런은 뇌속에 수조개가 존재하며 서로 상호작용하며 인지역할을 하는데 이를 본따 모델의 학습패턴을 상호작용하는 패턴으로 변화하고 또 상호작용의 횟수를 늘림으로써 보다 효율적이고 강력한 결과값을 도출할 수 있습니다. 

AI가 제일 범주가 크고 그 안에 Machine Learning, 그리고 가장 안쪽에 Deep Learning이 있습니다. 

<br>

## Machine Learning이 쓰이는 분야

___

ML은 아주 다양한 분야에서 쓰이는데 초기에는 이미지 복원에 가장 많이 쓰였습니다. 그러면서 점점 로봇공학, 네트워크의 발달, 빅데이터의 축적이 이뤄지면서 AI speaker, 검색엔진, 자연어 처리, 자율주행, 의료분야, 추천엔진, AI로보틱스 등 다양한 분야로 쓰임이 넓어지고 있습니다.