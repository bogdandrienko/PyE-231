import React, { useState, useEffect } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import axios from "axios";

function App1() {
  // logic - логика (js)
  //
  // ...
  return (
    // design - дизайн часть (html+css)
    <div></div>
    // ...
  );
}

function App() {
  // logic - логика (js)
  async function getData() {
    try {
      const response = await axios.get(
        "https://jsonplaceholder.typicode.com/todos",
      );
      console.log("data: ", response.data, new Date());
    } catch (error) {
      // Exception
      console.error("error: ", error, new Date());
    }
  }

  return (
    // design - дизайн часть (html+css)
    <div>
      <button onClick={getData}>click me</button>
    </div>
  );
}

createRoot(document.getElementById("root")!).render(
  // <React.StrictMode>
  <App />,
  // </React.StrictMode>
);
