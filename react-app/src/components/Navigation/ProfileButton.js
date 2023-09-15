import React, { useState, useEffect, useRef } from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";
import OpenModalButton from "../OpenModalButton";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import './ProfileButton.css'

function ProfileButton({ user, showLoginModal, showSignUpModal }) {
  const dispatch = useDispatch();
  // const [showMenu, setShowMenu] = useState(false);
  // const ulRef = useRef();

  // const openMenu = () => {
  //   if (showMenu) return;
  //   setShowMenu(true);
  // };

  // useEffect(() => {
  //   if (!showMenu) return;

  //   const closeMenu = (e) => {
  //     if (!ulRef.current.contains(e.target)) {
  //       setShowMenu(false);
  //     }
  //   };

  //   document.addEventListener("click", closeMenu);

  //   return () => document.removeEventListener("click", closeMenu);
  // }, [showMenu]);

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
  };

  // const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");
  // const closeMenu = () => setShowMenu(false);

  return (
    <div className="login-signin-button">
        {user ? (
          <>
            <div>{user.username}</div>
            <div>{user.email}</div>
              <button onClick={handleLogout}>Log Out</button>
          </>
        ) : (
          <>
                      {showLoginModal && <LoginFormModal />}
                      {showSignUpModal && <SignupFormModal />}

            {/* <OpenModalButton
              buttonText="Log In"
              onItemClick={closeMenu}
              modalComponent={<LoginFormModal />}
              className="log-in-modal-button"
            />

            <OpenModalButton
              buttonText="Sign Up"
              onItemClick={closeMenu}
              modalComponent={<SignupFormModal />}
              className='sign-in-modal-button'
            /> */}
          </>
        )}
    </div>
  );
}

export default ProfileButton;
