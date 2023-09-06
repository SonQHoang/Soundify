import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	return (
		<div className="nav-bar-container">
			<div className='nav-bar-left'>
				<NavLink exact to="/">
					Home
				</NavLink>
			</div>
			<div className='nav-bar-right'>

			{isLoaded && (
				<div>
					<ProfileButton user={sessionUser} />
				</div>
			)}
		</div>
			</div>
	);
}

export default Navigation;