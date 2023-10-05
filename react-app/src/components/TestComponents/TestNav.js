import React from 'react'
import { useState } from 'react'
import { logout } from "../../store/session";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from 'react-router-dom'
import LoginFormModal from '../LoginFormModal';
import SignupFormModal from '../SignupFormModal';
import './TestNav.css'

const TestNav = () => {
  const dispatch = useDispatch();
  const history = useHistory()
  const [dropDownMenu, setDropDownMenu] = useState(false)

  const user = useSelector((state) => state.session.user);
  const showLoginModal = useSelector((state) => state.showLoginModal);
  const showSignUpModal = useSelector((state) => state.showSignUpModal);

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
    history.push('/')
  };

  const handleDropDown = () => {
    setDropDownMenu(!dropDownMenu)
  }

  return (
    <>
      <div className="nav-component-nav-container">
        <div className="about-me-links">
          <a rel="noopener noreferrer" href='https://github.com/SonQHoang' id="github-link">
            <div className='about-me-github'>
            </div>
          </a>
          <a rel="noopener noreferrer" href='https://linkedin.com/in/sean-hoang' id="linkedin-link">
            <div className='about-me-linkedin'>
            </div>
          </a>
        </div>
        <div className="logout-container">
          {user ? (
            <button className="profile-icon-container" onClick={handleDropDown}>
              <img src="https://res.cloudinary.com/dgxpqnbwn/image/upload/v1695022422/user-4-16_jlmfwj.png" alt="icon" className="profile-icon" />
            </button>
          ) : (
            <>
              {showLoginModal && <LoginFormModal />}
              {showSignUpModal && <SignupFormModal />}
            </>
          )}
          {dropDownMenu && (
            <div className="drop-down-profile-menu">
              <div>{user.username}</div>
              <div>{user.email}</div>
              <button onClick={handleLogout}>LogOut</button>
            </div>
          )}
        </div>
      </div>
    </>
  )
}

export default TestNav