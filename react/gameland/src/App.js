import React from 'react';
import Navbar from './screen/Navbar';
import Home from './screen/Home';
import DinojumpScreen from './screen/DinojumpScreen';
import { Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div>
      <Navbar />
      <div style={{ padding: '50px' }}>
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/dinojump" element={<DinojumpScreen />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
