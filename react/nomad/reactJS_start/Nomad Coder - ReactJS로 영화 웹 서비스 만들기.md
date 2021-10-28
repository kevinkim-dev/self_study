# Nomad Coder - ReactJS로 영화 웹 서비스 만들기



## #0 Introduction



### 0.0 Introduction

- 왜 리액트를 좋아하는지
- 어떻게 활용
- 어떻게 앱을 만ㄷ르지
- API 다용법
- 데이터 출력법
- 배포하는법



### 0.1 Requirements

- npm : v6.9
  - 진행 버젼: 6.14.12
- node.js : version 10 or 12
  - 진행 버전: v14.16.1
- npx
  -  진행버젼: 6.14.12

- Visual Studio Code
  - 많은 플러그인 등
- Git
  - 진행버젼: 2.30.0.windows.1





### 0.2 Theory Requirement

- HTML
- CSS
- Vanila JS
  - function, variable, class



### 0.3 Why react

- facebook이 만들었음
- airbnb, npm, netflix, spotify, slack 등 많은 major 사이트들이 react를 씀
- facebook이 많은 지원을 하고 있음
- 프론트 생태계중 react가 64.8가 사용하고 앞으로도 사용한다. 다른 vue, angular등에 비해 압도적으로 높음





## #1 Setup



### 1.0 Creating your first React App

- browser는 이 코드를 이해하지 못하기 때문에 webpack과 babel이 필요함
- 하지만 이것을 `create react app` 하나로 해결

```
npx create-react-app <app 이름>
```

- yarn == npm

```
npm start
```





### 1.1 Creating a Github Repository

```
git init

git remote add origin <git 주소>
git add .
git commit -m "<commit name>"
git push origin master
```





### 1.2 How does React work?

- public
  - favicon
    - 브라우져 상단에서 탭에 보여지는 이미지
  - index
    - 초기 비워져 있음
  - manifest.json
    - 무시

- src

  - App.js

    ```javascript
    import React from "react"
    
    function App() {
      return <div>Hello!!!!</div>
    }
    
    export default App;
    ```

  - index.js

    ```javascript
    import React from 'react';
    import ReactDOM from 'react-dom';
    import App from './App';
    
    ReactDOM.render(<App />, document.getElementById('root'));
    ```

    index.html의 root id를 가진 div에 app.js의 내용을 집어 넣는 기본적인 코드





## #2 JSX & Props



### 2.0 Creating your first React Component

- component

  - HTML문법을 반환하는 함수(function)
  - <(function name) /> 형식으로 사용
  - 이러한 react에 특화된 javascript 와 HTML 사이의 조합을 JSX라고 부른다.

- component 제작하기

  - <이름>.js 파일 생성

  - 상단에 `import React from "react"` 추가

  - 하단에 `export default <이름>;  `추가

  - 중간에 function 작성

    ```javascript
    import React from "react"
    
    function Potato() {
        return <h3>I love potato</h3>
    }
    
    export default Potato
    ```

- component 사용하기

  - react의 DOM render는 한개의 element만 가능하다. 
  - 기본적으로 app.js를 render하므로 import를 index가 아닌 app에 해서 사용하면 된다.

  ```javascript
  import React from "react"
  import Potato from "./Potato"
  
  function App() {
    return <Potato />
  }
  
  export default App;
  ```





### 2.1 Reusable Components with JSX + Props

- component 사이에 정보를 주고 받을 수 있다.

  - 부모 컴포넌트에서 자식 컴포넌트에 이름을 설정해서 props를 넘겨줄 수 있다. (property)
  - 자식 컴포넌트에서 해당 이름을 사용해서 props에 접근할 수 있다.

  ```javascript
  import React from "react"
  
  // function Food(props) {
  function Food({ fav }) {
    console.log(fav)
    return <h3>I like {fav}</h3>
  }
  
  function App() {
    return (
      <div>
        <h1>Hello</h1>
        <Food fav="kimchi" />
        <Food fav="ramen" />
        <Food fav="samgiopsal" />
        <Food fav="chukumi" />
      </div>
    )
  }
  
  export default App;
  ```

  - props에 접근하는 법

    - 함수 뒤의 argument에 props를 쓰고 객체 attribute에 접근하기
    - es6의 문법을 이용해서 {<attribute>} 사용

    

### 2.2 Dynamic Component Generation

- 동적 데이터 생성

- map

  - array를 통해서 array를 줌

  ```javascript
  const friend = ["a", "b", "c", "d"]
  
  friend.map(current => {
      console.log(current);
      return 0
  })
  => [0, 0, 0, 0]
  
  friend.map(current => {
      return current + "e"
  })
  => ["ae", "be", "ce", "de"]
  ```

  - 각 요소를 순서대로 접근해서 요소를 함수의 parameter로 넘기고 해당 함수의 return 에 맞는 연산을해서 해당 return 값의 array를 반환

  ```javascript
  import React from "react"
  
  function Food({ name, picture }) {
    return (
      <div>
        <h3>I like {name}</h3>
        <img src={picture} alt="food" />
      </div>
    )
  }
  
  const foodILike = [
    {
      id: 1,
      name: "Kimchi",
      image:
        "http://aeriskitchen.com/wp-content/uploads/2008/09/kimchi_bokkeumbap_02-.jpg"
    },
    {
      id: 2,
      name: "Samgyeopsal",
      image:
        "https://3.bp.blogspot.com/-hKwIBxIVcQw/WfsewX3fhJI/AAAAAAAAALk/yHxnxFXcfx4ZKSfHS_RQNKjw3bAC03AnACLcBGAs/s400/DSC07624.jpg"
    },
    {
      name: "Bibimbap",
      image:
        "http://cdn-image.myrecipes.com/sites/default/files/styles/4_3_horizontal_-_1200x900/public/image/recipes/ck/12/03/bibimbop-ck-x.jpg?itok=RoXlp6Xb"
    },
    {
      name: "Doncasu",
      image:
        "https://s3-media3.fl.yelpcdn.com/bphoto/7F9eTTQ_yxaWIRytAu5feA/ls.jpg"
    },
    {
      name: "Kimbap",
      image:
        "http://cdn2.koreanbapsang.com/wp-content/uploads/2012/05/DSC_1238r-e1454170512295.jpg"
    }
  ];
  
  function App() {
    return (
      <div>
        <h1>Hello</h1>
        {foodILike.map(dish => <Food name={dish.name} picture={dish.image} />)}
      </div>
    )
  }
  
  export default App;
  ```

  

### 2.3 map Recap

- map을 쓸 때 unique한 key혹은 id가 있어야 한다.
- key={dish.id} 와 같이 key를 추가해주어야 warning이 사라진다.



### 2.4 Protection with PropTypes

- prop-types

  - prop type이 적합한지 확인해주는 라이브러리

  ```
  npm i prop-types
  ```

  - import 해야 사용 가능

  - type체크와 존재 유무 체크 가능

    ```javascript
    PropTypes.<type name>[.isRequired]
    ```



## #3 STATE



### #3.0 Class Components and State

- function (name)() {} :  function Component
- class (name) extends React.Component {} : class Component
- class Compoenent는 return이 없다.
- return 대신 render 메서드를 사용한다.
- render method에 return값을 줘서 사용한다.
- react가 자동으로 class component의 render 메서드를 실행시킨다.
- class component에 필요한 정보를 넣는 state가 있음





### #3.1 All you need to know about State

- state를 함수에서 직접적으로 바꾸면 warning이 뜨고 보여지는 것은 바뀌지 않는다
  - 왜냐하면 함수를 실행해도 render가 다시 실행되지 않으므로 반영이 되지 않음
- setState 함수를 사용하면 react가 rerender를 해야한다고 알기 때문에 setState를 사용해야한다.
- setState 함수를 사용할 때 this.state.<attribute> 로 사용하는 것을 비추천한다
  - 대신 current를 인자로 받아와서 사용





### #3.2 Component Life Cycle

- react class component는 render말고도 Life Cycle에 해당하는 함수가 더 있음
- mounting
  - component가 생성될 때
  - constructor가 실행됨
  - 그 후 render 실행
  - 그 다음 componentDidMount 실행
- updating
  - component가 업데이트 될 때
  - client에 인해서 일어남
  - render 실행
  - 그 다음 componentDidUpdate 실행
- unmounting
  - component가 죽을 때
  - componentWillUnmount 실행
    - 새로고침하면 로그가 사라지기 때문에 콘솔의 메뉴에서 Preserve log 체크 후 실험





### #3.3 Planning the Movie Component

- 





## #4 Making the Movie App



### #4.0 Fetching Movies from API

- AXIOS 사용할 것임

  ```
  npm install axios
  ```

- 영화 추천은 yts 사이트의 api 이용

  ```
  https://yts-proxy.now.sh/list_movies.json
  ```

- axios 통신의 경우 시간이 조금 걸릴 수 있으므로 async, await을 통해서 비동기 처리를 해준다.



### #4.1 Rendering the Movies

- axios.get의 응답으로 받은 것의 data 만 필요하므로 data프로퍼티에 접근한다
- 영화 제목을 출력하는 Movie.js 를 만들고 Movie로 export한다.
- app.js에서 import해서 map을 통해서 출력한다.





### #4.2 Styling the Movies

- style 주는 방법은 두가지 있음
  - 태그 안에 style={{}}을 이용해서 inline으로 넣기
  - css파일 생성해서 정의하고 import하기



### #4.3 Adding Genres

- html 태그 속 class가 react의 class와 햇깔리므로 className사용





### #4.4 Styles Timelapse





### #4.5 Cutting the summary

- slice(a,b) -> a~b index를 자른다.





## #5  Conclusion



### #5.0 Deploying to Github Pages

- 내 페이지를 깃헙 페이지 도메인에 나타나게 해줌 (무료)

  ```
  npm i gh-pages
  ```

- package.json에 homepage 프로퍼티 추가

  ```
  "homepage" : "https://kevinkim-dev.github.io/movie_app"
  ```

- package.json에 script에 build 및 deploy 과정 추가

  ```
    "scripts": {
      "start": "react-scripts start",
      "build": "react-scripts build",
      "deploy": "gh-pages -d build",
      "predeploy": "npm run build"
    },
  ```

- 그리고 npm run deploy 실행
  - predeploy도 자동으로 실행







### #5.1 Are We Done?

- state를 갖기 위해 class component를 무조건 가질 필요는 없음
- react hook이란 것이 생김
  - react hook 무료강의 들어보기
- react 유료강의 들어보기





## #6 Routing Bouns



### #6.0 Getting ready for the Router

- react router dom 을 install

  ```
  npm install react-router-dom
  ```

  



### #6.1 Building the Router

```
import { HashRouter, Route } from "react-router-dom"
```

- react router는 겹치면 모두 랜더링함
- 한 페이지에 컴포넌트가 두개 이상일 수도 있다.
  - exact={true} 추가해서 해결가능 => 이거랑 똑같지않으면 render 하지 않음





### #6.2 Building the Navigation

- Navigation 사용 시 <a> 태그에 href 사용 X -> 새로고침됨
  - 대신 Link 사용



### #6.3 Sharing Props Between Routes

- 다른 class나 function의 props를 전달할 수 있다.
- 해당 컴포넌트의 Link에서 중괄호 두개 열고 state까지 전달할 내용 지정





### #6.4 Redirecting

- props에 history가 있음
- 이 history에 push하면서 원하는 위치로 리다이랙션 시킬 수 있음
- id 를 props로 써서 rest하게 짤 수 있음