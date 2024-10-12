// HomeContent.js
import React from "react";
import "./HomeContent.css"; // Optional: Add styles in a separate CSS file

const HomeContent = () => {
  return (
    <div className="home-container">
      <div className="text-container">
        <h3>Welcome to HermitKeys</h3>
        <p>
          Find your perfect home with us. Explore various options tailored to
          your needs!
        </p>
      </div>
      <div className="image-container">
        <img src="/path/to/your/image.jpg" alt="Description" />
      </div>
      <div className="input-container">
        <label htmlFor="disabledInput">Your Message:</label>
        <input
          type="text"
          id="disabledInput"
          value="This is a grayed-out textbox."
          disabled // This makes the textbox non-editable
          className="textbox" // Add a class for styling
        />
      </div>
    </div>
  );
};

export default HomeContent;
