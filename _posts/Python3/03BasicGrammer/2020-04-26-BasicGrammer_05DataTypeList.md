## Immutable Sequence, Mutable Sequence

**Sequence**형에도 종류가 있습니다. 크게 **불변 시퀀스**와 **가변 시퀀스**로 나뉘어 지는데 문자열은 대표적인 불변 시퀀스 입니다. 문자열에서 더하기 연산같은 경우 각기 다른 두 문자열 객체를 이어 붙여 새로운 객체를 생성한 것입니다. 

~~~python
str1 = 'Hello'
str2 = 'World'
str3 = str1 + str2
print(str3)
~~~

불변시퀀스의 경우 선언이 될 때마다 메모리의 공간이 달라집니다. 

메모리 공간 두 곳에 생성된 객체를 가져와서(str1, str2) 새로운 변수(str3)에 두 객체를 더한 새로운 문자열 객체를 지정하게 됩니다.<br>

반면 가변시퀀스의 경우에 메모리공간이 하나가 주어지고 그 메모리공간 늘어나는 형식으로 관리가 됩니다. <br>대표적인 것이 이제부터 알아볼 **Lists**입니다.

 

불변시퀀스와 가변시퀀스의 명확한 차이점을 알기 위해서 아래의 코드를 쳐봅시다.

~~~python
testSequence = 'str is immutable sequence'
testList = []

print(id(testSequence)) #1422747973072
print(id(testList))		#1422748154560

testSequence = 'memory address was changed'
testList.append(1)

print(id(testSequence)) #1422748470368
print(id(testList))		#1422748154560

#가변시퀀스인 리스트는 객체의 주소가 변하지 않는다.
#불변시퀀스인 문자열은 객체의 주소가 변한다.
~~~



| 분류       | 이름                                                         |
| ---------- | ------------------------------------------------------------ |
| 불변시퀀스 | Sclasstring(문자열), Tuple(튜플), 바이트열(Bytes)            |
| 가변시퀀스 | Lists(리스트), 바이트 배열(Byte Arrays), arrays(확장 모듈 array) |

## Lists(리스트)

**Lists(리스트)**는 일반적으로 동일한 타입의 **객체**들의 모음을 저장하는데 사용됩니다. 

#### 리스트 초기화하기

~~~python
if __name__ == '__main__':
    list1 = []
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list3 = list('Hello World!')
    list4 = list((1, 2, 3))
    print(list1)
    print(list2)
    print(list3)
    print(list4)
~~~

리스트를 초기화하는 방법은 위와 같은 방법들이 있습니다. 여기에 더해서 나중에 반복문인 for문을 배우면 **List comprehension**이라는 초기화 방법을 배우고 **iterator 타입**이라는 것을 배우면 list(iterable)형식으로 초기화하는 방식을 배울 것입니다. 

![listresult](./images/listresult.png)

코드를 보면 알겠지만 리스트는 '**[**'와 '**]**' 기호를 가지고 초기화할 수 있습니다.<br>list1은 **빈 리스트로 초기화**가 되었고 list2는 1부터 10까지를 리스트의 값으로 만들었습니다. <br>list3는 문자열을 넣어주고 각 문자를 리스트의 값으로 만들었습니다. list4는 리스트 안에 Tuple이라는 것을 넣은 코드입니다. 



### Lists안에 Lists

물론 리스트의 값에 또 다른 리스트가 들어갈 수 있습니다.

```python
if __name__ == '__main__':
    list1 = []
    inList1 = [1,2,3]
    inList2 = [10, 20, 30]
    inList3 = [100, 200, 300]

    list1.append(inList1)
    list1.append(inList2)
    list1.append(inList3)
	
    print(list1[0][0])
    print(list1[0][1])
    print(list1[0][2])
    print(list1)
'''
결과:
1
2
3
[[1, 2, 3], [10, 20, 30], [100, 200, 300]]
'''
```

list1[0]은 inList1이 되고, list1[1]은 inList2가 되고 list1[2]는 inList3이 됩니다. <br>중첩된 리스트의 값에 접근하려면 `list1[0][0]`과 같이 `[]`기호를 두번 쓰면 됩니다. 첫번째 index자리에는  list1[0]의 값이 들어가고 두번째 index자리에는 list1[0]안에서 0번째의 값을 의미합니다.  

## 공통연산자 (가변 시퀀스)

가변 시퀀스의 공통 연산자들 중에서 자주 쓰이는 것을 확인해보겠습니다.

~~~python
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = list('Hello World!')
~~~

값  초기화

~~~python
	list1[0] = 100  #Indexing방법으로 접근... 0번째 값 출력
    print(list1) #[100, 2, 3, 4, 5, 6, 7, 8, 9, 10]
~~~

슬라이스 초기화

~~~python
	list1[0:5] = [5,4,3,2,1]    #문자열다루기에서 배웠던 슬라이싱!
    print(list1) #[5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
~~~

슬라이스 삭제

~~~python
	del list1[0:5]   		#첫번째부터 5개 지우기!
    print(list1) #[6, 7, 8, 9, 10] -> 리스트의 크기가 5로 줄었다. 
~~~

제일 끝 인덱스에 값 추가

~~~python
	list1.append(11) 
    print(list1) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
~~~

모든 항목을 제거(빈 리스트로 초기화)

~~~python
	list1.clear() #del list1[:]과 같습니다.
    print(list1) #[]
~~~

리스트의 얕은 복사본 생성

~~~python
	list3 = list1.copy()
    print(list3) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
~~~

지정한 인덱스에 값을 삽입

~~~python
	list1.insert(3, 100) #index가 3인 곳의 값을 100으로 초기화
    print(list1) #[1, 2, 3, 100, 4, 5, 6, 7, 8, 9, 10]
~~~

지정한 인덱스의 값을 리스트에서 꺼내버리기.

~~~python
    number = list1.pop(3)
    print(number) # 4
    print(list1) #[1, 2, 3, 5, 6, 7, 8, 9, 10]
~~~

특정 값과 같은 첫번째 값을 리스트에서 제거

~~~python
	list1.remove(4)
    print(list1) #[1, 2, 3, 5, 6, 7, 8, 9, 10]
~~~

값을 역으로 배치

~~~python
	list1.reverse()
    print(list1) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
~~~



#### Lists 정렬하기(Lists용 추가 메소드)

~~~python
if __name__ == '__main__':
    list1 = [6, 8, 2, 5, 1, 9, 10, 3, 4, 7]
    list1.sort()
    print(list1) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
~~~

**정렬**이라고 하는 것은 일정한 순서대로 값을 재배치하는 것을 말합니다. sort()메소드를 통해 1부터 10까지 오름차순으로 정렬할 수 있습니다. 

'정렬'이라고 하는 것은 '컴퓨팅 알고리즘'에서 굉장히 중요한 분야입니다.  

사람은 저 뒤죽박죽인 리스트를 보고 한번에 1과 2를 앞으로 옮기는 사고를 할 수 있지만 컴퓨터는 그렇지 못합니다. 한번에 하나의 값만 옮기거나 확인할 수 있습니다. 이런 한계가 있기 때문에 정렬을 하는 것은 효율적인 데이터 접근을 위해서 매우 중요합니다. 