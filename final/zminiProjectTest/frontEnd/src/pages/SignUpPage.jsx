import { Link } from "react-router-dom";
import "./SignUpPage.css";
import { useRef, useState } from "react";
import axios from "axios";

const SignUpPage = () => {
   const [idValCheck, setIdValCheck] = useState(false);
   const useInfo = useRef({
      id: "",
      pwd: "",
      pwd2: "",
      name: "",
      birthday1: "",
      birthday2: "",
      birthday3: "",
      postCode: "",
      addr2: "",
      addr3: "",
      files: "",
   });

   const idInput = useRef();
   const pwdInput = useRef();
   const pwdInput2 = useRef();
   const nameInput = useRef();
   const birth_select = useRef();
   const birth_select2 = useRef();
   const birth_select3 = useRef();
   const postCodeInput = useRef();
   const postCodeInput2 = useRef();
   const postCodeInput3 = useRef();
   const fileInput = useRef();

   const sameIdCheck = () => {
      axios
         .get(`http://localhost:9999/id.check?u_id=${idInput.current.value}`)
         .then((r) => {
            alert(r.data.msg);
            if (r.data.msg === "이미 존재하는 아이디입니다") {
               return setIdValCheck(false);
            }
            setIdValCheck(true);
         })
         .catch((err) => alert(err));
   };

   const handleJoin = (e) => {
      e.preventDefault();
      if (idValCheck === false) {
         alert("아이디 체크 해주세요");
         return false;
      }
      if (pwdInput.current.value.length < 5) {
         alert("비밀번호가 너무 짧습니다");
         return false;
      }
      if (pwdInput.current.value !== pwdInput2.current.value) {
         alert("비밀번호가 다릅니다");
         return false;
      }

      useInfo.current.id = idInput.current.value;
      useInfo.current.pwd = pwdInput.current.value;
      useInfo.current.pwd2 = pwdInput2.current.value;
      useInfo.current.name = nameInput.current.value;
      useInfo.current.birthday1 = birth_select.current.value;
      useInfo.current.birthday2 = birth_select2.current.value;
      useInfo.current.birthday3 = birth_select3.current.value;
      useInfo.current.postCode = postCodeInput.current.value;
      useInfo.current.addr2 = postCodeInput2.current.value;
      useInfo.current.addr3 = postCodeInput3.current.value;
      useInfo.current.files = fileInput.current.files[0];

      const fd = new FormData();
      fd.append("id", useInfo.current.id);
      fd.append("pwd", useInfo.current.pwd);
      fd.append("name", useInfo.current.name);
      fd.append(
         "birthday",
         useInfo.current.birthday1 +
            "-" +
            useInfo.current.birthday2 +
            "-" +
            useInfo.current.birthday3
      );
      fd.append("postCode", useInfo.current.postCode);
      fd.append("addr", useInfo.current.addr2 + useInfo.current.addr3);
      fd.append("files", useInfo.current.files);
      axios
         .post(`http://localhost:9999/sign.up`, fd, {
            withCredentials: true,
            headers: { "Content-Type": "multupart/form-data" },
         })
         .then((res) => {
            if (res.data.msg === "등록 성공") {
               alert("등록 성공");
               console.log(res.data.msg);
               idInput.current.value = "";
               pwdInput.current.value = "";
               pwdInput2.current.value = "";
               nameInput.current.value = "";
               birth_select.current.value = "";
               birth_select2.current.value = "";
               birth_select3.current.value = "";
               postCodeInput.current.value = "";
               postCodeInput2.current.value = "";
               postCodeInput3.current.value = "";
               fileInput.current.value = "";
            }
         })
         .catch((err) => alert(err));
   };

   const nowDate = new Date();
   const currentYear = nowDate.getFullYear();
   const years = [];
   for (let i = currentYear; i >= 1920; i--) {
      years.push(i);
   }

   const months = Array.from({ length: 12 }, (_, i) => i + 1);
   const days = Array.from({ length: 31 }, (_, i) => i + 1);
   const showAdressSearchPopup = () => {
      new window.daum.Postcode({
         oncomplete: function (data) {
            const { zonecode, address } = data;
            postCodeInput.current.value = zonecode;
            postCodeInput2.current.value = address;
         },
      }).open();
   };

   return (
      <div id="JoinWrap">
         <h3>Join</h3>

         <div className="row">
            <label>ID</label>
            <input
               type="text"
               className="id_input"
               ref={idInput}
               placeholder="아이디 입력"
            />
            <button type="button" className="check_btn" onClick={sameIdCheck}>
               중복체크
            </button>
         </div>

         <div className="row">
            <label>PW</label>
            <input type="password" ref={pwdInput} placeholder="비밀번호 입력" />
         </div>
         <div className="row">
            <label>PW확인</label>
            <input
               type="password"
               ref={pwdInput2}
               placeholder="비밀번호 입력"
            />
         </div>
         <div className="row">
            <label>이름</label>
            <input ref={nameInput} />
         </div>

         <div className="row">
            <label>Birth</label>

            <select ref={birth_select} className="birth_select">
               <option value="">년</option>
               {years.map((y) => (
                  <option key={y} value={y}>
                     {y}
                  </option>
               ))}
            </select>
            <select ref={birth_select2} className="birth_select">
               <option value="">월</option>
               {months.map((m) => (
                  <option key={m} value={m}>
                     {m}
                  </option>
               ))}
            </select>
            <select ref={birth_select3} className="birth_select">
               <option value="">일</option>
               {days.map((d) => (
                  <option key={d} value={d}>
                     {d}
                  </option>
               ))}
            </select>
         </div>

         <div className="row">
            <label>Addr</label>
            <input
               type="text"
               placeholder="우편 번호"
               onClick={showAdressSearchPopup}
               ref={postCodeInput}
            />
            <label>&nbsp;</label>
            <input type="text" ref={postCodeInput2} placeholder="주소" />
            <label>&nbsp;</label>

            <input type="text" ref={postCodeInput3} placeholder="상세주소" />
         </div>

         <div className="row">
            <label>Photo</label>
            <input ref={fileInput} type="file" />
         </div>

         <div className="btn_area">
            <button type="button" className="submit_btn" onClick={handleJoin}>
               가입하기
            </button>
            <Link to={-1} className="back_btn">
               뒤로가기
            </Link>
         </div>
      </div>
   );
};

export default SignUpPage;

//id pw 생년월일 주소 프사  유효성검사(id중복체크) 입력받고 가입
