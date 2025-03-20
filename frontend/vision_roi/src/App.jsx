import { useState } from 'react'
import './App.css';
import './Login.css';
import './navbar.css'
import Home from './home';
import NavBar from './navbar';
import Login from './Login';
import ProjectData from './ProjectData';

// wrap app with MsalProvider
import {MsalProvider, useIsAuthenticated, useAccount} from "@azure/msal-react";
import { PublicClientApplication } from '@azure/msal-browser';
import { msalConfig } from './authConfig';

const msalInstance = new PublicClientApplication(msalConfig);

const AppContent = () => {
  const [showLogin, setShowLogin] = useState(false);
  const isAuthenticated = useIsAuthenticated();
  const account = useAccount();

  return (
    <div className="App">
        
        <NavBar 
        onLoginClick={() => setShowLogin(true)} 
        isAuthenticated={isAuthenticated} 
        username={account?.idTokenClaims?.preferred_username || account?.name} 
        onLogout={() => msalInstance.logoutPopup()}
        />
        
        <div className='content'>
          {isAuthenticated ? <ProjectData /> : showLogin ? <Login /> : <Home onLoginClick= {() => setShowLogin(true)}/>}
        </div>
        
    </div>
  );
};

const App = () => {
  return (
    <MsalProvider instance={msalInstance}>
      <AppContent />
    </MsalProvider>
    
  );
};

export default App;