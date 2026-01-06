import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import axios from "axios";
import { setLoginMember } from "../src/store/memberSlice";
 

export const useTokenCheck = () => {
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const checkToken = () => {
    const memberId = sessionStorage.getItem("loginMember");
    axios.get(`http://localhost:9999/member.info.get?member=${memberId}`)
      .then((res) => {
        if (res.data.msg === "activeToken") {
          console.log('엑티브토큰');
          dispatch(setLoginMember(res.data.member));
        } else {
          alert('로그인 만료기간이 지났습니다. 다시 로그인해주세요');
          sessionStorage.removeItem('loginMember');
          dispatch(setLoginMember(""));
          navigate("/login");
        }
      })
      .catch((err) => alert(err));
  };

  return checkToken;
};