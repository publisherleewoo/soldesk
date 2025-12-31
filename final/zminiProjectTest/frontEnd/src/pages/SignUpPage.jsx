import { Link } from "react-router-dom";
import "./SignUpPage.css";
import { useRef, useState } from "react";
import axios from "axios";

const SignUpPage = () => {
   const [idValCheck, setIdValCheck] = useState(true); //False로 바꾸기

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

      const idCut = idInput.current;
      const pwdCut = pwdInput.current;
      const pwd2Cut = pwdInput2.current;
      const birthCut = birth_select.current;
      const birt2hCut = birth_select2.current;
      const birth3Cut = birth_select3.current;
      const postCodeCut = postCodeInput.current;
      const postCode2Cut = postCodeInput2.current;
      const postCode3Cut = postCodeInput3.current;
      const fileCut = fileInput.current;

      const nameCut = nameInput.current;
      if (idValCheck === false) {
         alert("아이디 체크 해주세요");
         return false;
      }
      if (pwdCut.value.length < 5) {
         alert("비밀번호가 너무 짧습니다. 5글자 이상으로 해주세요.");
         return false;
      }
      if (pwdCut.value !== pwd2Cut.value) {
         alert("비밀번호가 다릅니다");
         return false;
      }
      
      if (
         idCut.value == "" ||
         pwdCut.value == "" ||
         pwd2Cut.value == "" ||
         nameCut.value == "" ||
         birthCut.value == "" ||
         birt2hCut.value == "" ||
         birth3Cut.value == "" ||
         postCodeCut.value == "" ||
         postCode2Cut.value == "" ||
         postCode3Cut.value == "" ||
         fileCut.value == ""
      ) {
         alert("입력창이 비었습니다");
         return false;
      }

      const hangeulRegex = /^[ㄱ-ㅎㅏ-ㅣ가-힣]+$/;

      if (nameCut.value && !hangeulRegex.test(nameCut.value)) {
         alert("이름은 한글만 입력 가능합니다.");
         nameCut.focus();
         return false;
      }

      const fd = new FormData();
      fd.append("id", idCut.value);
      fd.append("pwd", pwdCut.value);
      fd.append("name", nameInput.current.value);
      fd.append(
         "birthday",
         birthCut.value + "-" + birt2hCut.value + "-" + birth3Cut.value
      );
      fd.append("postCode", postCodeCut.value);
      fd.append("addr", postCode2Cut.value + "∴" + postCode3Cut.value);
      fd.append("files", fileCut.files[0]);
      axios
         .post(`http://localhost:9999/sign.up`, fd, {
            withCredentials: true,
            headers: { "Content-Type": "multupart/form-data" },
         })
         .then((res) => {
            if (res.data.msg === "등록 성공") {
               alert("등록 성공");
               console.log(res.data.msg);
               idCut.value = "";
               pwdCut.value = "";
               pwd2Cut.value = "";
               nameInput.current.value = "";
               birthCut.value = "";
               birt2hCut.value = "";
               birth3Cut.value = "";
               postCodeCut.value = "";
               postCode2Cut.value = "";
               postCode3Cut.value = "";
               fileCut.value = "";
            } else {
               alert(res.data.msg);
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
   // id필수,한글x,최대10자,
   // pw필수,4자이상,숫자하나,최대10자
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
