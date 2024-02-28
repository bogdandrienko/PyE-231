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
  const userLogin = useSelector((state: any) => state.userLogin);
  const [form, setForm] = useState({
    username: "",
    password: "",
    sex: true,
    age: 18,
  });

  // TODO function ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  function sendForm(event: any) {
    // остановка перезагрузки страницы
    event.preventDefault();

    if (form.password !== "" && !userLogin.load) {
      components.constructorWebAction(
        dispatch,
        constants.userLogin,
        `${constants.host}/api/token/`,
        "POST",
        { username: form.username, password: form.password },
        // { ...form },
        10000,
        true,
      );
    } else {
      window.alert("Заполните пароль!");
    }
  }

  // TODO useEffect //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

  useEffect(() => {
    if (userLogin && userLogin.data) {
      utils.LocalStorage.set("userLogin.data.access", userLogin.data.access);
      utils.LocalStorage.set("userLogin.data.refresh", userLogin.data.refresh);
      setTimeout(() => {
        navigate("/");
      }, 2000);
    }
  }, [userLogin]);

  useEffect(() => {
    if (constants.isDebug) {
      console.log("userLogin: ", userLogin);
    }
  }, [userLogin]);

  return (
    <bases.Base1>
      <div className={"container text-center my-5"}>
        <h1 className="h3 display-5 lead fw-normal mb-3">Создайте аккаунт:</h1>

        <article>
          <loaders.Loader1 isView={userLogin.load} />
          {userLogin.error && (
            <div className="alert alert-danger" role="alert">
              {userLogin.error}
            </div>
          )}
          {userLogin.fail && (
            <div className="alert alert-danger" role="alert">
              {userLogin.fail}
            </div>
          )}
          {userLogin.data && (
            <div className="alert alert-success" role="alert">
              Вы успешно вошли в аккаунт!
            </div>
          )}
        </article>

        <form className={""} onSubmit={sendForm}>
          <div className={"m-1 p-1 input-group"}>
            <label className={"fw-bold p-2"}>Логин:</label>
            <input
              type={"email"}
              placeholder={"admin@gmail.com"}
              className={"form-control w-50"}
              value={form.username}
              onChange={(event) => {
                setForm({ ...form, username: event.target.value });
              }}
            ></input>
          </div>
          <div className={"m-1 p-1 input-group"}>
            <label className={"fw-bold p-2"}>Пароль:</label>
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
          <button
            className={
              userLogin.load
                ? "btn btn-outline-primary w-50 disabled"
                : "btn btn-outline-primary w-50"
            }
            type={"submit"}
          >
            войти в аккаунт
          </button>
        </form>
      </div>
    </bases.Base1>
  );
}
