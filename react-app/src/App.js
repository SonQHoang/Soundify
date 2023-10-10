import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import CreatePlaylist from "./components/CreatePlaylist/CreatePlaylist"
import UserPlaylist from "./components/UserPlaylist/UserPlaylist";
import PlaylistDetails from "./components/PlaylistDetails/PlaylistDetails";
import AlbumDetails from "./components/AlbumDetails/AlbumDetails";
import Song from "./components/Songs/Song"
import CreateAlbum from "./components/CreateAlbum/CreateAlbum";
import UserAlbum from "./components/UserAlbum/UserAlbum";
import SplashPage from "./components/SplashPage/SplashPage";
import LandingPagePlaylists from "./components/LandingPagePlaylists/LandingePagePlaylists";
import MainPageTest from "./components/MainPageTest/MainPageTest";
import TestNav from "./components/TestComponents/TestNav";
import TestSideBar from "./components/TestComponents/TestSideBar";
import UserPlaylistTile from "./components/UserPlaylistTile/UserPlaylistTile";
import UserAlbumTile from "./components/UserAlbumTile/UserAlbumTile";
import { SongProvider } from "./context/SongContext";
import Player from "./components/AudioBar/audiobar";
import SongDetails from "./components/SongDetails/SongDetails";
// import Footer from "./components/Footer/Footer";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <SongProvider>
        {/* <Navigation isLoaded={isLoaded} /> */}
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
    </>
  );
}

export default App;
