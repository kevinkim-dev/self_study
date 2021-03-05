# Generator와 Expression의 차이를 설명해보아라

`Generator란 무엇인가?`

> Generator(제네레이터)



- Generator는 iterator를 생성해주는 함수이며, 함수 안에서 yield라는 특별한 키워드를 사용한다.
  - Iterator 잠깐 복습!

    - Iterator란 iterable한 객체에서 값(element)을 하나씩 꺼낼 수 있는 객체를 말한다.
    - Iterable하다는 것은 값을 순차적으로 하나씩 꺼내는 것이 가능한 객체이다.
    - Iterable한 객체에는 list, tuple, set, dictionary, string 등이 있다.

  - Iterator 심화

    - Iterable한 객체는 dir()을 통해 속성을 확인해보면 `__iter__`를 가지고 있다. `__iter__` 은 iterator 생산자인 iter() 함수를 사용할 수 있게 해주는 ''스페셜 메소드'' 이다.
    - iterable한 객체에 iter()를 붙여 iterator를 만들 수 있다. iterator는 `__next__` 라는 스페셜 메소드를 사용할 수 있다. `__next__`는 iterable한 객체의 element를 차례로 반환하게 해주는 next() 함수를 사용할 수 있게 해주는 "스페셜 메소드"이다.
    - `__next__` 는 호출 될때마다 다음 element를 반환하는데, iterable은 항상 끝이 있을 것이다. 끝까지 다 반환하고 나면 StopIteration Exception이 발생한다.

    ```python
    a = [1, 2, 3] 			# iterable한 객체인 list
    b = '123'				# iterable한 객체인 string
    
    a_iter = iter(a)		# iterable한 객체인 list의 iterator 생성
    b_iter = iter(b)		# iterable한 객체인 string의 iterator 생성
    
    print(dir(a))			# 이 밑으로는 꼭 직접 돌려보면서
    print(dir(b))			# 스페셜 메소드의 존재를 확인하면 좋을 것 같다.
    print(dir(a_iter))
    print(dir(b_iter))
    print(type(a_iter))
    print(type(b_iter))
    ```

    - 복권 뽑기로 비유를 해보자.

      > 1부터 45의 숫자공(element)이 들어 있는 추첨기(iterable)를 본 적이 있을 것이다. 진행자(iterator)는  추첨기에 손을 넣고 숫자공(element)를 ''하나씩'' 뽑는다(next())
      >
      > 진행자가 이미 보너스 번호까지 7개의 공을 다 꺼냈는데, 또 꺼내려고 손을 집어 넣는다. 다른 진행자가 이미 다 뽑았다며 그 사람을 만류한다(StopIteration Exception)

- Generator

