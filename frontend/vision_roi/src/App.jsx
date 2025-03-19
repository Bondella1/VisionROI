import { useState } from 'react'
import './App.css';
import Home from './home';
import NavBar from './navbar';
import Login from './Login';

// wrap app with MsalProvider
import {MsalProvider} from "@azure/msal-react";
import { PublicClientApplication } from '@azure/msal-browser';
import { msalConfig } from './authConfig';

const App = () => {

  const [showLogin, setShowLogin] = useState(false);
  const msalInstance = new PublicClientApplication(msalConfig);


  return (
    
    <MsalProvider instance={msalInstance}>
      <div className="App">
        <NavBar onLoginClick={() => setShowLogin(true)} />
        <div className='content'>
          {showLogin ? <Login /> : <Home />} 
        </div>
      </div>
    </MsalProvider>
    
  );
}

export default App