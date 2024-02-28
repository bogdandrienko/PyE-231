// external
import * as bases from "../../components/bases";
import { useState } from "react";

// я - simple frontend
// Вы - full backend

export default function Page() {
  const [data, setData]: any = useState([]);
  const [form, setForm]: any = useState({ text: "" });
  function addNote(event: any) {
    event.preventDefault();
    if (form.text !== "") {
      setData([
        ...data,
        {
          text: form.text,
          datetime: `${new Date().getHours()} ${new Date().getMinutes()}`,
        },
      ]);
      setForm({ ...form, text: "" });
    } else {
      window.alert("Please enter text");
    }
  }
  function deleteNote(indexArr: number) {
    const tempData = data.filter(
      (value: never, index: number, array: never[]) => index !== indexArr,
    );
    setData([...tempData]);
  }

  function updateNote(indexArr: number) {
    const tempData = [];
    for (let i = 0; i < data.length; i++) {
      if (i == indexArr) {
        const d = data[i];
        d.datetime = `${new Date().getHours()} ${new Date().getMinutes()} updated`;
        tempData.push(d);
      } else {
        tempData.push(data[i]);
      }
    }
    setData([...tempData]);
  }

  return (
    <bases.Base2>
      <h1>Приложение для заметок</h1>
      <form onSubmit={addNote}>
        <input
          type={"text"}
          value={form.text}
          onChange={(event) => {
            setForm({ ...form, text: event.target.value });
          }}
        />
        <button type={"submit"}>добавить</button>
      </form>
      <hr />
      <ul>
        {data &&
          data.length > 0 &&
          data.map((item: any, index: number) => (
            <li key={index}>
              <span
                onClick={() => {
                  updateNote(index);
                }}
              >
                {item.text} ({item.datetime})
              </span>
              <button
                onClick={() => {
                  deleteNote(index);
                }}
              >
                удалить
              </button>
            </li>
          ))}
      </ul>
    </bases.Base2>
  );
}
