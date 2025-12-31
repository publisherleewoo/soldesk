import { useSelector } from "react-redux";

const Logined = () => {
   const loginMember = useSelector((s) => s.ms.loginMember);
   return (
      <table id="loginForm">
         <tr>
            <td rowSpan={2} align="center" className="imgTd">
               <img
                  src={`http://localhost:9999/member.info.psa.get?file=${loginMember.psa}`}
               />
            </td>
            <td className="idTd">{loginMember.id}</td>
         </tr>
         <tr>
            <td align="right">
               <button>정보확인</button>
               <button>로그아웃</button>
            </td>
         </tr>
      </table>
   );
};

export default Logined;
