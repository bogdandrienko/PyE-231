// external
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";

// internal
import * as bases from "../components/bases";
import * as utils from "../components/utils";
import * as constants from "../components/constants";
import * as components from "../components/components";
import * as loaders from "../components/loaders";

export default function Page() {
  // TODO hook ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const userRegister = useSelector((state: any) => state.userRegister);
  const [form, setForm] = useState({
    username: "",
    password: "",
    password2: "",
    sex: true,
    age: 18,
  });

  // TODO function ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  function sendForm(event: any) {
    // остановка перезагрузки страницы
    event.preventDefault();

    if (form.password === form.password2 && !userRegister.load) {
      components.constructorWebAction(
        dispatch,
        constants.userRegister,
        `${constants.host}/api/user/register/`,
        "POST",
        { username: form.username, password: form.password },
        // { ...form },
      );
    } else {
      window.alert("Заполните пароль!");
    }
  }

  // TODO useEffect //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

  useEffect(() => {
    if (userRegister && userRegister.data) {
      setTimeout(() => {
        navigate("/login");
        dispatch({ type: constants.userRegister.reset });
      }, 2000);
    }
  }, [userRegister]);

  useEffect(() => {
    if (constants.isDebug) {
      console.log("userRegister: ", userRegister);
    }
  }, [userRegister]);

  return (
    <bases.Base1>
      <div className={"container text-center my-5"}>
        <h1 className="h3 display-5 lead fw-normal mb-3">Создайте аккаунт:</h1>

        <article>
          // TODO можно собрать воедино для DRY
          <loaders.Loader1 isView={userRegister.load} />
          {userRegister.error && (
            <div className="alert alert-danger" role="alert">
              {userRegister.error}
            </div>
          )}
          {userRegister.fail && (
            <div className="alert alert-danger" role="alert">
              {userRegister.fail}
            </div>
          )}
          {userRegister.data && (
            <div className="alert alert-success" role="alert">
              Аккаунт успешно создан!
            </div>
          )}
        </article>

        <form className={""} onSubmit={sendForm}>
          <div className={"m-1 p-1 input-group"}>
            <label className={"fw-bold p-2"}>
              Введите почту для регистрации:
            </label>
            <input
              type={"email"} // регулярка HTML5
              placeholder={"admin@gmail.com"}
              className={"form-control w-50"}
              value={form.username}
              onChange={(event) => {
                setForm({ ...form, username: event.target.value });
              }}
            ></input>
          </div>
          <div className={"m-1 p-1 input-group"}>
            <label className={"fw-bold p-2"}>Введите пароль:</label>
            <input
              type={"password"}
              placeholder={"Qwerty!123"}
              className={"form-control w-50"}
              value={form.password}
              onChange={(event) => {
                setForm({
                  ...form,
                  password: utils.Regex.inputPassword2(event.target.value),
                });
              }}
            ></input>
          </div>
          <div className={"m-1 p-1 input-group"}>
            <label className={"fw-bold p-2"}>Повторите пароль:</label>
            <input
              type={"password"}
              placeholder={"Qwerty!123"}
              className={"form-control w-50"}
              value={form.password2}
              onChange={(event) => {
                setForm({
                  ...form,
                  password2: utils.Regex.inputPassword2(event.target.value),
                });
              }}
            ></input>
          </div>
          {form.password !== form.password2 && (
            <div className="alert alert-danger" role="alert">
              пароли не совпадают!
            </div>
          )}
          <button
            className={
              form.password !== form.password2
                ? "btn btn-outline-warning w-50 disabled"
                : "btn btn-outline-warning w-50"
            }
            type={"submit"}
          >
            создать аккаунт
          </button>
        </form>
      </div>
    </bases.Base1>
  );
}
