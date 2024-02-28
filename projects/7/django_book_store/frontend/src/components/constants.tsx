// external
import { constructorConstant } from "../components/components";

export const isDebug = true; // TODO - найти способ, автоматически
export const host = "http://127.0.0.1:8000";

// book
export const bookList = constructorConstant("bookList");
export const bookCreate = constructorConstant("bookCreate");
export const bookDetail = constructorConstant("bookDetail");
export const bookUpdate = constructorConstant("bookUpdate");
export const bookDelete = constructorConstant("bookDelete");

// user
export const userRegister = constructorConstant("userRegister");
export const userLogin = constructorConstant("userLogin");
export const userDetail = constructorConstant("userDetail");
export const userUpdate = constructorConstant("userUpdate");
