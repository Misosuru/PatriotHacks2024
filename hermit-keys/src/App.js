import React, { useState } from "react";
import Tabs from "./Tabs";
import HomeContent from "./HomeContent";
import RenterContent from "./RenterContent";
import BuyerContent from "./BuyerContent";
import RefContent from "./RefContent";

const App = () => {
  //https://www.geeksforgeeks.org/how-to-create-tabs-in-reactjs/
  const tabData = [
    { label: "Home", content: <HomeContent /> },
    { label: "Renter", content: <RenterContent /> },
    { label: "Buyer", content: <BuyerContent /> },
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
