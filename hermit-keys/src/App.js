import React, { useState } from "react";
import Tabs from "./Tabs";
import HomeContent from "./HomeContent";
import RenterContent from "./RenterContent";
import BuyerContent from "./BuyerContent";
import RefContent from "./RefContent";

const App = () => {
  const tabData = [
    { label: "Home", content: <HomeContent /> },
    { label: "Renter", content: <RenterContent /> },
    { label: "Buyer", content: <BuyerContent /> },
    { label: "About", content: <div>Learn More About The Project</div> },
    { label: "References", content: <RefContent /> },
  ];

  const [activeTab, setActiveTab] = useState("Home");

  const handleTabClick = (label) => {
    setActiveTab(label); // Set the clicked tab as the active tab
  };

  return (
    <div className="App">
      <h1 className="hermit-keys">
        <h3>
          <span>Find Your</span>
        </h3>
        <span>HermitKeys</span>
      </h1>
      <Tabs tabs={tabData} onTabClick={handleTabClick} activeTab={activeTab} />
    </div>
  );
};

export default App;
