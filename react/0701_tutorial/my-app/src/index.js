import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';

// #1. JSX 소개
// function printName(user) {
//   return user.firstName + ' ' + user.lastName
// }

// const user = {
//   firstName: '승현',
//   lastName: '김'
// }

// const element = <h1>{printName(user)}</h1>

// const element2 = React.createElement(
//   'h1',
//   {className: 'greeting'},
//   'Hello, world!'
// );

// ReactDOM.render(
//   element,
//   document.getElementById('root')
// );


// #2. 엘리먼트 렌더링
function tick() {
  const element = (
    <div>
      <h1>Hello, World!</h1>
      <h2>It is {new Date().toLocaleTimeString()}.</h2>
    </div>
  );
  ReactDOM.render(
    element,
    document.getElementById('root')
  );
}

setInterval(tick, 1000);

// #3. Component와 Props



// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
