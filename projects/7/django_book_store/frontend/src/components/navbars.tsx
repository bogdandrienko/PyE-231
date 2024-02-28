// external
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import { useEffect } from "react";
import * as constants from "./constants";
import * as utils from "./utils";

export function Navbar1() {
  const userLogin = useSelector((state: any) => state.userLogin);
  const dispatch = useDispatch();
  useEffect(() => {
    if (utils.LocalStorage.get("userLogin.data.access")) {
      dispatch({
        type: constants.userLogin.success,
        payload: {
          access: utils.LocalStorage.get("userLogin.data.access"),
          refresh: utils.LocalStorage.get("userLogin.data.refresh"),
        },
      });
    }
  }, []);

  return (
    <header className="p-3 text-bg-dark">
      <div className="container">
        <div className="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
          <ul className="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
            <li>
              <Link to="/" className="nav-link px-2 text-secondary">
                Домашняя
              </Link>
            </li>
            <li>
              <Link to="/book" className="nav-link px-2 text-white">
                Список книг
              </Link>
            </li>
            {userLogin && userLogin.data && (
              <li>
                <Link to="/book/public" className="nav-link px-2 text-danger">
                  Предложить книгу
                </Link>
              </li>
            )}
            <li>
              <a href="#" className="nav-link px-2 text-white">
                Поиск
              </a>
            </li>
            <li>
              <a href="#" className="nav-link px-2 text-white">
                Категории
              </a>
            </li>
            <li>
              <a href="#" className="nav-link px-2 text-white">
                Рейтинги
              </a>
            </li>
            <li>
              <Link to="/notes" className="nav-link px-2 text-white">
                Заметки
              </Link>
            </li>
          </ul>

          <div className="text-end">
            {userLogin && userLogin.data ? (
              <div className="input-group">
                <Link to="/logout" className="btn btn-outline-danger">
                  <i className="fa-solid fa-right-from-bracket p-2 m-0"></i>
                  Выйти
                </Link>
              </div>
            ) : (
              <div className="input-group">
                <Link to="/login" className="btn btn-outline-success">
                  <i className="fa-solid fa-door-open p-2 m-0"></i>
                  Войти
                </Link>
                <Link to="/register" className="btn btn-outline-warning">
                  <i className="fa-solid fa-user-plus p-2 m-0"></i>
                  Зарегистрироваться
                </Link>
              </div>
            )}
          </div>
        </div>
      </div>
    </header>
  );
}

export function Navbar2() {
  return <header></header>;
}
