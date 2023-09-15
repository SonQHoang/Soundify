import React from 'react'
import Sidebar from '../Sidebar/Sidebar'
import { logout } from "../../store/session";
// import ProfileButton from '../Navigation/ProfileButton';
// import Header from '../Header/Header'
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';
import { useSelector } from 'react-redux';
import { useDispatch } from 'react-redux';
import LoginFormModal from '../LoginFormModal';
import SignupFormModal from '../SignupFormModal';
import UserPlaylist from '../UserPlaylist/UserPlaylist'
import Footer from '../Footer/Footer'
import "./landingpage.css"

const LandingPage = () => {
    const dispatch = useDispatch()
    const history = useHistory()
    const user = useSelector((state) => state.session.user);
    // console.log('user======>', user)
    const showLoginModal = useSelector((state) => state.showLoginModal);
    const showSignUpModal = useSelector((state) => state.showSignUpModal);

    const handleLogout = (e) => {
        e.preventDefault();
        dispatch(logout());
        history.push('/')
    };

    return (
        <>
            <div className="landing-page-container">
                <Sidebar />
                <div className="main-content-container">
                    <div className="soundify-playlists-container">
                        <div className="landing-h1-container">
                        <h1 className="landing-h1">Soundify Playlists</h1>
                        {user ? (
                            <div>
                                <div>{user.username}</div>
                                <div>{user.email}</div>
                                <button onClick={handleLogout}>LogOut</button>
                            </div>
                        ) : (
                            <div>
                                {showLoginModal && <LoginFormModal />}
                                {showSignUpModal && <SignupFormModal />}
                            </div>
                        )}
                        </div>
                        <div className="landing-page-playlists-container">
                            <UserPlaylist />
                        </div>
                    </div>
                    <div className="focus-container">
                        <h1 className="landing-h1">Focus</h1>
                    </div>
                    <Footer />
                </div>
            </div>
        </>
    )
}

export default LandingPage