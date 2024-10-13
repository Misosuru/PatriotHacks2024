//https://www.geeksforgeeks.org/how-to-create-tabs-in-reactjs/
import React from "react";
import Tab from "./Tab";
import "./App.css";

const Tabs = ({ tabs, onTabClick, activeTab }) => {
  return (
    <div className="tabs-container">
      <div className="tabs">
        {tabs.map((tab, index) => (
          <Tab
            key={index}
            label={tab.label}
            isActive={tab.label === activeTab}
            onClick={() => onTabClick(tab.label)}
          />
        ))}
      </div>
      <div className="tab-content">
        {tabs.find((tab) => tab.label === activeTab)?.content}
      </div>
    </div>
  );
};

export default Tabs;
