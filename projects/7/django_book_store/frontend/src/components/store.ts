import { configureStore } from "@reduxjs/toolkit";
import * as components from "./components";
import * as constants from "./constants";
export const store = configureStore({
  reducer: {
    // @ts-ignore
    simpleReduxCounter: components.ReducerSimpleReduxCounter,
    // @ts-ignore
    simpleReduxWeb: components.ReducerSimpleReduxWeb,
    // @ts-ignore
    bookCreate: components.constructorReducer(constants.bookCreate),
    // @ts-ignore
    bookList: components.constructorReducer(constants.bookList),
    // @ts-ignore
    bookDetail: components.constructorReducer(constants.bookDetail),
    // @ts-ignore
    bookUpdate: components.constructorReducer(constants.bookUpdate),
    // @ts-ignore
    bookDelete: components.constructorReducer(constants.bookDelete),
  },
});
export default store;
