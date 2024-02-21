import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import Login from "../pages/Login";
import TodoList from "../pages/TodoList";
// import Login from "../pages/Login";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path={""} element={<Home />}></Route>
        <Route path={"login/"} element={<Login />}></Route>
        <Route path={"signup/"} element={<Login />}></Route>
        <Route path={"todos/"} element={<TodoList />}></Route>

        <Route path={"*"} element={<Home />}></Route>
      </Routes>
    </BrowserRouter>
  );
}
