import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import axios from "axios";
import { setLoginMember } from "../src/store/memberSlice";







export const useTokenCheck = () => {
  const navi = useNavigate();
  const dispatch = useDispatch();

  const checkToken = (memberId) => {
    
  
      axios.get(`http://localhost:9999/member.info.get?member=${memberId}`)
        .then((res) => {
          if (res.data.msg === "activeToken") {
            console.log('엑티브토큰');
            dispatch(setLoginMember(res.data.member));
            return true
          } else {
            alert('로그인 만료기간이 지났습니다. 다시 로그인해주세요');
            console.log("로그인낫");
            sessionStorage.removeItem('loginMember');
            dispatch(setLoginMember(""));
            navi("/login");
            return false
          }
        })
        .catch((err) => alert(err));
   
  };

  return checkToken;
};