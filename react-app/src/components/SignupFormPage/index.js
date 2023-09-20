import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { signUp } from "../../store/session";
import './SignupForm.css';

function SignupFormPage() {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [firstname, setFirstname] = useState("");
  const [lastname, setLastname] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errors, setErrors] = useState({});

  if (sessionUser) return <Redirect to="/landinge-page" />; 


  const isValidEmail = (email) => {
		return email.includes("@")
	}

	const handleSubmit = async (e) => {
		e.preventDefault();

		const newErrors = {};


		if (!username) {
			newErrors.username = "Username is required";
		} else if (username.length < 5) {
			newErrors.username = "Please provide a username that is at least 5 characters long."
		} else if (username.length >= 15) {
			newErrors.username = "Please provide a username that is less than 15 characters long."
		}

		if (!firstname) {
			newErrors.firstname = "First name is required";
		}

		if (!lastname) {
			newErrors.lastname = "Last name is required";
		}

		if (!email) {
			newErrors.email = "Email is required";
		} else if (!isValidEmail(email)) {
			newErrors.email = "Please provide a valid email address."
		}


		if (!password) {
			newErrors.password = "Password is required";
		} else if (password.length < 5) {
			newErrors.password = "Please provide a password that is at least 5 characters long.";
		}

		if(password !== confirmPassword) {
			newErrors.confirmPassword = "Confirmed password must patch password"
		}

		if (Object.keys(newErrors).length === 0) {
			const data = await dispatch(signUp(username, email, password, firstname, lastname));
			if (data) {
				setErrors(data);
			}
		} else {
			setErrors(newErrors);
		}
	};

  return (
    <>
      <h1>Sign Up</h1>
      <form onSubmit={handleSubmit} >
        <ul>
          {errors.map((error, idx) => <li key={idx}>{error}</li>)}
        </ul>
        <label>
          Email
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        <label>
          First Name
          <input
            type="text"
            value={firstname}
            onChange={(e) => setFirstname(e.target.value)}
            required
          />
        </label>
        <label>
          Last Name
          <input
            type="text"
            value={lastname}
            onChange={(e) => setLastname(e.target.value)}
            required
          />
        </label>
        <label>
          Username
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </label>
        <label>
          Password
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        <label>
          Confirm Password
          <input
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
          />
        </label>
        <button type="submit">Sign Up</button>
      </form>
    </>
  );
}

export default SignupFormPage;
