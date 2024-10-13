import React from "react";
import "./HomeContent.css";

const HomeContent = () => {
  return (
    <div className="home-container">
      <div className="content-container">
        <div className="text-container">
          <h1>Welcome to HermitKeys!</h1>
          <p>~</p>
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
          <p>~</p>
          <p>Add additional info about the graphics to the right.</p>
        </div>
        <div className="image-container">
          <img src="/nationalRent.png" alt="Description" />
          <img src="/nationalBuy.png" alt="Description" />
        </div>
      </div>
    </div>
  );
};

export default HomeContent;
