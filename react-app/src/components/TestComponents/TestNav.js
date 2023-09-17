import React, { useContext } from 'react'
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
          <a>Github</a>
          <a>LinkedIn</a>
        </div>
        <div className="logout-container">
          {user ? (
          <button onClick={handleDropDown}>Icon</button>
          ) : (
            <>
              {showLoginModal && <LoginFormModal />}
              {showSignUpModal && <SignupFormModal />}
            </>
          )}
          {dropDownMenu && (
            <div>
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