# Statement와 Expression의 차이를 설명해보아라

`Statement`

> 파이썬에 모든 한줄 한줄이 Statement



- .py 파일의 모든 줄은 Statement이다
- Statement는 특정 액션을 수행하는 코드를 말한다. Statement는 값을 도출 할 수도 있으며 아닐 수도 있다. 



`Expression`

> 어떠한 값을 가지고 있으면 Expression



- Expression은 값과 변수와 연산자의 조합으로 되어있다.
- 그 조합으로 도출되는 값이 있어야 Expression 이다.



`Statement와 Expression의 상관관계`

> Expression ⊂ Statement



- 위의 두 내용을 가지고 결론부터 말하면 Expression은 Statement의 부분집합이며, 모든 Expression은 Statement이다

- 둘의 차이점은 [도출되는 값이 "꼭" 있어야 하는가?] 이다.

- 이 차이점을 알기 위해서는 Compiler가 아니라 Interpreter를 사용하면 된다.

  - Compiler: 코드의 처음부터 끝까지 다 검사하여 machine code로 변환하는 프로그램

    VScode, Pycharm과 같이 어떤 .py 파일에 적고 싶은 만큼 적고 실행을 누르는 스타일의 프로그램이 Compiler라고 보면 된다.

    python.exe를 실행 시킨 후 File -> New File을 통해 스크립트를 작성할 때도 Compiler를 이용하는 것이다.

    

  - Interpreter: 코드 한 줄, 한 줄이 입력 될 때마다 코드를 실행하는 프로그램

    명령프롬포트나 VScode의 Bash창에서 python을 입력하고 코드를 한줄씩 입력하는 것이 Interpreter이다.

    python.exe를 그냥 켜서 나오는 창(Python 3.5.3 Shell)도 Interpreter이다

    

- Interpreter에서 코드를 작성하고 엔터키를 눌렀을 때 값이 나오면 Expression이다.

- ~~Interpreter에서 코드를 작성하고 엔터키를 눌렀을 때 값이 나오지 않으면 Statement이다.~~

  주로 하는 오해인데, 코드의 모든 줄이 Statement이므로, 값이 나오던 나오지 않던 Statement이다.

  즉 값이 나오지 않는 것은 그냥 Expression이 아닌 Statement인 것이고, 값이 나오면 Expression인 Statement인 것이다.

- 예시를 보면 차이점이 더 잘 드러날 것이다.

  ```python
  # Expression인 Statement 
  # 엔터를 누르면 출력이 있다
  >>> 3					# 그냥 값
  3						
  >>> 1 + 2				# 연산
  3
  >>> x = 3 				# 이건 Expression이 아닙니다!(밑의 줄을 위한 statement)
  >>> x					# 변수
  3
  
  
  # Expression이 아닌 Statement
  # 엔터를 눌러도 출력이 없다.
  >>> x = 3				# 할당
  >>>	if True:			# 조건문
  >>> import requests		# import 등등...
  ```

- Python을 단순 계산기처럼 쓰려는 것이 아니라면 Expression만으로 코드를 짜는 일은 없다. Expression을 통해서 나온 값을 변수로 할당한다던지, 판단을 한다던지의 과정을 거쳐서 다른 statement 속의 expression에 전달을 해야만 코드가 완성되는 것이다.

  - 오늘도 어김없이 등장하는 Subway를 통한 간단 예시

    > CS_Study 1주차 2번에 예시로 들었던 분업이 잘 되어 있는 서브웨이 B점을 다시 불러옵니다.
    >
    > 서브웨이 B점의 세명의 직원 a, b, c(Statement)는 분업을 하여 맛있는 샌드위치를 만들어 팔기(완성된 코드) 위해 분업을 하였다.
    >
    > 직원 a가 빵을 가르고 내용물을 채워서(expression) 직원 b에게 건내면, 소스를 뿌리고 포장해서(expression) 직원 c에게 건내고, c는 계산을 하고 샌드위치를 손님께 건냅니다(expression).

    - expression 만으로는 코드를 완성시킬 수는 있지만, 그건 계산기랑 다를바가 없다. 코딩으로 가치를 창출하려면 그것보다는 무언가 복잡한 일을 하는 것이 일반적이다.

      > 빵이 직원 a에서 갈라지고 내용물이 채워지고, 직원 b에게서 소스가 뿌려지고 포장되고, 직원 c의 손을 통해 판매가 되어야지 맞는 것이지, 그냥 빵을 손님에게 건내는 것은 의미가 없습니다. 그것은 샌드위치를 파는게 아니라 그냥 빵을 주는 거니까요.

    - expression으로 나온 값을 다음 Statement에게 전달해서 추가적인 일을 해야만 합니다. 그 과정에서 가장 자주 쓰이는 Statement인 할당이 또 필요합니다.

      > 직원 a가 빵을 가르고 내용물을 채워서 직원 b에게 "쨔잔!" 하고 보여준다고 해서 샌드위치를 만드는 작업을 진행할 수 없습니다. 빵을 가르고 내용물을 채우고, b한테 전달까지 해야 자신의 임무를 완수한 것입니다.
      >
      > python에서도 1 + 2 를 입력하면 3이 나오지만, 그 결과인 3을 사용하려면 변수에 할당해야 하고, 함수 x + y 를 만들어, x 에 1을 입력하고, y에 2를 입력하여 x+y = 3을 얻어내도 return하지 않으면 그 값을 사용할 수가 없습니다. 

      

`결론`

> 완성된 코드를 위해서 Statement와 Expression이 모두 필요하다.



- Expression은 결과를 연산하고 표현 하는 것
- Statement는 결과를 연산하고 표현하는 것 뿐만 아니라, 할당, 전달, 선언 등을 통해 결과를 매끄럽게 이용할 수 있게 하는 것