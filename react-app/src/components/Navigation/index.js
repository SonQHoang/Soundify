import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';

function Navigation({ isLoaded }) {
	const sessionUser = useSelector(state => state.session.user);

	return (
		<div className="main-page-container">
			<div className="side-bar-container">
				<div className='home-container'>
					<NavLink exact to="/">
						Home
					</NavLink>
				</div>
				<div className="playlists-container">
					<h1>Playlists</h1>
				</div>
				<div className="library-container">
					<h1>Your Library</h1>
				</div>
			</div>
			<div className="main-content-container">
				<div className='nav-bar'>
					<div className="upcoming-features">
						<h2>Upcoming Features!</h2>
					</div>
					{isLoaded && (
						<div>
							<ProfileButton user={sessionUser} />
						</div>
					)}
				</div>
				<div className="soundify-playlists">
					<h1>Soundify Playlists</h1>
				</div>
				<div className="focus">
					<h1>Focus</h1>
				</div>
			</div>

		</div>
	);
}

export default Navigation;