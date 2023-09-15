import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { signUp } from "../../store/session";
import "./SignupForm.css";

function SignupFormModal() {
	const dispatch = useDispatch();
	const [email, setEmail] = useState("");
	const [username, setUsername] = useState("");
	const [password, setPassword] = useState("");
	const [confirmPassword, setConfirmPassword] = useState("");
	const [errors, setErrors] = useState([]);
	const { closeModal } = useModal();

	const handleSubmit = async (e) => {
		e.preventDefault();
		if (password === confirmPassword) {
			const data = await dispatch(signUp(username, email, password));
			if (data) {
				setErrors(data);
			} else {
				closeModal();
			}
		} else {
			setErrors([
				"Confirm Password field must be the same as the Password field",
			]);
		}
	};

	return (
		<div className='sign-up-form-container'>
			<div className="title-container">
				<h1>Sign Up for free to start listening.</h1>
			</div>
			<form className="form-container" onSubmit={handleSubmit}>
				<ul>
					{errors.map((error, idx) => (
						<li key={idx}>{error}</li>
					))}
				</ul>
				<label>
					<div className="sign-up-labels">
						What's your email?
					</div>
					<input
						classname="sign-up-input"

						type="text"
						value={email}
						onChange={(e) => setEmail(e.target.value)}
						placeholder="Enter your email."
						required
					/>
				</label>
				<label>
					<div className="sign-up-labels">
						What should we call you?
					</div>
					<input
						classname="sign-up-input"

						type="text"
						value={username}
						placeholder="Enter a profile name."
						onChange={(e) => setUsername(e.target.value)}
						required
					/>
				</label>
				<label className="sign-up-labels">
					<div>
						Create a password
					</div>
					<input
						classname="sign-up-input"
						type="password"
						value={password}
						placerholder="Create a password."
						onChange={(e) => setPassword(e.target.value)}
						required
					/>
				</label>
				<label className="sign-up-labels">
					<div>
						Confirm Password
					</div>
					<input
						classname="sign-up-input"

						type="password"
						value={confirmPassword}
						onChange={(e) => setConfirmPassword(e.target.value)}
						required
					/>
				</label>
				<div>
					<button className="sign-up-sign-up-button" type="submit">Sign Up</button>
				</div>
			</form>
		</div>
	);
}

export default SignupFormModal;