import React from 'react';
import Dinojump from '../component/dinojump/Dinojump';

const DinojumpScreen = () => {
  return (
    <div 
      style={{ 
        display: 'flex', 
        flexDirection: 'column',
        alignItems: 'center'
      }}
    >
      <h2>Dinojump</h2>
      <div 
        style={{ 
          margin: '20px',
          border: 'solid 1px black',
          width: '80vw',
          height: '60vw'
        }}>
        <Dinojump />
      </div>
    </div>
  );
};

export default DinojumpScreen;