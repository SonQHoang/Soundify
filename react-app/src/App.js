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
import CreatePlaylist from "./components/CreatePlaylist/CreatePlaylist"
import Playlist from "./components/Playlists/Playlists";
import PlaylistDetails from "./components/PlaylistDetails/PlaylistDetails";

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
          <Route path="/playlist/all">
            <Playlist/>
          </Route>
          <Route path="/playlist/:playlistId">
            <PlaylistDetails/>
          </Route>
          <Route path="/signup">
            <SignupFormPage />
          </Route>
          <Route path="/">
            <LandingPage/>
          </Route>
          <Route path="/songs">
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
