import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import { Redirect } from "react-router-dom";
import { signUp } from "../../store/session";
import "./SignupForm.css";

function SignupFormModal() {
	const dispatch = useDispatch();
	const sessionUser = useSelector((state) => state.session.user);
	const [email, setEmail] = useState("");
	const [username, setUsername] = useState("");
	const [firstname, setFirstname] = useState("");
	const [lastname, setLastname] = useState("");
	const [password, setPassword] = useState("");
	const [confirmPassword, setConfirmPassword] = useState("");
	const [errors, setErrors] = useState([]);
	const { closeModal } = useModal();

	if (sessionUser) return <Redirect to="/" />;

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
		<div className='sign-up-form-container'>
			<div className="title-container">
				<h1>Sign Up to start listening!</h1>
			</div>
			<form className="form-container" onSubmit={handleSubmit}>
				{/* <ul>
					{errors.map((error, idx) => (
						<li key={idx}>{error}</li>
					))}
				</ul> */}
				<label>
					<div className="sign-up-labels">
						What's your email?
					</div>
					<div className="error-message">{errors.email}</div>
					<div>
					<input
						className="sign-up-input"
						type="text"
						value={email}
						onChange={(e) => setEmail(e.target.value)}
						placeholder="Enter your email."
						required
					/>
					</div>
				</label>
				<label>
					<div className="sign-up-labels">
						What's your first name?
					</div>
					<div className="error-message">{errors.firstname}</div>
					<div>
					<input
						className="sign-up-input"

						type="text"
						value={firstname}
						onChange={(e) => setFirstname(e.target.value)}
						placeholder="Enter your first name."
						required
					/>	
					</div>
				</label>
				<label>
					<div className="sign-up-labels">
						What's your last name?
					</div>
					<div className="error-message">{errors.lastname}</div>
					<div>
					<input
						className="sign-up-input"

						type="text"
						value={lastname}
						onChange={(e) => setLastname(e.target.value)}
						placeholder="Enter your last name."
						required
					/>

					</div>
				</label>
				<label>
					<div className="sign-up-labels">
						What should we call you?
					</div>
					<div className="error-message">{errors.username}</div>
					<div>
					<input
						className="sign-up-input"

						type="text"
						value={username}
						placeholder="Enter a user name"
						onChange={(e) => setUsername(e.target.value)}
						required
					/>
					</div>
				</label>
				<label className="sign-up-labels">
					<div>
						Create a password
					</div>
					<div className="error-message">{errors.password}</div>
					<div>

					<input
						className="sign-up-input"
						type="password"
						value={password}
						placeholder="Create a password."
						onChange={(e) => setPassword(e.target.value)}
						required
					/>
					</div>
				</label>
				<label className="sign-up-labels">
					<div>
						Confirm Password
					</div>
					<div className="error-message">{errors.confirmPassword}</div>
					<div>
					<input
						className="sign-up-input"

						type="password"
						value={confirmPassword}
						placeholder="Please confirm your password"
						onChange={(e) => setConfirmPassword(e.target.value)}
						required
					/>
					</div>
				</label>
				<div>
					<button className="sign-up-sign-up-button" type="submit">Sign Up</button>
				</div>
			</form>
		</div>
	);
}

export default SignupFormModal;