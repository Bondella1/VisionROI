const NavBar = ({ onLoginClick, isAuthenticated, username, onLogout }) => {

  return (
    <div className="navbar">
      <h1 className="navbar-title">Vision ROI</h1>
      <div className="navbar-links">
        <a href="/">Home</a>
        {isAuthenticated ? (
          <div className="user-info">
              <span>Welcome, {username}</span>
              <button onClick={onLogout} className="logout-button">Logout</button>
          </div>
        ) : (
          <button className="login-button" onClick={onLoginClick}>Login or Create Account</button>
        )}
      </div>
    </div>
  );
};

export default NavBar;