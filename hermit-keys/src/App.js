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
    //{ label: "Buyer", content: <BuyerContent /> },
    {
      label: "Buyer",
      content: (
        <div>
          <p>
            <i>Pardon the Sand!</i>
          </p>
          <p>
            Thank you for your patience! We're busy crafting the Buyer
            Information section to bring you everything you need to find your
            perfect home. Check back soon for exciting updates!
          </p>
        </div>
      ),
    },
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
      <img
        src="/THE_CUTEST_CRABS.png"
        alt="Description"
        style={{ width: "300px", height: "auto" }}
      />
    </div>
  );
};

export default App;
