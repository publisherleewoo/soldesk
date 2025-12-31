import { Route, Routes } from "react-router-dom";
import FirstPage from "../pages/FirstPage";
import SecondPage from "../pages/SecondPage";
import ThirdPage from "../pages/ThirdPage";
import FourthPage from "../pages/FourthPage";
import WrapLayout from "../layout/WrapLayout";
import ErrorPage from "../pages/ErrorPage";
import LoginPage from "../pages/LoginPage";
import SignUpPage from "../pages/SignUpPage";
import UserInfoPage from "../pages/UserInfoPage";

const Main = () => {
   return (
      <div>
         <Routes>
            <Route element={<WrapLayout />}>
               <Route path="/" element={<FirstPage />}></Route>
               <Route path="/b" element={<SecondPage />}></Route>
               <Route path="/c" element={<ThirdPage />}></Route>
               <Route path="/d" element={<FourthPage />}></Route>
            </Route>
            <Route path="/login" element={<LoginPage />}></Route>
            <Route path="/signUp" element={<SignUpPage />}></Route>
            <Route path="/userInfo" element={<UserInfoPage />}></Route>
            <Route path="*" element={<ErrorPage />}></Route>
         </Routes>
      </div>
   );
};

export default Main;
