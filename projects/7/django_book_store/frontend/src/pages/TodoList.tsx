import * as bases from "../components/bases";
import * as components from "../components/components";
import * as store from "../components/store";
import {useDispatch, useSelector} from "react-redux";
import {useEffect} from "react";
import {Link} from "react-router-dom";


export default function Page() {
  const dispatch = useDispatch();
  const todoList = useSelector((state: any) => state.todoList);
  async function getTodos() {
      if (!todoList.load){
        components.constructorWebAction(dispatch, store.todoList, "https://jsonplaceholder.typicode.com/todos", "GET")
      }
  }
  useEffect(() => {
      getTodos()
  }, [])
  // useEffect(() => {
  //     console.log("todoList: ", todoList)
  // }, [todoList])
  return (
    <bases.Base1>
        <hr className={"my-5"}/>
      <h1 className={"lead text-danger text-center"}>Todo list</h1>
      <button className={todoList.load ? "btn btn-danger disabled" : "btn btn-danger" } onClick={getTodos}>
        getTodos
      </button>
        <br/>
      <div className={"container container-fluid text-center"}>
      {todoList.load === true && (
        <div className={"small fw-light"}>Идёт загрузка</div>
      )}
      {todoList.error === true && (
        <div className={"small fw-light text-danger"}>Неизвестная ошибка</div>
      )}
      {todoList.fail === true && (
        <div className={"small fw-light text-danger"}>{todoList.fail}</div>
      )}
        <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-3 g-3">
            {todoList.data && todoList.data.length > 0 ? todoList.data.map((item: any, index: number)=> (
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
                      <p className="card-text">
                        This is a wider card with supporting text below as a
                        natural lead-in to additional content. This content is a
                        little bit longer. ({item.id})
                      </p>
                      <div className="d-flex justify-content-between align-items-center">
                        <div className="btn-group">
                          <Link to={`/todos/${item.id}`}>
                            <button
                              type="button"
                              className="btn btn-sm btn-outline-secondary"
                            >
                              View
                            </button>
                          </Link>
                          <button
                            type="button"
                            className="btn btn-sm btn-outline-secondary"
                          >
                            Edit
                          </button>
                        </div>
                        <small className="text-muted">{item.userId}</small>
                      </div>
                    </div>
                  </div>
                </div>
            )) : "данных пока нет"}
        </div>

      </div>


        <hr className={"my-5"}/>
    </bases.Base1>
  );
}
