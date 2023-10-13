import React, { useState, useEffect } from "react";
import { authenticate } from "./store/session";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import { SongProvider } from "./context/SongContext";
import { AuthProvider } from "./context/AuthContext";

import AlbumDetails from "./components/AlbumDetails/AlbumDetails";
import CreateAlbum from "./components/CreateAlbum/CreateAlbum";
import CreatePlaylist from "./components/CreatePlaylist/CreatePlaylist"
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import LandingPagePlaylists from "./components/LandingPagePlaylists/LandingePagePlaylists";
import MainPageTest from "./components/MainPageTest/MainPageTest";
import Player from "./components/AudioBar/audiobar";
import PlaylistDetails from "./components/PlaylistDetails/PlaylistDetails";
import Song from "./components/Songs/Song"
import SongDetails from "./components/SongDetails/SongDetails";
import SplashPage from "./components/SplashPage/SplashPage";
import TestNav from "./components/TestComponents/TestNav";
import TestSideBar from "./components/TestComponents/TestSideBar";
import UserAlbum from "./components/UserAlbum/UserAlbum";
import UserAlbumTile from "./components/UserAlbumTile/UserAlbumTile";
import UserPlaylist from "./components/UserPlaylist/UserPlaylist";
import UserPlaylistTile from "./components/UserPlaylistTile/UserPlaylistTile";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
    <AuthProvider>
      <SongProvider>
        {isLoaded && (
          <>
            <Switch>
              <Route exact path="/sidebar-test">
                <TestSideBar />
              </Route>
              <Route exact path="/nav-test">
                <TestNav />
              </Route>
              <Route exact path="/landing-page">
                <MainPageTest />
              </Route>
              <Route exact path="/login" >
                <LoginFormPage />
              </Route>
              <Route exact path="/playlist/new">
                <CreatePlaylist />
              </Route>
              <Route exact path="/album/new">
                <CreateAlbum />
              </Route>
              <Route exact path="/playlist/all">
                <UserPlaylist />
              </Route>
              <Route exact path="/album/all">
                <UserAlbum />
              </Route>
              <Route exact path="/playlist/:playlistId">
                <PlaylistDetails />
              </Route>
              <Route exact path="/album/:albumId">
                <AlbumDetails />
              </Route>
              <Route exact path="/signup">
                <SignupFormPage />
              </Route>
              <Route exact path="/song/all">
                <Song />
              </Route>
              <Route exact path="/">
                <SplashPage />
              </Route>
              <Route exact path="/song/:songId">
                <SongDetails/>
              </Route>
              <Route>
                <LandingPagePlaylists />
              </Route>
              <Route>
                <UserPlaylistTile />
              </Route>
              <Route>
                <UserAlbumTile />
              </Route>
            </Switch>
            <Player />
          </>
        )}
      </SongProvider>
      </AuthProvider>
    </>
  );
}

export default App;
