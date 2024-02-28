import * as bases from "../../components/bases";
import * as buttons from "../../components/buttons";
import * as inputs from "../../components/inputs";
import * as components from "../../components/components";
import {SimpleReduxCounter} from "../../components/components";
import {useSelector} from "react-redux";


export default function Page() {
    const simpleReduxCounter = useSelector(
    (state: any) => state.simpleReduxCounter
  );

    function getName(name: string) {
        console.log("Я ВЫЗВАН В РОДИТЕЛЕ NAME: ", name)
    }

  return (
    <bases.Base1>

      <hr/>
        <div className={""}>

      111111
          <buttons.Button1 bodyClass={"btn btn-md btn-danger"}>
            я текст на кнопке
          </buttons.Button1>

          <buttons.Button1 bodyClass={"btn btn-md btn-primary"}>
            я текст на кнопке 2
          </buttons.Button1>

          <buttons.Button1 bodyClass={"btn btn-md btn-success"}>
            я текст на кнопке 3
          </buttons.Button1>

            <inputs.Input1 callbackFunc={getName}/>
            <inputs.Input1 callbackFunc={getName}/>
            <inputs.Input1 callbackFunc={getName}/>

            <components.SimpleCounter />
            <components.SimpleCounter />
            <components.SimpleCounter />

            <components.SimpleReduxCounter />
            <components.SimpleReduxCounter />

        </div>
      <hr/>


      <div className="bg-dark text-secondary px-4 py-5 text-center">
        <div className="py-5">
          <h1 className="display-5 fw-bold text-white">Dark color hero</h1>
          <div className="col-lg-6 mx-auto">
            <p className="fs-5 mb-4">
              Quickly design and customize responsive mobile-first sites with
              Bootstrap, the world’s most popular front-end open source toolkit,
              featuring Sass variables and mixins, responsive grid system,
              extensive prebuilt components, and powerful JavaScript plugins.
            </p>
            <div className="d-grid gap-2 d-sm-flex justify-content-sm-center">
              <button
                type="button"
                className="btn btn-outline-info btn-lg px-4 me-sm-3 fw-bold"
              >
                Custom button
              </button>
              <button
                type="button"
                className="btn btn-outline-light btn-lg px-4"
              >
                Secondary
              </button>
            </div>
          </div>
        </div>
      </div>
        {simpleReduxCounter.data ? simpleReduxCounter.data : "нет данных"}
    </bases.Base1>
  );
}
