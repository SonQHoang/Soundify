import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation/Navigation";
import Player from "./components/AudioBar/audiobar";
import LandingPage from "./components/LandingPage/landingpage";
import Songs from "./components/Songs/songs";
import CreatePlaylist from "./components/CreatePlayList.js/CreatePlaylist";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <div className="app-container">
          <main className="content">
        <Switch>
          <Route path="/login" >
            <LoginFormPage />
          </Route>
          <Route path="/playlist/new">
            <CreatePlaylist/>
          </Route>
          <Route path="/signup">
            <SignupFormPage />
          </Route>
          <Route path="/">
            <LandingPage/>
          </Route>
          <Route>
            <Songs/>
          </Route>
        </Switch>
        </main>
        </div>
      )}
      <Player/>
    </>
  );
}

export default App;
