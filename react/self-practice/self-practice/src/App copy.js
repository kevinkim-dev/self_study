// /* eslint-disable */ -> lint 비활성화

import React, {useState} from 'react';
import './App.css';

function App() {

  // a에는 '남자 코트 추천', b에는 state를 변경하는 함수
  // state사용하면 변경 시 자동 재랜더링(새로고침 없이)
  var [title, title_change] = useState(['남자 코트 추천', '강남 우동 맛집', '홍대 데이트 추천']);
  var [likes, likes_change] = useState(0);

  // function change_title(){
  //   //state 절대 직접 수정하지 말 것. copy본 만들어서 수정할 것
  //   //es6 문법 [...<array>] -> deepcopy
  //   var newArray = [...title];
  //   newArray[0] = '여자 코트 추천';
  //   title_change(newArray);
  // }

  // function arrange_title(){
  //   var newArray = [...title];
  //   newArray = newArray.sort()
  //   title_change(newArray)
  // }


  return (
    <div className="App">
      <div className="navbar">
        <div>개발 Blog</div>
      </div>
      {/* <button onClick={()=>{ change_title() }}>버튼</button> */}
      {/* <button onClick={()=>{ arrange_title() }}>버튼2</button> */}
      <div className="list">
        <h4>{title[0]}</h4>
        <p>2021.07.03</p>
        <hr></hr>
      </div>
      <div className="list">
        <h4>{title[1]}<span onClick={()=>{ likes_change(likes + 1) }}> 👍 </span> {likes} </h4>
        <p>2021.07.03</p>
        <hr></hr>
      </div>
      <div className="list">
        <h4>{title[2]}</h4>
        <p>2021.07.03</p>
        <hr></hr>
      </div>
      <Modal />
      
    </div>
  );
}

function Modal(){
  return (
    // <></>로 의미없는 div 줄일 수 있음
    <>
    <div className="modal">
      <h2>제목</h2>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
    </>
  )
}

export default App;
