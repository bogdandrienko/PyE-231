import { Link } from "react-router-dom";

export function Navbar1() {
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
            !
            <li>
              <Link to="/book/public" className="nav-link px-2 text-white">
                Предложить книгу (если человек украдёт ссылку, его нужно
                перенаправлять AuthGuard)
              </Link>
            </li>
            !
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
          </ul>

          <form
            className="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3"
            role="search"
          >
            <input
              type="search"
              className="form-control form-control-dark text-bg-dark"
              placeholder="Search..."
              aria-label="Search"
            />
          </form>

          <div className="text-end">
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
          </div>
        </div>
      </div>
    </header>
  );
}

export function Navbar2() {
  return <header></header>;
}
