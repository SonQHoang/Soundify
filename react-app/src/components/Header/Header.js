// import { useSelector } from 'react-redux';
// // import ProfileButton from '../Navigation/ProfileButton'
// import LandingPage from '../LandingPage/landingpage';
// import Navigation from '../Navigation/Navigation'
import './Header.css'

const Header = (isLoaded) => {
    // const sessionUser = useSelector(state => state.session.user);

    return (
        <div className="header-container">
            {/* <Navigation/> */}
            {isLoaded && (
						<div className='sign-up-buttons'>
							{/* <LandingPage user={sessionUser} /> */}
						</div>
					)}
        </div>
    )
}

export default Header