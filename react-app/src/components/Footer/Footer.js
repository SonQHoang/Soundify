import React from "react";
import Player from "../AudioBar/audiobar";
import { usePlayer } from "../../context/AudioPlayerContext";
import "./Footer.css";

const Footer = () => {
  const { currentSong } = usePlayer();

  return (
    <div className="footer-container">
      {currentSong && (
        <div>
          <Player src={currentSong} />
        </div>
      )}
    </div>
  );
};

export default Footer;
