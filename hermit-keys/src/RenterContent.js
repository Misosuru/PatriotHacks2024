import React, { useState } from "react";
import axios from "axios";
import "./RenterContent.css";

const RenterContent = () => {
  // Define state for annual income and selected dropdown option
  const [annualIncome, setAnnualIncome] = useState("");
  const [selectedOption, setSelectedOption] = useState("");
  const [responseMessage, setResponseMessage] = useState(""); // For the response

  // Handle input change for the income
  const handleInputChange = (e) => {
    setAnnualIncome(e.target.value); // Update annual income state
  };

  //https://www.w3schools.com/howto/howto_css_dropdown.asp
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
    <div className="renter-container">
      <form onSubmit={handleSubmit}>
        <div className="user-container">
          <div className="combined-container">
            <div className="text-container">
              <p>
                Annual income is the biggest factor when it comes to choosing
                your home. Financial advisors typically advise their clients to
                set aside 30% of their gross annual income for house bills
                alone. We took that into account, and thought ahead about
                inflation! Renting laws vary from county to county, so some
                landlords can jack up prices for the second lease. To calculate
                an appropriate budget, we found the lower limit based on your
                current income, and an upper limit based on projected inflation
                for the next 4 years. All you need to look at are the final
                results! We make finding an affordable and stable home as breezy
                as the beach.
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
              <p>
                Over 3,000 counties across the US have different costs of
                living, welfare, transportation, local inflation, and renting
                laws. All these different criteria and boxes to check make house
                hunting so overwhelming. Thankfully, our tool can help you out.
                While currently we are only zoned for Fairfax County, VA, we
                plan to expand further out into Virginia, and then farther on
                the East Coast! We'll help you take into account the different
                aspects of living and commuting to work, to ensure your trip to
                work is as relaxing as a vacation.
              </p>
            </div>
            <div className="dropdown-container">
              <label htmlFor="county-preference">
                <p>Select County Preference:</p>
              </label>
              <select
                id="county-reference"
                value={selectedOption}
                onChange={handleDropdownChange}
              >
                <option value="" disabled>
                  Select an option
                </option>
                <option value="Fairfax">Fairfax</option>
              </select>
            </div>
          </div>
          <div className="combined-container">
            <div className="text-container">
              <p>
                Money isn't the only important thing about house-hunting! We
                understand there are multiple factors to making that dream home
                click. By inputting what type of house unit you want, we help
                match you with different building styles, community sizes, and
                age of buildings and appliances. We are currently in alpha, but
                we hope to introduce narrowing down sweet spots with appropriate
                vacancies and an archtectural style that fits your own.
              </p>
            </div>
            <div className="dropdown-container">
              <label htmlFor="unit-reference">
                <p>Select Unit Preference:</p>
              </label>
              <select
                id="unit-reference"
                value={selectedOption}
                onChange={handleDropdownChange}
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
        <div className="results-container">
          {responseMessage && <p>{responseMessage}</p>}
        </div>
      </form>
    </div>
  );
};

export default RenterContent;
