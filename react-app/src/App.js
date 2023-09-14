import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation/Navigation";
// import Player from "./components/AudioBar/audiobar";
import LandingPage from "./components/LandingPage/landingpage";
import CreatePlaylist from "./components/CreatePlaylist/CreatePlaylist"
// import Playlist from "./components/Playlists/Playlists";
import UserPlaylist from "./components/UserPlaylist/UserPlaylist";
import PlaylistDetails from "./components/PlaylistDetails/PlaylistDetails";
import AlbumDetails from "./components/AlbumDetails/AlbumDetails";
import Song from "./components/Songs/Song"
import CreateAlbum from "./components/CreateAlbum/CreateAlbum";
import UserAlbum from "./components/UserAlbum/UserAlbum";
import Footer from "./components/Footer/Footer";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      {/* <Navigation isLoaded={isLoaded} /> */}
      {isLoaded && (
        <div className="app-container">
          <main className="content">
        <Switch>
          <Route exact path="/login" >
            <LoginFormPage />
          </Route>
          <Route exact path="/playlist/new">
            <CreatePlaylist/>
          </Route>
          <Route exact path="/album/new">
            <CreateAlbum/>
          </Route>
          <Route exact path="/playlist/all">
            <UserPlaylist/>
          </Route>
          <Route exact path="/album/all">
            <UserAlbum/>
          </Route>
          <Route exact path="/playlist/:playlistId">
            <PlaylistDetails/>
          </Route>
          <Route exact path="/album/:albumId">
            <AlbumDetails/>
          </Route>
          <Route exact path="/signup">
            <SignupFormPage />
          </Route>
          <Route exact path="/song/all">
            <Song />
          </Route>
          <Route exact path="/">
            <LandingPage/>
          </Route>
          <Route>
            <Footer/>
          </Route>
        </Switch>
        </main>
        </div>
      )}
      {/* <Player/> */}
    </>
  );
}

export default App;
