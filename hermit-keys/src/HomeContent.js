import React from "react";
import "./HomeContent.css";

const HomeContent = () => {
  return (
    <div className="home-container">
      <div className="content-container">
        <div className="text-container">
          <h3>Welcome to HermitKeys</h3>
          <p>
            Find your perfect home with us. Explore various options tailored to
            your needs!
          </p>
        </div>
        <div className="image-container">
          <img src="/IMG_9744.jpg" alt="Description" />
        </div>
      </div>
      <div className="input-container">
        <label htmlFor="disabledInput">
          <p>Zip Code: </p>
        </label>
        <input
          type="text"
          id="disabledInput"
          value="Enter Zip Code Here."
          disabled
          className="textbox" // Add a class for styling
        />
      </div>
    </div>
  );
};

export default HomeContent;
