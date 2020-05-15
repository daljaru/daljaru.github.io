## Data Type(자료형)

Python의 대표적인 자료형을 알아보겠습니다. <br>파이썬에서 자주 사용하는 5가지의 자료형이 있습니다. 

* Number(숫자형)
* String(문자열) (Sequence Type)
* List(리스트) (Sequence Type)
* Tuple(튜플) (Sequence Type)
* Dictionary(딕셔너리) ()



### Number

우린 숫자형을 다루는 걸 이미 앞에서 해봤습니다. 

~~~python
#두 숫자를 더하는 프로그램
var1 = 10
var2 = 20
var3 = var1 + var2
print(var3)
~~~



### Numerical types

* int (signed integer) 정수
* long (long integers) 정수(배정할 수 있는 수가 크다.)
* float (floating point real value) (실수)
* complex (complex numbers) (허수)

숫자형 안에 위와같이 네가지의 타입이 더 있습니다. 당연히 컴퓨터프로그램이 정수만 쓸 수 있으면 안되겠죠. 우리가 사용하는 모든 수를 다룰 수 있어야 컴퓨터라고 할 수 있겠죠.

~~~python
#정수형                 변수명은 자신이 하고 싶은대로! 그렇지만 다른 사람도 알아볼 수 있도록 하자. 
var1 = 10              #정수형 객체 10을 변수 var1으로 지정합니다.
var2 = 20
var3 = var1 + var2
print(var3)

#정수형
long1 = 51924361
long2 = 122
long3 = long1 + long2
print(long3)

#실수형
myHeight = 175.5  #실수형 객체 175.5를 변수 myHeight로 지정합니다. 
yourHeight = 3.14e-10
averageHeight = (myHeight + yourHeight) / 2
print(averageHeight)

#complex형
cplx1 = 3.14j
cplx2 = 45.j
cplx3 = cplx1 + cplx2
print(cplx3)
~~~

.![calNumeric](./images/calNumeric.png)



앞에서 Python의 특징을 말할 때 동적인 데이터 타입 결정 지원(Dynamic Typing)이 있었습니다. 사실 파이썬이 쉽다고 하는 이유 중에 가장 큰 이유라고 할 수 있습니다. <br>위의 코드를 C++로 만든다면 아마 아래와 같이 했을 것입니다. 

~~~C++
//C++의 코드입니다. 
int val1 = 10;
int val2 = 20;
int val3 = 10 + 20;
std::cout<<val3<<std::endl;

long long1 = 51924361L;
long long2 = 122L;
long long3 = long1 + long2;
std::cout<<long3<<std::endl;


double myHeight = 175.5;
double yourHeight = 3.14e-10;
double averageHeight = (myHeight + yourHeight) / 2;
std::cout<<averageHeight<<std::endl;
~~~

다른 언어들은 변수명 앞에 변수의 타입을 적어주는 것이 보통입니다. 그러나 파이썬은 그런 과정없이 변수명만 적고 객체를 지정하면 실행시 자동으로 변수의 타입이 지정된 객체의 타입으로 정해지는 방식을 채택하고 있습니다. 



#### Dynamic Typing에 대한 이해

**동적 데이터 타입 결정(Dynamic Typing)**이 잘 이해가 되지 않는다면 아래의 코드를 봅시다. type()메소드는 객체의 타입을 확인합니다. 

~~~python
valuable = 10
print(type(valuable)) #<class 'int'>
~~~

변수 valuable과 정수형 객체 10을 연결하고 valuable의 타입을 출력해보면 'int' 클래스 타입이라고 나옵니다. 

~~~python
#이어서 valuable 변수를 실수로 초기화해보겠습니다. 
valuable = 10
print(type(valuable)) #<class 'int'>
valuable = 10.5
print(type(valuable)) <class 'float'>   
~~~

이번엔 'float'클래스 타입이라고 나오는 것을 확인 할 수 있습니다.<br>이렇게 변수에 어떤 객체를 넣느냐에 따라 코드의 실행시간에 타입이 결정되는 것을 **동적 데이터 타입 결정(Dynamic Typing)**이라고 합니다. 



## 숫자의 연산

자주 쓰이는 연산은 아래와 같습니다. 

~~~python
if __name__ == '__main__':
    number1 = 10
    number2 = 20
~~~

덧셈

~~~python
    number3 = number1 + number2 
    print(number3) #30
~~~

~~~python
	number1 += 1
    print(number1) # 11
~~~

뺄셈

~~~python
	number3 = number1 - number2
    print(number3) # -10
~~~

~~~python
	number1 -= 1
    print(number1) # 9
~~~

곱셈

~~~python
    number3 = number1 * number2
    print(number3) #200
~~~

~~~python
	number1 *= 2
    print(number1) = 20
~~~

나눗셈

~~~python
	number3 = number1 / number2
    print(number3) #0.5
    number3 = number2 / number1
    print(number3) # 2.0
~~~

~~~python
	number1 /= 2
    print(number1) #5.0
~~~

나눗셈(정수로 내림한 몫 구하기(소수점이하 버리기))

~~~python
	number3 = number1 // number2
    print(number3) #0
    number3 = number2 // number1
    print(number3) #2
~~~

~~~python
	number1 //= 2
    print(number1) = 5
~~~

나눗셈(나머지 구하기)

~~~python
	number3 = number1 % number2
    print(number3) #10
    number3 = number2 % number1
    print(number3) #0
~~~

~~~python
	number1 %= 2
    print(number1) = 0
~~~

나눗셈의 쌍

~~~python
print(divmod(number2, number1)) #(2, 0)
~~~

음의 값

~~~python
	number3 = -number2
    print(number3) #-20
~~~

절대값 구하기

~~~python
    number4 = -2.5
    print(abs(number4)) #2.5
~~~

정수로 변환

~~~python
	number4 = -2.6
    print(int(number4)) #-2
~~~

실수로 변환

~~~python
	print(float(number1)) #10.0
~~~

거듭제곱

~~~python
	print(pow(number1, 2)) #100
~~~



