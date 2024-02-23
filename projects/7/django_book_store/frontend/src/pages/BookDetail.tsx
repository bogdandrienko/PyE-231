// TODO external  //////////////////////////////////////////////////////////////////
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useParams } from "react-router-dom";
// TODO internal //////////////////////////////////////////////////////////////////
import * as bases from "../components/bases";
import * as components from "../components/components";
import * as constants from "../components/constants";
import * as store from "../components/store";
import * as loaders from "../components/loaders";

export default function Page() {
  // TODO hooks //////////////////////////////////////////////////////////////////
  const dispatch = useDispatch();
  const bookDetail = useSelector((state: any) => state.bookDetail);
  const params = useParams();

  // TODO functions //////////////////////////////////////////////////////////////////
  async function getBook() {
    if (!bookDetail.load) {
      components.constructorWebAction(
        dispatch,
        constants.bookDetail,
        `http://127.0.0.1:8000/api/book/${params.id}`,
        "GET",
      );
    }
  }

  // TODO useEffect //////////////////////////////////////////////////////////////////
  useEffect(() => {
    getBook();
  }, []);

  useEffect(() => {
    console.log("bookDetail: ", bookDetail);
  }, [bookDetail]);

  return (
    <bases.Base1>
      {" "}
      <hr className={"mt-5"} />
      <h1 className={"lead display-5 text-center"}>Детально о книге: </h1>
      <div className={"d-flex container justify-content-end"}>
        <Link
          to={"/book"}
          className={"btn btn-success m-1 p-3"}
          onClick={() => {}}
        >
          к списку книг
        </Link>
      </div>
      <br />
      <div className={"container container-fluid text-center"}>
        <loaders.Loader1 isView={bookDetail.load} />
        {bookDetail.error && (
          <div className="alert alert-danger" role="alert">
            {bookDetail.error}
          </div>
        )}
        {bookDetail.fail && (
          <div className="alert alert-danger" role="alert">
            {bookDetail.fail}
          </div>
        )}
        <div className="row row-cols-1 row-cols-sm-1 row-cols-md-1 row-cols-lg-1 g-3">
          {!bookDetail.load && bookDetail.data ? (
            <div className="col">
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
                  <title>{bookDetail.data.title}</title>
                  <rect width="100%" height="100%" fill="#55595c"></rect>
                  <text x="50%" y="50%" fill="#eceeef" dy=".3em">
                    {bookDetail.data.title} ({bookDetail.data.id})
                  </text>
                </svg>

                <div
                  className={
                    bookDetail.data.completed
                      ? "card-body border border-3 border-success"
                      : "card-body border border-3 border-warning"
                  }
                >
                  <p className="card-text">{bookDetail.data.description}</p>
                  <div className="d-flex justify-content-between align-items-center">
                    <div className="input-group">
                      <button
                        type="button"
                        className="btn btn-outline-secondary"
                      >
                        Edit
                      </button>
                    </div>
                    <small className="text-muted">
                      {bookDetail.data.userId}
                    </small>
                  </div>
                </div>
              </div>
            </div>
          ) : (
            ""
          )}
        </div>
      </div>
      <hr className={"mb-5"} />
    </bases.Base1>
  );
}
