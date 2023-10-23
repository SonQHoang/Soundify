import React from 'react'
import { SongContext } from '../../context/SongContext';
import { AuthContext } from '../../context/AuthContext';
import { useState } from 'react'
import { logout as logoutAction } from "../../store/session";
import { useContext } from 'react';
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from 'react-router-dom'
import LoginFormModal from '../LoginFormModal';
import SignupFormModal from '../SignupFormModal';
import './TestNav.css'


const TestNav = () => {
  const { logout } = useContext(AuthContext)
  const { pause } = useContext(SongContext);

  const dispatch = useDispatch();
  const history = useHistory()
  const [dropDownMenu, setDropDownMenu] = useState(false)
  const [hoverInfoVisible, setHoverInfoVisible] = useState(true)

  const user = useSelector((state) => state.session.user);
  const showLoginModal = useSelector((state) => state.showLoginModal);
  const showSignUpModal = useSelector((state) => state.showSignUpModal);

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logoutAction());
    pause();
    logout()
    history.push('/');
  };

  const handleDropDown = () => {
    setDropDownMenu(!dropDownMenu)
    setHoverInfoVisible(dropDownMenu)
  }

  const handleFeatureClick = () => {
    alert("This feature will be added in the future. Check back again soon!")
  }

  return (
    <>
      <div className="nav-component-nav-container">
        <div className="about-me-links">
        <a rel="noopener noreferrer" href='https://github.com/SonQHoang' id="github-link">
                                <div className='about-me-github-splash-page'>
                                </div>
                            </a>
                            <a rel="noopener noreferrer" href='https://linkedin.com/in/sean-hoang' id="linkedin-link">
                                <div className='about-me-linkedin-splash-page'>
                                </div>
                            </a>
        </div>
        <div className="logout-container">
          {user ? (
            <div className="profile-info-container">
              <button className="profile-icon-container" onClick={handleDropDown}>
                <img src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1695022422/user-4-16_jlmfwj.png" alt="icon" className="profile-icon" />
              </button>
              {hoverInfoVisible && !dropDownMenu && (
                <div className="hover-info">
                  <div>{user.username}</div>
                  <div>{user.email}</div>
                </div>
              )}
            </div>
          ) : (
            <>
              {showLoginModal && <LoginFormModal />}
              {showSignUpModal && <SignupFormModal />}
            </>
          )}
          {dropDownMenu && (
            <div className="drop-down-profile-menu">
              <button onClick={handleFeatureClick} className="account-button" >Account</button>
              <button onClick={handleFeatureClick} className="settings-button" >Settings</button>
              <button className="log-out-button" onClick={handleLogout}>LogOut</button>
            </div>

          )}
        </div>
      </div>
    </>
  )
}

export default TestNav