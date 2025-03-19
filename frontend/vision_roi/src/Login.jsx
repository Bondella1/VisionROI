import "./Login.css";
const Login = () => {

    return (
      <div className="login">
        <h2>Login</h2>
        <label>Email</label>
        <input type="email" placeholder="Enter email"/>

        <label>Password</label>
        <input type="password" placeholder="Enter password"/>

        <button>Login</button>

      </div>
    );
  };
  
  export default Login;