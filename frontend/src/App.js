// Importing modules
import "./App.css"
import React, { useState, useEffect } from "react";


function App() {


  const [data, setData] = useState({
    "Tokens": [
      {
        "price": '', 
        "symbol": ""
      }
    ]
  })

	useEffect(() => {
    
    // gets every 1 second data from the backend
    setInterval(() => {
      fetch("/data").then((res) =>
			res.json().then((APIdata) => {
        setData(APIdata)
        
			})
		)},1000);
	}, []);

	return (
		<div className="App">
			<header className="App-header">
        <h1>BlockChains</h1>
			</header>
      <div className="App-items">
      {data["Tokens"].map((f)=>{
            return(
            <p>
              <div>
                {f["symbol"]} {f["price"]}
              </div>
              
            </p>
            )
          })}
      </div>

		</div>
	);
}

export default App;


