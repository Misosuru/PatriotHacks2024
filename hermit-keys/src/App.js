import React, { useState } from "react";
import Tabs from "./Tabs";
import HomeContent from "./HomeContent";

const App = () => {
  const tabData = [
    { label: "Home", content: <HomeContent /> },
    { label: "Buyer", content: <div>Information for Buyers</div> },
    { label: "Rent", content: <div>Explore Rental Options</div> },
    { label: "About", content: <div>Learn More About The Project</div> },
    { label: "References", content: <div>Insert Zotero Citations Here</div> },
  ];

  const [activeTab, setActiveTab] = useState("Home");

  const handleTabClick = (label) => {
    setActiveTab(label); // Set the clicked tab as the active tab
  };

  return (
    <div className="App">
      <h1 className="hermit-keys">
        <h3>Find Your</h3>
        HermitKeys
      </h1>
      <Tabs tabs={tabData} onTabClick={handleTabClick} activeTab={activeTab} />
    </div>
  );
};

export default App;
