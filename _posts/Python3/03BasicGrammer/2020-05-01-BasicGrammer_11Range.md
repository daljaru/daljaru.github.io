## Range()

range형은 숫자의 범위를 나타내는 내장 클래스입니다. range는 **숫자형 불변 시퀀스**입니다. <br>range(start, stop, step)형식으로 쓰입니다. 일정한 간격이 있는 수열을 만들고 싶을 때 range를 쓰면 편리합니다. **start**는 시작하는 숫자, **stop**은 마지막 (검사)숫자, **step**은 간격입니다. 아래 예시를 볼까요.

~~~python
if __name__ == '__main__':
    print(range(5))
    
    testList = list(range(5)) #range(0, 5)와 같습니다. 숫자가 하나만 쓰이면 start가 0으로 책정이 되고 stop이 인자값으로 정해집니다. step의 기본값은 1입니다. 
    testList2 = list(range(3, 8))
    testList3 = list(range(1, 10, 2))
    testList4 = list(range(-1, -10, -3))
    print(testList)
    print(testList2)
    print(testList3)
'''
결과:
range(0, 5)
[0, 1, 2, 3, 4]
[3, 4, 5, 6, 7]
[1, 3, 5, 7, 9]
[-1, -4, -7]
'''
~~~

testList는 range(5)이기 때문에 0(기본)부터 5 직전까지 **1**씩 늘어납니다. <br>testList2는 range(3, 8)이기 때문에 3부터 8 직전까지 **1**씩 늘어납니다.<br>testList3은 range(1, 10, 2)이기 때문에 1부터 10 직전까지 **2**씩 늘어납니다.<br>testList4는 range(-1, -10, -3)이기 때문에 -1부터 -10직전까지 **-3**씩 줄어듭니다.

 range()는 시퀀스 형이기 때문에 **공통시퀀스연산을 지원**합니다. (Slicing, in, count, len 등등) 그렇지만 +연산(append)과 *(multiple append) 연산은 지원하지 않는 특징이 있습니다.  range()안에 있는 값을 확인하려면 순서있는 시퀀스로 바꿔야 합니다. (Lists 등)

~~~python
if __name__ == '__main__':
    r = range(10)
    print(len(r))
    print(r[5])
    print(8 in r)
    print(r[3:5])
'''
결과:
10
5
True
range(3, 5)
'''    
~~~



### for문에서 range()

주로 for문과 가장 많이 쓰입니다. 

~~~python
if __name__ == '__main__':
    for i in range(5): # for i in range(0, 5)
        print(i)
'''
n번 반복하고 싶을 때 range를 쓰면 편리합니다. 
결과:
0
1
2
3
4
'''
~~~
