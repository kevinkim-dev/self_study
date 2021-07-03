import React, { useState } from 'react'
import Modal from './Modal'

function Reviews(props){

  var titles = props.titles

  return (
    <div>
      <Review title={titles}/>
      {/* <Review title={titles[0]}/>
      <Review title={titles[1]}/>
      <Review title={titles[2]}/> */}
    </div>
  )
}

function Review(props){

  var [likes, likes_change] = useState(0);

  return (
    <div className="list">
      <h3>{props.title} <button onClick={() => {likes_change(likes+1)}}>좋아요</button> {likes} </h3>
      <p>2021.07.03</p>
      <Modal title={props.title}/>
      <hr></hr>
    </div>
  )
}

export default Reviews