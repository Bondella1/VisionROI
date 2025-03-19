import { loginRequest } from "./authConfig";
import "./Login.css";
import { useMsal, useIsAuthenticated } from "@azure/msal-react";

const Login = () => {
  const { instance } = useMsal();
  const isAuthenticated = useIsAuthenticated();
  
  const handleLogin = () => {
    console.log("Login button clicked");
    instance.loginPopup(loginRequest).catch((error) => {
      console.error("Login failed: ", error);
    });
  };

  const handleLogout = () => {
    console.log("Logout button clicked");
    instance.logoutPopup().catch((error) => {
      console.error("Logout failed", error);
    });
  };

    return (
      <div className="login">
        <h2>Login</h2>
        {!isAuthenticated ? (
        <button onClick={handleLogin}>Login with Microsoft</button>
      ) : (
        <button onClick={handleLogout}>Logout</button>
      )}
      </div>
    );
  };
  
  export default Login;