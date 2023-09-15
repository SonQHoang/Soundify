import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { signUp } from "../../store/session";
import "./SignupForm.css";
import { useHistory } from "react-router-dom"

function SignupFormModal() {
	const history = useHistory()
	const dispatch = useDispatch();
	const [email, setEmail] = useState("");
	const [username, setUsername] = useState("");
	const [firstname, setFirstname] = useState("");
	const [lastname, setLastname] = useState("");
	const [bio, setBio] = useState("");
	const [password, setPassword] = useState("");
	const [confirmPassword, setConfirmPassword] = useState("");
	const [errors, setErrors] = useState([]);
	const { closeModal } = useModal();

	const handleSubmit = async (e) => {
		e.preventDefault();
		if (password === confirmPassword) {
			const data = await dispatch(signUp(username, email, password, firstname, lastname, bio));
			if (data) {
				setErrors(data);
			} else {
				closeModal();
			}
			history.push('/landing-page')
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
						What's your first name?
					</div>
					<input
						classname="sign-up-input"

						type="text"
						value={firstname}
						onChange={(e) => setFirstname(e.target.value)}
						placeholder="Enter your email."
						required
					/>
				</label>
				<label>
					<div className="sign-up-labels">
						What's your last name?
					</div>
					<input
						classname="sign-up-input"

						type="text"
						value={lastname}
						onChange={(e) => setLastname(e.target.value)}
						placeholder="Enter your email."
						required
					/>
				</label>
				<label>
					<div className="sign-up-labels">
						Would you like to give a brief bio??
					</div>
					<input
						classname="sign-up-input"

						type="text"
						value={bio}
						onChange={(e) => setBio(e.target.value)}
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