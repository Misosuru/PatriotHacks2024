import React from "react";
import Tabs from "./Tabs";

const App = () => {
  const tabData = [{ label: "Tab 1" }, { label: "Tab 2" }, { label: "Tab 3" }];

  return (
    <div className="App">
      <h1 className="geeks">GeeksforGeeks</h1>
      <h1>React Tabs Example</h1>
      <Tabs tabs={tabData} />
    </div>
  );
};

export default App;
