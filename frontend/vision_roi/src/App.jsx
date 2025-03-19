import { useState } from 'react'
import './App.css';
import Home from './home';
import NavBar from './navbar';
import Login from './Login';

const App = () => {

  const [showLogin, setShowLogin] = useState(false);

  return (
    <div className="App">
      <NavBar onLoginClick={() => setShowLogin(true)} />
      <div className='content'>
        {showLogin ? <Login /> : <Home />} 
      </div>
    </div>
    
  )
}

export default App