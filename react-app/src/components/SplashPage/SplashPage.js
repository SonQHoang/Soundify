import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import { logout } from "../../store/session";
import { useDispatch } from 'react-redux';
import { useModal } from '../../context/Modal';

import "./SplashPage.css"

const SplashPage = () => {
    const dispatch = useDispatch()
    const { setModalContent, setOnModalClose } = useModal();

    const openLoginModal = () => {
        setModalContent(<LoginFormModal />);
        setOnModalClose(() => {
        });
    };


    const openSignUpModal = () => {
        setModalContent(<SignupFormModal />);
        setOnModalClose(() => {
        });
    };


    const handleLogout = (e) => {
        e.preventDefault();
        dispatch(logout());
    };

    return (
        <>
            <header className="splash-page-header">
                <div className="splash-page-logo-container">
                    <img className="splash-page-soundify-logo" src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1694681368/SOUNDIFY_9_znffp4.png" alt="Soundify Logo" />
                </div>
                <div>
                    <button className="upcoming-features">
                        {/* Upcoming Features */}
                    </button>

                    <button className="sign-up-button" onClick={openSignUpModal}>Sign Up</button>
                    <button className="log-in-button" onClick={openLoginModal}>Log In</button>
                </div>
            </header>
            <div className="splash-page-container">
                <h1>Music for everyone.</h1>
                <button className="soundify-button" onClick={openLoginModal}>Welcome to Soundify</button>
            </div>
        </>
    )
}


export default SplashPage