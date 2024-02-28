// external
import { BrowserRouter, Routes, Route } from "react-router-dom";

// base
import Home from "../pages/Home";
import Login from "../pages/Login";
import Logout from "../pages/Logout";
import Register from "../pages/Register";

// book
import BookList from "../pages/BookList";
import BookDetail from "../pages/BookDetail";

// notes
import NotesApp from "../pages/notes/NotesApp";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        {/* base */}
        <Route path={""} element={<Home />}></Route>
        <Route path={"register/"} element={<Register />}></Route>
        <Route path={"login/"} element={<Login />}></Route>
        <Route path={"logout/"} element={<Logout />}></Route>

        {/* book */}
        <Route path={"book/"} element={<BookList />}></Route>
        <Route path={"book/:id"} element={<BookDetail />}></Route>

        {/* book */}
        <Route path={"notes/"} element={<NotesApp />}></Route>

        {/* safe redirect */}
        <Route path={"*"} element={<Home />}></Route>
      </Routes>
    </BrowserRouter>
  );
}
