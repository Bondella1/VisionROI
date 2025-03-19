import { loginRequest } from "./authConfig";
import "./Login.css";
import { useMsal } from "@azure/msal-react";

const Login = () => {
  const { instance } = useMsal();
  
  const handleLogin = () => {
    console.log("Login button clicked");
    console.log("Instance:", instance);
    console.log("Login Request:", loginRequest);

    if (!instance) {
      console.error("MSAL instance is undefined");
      return;
    }
  
    if (!loginRequest) {
      console.error("Login request is undefined");
      return;
    }

    instance.loginPopup(loginRequest).catch((error) => {
      console.error("Login failed: ", error);
    });
  };

    return (
      <div className="login">
        <h2>Login</h2>
        <button onClick={handleLogin}>Login with Microsoft</button>

      </div>
    );
  };
  
  export default Login;