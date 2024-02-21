import React, { useEffect, useState } from "react";
import axios from "axios";

export default function Page() {
  // useState - запоминает и следит за переменной(если она изменяется, он перерисовывает все компоненты)
  const [command, setCommand]: any = useState("--(имя команды)");
  const [data, setData]: any = useState(undefined);
  const [data2, setData2]: any = useState(undefined);
  const [data3, setData3]: any = useState(undefined);

  // useEffect - делает действие, если хоть одна зависимость изменилась
  useEffect(() => {
    getData();
  }, []); // dependensies(deps)

  async function getData() {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/data/");
      console.log("data: ", response.data, new Date());
      setData(response.data.success);
    } catch (error) {
      console.error("error getData: ", error, new Date());
    }
  }

  async function sendAnswer(answer_id: number) {
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/api/answer/?command=${command}&answer_id=${answer_id}&question_id=${data.question_id}`,
      );
      console.log("data: ", response.data, new Date());
    } catch (error) {
      console.error("error sendAnswer: ", error, new Date());
    }
  }

  return (
    <div>
      {command}
      <input
        value={command}
        onChange={(event) => {
          setCommand(event.target.value);
        }}
        // двойное связывание
      />
      <hr />
      {
        // @ts-ignore
        data !== undefined && (
          <div>
            <h1>{data.question && data.question}</h1>
            <table>
              <thead>
                <tr>
                  <td></td>
                  <td></td>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>
                    <button
                      onClick={() => {
                        sendAnswer(0);
                      }}
                    >
                      {data.answers[0]}
                    </button>
                  </td>
                  <td>
                    <button
                      onClick={() => {
                        sendAnswer(1);
                      }}
                    >
                      {data.answers[1]}
                    </button>
                  </td>
                </tr>
                <tr>
                  <td>
                    <button
                      onClick={() => {
                        sendAnswer(2);
                      }}
                    >
                      {data.answers[2]}
                    </button>
                  </td>
                  <td>
                    <button
                      onClick={() => {
                        sendAnswer(3);
                      }}
                    >
                      {data.answers[3]}
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        )
      }
    </div>
  );
}
