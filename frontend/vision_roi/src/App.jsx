import { useState } from 'react'
import './App.css';
import Home from './home';
import NavBar from './navbar';

const App = () => {

  return (
    <div className="App">
      <NavBar />
      <div className='content'>
        <Home />
      </div>
    </div>
    
  )
}

export default App