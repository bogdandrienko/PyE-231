// external
import React, { useState, useEffect } from "react";
import { createRoot } from "react-dom/client";
import {Provider} from "react-redux";
// css
import "./css/bootstrap/bootstrap.css";
import "./css/fontawesome/css/all.css";
import "./index.css";
// internal
import Router from "./components/router";
import store from "./components/store";

const container = document.getElementById('root')!;
const root = createRoot(container);

root.render(
  // <React.StrictMode>
    <Provider store={store}>
      <Router />,
    </Provider>
  // </React.StrictMode>
);
