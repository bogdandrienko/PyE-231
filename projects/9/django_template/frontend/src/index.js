import React from 'react';
import ReactDOM from 'react-dom/client';
import axios from "axios";

function App(){

    async function getData(){
        try{
            const response = await axios.get("http://127.0.0.1:8000/api/contacts/")
            console.log("response: ", response)
        } catch(e){
            console.error(e)
        }
    }

    async function sendData(){
        try{
            const data = {"username": "User", "password": "Querty123!"}
            const response = await axios.post("http://127.0.0.1:8000/api/contacts/", {...data})
            console.log("response: ", response)
        } catch(e){
            console.error(e)
        }
    }

    return <div>
        <button onClick={getData}>getData</button>
        <button onClick={sendData}>sendData</button>
    </div>
}

ReactDOM.createRoot(document.getElementById('root')).render(
  // <React.StrictMode>
    <App />
  // </React.StrictMode>
);
