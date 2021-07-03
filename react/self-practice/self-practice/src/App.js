import React, {useState} from 'react';
import Reviews from './components/Review'
import Navbar from './components/Navbar'
import './App.css';

function App() {

  var [titles, titles_change] = useState('');
  var [text, text_change] = useState('');
  // var [titles, titles_change] = useState(['남자 코트 추천', '강남 우동 맛집', '홍대 데이트 추천']);

  function handle_change(text){
    return(
      text_change(text)
    )
  }

  return (
    <div className="App">
      <Reviews titles={titles}/>
      <input onChange={(e)=>{handle_change(e.target.value)}}></input>
      <button onClick={()=>{titles_change(text)}}>글 추가</button>
    </div>
  );
}







export default App;
