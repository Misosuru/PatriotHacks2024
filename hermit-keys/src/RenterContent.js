import React, { useState } from "react";
//import axios from "axios";

const RenterContent = () => {
  const [income, setIncome] = useState("");

  const handleInputChange = (e) => {
    setIncome(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    //   try {
    //     const response = await axios.post("http://localhost:3000/", {
    //       income: income,
    //     });
    //     console.log(response.data);
    //   } catch (error) {
    //     console.error("Error submitting income data:", error);
    //   }
    // };

    return (
      <div className="renter-container">
        <form onSubmit={handleSubmit}>
          <div className="text-container">
            <p>30% of your annual income should go to housing.</p>
          </div>
          <div className="input-container">
            <label htmlFor="annualIncome">Enter Your Annual Income:</label>
            <input
              type="number"
              id="annualIncome"
              value={income}
              onChange={handleInputChange}
              className="textbox"
              required
            />
          </div>
          <button type="submit">Submit</button>
        </form>
      </div>
    );
  };
};

export default RenterContent;
