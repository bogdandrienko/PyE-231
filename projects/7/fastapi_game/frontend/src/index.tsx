import React, { useState, useEffect } from "react";
import { createRoot } from "react-dom/client";
import "./css/bootstrap/bootstrap.css";
import "./css/fontawesome/css/all.css";
import "./index.css";
import axios from "axios";
import Router from "./components/router";

function CounterNotWorked() {
  let counter = 666;
  function Increase() {
    counter = counter + 1;
    console.log(counter, new Date());
  }
  function Decrease() {
    counter -= 1;
    console.log(counter, new Date());
  }
  return (
    <div>
      <div className={"header"}>{counter}</div>
      <div className={"body"}>
        <button onClick={Increase}>+</button>
      </div>
      <div className={"footer"}>
        <button onClick={Decrease}>-</button>
      </div>
    </div>
  );
}

function Counter() {
  //      getter           setter
  const [counter, setCounter] = useState(666);

  function Increase() {
    setCounter(counter + 1);
    console.log(counter, new Date());
  }
  function Decrease() {
    setCounter(counter - 1);
    console.log(counter, new Date());
  }
  return (
    <div>
      <div className={"header"}>{counter}</div>
      <div className={"body"}>
        <button onClick={Increase}>+</button>
      </div>
      <div className={"footer"}>
        <button onClick={Decrease}>-</button>
      </div>
    </div>
  );
}

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
  const var1 = "Богдан1";
  let var2 = "Богдан2";
  // var var3 = "Богдан3";  // устарело

  // logic - логика (js)
  async function getData() {
    // axios
    //   .get("https://jsonplaceholder.typicode.com/todos")
    //   .then((response) => {
    //     console.log("data: ", response.data, new Date());
    //   })
    //   .catch((error) => {
    //     console.error("error: ", error, new Date());
    //   });
    // Ecmascript

    try {
      const response = await axios.get(
        // "https://jsonplaceholder.typicode.com/todos",
        "http://127.0.0.1:8000/api/data/",
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
      <h1>
        {var1} {var2}
      </h1>
      <button onClick={getData}>click me</button>
      <hr />
      {12 > 5 && "Показать, если правда"}
      {12 < 5 && "Показать, если ложь"}
      {12 < 5 ? "Правда3" : "Ложь3"}
      <hr />
      <Counter />
      // js - javascript // ts - typescript // jsx - react // tsx - typescript +
      react
    </div>
  );
}

createRoot(document.getElementById("root")!).render(
  // <React.StrictMode>
  <Router />,
  // </React.StrictMode>
);
