import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    } else {
      closeModal()
    }
  };

  const handleDemoLogin = async () => {
    // Simulate input for demo login (replace with your demo credentials)
    const demoEmail = "demo@aa.io";
    const demoPassword = "password";

    // Set email and password state with demo credentials
    setEmail(demoEmail);
    setPassword(demoPassword);

    // Dispatch the login action directly
    const data = await dispatch(login(demoEmail, demoPassword));
    if (data) {
      setErrors(data);
    } else {
      closeModal();
    }
  };


  return (
    <>
      <div className="log-in-container">
        <div>
        <h1>Log In</h1>
        </div>
        <form className="login-form-container" onSubmit={handleSubmit}>
          <ul>
            {errors.map((error, idx) => (
              <li key={idx}>{error}</li>
            ))}
          </ul>
          <label>
            <div className="log-in-label">
              Email
            </div>
            <input
              type="text"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </label>
          <label>
            <div className="log-in-label">
              Password
            </div>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </label>
          <div>
            <button className="login-submit-button" type="submit">Log In</button>
          </div>
          <div>
            <button className="login-submit-button" type="button" onClick={handleDemoLogin}>Demo Log In</button>
          </div>
        </form>
      </div>
    </>
  );
}

export default LoginFormModal;
