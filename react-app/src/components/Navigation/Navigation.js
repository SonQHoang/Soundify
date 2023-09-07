// This will only appear on the sign-in page

import React from 'react';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';

function Navigation({ isLoaded }) {
	const sessionUser = useSelector(state => state.session.user);

	return (
		<>
				<div className='navigation-bar'>
					<div className="upcoming-features">
						<h2>Upcoming Features!</h2>
					</div>
					{isLoaded && (
						<div className='sign-up-buttons'>
							<ProfileButton user={sessionUser} />
						</div>
					)}
				</div>
		</>
	);
}

export default Navigation;