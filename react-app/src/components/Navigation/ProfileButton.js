import React from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";
// import OpenModalButton from "../OpenModalButton";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import './ProfileButton.css'

function ProfileButton({ user, showLoginModal, showSignUpModal }) {
  const dispatch = useDispatch();

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
  };

  return (
    <div className="login-signin-button">
        {user ? (
          <div>
            <div>{user.username}</div>
            <div>{user.email}</div>
              <button onClick={handleLogout}>Log Out</button>
          </div>
        ) : (
          <div>
                      {showLoginModal && <LoginFormModal />}
                      {showSignUpModal && <SignupFormModal />}
          </div>
        )}
    </div>
  );
}

export default ProfileButton;
