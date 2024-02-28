import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";

export function SimpleCounter() {
  const [counter, setCounter] = useState(666);
  return (
    <div>
      <div>
        <h2>SimpleCounter: {counter}</h2>
        <button
          onClick={() => {
            setCounter(counter + 1);
          }}
        >
          increase
        </button>
        <button
          onClick={() => {
            setCounter(counter - 1);
          }}
        >
          decrease
        </button>
      </div>
    </div>
  );
}

export function ReducerSimpleReduxCounter(
  state = { data: 666 },
  action: { type: string; payload: any },
) {
  switch (action.type) {
    case "increase":
      return { data: action.payload + 1 };
    case "decrease":
      return { data: action.payload - 1 };
    default:
      return state;
  }
}

export function SimpleReduxCounter() {
  const dispatch = useDispatch();
  const simpleReduxCounter = useSelector(
    (state: any) => state.simpleReduxCounter,
  );
  return (
    <div>
      <h1>
        SimpleReduxCounter:{" "}
        {simpleReduxCounter.data ? simpleReduxCounter.data : "нет данных"}
      </h1>
      <button
        onClick={() => {
          dispatch({ type: "increase", payload: simpleReduxCounter.data });
        }}
      >
        increase
      </button>
      <button
        onClick={() => {
          dispatch({ type: "decrease", payload: simpleReduxCounter.data });
        }}
      >
        decrease
      </button>
    </div>
  );
}

export const loadWeb = "loadWeb";
export const successWeb = "successWeb";
export const failWeb = "failWeb";
export const errorWeb = "errorWeb";
export const error2Web2 = "errorWeb";
export const resetWeb = "resetWeb";

export function ReducerSimpleReduxWeb(
  state = {},
  action: { type: string; payload: any },
) {
  switch (action.type) {
    case loadWeb:
      return { load: true, data: undefined, error: undefined };
    case successWeb:
      return { load: false, data: action.payload, error: undefined };
    case failWeb:
      return { load: false, data: undefined, error: action.payload };
    case errorWeb:
      return { load: false, data: undefined, error: action.payload };
    case resetWeb:
      return { load: undefined, data: undefined, error: undefined };
    default:
      return state;
  }
}

export function SimpleReduxWeb() {
  const dispatch = useDispatch();
  const simpleReduxWebPage = useSelector((state: any) => state.simpleReduxWeb);

  async function getData() {
    try {
      // начинает загрузка
      dispatch({ type: loadWeb });

      // загрузка
      const response = await axios.get(
        "https://jsonplaceholder.typicode.com/todos",
      );

      if (response.status === 200 || response.status === 201) {
        // данные успешно получены
        dispatch({ type: successWeb, payload: response.data });
      } else {
        // ошибка backend
        dispatch({ type: errorWeb, payload: response.statusText });
      }
    } catch (error: any) {
      // ошибка frontend
      dispatch({ type: failWeb, payload: error.toString() });
    }
  }

  return (
    <div>
      <button onClick={getData}>getData</button>
      <div className={"container container-fluid text-center"}>
        {simpleReduxWebPage.load === true && (
          <div className={"small fw-light"}>Идёт загрузка</div>
        )}
        {simpleReduxWebPage.fail && (
          <div className={"small fw-light"}>Обратитесь к администатору</div>
        )}
        {simpleReduxWebPage.error && (
          <div className={"small fw-light"}>{simpleReduxWebPage.error}</div>
        )}
        <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
          {!simpleReduxWebPage.data ? (
            "данных пока нет"
          ) : (
            <ul>
              {simpleReduxWebPage.data.map((item: any, index: number) => (
                <li key={item.id}>{item.title}</li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </div>
  );
}

export function constructorConstant(prefix: string) {
  return {
    load: `load_${prefix}`,
    success: `success_${prefix}`,
    fail: `fail_${prefix}`,
    error: `error_${prefix}`,
    reset: `reset_${prefix}`,
  };
}

export function constructorReducer(constant: any) {
  return function (state = {}, action: { type: string; payload: any }) {
    switch (action.type) {
      case constant.load:
        return { load: true };
      case constant.success:
        return { load: false, data: action.payload };
      case constant.fail:
        return { load: false, fail: action.payload };
      case constant.error:
        return { load: false, error: action.payload };
      case constant.reset:
        return { load: false };
      default:
        return state;
    }
  };
}

export async function constructorWebAction(
  dispatch: any,
  constant: any,
  url: string,
  method: string = "GET",
  data: any = {},
  timeout: number = 5000,
  isExtra: boolean = false,
) {
  try {
    dispatch({ type: constant.load });
    const config: any = {
      url: url,
      method: method,
      timeout: timeout,
      data: data,
      // "headers": 3000,
      // "auth": 3000,
      // "headers": 3000,
    };
    const response = await axios(config);
    // setTimeout(()=> {
    if (response.status === 200 || response.status === 201) {
      if (isExtra) {
        dispatch({ type: constant.success, payload: response.data });
      } else {
        dispatch({ type: constant.success, payload: response.data.success });
      }
    } else {
      dispatch({ type: constant.error, payload: response.statusText });
    }
    // }, 1000)
  } catch (error: any) {
    console.error(`constructorWebAction: ${url} ${method}`, error);
    dispatch({ type: constant.fail, payload: "Свяжитесь с админстратором" });
  }
}
