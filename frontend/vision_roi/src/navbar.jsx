const NavBar = ({ onLoginClick }) => {

  return (
    <div className="navbar">
      <h1 className="navbar-title">Vision ROI</h1>
      <div className="navbar-links">
        <a href="/">Home</a>
        <button className="login-button" onClick={onLoginClick}>Login or Create Account</button>
      </div>
    </div>
  );
};

export default NavBar