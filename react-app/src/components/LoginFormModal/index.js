import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { useHistory } from "react-router-dom"
import { userAccessDemoData } from "../../store/session";
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
  const history = useHistory()
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
      history.push('/landing-page')
    }
  };

  const handleDemoLogin = async () => {
    const demoEmail = "demo@aa.io";
    const demoPassword = "password";

    setEmail(demoEmail);
    setPassword(demoPassword);

    const data = await dispatch(login(demoEmail, demoPassword));
    if (data) {
      setErrors(data);
    } else {
      closeModal();
      history.push('/landing-page')
    }
  };


  return (
    <>
      <div className="log-in-container">
        <div>
          <h1>Log In</h1>
        </div>
        <form className="login-form-container" onSubmit={handleSubmit}>
          <div className="errors-list">
            {Object.values(errors).map((error, idx) => (
              <div key={idx}>{error}</div>
            ))}
          </div>
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
