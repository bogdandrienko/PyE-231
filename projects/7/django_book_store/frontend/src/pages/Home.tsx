// external
import * as bases from "../components/bases";

export default function Page() {
  return (
    <bases.Base1>
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
        <img
          src="https://getbootstrap.com/docs/5.3/examples/heroes/bootstrap-themes.png"
          className="d-block mx-lg-auto img-fluid"
          alt="Bootstrap Themes"
          width="400"
          height="300"
          loading="lazy"
        />
        <img
          src="/static/img/winter.jpg"
          className="d-block mx-lg-auto img-fluid"
          alt="Bootstrap Themes"
          width="400"
          height="300"
          loading="lazy"
        />
      </div>
    </bases.Base1>
  );
}
