import React from 'react';
import styled from "styled-components";
import { Link } from "react-router-dom"

const Navbar = () => {
  const Nav = styled.nav`
    display: flex;
    align-items: center;
    border-bottom: solid 1px black;
    background-color: #eee;
    height: 50px;
    text-align: center;
  `;

  return (
    <div>
      <Nav>
        <Link 
          to="/" 
          style={{ 
            textDecoration: 'none',
            color: 'black',
            fontSize: 20,
            paddingBottom: '4px',
            marginLeft: '20px'
          }}
        >
          Home
        </Link>
        <Link 
          to="/dinojump" 
          style={{
            textDecoration: 'none',
            color: 'black',
            fontSize: 20,
            paddingBottom: '4px',
            marginLeft: '20px'
          }}
        >
          Dinojump
        </Link>
      </Nav>
    </div>
  );
};


export default Navbar;