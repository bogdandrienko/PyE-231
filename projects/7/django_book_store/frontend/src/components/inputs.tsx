export function Input1({callbackFunc}:any){ // callback (обратный вызов)
    return <input className={"form-control"} onChange={(event)=> {
        callbackFunc(event.target.value);
    }} />
}