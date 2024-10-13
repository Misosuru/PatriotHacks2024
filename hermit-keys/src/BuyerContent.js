import React, { useState } from "react";
import axios from "axios";
import "./BuyerContent.css";

const BuyerContent = () => {
  // Define state for annual income and selected dropdown option
  const [annualIncome, setAnnualIncome] = useState("");
  const [selectedOption, setSelectedOption] = useState("");
  const [responseMessage, setResponseMessage] = useState(""); // For the response

  // Handle input change for the income
  const handleInputChange = (e) => {
    setAnnualIncome(e.target.value); // Update annual income state
  };

  // Handle dropdown change
  const handleDropdownChange = (e) => {
    setSelectedOption(e.target.value); // Update selected option state
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Send the data to the backend
      const response = await axios.post("/api/income", {
        annualIncome,
        selectedOption,
      });
      setResponseMessage("Submission successful!");
    } catch (error) {
      setResponseMessage("Error submitting data.");
    }
  };

  return (
    <div className="buyer-container">
      <form onSubmit={handleSubmit}>
        <div className="user-container">
          <div className="combined-container">
            <div className="text-container">
              <p>
                Financial experts recommend that no more than 30% of your annual
                income should go to housing costs. Use this tool to estimate how
                much you can comfortably spend on housing.
              </p>
            </div>

            <div className="input-container">
              <label htmlFor="annualIncome">
                <p>Enter Your Annual Income:</p>
              </label>
              <input
                type="number"
                id="annualIncome"
                placeholder="Enter your Annual Income"
                value={annualIncome}
                onChange={handleInputChange}
                className="textbox"
                required
              />
            </div>
          </div>
          <div className="combined-container">
            <div className="text-container">
              <p>Add descriptions for counties here.</p>
            </div>
            <div className="dropdown-container">
              <label htmlFor="county-preference">
                <p>Select County Preference:</p>
              </label>
              <select
                id="county-reference"
                value={selectedOption}
                onChange={handleDropdownChange}
                required
              >
                <option value="" disabled>
                  Select an option
                </option>
                <option value="Fairfax">Fairfax</option>
                <option value="Loudoun">Loudoun</option>
                <option value="Prince Williams">Prince Williams</option>
              </select>
            </div>
          </div>
          <div className="combined-container">
            <div className="text-container">
              <p>Add descriptions for units here.</p>
            </div>
            <div className="dropdown-container">
              <label htmlFor="unit-reference">
                <p>Select Unit Preference:</p>
              </label>
              <select
                id="unit-reference"
                value={selectedOption}
                onChange={handleDropdownChange}
                required
              >
                <option value="" disabled>
                  Select an option
                </option>
                <option value="Studio">Studio</option>
                <option value="1 Bedroom">1 Bedroom</option>
                <option value="1 Den">1 Den</option>
                <option value="2 Bedroom">2 Bedroom</option>
                <option value="2 Den">2 Den</option>
                <option value="3 Bedroom">3 Bedroom</option>
                <option value="3 Den">3 Den</option>
                <option value="4 Bedroom">3 Bedroom</option>
              </select>
            </div>
          </div>
        </div>
        <button type="submit" className="submit-button">
          Submit
        </button>

        {/* Display response message */}
        {responseMessage && <p>{responseMessage}</p>}
      </form>
    </div>
  );
};

export default BuyerContent;
