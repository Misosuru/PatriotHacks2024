import React from "react";
import "./HomeContent.css";

const HomeContent = () => {
  return (
    <div className="home-container">
      <div className="content-container">
        <div className="text-container">
          <h3>Welcome to HermitKeys!</h3>
          <p>
            Having trouble singling out your forever home? Looking for that
            perfect place that feels just right? Look no further!{" "}
          </p>
          <p>
            HermitKeys is the ultimate platform dedicated to helping you
            discover your ideal living space. We want to help you find your
            ideal home, transforming that dream vacation retreat into your
            forever home. We provide quality options tailored to your needs.
            With our intuitive search tools, you can easily explore a wide range
            of housing options designed to fit your budget and lifestyle
            preferences. Just enter your preferred zip code and must-haves, and
            let us do the rest! We know that the first step to finding a home
            can be a bit of a doozy, but we’re here to help. Let HermitKeys
            guide you on your home journey.
          </p>
        </div>
        <div className="image-container">
          <img src="/nationalBuy.png" alt="Description" />
          <img src="/nationalRent.png" alt="Description" />
        </div>
      </div>
      <div className="input-container">
        <label htmlFor="disabledInput">
          <p>County: </p>
        </label>
        <input
          type="text"
          id="disabledInput"
          value="Enter a County."
          disabled
          className="textbox" // Add a class for styling
        />
      </div>
    </div>
  );
};

export default HomeContent;
