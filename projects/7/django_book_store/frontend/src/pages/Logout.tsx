// external
import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";

// internal
import * as constants from "../components/constants";
import * as utils from "../components/utils";

export default function Page() {
  // TODO hook ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  const dispatch = useDispatch();
  const navigate = useNavigate();

  // TODO useEffect //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

  useEffect(() => {
    dispatch({ type: constants.userLogin.reset });
    dispatch({ type: constants.userRegister.reset });
    dispatch({ type: constants.userDetail.reset });

    utils.LocalStorage.remove("userLogin.data.access");
    utils.LocalStorage.remove("userLogin.data.refresh");

    navigate("/");
  }, []);

  return <div></div>;
}
