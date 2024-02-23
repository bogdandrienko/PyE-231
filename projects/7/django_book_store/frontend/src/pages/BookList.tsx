// TODO external  //////////////////////////////////////////////////////////////////
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
// TODO internal //////////////////////////////////////////////////////////////////
import * as bases from "../components/bases";
import * as components from "../components/components";
import * as constants from "../components/constants";
import * as store from "../components/store";
import * as loaders from "../components/loaders";

export default function Page() {
  // TODO hooks //////////////////////////////////////////////////////////////////
  const dispatch = useDispatch();
  const bookList = useSelector((state: any) => state.bookList);
  const [data, setData] = useState([]);
  const [isReversed, setIsReversed] = useState(false);

  // TODO functions //////////////////////////////////////////////////////////////////
  async function getBooks() {
    if (!bookList.load) {
      //  && !bookList.data
      components.constructorWebAction(
        dispatch,
        constants.bookList,
        `http://127.0.0.1:8000/api/book/`,
        "GET",
      );
    }
  }

  // TODO useEffect //////////////////////////////////////////////////////////////////
  useEffect(() => {
    getBooks();
  }, []);

  useEffect(() => {
    if (bookList.data) {
      //[1, 2, 3] -> [3, 2, 1]
      const newArray: any = [];
      for (let i = 0; i < bookList.data.length; i += 1) {
        if (isReversed) {
          newArray.push(bookList.data[bookList.data.length - i - 1]);
        } else {
          newArray.push(bookList.data[i]);
        }
      }
      setData(newArray);
    }
  }, [bookList.data, isReversed]);

  useEffect(() => {
    console.log("bookList: ", bookList);
  }, [bookList]);

  return (
    <bases.Base1>
      <hr className={"mt-5"} />
      <h1 className={"lead display-5 text-center"}>Список книг:</h1>
      <div className={"d-flex container justify-content-end"}>
        {isReversed ? (
          <button
            className={"btn btn-primary m-1 p-3"}
            onClick={() => {
              setIsReversed(!isReversed);
            }}
          >
            обратная сортировка
          </button>
        ) : (
          <button
            className={"btn btn-outline-primary m-1 p-3"}
            onClick={() => {
              setIsReversed(!isReversed);
            }}
          >
            прямая сортировка
          </button>
        )}
      </div>
      <br />
      <div className={"container container-fluid text-center"}>
        <loaders.Loader1 isView={bookList.load} />
        {bookList.error && (
          <div className="alert alert-danger" role="alert">
            {bookList.error}
          </div>
        )}
        {bookList.fail && (
          <div className="alert alert-danger" role="alert">
            {bookList.fail}
          </div>
        )}
        <div className="row row-cols-1 row-cols-sm-2 row-cols-md-2 row-cols-lg-2 g-3">
          {!bookList.load && data && data.length > 0
            ? data.map((item: any, index: number) => (
                <div key={item.id} className="col">
                  <div className="card shadow-sm">
                    <svg
                      className="bd-placeholder-img card-img-top"
                      width="100%"
                      height="225"
                      xmlns="http://www.w3.org/2000/svg"
                      role="img"
                      aria-label="Placeholder: Thumbnail"
                      preserveAspectRatio="xMidYMid slice"
                      focusable="false"
                    >
                      <title>{item.title}</title>
                      <rect width="100%" height="100%" fill="#55595c"></rect>
                      <text x="50%" y="50%" fill="#eceeef" dy=".3em">
                        {item.title} ({item.id})
                      </text>
                    </svg>

                    <div
                      className={
                        item.completed
                          ? "card-body border border-3 border-success"
                          : "card-body border border-3 border-warning"
                      }
                    >
                      <p className="card-text">{item.description}</p>
                      <div className="d-flex justify-content-between align-items-center">
                        <div className="input-group">
                          <Link
                            to={`/book/${item.id}`}
                            className="btn btn-outline-secondary"
                          >
                            Детальный просмотр
                          </Link>
                          <button
                            type="button"
                            className="btn btn-outline-secondary"
                          >
                            Edit
                          </button>
                        </div>
                        <small className="text-muted">{item.userId}</small>
                      </div>
                    </div>
                  </div>
                </div>
              ))
            : ""}
        </div>
      </div>

      <hr className={"mb-5"} />
    </bases.Base1>
  );
}
