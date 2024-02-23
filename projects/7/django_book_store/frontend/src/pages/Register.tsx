import * as bases from "../components/bases";
import { useEffect, useState } from "react";

export default function Page() {
  const [form, setForm] = useState({
    username: "",
    password: "",
    password2: "",
    sex: true,
    age: 18,
  });

  function sendForm() {
    if (form.password === form.password2) {
      // отправка формы
    }
  }

  useEffect(() => {
    console.log("form: ", form);
  }, [form]);

  return (
    <bases.Base1>
      <div className={"container text-center"}>
        <h1 className="h3 display-5 lead fw-normal mb-3">Создайте аккаунт:</h1>
        <form className={""}>
          <div className={"m-1 p-1 input-group"}>
            <label className={"fw-bold p-2"}>
              Введите почту для регистрации:
            </label>
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
            <label className={"fw-bold p-2"}>Введите пароль:</label>
            <input
              type={"password"}
              placeholder={"Qwerty!123"}
              className={"form-control w-50"}
              value={form.password}
              onChange={(event) => {
                setForm({ ...form, password: event.target.value });
              }}
            ></input>
          </div>
          {form.password !== form.password2 && (
            <div className="alert alert-danger" role="alert">
              пароли не совпадают!
            </div>
          )}
          <div className={"m-1 p-1 input-group"}>
            <label className={"fw-bold p-2"}>Повторите пароль:</label>
            <input
              type={"password"}
              placeholder={"Qwerty!123"}
              className={"form-control w-50"}
              value={form.password2}
              onChange={(event) => {
                setForm({ ...form, password2: event.target.value });
              }}
            ></input>
          </div>
          <button
            className={
              form.password !== form.password2
                ? "btn btn-warning disabled"
                : "btn btn-warning"
            }
          >
            создать аккаунт
          </button>
        </form>
      </div>

      <div className="bg-dark text-secondary px-4 py-5 text-center w-50">
        <main className="form-signin w-100 m-auto">
          <form>
            <img
              className="mb-4"
              src="https://getbootstrap.com/docs/5.3/assets/brand/bootstrap-logo.svg"
              alt=""
              width="72"
              height="57"
            />
            <h1 className="h3 mb-3 fw-normal">Please sign in</h1>

            <div className="form-floating">
              <input
                type="email"
                className="form-control"
                id="floatingInput"
                placeholder="name@example.com"
              />
              <label htmlFor="floatingInput">Email address</label>
            </div>
            <div className="form-floating">
              <input
                type="password"
                className="form-control"
                id="floatingPassword"
                placeholder="Password"
              />
              <label htmlFor="floatingPassword">Password</label>
            </div>

            <div className="form-check text-start my-3">
              <input
                className="form-check-input"
                type="checkbox"
                value="remember-me"
                id="flexCheckDefault"
              />
              <label className="form-check-label" htmlFor="flexCheckDefault">
                Remember me
              </label>
            </div>
            <button className="btn btn-primary w-100 py-2" type="submit">
              Sign in
            </button>
            <p className="mt-5 mb-3 text-body-secondary">© 2017–2023</p>
          </form>
        </main>
      </div>
    </bases.Base1>
  );
}
