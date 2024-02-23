import { BrowserRouter, Routes, Route } from "react-router-dom";

// base
import Home from "../pages/Home";
import Login from "../pages/Login";
import Register from "../pages/Register";

// book
import BookList from "../pages/BookList";
import BookDetail from "../pages/BookDetail";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        {/* base */}
        <Route path={""} element={<Home />}></Route>
        <Route path={"login/"} element={<Login />}></Route>
        <Route path={"register/"} element={<Register />}></Route>

        {/* book */}
        <Route path={"book/"} element={<BookList />}></Route>
        <Route path={"book/:id"} element={<BookDetail />}></Route>

        {/* safe */}
        <Route path={"*"} element={<Home />}></Route>
      </Routes>
    </BrowserRouter>
  );
}
