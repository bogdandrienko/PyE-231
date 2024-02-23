import * as footers from "./footers";
import * as navbars from "./navbars";

export function Base1({ children }: any) {
  return (
    <main className={"text-bg-dark text-white custom-main m-0 p-0"}>
      <navbars.Navbar1 />
      <div>{children}</div>
      <footers.Footer1 />
    </main>
  );
}

export function Base2({ children }: any) {
  return <div>{children}</div>;
}
