### Break, Continue

반복문 안에서만 쓰이는 제어흐름도구들이 있습니다. 

**Break**을 쓰면 현재 블록의 반복을 즉시 중단하고 반복문을 나옵니다.

~~~python
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    index = 0

    while index < len(list1):
        if index == 3:
            index += 1
            break
        print("index" + str(index) + ": "+str(list1[index]))
        index += 1
    print(index)
'''
결과:
index0: 1
index1: 2
index2: 3
4
'''
~~~

위 코드를 보면 list1에 있는 내용을 출력하는데 `if index == 3`조건문 아래에 **break**를 넣었습니다. index가 3이 되면 break를 만나게 되고 그 즉시 해당 반복문을 빠져나오게 됩니다. 그래서 index는 4에서 더 늘어나지 않은채 프로그램이 종료됩니다.



continue는 약간 다릅니다. continue는 **"현재 진행되고 있는 반복흐름만 한번 스킵한다"**는 의미입니다. **반복문을 빠져나가지는 않습니다.** continue가 실행이 되면 해당 반복문에서 continue아래에 있는 라인 전부가 스킵됩니다. 위 코드에서 break자리에 continue를 넣어볼까요

~~~python
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    index = 0

    while index < len(list1):
        if index == 3:
            index += 1
            continue;
        print("index" + str(index) + ": ", end='')
        print(list1[index])
        index += 1
    print(index)
'''
결과:
index0: 1
index1: 2
index2: 3
index4: 5
5
'''
~~~

결과를 보니 5까지 끝까지 출력되었습니다. index가 3인 경우에 **continue**문이 있고 해당 반복문의 continue아래의 내용을 한번 건너뛰었습니다. 위 코드에서는  `print("index" +...`부터 `index += 1`까지를 스킵했습니다. 

 이렇게 break와 continue는 각자 다른 방식으로 반복을 제어하는 역할을 합니다.  

