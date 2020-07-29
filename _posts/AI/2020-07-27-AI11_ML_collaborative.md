

collaborative filtering


추천 협업 시스템....workshop을 풀면서 정리할 예정.

넷플릭스.... 영화도 사이의 유사도. 

사용자기반 추천 시스템. . 사용자가 ㅈ신이 본 영화들 주에서 ㅕㅇ점을 매기면.. . .     . .



item기반이냐, 사용자 기반이냐. 로직은 똑같은데 
..
.
item기반이 더 쉽다. 

.
.
쿠팡... 이전 구매이력...... 조회한 이력... 머 그런걸로. 유사도 알고리즘(추천 협업 시스템)

.
.
명시적인 데이터, 암시적인 데이터 (조회한 내역, 구매한 내역) 둘다 데이터 확보를 위해서 쓰일 필요가 있다. 

아마존 사이트에서도 사용자기반이던 아이템기반이던 



validation -> training data가 현저히 부족할 때 . . . . .

7번이상 나누지 말것. 

epoch - 전체 데이터를 한 번 학습시키는 것. 

augmentation > 변형해서 양을 늘리는 것. 

inference는 테스트가 끝나고 다시 제대로 하는 것. 

정확하게는 height가 먼저 나온다.  open으로 제공하는 이미지들은 모두 정사각형 개수다. 

channel - > rgb  입력데이터의 대상이 되는 이미지의 채널. 

이 끔찍하고 슬픈 불완전한 인간.

mnist 28 * 28 * 1 -- 99.8
0~9손글씨 숫자, 검정색 바탕에 흰색글씨
10개의 카ㅔ고리
10% 딥러닝...정확도

mnist-fashion

Cifar10 32 * 32 * 3 -> 99.3%
10개의 카테고리
정보량이 더 많다. . 복잡한 입력.

cifar 100 - 93% 100개의 카테고리. . 

카테고리 개수가 영향이 가장 많다.

imagenet - 88% 1000개의 카테고리


그러므로 카테고리는 50개를 넘지 않도록 한다.

실제로 클래스 카테고리가 10개라 하더라도 정확도 99%도 안나온다. 

--> 해상도가 천차만별...? 

지금 토이 이미지 테이터셋(해상도 낮고 이미지 사이즈 크고)로 99%가 나온 것이다. accuracy 99%가 나오기 어렵다.


보통 학술적으로 연구할때 92~95% (학사수준) 이 정도 나오면 잘 나옴. 

여기서 99% 대로 올리는 것은 박사수준. 

비용적인 측면 . . 50만원
비용적인 측면 . . 5000만원

-> 정확도를 올리는 데는 가성비를 따져라.

__

NN 모델. . . . . . . . W*x + b


2행 2열. 


예측하기 전에 반드시 softmax loss function을 사용한다. 

L(W) -> 모델에 대한 loss

L(Model(W1, W2, W2,...))

괜찮다는 의미. 

-> 친해서  

or

-> 관심없어서.

람다는 weight값을 낮춰줘서 분산윽 적게 해준.ㄴ 역할... 



w1*x+b1+w2*x+b2+w3*x+b3

w값이 작으면 굴곡이 완만해진다. 
w값이 크면 클수록 pdf에서 보이는 파란색 그래프가 만드어진다. 

데이터들의 분포가 산만하다. 안정적이지 않다. 분산이 크다. 오버피팅. 

w(weight)값이 작아질 수록 훨씬 안정적인 그래프를 그리는데.... 초록색. . . 

Loss Function에서 람다 이 부분은 weight의 크기를 줄여주는 역할
그렇기 때문에 Regularization을 써야 weight의 값을 안정적으로 만들ㅇ어주고 오버피팅을 막을 수 있다. -> full loss function


optimization -> 어떻게 내려갈지 정의...?

loss function  -> 현재 고도. . . . .(좌표가 아니라) 0이 되는 지점 : global minimum  가짜는 local minimum....

가장 가파른 경사를 찾을때 편미분이 쓰이고 

Back propagation 이라고 한다. 


gradient descent : back propagation방법을 써서 하강하는 모델.

loss에 따라서 weight가 달라진다.   loss에 가장 영향을 많이 끼치는 건 weight

loss가 높으면 weight를 많이 수정. 

loss가 많이 높지는 않으면 weight를 덜 수정. 

random search
random local search  backpropa는 아님. 

위에꺼 둘 다 trial error도 나옴. 



정리 . Gradient Descent : 가장 가파르게 loss(고도)를 감소시키며 하강하는 방법인데....
가장 가파르게 loss(고도)를 감소시키는 weight의 방향을 찾아낸다. 
가장 가파르게 loss(고도)를 감소시키는 weight의 방향을 trial error 없이 찾아내는 optimization방법 중의 하나다. 

Loss에 대해서 책임론을 정량화하는 수식. 

아..

망했네.



NN에는 ----> ANN / DNN / CNN / RNN

Fully Connected Net

feature map



NN Neural Network















왜 바로바로 말이 안나왔던 것일까. . . . . . . . . . . . . . . . . . .












Optimization

하강하는 방법

Loss Function
현재 고도를 측정하는 것

Gradient Descent
- Optimization 중의 하나
 Backpropagation 방법을 이용해서 하산하는 Optimization
 정확한 방향을 하나하나 계산하기 때문에 slow, 하지만 global minimum까지 정확하게 찾아간다.
 learnign_rate는 기본적으로 0.1을 기본적으로 사용. 

 Backpropagation
 가장 가파르게 내려갈 수 있는 방향을 정하는 것. 
 이때 미분(실질적으로 편미분)이 사용된다. 

2) Weight값이 loss에 얼마나 영향을 주었는지를 수치화한 다음에 
loss를 가장 많이 줄이는 방향으로 weight값을 업데이트
loss에 영향을 많이 주었으면(책임을 많이 진다) 수정값이 크고
loss에 영향을 작게 주었으면(책음을 적게 진다.)수정값이 작다.



|｜／￣＿＼―


Great!!!!!                 |｜／￣＿＼―
Great!!!!!
Great!!!!!
Great!!!!!
Great!!!!!
Great!!!!!
Great!!!!!
Great!!!!!
Great!!!!!
Great!!!!!
Great!!!!!










