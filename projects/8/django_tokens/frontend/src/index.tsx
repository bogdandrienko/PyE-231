import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import axios from "axios";

const container = document.getElementById("root")!;
const root = createRoot(container);

interface Result {
  total_summ: number;
  result: boolean;
}

function HomePage() {
  const [form, setForm] = useState({
    summ: 1000000,
    date_planning: 36,
  });

  const [result, setResult] = useState<Result>({
    total_summ: 0,
    result: false,
  });

  useEffect(() => {
    console.log("change form: ", form);
  }, [form]);

  function Native(name: string) {
    console.log("hi!", name);
  }
  Native("Roman");

  const native = (name: string) => {
    console.log("hi!", name);
  };
  native("Roman");

  async function SendData(event: any) {
    event.preventDefault();
    try {
      // const config = { Authorization: { Token: "auth" } };
      const response = await axios.post(
        `http://127.0.0.1:8000/api/user/credit/check/`,
        { ...form },
      );
      setResult({
        total_summ: response.data.success.total_summ,
        result: response.data.success.result,
      });
      console.log("response SendData: ", response);
    } catch (error) {
      console.error("error SendData: ", error);
    }
  }

  return (
    <div>
      <form onSubmit={SendData}>
        <div>
          Введите желаемую сумму кредитования(тенге):
          <input
            type={"number"}
            className={""}
            min={100000}
            value={form.summ}
            onChange={(event) => {
              setForm({
                ...form, // spread, unpacking **kwargs
                summ: parseInt(event.target.value, 10),
              });
            }}
          />
        </div>
        <hr />
        <div>
          Введите срок возврата кредита(месяцы):
          <select
            className={""}
            value={form.date_planning}
            onChange={(event) => {
              setForm({
                ...form,
                date_planning: parseInt(event.target.value, 10),
              });
            }}
          >
            <option value={1}>1</option>
            <option value={3}>3</option>
            <option value={6}>6</option>
            <option value={12}>12</option>
            <option value={24}>24</option>
            <option value={36}>36</option>
          </select>
        </div>
        <hr />
        <input type={"submit"}></input>
      </form>

      <hr />
      <br />
      <hr />
      <div>
        Результат:{" "}
        <h1>
          {result == undefined
            ? "???(одобрено/не одобрено)"
            : `${result.total_summ} ${result.result ? "одобрено" : "не одобрено"}`}
        </h1>
      </div>

      <button
        onClick={async () => {
          const params = { order: "asc" };
          // @ts-ignore
          await axios.get(`http://127.0.0.1:8000/api/users?order=asc&page=6`);
        }}
      >
        get
      </button>
    </div>
  );
}

function Login() {
  const [token, setToken] = useState("");

  async function Login() {
    try {
      const response = await axios.post(`http://127.0.0.1:8000/api/token/`, {
        username: "admin",
        password: "admin",
      });
      setToken(response.data.access);
      console.log("success Login: ", response);
    } catch (error) {
      console.error("error Login: ", error);
    }
  }

  async function GetData() {
    try {
      const config = {
        url: `http://127.0.0.1:8000/api/users/`,
        method: "GET",
        timeout: 5000,
        timeoutErrorMessage: "timeout error",
        headers: {
          // @ts-ignore
          Authorization: `Bogdan ${token}`,
        },
        data: {},
      };
      const response = await axios(config);
      console.log("success GetData: ", response);
    } catch (error) {
      console.error("error GetData: ", error);
    }
  }

  return (
    <div>
      <h1>{token}</h1>
      <button onClick={Login}>Login</button>
      <button onClick={GetData}>GetData</button>
    </div>
  );
}

root.render(
  // <React.StrictMode>
  <Login />,
  // </React.StrictMode>
);
