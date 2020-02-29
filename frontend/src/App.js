import React, { useState, useEffect } from "react";
// import logo from "./logo.svg";
import "./style/App.css";

import Map from "./components/Map";

function App() {
  const [data, setData] = useState([]);

  //TODO: Change this to an API call
  // and the other fetch requests
  useEffect(_ => {
    fetch("http://127.0.0.1:5000/all", {
      method: "GET",
      headers: {
        "Content-Type": "application/json"
      }
    })
      .then(res => {
        return res.json();
      })
      .then(res => {
        console.log(res.test_data);
        setData(res.test_data);
      })
      .catch(e => {
        console.log(e);
      });
  }, []);

  return (
    <div>
      <Map data={data} />
    </div>
  );
}

export default App;
