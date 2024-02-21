import { configureStore, ThunkAction, Action } from '@reduxjs/toolkit';
import * as components from "../components/components";
import {constructorReducer, constructorConstant} from "../components/components";

// C
export const todoCreate = constructorConstant("todoDetail")
// R
export const todoList = constructorConstant("todoList")
export const todoDetail = constructorConstant("todoDetail")
// U
export const todoUpdate = constructorConstant("todoDetail")
// D
export const todoDelete = constructorConstant("todoDetail")

export const store = configureStore({
  reducer: {
    // counter: counterReducer,
      // @ts-ignore
      simpleReduxCounter: components.ReducerSimpleReduxCounter,
      // @ts-ignore
      simpleReduxWeb: components.ReducerSimpleReduxWeb,
      // @ts-ignore
      todoCreate: constructorReducer(todoCreate),
      // @ts-ignore
      todoList: constructorReducer(todoList),
      // @ts-ignore
      todoDetail: constructorReducer(todoDetail),
      // @ts-ignore
      todoUpdate: constructorReducer(todoUpdate),
      // @ts-ignore
      todoDelete: constructorReducer(todoDelete),
  },
});

 export default store;
